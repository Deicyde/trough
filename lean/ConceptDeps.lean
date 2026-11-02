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
(its constructor's type) do too. Walking through an unlisted declaration
follows its type, and also its body when it is data; walking for a proof
follows types and bodies alike.

This is a plain file, not a `module`: a plain importer sees each module's
private part, which is where Mathlib's theorem proofs live under the module
system.

    TROUGH_CONCEPTS=concepts.txt TROUGH_MODULES=modules.txt TROUGH_OUT=out.json \
      lake env lean ConceptDeps.lean
-/

open Lean Meta

namespace TroughDump

/-- What a constant's statement uses, and what its proof uses. -/
def directUses (env : Environment) (info : ConstantInfo) : Array Name × Array Name :=
  let type := info.type.getUsedConstants
  match info with
  | .thmInfo val => (type, val.value.getUsedConstants)
  | .defnInfo val => (type ++ val.value.getUsedConstants, #[])
  | .opaqueInfo val => (type ++ val.value.getUsedConstants, #[])
  | .inductInfo val =>
    let fields := val.ctors.foldl (init := type) fun acc ctor =>
      match env.find? ctor with
      | some c => acc ++ c.type.getUsedConstants
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
  uses : Option (Array Name × Array Name) := none
deriving Inhabited

/-- For every unlisted constant reachable from `starts`, the listed constants it reaches
without passing another listed one: through statements only, and through statements and
proofs. Bit `i` stands for the `i`th listed declaration. The walk keeps its own stack, since
Mathlib's dependency chains run deeper than Lean's call stack. A constant met again while it
is still being walked contributes what is known of it so far. -/
def fronts (env : Environment) (index : Std.HashMap Name Nat) (starts : Array Name) :
    Std.HashMap Name Nat × Std.HashMap Name Nat := Id.run do
  let mut stmt : Std.HashMap Name Nat := {}
  let mut all : Std.HashMap Name Nat := {}
  let mut active : Std.HashSet Name := {}
  for start in starts do
    if index.contains start || stmt.contains start then continue
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
            let uses := directUses env info
            stack := stack.set! (stack.size - 1) { frame with uses := some uses }
            active := active.insert frame.name
            for u in uses.1 ++ uses.2 do
              unless index.contains u || stmt.contains u || active.contains u do
                stack := stack.push { name := u }
      | some (statementUses, proofUses) =>
        stack := stack.pop
        active := active.erase frame.name
        let mut s := 0
        let mut a := 0
        for u in statementUses do
          match index[u]? with
          | some i =>
            s := s ||| (1 <<< i)
            a := a ||| (1 <<< i)
          | none =>
            s := s ||| stmt.getD u 0
            a := a ||| all.getD u 0
        for u in proofUses do
          match index[u]? with
          | some i => a := a ||| (1 <<< i)
          | none => a := a ||| all.getD u 0
        stmt := stmt.insert frame.name s
        all := all.insert frame.name a
  return (stmt, all)

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
  let mut missing : Array Json := #[]
  let mut theorems := 0
  let mut withProof := 0
  for name in listed do
    match env.find? name with
    | none => missing := missing.push (Json.str name.toString)
    | some info =>
      let (statementUses, proofUses) := directUses env info
      starts := starts ++ (statementUses ++ proofUses).filter (!index.contains ·)
      if info matches .thmInfo _ then
        theorems := theorems + 1
        unless proofUses.isEmpty do withProof := withProof + 1
  if theorems > 0 && withProof == 0 then
    throwError "none of the {theorems} listed theorems has a readable proof; private module data is missing"
  let (stmtFront, allFront) := fronts env index starts
  let mut concepts : Array (String × Json) := #[]
  for i in [0:listed.size] do
    let name := listed[i]!
    let some info := env.find? name | continue
    let (statementUses, proofUses) := directUses env info
    let s := statementUses.foldl (init := 0) fun acc u =>
      acc ||| (match index[u]? with | some j => 1 <<< j | none => stmtFront.getD u 0)
    let p := proofUses.foldl (init := 0) fun acc u =>
      acc ||| (match index[u]? with | some j => 1 <<< j | none => allFront.getD u 0)
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
