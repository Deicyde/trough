---
catalog: module
lean: Cedar.Thm.PEWellTyped, Cedar.Thm.entity_data_from_partial
statement: formalized
proof: formalized
---

# WellTyped/Basic

`Cedar.Thm.TPE.WellTyped.Basic`, in [Cedar/Thm/TPE/WellTyped/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Basic.lean).

> This file contains theorems about partial evaluation preserving well-typedness of residuals.

`Cedar.Thm.PEWellTyped` (abbreviation, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Basic.lean#L36))

```lean
abbrev PEWellTyped (env : TypeEnv)
  (r₁ r₂ : Residual)
  (req : Request)
  (preq : PartialRequest)
  (es : Entities)
  (pes : PartialEntities) : Prop
```

`Cedar.Thm.entity_data_from_partial` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Basic.lean#L47))

```lean
theorem entity_data_from_partial
  {env : TypeEnv} {req : Request} {es : Entities} {pes : PartialEntities}
  {uid : EntityUID} {pe : PartialEntityData} :
  InstanceOfWellFormedEnvironment req es env →
  EntitiesRefine es pes →
  pes.find? uid = some pe →
  ∃ (edata : EntityData),
    es.find? uid = some edata ∧
    PartialIsValid (· = edata.attrs) pe.attrs ∧
    PartialIsValid (· = edata.ancestors) pe.ancestors ∧
    PartialIsValid (· = edata.tags) pe.tags ∧
    InstanceOfSchemaEntry uid edata env
```

## Depends on

- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Basic.json)
