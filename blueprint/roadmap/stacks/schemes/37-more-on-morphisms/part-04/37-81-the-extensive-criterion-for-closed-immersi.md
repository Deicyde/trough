---
declaration: section
origin: cited
lean: AlgebraicGeometry.isClosedImmersion_iff_lifts_injective_specMap, CategoryTheory.mem_essImage_of_unit_isSplitMono, AlgebraicGeometry.Spec.reflective, AlgebraicGeometry.ΓSpec.adjunction_unit_app, AlgebraicGeometry.essImage_Spec, AlgebraicGeometry.ker_toSpecΓ_eq_bot, AlgebraicGeometry.eq_bot_of_le_ker_toSpecΓ, AlgebraicGeometry.toSpecΓ_app_injective
statement: formalized
proof: formalized
---

# 37.81 The extensive criterion for closed immersions

Section 37.81 of the Stacks Project, [Tag 0H2N](https://stacks.math.columbia.edu/tag/0H2N). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H2P, a lemma

[Tag 0H2P](https://stacks.math.columbia.edu/tag/0H2P) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_iff_lifts_injective_specMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/Affine.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/Affine.lean#L180).

> An affine morphism is a closed immersion exactly when maps out of spectra lift
> against every injective map of commutative rings.

```lean
theorem isClosedImmersion_iff_lifts_injective_specMap
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y) :
    IsClosedImmersion f ↔
      ∀ (A B : Type u) [CommRing A] [CommRing B] (ψ : A →+* B),
        Function.Injective ψ →
        ∀ (g : Spec (.of B) ⟶ X) (h : Spec (.of A) ⟶ Y),
          (Spec.map (CommRingCat.ofHom ψ) ≫ h = g ≫ f) →
          ∃ l : Spec (.of A) ⟶ X,
            (Spec.map (CommRingCat.ofHom ψ) ≫ l = g) ∧ (l ≫ f = h)
```

## Tag 0H2Q, a lemma

[Tag 0H2Q](https://stacks.math.columbia.edu/tag/0H2Q) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.mem_essImage_of_unit_isSplitMono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.mem_essImage_of_unit_isSplitMono#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch37.lean#L60) (StacksFrontier): “a retraction of the unit X → Spec Γ(X, 𝒪_X) puts X in Spec's essential image”.
- [`AlgebraicGeometry.Spec.reflective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Spec.reflective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch37.lean#L62) (StacksFrontier): “Spec is reflective with unit X.toSpecΓ”.
- [`AlgebraicGeometry.ΓSpec.adjunction_unit_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.ΓSpec.adjunction_unit_app#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch37.lean#L63) (StacksFrontier): “the unit is X.toSpecΓ”.
- [`AlgebraicGeometry.essImage_Spec`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.essImage_Spec#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch37.lean#L64) (StacksFrontier): “the essential image of Spec is the affine schemes”.

## Tag 0H2R, a lemma

[Tag 0H2R](https://stacks.math.columbia.edu/tag/0H2R) in the Stacks Project.

**`AlgebraicGeometry.ker_toSpecΓ_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean#L43). The attribute's comment: “the largest quasi-coherent submodule of `ker f^♯` is zero”.

> The largest quasi-coherent `𝒪_S`-module contained in the kernel of
> `f^♯ : 𝒪_S ⟶ f_* 𝒪_X`, for `f : X ⟶ S = Spec Γ(X, 𝒪_X)` the canonical morphism, is zero.

```lean
theorem ker_toSpecΓ_eq_bot : X.toSpecΓ.ker = ⊥
```

**`AlgebraicGeometry.eq_bot_of_le_ker_toSpecΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean#L54). The attribute's comment: “the largest quasi-coherent submodule of `ker f^♯` is zero, universal form”.

> A quasi-coherent ideal sheaf on `S = Spec Γ(X, 𝒪_X)` whose sections over every affine open are
> killed by `f^♯` is zero.

```lean
theorem eq_bot_of_le_ker_toSpecΓ {I : (Spec Γ(X, ⊤)).IdealSheafData}
    (hI : ∀ U, I.ideal U ≤ RingHom.ker (X.toSpecΓ.app U).hom) : I = ⊥
```

**`AlgebraicGeometry.toSpecΓ_app_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean#L68). The attribute's comment: “if `X` is quasi-compact then `f^♯` is injective”.

> If `X` is quasi-compact then `f^♯ : 𝒪_S ⟶ f_* 𝒪_X` is injective, for
> `f : X ⟶ S = Spec Γ(X, 𝒪_X)` the canonical morphism: it is injective on the sections over every
> open of `S`.

```lean
theorem toSpecΓ_app_injective [CompactSpace X] (U : (Spec Γ(X, ⊤)).Opens) :
    Function.Injective (X.toSpecΓ.app U)
```

**`AlgebraicGeometry.isDominant_toSpecΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/CanonicalMorphism.lean#L74). The attribute's comment: “if `X` is quasi-compact then `f` is dominant”.

> If `X` is quasi-compact then the canonical morphism `X ⟶ Spec Γ(X, 𝒪_X)` is dominant.

```lean
theorem isDominant_toSpecΓ [CompactSpace X] : IsDominant X.toSpecΓ
```

## Tag 0H2S, a lemma

[Tag 0H2S](https://stacks.math.columbia.edu/tag/0H2S) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_iff_lifts_injective_specMap_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/QuasiCompact.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ClosedImmersionCriterion/QuasiCompact.lean#L117).

> A quasi-compact scheme morphism is a closed immersion exactly when maps out of
> spectra lift against every injective homomorphism of commutative rings.

```lean
public theorem isClosedImmersion_iff_lifts_injective_specMap_of_quasiCompact
    {X Y : Scheme.{u}} (f : X ⟶ Y) [QuasiCompact f] :
    IsClosedImmersion f ↔
      ∀ (A B : Type u) [CommRing A] [CommRing B] (ψ : A →+* B),
      Function.Injective ψ →
      ∀ (g : Spec (.of B) ⟶ X) (h : Spec (.of A) ⟶ Y),
        (Spec.map (CommRingCat.ofHom ψ) ≫ h = g ≫ f) →
        ∃ l : Spec (.of A) ⟶ X,
          (Spec.map (CommRingCat.ofHom ψ) ≫ l = g) ∧ (l ≫ f = h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.81, Tag 0H2N](https://stacks.math.columbia.edu/tag/0H2N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
