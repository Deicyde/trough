---
catalog: module
lean: Cedar.Thm.partial_evaluate_is_sound_or
statement: formalized
proof: formalized
---

# Soundness/Or

`Cedar.Thm.TPE.Soundness.Or`, in [Cedar/Thm/TPE/Soundness/Or.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Or.lean).

`Cedar.Thm.partial_evaluate_is_sound_or` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Or.lean#L37))

```lean
theorem partial_evaluate_is_sound_or
{x₁ x₂ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{env : TypeEnv}
(h₂ : InstanceOfWellFormedEnvironment req es env)
(h₃ : RequestAndEntitiesRefine req es preq pes)
(hᵢ₁ : Residual.WellTyped env x₁)
(hᵢ₂ : Residual.WellTyped env x₂)
(hᵢ₃ : x₁.typeOf = CedarType.bool BoolType.anyBool)
(hᵢ₄ : x₂.typeOf = CedarType.bool BoolType.anyBool)
(hᵢ₅ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es))
(hᵢ₆ : Except.toOption (x₂.evaluate req es) = Except.toOption ((TPE.evaluate env x₂ preq pes).evaluate req es)) :
  Except.toOption ((x₁.or x₂ (CedarType.bool BoolType.anyBool)).evaluate req es) =
  Except.toOption ((TPE.evaluate env (x₁.or x₂ (CedarType.bool BoolType.anyBool)) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [ErrorFree](../errorfree.md)
- [TPE/WellTyped](../welltyped.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Or.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Or.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Or.json)
