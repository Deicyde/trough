---
catalog: module
lean: Cedar.Thm.verifyNeverErrors_is_sound, Cedar.Thm.verifyNeverErrors_is_complete, Cedar.Thm.verifyAlwaysMatches_is_sound, Cedar.Thm.verifyAlwaysMatches_is_sound', Cedar.Thm.verifyAlwaysMatches_is_complete, Cedar.Thm.verifyAlwaysMatches_is_complete', Cedar.Thm.verifyNeverMatches_is_sound, Cedar.Thm.verifyNeverMatches_is_sound', Cedar.Thm.verifyNeverMatches_is_complete, Cedar.Thm.verifyNeverMatches_is_complete', Cedar.Thm.verifyMatchesEquivalent_is_sound, Cedar.Thm.verifyMatchesEquivalent_is_complete, Cedar.Thm.verifyMatchesImplies_is_sound, Cedar.Thm.verifyMatchesImplies_is_complete, Cedar.Thm.verifyMatchesDisjoint_is_sound, Cedar.Thm.verifyMatchesDisjoint_is_complete, Cedar.Thm.verifyEquivalent_is_sound, Cedar.Thm.verifyEquivalent_is_complete, Cedar.Thm.verifyDisjoint_is_sound, Cedar.Thm.verifyDisjoint_is_complete, Cedar.Thm.verifyImplies_is_sound, Cedar.Thm.verifyImplies_is_complete, Cedar.Thm.verifyAlwaysDenies_is_sound, Cedar.Thm.verifyAlwaysDenies_is_complete, Cedar.Thm.verifyAlwaysAllows_is_sound, Cedar.Thm.verifyAlwaysAllows_is_complete
statement: formalized
proof: formalized
---

# Verification

`Cedar.Thm.Verification`, in [Cedar/Thm/Verification.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean).

> This file proves the soundness and completeness of the verification queries in
> `Cedar.SymCC.Verifier`, which are based on Cedar's reduction to SMT. For
> soundness, we show that if the result of a query is unsatisfiable, then the
> property checked by the query holds for all _strongly well-formed_ concrete
> environments `env` that are represented by a given strongly well-formed symbolic
> environment `εnv`. For completeness, we show that if the result of the query is
> satisfiable, then there is a strongly-well formed concrete environment `env`
> represented by `εnv` for which the queried property is violated.
>
> An environment is strongly well-formed if (1) it is free of dangling entity
> references, and (2) its ancestor relation is the transitive closure of a DAG.
> Cedar verification queries (dis)prove properties with respect to strongly
> well-formed environments.
> -

`Cedar.Thm.verifyNeverErrors_is_sound` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L46))

> The `verifyNeverError` analysis is sound: if the assertions
> `verifyNeverErrors p εnv` are unsatisfiable for the policy `p` and
> the strongly well-formed symbolic environment `εnv`, then the
> evaluator will not error when applied to `p` and any
> strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyNeverErrors_is_sound  {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverErrors p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    (evaluate p.toExpr env.request env.entities).isOk
```

`Cedar.Thm.verifyNeverErrors_is_complete` (theorem, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L64))

> The `verifyNeverError` analysis is complete: if the assertions
> `verifyNeverErrors p εnv` are satisfiable for the policy `p` and the strongly
> well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the evaluator
> will error when applied to `p` and `env`.

```lean
theorem verifyNeverErrors_is_complete {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverErrors p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ (evaluate p.toExpr env.request env.entities).isOk
```

`Cedar.Thm.verifyAlwaysMatches_is_sound` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L84))

> The `verifyAlwaysMatches` analysis is sound: if the assertions
> `verifyAlwaysMatches p εnv` are unsatisfiable for the policy `p` and the
> strongly well-formed symbolic environment `εnv`, then the evaluator will return
> `.ok true` when applied to `p` and any strongly well-formed concrete environment
> `env ∈ᵢ εnv`.

```lean
theorem verifyAlwaysMatches_is_sound {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyAlwaysMatches p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    evaluate p.toExpr env.request env.entities = .ok true
```

`Cedar.Thm.verifyAlwaysMatches_is_sound'` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L104))

> Alternate definition of soundness for alwaysMatches:
>
> For a singleton policyset, if symcc says the policy alwaysMatches, then the spec
> authorizer should say it always appears in determiningPolicies

```lean
theorem verifyAlwaysMatches_is_sound' {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyAlwaysMatches p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    p.id ∈ (Spec.isAuthorized env.request env.entities [p]).determiningPolicies
```

`Cedar.Thm.verifyAlwaysMatches_is_complete` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L127))

> The `verifyAlwaysMatches` analysis is complete: if the assertions
> `verifyAlwaysMatches p εnv` are satisfiable for the policy `p` and the
> strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the evaluator
> will not return `.ok true` when applied to `p` and `env`.

```lean
theorem verifyAlwaysMatches_is_complete {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyAlwaysMatches p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    evaluate p.toExpr env.request env.entities ≠ .ok true
```

`Cedar.Thm.verifyAlwaysMatches_is_complete'` (theorem, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L151))

