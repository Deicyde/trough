---
declaration: section
origin: cited
lean: Stacks.Models.hasSemistableReduction_iff_exists_isStableCurveFamily, Stacks.Models.existsUnique_isModelHom_iso_of_isStableFamilyOfSchemesOfGenus, Stacks.Models.stableReduction
statement: formalized
proof: formalized
---

# 109.24 Stable reduction theorem

Section 109.24 of the Stacks Project, [Tag 0E8C](https://stacks.math.columbia.edu/tag/0E8C). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E8D, a lemma

[Tag 0E8D](https://stacks.math.columbia.edu/tag/0E8D) in the Stacks Project.

**`Stacks.Models.hasSemistableReduction_iff_exists_isStableCurveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PrestableStabilizationTheorem.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PrestableStabilizationTheorem.lean#L119). The attribute's comment: “`C ⟶ Spec K` is smooth, projective, a curve (`IsCurve`), with `H⁰(C, 𝒪_C) = K` and genus `≥ 2`. (1) is `HasSemistableReduction R c hc` (Semistable Reduction, Definition 0CDH). (2), a stable family of curves over `R` with generic fibre `C`, is a stable family of curves `F` (Stacks 0E75) whose base is identified with `Spec R` (`ψ`), with a morphism of families of curves (a cartesian square) from the family `C ⟶ Spec K` to `F` lying over `Spec K ⟶ Spec R`.”.

> Let `R` be a discrete valuation ring with fraction field `K` and `C` a smooth projective curve
> over `K` with `H⁰(C, 𝒪_C) = K` of genus `g ≥ 2`. Then `C` has semistable reduction (Stacks 0CDH)
> exactly when it is the generic fibre of a stable family of curves over `R`: a stable family `F`
> over `Spec R` with a morphism of families of curves from `C ⟶ Spec K` to `F` lying over
> `Spec K ⟶ Spec R`.

```lean
theorem hasSemistableReduction_iff_exists_isStableCurveFamily
    (B : BigFppfSite.{u}) (hZ : B.Contains integerBase) (hR : B.Contains (Spec (.of R)))
    {C : Scheme.{u}} (c : C ⟶ Spec (.of K)) [IsCurve K c] [Smooth c] (hc : IsProjective c)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] (hg : 2 ≤ genus c) :
    HasSemistableReduction R c hc ↔
      ∃ (F : CurveFamily B hZ) (ψ : F.base ≅ integerSiteObject B hZ hR)
        (φ : @curveFamilyOfScheme K _ (Over.mk c) hc.isProper B hZ
          (contains_spec_of_isFractionRing hR)
          (IsCurve.topologicalKrullDim_eq_one (k := K) (f := c)).le ⟶ F),
        IsStableCurveFamily B hZ F ∧
          φ.baseMap ≫ ψ.hom = integerSiteMap B hZ (contains_spec_of_isFractionRing hR) hR
            (Spec.map (CommRingCat.ofHom (algebraMap R K)))
```

## Tag 0E97, a lemma

[Tag 0E97](https://stacks.math.columbia.edu/tag/0E97) in the Stacks Project.

**`Stacks.Models.existsUnique_isModelHom_iso_of_isStableFamilyOfSchemesOfGenus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StableModelExistsUnique.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StableModelExistsUnique.lean#L179).

> Let `R` be a discrete valuation ring with fraction field `K` and `C` a smooth proper curve over
> `K` with `K = H⁰(C, 𝒪_C)` and genus `g`. If `X` and `X'` are models of `C` (Section 0C2R) which are
> stable families of genus `g` curves over `R`, then there exists a unique isomorphism of models
> `X ≅ X'`.

```lean
theorem existsUnique_isModelHom_iso_of_isStableFamilyOfSchemesOfGenus (B : BigFppfSite.{u})
    (hZ : B.Contains integerBase) (hR : B.Contains (Spec (.of R))) {C : Scheme.{u}}
    (C_to_K : C ⟶ Spec (.of K)) [IsCurve K C_to_K] [Smooth C_to_K] [IsProper C_to_K]
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ C_to_K.appTop)] (g : ℕ) (_hg : genus C_to_K = g)
    {X X' : Scheme.{u}} {p : X ⟶ Spec (.of R)} {p' : X' ⟶ Spec (.of R)}
    {e : C ≅ pullback p (Spec.map (CommRingCat.ofHom (algebraMap R K)))}
    {e' : C ≅ pullback p' (Spec.map (CommRingCat.ofHom (algebraMap R K)))}
    (hX : IsModel C_to_K p e) (hX' : IsModel C_to_K p' e')
    (hst : IsStableFamilyOfSchemesOfGenus B hZ g p hR)
    (hst' : IsStableFamilyOfSchemesOfGenus B hZ g p' hR) :
    ∃! f : X ≅ X', IsModelHom p p' e e' f.hom
```

## Tag 0E98, a theorem

[Tag 0E98](https://stacks.math.columbia.edu/tag/0E98) in the Stacks Project.

**`Stacks.Models.stableReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/StableReduction/Main.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/StableReduction/Main.lean#L152).

> **Stacks Project, Tag 0E98** (stable reduction, [DM, Corollary 2.7]). Let `R` be a discrete
> valuation ring with fraction field `K` and let `C` be a smooth projective curve over `K` with
> `H⁰(C, 𝒪_C) = K` and genus `g ≥ 2`. Let `B` be a big fppf site containing `Spec R`. Then
>
> 1. there exist an extension of discrete valuation rings `R ⊆ R'` inducing a finite separable
>    extension of fraction fields `K'/K` and a stable family of curves `Y ⟶ Spec R'` of genus `g`
>    with `Y_{K'} ≅ C_{K'}` over `K'`, and
> 2. there exist a finite separable extension `L/K` and a stable family of curves `Y ⟶ Spec A` of
>    genus `g`, where `A ⊆ L` is the integral closure of `R` in `L`, such that `Y_L ≅ C_L` over
>    `L`.

```lean
theorem stableReduction (R K : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    [Field K] [Algebra R K] [IsFractionRing R K] {C : Scheme.{u}} (c : C ⟶ Spec (.of K))
    [IsCurve K c] [Smooth c] (hproj : IsProjective c)
    [IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ c.appTop)] (hg : 2 ≤ genus c) (B : BigFppfSite.{u})
    (hZ : B.Contains integerBase) (hR : B.Contains (Spec (.of R))) :
    (∃ (K' : Type u) (_ : Field K') (_ : Algebra K K') (_ : Algebra R K')
      (_ : IsScalarTower R K K'), FiniteDimensional K K' ∧ Algebra.IsSeparable K K' ∧
      ∃ (R' : Type u) (_ : CommRing R') (_ : IsDomain R') (_ : IsDiscreteValuationRing R')
        (_ : Algebra R' K') (_ : IsFractionRing R' K') (_ : Algebra R R')
        (_ : IsScalarTower R R' K'), IsLocalHom (algebraMap R R') ∧
        ∃ (hR' : B.Contains (Spec (.of R'))) (Y : Scheme.{u}) (p : Y ⟶ Spec (.of R')),
          IsStableFamilyOfSchemesOfGenus B hZ (genus c) p hR' ∧
          Nonempty (Over.mk (pullback.snd p (Spec.map (CommRingCat.ofHom (algebraMap R' K')))) ≅
            Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K K')))))) ∧
    (∃ (L : Type u) (_ : Field L) (_ : Algebra K L) (_ : Algebra R L)
      (_ : IsScalarTower R K L), FiniteDimensional K L ∧ Algebra.IsSeparable K L ∧
      ∃ (hA : B.Contains (Spec (.of (integralClosure R L)))) (Y : Scheme.{u})
        (p : Y ⟶ Spec (.of (integralClosure R L))),
        IsStableFamilyOfSchemesOfGenus B hZ (genus c) p hA ∧
        Nonempty (Over.mk (pullback.snd p
            (Spec.map (CommRingCat.ofHom (algebraMap (integralClosure R L) L)))) ≅
          Over.mk (pullback.snd c (Spec.map (CommRingCat.ofHom (algebraMap K L))))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.24, Tag 0E8C](https://stacks.math.columbia.edu/tag/0E8C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
