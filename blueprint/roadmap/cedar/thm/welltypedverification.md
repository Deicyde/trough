---
catalog: module
lean: Cedar.Thm.verifyNeverErrors_is_ok_and_sound, Cedar.Thm.verifyNeverErrors_is_ok_and_complete, Cedar.Thm.verifyAlwaysMatches_is_ok_and_sound, Cedar.Thm.verifyAlwaysMatches_is_ok_and_complete, Cedar.Thm.verifyNeverMatches_is_ok_and_sound, Cedar.Thm.verifyNeverMatches_is_ok_and_complete, Cedar.Thm.verifyMatchesEquivalent_is_ok_and_sound, Cedar.Thm.verifyMatchesEquivalent_is_ok_and_complete, Cedar.Thm.verifyMatchesImplies_is_ok_and_sound, Cedar.Thm.verifyMatchesImplies_is_ok_and_complete, Cedar.Thm.verifyMatchesDisjoint_is_ok_and_sound, Cedar.Thm.verifyMatchesDisjoint_is_ok_and_complete, Cedar.Thm.verifyEquivalent_is_ok_and_sound, Cedar.Thm.verifyEquivalent_is_ok_and_complete, Cedar.Thm.verifyDisjoint_is_ok_and_sound, Cedar.Thm.verifyDisjoint_is_ok_and_complete, Cedar.Thm.verifyImplies_is_ok_and_sound, Cedar.Thm.verifyImplies_is_ok_and_complete, Cedar.Thm.verifyAlwaysDenies_is_ok_and_sound, Cedar.Thm.verifyAlwaysDenies_is_ok_and_complete, Cedar.Thm.verifyAlwaysAllows_is_ok_and_sound, Cedar.Thm.verifyAlwaysAllows_is_ok_and_complete
statement: formalized
proof: formalized
---

# WellTypedVerification

`Cedar.Thm.WellTypedVerification`, in [Cedar/Thm/WellTypedVerification.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean).

> This file connects soundness theorems in `Cedar.Thm.Verification`
> with policy validation.
>
> We prove that if validation of a policy (set) succeeds in the sense of
> `wellTypedPolicy`/`wellTypedPolicies`), then various verification tasks
> would produce a symbolic encoding *without errors*, and is sound with
> respect to concrete `Env`s.

`Cedar.Thm.verifyNeverErrors_is_ok_and_sound` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L47))

> Concrete version of `verifyNeverErrors_is_sound`.
>
> NOTE: This theorem and many of the following soundness theorems
> use `env.StronglyWellFormedForPolicy p'` in the conclusion
> rather than `env.StronglyWellFormedForPolicy p`.
>
> One can obtain a weaker version with `env.StronglyWellFormedForPolicy p`,
> using the lemma `wellTypedPolicy_preserves_StronglyWellFormedForPolicy`.

```lean
theorem verifyNeverErrors_is_ok_and_sound {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyNeverErrors p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p' →
        (evaluate p.toExpr env.request env.entities).isOk)
```

`Cedar.Thm.verifyNeverErrors_is_ok_and_complete` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L70))

> Concrete version of `verifyNeverErrors_is_complete`.

```lean
theorem verifyNeverErrors_is_ok_and_complete {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyNeverErrors p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p' ∧
        ¬ (evaluate p.toExpr env.request env.entities).isOk)
```

`Cedar.Thm.verifyAlwaysMatches_is_ok_and_sound` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L94))

> Concrete version of `verifyAlwaysMatches_is_sound`.

```lean
theorem verifyAlwaysMatches_is_ok_and_sound {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyAlwaysMatches p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p' →
        evaluate p.toExpr env.request env.entities = .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyAlwaysMatches_is_ok_and_complete` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L118))

> Concrete version of `verifyAlwaysMatches_is_complete`.

```lean
theorem verifyAlwaysMatches_is_ok_and_complete {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyAlwaysMatches p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p' ∧
        evaluate p.toExpr env.request env.entities ≠ .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyNeverMatches_is_ok_and_sound` (theorem, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L144))

> Concrete version of `verifyNeverMatches_is_sound`.

```lean
theorem verifyNeverMatches_is_ok_and_sound {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyNeverMatches p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p' →
        evaluate p.toExpr env.request env.entities ≠ .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyNeverMatches_is_ok_and_complete` (theorem, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L168))

