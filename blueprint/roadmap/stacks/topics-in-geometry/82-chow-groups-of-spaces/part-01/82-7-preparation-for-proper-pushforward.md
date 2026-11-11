---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IntegralClosedSubspace.existsUnique_isDominant_hom_of_isGood, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueField, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueFieldMorphism_spec, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueFieldRepresentative_unique, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.exists_denseRange_isRepresentable_isOpenSubspace_of_isGood, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.exists_ringEquiv_residueField_schemeResidueField, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.isField_functionField, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.functionFieldRingEquiv
statement: formalized
proof: formalized
---

# 82.7 Preparation for proper pushforward

Section 82.7 of the Stacks Project, [Tag 0EEF](https://stacks.math.columbia.edu/tag/0EEF). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EEG, a lemma

[Tag 0EEG](https://stacks.math.columbia.edu/tag/0EEG) in the Stacks Project.

**`AlgebraicGeometry.Space.IntegralClosedSubspace.existsUnique_isDominant_hom_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralClosedImage.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralClosedImage.lean#L259).

> **Stacks 0EEG.** In Situation 0EDT, let `X` and `Y` be good algebraic spaces over the base
> and let `f : X ⟶ Y` be a morphism over the base. For an integral closed subspace `Z ⊂ X` there
> is exactly one integral closed subspace `Z' ⊂ Y` admitting a morphism `Z ⟶ Z'` over `f` — that
> is, one making the square with `Z ⟶ X`, `Z' ⟶ Y` and `f` commute — which is dominant; and if
> `f` is proper, then every such morphism is proper and surjective. Every morphism making that
> square commute is a morphism over the base, so the whole diagram is one over the base.
>
> The subspace is `AlgebraicGeometry.Space.IntegralClosedSubspace.closureImage` at `f`, the
> integral closed subspace of `Y` on the closure of the image of `|Z|`.

```lean
theorem IntegralClosedSubspace.existsUnique_isDominant_hom_of_isGood (pX : X ⟶ D.space)
    (pY : Y ⟶ D.space) (hX : D.IsGood pX) (hY : D.IsGood pY) (f : X ⟶ Y) (hf : f ≫ pY = pX)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) :
    (∃! Z' : IntegralClosedSubspace D.site D.base D.base_mem Y,
        ∃ g : Z.subspace.toFunctor ⟶ Z'.subspace.toFunctor,
          g ≫ Z'.subspace.ι = Z.subspace.ι ≫ f ∧
            IsDominant D.site D.base D.base_mem g) ∧
      (∀ (Z' : IntegralClosedSubspace D.site D.base D.base_mem Y)
          (g : Z.subspace.toFunctor ⟶ Z'.subspace.toFunctor),
          g ≫ Z'.subspace.ι = Z.subspace.ι ≫ f →
            g ≫ Z'.subspace.ι ≫ pY = Z.subspace.ι ≫ pX) ∧
      (IsProper D.site D.base D.base_mem f →
        ∀ (Z' : IntegralClosedSubspace D.site D.base D.base_mem Y)
          (g : Z.subspace.toFunctor ⟶ Z'.subspace.toFunctor),
          g ≫ Z'.subspace.ι = Z.subspace.ι ≫ f → IsDominant D.site D.base D.base_mem g →
            IsProper D.site D.base D.base_mem g ∧
              IsSurjective D.site D.base D.base_mem g)
```

## Tag 0ENW, a remark

[Tag 0ENW](https://stacks.math.columbia.edu/tag/0ENW) in the Stacks Project.

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean#L159).

> The residue field `κ(x)` of a good algebraic space over the base of a
> `BaseSpaceDimensionSituation` at a point `x` of `|X|`: the field of the monomorphism from a field
> spectrum representing `x`.

```lean
noncomputable abbrev BaseSpaceDimensionSituation.residueField (f : X ⟶ D.space)
    (hf : D.IsGood f) (x : points D.site D.base D.base_mem X) : Type u
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueFieldMorphism_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean#L176). The attribute's comment: “a point is represented by a monomorphism from the spectrum of its residue field”.

> A point `x` of a good algebraic space over the base of a `BaseSpaceDimensionSituation` is
> represented by the morphism `Spec κ(x) ⟶ X` out of the spectrum of its residue field, and that
> morphism is a monomorphism.

```lean
theorem BaseSpaceDimensionSituation.residueFieldMorphism_spec (f : X ⟶ D.space)
    (hf : D.IsGood f) (x : points D.site D.base D.base_mem X) :
    (D.residueFieldRepresentative f hf x).1.class D.site D.base D.base_mem X = x ∧
      Mono (D.residueFieldMorphism f hf x)
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueFieldRepresentative_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean#L187). The attribute's comment: “the monomorphism from a field spectrum representing a point is unique up to unique isomorphism over the space”.

> The monomorphism from a field spectrum representing a point `x` of a good algebraic space
> over the base of a `BaseSpaceDimensionSituation` is unique: any monomorphic field-valued
> representative of `x` is uniquely isomorphic, over the space, to `Spec κ(x) ⟶ X`.

```lean
theorem BaseSpaceDimensionSituation.residueFieldRepresentative_unique (f : X ⟶ D.space)
    (hf : D.IsGood f) (x : points D.site D.base D.base_mem X)
    (q : FieldValuedPoint D.site D.base D.base_mem X)
    (hq : q.class D.site D.base D.base_mem X = x)
    (hmq : Mono (fieldMorphism D.site D.base D.base_mem X q)) :
    ∃! e : yoneda.obj ((D.residueFieldRepresentative f hf x).1.siteObject
        D.site D.base D.base_mem X) ≅
        yoneda.obj (q.siteObject D.site D.base D.base_mem X),
      e.hom ≫ fieldMorphism D.site D.base D.base_mem X q = D.residueFieldMorphism f hf x
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.exists_denseRange_isRepresentable_isOpenSubspace_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean#L202). The attribute's comment: “a good algebraic space has a dense open subspace which is a scheme”.

> A good algebraic space over the base of a `BaseSpaceDimensionSituation` has a dense open
> subspace which is a scheme.

```lean
theorem BaseSpaceDimensionSituation.exists_denseRange_isRepresentable_isOpenSubspace_of_isGood
    (f : X ⟶ D.space) (hf : D.IsGood f) :
    ∃ G : Subfunctor X, IsOpenSubspace D.site D.base D.base_mem G ∧
      G.toFunctor.IsRepresentable ∧
      DenseRange (pointsMap D.site D.base D.base_mem G.toFunctor G.ι)
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.exists_ringEquiv_residueField_schemeResidueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ResidueFieldAtPoint.lean#L217). The attribute's comment: “at a point of an open subspace which is a scheme the residue field agrees with the residue field of the corresponding point on that scheme”.

> Let `X/B` be good over the base of a `BaseSpaceDimensionSituation` and let `U ⊆ X` be an
> open subspace which is a scheme, presented by an open immersion out of the presheaf
> represented by an object of the site. At a point `x` of `|X|` coming from a point `u` of that
> scheme, the residue field `κ(x)` agrees with the residue field of `u` on `U` as a scheme: they
> are isomorphic by an isomorphism whose spectrum is the comparison morphism over `X`.

```lean
theorem BaseSpaceDimensionSituation.exists_ringEquiv_residueField_schemeResidueField
    (f : X ⟶ D.space) (hf : D.IsGood f) (T : BigFppfOver D.site D.base D.base_mem)
    (j : yoneda.obj T ⟶ X) (hj : IsOpenImmersion D.site D.base D.base_mem j)
    (u : (BigFppfOver.toScheme D.site D.base D.base_mem).obj T)
    (x : points D.site D.base D.base_mem X)
    (hu : pointsMap D.site D.base D.base_mem (yoneda.obj T) j
      ((schemePointRepresentative D.site D.base D.base_mem T u).class
        D.site D.base D.base_mem (yoneda.obj T)) = x) :
    ∃ (φ : D.residueField f hf x ≃+*
        ((BigFppfOver.toScheme D.site D.base D.base_mem).obj T).residueField u)
      (g : (schemePointRepresentative D.site D.base D.base_mem T u).siteObject
          D.site D.base D.base_mem (yoneda.obj T) ⟶
        (D.residueFieldRepresentative f hf x).1.siteObject D.site D.base D.base_mem X),
      D.site.inclusion.map g.left = Spec.map (CommRingCat.ofHom φ.toRingHom) ∧
        yoneda.map g ≫ D.residueFieldMorphism f hf x =
          yoneda.map (schemePointRepresentative D.site D.base D.base_mem T u).siteHom ≫ j
```

## Tag 0ENX, a remark

[Tag 0ENX](https://stacks.math.columbia.edu/tag/0ENX) in the Stacks Project.

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.isField_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean#L205). The attribute's comment: “the function field R(X) of a good integral algebraic space is defined: its ring of rational functions is a field”.

> In the situation of Stacks 0EDT let `X/B` be good and let `X` be integral. Then the
> function field `R(X)` of `X` is defined: the ring of rational functions of
> `X` is a field.

```lean
theorem BaseSpaceDimensionSituation.isField_functionField (f : X ⟶ D.space)
    (hf : D.IsGood f) (hInt : IsIntegralSpace D.site D.base D.base_mem X) :
    IsField (rationalFunctions D.site D.base D.base_mem hf.1)
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.functionFieldRingEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean#L214). The attribute's comment: “the function field R(X) of a good integral algebraic space is the residue field at its generic point”.

> In the situation of Stacks 0EDT let `X/B` be good and let `X` be integral. Then the
> function field `R(X)` of `X` is the residue field of `X` at its generic point.

```lean
noncomputable def BaseSpaceDimensionSituation.functionFieldRingEquiv (f : X ⟶ D.space)
    (hf : D.IsGood f) (hInt : IsIntegralSpace D.site D.base D.base_mem X) :
    rationalFunctions D.site D.base D.base_mem hf.1 ≃+*
      residueField D.site D.base D.base_mem X hInt.2.1
        (genericPoint D.site D.base D.base_mem hf.1 hInt)
```

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.residueFieldRingEquivFunctionField`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FunctionFieldAtPoint.lean#L226). The attribute's comment: “for any point x of a good algebraic space, the residue field κ(x) is the function field of the unique integral closed subspace whose generic point is x”.

> In the situation of Stacks 0EDT let `X/B` be good. For a point `ξ` of `X` the residue field
> `κ(ξ)` is the function field of the unique integral closed subspace `Z ⊆ X` whose generic point
> is `ξ`.

```lean
noncomputable def BaseSpaceDimensionSituation.residueFieldRingEquivFunctionField
    (f : X ⟶ D.space) (hf : D.IsGood f) (ξ : points D.site D.base D.base_mem X) :
    residueField D.site D.base D.base_mem X (D.isDecentSpace_of_isGood f hf) ξ ≃+*
      rationalFunctions D.site D.base D.base_mem
        (integralClosedSubspaceOfPoint D.site D.base D.base_mem hf.1
          (D.isDecentSpace_of_isGood f hf) ξ).isClosedSubspace.1
```

## Tag 0ENY, a lemma

[Tag 0ENY](https://stacks.math.columbia.edu/tag/0ENY) in the Stacks Project.

**`AlgebraicGeometry.Space.factorsThrough_properIntegralClosedSubspace_or_isDominant_and_finite_functionField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EqualDeltaDimension.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EqualDeltaDimension.lean#L627).

> **Stacks 0ENY.** In Situation 0EDT let `X` and `Y` be good integral algebraic spaces over
> the fixed base with `dim_δ(X) = dim_δ(Y)`, and let `f : X ⟶ Y` be a morphism over the base.
> Then **either** `f` factors through a proper closed subspace of `Y` — namely the integral
> closed subspace of `Y` on the closure of the image of `|X|`, whose set of points is strictly
> smaller than `|Y|` — **or** `f` is dominant, carries the generic point of `X` to the generic
> point of `Y`, and the extension of function fields `R(X)/R(Y)` it induces is finite.
>
> The function fields are the residue fields at the generic points, by Stacks 0END, and the
> extension is the homomorphism `f` induces on them; finiteness is finiteness as a module.
>
> If the image of `|X|` is not dense its closure is an irreducible closed proper subset of
> `|Y|`, and `X` is reduced, so `f` factors through the integral closed subspace on it by
> Stacks 03IQ and Stacks 03JJ. If the image is dense, then `f` is dominant and carries the
> generic point to the generic point; equality of the δ-dimensions makes the relative
> transcendence degree at the generic point vanish, and then Spaces over Fields, Lemma 0AD5
> gives finiteness.

```lean
theorem factorsThrough_properIntegralClosedSubspace_or_isDominant_and_finite_functionField
    (pX : X ⟶ D.space) (pY : Y ⟶ D.space) (hX : D.IsGood pX) (hY : D.IsGood pY)
    (hXInt : IsIntegralSpace D.site D.base D.base_mem X)
    (hYInt : IsIntegralSpace D.site D.base D.base_mem Y) (f : X ⟶ Y) (hf : f ≫ pY = pX)
    (hdim : deltaDimensionClosed D pX hX Set.univ isClosed_univ =
      deltaDimensionClosed D pY hY Set.univ isClosed_univ) :
    (∃ Z : IntegralClosedSubspace D.site D.base D.base_mem Y,
        subspacePointSet D.site D.base D.base_mem Y Z.subspace ≠ Set.univ ∧
          ∃ g : X ⟶ Z.subspace.toFunctor, g ≫ Z.subspace.ι = f) ∨
      (IsDominant D.site D.base D.base_mem f ∧
        pointsMap D.site D.base D.base_mem X f
            (genericPoint D.site D.base D.base_mem hX.1 hXInt) =
          genericPoint D.site D.base D.base_mem hY.1 hYInt ∧
        letI := (residueFieldHom D.site D.base D.base_mem X Y hY.1 hXInt.2.1 hYInt.2.1 f
          (genericPoint D.site D.base D.base_mem hX.1 hXInt)).toAlgebra
        Module.Finite
          (residueField D.site D.base D.base_mem Y hYInt.2.1
            (pointsMap D.site D.base D.base_mem X f
              (genericPoint D.site D.base D.base_mem hX.1 hXInt)))
          (residueField D.site D.base D.base_mem X hXInt.2.1
            (genericPoint D.site D.base D.base_mem hX.1 hXInt)))
```

## Tag 0ENZ, a lemma

[Tag 0ENZ](https://stacks.math.columbia.edu/tag/0ENZ) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyFinite_closure_image_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforward.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforward.lean#L66).

> **Stacks 0ENZ.** Let `X/B` and `Y/B` be good algebraic spaces over the base of the theory
> of cycles and let `f : X ⟶ Y` be a quasi-compact morphism over `B`. The closures of the images
> under `|f|` of a locally finite collection of closed subsets of `|X|` form a locally finite
> collection of closed subsets of `|Y|`.

```lean
theorem locallyFinite_closure_image_pointsMap
    {X Y : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u}
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY)
    {f : X ⟶ Y} (_hfB : f ≫ sY = sX)
    (hf : IsQuasiCompact D.site D.base D.base_mem f)
    {I : Type v} (T : I → Set (points D.site D.base D.base_mem X))
    (_hT : ∀ i, IsClosed (T i)) (hTlf : LocallyFinite T) :
    LocallyFinite (fun i ↦ closure (pointsMap D.site D.base D.base_mem X f '' T i)) ∧
      ∀ i, IsClosed (closure (pointsMap D.site D.base D.base_mem X f '' T i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.7, Tag 0EEF](https://stacks.math.columbia.edu/tag/0EEF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