> Alternate definition of completeness for alwaysMatches:
>
> For a singleton policyset, if symcc says the policy does not alwaysMatch, then
> there exists a concrete environment where the policy does not appear in
> determiningPolicies.

```lean
theorem verifyAlwaysMatches_is_complete' {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyAlwaysMatches p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    p.id ∉ (Spec.isAuthorized env.request env.entities [p]).determiningPolicies
```

`Cedar.Thm.verifyNeverMatches_is_sound` (theorem, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L179))

> The `verifyNeverMatches` analysis is sound: if the assertions
> `verifyNeverMatches p εnv` are unsatisfiable for the policy `p` and the
> strongly well-formed symbolic environment `εnv`, then the evaluator will never
> return `.ok true` when applied to `p` and any strongly well-formed concrete
> environment `env ∈ᵢ εnv`.

```lean
theorem verifyNeverMatches_is_sound {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverMatches p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    evaluate p.toExpr env.request env.entities ≠ .ok true
```

`Cedar.Thm.verifyNeverMatches_is_sound'` (theorem, [line 199](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L199))

> Alternate definition of soundness for neverMatches:
>
> For a singleton policyset, if symcc says the policy neverMatches, then the spec
> authorizer should say it never appears in determiningPolicies.

```lean
theorem verifyNeverMatches_is_sound' {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverMatches p εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p →
    p.id ∉ (Spec.isAuthorized env.request env.entities [p]).determiningPolicies
```

`Cedar.Thm.verifyNeverMatches_is_complete` (theorem, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L222))

> The `verifyNeverMatches` analysis is complete: if the assertions
> `verifyNeverMatches p εnv` are satisfiable for the policy `p` and the
> strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the evaluator
> will return `.ok true` when applied to `p` and `env`.

```lean
theorem verifyNeverMatches_is_complete {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverMatches p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    evaluate p.toExpr env.request env.entities = .ok true
```

`Cedar.Thm.verifyNeverMatches_is_complete'` (theorem, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L249))

> Alternate definition of completeness for neverMatches:
>
> For a singleton policyset, if symcc says the policy does not neverMatch, then
> there exists a concrete environment where the policy appears in
> determiningPolicies.

```lean
theorem verifyNeverMatches_is_complete' {p : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p →
  verifyNeverMatches p εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p ∧
    Env.EnumCompleteFor env εnv ∧
    p.id ∈ (Spec.isAuthorized env.request env.entities [p]).determiningPolicies
```

`Cedar.Thm.verifyMatchesEquivalent_is_sound` (theorem, [line 277](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L277))

