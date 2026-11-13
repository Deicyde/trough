import Cslib

/-!
# Module dependencies for trough's CSLib map

Runs in a CSLib checkout after `lake build`, below an import of `Cslib`, which imports every module of the
library. Writes `$TROUGH_OUT`: for each `Cslib` module, the other `Cslib` modules whose declarations its
statements use, and those that only its proofs use.

A module's statements are the types of its declarations, the values of its definitions and the fields or
constructors of its structures and inductive types. Its proofs are the values of its theorems and instances,
and everything that the declarations Lean generates for it (matchers, auxiliary proofs) or that its private
declarations use. A constant belongs to the module that declares it, so the walk stops at the first constant
of another module: every module has its own record.

Of the names in `$TROUGH_NAMES`, one per line, the declarations read from the source, it lists under `private`
each one Lean has only as a private declaration of a `Cslib` module (in a `module` file, a declaration outside a
`public section` and not marked `public` is private), and under `missing` each one it has neither as a public nor
as a private declaration there: the map shows only what Lean has as public under the name the source gives.

This is a plain file, not a `module`, so it sees each module's private part, where theorem proofs live under
the module system; without it the run stops rather than give partial data.

    TROUGH_NAMES=names.txt TROUGH_OUT=deps.json TROUGH_CSLIB_REV=<commit> lake env lean CslibDeps.lean
-/

open Lean Meta

namespace TroughCslib

/-- `e` without the tactic scripts of its `autoParam`s. -/
partial def withoutTactics (e : Expr) : Expr :=
  e.replace fun t =>
    if t.isAppOfArity ``autoParam 2 then some (withoutTactics t.appFn!.appArg!) else none

def usedConstants (e : Expr) : Array Name :=
  (withoutTactics e).getUsedConstants

/-- What a constant's statement uses, and what its proof uses. -/
def uses (env : Environment) (info : ConstantInfo) : Array Name × Array Name :=
  let type := usedConstants info.type
  match info with
  | .thmInfo val => (type, usedConstants val.value)
  | .defnInfo val =>
    if Meta.isInstanceCore env info.name then (type, usedConstants val.value)
    else (type ++ usedConstants val.value, #[])
  | .opaqueInfo val => (type ++ usedConstants val.value, #[])
  | .inductInfo val =>
    let fields := val.ctors.foldl (init := type) fun acc ctor =>
      match env.find? ctor with
      | some c => acc ++ usedConstants c.type
      | none => acc
    (fields, #[])
  | .ctorInfo _ | .recInfo _ | .quotInfo _ => (#[], #[])
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
  let rev := (← IO.getEnv "TROUGH_CSLIB_REV").getD ""
  let moduleNames := env.header.moduleNames
  let moduleOf (name : Name) : Option Name := do
    let idx ← env.getModuleIdxFor? name
    let module := moduleNames[idx.toNat]!
    if (`Cslib).isPrefixOf module then some module else none
  let mut records : Array (String × Json) := #[]
  -- The names private declarations of Cslib modules are written with.
  let mut privateNames : Std.HashSet Name := {}
  let mut theorems := 0
  let mut withProof := 0
  let mut statementEdges := 0
  let mut proofEdges := 0
  for i in [0:moduleNames.size] do
    let module := moduleNames[i]!
    unless (`Cslib).isPrefixOf module do continue
    let mut statement : Std.HashSet Name := {}
    let mut proof : Std.HashSet Name := {}
    for name in env.header.moduleData[i]!.constNames do
      if let some user := privateToUserName? name then privateNames := privateNames.insert user
      let some info := env.find? name | continue
      let (stated, proved) := uses env info
      if info matches .thmInfo _ then
        theorems := theorems + 1
        unless proved.isEmpty do withProof := withProof + 1
      -- What Lean generates for a declaration, or a private helper, serves the module's proofs.
      let helper := name.isInternalDetail || isPrivateName name
      for used in stated do
        if let some other := moduleOf used then
          if other != module then
            if helper then proof := proof.insert other else statement := statement.insert other
      for used in proved do
        if let some other := moduleOf used then
          if other != module then proof := proof.insert other
    let proofOnly := proof.fold (init := ({} : Std.HashSet Name)) fun acc other =>
      if statement.contains other then acc else acc.insert other
    statementEdges := statementEdges + statement.size
    proofEdges := proofEdges + proofOnly.size
    records := records.push (module.toString, Json.mkObj [
      ("statement", sorted statement),
      ("proof", sorted proofOnly)])
  -- Without a module's private data its theorems import as axioms.
  if theorems == 0 || withProof == 0 then
    throwError "{theorems} theorems, {withProof} with a readable proof: private module data is missing"
  let requested := ((← IO.FS.readFile namesPath).splitOn "\n").filter (· ≠ "")
  let isPublic (name : Name) : Bool := env.contains name && !isPrivateName name && (moduleOf name).isSome
  let privateOnly := requested.filter fun text =>
    let name := parseName text
    !isPublic name && privateNames.contains name
  let missing := requested.filter fun text =>
    let name := parseName text
    !isPublic name && !privateNames.contains name
  let out := Json.mkObj [
    ("schema", "trough-cslib-deps/v1"),
    ("rev", rev),
    ("lean_githash", Json.str Lean.githash),
    ("modules", Json.mkObj ((records.qsort (·.1 < ·.1)).toList)),
    ("private", Json.arr (privateOnly.toArray.map Json.str)),
    ("missing", Json.arr (missing.toArray.map Json.str)),
    ("stats", Json.mkObj [
      ("modules", toJson records.size),
      ("theorems", toJson theorems),
      ("theorems_with_proof", toJson withProof),
      ("statement_edges", toJson statementEdges),
      ("proof_edges", toJson proofEdges),
      ("requested", toJson requested.length),
      ("private", toJson privateOnly.length),
      ("missing", toJson missing.length)])]
  IO.FS.writeFile outPath (out.pretty 100 ++ "\n")
  IO.println s!"{records.size} modules, {theorems} theorems ({withProof} with a proof), {statementEdges} statement and {proofEdges} proof edges before reduction; of {requested.length} names read from the source, {privateOnly.length} private, {missing.length} missing"

end TroughCslib

set_option maxHeartbeats 0 in
#eval TroughCslib.run
