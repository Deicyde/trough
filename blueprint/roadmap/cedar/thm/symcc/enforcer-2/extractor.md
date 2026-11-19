---
catalog: module
lean: Cedar.Thm.repair_wf, Cedar.Thm.repair_env_wf_same, Cedar.Thm.extract?_env_wf_same, Cedar.Thm.not_mem_footprintUIDs_implies_empty_ancs, Cedar.Thm.mem_footprintUIDs_implies_eq_ancs, Cedar.Thm.mem_footprintUIDs_mem_footprints, Cedar.Thm.mem_mem_footprints_footprintUIDs, Cedar.Thm.εnv_same_on_footprints, Cedar.Thm.sym_entities_entityUIDs_include_enums, Cedar.Thm.extract?_implies_enum_complete
statement: formalized
proof: formalized
---

# Enforcer/Extractor

`Cedar.Thm.SymCC.Enforcer.Extractor`, in [Cedar/Thm/SymCC/Enforcer/Extractor.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean).

> This file proves properties of the counterexample extraction functions
> in `Cedar/SymCC/Extractor.lean`.
> -

`Cedar.Thm.repair_wf` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L156))

```lean
theorem repair_wf {xs : List Expr} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormed →
  (∀ x ∈ xs, εnv.entities.ValidRefsFor x) →
  I.WellFormed εnv.entities →
  (I.repair (footprints xs εnv) εnv).WellFormed εnv.entities
```

`Cedar.Thm.repair_env_wf_same` (theorem, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L198))

```lean
theorem repair_env_wf_same {xs : List Expr} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormed →
  (∀ x ∈ xs, εnv.entities.ValidRefsFor x) →
  I.WellFormed εnv.entities →
  (I.repair (footprints xs εnv) εnv).WellFormed εnv.entities ∧
  ∃ env : Env,
    env ∼ εnv.interpret (I.repair (footprints xs εnv) εnv) ∧
    env.WellFormed ∧
    ∀ x ∈ xs, env.entities.ValidRefsFor x
```

`Cedar.Thm.extract?_env_wf_same` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L212))

```lean
theorem extract?_env_wf_same {xs : List Expr} {εnv : SymEnv} {I : Interpretation} :
  εnv.WellFormed →
  (∀ x ∈ xs, εnv.entities.ValidRefsFor x) →
  I.WellFormed εnv.entities →
  ∃ env : Env,
    εnv.extract? xs I = .some env ∧
    env ∼ εnv.interpret (I.repair (footprints xs εnv) εnv) ∧
    env.WellFormed ∧
    ∀ x ∈ xs, env.entities.ValidRefsFor x
```

`Cedar.Thm.not_mem_footprintUIDs_implies_empty_ancs` (theorem, [line 276](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L276))

```lean
theorem not_mem_footprintUIDs_implies_empty_ancs {uid : EntityUID} {ety : EntityType} {f : UUF} {δ : SymEntityData} {xs : List Expr} {εnv : SymEnv} {I : Interpretation}
  (hwε : εnv.WellFormed)
  (hI  : I.WellFormed εnv.entities)
  (hδ  : Map.find? εnv.entities uid.ty = some δ)
  (hf  : δ.ancestors.find? ety = some (UnaryFunction.uuf f))
  (hft : ¬uid ∈ Interpretation.repair.footprintUIDs (footprints xs εnv) I) :
  app ((UnaryFunction.uuf f).interpret (I.repair (footprints xs εnv) εnv)) (Term.entity uid) =
  Term.set Set.empty (TermType.entity ety)
```

`Cedar.Thm.mem_footprintUIDs_implies_eq_ancs` (theorem, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L308))

```lean
theorem mem_footprintUIDs_implies_eq_ancs {uid : EntityUID} {ety : EntityType} {f : UUF} {δ : SymEntityData} {xs : List Expr} {εnv : SymEnv} {I : Interpretation}
  (hwε : εnv.WellFormed)
  (hI  : I.WellFormed εnv.entities)
  (hδ  : Map.find? εnv.entities uid.ty = some δ)
  (hf  : δ.ancestors.find? ety = some (UnaryFunction.uuf f))
  (hft : uid ∈ Interpretation.repair.footprintUIDs (footprints xs εnv) I) :
  app ((UnaryFunction.uuf f).interpret (I.repair (footprints xs εnv) εnv)) (Term.entity uid) =
  app ((UnaryFunction.uuf f).interpret I) (Term.entity uid)
```

`Cedar.Thm.mem_footprintUIDs_mem_footprints` (theorem, [line 326](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L326))

```lean
theorem mem_footprintUIDs_mem_footprints {uid : EntityUID} {xs : List Expr} {εnv : SymEnv} {I : Interpretation}
  (hwε : εnv.WellFormed)
  (hvr : ∀ x ∈ xs, εnv.entities.ValidRefsFor x)
  (hI  : I.WellFormed εnv.entities)
  (hin : uid ∈ Interpretation.repair.footprintUIDs (footprints xs εnv) I) :
  ∃ t ∈ footprints xs εnv, t.interpret I = Term.some (Term.entity uid)
```

`Cedar.Thm.mem_mem_footprints_footprintUIDs` (theorem, [line 349](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L349))

```lean
theorem mem_mem_footprints_footprintUIDs {t : Term} {uid : EntityUID} {xs : List Expr} {εnv : SymEnv} {I : Interpretation}
  (hin : t ∈ footprints xs εnv)
  (ht  : t.interpret I = Term.some (Term.entity uid)) :
  uid ∈ Interpretation.repair.footprintUIDs (footprints xs εnv) I
```

`Cedar.Thm.εnv_same_on_footprints` (theorem, [line 460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L460))

```lean
theorem εnv_same_on_footprints {xs : List Expr} {εnv : SymEnv} {I : Interpretation}
  (hsε : εnv.StronglyWellFormedForAll xs)
  (hI  : I.WellFormed εnv.entities) :
  εnv.SameOn (footprints xs εnv) I (I.repair (footprints xs εnv) εnv)
```

`Cedar.Thm.sym_entities_entityUIDs_include_enums` (theorem, [line 480](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L480))

```lean
theorem sym_entities_entityUIDs_include_enums
  {εnv : SymEnv} {uid : EntityUID}
  {δ : SymEntityData} {eids : Set String}
  (I : Interpretation)
  (hfind_uid_ty : Map.find? εnv.entities uid.ty = some δ)
  (heids : δ.members = some eids)
  (heid : uid.eid ∈ eids) :
  uid ∈ (SymEnv.interpret I εnv).entities.entityUIDs
```

`Cedar.Thm.extract?_implies_enum_complete` (theorem, [line 505](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean#L505))

> `SymEnv.extract?` always produces a concrete `Env` that satisfies `Env.EnumCompleteFor`.

```lean
theorem extract?_implies_enum_complete
  {env : Env} {εnv : SymEnv} {I : Interpretation} {exprs : List Expr}
  (hext : env = εnv.extract? exprs I) :
  Env.EnumCompleteFor env εnv
```

## Depends on

- [Extracting strongly well-formed counterexamples to verification queries (SymCC/Extractor)](../../../symcc/part-01/extractor.md)
- [Footprint](footprint.md)

## Proof depends on

- [Concretizer](../concretizer.md)
- [Enforcer/Util](util.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Extractor.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Extractor.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Extractor.json)
