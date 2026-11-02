import Mathlib
import Archive
import Counterexamples

/-!
# Concept dependencies for trough's Mathlib map

Reads the declaration names in `$TROUGH_CONCEPTS` and the module names in
`$TROUGH_MODULES`, one per line, and writes `$TROUGH_OUT`. For each listed
declaration it records the module, kind, line, docstring and signature, and the
nearest listed declarations that its statement and its proof use, reached
through declarations that are not listed. For each listed module it records the
module docstring and the documented declarations, in source order.

A definition's body counts as part of its statement, and a structure's fields
(its constructor's type) do too. A statement reaches listed declarations
through the statements of unlisted ones. A proof reaches what the statements of
the declarations it uses reach, and the proofs of unlisted declarations from
its own module count as part of it; proofs elsewhere do not, since following
them reaches most of the library. The walk leaves out tactic scripts and does
not go through tactic machinery (see `withoutTactics` and `isTactic`).

This is a plain file, not a `module`: a plain importer sees each module's
private part, which is where Mathlib's theorem proofs live under the module
system.

    TROUGH_CONCEPTS=concepts.txt TROUGH_MODULES=modules.txt TROUGH_OUT=out.json \
      lake env lean ConceptDeps.lean
-/

open Lean Meta

namespace TroughDump

/-- `e` without the tactic scripts of its `autoParam`s. A structure field with a `by ...`
default carries that script as `Lean.Syntax` in its type, and the script's constants
(`Array`, `List`, `Lean.Name`, ...) are not part of the mathematics. -/
partial def withoutTactics (e : Expr) : Expr :=
  e.replace fun t =>
    if t.isAppOfArity ``autoParam 2 then some (withoutTactics t.appFn!.appArg!) else none

/-- The constants an expression uses, its tactic scripts left out. -/
def usedConstants (e : Expr) : Array Name :=
  (withoutTactics e).getUsedConstants

/-- Constants of tactic machinery: the walk does not go through them. Their certificates
(`omega`'s linear combinations, `ring`'s normal forms) would otherwise make a proof
depend on `List` or `Array`. -/
def isTactic (name : Name) : Bool :=
  [`Lean, `Mathlib.Tactic, `Mathlib.Meta, `Aesop, `Qq, `Batteries.Tactic, `Std.Tactic, `Linarith,
    `Polyrith].any (·.isPrefixOf name)

/-- What a constant's statement uses, and what its proof uses. -/
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

/-- The declarations `name`'s proof uses, the proofs of unlisted declarations from `name`'s
own module counted as part of it. -/
def proofReach (env : Environment) (index : Std.HashMap Name Nat) (name : Name) (uses : Array Name) :
    Array Name := Id.run do
  let home := (env.getModuleIdxFor? name).map (·.toNat)
  let mut seen : Std.HashSet Name := {}
  let mut stack := uses
  while !stack.isEmpty do
    let u := stack.back!
    stack := stack.pop
    if seen.contains u || isTactic u then continue
    seen := seen.insert u
    if index.contains u || (env.getModuleIdxFor? u).map (·.toNat) != home then continue
    if let some info := env.find? u then
      stack := stack ++ (directUses env info).2
  return seen.toArray

/-- A constant waiting on the walk's stack, with its statement's uses once it is expanded. -/
structure Frame where
  name : Name
  uses : Option (Array Name) := none
deriving Inhabited

/-- For every unlisted constant whose statement is reachable from `starts`, the listed
constants its statement reaches without passing another listed one. Bit `i` stands for the
`i`th listed declaration. The walk keeps its own stack, since Mathlib's dependency chains run
deeper than Lean's call stack. A constant met again while it is still being walked
contributes what is known of it so far. -/
def fronts (env : Environment) (index : Std.HashMap Name Nat) (starts : Array Name) :
    Std.HashMap Name Nat := Id.run do
  let mut stmt : Std.HashMap Name Nat := {}
  let mut active : Std.HashSet Name := {}
  for start in starts do
    if index.contains start || stmt.contains start || isTactic start then continue
    let mut stack : Array Frame := #[{ name := start }]
    while !stack.isEmpty do
      let frame := stack.back!
      match frame.uses with
      | none =>
        if stmt.contains frame.name || active.contains frame.name then
          stack := stack.pop
        else
          match env.find? frame.name with
          | none => stack := stack.pop
          | some info =>
            let uses := (directUses env info).1
            stack := stack.set! (stack.size - 1) { frame with uses := some uses }
            active := active.insert frame.name
            for u in uses do
              unless index.contains u || stmt.contains u || active.contains u || isTactic u do
                stack := stack.push { name := u }
      | some uses =>
        stack := stack.pop
        active := active.erase frame.name
        let mut s := 0
        for u in uses do
          s := s ||| (match index[u]? with | some i => 1 <<< i | none => stmt.getD u 0)
        stmt := stmt.insert frame.name s
  return stmt

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
  let some conceptsPath ← IO.getEnv "TROUGH_CONCEPTS" | throwError "TROUGH_CONCEPTS is not set"
  let some modulesPath ← IO.getEnv "TROUGH_MODULES" | throwError "TROUGH_MODULES is not set"
  let some outPath ← IO.getEnv "TROUGH_OUT" | throwError "TROUGH_OUT is not set"
  let rev := (← IO.getEnv "TROUGH_MATHLIB_REV").getD ""
  let started ← IO.monoMsNow
  let listed ← readNames conceptsPath
  let mut index : Std.HashMap Name Nat := {}
  for i in [0:listed.size] do
    index := index.insert listed[i]! i
  -- `moduleNames` builds a fresh array on every call; take it once.
  let moduleNames := env.header.moduleNames
  let mut starts : Array Name := #[]
  let mut proofs : Std.HashMap Name (Array Name) := {}
  let mut missing : Array Json := #[]
  let mut theorems := 0
  let mut withProof := 0
  for name in listed do
    match env.find? name with
    | none => missing := missing.push (Json.str name.toString)
    | some info =>
      let (statementUses, proofUses) := directUses env info
      let reached := proofReach env index name proofUses
      proofs := proofs.insert name reached
      starts := starts ++ (statementUses ++ reached).filter (!index.contains ·)
      if info matches .thmInfo _ then
        theorems := theorems + 1
        unless proofUses.isEmpty do withProof := withProof + 1
  if theorems > 0 && withProof == 0 then
    throwError "none of the {theorems} listed theorems has a readable proof; private module data is missing"
  let stmtFront := fronts env index starts
  let mut concepts : Array (String × Json) := #[]
  for i in [0:listed.size] do
    let name := listed[i]!
    let some info := env.find? name | continue
    let front (acc : Nat) (u : Name) : Nat :=
      acc ||| (match index[u]? with | some j => 1 <<< j | none => stmtFront.getD u 0)
    let s := (directUses env info).1.foldl front 0
    let p := (proofs.getD name #[]).foldl front 0
    let self := 1 <<< i
    let module := (env.getModuleIdxFor? name).map fun idx => moduleNames[idx.toNat]!.toString
    let doc ← findDocString? env name
    let line := (← findDeclarationRanges? name).map (·.range.pos.line)
    let mut signature : Option String := none
    try
      signature := some ((← PrettyPrinter.ppSignature name).fmt.pretty 100)
    catch _ =>
      pure ()
    concepts := concepts.push (name.toString, Json.mkObj [
      ("module", optionalJson module),
      ("kind", Json.str (kindOf env info)),
      ("line", match line with | some l => toJson l | none => Json.null),
      ("doc", optionalJson doc),
      ("signature", optionalJson signature),
      ("statement", names listed s self),
      ("proof", names listed p (s ||| self))])
  let mut modules : Array (String × Json) := #[]
  for module in ← readNames modulesPath do
    match env.getModuleIdx? module with
    | none => modules := modules.push (module.toString, Json.mkObj [("found", false)])
    | some idx =>
      let docs := (getModuleDoc? env module).getD #[]
      let doc := if docs.isEmpty then none else some ("\n\n".intercalate (docs.toList.map (·.doc)))
      let mut documented : Array (Nat × Name) := #[]
      for constant in env.header.moduleData[idx.toNat]!.constNames do
        if isPrivateName constant || constant.isInternalDetail then continue
        let some info := env.find? constant | continue
        if info matches .ctorInfo _ | .recInfo _ | .quotInfo _ then continue
        if env.isProjectionFn constant || isAuxRecursor env constant || isNoConfusion env constant
            || Meta.isMatcherCore env constant then continue
        unless (← findDocString? env constant).isSome do continue
        let line := ((← findDeclarationRanges? constant).map (·.range.pos.line)).getD 0
        documented := documented.push (line, constant)
      let ordered := documented.qsort (fun a b => a.1 < b.1 || (a.1 == b.1 && a.2.toString < b.2.toString))
      modules := modules.push (module.toString, Json.mkObj [
        ("found", true),
        ("doc", optionalJson doc),
        ("decls", Json.arr (ordered.map fun entry => Json.str entry.2.toString))])
  let elapsed := (← IO.monoMsNow) - started
  let out := Json.mkObj [
    ("schema", "trough-concept-deps/v1"),
    ("mathlib_rev", rev),
    ("concepts", Json.mkObj concepts.toList),
    ("missing", Json.arr missing),
    ("modules", Json.mkObj modules.toList),
    ("stats", Json.mkObj [
      ("listed", toJson listed.size),
      ("theorems", toJson theorems),
      ("theorems_with_proof", toJson withProof),
      ("walked", toJson stmtFront.size),
      ("milliseconds", toJson elapsed)])]
  IO.FS.writeFile outPath (out.pretty 100 ++ "\n")
  IO.println s!"{listed.size} listed, {missing.size} missing, {stmtFront.size} constants walked in {elapsed} ms"

end TroughDump

set_option maxHeartbeats 0 in
#eval TroughDump.run
