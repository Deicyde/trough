---
declaration: section
origin: cited
lean: Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_henselization, Stacks.Deformation.exists_squareZeroAlgebraExtensionClassesHenselizationEquiv, Deformation.Examples.bijective_differential_henselizationFunctorData, Deformation.Examples.bijective_differential_henselizationFunctor, Deformation.Examples.isSmooth_henselizationFunctorData, Deformation.Examples.isSmooth_henselizationFunctor, Stacks.Deformation.exists_squareZeroAlgebraExtensionClassesHenselizationTangentEquiv
statement: formalized
proof: formalized
---

# 93.14 Deformations of henselizations

Section 93.14 of the Stacks Project, [Tag 0DZA](https://stacks.math.columbia.edu/tag/0DZA). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DZB, a lemma

[Tag 0DZB](https://stacks.math.columbia.edu/tag/0DZB) in the Stacks Project.

**`Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatAlgebraLiftHenselizationNilpotent.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/FlatAlgebraLiftHenselizationNilpotent.lean#L417). The attribute's comment: “The henselization of the pair `(B, 𝔟)` is any `Bʰ` with `(Bʰ, 𝔟Bʰ)` henselian (`hhens`) and initial among henselian pairs under `(B, 𝔟)` (`huniv`), which is the defining universal property of the henselization (Stacks 0A02). The library's construction `henselization B b` has both properties (`henselianPair_henselization`, `henselization_universalProperty`), and the statement for it is `Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_canonicalHenselization`. The syntomic hypothesis is the affine reading: the complement of `V(𝔟)` is covered by the `D(h)`, `h ∈ 𝔟`, and syntomy is local on the source. Both published proofs rest on Stacks 0DZ2, which is false; the proof here approximates a flat lift over the henselized presentation by solutions over the polynomial presentation and corrects them one power of the kernel at a time (Artin-Rees plus Stacks 07M8 at every level). See the module docstring.”.

> **Stacks 0DZB.** Let `A' → A` be a surjective map of Noetherian rings with nilpotent kernel,
> let `A → B` be a finite type flat ring map and let `𝔟 ⊆ B` be an ideal such that
> `Spec(B) → Spec(A)` is syntomic on the complement of `V(𝔟)`, that is `A → B_h` is syntomic for
> every `h ∈ 𝔟`. Let `(Bʰ, 𝔟ʰ)` be the henselization of the pair `(B, 𝔟)`. Then `B` has a flat lift
> to `A'` if and only if `Bʰ` has a flat lift to `A'`.
>
> The proof does not go through Stacks 0DZ2 (which is false); see the module documentation.

```lean
public theorem hasFlatAlgebraLift_iff_hasFlatAlgebraLift_henselization
    (A' A B : Type u) [CommRing A'] [CommRing A] [CommRing B]
    [IsNoetherianRing A'] [IsNoetherianRing A] [Algebra A' A] [Algebra A B]
    (hsurjA : Function.Surjective (algebraMap A' A))
    (hnilA : IsNilpotent (RingHom.ker (algebraMap A' A)))
    [Algebra.FiniteType A B] [Module.Flat A B] (b : Ideal B)
    (hsyn : ∀ h ∈ b, Algebra.Syntomic A (Localization.Away h))
    (Bh : Type u) [CommRing Bh] [Algebra B Bh] [Algebra A Bh] [IsScalarTower A B Bh]
    (hhens : HenselianPair Bh (b.map (algebraMap B Bh)))
    (huniv : ∀ (D : Type u) (_ : CommRing D) (K : Ideal D), HenselianPair D K →
      ∀ f : B →+* D, b ≤ K.comap f →
        ∃! g : Bh →+* D, g.comp (algebraMap B Bh) = f ∧
          b.map (algebraMap B Bh) ≤ K.comap g) :
    HasFlatAlgebraLift A' A B ↔ HasFlatAlgebraLift A' A Bh
```

## Tag 0DZC, a lemma

[Tag 0DZC](https://stacks.math.columbia.edu/tag/0DZC) in the Stacks Project.

**`Stacks.Deformation.exists_squareZeroAlgebraExtensionClassesHenselizationEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationDeformation.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/HenselizationDeformation.lean#L78).

> **Stacks 0DZC.** Let `k` be a field, `B` a finite type `k`-algebra and `J ⊆ B` an ideal
> containing the non-smooth locus of `B` over `k` in its vanishing locus, and let `(Bʰ, Jʰ)` be
> the henselization of the pair `(B, J)`. For a `B`-module `N` with `Nʰ = Bʰ ⊗_B N` there is a
> bijection between the isomorphism classes of square-zero extensions of `B` by `N` and those of
> `Bʰ` by `Nʰ`, namely the one inducing extension of scalars along `B → Bʰ` on the groups
> `Ext¹_B(NL_{B/k}, N)` and `Ext¹_{Bʰ}(NL_{Bʰ/k}, Nʰ)` that classify those classes.

```lean
public theorem exists_squareZeroAlgebraExtensionClassesHenselizationEquiv
    (k : Type uk) [Field k] (B : Type uB) [CommRing B] [Algebra k B]
    [Algebra.FiniteType k B]
    (J : Ideal B)
    (hsmooth : ∀ q : PrimeSpectrum B, ¬ Algebra.IsSmoothAt k q.asIdeal → J ≤ q.asIdeal)
    (N : Type uN) [AddCommGroup N] [Module B N]
    (Bh : Type uB) [CommRing Bh] [Algebra B Bh] [Algebra k Bh] [IsScalarTower k B Bh]
    (hhens : HenselianPair Bh (J.map (algebraMap B Bh)))
    (huniv : ∀ (C : Type uB) (_ : CommRing C) (JC : Ideal C), HenselianPair C JC →
      ∀ f : B →+* C, J ≤ JC.comap f →
        ∃! g : Bh →+* C, g.comp (algebraMap B Bh) = f ∧
          J.map (algebraMap B Bh) ≤ JC.comap g) :
    ∃ e : SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uN,
          max uB uN} (algebraExtensionProblem k B N) ≃
        SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB,
          max uB uN, max uB uN} (algebraExtensionProblem k Bh (Bh ⊗[B] N)),
      ∀ x, extOneCokernelHenselizationFlatBaseChangeEquiv.{uk, uB, uN} k B N Bh J hhens huniv
              (extCokernelIso k Bh (Bh ⊗[B] N)
                (squareZeroAlgebraExtensionClassesEquivExtOne k Bh (Bh ⊗[B] N) (e x)))
            = extCokernelIso k B N (squareZeroAlgebraExtensionClassesEquivExtOne k B N x)
                ⊗ₜ[B] (1 : Bh)
```

## Tag 0DZD, a lemma

[Tag 0DZD](https://stacks.math.columbia.edu/tag/0DZD) in the Stacks Project.

**`Deformation.Examples.bijective_differential_henselizationFunctorData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/HenselizationDifferential.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/HenselizationDifferential.lean#L446). The attribute's comment: “the second conclusion, the tangent-space assertion, for the map INDUCED by the functor of Stacks 0DYT: `Deformation.differential` of that functor is bijective, the tangent spaces being those of Stacks 06IH carried by the two deformation categories. Under the tag's own hypotheses and no others: (1) is `Algebra.FiniteType k P` and (2) is `hsm`, smoothness of `Spec(P) -> Spec(k)` at every prime outside `V(J)`. Stated for an arbitrary functor datum of Stacks 0DYT, with no extra hypothesis on the datum. The inputs are the classification of Stacks 0GPT through Stacks 0DY3, the comparison criterion of Stacks 0GPV, the coefficient half of Stacks 0DZC and injectivity of restriction along `P -> P^h`”.

> **Stacks 0DZD, the tangent-space conclusion, for the map induced by the functor.** Let `k`
> be a field, `P` a finite type `k`-algebra and `J ⊆ P` an ideal such that `Spec(P) → Spec(k)` is
> smooth on the complement of `V(J)`. The henselization functor `𝓓_P ⟶ 𝓓_{Pʰ}` of **Stacks 0DYT**
> induces a bijection on tangent spaces.
>
> The proof is the source's: the family of extension classes of **Stacks 0DY3** is a bijection of
> each tangent space with a first Ext group of the naive cotangent complex, by
> `Deformation.Examples.bijective_tangentExtClass`; the functor is compatible with those classes
> through the two comparison maps of **Stacks 0GPV**, by
> `Deformation.Examples.squareZeroFiberExtClass_henselization`; the coefficient comparison is
> bijective by the henselization half of **Stacks 0DZC**, in the form
> `Deformation.Examples.bijective_naiveCotangentExtOneMap_tensorCoefficientMap`; and restriction
> along `P → Pʰ` is injective, by
> `Stacks.Deformation.injective_naiveCotangentExtOneTowerMap_henselization`.

```lean
public theorem bijective_differential_henselizationFunctorData [Algebra.FiniteType k P]
    (F : HenselizationFunctorData (Λ := Λ) (k := k) (P := P) J)
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (henselization P J : Type w))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection F.functor)
```

**`Deformation.Examples.bijective_differential_henselizationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/HenselizationDifferential.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/HenselizationDifferential.lean#L485). The attribute's comment: “the second conclusion, the tangent-space assertion for the map induced by the functor, at the canonical henselization functor `Deformation.Examples.henselizationFunctor` of Stacks 0DYT. Under the tag's own hypotheses and no others”.

> **Stacks 0DZD, the tangent-space conclusion, at the canonical henselization functor.** This
> is `Deformation.Examples.bijective_differential_henselizationFunctorData` specialized to
> `Deformation.Examples.henselizationFunctor`, the functor datum built in the proof of
> **Stacks 0DYT**.

```lean
public theorem bijective_differential_henselizationFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (henselization P J : Type w))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection
      (henselizationFunctor (Λ := Λ) (k := k) J).functor)
