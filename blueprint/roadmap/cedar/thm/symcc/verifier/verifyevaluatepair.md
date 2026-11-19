---
catalog: module
lean: Cedar.Thm.WellBehavedEvaluatePairQuery, Cedar.Thm.verifyEvaluatePair_is_sound, Cedar.Thm.verifyEvaluatePair_is_complete
statement: formalized
proof: formalized
---

# VerifyEvaluatePair

`Cedar.Thm.SymCC.Verifier.VerifyEvaluatePair`, in [Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean).

> This file proves the soundness and completeness of
> `Cedar.SymCC.verifyEvaluatePair` for well-behaved verification queries.  This
> enables proving soundness and completeness of analyses built on `verifyEvaluatePair`
> by proving that their queries are well-behaved.
> -

`Cedar.Thm.WellBehavedEvaluatePairQuery` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean#L33))

```lean
def WellBehavedEvaluatePairQuery (φ : Term → Term → Term) (f : Spec.Result Value → Spec.Result Value → Bool) : Prop
```

`Cedar.Thm.verifyEvaluatePair_is_sound` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean#L103))

```lean
theorem verifyEvaluatePair_is_sound {φ : Term → Term → Term} {f : Spec.Result Value → Spec.Result Value → Bool} {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedEvaluatePairQuery φ f →
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyEvaluatePair φ p₁ p₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p₁ →
    env.StronglyWellFormedForPolicy p₂ →
    f (evaluate p₁.toExpr env.request env.entities) (evaluate p₂.toExpr env.request env.entities) = true
```

`Cedar.Thm.verifyEvaluatePair_is_complete` (theorem, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean#L142))

```lean
theorem verifyEvaluatePair_is_complete {φ : Term → Term → Term} {f : Spec.Result Value → Spec.Result Value → Bool} {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedEvaluatePairQuery φ f →
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyEvaluatePair φ p₁ p₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p₁ ∧
    env.StronglyWellFormedForPolicy p₂ ∧
    Env.EnumCompleteFor env εnv ∧
    f (evaluate p₁.toExpr env.request env.entities) (evaluate p₂.toExpr env.request env.entities) = false
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Verifier/Same](same.md)

## Proof depends on

- [Thm/SymCC/Authorizer](../authorizer.md)
- [Thm/SymCC/Enforcer](../enforcer.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluatePair.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyEvaluatePair.json)
