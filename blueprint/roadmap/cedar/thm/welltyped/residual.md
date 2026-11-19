---
catalog: module
lean: Cedar.Thm.residual_well_typed_is_sound
statement: formalized
proof: formalized
---

# WellTyped/Residual

`Cedar.Thm.WellTyped.Residual`, in [Cedar/Thm/WellTyped/Residual.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual.lean).

> This file contains well-typedness theorems of `Residual`

`Cedar.Thm.residual_well_typed_is_sound` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual.lean#L39))

> Successful evaluation of a well-typed residual should produce a value
> of corresponding type.

```lean
theorem residual_well_typed_is_sound {r : Residual} {v : Value} {env : TypeEnv} {request : Request} {entities : Entities} :
  InstanceOfWellFormedEnvironment request entities env →
  Residual.WellTyped env r →
  r.evaluate request entities = .ok v →
  InstanceOfType env v r.typeOf
```

## Depends on

- [Residual/Definition](residual-2/definition.md)

## Proof depends on

- [Residual/Soundness](residual-2/soundness.md)

## Sources

- [Cedar/Thm/WellTyped/Residual.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.WellTyped.Residual.json)
