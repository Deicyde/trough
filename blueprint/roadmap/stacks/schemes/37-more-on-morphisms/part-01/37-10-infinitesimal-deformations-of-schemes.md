---
declaration: section
origin: cited
lean: Stacks.Thickenings.flat_and_isPullback_of_isIso_firstOrderThickeningConormalSheafMap, Stacks.Thickenings.flat_and_isPullback_iff_isIso_firstOrderThickeningConormalSheafMap, Stacks.Thickenings.epi_firstOrderThickeningConormalSheafMap, Stacks.Thickenings.isIso_firstOrderThickeningConormalSheafMap, Ideal.bijective_tensorSMulHomToKer_iff, Ideal.bijective_fibreTensorSMulHomToKer_iff, AlgebraicGeometry.flat_of_flat_reduction, AlgebraicGeometry.flatAt_target_of_flat_reduction
statement: formalized
proof: formalized
---

# 37.10 Infinitesimal deformations of schemes

Section 37.10 of the Stacks Project, [Tag 063X](https://stacks.math.columbia.edu/tag/063X). 6 tags here are carried by 50 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 063Y, a lemma

[Tag 063Y](https://stacks.math.columbia.edu/tag/063Y) in the Stacks Project.

**`Stacks.Thickenings.flat_and_isPullback_of_isIso_firstOrderThickeningConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalConverse.lean, line 585](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalConverse.lean#L585). The attribute's comment: “(2) ⟹ (1) for schemes”.

> **[Stacks Project, Tag 063Y], (2) ⟹ (1), for schemes.** Let
> `(f, f') : (X ⊂ X') → (S ⊂ S')` be a morphism of first-order thickenings of schemes, with
> `f = φ.left` and `f' = φ.right`, and let `f` be flat.  If the canonical map
> `f^* 𝒞_{S/S'} ⟶ 𝒞_{X/X'}` is an isomorphism, then `f'` is flat and `X = S ×_{S'} X'`.
>
> The hypothesis is condition (2) of the tag and the conclusion is its condition (1): `Flat φ.right`
> is flatness of `f'` and `IsPullback i φ.left φ.right j` is the base-change identity
> `X = S ×_{S'} X'`.  The flatness of `f` is the tag's standing hypothesis, and here it is used: it
> is what makes `Γ(S, j⁻¹V) ⟶ Γ(X, i⁻¹U)` flat, which is a hypothesis of the commutative algebra
> `Ideal.bijective_fibreTensorSMulHomToKer_iff`.

```lean
theorem flat_and_isPullback_of_isIso_firstOrderThickeningConormalSheafMap {i : X ⟶ X'}
    {j : S ⟶ S'} (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (φ : Arrow.mk i ⟶ Arrow.mk j) [Flat φ.left]
    (hiso : letI := hi.1
      letI := hj.1
      IsIso (firstOrderThickeningConormalSheafMap hi hj φ)) :
    Flat φ.right ∧ IsPullback i φ.left φ.right j
```

**`Stacks.Thickenings.flat_and_isPullback_iff_isIso_firstOrderThickeningConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalConverse.lean, line 609](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalConverse.lean#L609).

> **[Stacks Project, Tag 063Y] for schemes.** Let `(f, f') : (X ⊂ X') → (S ⊂ S')` be a morphism
> of first-order thickenings of schemes with `f = φ.left` flat.  Then the following are equivalent:
>
> * **(1)** `f'` is flat and `X = S ×_{S'} X'`;
> * **(2)** the canonical map `f^* 𝒞_{S/S'} ⟶ 𝒞_{X/X'}` is an isomorphism.
>
> The two directions are
> `Stacks.Thickenings.isIso_firstOrderThickeningConormalSheafMap` and
> `Stacks.Thickenings.flat_and_isPullback_of_isIso_firstOrderThickeningConormalSheafMap`.  The
> standing hypothesis that `f` be flat is not needed for (1) ⟹ (2), where it follows from the other
> two; it is needed for (2) ⟹ (1).

```lean
theorem flat_and_isPullback_iff_isIso_firstOrderThickeningConormalSheafMap {i : X ⟶ X'}
    {j : S ⟶ S'} (hi : IsFirstOrderThickening i) (hj : IsFirstOrderThickening j)
    (φ : Arrow.mk i ⟶ Arrow.mk j) [Flat φ.left] :
    letI := hi.1
    letI := hj.1
    (Flat φ.right ∧ IsPullback i φ.left φ.right j) ↔
      IsIso (firstOrderThickeningConormalSheafMap hi hj φ)
```

**`Stacks.Thickenings.epi_firstOrderThickeningConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalMap.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalMap.lean#L137). The attribute's comment: “(1) ⟹ (2) for schemes, surjectivity”.

> **The surjectivity half of condition (2) of [Stacks Project, Tag 063Y], for schemes.** For a
> morphism of first-order thickenings whose square is cartesian, so that `X = S ×_{S'} X'`, the
> canonical map `f^* 𝒞_{S/S'} ⟶ 𝒞_{X/X'}` is an epimorphism.
>
> No flatness is used: cartesianness alone gives surjectivity, by
> `Stacks.Immersion.epi_immersionConormalSheafMap`, which is the surjectivity clause of
> [Stacks Project, Tag 0473] for a cartesian square of immersions.  The cartesian hypothesis is
> the second half of condition (1) of the tag, so this is the half of (1) ⟹ (2) that the flatness
> hypotheses are not needed for.

```lean
theorem epi_firstOrderThickeningConormalSheafMap (hi : IsFirstOrderThickening i)
    (hj : IsFirstOrderThickening j) (φ : Arrow.mk i ⟶ Arrow.mk j)
    (sq : IsPullback i φ.left φ.right j) :
    letI := hi.1
    letI := hj.1
    Epi (firstOrderThickeningConormalSheafMap hi hj φ)
```

**`Stacks.Thickenings.isIso_firstOrderThickeningConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalMap.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FirstOrderThickeningConormalMap.lean#L183). The attribute's comment: “(1) ⟹ (2) for schemes”.

> **[Stacks Project, Tag 063Y], (1) ⟹ (2), for schemes.**  Let `(f, f') : (X ⊂ X') → (S ⊂ S')`
> be a morphism of first-order thickenings of schemes, with `f = φ.left` and `f' = φ.right`.  If
> `f'` is flat and `X = S ×_{S'} X'`, then the canonical map `f^* 𝒞_{S/S'} ⟶ 𝒞_{X/X'}` is an
> isomorphism.
>
> The two hypotheses are exactly the two halves of condition (1) of the tag: `Flat φ.right` is
> flatness of `f'`, and `sq` is the base-change identity `X = S ×_{S'} X'`.  The conclusion is
> condition (2).  The standing hypothesis of the tag that `f` be flat is not needed, because it is
> a consequence of the other two.
>
> This is `Stacks.Immersion.isIso_immersionConormalSheafMap_of_flat`, the flat base-change clause
> of [Stacks Project, Tag 0473], applied to the square of immersions underlying the morphism of
> thickenings.

```lean
theorem isIso_firstOrderThickeningConormalSheafMap (hi : IsFirstOrderThickening i)
    (hj : IsFirstOrderThickening j) (φ : Arrow.mk i ⟶ Arrow.mk j) [Flat φ.right]
    (sq : IsPullback i φ.left φ.right j) :
    letI := hi.1
    letI := hj.1
    IsIso (firstOrderThickeningConormalSheafMap hi hj φ)
```

**`Ideal.bijective_tensorSMulHomToKer_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/SquareZeroConormal.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/SquareZeroConormal.lean#L346). The attribute's comment: “affine case”. References: SGA 3 III (0.14), “partial”; SGA 3 XV (2.7), “affine case”.

> **Stacks 063Y, the affine case.** Let `I ^ 2 = 0` in `A'`, write `A = A' ⧸ I`, let `B` be a
> quotient of the `A'`-algebra `B'` which is compatibly an `A`-algebra, and let `J` be the kernel of
> `B' → B`.  Assume `A → B` flat.  Then the canonical map `I ⊗[A'] B' → J` is an isomorphism if and
> only if `A' → B'` is flat and `J = I B'`.
>
> The second condition says that `X = Spec B` is the fibre product `S ×_{S'} X'`, and
> `I ⊗[A'] B'` is the pullback to `X` of the conormal module of `S ⊂ S'` by
> `Ideal.tensorEquivTensorQuot`.

```lean
theorem bijective_tensorSMulHomToKer_iff (hI2 : I ^ 2 = ⊥)
    (hsurj : Function.Surjective (algebraMap B' B)) (hflat : Module.Flat (A' ⧸ I) B) :
    Function.Bijective (I.tensorSMulHomToKer B' B) ↔
      Module.Flat A' B' ∧
        (RingHom.ker (algebraMap B' B)).restrictScalars A' = I • (⊤ : Submodule A' B')
```

**`Ideal.bijective_fibreTensorSMulHomToKer_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/SquareZeroConormal.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/SquareZeroConormal.lean#L521). The attribute's comment: “affine case, with the source the pullback of the conormal module”.

> **Stacks 063Y in the affine case, with the source as the pullback of the conormal module.**
> Let `I ^ 2 = 0` in `A'`, write `A = A' ⧸ I`, let `B` be a quotient of the `A'`-algebra `B'` which
> is compatibly an `A`-algebra, and let `J` be the kernel of `B' → B`. Assume `J ^ 2 = 0` and
> `A → B` flat. Then the canonical map `I ⊗[A'] B → J` is an isomorphism if and only if `A' → B'`
> is flat and `J = I B'`.
>
> This is `Ideal.bijective_tensorSMulHomToKer_iff` with the source replaced by the pullback
> `I ⊗[A'] B` of the conormal module of `S ⊂ S'` to `X`, which is the module condition (2) of the
> source speaks about; that form needs `J ^ 2 = 0`, which the version with source `I ⊗[A'] B'` does
> not.

```lean
theorem bijective_fibreTensorSMulHomToKer_iff (hI2 : I ^ 2 = ⊥)
    (hJ2 : RingHom.ker (algebraMap B' B) ^ 2 = ⊥)
    (hsurj : Function.Surjective (algebraMap B' B)) (hflat : Module.Flat (A' ⧸ I) B) :
    Function.Bijective (I.fibreTensorSMulHomToKer B' B hJ2 hsurj) ↔
      Module.Flat A' B' ∧
        (RingHom.ker (algebraMap B' B)).restrictScalars A' = I • (⊤ : Submodule A' B')
```

## Tag 06AF, a lemma

[Tag 06AF](https://stacks.math.columbia.edu/tag/06AF) in the Stacks Project.

**`AlgebraicGeometry.flat_of_flat_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Flatness.lean, line 750](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Flatness.lean#L750). The attribute's comment: “flatness of the upper morphism”.

> Flatness of a morphism lifts from its reduction over a finite-order
> thickening when its source is flat over the thickened base.

```lean
public theorem flat_of_flat_reduction
    (hiX : IsThickening iX)
    (hiY : IsThickening iY)
    (hiS : IsFiniteOrderThickening iS)
    (hX : IsPullback iX pX pX' iS)
    (hY : IsPullback iY pY pY' iS)
    (hf : iX ≫ f' = f ≫ iY)
    (hfbase : f ≫ pY = pX)
    (hf'base : f' ≫ pY' = pX')
    (hflatX' : Flat pX') (hflatf : Flat f) : Flat f'
```

**`AlgebraicGeometry.flatAt_target_of_flat_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/Flatness.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/Flatness.lean#L766). The attribute's comment: “flatness of the upper target along the image”.

> The thickened target is flat over the thickened base at every point in
> the image of the upper morphism.

```lean
public theorem flatAt_target_of_flat_reduction
    (hiX : IsThickening iX)
    (hiY : IsThickening iY)
    (hiS : IsFiniteOrderThickening iS)
    (hX : IsPullback iX pX pX' iS)
    (hY : IsPullback iY pY pY' iS)
    (hf : iX ≫ f' = f ≫ iY)
    (hfbase : f ≫ pY = pX)
    (hf'base : f' ≫ pY' = pX')
    (hflatX' : Flat pX') (hflatf : Flat f)
    (x' : X') : IsFlatAt pY'.toLRSHom.toShHom (f' x')
```

## Tag 06AG, a lemma

[Tag 06AG](https://stacks.math.columbia.edu/tag/06AG) in the Stacks Project.

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.locallyOfFinitePresentation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/FinitePresentation.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/FinitePresentation.lean#L353). The attribute's comment: “locally\_finite\_presentation”.

> Local finite presentation is invariant under a cartesian finite-order deformation when the
> enlarged source is flat over the enlarged base.

```lean
theorem locallyOfFinitePresentation_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    LocallyOfFinitePresentation D.f ↔ LocallyOfFinitePresentation D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.locallyOfFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L70). The attribute's comment: “locally\_finite\_type”.

> Local finite type is invariant under a cartesian finite-order deformation.

```lean
theorem locallyOfFiniteType_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    LocallyOfFiniteType D.f ↔ LocallyOfFiniteType D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.locallyQuasiFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L83). The attribute's comment: “locally\_quasi\_finite”.

> Local quasi-finiteness is invariant under a cartesian finite-order deformation with flat
> enlarged source.

```lean
theorem locallyQuasiFinite_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    (LocallyOfFiniteType D.f ∧ LocallyQuasiFinite D.f) ↔
      (LocallyOfFiniteType D.f' ∧ LocallyQuasiFinite D.f')
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L108). The attribute's comment: “proper”.

> Properness is invariant under a cartesian finite-order deformation.

```lean
theorem isProper_iff (d : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsProper d.f ↔ IsProper d.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isAffineHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean#L96). The attribute's comment: “affine”.

> **Stacks 06AG, affine case.** Affineness is invariant under a cartesian finite-order
> deformation with flat ambient source.

```lean
theorem isAffineHom_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsAffineHom D.f ↔ IsAffineHom D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isIntegralHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean#L104). The attribute's comment: “integral”.

> **Stacks 06AG, integral case.** Integrality is invariant under a cartesian finite-order
> deformation with flat ambient source: it is universal closedness together with affineness.

```lean
theorem isIntegralHom_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsIntegralHom D.f ↔ IsIntegralHom D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean#L115). The attribute's comment: “finite”.

> **Stacks 06AG, finite case.** Finiteness is invariant under a cartesian finite-order
> deformation with flat ambient source: it is integrality together with local finite type.

```lean
theorem isFinite_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsFinite D.f ↔ IsFinite D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.etale_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Etale.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Etale.lean#L89). The attribute's comment: “etale”.

> **Stacks 06AG, étale case.** Étaleness is invariant under a cartesian finite-order
> deformation with flat ambient source.

```lean
theorem CartesianFiniteOrderDeformationDiagram.etale_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) : Etale D.f ↔ Etale D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isFiniteLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean#L84). The attribute's comment: “finite\_locally\_free”.

> In a cartesian finite-order deformation diagram, `f` is finite, flat and locally of finite
> presentation if and only if `f'` is.

```lean
theorem isFiniteLocallyFree_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    (IsFinite D.f ∧ Flat D.f ∧ LocallyOfFinitePresentation D.f) ↔
      (IsFinite D.f' ∧ Flat D.f' ∧ LocallyOfFinitePresentation D.f')
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isFiniteLocallyFreeOfRank_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean#L92). The attribute's comment: “finite\_locally\_free\_of\_rank”.

> In a cartesian finite-order deformation diagram, `f` is finite locally free of rank `d` if and
> only if `f'` is.

```lean
theorem isFiniteLocallyFreeOfRank_iff (D : CartesianFiniteOrderDeformationDiagram.{u})
    (d : ℕ) :
    (IsFinite D.f ∧ Flat D.f ∧ LocallyOfFinitePresentation D.f ∧
        ∀ y : D.Y, D.f.finrank y = d) ↔
      (IsFinite D.f' ∧ Flat D.f' ∧ LocallyOfFinitePresentation D.f' ∧
        ∀ y' : D.Y', D.f'.finrank y' = d)
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.flat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Flat.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Flat.lean#L71). The attribute's comment: “flat”.

> **Stacks 06AG, flat case.** Flatness is invariant under a cartesian finite-order deformation
> with flat ambient source.

```lean
theorem CartesianFiniteOrderDeformationDiagram.flat_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) : Flat D.f ↔ Flat D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isOpenImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L95). The attribute's comment: “open\_immersion”.

> Being an open immersion is invariant under a cartesian finite-order deformation with flat
> ambient source.

```lean
theorem isOpenImmersion_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsOpenImmersion D.f ↔ IsOpenImmersion D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.isIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L107). The attribute's comment: “isomorphism”.

> Being an isomorphism is invariant under a cartesian finite-order deformation with flat ambient
> source.

```lean
theorem isIso_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    IsIso D.f ↔ IsIso D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L164). The attribute's comment: “monomorphism”.

> Being a monomorphism is invariant under a cartesian finite-order deformation with flat ambient
> source.

```lean
theorem mono_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) :
    Mono D.f ↔ Mono D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.relativeDimension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/RelativeDimension.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/RelativeDimension.lean#L65). The attribute's comment: “relative\_dimension”.

> Being locally of finite type of relative dimension `d` is invariant under a cartesian
> finite-order deformation with flat ambient source.

```lean
theorem relativeDimension_iff (D : CartesianFiniteOrderDeformationDiagram.{u}) (d : ℕ) :
    (∃ _ : LocallyOfFiniteType D.f, RelativeDimension D.f d) ↔
      (∃ _ : LocallyOfFiniteType D.f', RelativeDimension D.f' d)
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.smooth_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Smooth.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Smooth.lean#L82). The attribute's comment: “smooth”.

> **Stacks 06AG, smooth case.** Smoothness is invariant under a cartesian finite-order
> deformation with flat ambient source.

```lean
theorem CartesianFiniteOrderDeformationDiagram.smooth_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) : Smooth D.f ↔ Smooth D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.syntomic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Syntomic.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Syntomic.lean#L80). The attribute's comment: “syntomic”.

> **Stacks 06AG, syntomic case.** Syntomicity is invariant under a cartesian finite-order
> deformation with flat ambient source.

```lean
theorem CartesianFiniteOrderDeformationDiagram.syntomic_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) : Syntomic D.f ↔ Syntomic D.f'
```

**`Stacks.Thickenings.CartesianFiniteOrderDeformationDiagram.unramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Unramified.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Unramified.lean#L87). The attribute's comment: “unramified”.

> **Stacks 06AG, unramified case.** Unramifiedness is invariant under a cartesian finite-order
> deformation with flat ambient source.

```lean
theorem CartesianFiniteOrderDeformationDiagram.unramified_iff
    (D : CartesianFiniteOrderDeformationDiagram.{u}) : Unramified D.f ↔ Unramified D.f'
```

Declarations registered for the tag:

- [`Stacks.Thickenings.quasiCompact_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L73), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L122) (StacksFrontier): “quasi\_compact”.
- [`Stacks.Thickenings.isSeparated_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L123) (StacksFrontier): “separated”.
- [`Stacks.Thickenings.quasiSeparated_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L124) (StacksFrontier): “separated”.
- [`Stacks.Thickenings.surjective_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L125) (StacksFrontier): “surjective”.
- [`Stacks.Thickenings.universallyClosed_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L126), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L126) (StacksFrontier): “universally\_closed”.
- [`Stacks.Thickenings.universallyInjective_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L157), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L127) (StacksFrontier): “universally\_injective”.
- [`Stacks.Thickenings.universallyOpen_left_iff_right`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L245), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Deformation/Properties.lean#L128) (StacksFrontier): “universally\_open”.

## Tag 0CF3, a lemma

[Tag 0CF3](https://stacks.math.columbia.edu/tag/0CF3) in the Stacks Project.

**`Stacks.Flatness.flat_of_flat_baseChange_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean#L315). The attribute's comment: “flatness of the ambient morphism”.

> **Flatness lifts across cartesian thickenings.** Let `iX : X ⟶ X'`, `iY : Y ⟶ Y'` and
> `iS : S ⟶ S'` be thickenings, let `f : X ⟶ Y` and `f' : X' ⟶ Y'` be compatible morphisms over
> `S` and `S'`, and let both `X` and `Y` be the base change of `S` along `X' ⟶ S'` and
> `Y' ⟶ S'`. If `Y' ⟶ S'` is locally of finite type, `X' ⟶ S'` is flat and locally of finite
> presentation and `f` is flat, then `f'` is flat.

```lean
theorem flat_of_flat_baseChange_thickening
    {X X' Y Y' S S' : Scheme.{u}}
    (iX : X ⟶ X') (iY : Y ⟶ Y') (iS : S ⟶ S')
    (f : X ⟶ Y) (f' : X' ⟶ Y')
    (gX : X ⟶ S) (gX' : X' ⟶ S')
    (gY : Y ⟶ S) (gY' : Y' ⟶ S')
    (hiX : IsThickening iX)
    (hiY : IsThickening iY)
    (hiS : IsThickening iS)
    (hcomm : f ≫ iY = iX ≫ f')
    (hover : f ≫ gY = gX)
    (hover' : f' ≫ gY' = gX')
    (hX : IsPullback iX gX gX' iS)
    (hY : IsPullback iY gY gY' iS)
    [LocallyOfFiniteType gY'] [Flat gX'] [LocallyOfFinitePresentation gX']
    (hf : Flat f) : Flat f'
```

**`Stacks.Flatness.flat_stalkMap_of_flat_baseChange_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean#L338). The attribute's comment: “flatness of the target local ring”.

> **The local ring of the target is flat over the base.** In the situation of Stacks Tag 0CF3,
> the local ring of `Y'` at the image of a point of `X'` is flat over the local ring of `S'`.

```lean
theorem flat_stalkMap_of_flat_baseChange_thickening
    {X X' Y Y' S S' : Scheme.{u}}
    (iX : X ⟶ X') (iY : Y ⟶ Y') (iS : S ⟶ S')
    (f : X ⟶ Y) (f' : X' ⟶ Y')
    (gX : X ⟶ S) (gX' : X' ⟶ S')
    (gY : Y ⟶ S) (gY' : Y' ⟶ S')
    (hiX : IsThickening iX)
    (hiY : IsThickening iY)
    (hiS : IsThickening iS)
    (hcomm : f ≫ iY = iX ≫ f')
    (hover : f ≫ gY = gX)
    (hover' : f' ≫ gY' = gX')
    (hX : IsPullback iX gX gX' iS)
    (hY : IsPullback iY gY gY' iS)
    [LocallyOfFiniteType gY'] [Flat gX'] [LocallyOfFinitePresentation gX']
    (hf : Flat f) (x' : X') : (gY'.stalkMap (f' x')).hom.Flat
```

**`Stacks.Flatness.essentiallyOfFinitePresentation_stalkMap_of_flat_baseChange_thickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/ThickeningBaseChange.lean#L361). The attribute's comment: “essential finite presentation of the target local ring”.

> **The local ring of the target is essentially of finite presentation over the base.** In the
> situation of Stacks Tag 0CF3, the local ring of `Y'` at the image of a point of `X'` is
> essentially of finite presentation over the local ring of `S'`.

```lean
theorem essentiallyOfFinitePresentation_stalkMap_of_flat_baseChange_thickening
    {X X' Y Y' S S' : Scheme.{u}}
    (iX : X ⟶ X') (iY : Y ⟶ Y') (iS : S ⟶ S')
    (f : X ⟶ Y) (f' : X' ⟶ Y')
    (gX : X ⟶ S) (gX' : X' ⟶ S')
    (gY : Y ⟶ S) (gY' : Y' ⟶ S')
    (hiX : IsThickening iX)
    (hiY : IsThickening iY)
    (hiS : IsThickening iS)
    (hcomm : f ≫ iY = iX ≫ f')
    (hover : f ≫ gY = gX)
    (hover' : f' ≫ gY' = gX')
    (hX : IsPullback iX gX gX' iS)
    (hY : IsPullback iY gY gY' iS)
    [LocallyOfFiniteType gY'] [Flat gX'] [LocallyOfFinitePresentation gX']
    (hf : Flat f) (x' : X') :
    IsEssentiallyOfFinitePresentation
      (S'.presheaf.stalk (gY' (f' x')))
      (Y'.presheaf.stalk (f' x'))
      (gY'.stalkMap (f' x')).hom
```

## Tag 0CF4, a lemma

[Tag 0CF4](https://stacks.math.columbia.edu/tag/0CF4) in the Stacks Project.

**`Stacks.Thickenings.FlatDeformationDiagram.isAffineHom_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean#L127). The attribute's comment: “affine”.

> Affineness is invariant under a flat deformation diagram.

```lean
theorem isAffineHom_iff (D : FlatDeformationDiagram.{u}) :
    IsAffineHom D.f ↔ IsAffineHom D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Affine.lean#L143). The attribute's comment: “finite”.

> Finiteness is invariant under a flat deformation diagram: it is integrality together with
> local finite type, and both horizontal morphisms are locally of finite type.

```lean
theorem isFinite_iff (D : FlatDeformationDiagram.{u}) : IsFinite D.f ↔ IsFinite D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.etale_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Etale.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Etale.lean#L74). The attribute's comment: “etale”.

> Étaleness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.etale_iff (D : FlatDeformationDiagram.{u}) :
    Etale D.f ↔ Etale D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.finiteLocallyFree_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FiniteLocallyFree.lean#L133). The attribute's comment: “finite\_locally\_free”.

> Being finite locally free, and being finite locally free of a given rank `d`, are each
> invariant under a flat deformation diagram.

```lean
theorem finiteLocallyFree_iff (D : FlatDeformationDiagram.{u}) :
    ((IsFinite D.f ∧ Flat D.f ∧ LocallyOfFinitePresentation D.f) ↔
      (IsFinite D.f' ∧ Flat D.f' ∧ LocallyOfFinitePresentation D.f')) ∧
    ∀ d : ℕ, (IsFinite D.f ∧ Flat D.f ∧ LocallyOfFinitePresentation D.f ∧
        ∀ y : D.Y, D.f.finrank y = d) ↔
      (IsFinite D.f' ∧ Flat D.f' ∧ LocallyOfFinitePresentation D.f' ∧
        ∀ y' : D.Y', D.f'.finrank y' = d)
```

**`Stacks.Thickenings.FlatDeformationDiagram.flat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Flat.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Flat.lean#L57). The attribute's comment: “flat”.

> Flatness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.flat_iff (D : FlatDeformationDiagram.{u}) :
    Flat D.f ↔ Flat D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.quasiCompact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L60). The attribute's comment: “quasi\_compact”.

> Quasi-compactness is invariant under a flat deformation diagram.

```lean
theorem quasiCompact_iff : QuasiCompact D.f ↔ QuasiCompact D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.universallyClosed_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L65). The attribute's comment: “universally\_closed”.

> Universal closedness is invariant under a flat deformation diagram.

```lean
theorem universallyClosed_iff : UniversallyClosed D.f ↔ UniversallyClosed D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.separated_and_quasiSeparated_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L71). The attribute's comment: “separated”.

> Separatedness and quasi-separatedness are each invariant under a flat deformation
> diagram.

```lean
theorem separated_and_quasiSeparated_iff :
    (IsSeparated D.f ↔ IsSeparated D.f') ∧ (QuasiSeparated D.f ↔ QuasiSeparated D.f')
```

**`Stacks.Thickenings.FlatDeformationDiagram.surjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L78). The attribute's comment: “surjective”.

> Surjectivity is invariant under a flat deformation diagram.

```lean
theorem surjective_iff : Surjective D.f ↔ Surjective D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.universallyInjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L83). The attribute's comment: “universally\_injective”.

> Universal injectivity is invariant under a flat deformation diagram.

```lean
theorem universallyInjective_iff : UniversallyInjective D.f ↔ UniversallyInjective D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.universallyOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/FromThickeningMorphism.lean#L88). The attribute's comment: “universally\_open”.

> Universal openness is invariant under a flat deformation diagram.

```lean
theorem universallyOpen_iff : UniversallyOpen D.f ↔ UniversallyOpen D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.isOpenImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L176). The attribute's comment: “open\_immersion”.

> Being an open immersion is invariant under a flat deformation diagram.

```lean
theorem isOpenImmersion_iff (D : FlatDeformationDiagram.{u}) :
    IsOpenImmersion D.f ↔ IsOpenImmersion D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.isIso_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L185). The attribute's comment: “isomorphism”.

> Being an isomorphism is invariant under a flat deformation diagram.

```lean
theorem isIso_iff (D : FlatDeformationDiagram.{u}) : IsIso D.f ↔ IsIso D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/OpenImmersion.lean#L192). The attribute's comment: “monomorphism”.

> Being a monomorphism is invariant under a flat deformation diagram.

```lean
theorem mono_iff (D : FlatDeformationDiagram.{u}) : Mono D.f ↔ Mono D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Proper.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Proper.lean#L47). The attribute's comment: “proper”.

> Properness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.isProper_iff (d : FlatDeformationDiagram.{u}) :
    IsProper d.f ↔ IsProper d.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.locallyQuasiFinite_conditions_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/QuasiFinite.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/QuasiFinite.lean#L46). The attribute's comment: “locally\_quasi\_finite”.

> Local quasi-finiteness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.locallyQuasiFinite_conditions_iff
    (D : FlatDeformationDiagram.{u}) :
    (LocallyOfFiniteType D.f ∧ LocallyQuasiFinite D.f) ↔
      (LocallyOfFiniteType D.f' ∧ LocallyQuasiFinite D.f')
```

**`Stacks.Thickenings.FlatDeformationDiagram.relativeDimension_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/RelativeDimension.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/RelativeDimension.lean#L92). The attribute's comment: “relative\_dimension”.

> Being locally of finite type of relative dimension `d` is invariant under a flat deformation
> diagram.

```lean
theorem relativeDimension_iff (D : FlatDeformationDiagram.{u}) (d : ℕ) :
    (∃ _ : LocallyOfFiniteType D.f, RelativeDimension D.f d) ↔
      (∃ _ : LocallyOfFiniteType D.f', RelativeDimension D.f' d)
```

**`Stacks.Thickenings.FlatDeformationDiagram.smooth_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Smooth.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Smooth.lean#L69). The attribute's comment: “smooth”.

> Smoothness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.smooth_iff (D : FlatDeformationDiagram.{u}) :
    Smooth D.f ↔ Smooth D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.syntomic_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Syntomic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Syntomic.lean#L60). The attribute's comment: “syntomic”.

> Syntomicity is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.syntomic_iff (D : FlatDeformationDiagram.{u}) :
    Syntomic D.f ↔ Syntomic D.f'
```

**`Stacks.Thickenings.FlatDeformationDiagram.unramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Unramified.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/DeformationFiniteOrder/Unramified.lean#L76). The attribute's comment: “unramified”.

> Unramifiedness is invariant under a flat deformation diagram.

```lean
theorem FlatDeformationDiagram.unramified_iff (D : FlatDeformationDiagram.{u}) :
    Unramified D.f ↔ Unramified D.f'
```

## Tag 0D4F, a lemma

[Tag 0D4F](https://stacks.math.columbia.edu/tag/0D4F) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveDeformation.exists_uniform_degreeBound_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveDeformation/DeformationsOfProjectiveSchemesFunctorial.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveDeformation/DeformationsOfProjectiveSchemesFunctorial.lean#L75).

> **Deformations of projective schemes** ([Stacks, Tag 0D4F]).  Let `(f : X ⟶ S, ℒ)` be a
> polarized family: `f` proper, flat and of finite presentation, `S` quasi-compact, `ℒ` invertible
> and ample relative to `f`.  There is a positive `d₀` such that for every admissible deformation
> `(X', S', i, i', f', ℒ')` of it — a cartesian square over a thickening `S ⊂ S'` with `f'` proper,
> flat and of finite presentation, and `ℒ'` invertible with `ℒ ≅ (i')^* ℒ'`:
>
> 1. `R^p (f')_* (ℒ')^{⊗ d} = 0` for all `p > 0` and `d ≥ d₀`;
> 2. `𝒜'_d = (f')_* (ℒ')^{⊗ d}` is finite locally free for `d ≥ d₀`;
> 3. `𝒜' = 𝒪_{S'} ⊕ ⨁_{d ≥ d₀} 𝒜'_d` (`truncatedSectionAlgebra`) is a quasi-coherent graded
>    `𝒪_{S'}`-algebra with these pieces, its comparison `𝒜' ⟶ ⨁_{d ≥ 0} 𝒜'_d`
>    (`sectionAlgebraComparison`) is an isomorphism in every degree `≥ d₀`, and `𝒜'` is of finite
>    presentation over every affine open of `S'`;
> 4. the canonical morphism `r' : X' ⟶ Proj_{S'}(𝒜')` (`canonicalProjHom`) is an isomorphism over
>    `S'`;
> 5. the canonical map `θ' : (r')^* 𝒪_{Proj_{S'}(𝒜')}(1) ⟶ ℒ'` (`canonicalTwistMap`) is an
>    isomorphism;
>
> and the formation of each `𝒜'_d`, `d ≥ d₀`, commutes with arbitrary base change.
>
> **Functoriality.** For every morphism `φ : D₁ ⟶ D₂` of admissible deformations (a cartesian
> square `g' : X'₁ ⟶ X'₂` over `g : S'₁ ⟶ S'₂` compatible with the immersions of the family, with
> polarization `g'^* ℒ'₂ ≅ ℒ'₁`):
>
> * `𝒜'` is functorial: the homomorphism of graded algebras `g^* 𝒜'(D₂) ⟶ 𝒜'(D₁)` obtained by
>   pulling sections back (`algebraPullbackHom`) is an isomorphism in every degree;
> * `r'` is functorial: with `M : Proj_{S'₁}(𝒜'(D₁)) ⟶ Proj_{S'₂}(𝒜'(D₂))` the morphism it induces
>   followed by the base change morphism of [Stacks, Tag 01O3] (`projBaseChangeHom`),
>   `r'₁ ≫ M = g' ≫ r'₂`;
> * `θ'` is functorial: `g'^* θ'₂` followed by the polarization equals, through
>   `g'^* (r'₂)^* ≅ (r'₁ ≫ M)^* ≅ (r'₁)^* M^*`, the inverse image along `r'₁` of the map of Serre
>   twists `M^* 𝒪(1) ⟶ 𝒪(1)` of [Stacks, Tags 01O3, 07ZJ] (`projBaseChangeTwistMap`) followed by
>   `θ'₁`.

```lean
public theorem exists_uniform_degreeBound_functorial (P : PolarizedFamily.{u}) :
    ∃ (d₀ : ℕ) (hd₀ : 0 < d₀), (∀ D : P.AdmissibleDeformation,
      (∀ d : ℕ, d₀ ≤ d → ∀ p : ℤ, 0 < p →
          IsZero (((Scheme.Modules.pushforward D.f').rightDerivedPlus p).obj
            (tensorPowModule D.X' D.L' (d : ℤ)))) ∧
        (∀ d : ℕ, d₀ ≤ d →
          _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
            (R := D.S'.ringCatSheaf) (D.sectionPiece d)) ∧
        (D.IsTruncatedSectionAlgebraWithComparison d₀ (D.truncatedSectionAlgebra d₀ hd₀) ∧
          (∀ d : ℕ, d₀ ≤ d → IsIso ((D.sectionAlgebraComparison d₀ hd₀).app (d : ℤ))) ∧
          (∀ U : D.S'.Opens, IsAffineOpen U →
            RingHom.FinitePresentation ((D.truncatedSectionAlgebra d₀ hd₀).strHom U))) ∧
        (IsIso (D.canonicalProjHom d₀ hd₀) ∧
          D.canonicalProjHom d₀ hd₀ ≫ (relativeProj (D.truncatedSectionAlgebra d₀ hd₀)).toBase =
            D.f') ∧
        IsIso (D.canonicalTwistMap d₀ hd₀) ∧
        ∀ d : ℕ, d₀ ≤ d → ∀ (T Y : Scheme.{u}) (h : T ⟶ D.S') (fT : Y ⟶ T) (h' : Y ⟶ D.X')
          (hsq : IsPullback h' fT D.f' h),
          IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app
            (tensorPowModule D.X' D.L' (d : ℤ)))) ∧
      ∀ (D₁ D₂ : P.AdmissibleDeformation) (φ : Hom D₁ D₂),
        ∃ hiso : ∀ n : ℤ, IsIso ((algebraPullbackHom φ d₀ hd₀).app n),
          D₁.canonicalProjHom d₀ hd₀ ≫ projBaseChangeHom φ d₀ hd₀ hiso =
            φ.total ≫ D₂.canonicalProjHom d₀ hd₀ ∧
          (Scheme.Modules.pullback φ.total).map (D₂.canonicalTwistMap d₀ hd₀) ≫
              φ.polarization.hom =
            (Scheme.Modules.pullbackComp φ.total (D₂.canonicalProjHom d₀ hd₀)).hom.app _ ≫
              (Scheme.Modules.pullbackCongr
                (canonicalProjHom_comp_projBaseChangeHom φ d₀ hd₀ hiso).symm).hom.app _ ≫
              (Scheme.Modules.pullbackComp (D₁.canonicalProjHom d₀ hd₀)
                (projBaseChangeHom φ d₀ hd₀ hiso)).inv.app _ ≫
              (Scheme.Modules.pullback (D₁.canonicalProjHom d₀ hd₀)).map
                (projBaseChangeTwistMap φ d₀ hd₀ hiso) ≫
              D₁.canonicalTwistMap d₀ hd₀
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.10, Tag 063X](https://stacks.math.columbia.edu/tag/063X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
