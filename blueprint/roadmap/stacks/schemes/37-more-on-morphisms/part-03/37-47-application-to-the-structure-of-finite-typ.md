---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finite_over_smooth_of_locallyOfFiniteType, AlgebraicGeometry.exists_finite_over_smooth, AlgebraicGeometry.exists_finite_over_smooth_affine, AlgebraicGeometry.exists_open_preimage_le, AlgebraicGeometry.finite_stalkMap_of_preimage_singleton, AlgebraicGeometry.finitePresentation_stalkMap_of_preimage_singleton, AlgebraicGeometry.exists_linearEquiv_stalkPushforward_of_finite_singleton_fiber
statement: formalized
proof: formalized
---

# 37.47 Application to the structure of finite type morphisms

Section 37.47 of the Stacks Project, [Tag 052D](https://stacks.math.columbia.edu/tag/052D). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 052E, a lemma

[Tag 052E](https://stacks.math.columbia.edu/tag/052E) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_over_smooth_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteOverSmooth/Main.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FiniteOverSmooth/Main.lean#L59).

> **Stacks 052E.** Let `f : X ⟶ S` be locally of finite type, let `x ∈ X` and set `s = f x`.
> If the fibre `X_s` has local dimension `n` at `x`, then there is a commutative square
> `g ≫ f = π ≫ h` in which `h : Y ⟶ S` is smooth of relative dimension `n`,
> `g : (X', x') ⟶ (X, x)` is an elementary étale neighbourhood, `π : X' ⟶ Y` is finite, and the
> fibre of `π` over `y = π x'` is the single point `x'`; moreover `κ(y)` is a purely
> transcendental extension of `κ(s)`, and if `f` is locally of finite presentation then `π` is of
> finite presentation.

```lean
theorem exists_finite_over_smooth_of_locallyOfFiniteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) (n : ℕ)
    (hdim : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = n) :
    ∃ (Y : Scheme.{u}) (h : Y ⟶ S) (N : EtaleNeighborhood X x) (π : N.scheme ⟶ Y),
      SmoothOfRelativeDimension n h ∧ N.IsElementary ∧ IsFinite π ∧
      {z : N.scheme | π z = π N.point} = {N.point} ∧
      N.toBase ≫ f = π ≫ h ∧
      (∃ hy : h (π N.point) = f x,
        letI : Algebra (S.residueField (f x)) (Y.residueField (π N.point)) :=
          (((S.residueFieldCongr hy).inv ≫ h.residueFieldMap (π N.point)).hom).toAlgebra
        PurelyTranscendental (S.residueField (f x)) (Y.residueField (π N.point))) ∧
      (LocallyOfFinitePresentation f → FinitePresentation π)
```

## Tag 057K, a lemma

[Tag 057K](https://stacks.math.columbia.edu/tag/057K) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_over_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L149).

> **Stacks Project, Tag 057K.** A morphism locally of finite type is, in elementary étale
> neighbourhoods of a point and of its image, finite over a smooth morphism of relative dimension
> the dimension of the fibre at that point, with geometrically integral fibres and purely
> transcendental residue field extension; and the finite morphism is of finite presentation as
> soon as the original one is.

```lean
theorem exists_finite_over_smooth : Statement057K.{u}
```

## Tag 057L, a lemma

[Tag 057L](https://stacks.math.columbia.edu/tag/057L) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_over_smooth_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FiniteOverSmoothAffine.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/FiniteOverSmoothAffine.lean#L186).

> **Stacks Project, Tag 057L.** The finite-over-smooth local structure of a locally
> finite-type morphism can be obtained with all three new schemes affine.

```lean
theorem exists_finite_over_smooth_affine {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) :
    ∃ (n : ℕ) (_ : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = n)
      (U : EtaleNeighborhood X x) (V : EtaleNeighborhood S (f x))
      (Y : Scheme.{u}) (h : Y ⟶ V.scheme) (π : U.scheme ⟶ Y),
      U.IsElementary ∧ V.IsElementary ∧ (U.toBase ≫ f = π ≫ h ≫ V.toBase) ∧
        SmoothOfRelativeDimension n h ∧
        (∀ s' : V.scheme, GeometricallyIntegral (h.fiberToSpecResidueField s')) ∧
        IsFinite π ∧ (∀ z : U.scheme, π z = π U.point ↔ z = U.point) ∧
        (∃ heq : h (π U.point) = V.point,
          letI : Algebra (V.scheme.residueField V.point) (Y.residueField (π U.point)) :=
            ((V.scheme.residueFieldCongr heq).inv ≫ h.residueFieldMap (π U.point)).hom.toAlgebra
          PurelyTranscendental (V.scheme.residueField V.point)
            (Y.residueField (π U.point))) ∧
        (LocallyOfFinitePresentation f → FinitePresentation π) ∧
        IsAffine V.scheme ∧ IsAffine Y ∧ IsAffine U.scheme
```

## Tag 05B8, a lemma

[Tag 05B8](https://stacks.math.columbia.edu/tag/05B8) in the Stacks Project.

**`AlgebraicGeometry.exists_open_preimage_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean#L62). The attribute's comment: “inverse\_image\_neighbourhoods”.

> For a finite morphism whose fibre over `y` is the singleton `x`, the inverse image of
> some open neighbourhood of `y` is contained in any prescribed open neighbourhood of `x`.

```lean
lemma exists_open_preimage_le {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f]
    (x : X) (y : Y) (hxy : f x = y) (hfiber : f ⁻¹' {y} = {x})
    (U : X.Opens) (hxU : x ∈ U) :
    ∃ V : Y.Opens, y ∈ V ∧ f ⁻¹ᵁ V ≤ U
```

**`AlgebraicGeometry.finite_stalkMap_of_preimage_singleton`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean#L202). The attribute's comment: “finite\_local\_ring\_map”.

> For a finite morphism with a singleton fibre at `x`, the induced map on the local rings at
> `f x` and `x` is finite.

```lean
lemma finite_stalkMap_of_preimage_singleton
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f]
    (x : X) (hx : f ⁻¹' {f x} = {x}) :
    (f.stalkMap x).hom.Finite
```

**`AlgebraicGeometry.finitePresentation_stalkMap_of_preimage_singleton`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean#L258). The attribute's comment: “finitely\_presented\_local\_ring\_map”.

> If a finite morphism of finite presentation has a singleton fibre over
> `f x`, its local-ring map at `x` is of finite presentation.

```lean
lemma finitePresentation_stalkMap_of_preimage_singleton
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f]
    (x : X) (hx : f ⁻¹' {f x} = {x}) (hfp : FinitePresentation f) :
    (f.stalkMap x).hom.FinitePresentation
```

**`AlgebraicGeometry.exists_linearEquiv_stalkPushforward_of_finite_singleton_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/FiniteSingletonFibre.lean#L424). The attribute's comment: “pushforward\_stalk”.

> Let `f : X ⟶ Y` be finite and suppose that the fibre over `f x` is the singleton `{x}`.
> For a quasi-coherent `O_X`-module `F` we have `F_x = (f_* F)_{f x}` as `O_{Y,f x}`-modules:
> the canonical map `TopCat.Presheaf.stalkPushforward` from the stalk of `f_* F` at `f x` to the
> stalk of `F` at `x` (sending the germ of a section over `V` to the germ of the same section
> over `f ⁻¹ V`) is an `O_{Y,f x}`-linear isomorphism, where `O_{Y,f x}` acts on `F_x` through
> the stalk map. The statement provides a linear equivalence whose underlying function is this
> canonical map.

```lean
theorem exists_linearEquiv_stalkPushforward_of_finite_singleton_fiber
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsFinite f]
    (x : X) (hfiber : f ⁻¹' ({f x} : Set Y) = {x})
    (F : X.Modules) [F.IsQuasicoherent] :
    letI : Module (X.presheaf.stalk x)
        ↑(TopCat.Presheaf.stalk F.val.presheaf x) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        (R := X.presheaf) F.val x
    letI : Module (Y.presheaf.stalk (f x))
        ↑(TopCat.Presheaf.stalk F.val.presheaf x) :=
      Module.compHom _ (f.stalkMap x).hom
    letI : Module (Y.presheaf.stalk (f x))
        ↑(TopCat.Presheaf.stalk
          ((Scheme.Modules.pushforward f).obj F).val.presheaf (f x)) :=
      PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
        (R := Y.presheaf) ((Scheme.Modules.pushforward f).obj F).val (f x)
    ∃ e : ↑(TopCat.Presheaf.stalk
          ((Scheme.Modules.pushforward f).obj F).val.presheaf (f x)) ≃ₗ[Y.presheaf.stalk (f x)]
        ↑(TopCat.Presheaf.stalk F.val.presheaf x),
      ⇑e = ConcreteCategory.hom
        (TopCat.Presheaf.stalkPushforward Ab f.base F.val.presheaf x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.47, Tag 052D](https://stacks.math.columbia.edu/tag/052D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