> The `verifyMatchesEquivalent` analysis is sound: if the assertions
> `verifyMatchesEquivalent p₁ p₂ εnv` are unsatisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then the policies
> will have the same matching behavior (both match or both don't match) when
> applied to any strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyMatchesEquivalent_is_sound {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesEquivalent p₁ p₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p₁ →
    env.StronglyWellFormedForPolicy p₂ →
    (evaluate p₁.toExpr env.request env.entities = .ok true) =
    (evaluate p₂.toExpr env.request env.entities = .ok true)
```

`Cedar.Thm.verifyMatchesEquivalent_is_complete` (theorem, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L308))

> The `verifyMatchesEquivalent` analysis is complete: if the assertions
> `verifyMatchesEquivalent p₁ p₂ εnv` are satisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the policies
> will have different matching behavior (one matches and the other doesn't) when
> applied to `env`.

```lean
theorem verifyMatchesEquivalent_is_complete {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesEquivalent p₁ p₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p₁ ∧
    env.StronglyWellFormedForPolicy p₂ ∧
    Env.EnumCompleteFor env εnv ∧
    (evaluate p₁.toExpr env.request env.entities = .ok true) ≠
    (evaluate p₂.toExpr env.request env.entities = .ok true)
```

`Cedar.Thm.verifyMatchesImplies_is_sound` (theorem, [line 343](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L343))

> The `verifyMatchesImplies` analysis is sound: if the assertions
> `verifyMatchesImplies p₁ p₂ εnv` are unsatisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then if `p₁` matches
> in any strongly well-formed concrete environment `env ∈ᵢ εnv`, then `p₂` also matches.

```lean
theorem verifyMatchesImplies_is_sound {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesImplies p₁ p₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p₁ →
    env.StronglyWellFormedForPolicy p₂ →
    evaluate p₁.toExpr env.request env.entities = .ok true →
    evaluate p₂.toExpr env.request env.entities = .ok true
```

`Cedar.Thm.verifyMatchesImplies_is_complete` (theorem, [line 369](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L369))

> The `verifyMatchesImplies` analysis is complete: if the assertions
> `verifyMatchesImplies p₁ p₂ εnv` are satisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that `p₁` matches
> but `p₂` does not match in `env`.

```lean
theorem verifyMatchesImplies_is_complete {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesImplies p₁ p₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p₁ ∧
    env.StronglyWellFormedForPolicy p₂ ∧
    Env.EnumCompleteFor env εnv ∧
    evaluate p₁.toExpr env.request env.entities = .ok true ∧
    evaluate p₂.toExpr env.request env.entities ≠ .ok true
```

`Cedar.Thm.verifyMatchesDisjoint_is_sound` (theorem, [line 394](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L394))

> The `verifyMatchesDisjoint` analysis is sound: if the assertions
> `verifyMatchesDisjoint p₁ p₂ εnv` are unsatisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then the policies
> cannot both match in any strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyMatchesDisjoint_is_sound {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesDisjoint p₁ p₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicy p₁ →
    env.StronglyWellFormedForPolicy p₂ →
    ¬ (evaluate p₁.toExpr env.request env.entities = .ok true ∧
       evaluate p₂.toExpr env.request env.entities = .ok true)
```

`Cedar.Thm.verifyMatchesDisjoint_is_complete` (theorem, [line 421](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L421))

> The `verifyMatchesDisjoint` analysis is complete: if the assertions
> `verifyMatchesDisjoint p₁ p₂ εnv` are satisfiable for the policies `p₁` and `p₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that both policies
> match in `env`.

```lean
theorem verifyMatchesDisjoint_is_complete {p₁ p₂ : Policy} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicy p₁ →
  εnv.StronglyWellFormedForPolicy p₂ →
  verifyMatchesDisjoint p₁ p₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicy p₁ ∧
    env.StronglyWellFormedForPolicy p₂ ∧
    Env.EnumCompleteFor env εnv ∧
    evaluate p₁.toExpr env.request env.entities = .ok true ∧
    evaluate p₂.toExpr env.request env.entities = .ok true
```

`Cedar.Thm.verifyEquivalent_is_sound` (theorem, [line 448](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L448))

> The `verifyEquivalent` analysis is sound: if the assertions
> `verifyEquivalent ps₁ ps₂ εnv` are unsatisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then the authorizer
> will produce the same authorization decision when applied to `ps₁`, `ps₂`, and
> any strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyEquivalent_is_sound  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyEquivalent ps₁ ps₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    env.StronglyWellFormedForPolicies ps₂ →
    bothAllowOrBothDeny
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyEquivalent_is_complete` (theorem, [line 471](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L471))

> The `verifyEquivalent` analysis is complete: if the assertions
> `verifyEquivalent ps₁ ps₂ εnv` are satisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the authorizer
> will produce different authorization decisions when applied to `ps₁`, `ps₂`,
> and `env`.

```lean
theorem verifyEquivalent_is_complete  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyEquivalent ps₁ ps₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    env.StronglyWellFormedForPolicies ps₂ ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ bothAllowOrBothDeny
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyDisjoint_is_sound` (theorem, [line 495](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L495))

> The `verifyDisjoint` analysis is sound: if the assertions
> `verifyDisjoint ps₁ ps₂ εnv` are unsatisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then the authorizer
> will not produce two `allow` decisions when applied to `ps₁`, `ps₂`, and
> any strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyDisjoint_is_sound  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyDisjoint ps₁ ps₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    env.StronglyWellFormedForPolicies ps₂ →
    atLeastOneDenies
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyDisjoint_is_complete` (theorem, [line 518](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L518))

> The `verifyDisjoint` analysis is complete: if the assertions
> `verifyDisjoint ps₁ ps₂ εnv` are satisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the authorizer
> will produce two `allow` decisions when applied to `ps₁`, `ps₂`,
> and `env`.

```lean
theorem verifyDisjoint_is_complete  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyDisjoint ps₁ ps₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    env.StronglyWellFormedForPolicies ps₂ ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ atLeastOneDenies
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyImplies_is_sound` (theorem, [line 542](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L542))

> The `verifyImplies` analysis is sound: if the assertions
> `verifyImplies ps₁ ps₂ εnv` are unsatisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then if the authorizer
> returns `allow` for `ps₁`, it also returns `allow` for `ps₂` in
> any strongly well-formed concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyImplies_is_sound  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyImplies ps₁ ps₂ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    env.StronglyWellFormedForPolicies ps₂ →
    ifFirstAllowsSoDoesSecond
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyImplies_is_complete` (theorem, [line 564](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L564))

> The `verifyImplies` analysis is complete: if the assertions
> `verifyImplies ps₁ ps₂ εnv` are satisfiable for the policies `ps₁` and `ps₂`
> and the strongly well-formed symbolic environment `εnv`, then there exists a
> strongly well-formed concrete environment `env ∈ᵢ εnv` such that the authorizer
> will produce `allow` for `ps₁` but `deny` for `ps₂` in `env`.

```lean
theorem verifyImplies_is_complete  {ps₁ ps₂ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  εnv.StronglyWellFormedForPolicies ps₂ →
  verifyImplies ps₁ ps₂ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    env.StronglyWellFormedForPolicies ps₂ ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ ifFirstAllowsSoDoesSecond
      (Spec.isAuthorized env.request env.entities ps₁)
      (Spec.isAuthorized env.request env.entities ps₂)
```

`Cedar.Thm.verifyAlwaysDenies_is_sound` (theorem, [line 588](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L588))

> The `verifyAlwaysDenies` analysis is sound: if the assertions
> `verifyAlwaysDenies ps₁ εnv` are unsatisfiable for the policies `ps₁`
> and the strongly well-formed symbolic environment `εnv`, then the authorizer
> will return `deny` when applied to `ps₁` and any strongly well-formed
> concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyAlwaysDenies_is_sound  {ps₁ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  verifyAlwaysDenies ps₁ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    denies (Spec.isAuthorized env.request env.entities ps₁)
```

`Cedar.Thm.verifyAlwaysDenies_is_complete` (theorem, [line 611](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L611))

> The `verifyAlwaysDenies` analysis is sound: if the assertions
> `verifyAlwaysDenies ps₁ εnv` are satisfiable for the policies `ps₁`
> and the strongly well-formed symbolic environment `εnv`, then there
> exists a strongly well-formed concrete environment `env ∈ᵢ εnv` such
> that the authorizer will not return `deny` when applied to `ps₁` and `env`.

```lean
theorem verifyAlwaysDenies_is_complete {ps₁ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  verifyAlwaysDenies ps₁ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ denies (Spec.isAuthorized env.request env.entities ps₁)
```

`Cedar.Thm.verifyAlwaysAllows_is_sound` (theorem, [line 636](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L636))

> The `verifyAlwaysAllows` analysis is sound: if the assertions
> `verifyAlwaysAllows ps₁ εnv` are unsatisfiable for the policies `ps₁`
> and the strongly well-formed symbolic environment `εnv`, then the authorizer
> will return `allow` when applied to `ps₁` and any strongly well-formed
> concrete environment `env ∈ᵢ εnv`.

```lean
theorem verifyAlwaysAllows_is_sound  {ps₁ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  verifyAlwaysAllows ps₁ εnv = .ok asserts →
  εnv ⊭ asserts →
  ∀ env,
    env ∈ᵢ εnv →
    env.StronglyWellFormedForPolicies ps₁ →
    allows (Spec.isAuthorized env.request env.entities ps₁)
```

`Cedar.Thm.verifyAlwaysAllows_is_complete` (theorem, [line 660](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean#L660))

> The `verifyAlwaysAllows` analysis is sound: if the assertions
> `verifyAlwaysAllows ps₁ εnv` are satisfiable for the policies `ps₁`
> and the strongly well-formed symbolic environment `εnv`, then there
> exists a strongly well-formed concrete environment `env ∈ᵢ εnv` such
> that the authorizer will not return `allow` when applied to `ps₁` and `env`.

```lean
theorem verifyAlwaysAllows_is_complete {ps₁ : Policies} {εnv : SymEnv} {asserts : Asserts} :
  εnv.StronglyWellFormedForPolicies ps₁ →
  verifyAlwaysAllows ps₁ εnv = .ok asserts →
  εnv ⊧ asserts →
  ∃ env,
    env ∈ᵢ εnv ∧
    env.StronglyWellFormedForPolicies ps₁ ∧
    Env.EnumCompleteFor env εnv ∧
    ¬ allows (Spec.isAuthorized env.request env.entities ps₁)
```

## Depends on

- [VerifyIsAuthorizedQueries](symcc/verifier/verifyisauthorizedqueries.md)

## Proof depends on

- [VerifyEvaluatePairQueries](symcc/verifier/verifyevaluatepairqueries.md)

## Sources

- [Cedar/Thm/Verification.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Verification.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.Verification.json)
