import Lean

/-!
# Every Tau Ceti declaration's docstring opening, for choosing trough's named results

Runs in a Tau Ceti checkout, after the Tau Ceti data workflow puts an import of every `TauCeti`
module above this line. Writes `$TROUGH_OUT`, one JSON object per line, for each public
declaration in a Tau Ceti module: its name `n`, kind `k`, module `m`, and the first 300
characters of its docstring `d`, or null. Internal details, private names, constructors,
recursors, matchers, projections and auxiliary recursors are left out.
`tools/select_tauceti.py` reads it.

    TROUGH_OUT=survey.jsonl lake env lean TauCetiSurvey.lean
-/

open Lean Meta

namespace TroughTauCetiSurvey

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

def run : MetaM Unit := do
  let env ← getEnv
  let some outPath ← IO.getEnv "TROUGH_OUT" | throwError "TROUGH_OUT is not set"
  let started ← IO.monoMsNow
  let moduleNames := env.header.moduleNames
  let handle ← IO.FS.Handle.mk outPath .write
  let mut rows := 0
  let mut documented := 0
  for (name, info) in env.constants.map₁.toList do
    let some idx := env.getModuleIdxFor? name | continue
    let module := moduleNames[idx.toNat]!
    unless (`TauCeti).isPrefixOf module do continue
    if name.isInternalDetail || isPrivateName name then continue
    if info matches .ctorInfo _ | .recInfo _ | .quotInfo _ then continue
    if env.isProjectionFn name || isAuxRecursor env name || isNoConfusion env name
        || Meta.isMatcherCore env name then continue
    let doc ← findDocString? env name
    if doc.isSome then documented := documented + 1
    rows := rows + 1
    handle.putStrLn (Json.mkObj [
      ("n", Json.str name.toString),
      ("k", Json.str (kindOf env info)),
      ("m", Json.str module.toString),
      ("d", match doc with | some text => Json.str (String.mk (text.toList.take 300)) | none => Json.null)
    ]).compress
  let elapsed := (← IO.monoMsNow) - started
  IO.println s!"{rows} Tau Ceti declarations, {documented} documented, in {elapsed} ms"

end TroughTauCetiSurvey

set_option maxHeartbeats 0 in
#eval TroughTauCetiSurvey.run
