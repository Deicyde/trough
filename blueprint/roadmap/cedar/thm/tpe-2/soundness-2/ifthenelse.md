---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_ite
statement: formalized
proof: formalized
---

# Soundness/IfThenElse

`Cedar.Thm.TPE.Soundness.IfThenElse`, in [Cedar/Thm/TPE/Soundness/IfThenElse.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/IfThenElse.lean).

`Cedar.Thm.partial_evaluate_is_sound_ite` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/IfThenElse.lean#L37))

```lean
theorem partial_evaluate_is_sound_ite
{x₁ x₂ x₃ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{env : TypeEnv}
(h₂ : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env x₁)
(hₜ : x₁.typeOf = CedarType.bool BoolType.anyBool)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es))
(hᵢ₂ : Except.toOption (x₂.evaluate req es) = Except.toOption ((TPE.evaluate env x₂ preq pes).evaluate req es))
(hᵢ₃ : Except.toOption (x₃.evaluate req es) = Except.toOption ((TPE.evaluate env x₃ preq pes).evaluate req es)) :
  Except.toOption ((x₁.ite x₂ x₃ x₂.typeOf).evaluate req es) =
  Except.toOption ((TPE.evaluate env (x₁.ite x₂ x₃ x₂.typeOf) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [WellTyped/Residual](../../welltyped/residual.md)

## Sources

- [Cedar/Thm/TPE/Soundness/IfThenElse.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/IfThenElse.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.IfThenElse.json)
