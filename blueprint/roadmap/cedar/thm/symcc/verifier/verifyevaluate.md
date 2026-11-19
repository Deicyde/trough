---
catalog: module
lean: Cedar.Thm.WellBehavedEvaluateQuery, Cedar.Thm.verifyEvaluate_is_sound, Cedar.Thm.verifyEvaluate_is_complete
statement: formalized
proof: formalized
---

# VerifyEvaluate

`Cedar.Thm.SymCC.Verifier.VerifyEvaluate`, in [Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean).

> This file proves the soundness and completeness of
> `Cedar.SymCC.verifyEvaluate` for well-behaved verification queries.  This
> enables proving soundness and completeness of analyses built on `verifyEvaluate`
> by proving that their queries are well-behaved.
> -

`Cedar.Thm.WellBehavedEvaluateQuery` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean#L33))

```lean
def WellBehavedEvaluateQuery (φ : Term → Term) (f : Spec.Result Value → Bool) : Prop
```

`Cedar.Thm.verifyEvaluate_is_sound` (theorem, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean#L92))

```lean
theorem verifyEvaluate_is_sound {φ : Term → Term} {f : Spec.Result Value → Bool} {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedEvaluateQuery φ f →
  εnv.StronglyWellFormedForPolicy p →
  verifyEvaluate φ p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    f (evaluate p.toExpr env.request env.entities) = true
```

`Cedar.Thm.verifyEvaluate_is_complete` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean#L121))

```lean
theorem verifyEvaluate_is_complete {φ : Term → Term} {f : Spec.Result Value → Bool} {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedEvaluateQuery φ f →
  εnv.StronglyWellFormedForPolicy p →
  verifyEvaluate φ p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    f (evaluate p.toExpr env.request env.entities) = false
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Verifier/Same](same.md)

## Proof depends on

- [Thm/SymCC/Authorizer](../authorizer.md)
- [Thm/SymCC/Enforcer](../enforcer.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluate.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyEvaluate.json)
