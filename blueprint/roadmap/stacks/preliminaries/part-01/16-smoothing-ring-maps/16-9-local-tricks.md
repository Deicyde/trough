---
declaration: section
origin: cited
lean: Stacks.Smoothing.canBeResolved_of_quotient_eighthPowerIdeal, Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal_not_le, Stacks.Smoothing.canBeResolved_of_localization_dim_zero
statement: formalized
proof: formalized
---

# 16.9 Local tricks

Section 16.9 of the Stacks Project, [Tag 07F6](https://stacks.math.columbia.edu/tag/07F6). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07F8, a lemma

[Tag 07F8](https://stacks.math.columbia.edu/tag/07F8) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_quotient_eighthPowerIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/LiftingResolutionsFromEighthPowers.lean, line 1264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/LiftingResolutionsFromEighthPowers.lean#L1264).

> **Stacks 07F8.** Let `R → A → Λ ⊃ q` be a local smoothing situation, let `r ≥ 1` and let
> `π₁, …, π_r ∈ R` map into `q`. Assume that for `i = 1, …, r` the annihilator of `π_i` equals
> the annihilator of `π_i²` in `R/(π₁⁸, …, π_{i-1}⁸)R` and likewise in
> `Λ/(π₁⁸, …, π_{i-1}⁸)Λ`, and that `π_i` maps to a strictly standard element of `A` over `R`.
> If the chain `R/(π₁⁸, …, π_r⁸)R → A/(π₁⁸, …, π_r⁸)A → Λ/(π₁⁸, …, π_r⁸)Λ`
> can be resolved at `q/(π₁⁸, …, π_r⁸)Λ`, then `R → A → Λ ⊃ q` can be resolved.

```lean
theorem canBeResolved_of_quotient_eighthPowerIdeal
    (S : LocalSmoothingSituation.{u, v, w})
    {r : ℕ} (hr : 1 ≤ r) (π : Fin r → S.R)
    (hπq : ∀ i, algebraMap S.R S.Λ (π i) ∈ S.q)
    (hannR : ∀ i,
      let I := eighthPowerPrefixIdeal π i
      (Submodule.span (S.R ⧸ I) {Ideal.Quotient.mk I (π i)}).annihilator =
        (Submodule.span (S.R ⧸ I) {(Ideal.Quotient.mk I (π i)) ^ 2}).annihilator)
    (hannΛ : ∀ i,
      let I := Ideal.map (algebraMap S.R S.Λ) (eighthPowerPrefixIdeal π i)
      (Submodule.span (S.Λ ⧸ I)
          {Ideal.Quotient.mk I (algebraMap S.R S.Λ (π i))}).annihilator =
        (Submodule.span (S.Λ ⧸ I)
          {(Ideal.Quotient.mk I (algebraMap S.R S.Λ (π i))) ^ 2}).annihilator)
    (hstandard : ∀ i,
      IsStrictlyStandard (R := S.R) (A := S.A) (algebraMap S.R S.A (π i)))
    (hresolve :
      let I := eighthPowerIdeal π
      let IA := Ideal.map (algebraMap S.R S.A) I
      let IΛ := Ideal.map (algebraMap S.A S.Λ) IA
      letI : Algebra (S.R ⧸ I) (S.Λ ⧸ IΛ) :=
        ((algebraMap (S.A ⧸ IA) (S.Λ ⧸ IΛ)).comp
          (algebraMap (S.R ⧸ I) (S.A ⧸ IA))).toAlgebra
      letI : IsScalarTower (S.R ⧸ I) (S.A ⧸ IA) (S.Λ ⧸ IΛ) :=
        IsScalarTower.of_algebraMap_eq (fun _ => rfl)
      CanBeResolved
        (S.R ⧸ I) (S.A ⧸ IA) (S.Λ ⧸ IΛ)
        (Ideal.map (Ideal.Quotient.mk IΛ) S.q)) :
    S.CanBeResolved
```

## Tag 07F9, a lemma

[Tag 07F9](https://stacks.math.columbia.edu/tag/07F9) in the Stacks Project.

**`Stacks.Smoothing.exists_finitePresentation_factorization_singularIdeal_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/SpreadingOutResolutions.lean, line 1306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/SpreadingOutResolutions.lean#L1306).

> **Stacks 07F9.** Let `R → A → Λ ⊃ q` be a local smoothing situation, `p = R ∩ q`. If `q` is
> minimal over `𝔥_A` and the localized chain `R_p → A_p → Λ_q ⊃ q Λ_q` can be resolved, then there
> is a factorization `A → C → Λ` with `C` of finite presentation over `R` and
> `H_{C/R} Λ ⊄ q`.

```lean
theorem exists_finitePresentation_factorization_singularIdeal_not_le
    (S : LocalSmoothingSituation.{u, v, w})
    (_hq : S.q ∈ S.radicalSingularIdealExtension.minimalPrimes)
    (hresolve : S.IsResolvableAfterLocalizing) :
    ∃ (Cr : Type (max u v w)) (_ : CommRing Cr) (_ : Algebra S.R Cr) (_ : Algebra S.A Cr)
        (_ : Algebra Cr S.Λ),
      IsScalarTower S.R S.A Cr ∧ IsScalarTower S.A Cr S.Λ ∧ IsScalarTower S.R Cr S.Λ ∧
        Algebra.FinitePresentation S.R Cr ∧
        ¬ Ideal.map (algebraMap Cr S.Λ) (singularIdeal S.R Cr) ≤ S.q
```

## Tag 07FA, a lemma

[Tag 07FA](https://stacks.math.columbia.edu/tag/07FA) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_localization_dim_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ZeroDimensionalResolution.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/ZeroDimensionalResolution.lean#L556).

> **Stacks 07FA.** Let `R → A → Λ ⊃ q` be a local smoothing situation with `q` minimal over
> `𝔥_A = √(H_{A/R} Λ)`. If the localized chain `R_p → A_p → Λ_q ⊃ q Λ_q` can be resolved and `Λ_q`
> has Krull dimension zero, then `R → A → Λ ⊃ q` can be resolved.

```lean
theorem canBeResolved_of_localization_dim_zero (S : LocalSmoothingSituation.{u, v, w})
    (hq : S.q ∈ S.radicalSingularIdealExtension.minimalPrimes)
    (hresolve : S.IsResolvableAfterLocalizing)
    (hdim : ringKrullDim (Localization.AtPrime S.q) = 0) : S.CanBeResolved
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.9, Tag 07F6](https://stacks.math.columbia.edu/tag/07F6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
