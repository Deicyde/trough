---
catalog: module
lean: Cedar.Thm.satisfiedPolicies_eq_error, Cedar.Thm.isAuthorized_eq_error, Cedar.Thm.compile_ok_iff_welltypedpolicy_ok, Cedar.Thm.compile_ok_iff_welltypedpolicies_ok, Cedar.Thm.compile_ok_then_exists_wtp, Cedar.Thm.compile_ok_then_exists_wtps, Cedar.Thm.cp_satAssertsOpt?_eqv_satAsserts?_ok, Cedar.Thm.cpset_satAssertsOpt?_eqv_satAsserts?_ok, Cedar.Thm.neverErrorsOpt?_eqv_neverErrors?_ok, Cedar.Thm.alwaysMatchesOpt?_eqv_alwaysMatches?_ok, Cedar.Thm.neverMatchesOpt?_eqv_neverMatches?_ok, Cedar.Thm.matchesEquivalentOpt?_eqv_matchesEquivalent?_ok, Cedar.Thm.matchesImpliesOpt?_eqv_matchesImplies?_ok, Cedar.Thm.matchesDisjointOpt?_eqv_matchesDisjoint?_ok, Cedar.Thm.neverErrorsOpt?_eqv_neverErrors?, Cedar.Thm.alwaysMatchesOpt?_eqv_alwaysMatches?, Cedar.Thm.neverMatchesOpt?_eqv_neverMatches?, Cedar.Thm.matchesEquivalentOpt?_eqv_matchesEquivalent?, Cedar.Thm.matchesImpliesOpt?_eqv_matchesImplies?, Cedar.Thm.matchesDisjointOpt?_eqv_matchesDisjoint?, Cedar.Thm.impliesOpt?_eqv_implies?_ok, Cedar.Thm.impliesOpt?_eqv_implies?, Cedar.Thm.alwaysAllowsOpt?_eqv_alwaysAllows?_ok, Cedar.Thm.alwaysAllowsOpt?_eqv_alwaysAllows?, Cedar.Thm.alwaysDeniesOpt?_eqv_alwaysDenies?_ok, Cedar.Thm.alwaysDeniesOpt?_eqv_alwaysDenies?, Cedar.Thm.equivalentOpt?_eqv_equivalent?_ok, Cedar.Thm.equivalentOpt?_eqv_equivalent?, Cedar.Thm.disjointOpt?_eqv_disjoint?_ok, Cedar.Thm.disjointOpt?_eqv_disjoint?, Cedar.Thm.checkNeverErrorsOpt_eqv_checkNeverErrors_ok, Cedar.Thm.checkAlwaysMatchesOpt_eqv_checkAlwaysMatches_ok, Cedar.Thm.checkNeverMatchesOpt_eqv_checkNeverMatches_ok, Cedar.Thm.checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent_ok, Cedar.Thm.checkMatchesImpliesOpt_eqv_checkMatchesImplies_ok, Cedar.Thm.checkMatchesDisjointOpt_eqv_checkMatchesDisjoint_ok, Cedar.Thm.checkNeverErrorsOpt_eqv_checkNeverErrors, Cedar.Thm.checkAlwaysMatchesOpt_eqv_checkAlwaysMatches, Cedar.Thm.checkNeverMatchesOpt_eqv_checkNeverMatches, Cedar.Thm.checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent, Cedar.Thm.checkMatchesImpliesOpt_eqv_checkMatchesImplies, Cedar.Thm.checkMatchesDisjointOpt_eqv_checkMatchesDisjoint, Cedar.Thm.checkImpliesOpt_eqv_checkImplies_ok, Cedar.Thm.checkImpliesOpt_eqv_checkImplies, Cedar.Thm.checkAlwaysAllowsOpt_eqv_checkAlwaysAllows_ok, Cedar.Thm.checkAlwaysAllowsOpt_eqv_checkAlwaysAllows, Cedar.Thm.checkAlwaysDeniesOpt_eqv_checkAlwaysDenies_ok, Cedar.Thm.checkAlwaysDeniesOpt_eqv_checkAlwaysDenies, Cedar.Thm.checkEquivalentOpt_eqv_checkEquivalent_ok, Cedar.Thm.checkEquivalentOpt_eqv_checkEquivalent, Cedar.Thm.checkDisjointOpt_eqv_checkDisjoint_ok, Cedar.Thm.checkDisjointOpt_eqv_checkDisjoint
statement: formalized
proof: formalized
---

