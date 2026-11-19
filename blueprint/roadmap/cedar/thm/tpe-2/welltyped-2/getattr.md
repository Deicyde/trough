---
catalog: module
lean: Cedar.Thm.find_lifted_type, Cedar.Thm.attrs_if_partial_attrs, Cedar.Thm.entity_attr_well_typed, Cedar.Thm.partial_eval_well_typed_getAttr
statement: formalized
proof: formalized
---

# WellTyped/GetAttr

`Cedar.Thm.TPE.WellTyped.GetAttr`, in [Cedar/Thm/TPE/WellTyped/GetAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean).

`Cedar.Thm.find_lifted_type` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean#L34))

```lean
theorem find_lifted_type {attr ty₁ ty₂} {m: RecordType} :
  Map.find? m attr = some ty₁ →
  Map.find? m.liftBoolTypes attr = some ty₂ →
  ty₂ = ty₁.liftBoolTypes
```

`Cedar.Thm.attrs_if_partial_attrs` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean#L69))

```lean
theorem attrs_if_partial_attrs
  {env : TypeEnv} {req : Request} {es : Entities} {pes : PartialEntities}
  {uid : EntityUID} {m : Map Attr Value}
  (h_wf : InstanceOfWellFormedEnvironment req es env)
  (h_eref : EntitiesRefine es pes)
  (h_attrs : PartialEntities.attrs pes uid = some m) :
  ∃ (edata : EntityData),
    edata.attrs = m ∧
    InstanceOfSchemaEntry uid edata env
```

`Cedar.Thm.entity_attr_well_typed` (theorem, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean#L93))

```lean
theorem entity_attr_well_typed
  {env : TypeEnv} {req : Request} {es : Entities} {pes : PartialEntities}
  {uid : EntityUID} {ety : EntityType} {rty : RecordType}
  {m : Map Attr Value} {attr : Attr} {v : Value} {ty : CedarType} :
  InstanceOfWellFormedEnvironment req es env →
  RequestAndEntitiesRefine req es preq pes →
  InstanceOfEntityType uid ety env →
  PartialEntities.attrs pes uid = some m →
  m.find? attr = some v →
  (env.ets.attrs? ety).map RecordType.liftBoolTypes = .some rty →
  (rty.find? attr).map Qualified.getType = .some ty →
  InstanceOfType env v ty
```

`Cedar.Thm.partial_eval_well_typed_getAttr` (theorem, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean#L159))

```lean
theorem partial_eval_well_typed_getAttr {env : TypeEnv} {expr : Residual} {attr : Attr} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env expr preq pes) →
  PEWellTyped env (Residual.getAttr expr attr ty) (TPE.evaluate env (Residual.getAttr expr attr ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [TypeLifting](../../welltyped/expr-2/typelifting.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/GetAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/GetAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.GetAttr.json)
