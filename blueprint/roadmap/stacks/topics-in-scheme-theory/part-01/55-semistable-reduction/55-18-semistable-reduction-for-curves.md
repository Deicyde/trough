---
declaration: section
origin: cited
lean: AlgebraicGeometry.SemistableReduction.semistableReductionDegreeBound, Stacks.Models.semistableReduction, Stacks.Models.exists_genusOne_semistableReduction, Stacks.Models.exists_hasSemistableReductionAtMaximalIdeals_of_two_le_genus, AlgebraicGeometry.SemistableReduction.genusZero_splitting
statement: formalized
proof: formalized
---

# 55.18 Semistable reduction for curves

Section 55.18 of the Stacks Project, [Tag 0CDM](https://stacks.math.columbia.edu/tag/0CDM). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CEJ, an equation

[Tag 0CEJ](https://stacks.math.columbia.edu/tag/0CEJ) in the Stacks Project.

**`AlgebraicGeometry.SemistableReduction.semistableReductionDegreeBound`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/Curves.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/Curves.lean#L37).

> The genus-dependent degree bound used in the semistable reduction theorem.
> Here `ℓ` is the second prime strictly greater than `768 * g`.

```lean
public noncomputable def semistableReductionDegreeBound (g : ℕ) : ℕ
```

## Tag 0CDN, a theorem

[Tag 0CDN](https://stacks.math.columbia.edu/tag/0CDN) in the Stacks Project.

**`Stacks.Models.semistableReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean#L81).

> **Stacks Project, Tag 0CDN.** Let `R` be a discrete valuation ring with fraction field `K` and
> `C` a smooth projective curve over `K` with `H⁰(C, 𝒪_C) = K`. Then there is an extension of
> discrete valuation rings `R ⊆ R'` inducing a finite separable extension `K'/K` of fraction fields
> such that `C_{K'}` has semistable reduction over `R'`. More precisely:
>
> 1. if the genus of `C` is zero, there is a separable `K'/K` of degree `2` with `C_{K'} ≅ 𝐏¹_{K'}`,
>    and `C_{K'}` is the generic fibre of the smooth projective `𝐏¹_{R'}` over the integral closure
>    `R'` of `R` in `K'`;
> 2. if the genus of `C` is one, there is a finite separable `K'/K` such that `C_{K'}` has
>    semistable reduction over `R'_𝔪` for every maximal ideal `𝔪` of the integral closure `R'` of `R`
>    in `K'`, and the special fibre of the minimal model of `C_{K'}` over `R'_𝔪` is a smooth genus
>    one curve or a cycle of rational curves;
> 3. if the genus `g` of `C` is at least two, there is a finite separable `K'/K` of degree at most
>    `B_g` such that `C_{K'}` has semistable reduction over `R'_𝔪` for every maximal ideal `𝔪` of
>    the integral closure `R'` of `R` in `K'`.

```lean
theorem semistableReduction
    (R K : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] [Field K] [Algebra R K]
    [IsFractionRing R K] {C : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c]
    (hproj : IsProjective c) [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] :
    haveI : IsProper c := hproj.isProper
    (∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
      (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
      ∃ (R' : Type u) (_ : CommRing R') (_ : IsDomain R') (_ : IsDiscreteValuationRing R')
        (_ : Algebra R' K') (_ : IsFractionRing R' K') (_ : Algebra R R')
        (_ : IsScalarTower R R' K'), IsLocalHom (algebraMap R R') ∧
        HasSemistableReduction R'
          (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
          (hproj.pullback_snd _)) ∧
    (genus c = 0 →
      ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
        (_ : IsScalarTower R K K'),
        FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧ Module.finrank K K' = 2 ∧
        Nonempty (Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K')))) ≅
          Over.mk (projectiveSpaceOver 1 (Spec (.of K')) ↘ Spec (.of K'))) ∧
        IsFractionRing (integralClosure R K') K' ∧
        Smooth (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
          Spec (.of (integralClosure R K'))) ∧
        IsProjective (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
          Spec (.of (integralClosure R K'))) ∧
        Nonempty (Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K')))) ≅
          Over.mk (pullback.snd (C := Scheme.{u})
            (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
              Spec (.of (integralClosure R K')))
            (Spec.map (CommRingCat.ofHom (algebraMap (integralClosure R K') K')))))) ∧
    (genus c = 1 →
      ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
        (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
        HasSemistableReductionAtMaximalIdeals R K'
          (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
          (hproj.pullback_snd _) ∧
        HasGenusOneMinimalFibresAtMaximalIdeals R K'
          (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))) ∧
    (2 ≤ genus c →
      ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
        (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
        Module.finrank K K' ≤
          AlgebraicGeometry.SemistableReduction.semistableReductionDegreeBound (genus c) ∧
        HasSemistableReductionAtMaximalIdeals R K'
          (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
          (hproj.pullback_snd _))
```

**`Stacks.Models.exists_genusOne_semistableReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean#L146). The attribute's comment: “(2), genus one”.

> **Stacks Project, Tag 0CDN (2), genus one.** Let `R` be a discrete valuation ring with fraction
> field `K` and `C` a smooth projective curve of genus one over `K` with `H⁰(C, 𝒪_C) = K`. Then there
> is a finite separable extension `K'/K` such that `C_{K'}` has semistable reduction over `R'_𝔪` for
> every maximal ideal `𝔪` of the integral closure `R'` of `R` in `K'`, and the special fibre of the
> minimal model of `C_{K'}` over `R'_𝔪` is a smooth genus one curve or a cycle of rational
> curves.

```lean
theorem exists_genusOne_semistableReduction
    (R K : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] [Field K] [Algebra R K]
    [IsFractionRing R K] {C : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c]
    (hproj : IsProjective c) [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)]
    (hg : genus c = 1) :
    haveI : IsProper c := hproj.isProper
    ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
      (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
      HasSemistableReductionAtMaximalIdeals R K'
        (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
        (hproj.pullback_snd _) ∧
      HasGenusOneMinimalFibresAtMaximalIdeals R K'
        (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
```

**`Stacks.Models.exists_hasSemistableReductionAtMaximalIdeals_of_two_le_genus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/Models/SemistableReduction/Unconditional.lean#L167). The attribute's comment: “(3), genus at least two”.

> **Stacks Project, Tag 0CDN (3), genus at least two.** Let `R` be a discrete valuation ring with
> fraction field `K` and `C` a smooth projective curve over `K` with `H⁰(C, 𝒪_C) = K`, of genus
> `g ≥ 2`. Then there is a finite separable extension `K'/K` of degree at most `B_g` such that
> `C_{K'}` has semistable reduction over `R'_𝔪` for every maximal ideal `𝔪` of the integral closure
> `R'` of `R` in `K'`.

```lean
theorem exists_hasSemistableReductionAtMaximalIdeals_of_two_le_genus
    (R K : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] [Field K] [Algebra R K]
    [IsFractionRing R K] {C : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c]
    (hproj : IsProjective c) [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)]
    (hg : 2 ≤ genus c) :
    haveI : IsProper c := hproj.isProper
    ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
      (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
      Module.finrank K K' ≤ AlgebraicGeometry.SemistableReduction.semistableReductionDegreeBound
        (genus c) ∧
      HasSemistableReductionAtMaximalIdeals R K'
        (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K'))))
        (hproj.pullback_snd _)
```

**`AlgebraicGeometry.SemistableReduction.genusZero_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroSplitting.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/GenusZeroSplitting.lean#L287). The attribute's comment: “(1), genus zero”.

> **Stacks Project, Tag 0CDN, part (1).** Let `R` be a discrete valuation ring with fraction
> field `K` and `C` a smooth projective curve over `K` with `H⁰(C, 𝒪_C) = K`. If the genus of `C`
> is zero, then there exists a separable extension `K'/K` of degree `2` such that
> `C_{K'} ≅ 𝐏¹_{K'}`, and hence `C_{K'}` is isomorphic to the generic fibre of the smooth projective
> scheme `𝐏¹_{R'}` over the integral closure `R'` of `R` in `K'` (whose fraction field is `K'`).
>
> The extension `K'` is returned with an `R`-algebra structure compatible with `K ⟶ K'`, the
> integral closure is `integralClosure R K'`, and the generic fibre is the base change of
> `𝐏¹_{R'} ⟶ Spec R'` along `Spec K' ⟶ Spec R'`; both isomorphisms are over `K'`.

```lean
theorem genusZero_splitting (R K : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    [Field K] [Algebra R K] [IsFractionRing R K] {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (hc : IsProjective c)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] (hgenus : genus c = 0) :
    ∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
      (_ : IsScalarTower R K K'),
      FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧ Module.finrank K K' = 2 ∧
      Nonempty (Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K')))) ≅
        Over.mk (projectiveSpaceOver 1 (Spec (.of K')) ↘ Spec (.of K'))) ∧
      IsFractionRing (integralClosure R K') K' ∧
      Smooth (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
        Spec (.of (integralClosure R K'))) ∧
      IsProjective (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
        Spec (.of (integralClosure R K'))) ∧
      Nonempty (Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K')))) ≅
        Over.mk (pullback.snd (C := Scheme.{u})
          (projectiveSpaceOver 1 (Spec (.of (integralClosure R K'))) ↘
            Spec (.of (integralClosure R K')))
          (Spec.map (CommRingCat.ofHom (algebraMap (integralClosure R K') K')))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.18, Tag 0CDM](https://stacks.math.columbia.edu/tag/0CDM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