# Opt

`Cedar.Thm.SymCC.Opt`, in [Cedar/Thm/SymCC/Opt.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean).

> Proofs that the optimized interface in SymCCOpt is equivalent to the unoptimized
> interface in SymCC.

`Cedar.Thm.satisfiedPolicies_eq_error` (theorem, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L57))

> If `SymCC.satisfiedPolicies` fails, that must be because `SymCC.compile` failed
> with that error on some policy

```lean
theorem satisfiedPolicies_eq_error {e : SymCC.Error} {effect : Effect} {ps : Policies} {εnv : SymEnv} :
  SymCC.satisfiedPolicies effect ps εnv = .error e →
  ∃ p ∈ ps, SymCC.compile p.toExpr εnv = .error e
```

`Cedar.Thm.isAuthorized_eq_error` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L77))

> If `SymCC.isAuthorized` fails, that must be because `SymCC.compile` failed with
> that error on some policy

```lean
theorem isAuthorized_eq_error {e : SymCC.Error} {ps : Policies} {εnv : SymEnv} :
  SymCC.isAuthorized ps εnv = .error e →
  ∃ p ∈ ps, SymCC.compile p.toExpr εnv = .error e
```

`Cedar.Thm.compile_ok_iff_welltypedpolicy_ok` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L91))

> `CompiledPolicy.compile` succeeds iff `wellTypedPolicy` succeeds
>
> Note: `Γ.WellFormed` is technically only required for the reverse direction

```lean
theorem compile_ok_iff_welltypedpolicy_ok {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed → (
  Except.isOk (CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty) ↔
  Except.isOk (wellTypedPolicy p Γ)
  )
```

`Cedar.Thm.compile_ok_iff_welltypedpolicies_ok` (theorem, [line 112](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L112))

> `CompiledPolicySet.compile` succeeds iff `wellTypedPolicies` succeeds
>
> Note: `Γ.WellFormed` is technically only required for the reverse direction

```lean
theorem compile_ok_iff_welltypedpolicies_ok {ps : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed → (
  Except.isOk (CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty) ↔
  Except.isOk (wellTypedPolicies ps Γ)
  )
```

`Cedar.Thm.compile_ok_then_exists_wtp` (theorem, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L143))

> If `CompiledPolicy.compile` succeeds, then `wellTypedPolicy` succeeds
>
> Note: Can be proved without `Γ.WellFormed`

```lean
theorem compile_ok_then_exists_wtp {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp, wellTypedPolicy p Γ = .ok wp
```

`Cedar.Thm.compile_ok_then_exists_wtps` (theorem, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L161))

> If `CompiledPolicySet.compile` succeeds, then `wellTypedPolicies` succeeds
>
> Note: Can be proved without `Γ.WellFormed`

```lean
theorem compile_ok_then_exists_wtps {ps : Policies} {cpset : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset →
  ∃ wps, wellTypedPolicies ps Γ = .ok wps
```

`Cedar.Thm.cp_satAssertsOpt?_eqv_satAsserts?_ok` (theorem, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L179))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation with `CompiledPolicy.compile` succeeds, then `satAsserts?` and
> `satAssertsOpt?` are equivalent.