> Concrete version of `verifyNeverMatches_is_complete`.

```lean
theorem verifyNeverMatches_is_ok_and_complete {p p' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p Γ = .ok p' →
  ∃ asserts,
    verifyNeverMatches p' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p' ∧
        evaluate p.toExpr env.request env.entities = .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyMatchesEquivalent_is_ok_and_sound` (theorem, [line 194](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L194))

> Concrete version of `verifyMatchesEquivalent_is_sound`.

```lean
theorem verifyMatchesEquivalent_is_ok_and_sound {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesEquivalent p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p₁' →
        env.StronglyWellFormedForPolicy p₂' →
        (evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true))) =
        (evaluate p₂.toExpr env.request env.entities = .ok (.prim (.bool true))))
```

`Cedar.Thm.verifyMatchesEquivalent_is_ok_and_complete` (theorem, [line 223](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L223))

> Concrete version of `verifyMatchesEquivalent_is_complete`.

```lean
theorem verifyMatchesEquivalent_is_ok_and_complete {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesEquivalent p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p₁' ∧
        env.StronglyWellFormedForPolicy p₂' ∧
        (evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true))) ≠
        (evaluate p₂.toExpr env.request env.entities = .ok (.prim (.bool true))))
```

`Cedar.Thm.verifyMatchesImplies_is_ok_and_sound` (theorem, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L253))

> Concrete version of `verifyMatchesImplies_is_sound`.

```lean
theorem verifyMatchesImplies_is_ok_and_sound {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesImplies p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p₁' →
        env.StronglyWellFormedForPolicy p₂' →
        evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true)) →
        evaluate p₂.toExpr env.request env.entities = .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyMatchesImplies_is_ok_and_complete` (theorem, [line 282](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L282))

> Concrete version of `verifyMatchesImplies_is_complete`.

```lean
theorem verifyMatchesImplies_is_ok_and_complete {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesImplies p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p₁' ∧
        env.StronglyWellFormedForPolicy p₂' ∧
        evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true)) ∧
        evaluate p₂.toExpr env.request env.entities ≠ .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyMatchesDisjoint_is_ok_and_sound` (theorem, [line 312](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L312))

> Concrete version of `verifyMatchesDisjoint_is_sound`.

```lean
theorem verifyMatchesDisjoint_is_ok_and_sound {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesDisjoint p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicy p₁' →
        env.StronglyWellFormedForPolicy p₂' →
        ¬ (evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true)) ∧
           evaluate p₂.toExpr env.request env.entities = .ok (.prim (.bool true))))
```

`Cedar.Thm.verifyMatchesDisjoint_is_ok_and_complete` (theorem, [line 341](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L341))

> Concrete version of `verifyMatchesDisjoint_is_complete`.

```lean
theorem verifyMatchesDisjoint_is_ok_and_complete {p₁ p₁' p₂ p₂' : Policy} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicy p₁ Γ = .ok p₁' →
  wellTypedPolicy p₂ Γ = .ok p₂' →
  ∃ asserts,
    verifyMatchesDisjoint p₁' p₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicy p₁' ∧
        env.StronglyWellFormedForPolicy p₂' ∧
        evaluate p₁.toExpr env.request env.entities = .ok (.prim (.bool true)) ∧
        evaluate p₂.toExpr env.request env.entities = .ok (.prim (.bool true)))
```

`Cedar.Thm.verifyEquivalent_is_ok_and_sound` (theorem, [line 371](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L371))

> Concrete version of `verifyEquivalent_is_sound`.

```lean
theorem verifyEquivalent_is_ok_and_sound {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyEquivalent ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicies ps₁' →
        env.StronglyWellFormedForPolicies ps₂' →
        bothAllowOrBothDeny
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyEquivalent_is_ok_and_complete` (theorem, [line 401](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L401))

> Concrete version of `verifyEquivalent_is_complete`.

```lean
theorem verifyEquivalent_is_ok_and_complete {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyEquivalent ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicies ps₁' ∧
        env.StronglyWellFormedForPolicies ps₂' ∧
        ¬ bothAllowOrBothDeny
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyDisjoint_is_ok_and_sound` (theorem, [line 432](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L432))

> Concrete version of `verifyDisjoint_is_sound`.

```lean
theorem verifyDisjoint_is_ok_and_sound {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyDisjoint ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicies ps₁' →
        env.StronglyWellFormedForPolicies ps₂' →
        atLeastOneDenies
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyDisjoint_is_ok_and_complete` (theorem, [line 462](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L462))