```

**`Deformation.Examples.isSmooth_henselizationFunctorData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/HenselizationSmooth.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/HenselizationSmooth.lean#L230). The attribute's comment: “the first conclusion, smoothness: the functor of Stacks 0DYT is smooth. Under the tag's own hypotheses and no others: (1) is `Algebra.FiniteType k P` and (2) is `hsm`, smoothness of `Spec(P) -> Spec(k)` at every prime outside `V(J)`. Stated for an arbitrary functor datum of Stacks 0DYT, with no extra hypothesis on the datum. The criterion of Stacks 0DYP reduces it to surjectivity of the differential, which is `Deformation.Examples.bijective_differential_henselizationFunctorData`, and to the correspondence of liftability, which is proved here in `Deformation.Examples.lifts_henselizationFunctorData` -- that is Stacks 0DZB, which Stacks 0DYP needs only across small extensions, whose kernel is square-zero, so the form used is `Deformation.hasFlatAlgebraLift_of_hasFlatAlgebraLift_henselization_of_sqZero` and NO `h0DZ2`-style hypothesis is carried”.

> **Stacks 0DZD, the smoothness conclusion.** Let `k` be a field, `P` a finite type
> `k`-algebra and `J ⊆ P` an ideal such that `Spec(P) → Spec(k)` is smooth on the complement of
> `V(J)`. The henselization functor `𝓓_P ⟶ 𝓓_{Pʰ}` of **Stacks 0DYT** is smooth.

