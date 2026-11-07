import Lean

/-!
# Declarations and dependencies for trough's Tau Ceti map

Runs in a Tau Ceti checkout, after the Tau Ceti data workflow puts an import of
every `TauCeti` module above this line: Tau Ceti's root module imports nothing.

Reads the declaration names in `$TROUGH_NAMES`, one per line, and writes
`$TROUGH_OUT`. For each listed declaration that resolves it records the module,
kind, line, docstring and signature, the nearest listed declarations that its
statement and its proof use, and whether its proof reaches `sorryAx`. A listed
name that does not resolve is listed under `missing`: the map has only what Tau
Ceti has at this commit. Listed theorems whose proofs cannot be read stop the run
rather than give partial data.

The walk goes through Tau Ceti's declarations only: nothing outside Tau Ceti uses
a Tau Ceti declaration, so Mathlib and core are where it stops. A statement
reaches listed declarations through the statements of unlisted ones, where an
unlisted instance's statement is its type alone, as in `lean/ConceptDeps.lean`.
A proof reaches listed declarations through both the statements and the proofs
of unlisted ones: Tau Ceti lists a small part of itself, so the whole chain of
helpers between two listed results is followed. A proof that reaches `sorryAx`
through unlisted declarations is not complete; one that reaches a listed
declaration stops there, and that declaration has its own record.

This is a plain file, not a `module`, so it sees each module's private part,
where theorem proofs live under the module system.

    TROUGH_NAMES=names.txt TROUGH_OUT=out.json lake env lean TauCetiDeps.lean
-/

open Lean Meta

namespace TroughTauCeti

/-- `e` without the tactic scripts of its `autoParam`s. -/
partial def withoutTactics (e : Expr) : Expr :=
  e.replace fun t =>
    if t.isAppOfArity ``autoParam 2 then some (withoutTactics t.appFn!.appArg!) else none

def usedConstants (e : Expr) : Array Name :=
  (withoutTactics e).getUsedConstants