> Concrete version of `verifyDisjoint_is_complete`.

```lean
theorem verifyDisjoint_is_ok_and_complete {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyDisjoint ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicies ps₁' ∧
        env.StronglyWellFormedForPolicies ps₂' ∧
        ¬ atLeastOneDenies
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyImplies_is_ok_and_sound` (theorem, [line 493](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L493))

> Concrete version of `verifyImplies_is_sound`.

```lean
theorem verifyImplies_is_ok_and_sound {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyImplies ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicies ps₁' →
        env.StronglyWellFormedForPolicies ps₂' →
        ifFirstAllowsSoDoesSecond
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyImplies_is_ok_and_complete` (theorem, [line 523](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L523))

> Concrete version of `verifyImplies_is_complete`.

```lean
theorem verifyImplies_is_ok_and_complete {ps₁ ps₁' ps₂ ps₂' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  wellTypedPolicies ps₂ Γ = .ok ps₂' →
  ∃ asserts,
    verifyImplies ps₁' ps₂' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicies ps₁' ∧
        env.StronglyWellFormedForPolicies ps₂' ∧
        ¬ ifFirstAllowsSoDoesSecond
          (Spec.isAuthorized env.request env.entities ps₁)
          (Spec.isAuthorized env.request env.entities ps₂))
```

`Cedar.Thm.verifyAlwaysDenies_is_ok_and_sound` (theorem, [line 554](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L554))

> Concrete version of `verifyAlwaysDenies_is_sound`.

```lean
theorem verifyAlwaysDenies_is_ok_and_sound {ps₁ ps₁' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  ∃ asserts,
    verifyAlwaysDenies ps₁' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicies ps₁' →
        denies (Spec.isAuthorized env.request env.entities ps₁))
```

`Cedar.Thm.verifyAlwaysDenies_is_ok_and_complete` (theorem, [line 578](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L578))

> Concrete version of `verifyAlwaysDenies_is_complete`.

```lean
theorem verifyAlwaysDenies_is_ok_and_complete {ps₁ ps₁' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  ∃ asserts,
    verifyAlwaysDenies ps₁' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicies ps₁' ∧
        ¬ denies (Spec.isAuthorized env.request env.entities ps₁))
```

`Cedar.Thm.verifyAlwaysAllows_is_ok_and_sound` (theorem, [line 603](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L603))

> Concrete version of `verifyAlwaysAllows_is_sound`.

```lean
theorem verifyAlwaysAllows_is_ok_and_sound {ps₁ ps₁' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  ∃ asserts,
    verifyAlwaysAllows ps₁' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊭ asserts →
      ∀ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ →
        env.StronglyWellFormedForPolicies ps₁' →
        allows (Spec.isAuthorized env.request env.entities ps₁))
```

`Cedar.Thm.verifyAlwaysAllows_is_ok_and_complete` (theorem, [line 627](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean#L627))

> Concrete version of `verifyAlwaysAllows_is_complete`.

```lean
theorem verifyAlwaysAllows_is_ok_and_complete {ps₁ ps₁' : Policies} {Γ : TypeEnv} :
  Γ.WellFormed →
  wellTypedPolicies ps₁ Γ = .ok ps₁' →
  ∃ asserts,
    verifyAlwaysAllows ps₁' (SymEnv.ofEnv Γ) = .ok asserts ∧
    (SymEnv.ofEnv Γ ⊧ asserts →
      ∃ env : Env,
        InstanceOfWellFormedEnvironment env.request env.entities Γ ∧
        env.StronglyWellFormedForPolicies ps₁' ∧
        ¬ allows (Spec.isAuthorized env.request env.entities ps₁))
```

## Depends on

- [SymCC](../symcc-2.md)
- [VerifyIsAuthorizedQueries](symcc/verifier/verifyisauthorizedqueries.md)
- [Typechecker/Types](validation-2/typechecker-2/types.md)

## Proof depends on

- [Completeness](symcc/env/completeness.md)
- [Env/Soundness](symcc/env/soundness.md)
- [WellTypedOk](symcc/verifier/welltypedok.md)
- [Verification](verification.md)

## Sources

- [Cedar/Thm/WellTypedVerification.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTypedVerification.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.WellTypedVerification.json)
