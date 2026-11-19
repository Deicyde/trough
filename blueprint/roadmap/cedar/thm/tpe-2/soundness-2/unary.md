---
catalog: module
lean: Cedar.Thm.is_eq_type_comparison_of_entity_type, Cedar.Thm.try_decide_residual₁_sound, Cedar.Thm.partial_evaluate_is_sound_unary_app
statement: formalized
proof: formalized
---

# Soundness/Unary

`Cedar.Thm.TPE.Soundness.Unary`, in [Cedar/Thm/TPE/Soundness/Unary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Unary.lean).

`Cedar.Thm.is_eq_type_comparison_of_entity_type` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Unary.lean#L39))

> `is` on an entity-typed value is decided by comparing the two types.

```lean
theorem is_eq_type_comparison_of_entity_type
  {env : TypeEnv} {v : Value} {ety₁ ety₂ : EntityType}
  (hinst : InstanceOfType env v (.entity ety₂)) :
  Spec.apply₁ (.is ety₁) v = .ok (Value.prim (Prim.bool (ety₁ == ety₂)))
```

`Cedar.Thm.try_decide_residual₁_sound` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Unary.lean#L48))

```lean
theorem try_decide_residual₁_sound
{env : TypeEnv} {r₁ : Residual} {req : Request}
{es : Entities} {op₁ : UnaryOp} {v : Value}
(hwf : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env r₁)
(hdec : TPE.tryDecideResidual₁ op₁ r₁ = .some v) :
  ∃ v', r₁.evaluate req es = .ok v' ∧ Spec.apply₁ op₁ v' = .ok v
```

`Cedar.Thm.partial_evaluate_is_sound_unary_app` (theorem, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Unary.lean#L72))

```lean
theorem partial_evaluate_is_sound_unary_app
{x₁ : Residual}
{req : Request}
{es : Entities}
{preq : PartialRequest}
{pes : PartialEntities}
{op₁ : UnaryOp}
{ty : CedarType}
{env : TypeEnv}
(h₂ : InstanceOfWellFormedEnvironment req es env)
(hwt : Residual.WellTyped env x₁)
(h_ref : RequestAndEntitiesRefine req es preq pes)
(hᵢ₁ : Except.toOption (x₁.evaluate req es) = Except.toOption ((TPE.evaluate env x₁ preq pes).evaluate req es)) :
  Except.toOption ((Residual.unaryApp op₁ x₁ ty).evaluate req es) =
  Except.toOption ((TPE.evaluate env (Residual.unaryApp op₁ x₁ ty) preq pes).evaluate req es)
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [Thm/TPE/Input](../input.md)
- [Residual/Definition](../../welltyped/residual-2/definition.md)

## Proof depends on

- [ErrorFree](../errorfree.md)
- [Soundness/Basic](basic.md)
- [TPE/WellTyped](../welltyped.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Unary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Unary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Unary.json)