```lean
theorem cp_satAssertsOpt?_eqv_satAsserts?_ok {ps wps : Policies} {cps : List CompiledPolicy} {Γ : Validation.TypeEnv} :
  ps.length = cps.length →
  cps ≠ [] →
  ps.mapM (CompiledPolicy.compile · (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty) = .ok cps →
  ps.mapM (wellTypedPolicy · Γ) = .ok wps →
  satAsserts? wps asserts (SymEnv.ofTypeEnv Γ) = satAssertsOpt? (cps.map CompiledPolicies.policy) asserts
```

`Cedar.Thm.cpset_satAssertsOpt?_eqv_satAsserts?_ok` (theorem, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L253))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation with `CompiledPolicySet.compile` succeeds, then `satAsserts?` and
> `satAssertsOpt?` are equivalent.

```lean
theorem cpset_satAssertsOpt?_eqv_satAsserts?_ok {pss wpss : List Policies} {cpsets : List CompiledPolicySet} {Γ : Validation.TypeEnv} :
  pss.length = cpsets.length →
  cpsets ≠ [] →
  pss.mapM (CompiledPolicySet.compile · (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty) = .ok cpsets →
  pss.mapM (wellTypedPolicies · Γ) = .ok wpss →
  satAsserts? wpss.flatten asserts (SymEnv.ofTypeEnv Γ) = satAssertsOpt? (cpsets.map CompiledPolicies.pset) asserts
```

`Cedar.Thm.neverErrorsOpt?_eqv_neverErrors?_ok` (theorem, [line 329](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L329))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `neverErrors?` and
> `neverErrorsOpt?` are equivalent.

```lean
theorem neverErrorsOpt?_eqv_neverErrors?_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    neverErrorsOpt? cp = neverErrors? wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.alwaysMatchesOpt?_eqv_alwaysMatches?_ok` (theorem, [line 355](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L355))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `alwaysMatches?` and
> `alwaysMatchesOpt?` are equivalent.

```lean
theorem alwaysMatchesOpt?_eqv_alwaysMatches?_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    alwaysMatchesOpt? cp = alwaysMatches? wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.neverMatchesOpt?_eqv_neverMatches?_ok` (theorem, [line 381](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L381))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `neverMatches?` and
> `neverMatchesOpt?` are equivalent.

```lean
theorem neverMatchesOpt?_eqv_neverMatches?_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    neverMatchesOpt? cp = neverMatches? wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.matchesEquivalentOpt?_eqv_matchesEquivalent?_ok` (theorem, [line 407](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L407))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `matchesEquivalent?` and
> `matchesEquivalentOpt?` are equivalent.

```lean
theorem matchesEquivalentOpt?_eqv_matchesEquivalent?_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  matchesEquivalentOpt? cp₁ cp₂ = matchesEquivalent? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.matchesImpliesOpt?_eqv_matchesImplies?_ok` (theorem, [line 432](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L432))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `matchesImplies?` and
> `matchesImpliesOpt?` are equivalent.

```lean
theorem matchesImpliesOpt?_eqv_matchesImplies?_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  matchesImpliesOpt? cp₁ cp₂ = matchesImplies? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.matchesDisjointOpt?_eqv_matchesDisjoint?_ok` (theorem, [line 457](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L457))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `matchesDisjoint?` and
> `matchesDisjointOpt?` are equivalent.

```lean
theorem matchesDisjointOpt?_eqv_matchesDisjoint?_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  matchesDisjointOpt? cp₁ cp₂ = matchesDisjoint? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.neverErrorsOpt?_eqv_neverErrors?` (theorem, [line 481](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L481))

> Full equivalence for `neverErrors?` and `neverErrorsOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem neverErrorsOpt?_eqv_neverErrors? {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ neverErrorsOpt? cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ neverErrors? wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.alwaysMatchesOpt?_eqv_alwaysMatches?` (theorem, [line 513](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L513))

> Full equivalence for `alwaysMatches?` and `alwaysMatchesOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem alwaysMatchesOpt?_eqv_alwaysMatches? {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ alwaysMatchesOpt? cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ alwaysMatches? wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.neverMatchesOpt?_eqv_neverMatches?` (theorem, [line 545](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L545))

