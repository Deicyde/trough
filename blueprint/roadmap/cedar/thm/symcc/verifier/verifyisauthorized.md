---
catalog: module
lean: Cedar.Thm.WellBehavedIsAuthorizedQuery, Cedar.Thm.verifyIsAuthorized_is_sound, Cedar.Thm.verifyIsAuthorized_is_complete
statement: formalized
proof: formalized
---

# VerifyIsAuthorized

`Cedar.Thm.SymCC.Verifier.VerifyIsAuthorized`, in [Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean).

> This file proves the soundness and completeness of
> `Cedar.SymCC.verifyIsAuthorized` for well-behaved verification queries.  This
> enables proving soundness and completenss of analyses built on
> `verifyIsAuthorized` by proving that their queries are well-behaved.
> -

`Cedar.Thm.WellBehavedIsAuthorizedQuery` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean#L33))

```lean
def WellBehavedIsAuthorizedQuery (φ : Term → Term → Term) (f : Response → Response → Bool) : Prop
```

`Cedar.Thm.verifyIsAuthorized_is_sound` (theorem, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean#L99))

```lean
theorem verifyIsAuthorized_is_sound {φ : Term → Term → Term} {f : Response → Response → Bool} {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedIsAuthorizedQuery φ f →
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyIsAuthorized φ ps₁ ps₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    env.StronglyWellFormedForPolicies ps₂ →
    f (Spec.isAuthorized env.request env.entities ps₁) (Spec.isAuthorized env.request env.entities ps₂) = true
```

`Cedar.Thm.verifyIsAuthorized_is_complete` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean#L134))

```lean
theorem verifyIsAuthorized_is_complete {φ : Term → Term → Term} {f : Response → Response → Bool} {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  WellBehavedIsAuthorizedQuery φ f →
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyIsAuthorized φ ps₁ ps₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    env.StronglyWellFormedForPolicies ps₂ ∧
    Env.EnumCompleteFor env εnv ∧
    f (Spec.isAuthorized env.request env.entities ps₁) (Spec.isAuthorized env.request env.entities ps₂) = false
```

## Depends on

- [Spec/Authorizer](../../../spec/authorizer.md)
- [Strongly well-formed ancestor relations](../data/hierarchy.md)
- [Verifier/Same](same.md)

## Proof depends on

- [Thm/SymCC/Authorizer](../authorizer.md)
- [Thm/SymCC/Enforcer](../enforcer.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyIsAuthorized.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyIsAuthorized.json)
