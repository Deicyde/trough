---
catalog: module
lean: Cedar.Thm.try_decide_residual₂_is_bool, Cedar.Thm.tags_if_partial_tags, Cedar.Thm.entity_tag_well_typed, Cedar.Thm.partial_eval_well_typed_app₂_values_hasTag, Cedar.Thm.partial_eval_well_typed_app₂_values_getTag, Cedar.Thm.partial_eval_well_typed_app₂_values_mem, Cedar.Thm.partial_eval_well_typed_app₂_values, Cedar.Thm.partial_eval_well_typed_app₂_nonvalues, Cedar.Thm.partial_eval_well_typed_app₂
statement: formalized
proof: formalized
---

# WellTyped/Binary

`Cedar.Thm.TPE.WellTyped.Binary`, in [Cedar/Thm/TPE/WellTyped/Binary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean).

`Cedar.Thm.try_decide_residual₂_is_bool` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L35))

> The reductions only ever decide a boolean.

```lean
theorem try_decide_residual₂_is_bool
  {env : TypeEnv} {op₂ : BinaryOp} {r₁ r₂ : Residual} {v : Value}
  (hdec : TPE.tryDecideResidual₂ env op₂ r₁ r₂ = .some v) :
  ∃ b : Bool, v = .prim (.bool b)
```

`Cedar.Thm.tags_if_partial_tags` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L45))

```lean
theorem tags_if_partial_tags
  {env : TypeEnv} {req : Request} {es : Entities} {pes : PartialEntities}
  {uid : EntityUID} {tags : Map Tag Value}
  (h_wf : InstanceOfWellFormedEnvironment req es env)
  (h_eref : EntitiesRefine es pes)
  (h_tags : PartialEntities.tags pes uid = some tags) :
  ∃ (edata : EntityData),
    edata.tags = tags ∧
    InstanceOfSchemaEntry uid edata env
```

`Cedar.Thm.entity_tag_well_typed` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L69))

```lean
theorem entity_tag_well_typed
  {env : TypeEnv} {req : Request} {es : Entities} {pes : PartialEntities}
  {uid : EntityUID} {ety : EntityType}
  {tags : Map Tag Value} {v : Value} {ty : CedarType} :
  InstanceOfWellFormedEnvironment req es env →
  EntitiesRefine es pes →
  InstanceOfEntityType uid ety env →
  PartialEntities.tags pes uid = some tags →
  v ∈ tags.values →
  env.ets.tags? ety = some (some ty) →
  InstanceOfType env v ty.liftBoolTypes
```

`Cedar.Thm.partial_eval_well_typed_app₂_values_hasTag` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L110))

```lean
theorem partial_eval_well_typed_app₂_values_hasTag :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  (TPE.evaluate env expr1 preq pes).asValue = some (Value.prim (Prim.entityUID id₁)) →
  (TPE.evaluate env expr2 preq pes).asValue = some (Value.prim (Prim.string id₂)) →
  PEWellTyped env (Residual.binaryApp BinaryOp.hasTag expr1 expr2 ty)
    (someOrSelf ((TPE.hasTag id1 id2 pes).bind fun a => some (Value.prim (Prim.bool a))) ty
    (Residual.binaryApp BinaryOp.hasTag (TPE.evaluate env expr1 preq pes) (TPE.evaluate env expr2 preq pes) ty)) req preq es pes
```

`Cedar.Thm.partial_eval_well_typed_app₂_values_getTag` (theorem, [line 181](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L181))

```lean
theorem partial_eval_well_typed_app₂_values_getTag :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  (TPE.evaluate env expr1 preq pes).asValue = some (Value.prim (Prim.entityUID id₁)) →
  (TPE.evaluate env expr2 preq pes).asValue = some (Value.prim (Prim.string id₂)) →
  PEWellTyped env (Residual.binaryApp BinaryOp.getTag expr1 expr2 ty) (TPE.getTag id₁ id₂ pes ty) req preq es pes
```

`Cedar.Thm.partial_eval_well_typed_app₂_values_mem` (theorem, [line 287](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L287))

```lean
theorem partial_eval_well_typed_app₂_values_mem :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  (TPE.evaluate env expr1 preq pes).asValue = .some v₁ →
  (TPE.evaluate env expr2 preq pes).asValue = .some v₂ →
  PEWellTyped env (Residual.binaryApp BinaryOp.mem expr1 expr2 ty) (Residual.binaryApp BinaryOp.mem (TPE.evaluate env expr1 preq pes) (TPE.evaluate env expr2 preq pes) ty) req preq es pes
```

`Cedar.Thm.partial_eval_well_typed_app₂_values` (theorem, [line 371](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L371))

```lean
theorem partial_eval_well_typed_app₂_values :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  (TPE.evaluate env expr1 preq pes).asValue = .some v₁ →
  (TPE.evaluate env expr2 preq pes).asValue = .some v₂ →
  PEWellTyped env (Residual.binaryApp op expr1 expr2 ty) (TPE.apply₂ env op (TPE.evaluate env expr1 preq pes) (TPE.evaluate env expr2 preq pes) pes ty) req preq es pes
```

`Cedar.Thm.partial_eval_well_typed_app₂_nonvalues` (theorem, [line 440](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L440))

```lean
theorem partial_eval_well_typed_app₂_nonvalues :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  (TPE.evaluate env expr1 preq pes).asValue = .none ∨ (TPE.evaluate env expr2 preq pes).asValue = .none →
  PEWellTyped env (Residual.binaryApp op expr1 expr2 ty) (TPE.apply₂ env op (TPE.evaluate env expr1 preq pes) (TPE.evaluate env expr2 preq pes) pes ty) req preq es pes
```

`Cedar.Thm.partial_eval_well_typed_app₂` (theorem, [line 576](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean#L576))

```lean
theorem partial_eval_well_typed_app₂ :
  Residual.WellTyped env (TPE.evaluate env expr1 preq pes) →
  Residual.WellTyped env (TPE.evaluate env expr2 preq pes) →
  PEWellTyped env (Residual.binaryApp op expr1 expr2 ty) (TPE.apply₂ env op (TPE.evaluate env expr1 preq pes) (TPE.evaluate env expr2 preq pes) pes ty) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [TypeLifting](../../welltyped/expr-2/typelifting.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Binary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Binary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Binary.json)
