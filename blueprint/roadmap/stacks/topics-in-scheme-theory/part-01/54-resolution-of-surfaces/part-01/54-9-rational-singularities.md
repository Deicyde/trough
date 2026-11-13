---
declaration: section
origin: cited
lean: AlgebraicGeometry.RationalSingularitySituation, AlgebraicGeometry.RationalSingularitySituation.isZero_cohomology_of_isQuasicoherent, AlgebraicGeometry.RationalSingularitySituation.isZero_firstCohomology_exceptionalIdealPow_unconditional, AlgebraicGeometry.RationalSingularitySituation.idealSheafGlobalSections_exceptionalIdealPow_unconditional, AlgebraicGeometry.isNormal_blowUp_maximalIdeal_rationalSingularitySituation, AlgebraicGeometry.isProper_exceptionalDivisorToCentre_residuePoint, AlgebraicGeometry.topologicalKrullDim_exceptionalDivisor_residuePoint, AlgebraicGeometry.isProper_and_topologicalKrullDim_eq_one_and_isCohenMacaulay_exceptionalDivisor
statement: formalized
proof: formalized
---

# 54.9 Rational singularities

Section 54.9 of the Stacks Project, [Tag 0B4V](https://stacks.math.columbia.edu/tag/0B4V). 8 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B4W, a situation

[Tag 0B4W](https://stacks.math.columbia.edu/tag/0B4W) in the Stacks Project.

**`AlgebraicGeometry.RationalSingularitySituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/Basic.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/Basic.lean#L52).

> **Stacks Project, Tag 0B4W.** A local normal Nagata domain of dimension two defining a
> rational singularity, a normal modification of its spectrum, and an enumeration of the
> irreducible components of the special fibre.

```lean
structure RationalSingularitySituation
```

## Tag 0B4X, a lemma

[Tag 0B4X](https://stacks.math.columbia.edu/tag/0B4X) in the Stacks Project.

**`AlgebraicGeometry.RationalSingularitySituation.isZero_cohomology_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/QuasicoherentCohomologyExtra.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/QuasicoherentCohomologyExtra.lean#L95).

> **[Stacks, Tag 0B4X].** In Situation [Stacks, Tag 0B4W], let `ℱ` be a quasi-coherent
> `𝒪_X`-module. Then
>
> 1. `Hᵖ(X, ℱ) = 0` for `p ∉ {0, 1}`, and
> 2. `H¹(X, ℱ) = 0` if `ℱ` is globally generated.
>
> "Globally generated" is the existence of a family of global sections generating `ℱ`, Mathlib's
> `SheafOfModules.GeneratingSections`.

```lean
theorem isZero_cohomology_of_isQuasicoherent (F : S.X.Modules) [F.IsQuasicoherent] :
    (∀ p : ℤ, p ∉ ({0, 1} : Set ℤ) →
        IsZero (((moduleGlobalSections S.X).rightDerivedPlus p).obj F)) ∧
      (Nonempty (SheafOfModules.GeneratingSections F) →
        IsZero (((moduleGlobalSections S.X).rightDerivedPlus 1).obj F))
```

## Tag 0B4Y, a lemma

[Tag 0B4Y](https://stacks.math.columbia.edu/tag/0B4Y) in the Stacks Project.

**`AlgebraicGeometry.RationalSingularitySituation.isZero_firstCohomology_exceptionalIdealPow_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalIdealPowersExtra.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalIdealPowersExtra.lean#L81). The attribute's comment: “the conclusion H¹(X, 𝓘ⁿ) = 0 for all n”.

> In Situation [Stacks, Tag 0B4W], `H¹(X, 𝓘ⁿ) = 0` for every `n`, where `𝓘` is the ideal
> sheaf of the special fibre `E = X_s`.

```lean
theorem isZero_firstCohomology_exceptionalIdealPow_unconditional (n : ℕ) :
    IsZero (((moduleGlobalSections S.X).rightDerivedPlus 1).obj
      (S.exceptionalIdealPow n))
```

**`AlgebraicGeometry.RationalSingularitySituation.idealSheafGlobalSections_exceptionalIdealPow_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalIdealPowersExtra.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalIdealPowersExtra.lean#L109). The attribute's comment: “the conclusion H⁰(X, 𝓘ⁿ) = 𝔪ⁿ for all n, under the source's own further requirement that the special fibre be an effective Cartier divisor (hE)”.

> In Situation [Stacks, Tag 0B4W] with the special fibre `E = X_s` an effective Cartier
> divisor, `H⁰(X, 𝓘ⁿ) = 𝔪ⁿ` for every `n`: the global sections of `𝓘ⁿ` are exactly the image of
> `𝔪ⁿ` under the isomorphism `A ≅ Γ(X, 𝒪_X)`.

```lean
theorem idealSheafGlobalSections_exceptionalIdealPow_unconditional
    (hE : Stacks.Divisors.IsEffectiveCartierDivisor S.exceptionalIdeal) (n : ℕ) :
    idealSheafGlobalSections (S.exceptionalIdeal ^ n) =
      (S.maximalIdeal ^ n).map ((Scheme.ΓSpecIso (.of S.A)).inv ≫ S.f.appTop).hom
```

## Tag 0B4Z, a lemma

[Tag 0B4Z](https://stacks.math.columbia.edu/tag/0B4Z) in the Stacks Project.

**`AlgebraicGeometry.isNormal_blowUp_maximalIdeal_rationalSingularitySituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormal.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormal.lean#L255). The attribute's comment: “In Situation 0B4W the blowup of Spec(A) in the maximal ideal is normal”.

> In Situation [Stacks, Tag 0B4W] the blowup of `Spec(A)` in the maximal ideal is a normal
> scheme.

```lean
theorem isNormal_blowUp_maximalIdeal_rationalSingularitySituation
    (S : RationalSingularitySituation.{u}) :
    IsNormal (blowUp (Scheme.IdealSheafData.ofIdealTop
      (Ideal.map (Scheme.ΓSpecIso (.of S.A)).inv.hom S.maximalIdeal)))
```

## Tag 0B63, a lemma

[Tag 0B63](https://stacks.math.columbia.edu/tag/0B63) in the Stacks Project.

**`AlgebraicGeometry.isProper_exceptionalDivisorToCentre_residuePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurve.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurve.lean#L202). The attribute's comment: “clause (1): the exceptional curve is proper over the residue field”.

> **[Stacks, Tag 0B63] clause (1), properness.** The exceptional divisor of the blowup of the
> spectrum of a Noetherian local ring in its maximal ideal is proper over the residue field.

```lean
theorem isProper_exceptionalDivisorToCentre_residuePoint (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] :
    IsProper (exceptionalDivisorToCentre (residuePoint A))
```

**`AlgebraicGeometry.topologicalKrullDim_exceptionalDivisor_residuePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurve.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurve.lean#L283). The attribute's comment: “clause (1): the exceptional curve has dimension one”.

> **[Stacks, Tag 0B63] clause (1), the dimension.** The exceptional divisor of the blowup of
> the spectrum of a two-dimensional Noetherian local domain in its maximal ideal is a curve.

```lean
theorem topologicalKrullDim_exceptionalDivisor_residuePoint (A : Type u) [CommRing A]
    [IsLocalRing A] [IsDomain A] [IsNoetherianRing A] (hdim : ringKrullDim A = 2) :
    topologicalKrullDim (exceptionalDivisor (residuePoint A).ker) = 1
```

**`AlgebraicGeometry.isProper_and_topologicalKrullDim_eq_one_and_isCohenMacaulay_exceptionalDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurveCohenMacaulay.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurveCohenMacaulay.lean#L40). The attribute's comment: “clause (1)”.

> In Situation [Stacks, Tag 0B4W], let `X` be the blowup of `Spec(A)` in the maximal ideal and
> `E ⊆ X` its exceptional divisor. Then `E` is a proper Cohen–Macaulay curve over the residue field
> `κ`: the morphism `E ⟶ Spec(κ)` is proper, `E` has dimension one, and `E` is Cohen–Macaulay.
>
> Cohen–Macaulayness comes from the normality of `X` ([Stacks, Tag 0B4Z]): `E` is an effective
> Cartier divisor on a normal scheme, so it satisfies `(S₁)`, which for a scheme of dimension at
> most one is Cohen–Macaulayness.

```lean
theorem isProper_and_topologicalKrullDim_eq_one_and_isCohenMacaulay_exceptionalDivisor
    (S : RationalSingularitySituation.{u}) :
    IsProper (exceptionalDivisorToCentre (residuePoint S.A)) ∧
      topologicalKrullDim (exceptionalDivisor (residuePoint S.A).ker) = 1 ∧
      IsCohenMacaulay (exceptionalDivisor (residuePoint S.A).ker)
```

**`AlgebraicGeometry.isCohenMacaulay_exceptionalDivisor_residuePoint_of_situation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurveSupplement.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalCurveSupplement.lean#L66). The attribute's comment: “clause (1): in Situation 0B4W the exceptional curve of the blowup in the maximal ideal is Cohen-Macaulay”.

> **[Stacks, Tag 0B63] clause (1), Cohen–Macaulayness.** In Situation [Stacks, Tag 0B4W] the
> exceptional divisor of the blowup of `Spec(A)` in the maximal ideal is Cohen–Macaulay.
>
> The blowup is normal by [Stacks, Tag 0B4Z]
> (`AlgebraicGeometry.isNormal_blowUp_maximalIdeal_rationalSingularitySituation`), so the
> exceptional divisor satisfies Serre's condition `(S₁)`; in dimension at most one that is
> Cohen–Macaulayness.

```lean
theorem isCohenMacaulay_exceptionalDivisor_residuePoint_of_situation
    (S : RationalSingularitySituation.{u}) :
    IsCohenMacaulay (exceptionalDivisor (residuePoint S.A).ker)
```

**`AlgebraicGeometry.BlowUpDualizing.isZero_firstCohomology_curveTwistSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistCohomology.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistCohomology.lean#L254). The attribute's comment: “clause (4): H^1(E, O\_E(n)) = 0 for n >= 0”.

> **`H¹(E, 𝒪_E(n)) = 0` for every `n ≥ 0`.**
>
> From the restriction sequence `0 ⟶ ℐⁿ⁺¹ ⟶ ℐⁿ ⟶ i_*𝒪_E(n) ⟶ 0` and its long exact cohomology
> sequence: `H¹(X, ℐⁿ) = 0` is [Stacks, Tag 0B4Y] and `H²(X, ℐⁿ⁺¹) = 0` is
> `isZero_secondCohomology_exceptionalIdealPow`, so the term between them vanishes; and
> `H¹(X, i_*𝒪_E(n))` is `H¹(E, 𝒪_E(n))` because cohomology does not change along a closed
> immersion ([Stacks, Tag 01EX]).

```lean
theorem isZero_firstCohomology_curveTwistSheaf (n : ℕ) :
    IsZero (((Stacks.Cohomology.AffineBase.moduleGlobalSections
        (exceptionalCurve S.A)).rightDerived 1).obj (curveTwistSheaf S.A (n : ℤ)))
```

**`AlgebraicGeometry.BlowUpDualizing.one_le_invertibleCurveDegree_and_isRegularLocalRing_of_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistDegree.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistDegree.lean#L317). The attribute's comment: “clause (3)”.

> In Situation [Stacks, Tag 0B4W], with `E` the exceptional curve of the blowup of `Spec(A)` in
> the maximal ideal and `𝒪_E(1)` the restriction of `𝒪_X(1)`, `deg 𝒪_E(1) ≥ 1`, and equality holds
> only if `A` is a regular local ring.

```lean
theorem one_le_invertibleCurveDegree_and_isRegularLocalRing_of_eq_one :
    1 ≤ invertibleCurveDegree (ResidueField S.A)
        (exceptionalDivisorToCentre (Stacks.Blowup.residuePoint S.A))
        (le_of_eq (topologicalKrullDim_exceptionalDivisor_residuePoint S.A S.dimension_two))
        (curveTwistSheaf S.A 1) ∧
      (invertibleCurveDegree (ResidueField S.A)
          (exceptionalDivisorToCentre (Stacks.Blowup.residuePoint S.A))
          (le_of_eq (topologicalKrullDim_exceptionalDivisor_residuePoint S.A S.dimension_two))
          (curveTwistSheaf S.A 1) = 1 → IsRegularLocalRing S.A)
```

**`AlgebraicGeometry.BlowUpDualizing.nonempty_curveTwistSheafSections_iso_gradedPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistSections.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistSections.lean#L473). The attribute's comment: “clause (5): H^0(E, O\_E(n)) = m^n/m^(n+1) for every n >= 0”.

> **`H⁰(E, 𝒪_E(n)) = 𝔪ⁿ/𝔪ⁿ⁺¹` for every `n ≥ 0`.**
>
> The global sections of the `n`-th twist on the exceptional curve, read as a module over `A`
> through the structure morphism `E ⟶ X ⟶ Spec(A)`, are the `n`-th graded piece `𝔪ⁿ/𝔪ⁿ⁺¹` of the
> maximal-ideal filtration. The quotient is written by the submodule `𝔪·𝔪ⁿ` of `𝔪ⁿ`, which is
> `𝔪ⁿ⁺¹` by `AlgebraicGeometry.BlowUpDualizing.comap_subtype_eq_smul_top` and is the shape
> `Ideal.Cotangent` uses.
>
> This is read off the restriction sequence
> `0 ⟶ ℐⁿ⁺¹ ⟶ ℐⁿ ⟶ i_*𝒪_E(n) ⟶ 0` and its long exact cohomology sequence: `H¹(X, ℐⁿ⁺¹) = 0` makes
> `H⁰(X, ℐⁿ) ⟶ H⁰(X, i_*𝒪_E(n))` surjective, its kernel is the image of `H⁰(X, ℐⁿ⁺¹)`, and the
> first map of the sequence is the inclusion of ideal sheaves, so that image is `𝔪ⁿ⁺¹` inside
> `H⁰(X, ℐⁿ) = 𝔪ⁿ`. Both of the latter identifications are [Stacks, Tag 0B4Y]: `H¹(X, ℐⁿ⁺¹) = 0`
> and `H⁰(X, ℐⁿ) = 𝔪ⁿ`. **No `H²` is used**, and no hypothesis beyond Situation
> [Stacks, Tag 0B4W] is placed on `A`.
>
> The cohomology on `E` is compared with the cohomology of the direct image on `X` by
> [Stacks, Tag 01EZ] over the whole space
> (`Stacks.Cohomology.AffineBase.sectionsRestrictionIsoTop`), and the `A`-module structure is the
> restriction of scalars along `A ≅ Γ(X, 𝒪_X) ⟶ Γ(E, 𝒪_E)`, which
> `ModuleCat.restrictScalarsComp'App` splits into the two steps.

```lean
theorem nonempty_curveTwistSheafSections_iso_gradedPiece (n : ℕ) :
    Nonempty ((ModuleCat.restrictScalars
          ((Scheme.ΓSpecIso (.of S.A)).inv ≫
            (exceptionalImmersion S.A ≫ blowUpToBase (centre S.A)).appTop).hom).obj
        ((Stacks.Cohomology.AffineBase.moduleGlobalSections (exceptionalCurve S.A)).obj
          (curveTwistSheaf S.A (n : ℤ))) ≅
      ModuleCat.of S.A ((IsLocalRing.maximalIdeal S.A ^ n : Ideal S.A) ⧸
        (IsLocalRing.maximalIdeal S.A • ⊤ :
          Submodule S.A (IsLocalRing.maximalIdeal S.A ^ n : Ideal S.A))))
```

**`AlgebraicGeometry.isRelativelyVeryAmple_curveTwistSheaf_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistVeryAmple.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/ExceptionalTwistVeryAmple.lean#L82). The attribute's comment: “clause (2): the first twist on the exceptional curve is very ample over the residue field”.

> **[Stacks, Tag 0B63] clause (2).** For a Noetherian local ring `(A, 𝔪, κ)`, with `X` the
> blowup of `Spec(A)` in `𝔪` and `E ⊆ X` the exceptional divisor, the first twist `𝒪_E(1)` is very
> ample for the structure morphism `E ⟶ Spec(κ)`.
>
> Very ampleness is [Stacks, Tag 01VM],
> `Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple`: there are a quasi-coherent `𝒪_{Spec κ}`-module
> `F` and an immersion `E ⟶ 𝐏(F)` over `Spec(κ)` pulling `𝒪_{𝐏(F)}(1)` back to `𝒪_E(1)`.

```lean
theorem isRelativelyVeryAmple_curveTwistSheaf_one (A : Type u) [CommRing A] [IsLocalRing A]
    [IsNoetherianRing A] :
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple
      (exceptionalDivisorToCentre (residuePoint A)) (curveTwistSheaf A 1)
```

## Tag 0BBU, a lemma

[Tag 0BBU](https://stacks.math.columbia.edu/tag/0BBU) in the Stacks Project.

**`AlgebraicGeometry.RationalSingularitySituation.bijective_normalizedTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedDualizingTrace.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedDualizingTrace.lean#L105). The attribute's comment: “the trace H^0(X, omega\_X) -> omega\_A of the dualizing module normalized relative to omega\_A (Remark 0B4R: f^!(omega\_A) = omega\_X in degree zero) is an isomorphism; the canonical map f^*omega\_A -> omega\_X is normalizedPullbackMap”.

> **Stacks Project, Tag 0BBU.** In Situation [Stacks, Tag 0B4W], let `ω_A` be a dualizing
> module of `A` and let `ω_X` be the dualizing module of `X` normalized relative to `ω_A`
> ([Stacks, Remark 0B4R]: `ω_X[2] = f^!(ω_A[2])`, here the isomorphism `e : f^!(ω_A) ≅ ω_X` in
> degree zero). Then the trace map `H⁰(X, ω_X) ⟶ ω_A` is an isomorphism. The consequent canonical
> map `f^*ω_A ⟶ ω_X` is `AlgebraicGeometry.RationalSingularitySituation.normalizedPullbackMap`.
>
> The proof is duality in degree zero against `𝒪_X`: `H¹(X, 𝒪_X) = 0` because `A` defines a rational
> singularity, so `Hom(𝒪_X, ω_X) ⟶ Hom_A(Γ(X, 𝒪_X), ω_A)` is bijective, and its source is
> `H⁰(X, ω_X)` and its target `ω_A`, as `Γ(X, 𝒪_X) = A` ([Stacks, Tag 0B4Y]).

```lean
theorem bijective_normalizedTrace (_hωA : Stacks.Duality.IsDualizingRingModule S.A ωA)
    (e : (S.relativeDualizingComplex ωA).obj ≅
      (DerivedCategory.singleFunctor S.X.Modules 0).obj ωX) :
    Function.Bijective (S.normalizedTrace e).hom
```

**`AlgebraicGeometry.RationalSingularitySituation.normalizedPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedDualizingTrace.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/NormalizedDualizingTrace.lean#L141). The attribute's comment: “the canonical map f^*omega\_A -> omega\_X induced by the trace isomorphism, for the dualizing module normalized relative to omega\_A”.

> **Stacks Project, Tag 0BBU, the canonical map.** The map `f^*ω_A ⟶ ω_X` induced by the trace
> isomorphism of the normalized dualizing module: the adjunct, under
> `M ↦ f^*M̃ ⊣ ℱ ↦ H⁰(X, ℱ)` (`globalSectionsAdjunction`), of the inverse of the trace.

```lean
def normalizedPullbackMap (hωA : Stacks.Duality.IsDualizingRingModule S.A ωA)
    (e : (S.relativeDualizingComplex ωA).obj ≅
      (DerivedCategory.singleFunctor S.X.Modules 0).obj ωX) :
    (Scheme.Modules.pullback S.f).obj (tilde ωA) ⟶ ωX
```

## Tag 0B64, a lemma

[Tag 0B64](https://stacks.math.columbia.edu/tag/0B64) in the Stacks Project.

**`AlgebraicGeometry.BlowUpDualizing.nonempty_dualizingSheafOverField_iso_curveTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ExceptionalDualizingSheafIdentification.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ExceptionalDualizingSheafIdentification.lean#L232). The attribute's comment: “clause (1) in Situation 0B4W: for omega\_A a dualizing module for A and omega\_X the dualizing module of the blowup X of Spec(A) in the maximal ideal, normalized relative to omega\_A as in Remark 0B4R (DualizingNormalization: omega\_X dualizing with f^!(omega\_A) = omega\_X in degree zero), omega\_E = omega\_X|\_E tensor O\_E(-1), omega\_E the dualizing sheaf dualizingSheafOverField g of the exceptional curve E as a proper curve over kappa. The source's route, Lemmas 0AA4 and 0A9X, is followed: the adjunction formula and the normal sheaf O\_E(-1) give H^1(a(omega\_X)) = omega\_X|\_E tensor O\_E(-1), and the propagation of the normalization along g ; j = i ; f identifies H^1(a(omega\_X)) with dualizingSheafOverField g. The non-regularity of A is not used and not assumed (a generalization). Nothing is carried”.

> **[Stacks, Tag 0B64], clause (1).** In Situation [Stacks, Tag 0B4W] let `X` be the blowup of
> `Spec(A)` in the maximal ideal with exceptional divisor `i : E ⟶ X`, let `ω_A` be a dualizing
> module for `A` and let `ω_X` be the dualizing module of `X`, normalized relative to `ω_A` as in
> [Stacks, Remark 0B4R]. Then `ω_E = ω_X|_E ⊗ 𝒪_E(-1)`, where `ω_E` is the dualizing sheaf
> `Stacks.Duality.dualizingSheafOverField g` of `E` as a proper curve over the residue field `κ`.
>
> This splices `AlgebraicGeometry.BlowUpDualizing.nonempty_exceptionalDualizingModule_iso_curveTwist`
> (the adjunction formula, for the module `H¹(a(ω_X))`) with
> `AlgebraicGeometry.BlowUpDualizing.nonempty_exceptionalDualizingModule_iso_dualizingSheafOverField`
> (that module is the dualizing sheaf of `E` over `κ`).

```lean
theorem nonempty_dualizingSheafOverField_iso_curveTwist
    (ωA : ModuleCat.{u} S.A) (hωA : Stacks.Duality.IsDualizingRingModule S.A ωA)
    (ωX : (blowUpScheme S.A).Modules)
    (N : letI : IsLocallyNoetherian (rationalSingularitySituationBlowUp S).X :=
        isLocallyNoetherian_blowUpScheme S.A
      (rationalSingularitySituationBlowUp S).DualizingNormalization ωA ωX) :
    Nonempty (Stacks.Duality.dualizingSheafOverField
        (X := (cohenMacaulayCurveSituationExceptionalDivisor S).X)
        (cohenMacaulayCurveSituationExceptionalDivisor S).f ≅
      curveTwist S.A ((Scheme.Modules.pullback (exceptionalImmersion S.A)).obj ωX) (-1))
```

**`AlgebraicGeometry.BlowUpDualizing.epi_normalizedPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormalizedDualizingGeneration.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormalizedDualizingGeneration.lean#L324). The attribute's comment: “clause (3) in Situation 0B4W with A not regular: for omega\_A a dualizing module for A and omega\_X the dualizing module of the blowup X of Spec(A) in the maximal ideal, normalized relative to omega\_A as in Remark 0B4R (DualizingNormalization: omega\_X dualizing with f^!(omega\_A) = omega\_X in degree zero), the canonical map f^*omega\_A -> omega\_X of Tag 0BBU (normalizedPullbackMap) is surjective. The source's route: Tag 0B5H at E (via Tag 0E32 to kappa-bar, clause (2) of Tag 0B63 for very ampleness, clause (3) of Tag 0B63 for the degree) gives global generation of omega\_X|\_E = omega\_E(1) (clause (1)); H^1(X, omega\_X(1)) = 0 (clause (2), from that generation) lifts it to Gamma(X, omega\_X) = omega\_A; surjectivity is detected on the closed fibre. Nothing is carried”.

> **[Stacks, Tag 0B64], clause (3).** In Situation [Stacks, Tag 0B4W] assume `A` is not
> regular, let `ω_A` be a dualizing module for `A`, let `X` be the blowup of `Spec(A)` in the
> maximal ideal and let `ω_X` be the dualizing module of `X`, normalized relative to `ω_A` as in
> [Stacks, Remark 0B4R] (`DualizingNormalization`: `ω_X` is dualizing and `f^!(ω_A) ≅ ω_X` in
> degree zero). Then the canonical map `f^*ω_A ⟶ ω_X` of [Stacks, Tag 0BBU]
> (`AlgebraicGeometry.RationalSingularitySituation.normalizedPullbackMap`) is surjective.
>
> The source's proof: `ω_X|_E ≅ ω_E ⊗ 𝒪_E(1)` (clause (1)) is globally generated by
> [Stacks, Tag 0B5H], reduced to `κ̄` through [Stacks, Tag 0E32]
> (`CohenMacaulayCurveSituation.pullbackDualizingSheafOverFieldIso`); `H¹(X, ω_X(1)) = 0` lifts its
> generators to `Γ(X, ω_X) = ω_A`, and an epimorphism onto `ω_X` is detected on the closed
> fibre.

```lean
theorem epi_normalizedPullbackMap
    (hnot : ¬ IsRegularLocalRing S.A)
    (ωA : ModuleCat.{u} S.A) (hωA : Stacks.Duality.IsDualizingRingModule S.A ωA)
    (ωX : (blowUpScheme S.A).Modules)
    (N : letI : IsLocallyNoetherian (rationalSingularitySituationBlowUp S).X :=
        isLocallyNoetherian_blowUpScheme S.A
      (rationalSingularitySituationBlowUp S).DualizingNormalization ωA ωX) :
    letI : IsLocallyNoetherian (rationalSingularitySituationBlowUp S).X :=
      isLocallyNoetherian_blowUpScheme S.A
    Epi ((rationalSingularitySituationBlowUp S).normalizedPullbackMap hωA N.normalizedIso)
```

**`AlgebraicGeometry.BlowUpDualizing.isZero_firstCohomology_schemeTwist_of_dualizingNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormalizedDualizingGeneration.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/BlowUpNormalizedDualizingGeneration.lean#L354). The attribute's comment: “clause (2)”.

> **[Stacks, Tag 0B64], clause (2).** In Situation [Stacks, Tag 0B4W] assume `A` is not
> regular, let `ω_A` be a dualizing module for `A`, let `X` be the blowup of `Spec(A)` in the
> maximal ideal and let `ω_X` be the dualizing module of `X`, normalized relative to `ω_A` as in
> [Stacks, Remark 0B4R] (`DualizingNormalization`). Then `H¹(X, ω_X(n)) = 0` for every `n ≥ 0`.
>
> The source's proof: `ω_X|_E ≅ ω_E ⊗ 𝒪_E(1)` (clause (1)) is generated by its global sections by
> [Stacks, Tag 0B5H] (reduced to `κ̄` through [Stacks, Tag 0E32],
> `CohenMacaulayCurveSituation.pullbackDualizingSheafOverFieldIso`), so its twists `(ω_X|_E)(n)`,
> `n ≥ 0`, have no first cohomology (`isZero_firstCohomology_curveTwist_of_generatingSections`,
> from clause (4) of [Stacks, Tag 0B63]); the restriction sequence and the eventual vanishing of
> [Stacks, Tag 02O1] then give the vanishing on `X`
> (`isZero_firstCohomology_dualizingTwist_of_restrictionVanishing`).

```lean
theorem isZero_firstCohomology_schemeTwist_of_dualizingNormalization
    (hnot : ¬ IsRegularLocalRing S.A)
    (ωA : ModuleCat.{u} S.A) (hωA : Stacks.Duality.IsDualizingRingModule S.A ωA)
    (ωX : (blowUpScheme S.A).Modules)
    (N : letI : IsLocallyNoetherian (rationalSingularitySituationBlowUp S).X :=
        isLocallyNoetherian_blowUpScheme S.A
      (rationalSingularitySituationBlowUp S).DualizingNormalization ωA ωX)
    (n : ℕ) :
    IsZero (((cohomologyDeltaFunctor (blowUpScheme S.A)).functor 1).obj
      (schemeTwist S.A ωX n))
```

## Tag 0BBV, a lemma

[Tag 0BBV](https://stacks.math.columbia.edu/tag/0BBV) in the Stacks Project.

**`AlgebraicGeometry.exists_singularPointBlowupChain_isDualizingModule_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/InvertibleDualizingBlowupSequence.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalSingularities/InvertibleDualizingBlowupSequence.lean#L45).

> Let `A` be a local normal Nagata domain of dimension two which defines a rational singularity
> and has a dualizing complex. Then there is a finite sequence of blowups in singular closed points
> `X = Xₙ ⟶ … ⟶ X₁ ⟶ X₀ = Spec(A)` with every `Xᵢ` normal such that the dualizing module of `X` is
> an invertible `𝒪_X`-module.

```lean
theorem exists_singularPointBlowupChain_isDualizingModule_isInvertible
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A]
    (hN : IsNagataRing A) (hdim : ringKrullDim A = 2) (hrat : DefinesRationalSingularity A)
    (hdual : letI : IsNoetherianRing A := hN.1
      letI := HasDerivedCategory.standard (ModuleCat.{u} A)
      ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K) :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of A)),
      SingularPointBlowupChain IsNormal (Spec (.of A)) X f ∧
        ∃ _ : IsLocallyNoetherian X, ∃ ω : X.Modules, Stacks.Duality.IsDualizingModule ω ∧
          AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 ω
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.9, Tag 0B4V](https://stacks.math.columbia.edu/tag/0B4V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
