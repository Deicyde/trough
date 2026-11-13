---
declaration: section
origin: cited
lean: AlgebraicGeometry.RationalDoublePointSituation, MvPolynomial.eq_smul_sq_affineLinear_of_mem_ideal_sq, AlgebraicGeometry.exists_singularPointBlowupChain_isRegular_of_definesRationalSingularity
statement: formalized
proof: formalized
---

# 54.12 Rational double points

Section 54.12 of the Stacks Project, [Tag 0BGB](https://stacks.math.columbia.edu/tag/0BGB). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BGC, a situation

[Tag 0BGC](https://stacks.math.columbia.edu/tag/0BGC) in the Stacks Project.

**`AlgebraicGeometry.RationalDoublePointSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/Situation.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/Situation.lean#L48).

> **Stacks Project, Tag 0BGC.** A Nagata local normal domain of dimension two which defines a
> rational singularity, whose completion is normal, which is Gorenstein, and which is not
> regular.

```lean
structure RationalDoublePointSituation
```

## Tag 0BGD, a lemma

[Tag 0BGD](https://stacks.math.columbia.edu/tag/0BGD) in the Stacks Project.

**`MvPolynomial.eq_smul_sq_affineLinear_of_mem_ideal_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/Basic/QuadraticInIdealSquare.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/Basic/QuadraticInIdealSquare.lean#L335).

> A nonzero quadratic polynomial in the square of an ideal `I ⊆ κ[x, y]`, where `I`
> has colength greater than one, is a scalar multiple of the square of an affine linear
> polynomial.

```lean
theorem eq_smul_sq_affineLinear_of_mem_ideal_sq
    {k : Type*} [Field k] (I : Ideal (MvPolynomial (Fin 2) k))
    (a b c d e f : k)
    (hnonzero : a ≠ 0 ∨ b ≠ 0 ∨ c ≠ 0 ∨ d ≠ 0 ∨ e ≠ 0 ∨ f ≠ 0)
    (hmem : C a + C b * X 0 + C c * X 1 + C d * X 0 ^ 2 +
      C e * X 0 * X 1 + C f * X 1 ^ 2 ∈ I ^ 2)
    (hcolength : 1 < Module.rank k (MvPolynomial (Fin 2) k ⧸ I)) :
    ∃ j g h i : k,
      C a + C b * X 0 + C c * X 1 + C d * X 0 ^ 2 +
          C e * X 0 * X 1 + C f * X 1 ^ 2 =
        C j * (C g + C h * X 0 + C i * X 1) ^ 2
```

## Tag 0BGE, a lemma

[Tag 0BGE](https://stacks.math.columbia.edu/tag/0BGE) in the Stacks Project.

**`AlgebraicGeometry.exists_singularPointBlowupChain_isRegular_of_definesRationalSingularity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/RationalDoublePointResolutionTag.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/RationalDoublePoints/RationalDoublePointResolutionTag.lean#L43).

> Let `(A, 𝔪, κ)` be a local normal Nagata domain of dimension two which defines a rational
> singularity, whose completion is normal, and which is Gorenstein. Then there exists a finite
> sequence of blowups in singular closed points `Xₙ → Xₙ₋₁ → ⋯ → X₁ → X₀ = Spec(A)` such that `Xₙ`
> is regular and such that each scheme `Xᵢ` of the sequence is normal with finitely many singular
> points of the same type: the local ring at each singular point is again the ring of a Situation
> [Stacks, Tag 0BGC].

```lean
theorem exists_singularPointBlowupChain_isRegular_of_definesRationalSingularity
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNormalDomain A] (hnagata : IsNagataRing A)
    (hdim : ringKrullDim A = 2) (hrational : DefinesRationalSingularity A)
    (hcompletion : IsNormalDomain (AdicCompletion (maximalIdeal A) A))
    (hgorenstein : letI : IsNoetherianRing A := hnagata.isNoetherianRing
      Dualizing.IsGorensteinLocalRing A) :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ Spec (.of A)),
      SingularPointBlowupChain (fun W => IsNormal W ∧ (singularLocus W).Finite ∧
          ∀ w ∈ singularLocus W, ∃ S : RationalDoublePointSituation.{u},
            Nonempty (S.A ≃+* W.presheaf.stalk w))
        (Spec (.of A)) Y f ∧ IsRegular Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.12, Tag 0BGB](https://stacks.math.columbia.edu/tag/0BGB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
