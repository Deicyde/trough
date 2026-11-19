import Lean

/-!
# Which modules each module of Physlib uses, for trough's Physlib map

Runs in a physlib checkout, after the Physlib data workflow puts an import of every module of
Physlib, PhyslibAlpha and QuantumInfo above this line.

Writes `$TROUGH_OUT`. For each module of the three libraries it records the other modules of the
three whose declarations its own declarations use: in a statement, or in a proof. A declaration's
statement is its type; a definition's value, an opaque constant's and a structure's or inductive
type's constructors count as its statement too, and a theorem's value is its proof. Every constant
a module adds counts, the ones Lean generates included, since the auxiliary definitions made for a
proof are where much of its use is; a constant Lean marks as an internal detail counts as proof.
When several modules' data hold a name, the one the using module imports declares it there.
Of the names in `$TROUGH_NAMES`, one per line, the declarations read from the source, it lists
under `missing` each one that is not a public declaration of a module of the three libraries:
the map shows only what Lean has under the name the source gives.

This is a plain file, not a `module`, so it sees each module's private part, where theorem proofs
live under the module system. A run that finds no theorem with a proof stops rather than write
edges without proofs.

    TROUGH_NAMES=names.txt TROUGH_OUT=deps.json lake env lean PhyslibDeps.lean
-/

open Lean Meta

namespace TroughPhyslib

def libraries : Array Name := #[`Physlib, `PhyslibAlpha, `QuantumInfo]

/-- `e` without the tactic scripts of its `autoParam`s. -/
partial def withoutTactics (e : Expr) : Expr :=
  e.replace fun t =>
    if t.isAppOfArity ``autoParam 2 then some (withoutTactics t.appFn!.appArg!) else none

def usedConstants (e : Expr) : Array Name :=
  (withoutTactics e).getUsedConstants

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

/-- A name as the source writes it, with `«»` around a component that is not an identifier. -/
def parseName (text : String) : Name :=
  (Syntax.decodeNameLit ("`" ++ text)).getD text.toName

def sorted (names : Std.HashSet Name) : Json :=
  Json.arr ((names.toArray.map toString).qsort (· < ·) |>.map Json.str)

def run : MetaM Unit := do
  let env ← getEnv
  let some namesPath ← IO.getEnv "TROUGH_NAMES" | throwError "TROUGH_NAMES is not set"
  let some outPath ← IO.getEnv "TROUGH_OUT" | throwError "TROUGH_OUT is not set"
  let rev := (← IO.getEnv "TROUGH_PHYSLIB_REV").getD ""
  let started ← IO.monoMsNow
  let moduleNames := env.header.moduleNames
  let moduleOf (name : Name) : Option Name :=
    (env.getModuleIdxFor? name).map fun idx => moduleNames[idx.toNat]!
  let inLibraries (module : Name) : Bool := libraries.any (·.isPrefixOf module)
  let mut indexOf : Std.HashMap Name Nat := {}
  for i in [0:moduleNames.size] do
    indexOf := indexOf.insert moduleNames[i]! i
  -- The modules of the three whose data hold each name: a name can be in several modules' data, and the
  -- environment then gives it to one of them, which need not be one the module using it imports.
  let mut declaredIn : Std.HashMap Name (Array Name) := {}
  for i in [0:moduleNames.size] do
    let module := moduleNames[i]!
    unless inLibraries module do continue
    for name in env.header.moduleData[i]!.constNames do
      declaredIn := declaredIn.insert name ((declaredIn.getD name #[]).push module)
  -- The modules of the three each of them imports, directly or through others of them.
  let mut importsOf : Std.HashMap Name (Std.HashSet Name) := {}
  for i in [0:moduleNames.size] do
    unless inLibraries moduleNames[i]! do continue
    let mut seen : Std.HashSet Name := {}
    let mut todo := #[i]
    while !todo.isEmpty do
      let j := todo.back!
      todo := todo.pop
      for imp in env.header.moduleData[j]!.imports do
        if inLibraries imp.module && !seen.contains imp.module then
          seen := seen.insert imp.module
          if let some k := indexOf[imp.module]? then todo := todo.push k
    importsOf := importsOf.insert moduleNames[i]! seen
  -- A name a module uses belongs to the module itself, when its data hold the name, or else to a module it imports
  -- whose data do; as lean/library/LibraryDeps.lean gives it.
  let ownerOf (module : Name) (used : Name) : Option Name :=
    let owners := declaredIn.getD used #[]
    if owners.contains module then some module else owners.find? (importsOf.getD module {}).contains
  let mut reassigned := 0
  let mut reassignedExamples : Array Name := #[]
  let mut statement : Std.HashMap Name (Std.HashSet Name) := {}
  let mut proof : Std.HashMap Name (Std.HashSet Name) := {}
  let mut constants := 0
  let mut theorems := 0
  let mut withProof := 0
  for module in moduleNames do
    if inLibraries module then
      statement := statement.insert module {}
      proof := proof.insert module {}
  for (name, info) in env.constants.map₁.toList do
    let some module := moduleOf name | continue
    unless inLibraries module do continue
    constants := constants + 1
    let (s, p) := directUses env info
    if info matches .thmInfo _ then
      theorems := theorems + 1
      unless p.isEmpty do withProof := withProof + 1
    let internal := name.isInternalDetail
    for (used, isStatement) in s.map (·, !internal) ++ p.map (·, false) do
      let owner := ownerOf module used
      if owner != (moduleOf used).filter inLibraries then
        reassigned := reassigned + 1
        if reassignedExamples.size < 5 then reassignedExamples := reassignedExamples.push used
      let some target := owner | continue
      if target != module then
        if isStatement then
          statement := statement.modify module (·.insert target)
        else
          proof := proof.modify module (·.insert target)
  -- Without a module's private data its theorems import as axioms.
  if theorems == 0 || withProof == 0 then
    throwError "{theorems} theorems, {withProof} with a readable proof: private module data is missing"
  let requested := ((← IO.FS.readFile namesPath).splitOn "\n").filter (· ≠ "")
  let missing := requested.filter fun text =>
    let name := parseName text
    !(env.contains name && !isPrivateName name && (moduleOf name).any inLibraries)
  let modules := (statement.toArray.map (·.1)).qsort (·.toString < ·.toString)
  let records := modules.map fun module =>
    (module.toString, Json.mkObj [
      ("statement", sorted (statement.getD module {})),
      ("proof", sorted (proof.getD module {}))])
  let out := Json.mkObj [
    ("schema", "trough-physlib-deps/v1"),
    ("rev", rev),
    ("lean_githash", Json.str Lean.githash),
    ("modules", Json.mkObj records.toList),
    ("missing", Json.arr (missing.toArray.map Json.str)),
    ("stats", Json.mkObj [
      ("modules", toJson modules.size),
      ("constants", toJson constants),
      ("theorems", toJson theorems),
      ("theorems_with_proof", toJson withProof),
      ("requested", toJson requested.length),
      ("missing", toJson missing.length)])]
  IO.FS.writeFile outPath (out.pretty 100 ++ "\n")
  let finished ← IO.monoMsNow
  IO.println s!"{reassigned} uses of a name the environment gives to a module the user does not import, such as {reassignedExamples}"
  IO.println s!"{modules.size} modules, {constants} constants ({withProof} of {theorems} theorems with a proof); {missing.length} of {requested.length} names missing; {finished - started} ms"

end TroughPhyslib

set_option maxHeartbeats 0 in
#eval TroughPhyslib.run