> Full equivalence for `neverMatches?` and `neverMatchesOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem neverMatchesOpt?_eqv_neverMatches? {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ neverMatchesOpt? cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ neverMatches? wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.matchesEquivalentOpt?_eqv_matchesEquivalent?` (theorem, [line 577](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L577))

> Full equivalence for `matchesEquivalent?` and `matchesEquivalentOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem matchesEquivalentOpt?_eqv_matchesEquivalent? {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ matchesEquivalentOpt? cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ matchesEquivalent? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.matchesImpliesOpt?_eqv_matchesImplies?` (theorem, [line 614](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L614))

> Full equivalence for `matchesImplies?` and `matchesImpliesOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem matchesImpliesOpt?_eqv_matchesImplies? {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ matchesImpliesOpt? cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ matchesImplies? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.matchesDisjointOpt?_eqv_matchesDisjoint?` (theorem, [line 651](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L651))

> Full equivalence for `matchesDisjoint?` and `matchesDisjointOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem matchesDisjointOpt?_eqv_matchesDisjoint? {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ matchesDisjointOpt? cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ matchesDisjoint? wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.impliesOpt?_eqv_implies?_ok` (theorem, [line 689](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L689))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `implies?` and
> `impliesOpt?` are equivalent.

```lean
theorem impliesOpt?_eqv_implies?_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    impliesOpt? cpset₁ cpset₂ = implies? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.impliesOpt?_eqv_implies?` (theorem, [line 720](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L720))

> Full equivalence for `implies?` and `impliesOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem impliesOpt?_eqv_implies? {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ impliesOpt? cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ implies? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.alwaysAllowsOpt?_eqv_alwaysAllows?_ok` (theorem, [line 759](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L759))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `alwaysAllows?` and
> `alwaysAllowsOpt?` are equivalent.

```lean
theorem alwaysAllowsOpt?_eqv_alwaysAllows?_ok {ps : Policies} {cpset : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset →
  ∃ wps,
    wellTypedPolicies ps Γ = .ok wps ∧
    alwaysAllowsOpt? cpset = alwaysAllows? wps (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.alwaysAllowsOpt?_eqv_alwaysAllows?` (theorem, [line 786](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L786))

> Full equivalence for `alwaysAllows?` and `alwaysAllowsOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem alwaysAllowsOpt?_eqv_alwaysAllows? {ps : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset ← CompiledPolicySet.compile ps s Γ.reqty
    pure $ alwaysAllowsOpt? cpset
  ) =
  (do
    let wps ← wellTypedPolicies ps Γ |>.mapError .validationError
    pure $ alwaysAllows? wps (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.alwaysDeniesOpt?_eqv_alwaysDenies?_ok` (theorem, [line 817](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L817))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `alwaysDenies?` and
> `alwaysDeniesOpt?` are equivalent.

```lean
theorem alwaysDeniesOpt?_eqv_alwaysDenies?_ok {ps : Policies} {cpset : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset →
  ∃ wps,
    wellTypedPolicies ps Γ = .ok wps ∧
    alwaysDeniesOpt? cpset = alwaysDenies? wps (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.alwaysDeniesOpt?_eqv_alwaysDenies?` (theorem, [line 844](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L844))

> Full equivalence for `alwaysDenies?` and `alwaysDeniesOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem alwaysDeniesOpt?_eqv_alwaysDenies? {ps : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset ← CompiledPolicySet.compile ps s Γ.reqty
    pure $ alwaysDeniesOpt? cpset
  ) =
  (do
    let wps ← wellTypedPolicies ps Γ |>.mapError .validationError
    pure $ alwaysDenies? wps (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.equivalentOpt?_eqv_equivalent?_ok` (theorem, [line 875](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L875))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `equivalent?` and
> `equivalentOpt?` are equivalent.

```lean
theorem equivalentOpt?_eqv_equivalent?_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    equivalentOpt? cpset₁ cpset₂ = equivalent? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.equivalentOpt?_eqv_equivalent?` (theorem, [line 906](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L906))