/-- What a constant's statement uses, and what its proof uses. A definition's body and a
structure's fields count as its statement. -/
def directUses (env : Environment) (info : ConstantInfo) : Array Name × Array Name :=
  let type := usedConstants info.type
  match info with
  | .thmInfo val => (type, usedConstants val.value)
  | .defnInfo val => (type ++ usedConstants val.value, #[])
  | .opaqueInfo val => (type ++ usedConstants val.value, #[])
  | .inductInfo val =>
    let fields := val.ctors.foldl (init := type) fun acc ctor =>
      match env.find? ctor with
      | some c => acc ++ usedConstants c.type
      | none => acc
    (fields, #[])
  | _ => (type, #[])

def kindOf (env : Environment) (info : ConstantInfo) : String :=
  match info with
  | .thmInfo _ => "theorem"
  | .defnInfo val =>
    if Meta.isInstanceCore env info.name then "instance"
    else if val.hints matches .abbrev then "abbrev"
    else "def"
  | .axiomInfo _ => "axiom"
  | .opaqueInfo _ => "opaque"
  | .inductInfo _ =>
    if isClass env info.name then "class"
    else if isStructure env info.name then "structure"
    else "inductive"
  | .ctorInfo _ => "constructor"
  | .recInfo _ => "recursor"
  | .quotInfo _ => "quot"

/-- A constant waiting on the walk's stack, with its uses once it is expanded. -/
structure Frame where
  name : Name
  uses : Option (Array Name) := none
deriving Inhabited

/-- For every unlisted Tau Ceti constant reachable from `starts`, the listed constants it
reaches without passing another listed one, through what `uses` says each constant uses. Bit
`i` stands for the `i`th entry of `index`. The walk keeps its own stack, since dependency
chains run deeper than Lean's call stack; a constant met again while it is still being walked
contributes what is known of it so far. -/
def fronts (env : Environment) (index : Std.HashMap Name Nat) (inTauCeti : Name → Bool)
    (uses : ConstantInfo → Array Name) (starts : Array Name) : Std.HashMap Name Nat := Id.run do
  let mut front : Std.HashMap Name Nat := {}
  let mut active : Std.HashSet Name := {}
  for start in starts do
    if index.contains start || front.contains start || !inTauCeti start then continue
    let mut stack : Array Frame := #[{ name := start }]
    while !stack.isEmpty do
      let frame := stack.back!
      match frame.uses with
      | none =>
        if front.contains frame.name || active.contains frame.name then
          stack := stack.pop
        else
          match env.find? frame.name with
          | none => stack := stack.pop
          | some info =>
            let used := uses info
            stack := stack.set! (stack.size - 1) { frame with uses := some used }
            active := active.insert frame.name
            for u in used do
              unless index.contains u || front.contains u || active.contains u || !inTauCeti u do
                stack := stack.push { name := u }
      | some used =>
        stack := stack.pop
        active := active.erase frame.name
        let mut s := 0
        for u in used do
          s := s ||| (match index[u]? with | some i => 1 <<< i | none => front.getD u 0)
        front := front.insert frame.name s
  return front

def names (listed : Array Name) (bits exclude : Nat) : Json := Id.run do
  let mut out : Array Json := #[]
  for i in [0:listed.size] do
    if bits.testBit i && !exclude.testBit i then
      out := out.push (Json.str listed[i]!.toString)
  return Json.arr out

def readNames (path : String) : IO (Array Name) := do
  let text ← IO.FS.readFile path
  return ((text.splitOn "\n").filter (· ≠ "")).toArray.map String.toName

def optionalJson (value : Option String) : Json :=
  match value with
  | some text => Json.str text
  | none => Json.null

def run : MetaM Unit := do
  let env ← getEnv
  let some namesPath ← IO.getEnv "TROUGH_NAMES" | throwError "TROUGH_NAMES is not set"
  let some outPath ← IO.getEnv "TROUGH_OUT" | throwError "TROUGH_OUT is not set"
  let rev := (← IO.getEnv "TROUGH_TAUCETI_REV").getD ""
  let started ← IO.monoMsNow
  let requested ← readNames namesPath
  let moduleNames := env.header.moduleNames
  let inTauCeti (name : Name) : Bool :=
    match env.getModuleIdxFor? name with
    | some idx => (`TauCeti).isPrefixOf moduleNames[idx.toNat]!
    | none => false
  let listed := requested.filter (env.contains ·)
  let missing := requested.filter (!env.contains ·)
  -- `sorryAx` gets the bit after the listed declarations', so a proof's front says whether it
  -- reaches one. It is never walked, being core's.
  let sorryBit := 1 <<< listed.size
  let mut index : Std.HashMap Name Nat := {}
  for i in [0:listed.size] do
    index := index.insert listed[i]! i
  index := index.insert ``sorryAx listed.size
  let statementUses (info : ConstantInfo) : Array Name :=
    if Meta.isInstanceCore env info.name then usedConstants info.type else (directUses env info).1
  let allUses (info : ConstantInfo) : Array Name :=
    let (statement, proof) := directUses env info
    statement ++ proof
  let mut statementStarts : Array Name := #[]
  let mut proofStarts : Array Name := #[]
  let mut theorems := 0
  let mut withProof := 0
  for name in listed do
    let some info := env.find? name | continue
    let (statement, proof) := directUses env info
    statementStarts := statementStarts ++ statement
    proofStarts := proofStarts ++ proof
    if info matches .thmInfo _ then
      theorems := theorems + 1
      unless proof.isEmpty do withProof := withProof + 1
  -- Without a module's private data its theorems import as axioms.
  if theorems == 0 || withProof == 0 then
    throwError "{theorems} listed theorems, {withProof} with a readable proof: private module data is missing"
  let statementFront := fronts env index inTauCeti statementUses statementStarts
  let proofFront := fronts env index inTauCeti allUses (statementStarts ++ proofStarts)
  let mut records : Array (String × Json) := #[]
  let mut incomplete := 0
  for i in [0:listed.size] do
    let name := listed[i]!
    let some info := env.find? name | continue
    let (statement, proof) := directUses env info
    let reach (front : Std.HashMap Name Nat) (acc : Nat) (u : Name) : Nat :=
      acc ||| (match index[u]? with | some j => 1 <<< j | none => front.getD u 0)
    let s := statement.foldl (reach statementFront) 0
    let p := (statement ++ proof).foldl (reach proofFront) 0
    let self := 1 <<< i
    let usesSorry := (s ||| p) &&& sorryBit != 0
    if usesSorry then incomplete := incomplete + 1
    let module := (env.getModuleIdxFor? name).map fun idx => moduleNames[idx.toNat]!.toString
    let line := (← findDeclarationRanges? name).map (·.range.pos.line)
    let mut signature : Option String := none
    try
      signature := some ((← PrettyPrinter.ppSignature name).fmt.pretty 100)
    catch _ =>
      pure ()
    records := records.push (name.toString, Json.mkObj [
      ("module", optionalJson module),
      ("kind", Json.str (kindOf env info)),
      ("line", match line with | some l => toJson l | none => Json.null),
      ("signature", optionalJson signature),
      ("doc", optionalJson (← findDocString? env name)),
      ("sorry", toJson usesSorry),
      ("statement", names listed s self),
      ("proof", names listed p (s ||| self))])
  let elapsed := (← IO.monoMsNow) - started
  let out := Json.mkObj [
    ("schema", "trough-tauceti-deps/v1"),
    ("tauceti_rev", rev),
    ("lean_githash", Json.str Lean.githash),
    ("declarations", Json.mkObj records.toList),
    ("missing", Json.arr (missing.map (Json.str ·.toString))),
    ("stats", Json.mkObj [
      ("requested", toJson requested.size),
      ("listed", toJson listed.size),
      ("theorems", toJson theorems),
      ("theorems_with_proof", toJson withProof),
      ("reaching_sorry", toJson incomplete),
      ("walked_statements", toJson statementFront.size),
      ("walked_proofs", toJson proofFront.size)])]
  IO.FS.writeFile outPath (out.pretty 100 ++ "\n")
  IO.println s!"{listed.size} of {requested.size} names resolve; {statementFront.size} and {proofFront.size} constants walked in {elapsed} ms"

end TroughTauCeti

set_option maxHeartbeats 0 in
#eval TroughTauCeti.run
