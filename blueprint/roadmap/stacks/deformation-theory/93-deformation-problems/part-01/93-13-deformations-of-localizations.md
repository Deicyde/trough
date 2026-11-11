---
declaration: section
origin: cited
lean: Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_localization, Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv, Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv_apply, Deformation.Examples.IsLocalizedExtension, Deformation.Examples.isSmooth_localizationFunctorData, Deformation.Examples.isSmooth_localizationFunctor, Deformation.Examples.bijective_differential_localizationFunctorData, Deformation.Examples.bijective_differential_localizationFunctor
statement: formalized
proof: formalized
---

# 93.13 Deformations of localizations

Section 93.13 of the Stacks Project, [Tag 0DZ6](https://stacks.math.columbia.edu/tag/0DZ6). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZ7, a lemma

[Tag 0DZ7](https://stacks.math.columbia.edu/tag/0DZ7) in the Stacks Project.

**`Deformation.hasFlatAlgebraLift_iff_hasFlatAlgebraLift_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FlatAlgebraLiftLocalizationNilpotent.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FlatAlgebraLiftLocalizationNilpotent.lean#L335). The attribute's comment: “`S⁻¹B` is any `C` with `IsLocalization S C`. `Spec(B) → Spec(A)` being syntomic at the point `𝔮` is read affinely as `∃ g ∉ 𝔮, A → B_g` syntomic, the characterization of Stacks 00SY and 01UE; `S ∩ 𝔮 = ∅` is `∀ s ∈ S, s ∉ 𝔮`. The published proof rests on Stacks 0DZ2, which is false; the proof here approximates a flat lift over the localized presentation by relation solutions over the polynomial presentation and corrects them one power of the kernel at a time (Artin-Rees plus Stacks 07M8 at every level). See the module docstring.”.

> **Stacks 0DZ7.** Let `A' → A` be a surjective map of Noetherian rings with nilpotent kernel,
> let `A → B` be a finite type flat ring map and let `S ⊆ B` be a multiplicative subset such that if
> `Spec(B) → Spec(A)` is not syntomic at `𝔮`, then `S ∩ 𝔮 = ∅`. Then `B` has a flat lift to `A'` if
> and only if `S⁻¹B` has a flat lift to `A'`.
>
> `Spec(B) → Spec(A)` is syntomic at the point `𝔮` exactly when `A → B_g` is syntomic for some
> `g ∉ 𝔮` (Stacks 00SY, 01UE); that is how the hypothesis `hS` reads the source's condition. The
> proof does not go through Stacks 0DZ2 (which is false); see the module documentation.

```lean
public theorem hasFlatAlgebraLift_iff_hasFlatAlgebraLift_localization
    (A' A B : Type u) [CommRing A'] [CommRing A] [CommRing B]
    [IsNoetherianRing A'] [IsNoetherianRing A] [Algebra A' A] [Algebra A B]
    (hsurjA : Function.Surjective (algebraMap A' A))
    (hnilA : IsNilpotent (RingHom.ker (algebraMap A' A)))
    [Algebra.FiniteType A B] [Module.Flat A B] (S : Submonoid B)
    (hS : ∀ q : Ideal B, q.IsPrime →
      (¬ ∃ g ∉ q, Algebra.Syntomic A (Localization.Away g)) → ∀ s ∈ S, s ∉ q)
    (C : Type u) [CommRing C] [Algebra B C] [IsLocalization S C] [Algebra A C]
    [IsScalarTower A B C] :
    HasFlatAlgebraLift A' A B ↔ HasFlatAlgebraLift A' A C
```

## Tag 0DZ8, a lemma

[Tag 0DZ8](https://stacks.math.columbia.edu/tag/0DZ8) in the Stacks Project.

**`Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/ClassesLocalizationEquiv.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/ClassesLocalizationEquiv.lean#L546). The attribute's comment: “localization equivalence”.

> **Stacks 0DZ8.** If a multiplicative subset `S` of a finite type algebra `B` over a field
> `k` is disjoint from every prime in the non-smooth locus of `B`, then localization at `S` is a
> bijection from the isomorphism classes of square-zero extensions of `B` by `N` to those of
> square-zero extensions of `S⁻¹B` by `S⁻¹N`.
>
> The companion lemma
> `Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv_apply` identifies the
> forward map with localization.

```lean
noncomputable def squareZeroAlgebraExtensionClassesLocalizationEquiv
    (k : Type uk) (B : Type uB) [Field k] [CommRing B] [Algebra k B]
    [Algebra.FiniteType k B] (S : Submonoid B)
    (hS : ∀ q : PrimeSpectrum B,
      ¬ Algebra.IsSmoothAt k q.asIdeal →
        Disjoint (S : Set B) (q.asIdeal : Set B))
    (N : Type uN) [AddCommGroup N] [Module B N] :
    SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB, uN,
        max uk (max uB uN)} (algebraExtensionProblem k B N) ≃
      SquareZeroExtensionProblem.CompatibleExtension.IsomorphismClasses.{uk, uk, uB,
        max uB uN, max uk (max uB uN)}
        (algebraExtensionProblem k (Localization S) (LocalizedModule S N))
```

**`Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/ClassesLocalizationEquiv.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/ClassesLocalizationEquiv.lean#L589). The attribute's comment: “forward map is localization”.

> **Stacks 0DZ8.** The forward map of
> `Deformation.Examples.squareZeroAlgebraExtensionClassesLocalizationEquiv` is localization of an
> extension at the inverse image of `S` in its middle ring.

```lean
theorem squareZeroAlgebraExtensionClassesLocalizationEquiv_apply
    (k : Type uk) (B : Type uB) [Field k] [CommRing B] [Algebra k B]
    [Algebra.FiniteType k B] (S : Submonoid B)
    (hS : ∀ q : PrimeSpectrum B,
      ¬ Algebra.IsSmoothAt k q.asIdeal →
        Disjoint (S : Set B) (q.asIdeal : Set B))
    (N : Type uN) [AddCommGroup N] [Module B N]
    (X : (algebraExtensionProblem k B N).CompatibleExtension.{max uk (max uB uN)}) :
    ∃ Y : (algebraExtensionProblem k (Localization S)
        (LocalizedModule S N)).CompatibleExtension.{max uk (max uB uN)},
      squareZeroAlgebraExtensionClassesLocalizationEquiv k B S hS N
          (Quotient.mk
            (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
              (algebraExtensionProblem k B N)) X) =
        Quotient.mk
          (SquareZeroExtensionProblem.CompatibleExtension.isomorphicSetoid
            (algebraExtensionProblem k (Localization S)
              (LocalizedModule S N))) Y ∧
      IsLocalizedExtension k B S N X Y
```

**`Deformation.Examples.IsLocalizedExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/LocalizedExtension.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationFirstOrder/LocalizedExtension.lean#L346). The attribute's comment: “the localization relation between two extensions”.

> **Stacks 0DZ8.** The extension `Y` of `S⁻¹B` is obtained from the extension `X` of `B` by
> localizing its middle ring at the inverse image of `S`: there is a map of the two middle rings
> which is such a localization, and which is compatible both with the quotient maps down to `B`
> and `S⁻¹B` and with the identifications of the two kernels with `N` and `S⁻¹N`.

```lean
def IsLocalizedExtension
    (k : Type uk) (B : Type uB) [Field k] [CommRing B] [Algebra k B]
    (S : Submonoid B) (N : Type uN) [AddCommGroup N] [Module B N]
    (X : (algebraExtensionProblem k B N).CompatibleExtension.{max uk (max uB uN)})
    (Y : (algebraExtensionProblem k (Localization S)
      (LocalizedModule S N)).CompatibleExtension.{max uk (max uB uN)}) : Prop
```

## Tag 0DZ9, a lemma

[Tag 0DZ9](https://stacks.math.columbia.edu/tag/0DZ9) in the Stacks Project.

**`Deformation.Examples.isSmooth_localizationFunctorData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationSmooth.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationSmooth.lean#L268). The attribute's comment: “the first conclusion, smoothness: the functor of Stacks 0DYS is smooth. Under the tag's own hypotheses: (1) is `Algebra.FiniteType k P` and (2) is `hsm`, smoothness of `Spec(P) → Spec(k)` at every point of `V(g)` for every `g` of `S`. Stated for an arbitrary functor datum of Stacks 0DYS, with no extra hypothesis on the datum. The criterion of Stacks 0DYP reduces it to surjectivity of the differential, which is `Deformation.Examples.bijective_differential_localizationFunctorData`, and to the correspondence of liftability, which is proved here in `Deformation.Examples.lifts_localizationFunctorData`”.

> **Stacks 0DZ9, the smoothness conclusion.** Let `k` be a field, `P` a finite type
> `k`-algebra and `S ⊆ P` a multiplicative subset such that `Spec(P) → Spec(k)` is smooth at
> every point of `V(g)` for every `g ∈ S`. The localization functor `𝓓_P ⟶ 𝓓_{S⁻¹P}` of
> **Stacks 0DYS** is smooth.

```lean
theorem isSmooth_localizationFunctorData [Algebra.FiniteType k P]
    (F : LocalizationFunctorData (Λ := Λ) (k := k) S)
    (hsm : ∀ g ∈ S, ∀ q : PrimeSpectrum P, g ∈ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth F.functor
```

**`Deformation.Examples.isSmooth_localizationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationSmooth.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationSmooth.lean#L285). The attribute's comment: “the first conclusion, smoothness, at the canonical localization functor `Deformation.Examples.localizationFunctor` of Stacks 0DYS. Under the tag's own hypotheses”.

> **Stacks 0DZ9, the smoothness conclusion, at the canonical localization functor.** This is
> `Deformation.Examples.isSmooth_localizationFunctorData` specialized to
> `Deformation.Examples.localizationFunctor`, the functor datum built in the proof of
> **Stacks 0DYS**.

```lean
theorem isSmooth_localizationFunctor [Algebra.FiniteType k P]
    (hsm : ∀ g ∈ S, ∀ q : PrimeSpectrum P, g ∈ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    IsSmooth (localizationFunctor (Λ := Λ) (k := k) S).functor
```

**`Deformation.Examples.bijective_differential_localizationFunctorData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationTangentSpace.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationTangentSpace.lean#L273). The attribute's comment: “the tangent-space assertion: the functor of Stacks 0DYS induces an isomorphism on tangent spaces. Under the tag's own hypotheses: (1) is `Algebra.FiniteType k P` and (2) is `hsm`, smoothness of `Spec(P) → Spec(k)` at every point of `V(g)` for every `g` of `S`. Stated for an arbitrary functor datum of Stacks 0DYS, with no extra hypothesis on the datum”.

> Let `k` be a field, `P` a finite type `k`-algebra and `S ⊆ P` a multiplicative subset such
> that `Spec(P) → Spec(k)` is smooth at every point of `V(g)` for every `g ∈ S`. Then the
> localization functor `𝓓_P ⟶ 𝓓_{S⁻¹P}` of **Stacks 0DYS**, given by any
> `LocalizationFunctorData`, induces a bijection on tangent spaces.
>
> The proof is the source's: the family of extension classes of **Stacks 0DY3** is a bijection of
> each tangent space with a first Ext group of the naive cotangent complex, by
> `Deformation.Examples.bijective_tangentExtClass`; the functor is compatible with those classes
> through the two comparison maps of **Stacks 0GPV**, by
> `Deformation.Examples.squareZeroFiberExtClass_localization`; the bijection of **Stacks 0DZ8**
> is compatible with the same two maps, by
> `Deformation.Examples.naiveCotangentExtOneMap_localizationCoefficientMap`; and restriction along
> `P → S⁻¹P` is injective, by
> `Stacks.Deformation.injective_naiveCotangentExtOneTowerMap_isLocalization`.

```lean
public theorem bijective_differential_localizationFunctorData
    [Algebra.FiniteType k P]
    (F : LocalizationFunctorData (Λ := Λ) (k := k) S)
    (hsm : ∀ g ∈ S, ∀ q : PrimeSpectrum P, g ∈ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (Localization S))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection F.functor)
```

**`Deformation.Examples.bijective_differential_localizationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/LocalizationTangentSpace.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/LocalizationTangentSpace.lean#L332). The attribute's comment: “the tangent-space assertion: the functor induces an isomorphism on tangent spaces, at the canonical localization functor `Deformation.Examples.localizationFunctor` of Stacks 0DYS. Under the tag's own hypotheses”.

> Under the hypotheses of `Deformation.Examples.bijective_differential_localizationFunctorData`,
> the canonical localization functor `Deformation.Examples.localizationFunctor`, the functor datum
> built in the proof of **Stacks 0DYS**, induces a bijection on tangent spaces.

```lean
public theorem bijective_differential_localizationFunctor [Algebra.FiniteType k P]
    (hsm : ∀ g ∈ S, ∀ q : PrimeSpectrum P, g ∈ q.asIdeal → Algebra.IsSmoothAt k q.asIdeal) :
    Function.Bijective (differential (𝓕 := ringDeformationBasedCategory Λ k P)
      (𝓖 := ringDeformationBasedCategory Λ k (Localization S))
      isCofiberedInGroupoids_ringDeformationProjection
      isCofiberedInGroupoids_ringDeformationProjection
      (localizationFunctor (Λ := Λ) (k := k) S).functor)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.13, Tag 0DZ6](https://stacks.math.columbia.edu/tag/0DZ6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