> Full equivalence for `equivalent?` and `equivalentOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem equivalentOpt?_eqv_equivalent? {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ equivalentOpt? cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ equivalent? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.disjointOpt?_eqv_disjoint?_ok` (theorem, [line 945](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L945))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `disjoint?` and
> `disjointOpt?` are equivalent.

```lean
theorem disjointOpt?_eqv_disjoint?_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    disjointOpt? cpset₁ cpset₂ = disjoint? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.disjointOpt?_eqv_disjoint?` (theorem, [line 976](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L976))

> Full equivalence for `disjoint?` and `disjointOpt?`, including both the
> `.ok` and `.error` cases

```lean
theorem disjointOpt?_eqv_disjoint? {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ disjointOpt? cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ disjoint? wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkNeverErrorsOpt_eqv_checkNeverErrors_ok` (theorem, [line 1015](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1015))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkNeverErrors` and
> `checkNeverErrorsOpt?` are equivalent.

```lean
theorem checkNeverErrorsOpt_eqv_checkNeverErrors_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    checkNeverErrorsOpt cp = checkNeverErrors wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkAlwaysMatchesOpt_eqv_checkAlwaysMatches_ok` (theorem, [line 1039](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1039))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `checkAlwaysMatches` and
> `checkAlwaysMatchesOpt` are equivalent.

```lean
theorem checkAlwaysMatchesOpt_eqv_checkAlwaysMatches_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    checkAlwaysMatchesOpt cp = checkAlwaysMatches wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkNeverMatchesOpt_eqv_checkNeverMatches_ok` (theorem, [line 1063](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1063))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `checkNeverMatches` and
> `checkNeverMatchesOpt` are equivalent.

```lean
theorem checkNeverMatchesOpt_eqv_checkNeverMatches_ok {p : Policy} {cp : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp →
  ∃ wp,
    wellTypedPolicy p Γ = .ok wp ∧
    checkNeverMatchesOpt cp = checkNeverMatches wp (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent_ok` (theorem, [line 1087](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1087))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `checkMatchesEquivalent` and
> `checkMatchesEquivalentOpt` are equivalent.

```lean
theorem checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  checkMatchesEquivalentOpt cp₁ cp₂ = checkMatchesEquivalent wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkMatchesImpliesOpt_eqv_checkMatchesImplies_ok` (theorem, [line 1110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1110))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `checkMatchesImplies` and
> `checkMatchesImpliesOpt` are equivalent.

```lean
theorem checkMatchesImpliesOpt_eqv_checkMatchesImplies_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  checkMatchesImpliesOpt cp₁ cp₂ = checkMatchesImplies wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkMatchesDisjointOpt_eqv_checkMatchesDisjoint_ok` (theorem, [line 1133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1133))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicy` succeeds and `checkMatchesDisjoint` and
> `checkMatchesDisjointOpt` are equivalent.

```lean
theorem checkMatchesDisjointOpt_eqv_checkMatchesDisjoint_ok {p₁ p₂ wp₁ wp₂ : Policy} {cp₁ cp₂ : CompiledPolicy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicy.compile p₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₁ →
  CompiledPolicy.compile p₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cp₂ →
  wellTypedPolicy p₁ Γ = .ok wp₁ →
  wellTypedPolicy p₂ Γ = .ok wp₂ →
  checkMatchesDisjointOpt cp₁ cp₂ = checkMatchesDisjoint wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkNeverErrorsOpt_eqv_checkNeverErrors` (theorem, [line 1155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1155))

> Full equivalence for checkNeverErrors` and `checkNeverErrorsOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkNeverErrorsOpt_eqv_checkNeverErrors {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ checkNeverErrorsOpt cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ checkNeverErrors wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkAlwaysMatchesOpt_eqv_checkAlwaysMatches` (theorem, [line 1187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1187))

> Full equivalence for `checkAlwaysMatches` and `checkAlwaysMatchesOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkAlwaysMatchesOpt_eqv_checkAlwaysMatches {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ checkAlwaysMatchesOpt cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ checkAlwaysMatches wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkNeverMatchesOpt_eqv_checkNeverMatches` (theorem, [line 1219](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1219))

> Full equivalence for `checkNeverMatches` and `checkNeverMatchesOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkNeverMatchesOpt_eqv_checkNeverMatches {p : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp ← CompiledPolicy.compile p s Γ.reqty
    pure $ checkNeverMatchesOpt cp
  ) =
  (do
    let wp ← wellTypedPolicy p Γ |>.mapError .validationError
    pure $ checkNeverMatches wp (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent` (theorem, [line 1251](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1251))

> Full equivalence for `checkMatchesEquivalent` and `checkMatchesEquivalentOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkMatchesEquivalentOpt_eqv_checkMatchesEquivalent {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ checkMatchesEquivalentOpt cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ checkMatchesEquivalent wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkMatchesImpliesOpt_eqv_checkMatchesImplies` (theorem, [line 1288](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1288))

> Full equivalence for `checkMatchesImplies` and `checkMatchesImpliesOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkMatchesImpliesOpt_eqv_checkMatchesImplies {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ checkMatchesImpliesOpt cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ checkMatchesImplies wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkMatchesDisjointOpt_eqv_checkMatchesDisjoint` (theorem, [line 1325](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1325))

> Full equivalence for `checkMatchesDisjoint` and `checkMatchesDisjointOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkMatchesDisjointOpt_eqv_checkMatchesDisjoint {p₁ p₂ : Policy} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cp₁ ← CompiledPolicy.compile p₁ s Γ.reqty
    let cp₂ ← CompiledPolicy.compile p₂ s Γ.reqty
    pure $ checkMatchesDisjointOpt cp₁ cp₂
  ) =
  (do
    let wp₁ ← wellTypedPolicy p₁ Γ |>.mapError .validationError
    let wp₂ ← wellTypedPolicy p₂ Γ |>.mapError .validationError
    pure $ checkMatchesDisjoint wp₁ wp₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkImpliesOpt_eqv_checkImplies_ok` (theorem, [line 1363](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1363))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkImplies` and
> `checkImpliesOpt` are equivalent.

```lean
theorem checkImpliesOpt_eqv_checkImplies_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    checkImpliesOpt cpset₁ cpset₂ = checkImplies wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkImpliesOpt_eqv_checkImplies` (theorem, [line 1390](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1390))

> Full equivalence for `checkImplies` and `checkImpliesOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkImpliesOpt_eqv_checkImplies {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ checkImpliesOpt cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ checkImplies wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkAlwaysAllowsOpt_eqv_checkAlwaysAllows_ok` (theorem, [line 1429](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1429))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkAlwaysAllows` and
> `checkAlwaysAllowsOpt` are equivalent.

```lean
theorem checkAlwaysAllowsOpt_eqv_checkAlwaysAllows_ok {ps : Policies} {cpset : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset →
  ∃ wps,
    wellTypedPolicies ps Γ = .ok wps ∧
    checkAlwaysAllowsOpt cpset = checkAlwaysAllows wps (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkAlwaysAllowsOpt_eqv_checkAlwaysAllows` (theorem, [line 1452](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1452))

> Full equivalence for `checkAlwaysAllows` and `checkAlwaysAllowsOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkAlwaysAllowsOpt_eqv_checkAlwaysAllows {ps : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset ← CompiledPolicySet.compile ps s Γ.reqty
    pure $ checkAlwaysAllowsOpt cpset
  ) =
  (do
    let wps ← wellTypedPolicies ps Γ |>.mapError .validationError
    pure $ checkAlwaysAllows wps (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkAlwaysDeniesOpt_eqv_checkAlwaysDenies_ok` (theorem, [line 1483](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1483))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkAlwaysDenies` and
> `checkAlwaysDeniesOpt` are equivalent.

```lean
theorem checkAlwaysDeniesOpt_eqv_checkAlwaysDenies_ok {ps : Policies} {cpset : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset →
  ∃ wps,
    wellTypedPolicies ps Γ = .ok wps ∧
    checkAlwaysDeniesOpt cpset = checkAlwaysDenies wps (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkAlwaysDeniesOpt_eqv_checkAlwaysDenies` (theorem, [line 1506](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1506))

> Full equivalence for `checkAlwaysDenies` and `checkAlwaysDeniesOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkAlwaysDeniesOpt_eqv_checkAlwaysDenies {ps : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset ← CompiledPolicySet.compile ps s Γ.reqty
    pure $ checkAlwaysDeniesOpt cpset
  ) =
  (do
    let wps ← wellTypedPolicies ps Γ |>.mapError .validationError
    pure $ checkAlwaysDenies wps (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkEquivalentOpt_eqv_checkEquivalent_ok` (theorem, [line 1537](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1537))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkEquivalent` and
> `checkEquivalentOpt` are equivalent.

```lean
theorem checkEquivalentOpt_eqv_checkEquivalent_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    checkEquivalentOpt cpset₁ cpset₂ = checkEquivalent wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkEquivalentOpt_eqv_checkEquivalent` (theorem, [line 1564](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1564))

> Full equivalence for `checkEquivalent` and `checkEquivalentOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkEquivalentOpt_eqv_checkEquivalent {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ checkEquivalentOpt cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ checkEquivalent wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

`Cedar.Thm.checkDisjointOpt_eqv_checkDisjoint_ok` (theorem, [line 1603](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1603))

> This theorem covers the "happy path" -- showing that if optimized policy
> compilation succeeds, then `wellTypedPolicies` succeeds and `checkDisjoint` and
> `checkDisjointOpt` are equivalent.

```lean
theorem checkDisjointOpt_eqv_checkDisjoint_ok {ps₁ ps₂ : Policies} {cpset₁ cpset₂ : CompiledPolicySet} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  CompiledPolicySet.compile ps₁ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₁ →
  CompiledPolicySet.compile ps₂ (CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩) Γ.reqty = .ok cpset₂ →
  ∃ wps₁ wps₂,
    wellTypedPolicies ps₁ Γ = .ok wps₁ ∧
    wellTypedPolicies ps₂ Γ = .ok wps₂ ∧
    checkDisjointOpt cpset₁ cpset₂ = checkDisjoint wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
```

`Cedar.Thm.checkDisjointOpt_eqv_checkDisjoint` (theorem, [line 1630](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean#L1630))

> Full equivalence for `checkDisjoint` and `checkDisjointOpt`, including both the
> `.ok` and `.error` cases

```lean
theorem checkDisjointOpt_eqv_checkDisjoint {ps₁ ps₂ : Policies} {Γ : Validation.TypeEnv} :
  Γ.WellFormed →
  (do
    let s := CompiledSchema.compile ⟨Γ.ets, Γ.acts⟩
    let cpset₁ ← CompiledPolicySet.compile ps₁ s Γ.reqty
    let cpset₂ ← CompiledPolicySet.compile ps₂ s Γ.reqty
    pure $ checkDisjointOpt cpset₁ cpset₂
  ) =
  (do
    let wps₁ ← wellTypedPolicies ps₁ Γ |>.mapError .validationError
    let wps₂ ← wellTypedPolicies ps₂ Γ |>.mapError .validationError
    pure $ checkDisjoint wps₁ wps₂ (SymEnv.ofTypeEnv Γ)
  )
```

## Depends on

- [SymCCOpt](../../symccopt-2.md)
- [Typechecker/WF](../validation-2/typechecker-2/wf.md)

## Proof depends on

- [Opt/Extractor](opt-2/extractor.md)
- [Opt/Verifier](opt-2/verifier.md)
- [WellTypedOk](verifier/welltypedok.md)

## Sources

- [Cedar/Thm/SymCC/Opt.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.Opt.json)
