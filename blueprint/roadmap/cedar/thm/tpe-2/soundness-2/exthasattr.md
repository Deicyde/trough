---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_ext_has_attr
statement: formalized
proof: formalized
---

# Soundness/ExtHasAttr

`Cedar.Thm.TPE.Soundness.ExtHasAttr`, in [Cedar/Thm/TPE/Soundness/ExtHasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/ExtHasAttr.lean).

`Cedar.Thm.partial_evaluate_is_sound_ext_has_attr` (theorem, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/ExtHasAttr.lean#L155))

```lean
theorem partial_evaluate_is_sound_ext_has_attr
{env : TypeEnv}
{x₁ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{attr : Attr}
{attrs : List Attr}
(hwf : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env x₁)
(h₄ : RequestAndEntitiesRefine req es preq pes)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es)) :
  Except.toOption ((x₁.extHasAttr attr attrs (CedarType.bool BoolType.anyBool)).evaluate req es) =
  Except.toOption ((TPE.evaluate env (x₁.extHasAttr attr attrs (CedarType.bool BoolType.anyBool)) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [Soundness/HasAttr](hasattr.md)

## Sources

- [Cedar/Thm/TPE/Soundness/ExtHasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/ExtHasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.ExtHasAttr.json)