```lean
public theorem isSmooth_henselizationFunctorData [Algebra.FiniteType k P]
    (F : HenselizationFunctorData (Λ := Λ) (k := k) (P := P) J)
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth F.functor
```

**`Deformation.Examples.isSmooth_henselizationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/HenselizationSmooth.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/HenselizationSmooth.lean#L249). The attribute's comment: “the first conclusion, smoothness, at the canonical henselization functor `Deformation.Examples.henselizationFunctor` of Stacks 0DYT. Under the tag's own hypotheses and no others”.

> **Stacks 0DZD, the smoothness conclusion, at the canonical henselization functor.** This is
> `Deformation.Examples.isSmooth_henselizationFunctorData` specialized to
> `Deformation.Examples.henselizationFunctor`, the functor datum built in the proof of
> **Stacks 0DYT**.

```lean
public theorem isSmooth_henselizationFunctor [Algebra.FiniteType k P]
    (hsm : ∀ q : PrimeSpectrum P, ¬ J ≤ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth (henselizationFunctor (Λ := Λ) (k := k) J).functor
```

**`Stacks.Deformation.exists_squareZeroAlgebraExtensionClassesHenselizationTangentEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationTangentSpace.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Henselian/HenselizationTangentSpace.lean#L215). The attribute's comment: “ONLY the second conclusion, that the functor of Stacks 0DYT induces an isomorphism on tangent spaces -- and that in the form the source's own proof produces it, as the case `N = B` of Stacks 0DZC: the tangent spaces are the groups `Ext¹_B(NL_{B/k}, B)` and `Ext¹_{Bʰ}(NL_{Bʰ/k}, Bʰ ⊗_B B)` of Stacks 0DY3, which classify isomorphism classes of square-zero extensions by Stacks 0GPT, and it is those classes the bijection is between. That the bijection is the map INDUCED by the functor of Stacks 0DYT is not established: no naturality comparing `Deformation.Examples.henselizationFunctor` with the classification of Stacks 0GPT is formalized. No hypothesis the source does not have is carried: Stacks 0DZC is proved outright, base-change input and all -- Stacks 0D08, Stacks 0GPY and flat base change of the conormal cokernel for the comparison of the two Ext groups, and Stacks 00S1 for the J-power torsion of `Ext¹_B(NL_{B/k}, N)`. The FIRST conclusion, that the functor is smooth, is NOT proved at all: it rests on Stacks 0DZ2 through Stacks 0DZB, and the nilpotent devissage needed for 0DZ2 is refuted under 0DZ2's own hypotheses -- it would need `Ext¹` to be power torsion, whereas local liftability kills only the `Ext²` obstruction. See the implementation notes.”.

> **The case `N = B` of Stacks 0DZC, in the form this file's Ext comparison produces it.**
> Let `k` be a field, `B` a finite type `k`-algebra and `J ⊆ B` an ideal containing the non-smooth
> locus of `B` over `k` in its vanishing locus, and let `(Bʰ, Jʰ)` be the henselization of the
> pair `(B, J)`.  Then the isomorphism classes of square-zero extensions of `B` by `B` are in
> bijection with those of `Bʰ` by `Bʰ ⊗_B B`, compatibly with extension of scalars along
> `B → Bʰ` on the groups `Ext¹_B(NL_{B/k}, B)` and `Ext¹_{Bʰ}(NL_{Bʰ/k}, Bʰ ⊗_B B)` that
> classify them.
>
> By Stacks 0DY3 those two groups are the tangent spaces of the deformation categories `Def_B`
> and `Def_{Bʰ}`.  The tangent-space conclusion of Stacks 0DZD itself is registered on
> `Deformation.Examples.bijective_differential_henselizationFunctorData`, for the map the functor
> of Stacks 0DYT induces; see the section note above for why the attribute is not here.

```lean
public theorem exists_squareZeroAlgebraExtensionClassesHenselizationTangentEquiv
    (J : Ideal B)
    (hsmooth : ∀ q : PrimeSpectrum B, ¬ Algebra.IsSmoothAt k q.asIdeal → J ≤ q.asIdeal)
    (Bh : Type uB) [CommRing Bh] [Algebra B Bh] [Algebra k Bh] [IsScalarTower k B Bh]
    (hhens : HenselianPair Bh (J.map (algebraMap B Bh)))
    (huniv : ∀ (C : Type uB) (_ : CommRing C) (JC : Ideal C), HenselianPair C JC →
      ∀ f : B →+* C, J ≤ JC.comap f →
        ∃! g : Bh →+* C, g.comp (algebraMap B Bh) = f ∧
          J.map (algebraMap B Bh) ≤ JC.comap g) :
    ∃ e : SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uB,
          uB} (algebraExtensionProblem k B B) ≃
        SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uB,
          uB} (algebraExtensionProblem k Bh (Bh ⊗[B] B)),
      ∀ x, extOneCokernelHenselizationFlatBaseChangeEquiv.{uk, uB, uB} k B B Bh J hhens huniv
              (extCokernelIso k Bh (Bh ⊗[B] B)
                (squareZeroAlgebraExtensionClassesEquivExtOne k Bh (Bh ⊗[B] B) (e x)))
            = extCokernelIso k B B (squareZeroAlgebraExtensionClassesEquivExtOne k B B x)
                ⊗ₜ[B] (1 : Bh)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.14, Tag 0DZA](https://stacks.math.columbia.edu/tag/0DZA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
