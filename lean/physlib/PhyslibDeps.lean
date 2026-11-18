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
    for used in s do
      let some target := moduleOf used | continue
      if target != module && inLibraries target then
        if internal then
          proof := proof.modify module (·.insert target)
        else
          statement := statement.modify module (·.insert target)
    for used in p do
      let some target := moduleOf used | continue
      if target != module && inLibraries target then
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
  IO.println s!"{modules.size} modules, {constants} constants ({withProof} of {theorems} theorems with a proof); {missing.length} of {requested.length} names missing; {finished - started} ms"

end TroughPhyslib

set_option maxHeartbeats 0 in
#eval TroughPhyslib.run
