---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.isOpenMap_comp_of_objects_isFieldSpectrum, AlgebraicGeometry.isSeparated_arrows_of_objects_isSpec_field, Stacks.Groupoids.GroupoidScheme.exists_fieldExtension_sourceFiber_iso_mapping_points, AlgebraicGeometry.surjective_restrictionDiagramMorphisms, AlgebraicGeometry.flat_restrictionDiagramMorphisms, AlgebraicGeometry.universallyOpen_restrictionDiagramMorphisms, AlgebraicGeometry.isAffineHom_restrictionArrowsToArrows, AlgebraicGeometry.GroupoidScheme.exists_isIso_source_target_over_isAlgClosed
statement: formalized
proof: formalized
---

# 40.10 Properties of groupoids on fields

Section 40.10 of the Stacks Project, [Tag 04LL](https://stacks.math.columbia.edu/tag/04LL). 13 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04LM, a lemma

[Tag 04LM](https://stacks.math.columbia.edu/tag/04LM) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isOpenMap_comp_of_objects_isFieldSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CompositionOpen.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/CompositionOpen.lean#L42).

> Composition in a groupoid scheme is an open map when the scheme of objects is the
> spectrum of a field.

```lean
public theorem isOpenMap_comp_of_objects_isFieldSpectrum
    {S : Scheme.{u}} (G : GroupoidScheme S)
    (k : Type u) [Field k] (e : G.objects.left ≅ Spec (.of k)) :
    IsOpenMap G.comp.left
```

## Tag 04LN, a lemma

[Tag 04LN](https://stacks.math.columbia.edu/tag/04LN) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_arrows_of_objects_isSpec_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Separated.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Separated.lean#L50).

> **Stacks Project, Tag 04LN.** The arrow scheme of a groupoid scheme with object scheme the
> spectrum of a field is separated.

```lean
public theorem isSeparated_arrows_of_objects_isSpec_field
    {S : Scheme.{u}} (G : GroupoidScheme S) {k : Type u} [Field k]
    (_ : G.objects.left ≅ Spec (.of k)) : G.arrows.left.IsSeparated
```

## Tag 04LP, a lemma

[Tag 04LP](https://stacks.math.columbia.edu/tag/04LP) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_fieldExtension_sourceFiber_iso_mapping_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionFiber.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionFiber.lean#L94). The attribute's comment: “corrected form: the printed statement, with one base change on both sides of the isomorphism, is false (refuted by Stacks.Groupoids.not\_groupoidOnFieldHomogeneousStatement); this is what its proof via 02YF (1), (2) establishes, with two embeddings of k into k'”.

> If the object scheme of a groupoid scheme is the spectrum of a field `k`, then any two
> points of its arrow scheme lift, after a field extension `k'/k`, to points of two base changes
> of the arrow scheme along the source map which are carried to one another by an isomorphism
> over `Spec k'`.
>
> The two base changes are taken along the two `k`-algebra structures on `k'` that Tag 02YF
> produces, namely the ones induced by the target and by the source of a chosen arrow.  This is
> the corrected form of Tag 04LP: the printed form, an automorphism of a single base change, is
> false (`Stacks.Groupoids.not_groupoidOnFieldHomogeneousStatement`).

```lean
theorem exists_fieldExtension_sourceFiber_iso_mapping_points
    {S : Scheme.{u}} (G : GroupoidScheme S)
    (k : Type u) [Field k] (e : G.objects.left ≅ Spec (.of k))
    (r r' : G.arrows.left) :
    let s : G.arrows.left ⟶ Spec (.of k) := G.source.left ≫ e.hom
    ∃ (k' : Type u) (_ : Field k') (α β : Algebra k k'),
      let gt : Spec (.of k') ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom (@algebraMap k k' _ _ α))
      let gs : Spec (.of k') ⟶ Spec (.of k) :=
        Spec.map (CommRingCat.ofHom (@algebraMap k k' _ _ β))
      let P : Scheme.{u} := pullback s gt
      let P' : Scheme.{u} := pullback s gs
      let POver : Over (Spec (.of k')) := Over.mk (pullback.snd s gt)
      let POver' : Over (Spec (.of k')) := Over.mk (pullback.snd s gs)
      ∃ (r₁ : P) (r₂ : P') (φ : POver ≅ POver'),
        φ.hom.left.base r₁ = r₂ ∧
          (pullback.fst s gt).base r₁ = r ∧
          (pullback.fst s gs).base r₂ = r'
```

## Tag 04LQ, a lemma

[Tag 04LQ](https://stacks.math.columbia.edu/tag/04LQ) in the Stacks Project.

**`AlgebraicGeometry.surjective_restrictionDiagramMorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean#L102). The attribute's comment: “surjectivity”.

> Every morphism in the defining restriction diagram over a field extension is
> surjective.

```lean
public lemma surjective_restrictionDiagramMorphisms {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) (k k' : Type u) [Field k] [Field k']
    (_ : G.objects.left ≅ Spec (.of k)) (_ : U'.left ≅ Spec (.of k'))
    (i : Fin 12) :
    Surjective ((restrictionDiagramMorphisms G g i).hom)
```

**`AlgebraicGeometry.flat_restrictionDiagramMorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean#L115). The attribute's comment: “flatness”.

> Every morphism in the defining restriction diagram over a field extension is flat.

```lean
public lemma flat_restrictionDiagramMorphisms {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) (k k' : Type u) [Field k] [Field k']
    (_ : G.objects.left ≅ Spec (.of k)) (_ : U'.left ≅ Spec (.of k'))
    (i : Fin 12) :
    Flat ((restrictionDiagramMorphisms G g i).hom)
```

**`AlgebraicGeometry.universallyOpen_restrictionDiagramMorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean#L128). The attribute's comment: “universal openness”.

> Every morphism in the defining restriction diagram over a field extension is universally
> open.

```lean
public lemma universallyOpen_restrictionDiagramMorphisms {S : Scheme.{u}}
    (G : GroupoidScheme S) {U' : Over S} (g : U' ⟶ G.objects)
    (k k' : Type u) [Field k] [Field k']
    (_ : G.objects.left ≅ Spec (.of k)) (_ : U'.left ≅ Spec (.of k'))
    (i : Fin 12) :
    UniversallyOpen ((restrictionDiagramMorphisms G g i).hom)
```

**`AlgebraicGeometry.isAffineHom_restrictionArrowsToArrows`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RestrictionOverField.lean#L142). The attribute's comment: “affineness of the dotted morphism”.

> The dotted morphism from the arrow scheme of a restriction to the original arrow scheme
> is affine.

```lean
public lemma isAffineHom_restrictionArrowsToArrows {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) (k k' : Type u) [Field k] [Field k']
    (_ : G.objects.left ≅ Spec (.of k)) (_ : U'.left ≅ Spec (.of k')) :
    IsAffineHom (restrictionArrowsToArrows G g).left
```

## Tag 04LR, a lemma

[Tag 04LR](https://stacks.math.columbia.edu/tag/04LR) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_isIso_source_target_over_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/PointsOverField.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/PointsOverField.lean#L217).

> An arrow over a point of a groupoid scheme on `Spec k` can be lifted after an algebraically
> closed extension of `k` so that both its source and target induce isomorphisms from the
> extending field to the residue field of the lifted point.

```lean
public theorem exists_isIso_source_target_over_isAlgClosed {S : Scheme.{u}} {k : Type u}
    [Field k] (structureMap : Spec (.of k) ⟶ S) (G : GroupoidScheme S)
    (objects_eq : G.objects = Over.mk structureMap) (r : G.arrows.left) :
    ∃ (k' : Type u) (_ : Field k') (_ : IsAlgClosed k') (i : k →+* k'),
      let g : Over.mk (Scheme.Spec.map (CommRingCat.ofHom i).op ≫ structureMap) ⟶ G.objects :=
        extensionMap structureMap i ≫ eqToHom objects_eq.symm
      ∃ (r' : Spec (.of k') ⟶ (restrictionArrows G g).left),
      let rPoint := r' (IsLocalRing.closedPoint k')
      (restrictionArrowsToArrows G g).left rPoint = r ∧
        IsIso ((restrictionSource G g).left.residueFieldMap rPoint) ∧
        IsIso ((restrictionTarget G g).left.residueFieldMap rPoint)
```

## Tag 04LS, a lemma

[Tag 04LS](https://stacks.math.columbia.edu/tag/04LS) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.translationByPoint_isIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Translation.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/Translation.lean#L459). The attribute's comment: “the automorphism”.

> **Stacks Project, Tag 04LS.** Translation by a point whose source and target induce
> isomorphisms on residue fields is an automorphism of the arrow scheme.

```lean
public lemma translationByPoint_isIso {S : Scheme.{u}} (G : GroupoidScheme S)
    (k : Type u) [Field k] (hU : G.objects.left = Spec (.of k))
    (r : G.arrows.left) [IsIso (G.source.left.residueFieldMap r)]
    [IsIso (G.target.left.residueFieldMap r)] :
    IsIso (translationByPoint G k hU r)
```

**`AlgebraicGeometry.GroupoidScheme.identity_image_translationByPoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Translation.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/Translation.lean#L472). The attribute's comment: “image of the identity”.

> **Stacks Project, Tag 04LS.** Translation by `r` maps the identity arrow at the source of
> `r` to `r`.

```lean
public lemma identity_image_translationByPoint {S : Scheme.{u}} (G : GroupoidScheme S)
    (k : Type u) [Field k] (hU : G.objects.left = Spec (.of k))
    (r : G.arrows.left) [IsIso (G.source.left.residueFieldMap r)] :
    (G.identity ≫ translationByPoint G k hU r).left (G.source.left r) = r
```

## Tag 0B7V, a lemma

[Tag 0B7V](https://stacks.math.columbia.edu/tag/0B7V) in the Stacks Project.

**`AlgebraicGeometry.isOpen_image_comp_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/OpenTranslates.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/OpenTranslates.lean#L254).

> **Stacks Project, Tag 0B7V.** If the objects of a groupoid scheme form the spectrum
> of a field, the image of the composition of a family of arrows with an open set of arrows
> is open.

```lean
public theorem isOpen_image_comp_of_isOpen
    {S : Scheme.{u}} (G : GroupoidScheme S) (k : Type u) [Field k]
    (hobjects : G.objects.left ≅ Spec (.of k))
    (Z : Over S) (f : Z ⟶ G.arrows) (W : G.arrows.left.Opens) :
    let p := pullback.snd f (pullback.fst G.source G.target)
    IsOpen ((p ≫ G.comp).left.base ''
      {x | (p ≫ pullback.snd G.source G.target).left.base x ∈ W})
```

## Tag 04LT, a lemma

[Tag 04LT](https://stacks.math.columbia.edu/tag/04LT) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.existsUnique_minimalPrime_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean#L575). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 04LT.** Every local ring of the arrows of a groupoid scheme over a
> field has a unique minimal prime ideal.

```lean
public theorem existsUnique_minimalPrime_stalk {S : Scheme.{u}} (G : GroupoidScheme S)
    (k : Type u) [Field k] (hU : G.objects.left = Spec (.of k))
    (r : G.arrows.left) :
    ∃! p : Ideal (G.arrows.left.presheaf.stalk r),
      p ∈ minimalPrimes (G.arrows.left.presheaf.stalk r)
```

**`AlgebraicGeometry.GroupoidScheme.existsUnique_irreducibleComponent_containing_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean#L633). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 04LT.** There is exactly one irreducible component of the arrow scheme
> containing the identity section.

```lean
public theorem existsUnique_irreducibleComponent_containing_identity
    {S : Scheme.{u}} (G : GroupoidScheme S) (k : Type u) [Field k]
    (hU : G.objects.left = Spec (.of k)) :
    ∃! Z : irreducibleComponents G.arrows.left,
      Set.range G.identity.left ⊆ (Z : Set G.arrows.left)
```

**`AlgebraicGeometry.GroupoidScheme.geometricallyIrreducible_irreducibleComponent_of_identity_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean, line 838](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean#L838). The attribute's comment: “part (3), source”. References: EGA IV (15.6.10), “partial”; SGA 3 VIA (2.6.2), “more general”; SGA 3 VIA (2.6.5), “more general”.

> **Stacks Project, Tag 04LT.** The component containing the identity is geometrically
> irreducible over the field via the source morphism.

```lean
public theorem geometricallyIrreducible_irreducibleComponent_of_identity_source
    {S : Scheme.{u}} (G : GroupoidScheme S) (k : Type u) [Field k]
    (hU : G.objects.left = Spec (.of k)) (Z : irreducibleComponents G.arrows.left)
    (he : Set.range G.identity.left ⊆ (Z : Set G.arrows.left)) :
    GeometricallyIrreducible
      ((Scheme.IdealSheafData.vanishingIdeal
        (⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩ :
          Closeds G.arrows.left)).subschemeι ≫ G.source.left ≫ eqToHom hU)
```

**`AlgebraicGeometry.GroupoidScheme.geometricallyIrreducible_irreducibleComponent_of_identity_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean, line 855](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IrreducibleComponents.lean#L855). The attribute's comment: “part (3), target”. References: EGA IV (15.6.10), “partial”; SGA 3 VIA (2.6.2), “more general”; SGA 3 VIA (2.6.5), “more general”.

> **Stacks Project, Tag 04LT.** The component containing the identity is geometrically
> irreducible over the field via the target morphism.

```lean
public theorem geometricallyIrreducible_irreducibleComponent_of_identity_target
    {S : Scheme.{u}} (G : GroupoidScheme S) (k : Type u) [Field k]
    (hU : G.objects.left = Spec (.of k)) (Z : irreducibleComponents G.arrows.left)
    (he : Set.range G.identity.left ⊆ (Z : Set G.arrows.left)) :
    GeometricallyIrreducible
      ((Scheme.IdealSheafData.vanishingIdeal
        (⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩ :
          Closeds G.arrows.left)).subschemeι ≫ G.target.left ≫ eqToHom hU)
```

## Tag 04LU, a lemma

[Tag 04LU](https://stacks.math.columbia.edu/tag/04LU) in the Stacks Project.

**`AlgebraicGeometry.trdeg_residueField_eq_of_target_isSpec_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean#L159). The attribute's comment: “transcendence\_degrees”.

> **Stacks Project, Tag 04LU.** The transcendence degree of the residue field at a point of a
> scheme over the residue field of its image does not depend on which morphism locally of finite
> type to the spectrum of a field is used.

```lean
theorem trdeg_residueField_eq_of_target_isSpec_field {X Y : Scheme.{u}} {k : Type u} [Field k]
    (e : Y ≅ Spec (.of k)) (f g : X ⟶ Y) [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (x : X) :
    letI : Algebra (Y.residueField (f x)) (X.residueField x) :=
      (f.residueFieldMap x).hom.toAlgebra
    letI : Algebra (Y.residueField (g x)) (X.residueField x) :=
      (g.residueFieldMap x).hom.toAlgebra
    Algebra.trdeg (Y.residueField (f x)) (X.residueField x) =
      Algebra.trdeg (Y.residueField (g x)) (X.residueField x)
```

**`AlgebraicGeometry.GroupoidScheme.topologicalKrullDim_arrows_eq_topologicalKrullDimAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean#L230). The attribute's comment: “dimension\_at\_every\_point”.

> **Stacks Project, Tag 04LU.** The dimension of the arrow scheme of a groupoid scheme whose
> object scheme is the spectrum of a field is its local dimension at every point, provided both
> structure morphisms are locally of finite type.

```lean
theorem topologicalKrullDim_arrows_eq_topologicalKrullDimAt {S : Scheme.{u}}
    (G : GroupoidScheme S) {k : Type u} [Field k] (e : G.objects.left ≅ Spec (.of k))
    [LocallyOfFiniteType G.source.left] [LocallyOfFiniteType G.target.left]
    (r : G.arrows.left) :
    topologicalKrullDim G.arrows.left = topologicalKrullDimAt G.arrows.left r
```

**`AlgebraicGeometry.GroupoidScheme.topologicalKrullDim_arrows_eq_ringKrullDim_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean#L244). The attribute's comment: “dimension\_at\_closed\_point”.

> **Stacks Project, Tag 04LU.** At a closed point of the arrow scheme of a groupoid scheme
> whose object scheme is the spectrum of a field, the dimension of the arrow scheme is the Krull
> dimension of the local ring.

```lean
theorem topologicalKrullDim_arrows_eq_ringKrullDim_stalk {S : Scheme.{u}}
    (G : GroupoidScheme S) {k : Type u} [Field k] (e : G.objects.left ≅ Spec (.of k))
    [LocallyOfFiniteType G.source.left] [LocallyOfFiniteType G.target.left]
    (r : G.arrows.left) (hr : IsClosed ({r} : Set G.arrows.left)) :
    topologicalKrullDim G.arrows.left = ringKrullDim (G.arrows.left.presheaf.stalk r)
```

**`AlgebraicGeometry.GroupoidScheme.equidimensional_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Dimension.lean#L257). The attribute's comment: “equidimensional”.

> **Stacks Project, Tag 04LU.** The arrow scheme of a groupoid scheme whose object scheme is
> the spectrum of a field is equidimensional, provided both structure morphisms are locally of
> finite type.

```lean
theorem equidimensional_arrows {S : Scheme.{u}} (G : GroupoidScheme S) {k : Type u} [Field k]
    (e : G.objects.left ≅ Spec (.of k)) [LocallyOfFiniteType G.source.left]
    [LocallyOfFiniteType G.target.left] :
    Equidimensional G.arrows.left
```

## Tag 04MQ, a lemma

[Tag 04MQ](https://stacks.math.columbia.edu/tag/04MQ) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.topologicalKrullDim_arrows_eq_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/StabilizerDimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/StabilizerDimension.lean#L142).

> **Stacks Project, Tag 04MQ.** The arrow scheme of a groupoid scheme whose object scheme is
> the spectrum of a field has the same dimension as its stabilizer group scheme, provided both
> structure morphisms are locally of finite type.

```lean
theorem topologicalKrullDim_arrows_eq_stabilizer
    {S : Scheme.{u}} (G : GroupoidScheme S)
    {k : Type u} [Field k] (e : G.objects.left ≅ Spec (.of k))
    [LocallyOfFiniteType G.source.left] [LocallyOfFiniteType G.target.left] :
    topologicalKrullDim G.arrows.left = topologicalKrullDim (stabilizer G).left
```

## Tag 04MR, a remark

[Tag 04MR](https://stacks.math.columbia.edu/tag/04MR) in the Stacks Project.

**`AlgebraicGeometry.RationalFunctionPairGroupoid.groupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L701). The attribute's comment: “the groupoid scheme of the warning, as the pair groupoid of Spec Q(x) over Q”.

> **The groupoid scheme of the warning.**  The restriction of the groupoid scheme of the
> multiplicative action of `𝐆_{m,𝐐}` on `𝐀¹_𝐐` to the generic point of `𝐀¹_𝐐`, presented as the
> pair groupoid of `Spec 𝐐(x) → Spec 𝐐`: its object scheme is `Spec 𝐐(x)`, the spectrum of a
> field, and its arrow scheme is `Spec 𝐐(x) ×_{Spec 𝐐} Spec 𝐐(x)`, whose ring of functions is
> the arrow ring `𝐐(x)[Y][1/P(Y)]` of the source.

```lean
noncomputable def groupoid : GroupoidScheme (Spec (CommRingCat.of ℚ))
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.topologicalKrullDim_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 734](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L734). The attribute's comment: “dim G = 0”.

> The stabilizer group scheme has dimension zero: the second projection of its defining
> square carries it isomorphically onto `Spec 𝐐(x)`.

```lean
theorem topologicalKrullDim_stabilizer :
    topologicalKrullDim (stabilizer groupoid).left = 0
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.topologicalKrullDim_arrows_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 761](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L761). The attribute's comment: “dim R = 1”.

> The arrow scheme has dimension one.

```lean
theorem topologicalKrullDim_arrows_eq_one :
    topologicalKrullDim groupoid.arrows.left = 1
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.topologicalKrullDim_arrows_ne_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L773). The attribute's comment: “dim R = 1 ≠ 0 = dim G there, so the conclusion of Tag 04MQ fails for this groupoid scheme; that its source and target are not locally of finite type, which is the hypothesis of Tag 04MQ the example drops, is proved below”.

> **The conclusion of Tag 04MQ fails for this groupoid scheme.**  Its object scheme is the
> spectrum of a field, yet the dimension of its arrow scheme is not the dimension of its
> stabilizer group scheme: the stabilizer has dimension zero and the arrows have dimension one.
> The source and target morphisms are not locally of finite type, which is the hypothesis of
> Tag 04MQ that this example drops.

```lean
theorem topologicalKrullDim_arrows_ne_stabilizer :
    topologicalKrullDim groupoid.arrows.left
      ≠ topologicalKrullDim (stabilizer groupoid).left
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.not_locallyOfFiniteType_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 790](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L790). The attribute's comment: “s is not locally of finite type”.

> **The source of the groupoid scheme is not locally of finite type.**  On rings it is the
> inclusion of `𝐐(x)` into `𝐐(x) ⊗_𝐐 𝐐(x)` as the right factor, which is not of finite type.

```lean
theorem not_locallyOfFiniteType_source : ¬ LocallyOfFiniteType groupoid.source.left
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.not_locallyOfFiniteType_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 803](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L803). The attribute's comment: “t is not locally of finite type”.

> **The target of the groupoid scheme is not locally of finite type.**  On rings it is the
> inclusion of `𝐐(x)` into `𝐐(x) ⊗_𝐐 𝐐(x)` as the left factor, which is not of finite type.

```lean
theorem not_locallyOfFiniteType_target : ¬ LocallyOfFiniteType groupoid.target.left
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.exists_dim_arrows_eq_one_dim_stabilizer_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 832](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L832). The attribute's comment: “the example in full: U = Spec Q(x) with Q(x) a field, R = Spec (Q(x)[y][1/P(xy)]), s and t are not locally of finite type, dim R = 1 and dim G = 0”.

> **The example of Tag 04MR, in full.**  There is a groupoid scheme whose object scheme is
> the spectrum of a field — here `𝐐(x)` — whose arrow scheme is `Spec (𝐐(x)[y][1/P(xy)])`, whose
> source and target morphisms are not locally of finite type, and for which the dimension of the
> arrow scheme is one while the dimension of the stabilizer group scheme is zero.

```lean
theorem exists_dim_arrows_eq_one_dim_stabilizer_eq_zero :
    ∃ (k : Type) (_ : Field k) (G : GroupoidScheme (Spec (CommRingCat.of ℚ))),
      G.objects.left = Spec (CommRingCat.of k) ∧
        Nonempty (G.arrows.left ≅ Spec (CommRingCat.of sourceArrowRing)) ∧
        ¬ LocallyOfFiniteType G.source.left ∧
        ¬ LocallyOfFiniteType G.target.left ∧
        topologicalKrullDim G.arrows.left = 1 ∧
        topologicalKrullDim (stabilizer G).left = 0
```

**`AlgebraicGeometry.RationalFunctionPairGroupoid.not_forall_dim_arrows_eq_dim_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean, line 848](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/DimensionWithoutFiniteType.lean#L848). The attribute's comment: “Tag 04MQ is wrong without the condition that s and t are locally of finite type”.

> **The warning of Tag 04MR.**  Tag 04MQ is wrong without the condition that `s` and `t` are
> locally of finite type: for a groupoid scheme whose object scheme is the spectrum of a field,
> the dimension of the arrow scheme need not be the dimension of the stabilizer group scheme.

```lean
theorem not_forall_dim_arrows_eq_dim_stabilizer :
    ¬ ∀ (S : Scheme.{0}) (G : GroupoidScheme S) (k : Type) (_ : Field k),
        G.objects.left = Spec (CommRingCat.of k) →
          topologicalKrullDim G.arrows.left = topologicalKrullDim (stabilizer G).left
```

## Tag 04RA, a lemma

[Tag 04RA](https://stacks.math.columbia.edu/tag/04RA) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.smooth_source_left_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean#L195). The attribute's comment: “the source morphism”. References: SGA 3 VIB (1.6), “special case”; SGA 3 XVII (5.5), “partial”.

> **[Stacks Project, Tag 04RA]: the source morphism of a groupoid scheme on a field of
> characteristic zero is smooth.** If the scheme of objects of a groupoid scheme is the spectrum of
> a field of characteristic zero and the source morphism is locally of finite type, then the source
> morphism is smooth.
>
> The sheaf of differentials `Ω_{R/U}` is free by
> `Stacks.Groupoids.GroupoidScheme.exists_free_iso_relativeDifferentials_source_left`, and a
> scheme locally of finite type over a field of characteristic zero whose differentials are locally
> free is smooth by [Stacks Project, Tag 04QN].

```lean
theorem smooth_source_left_of_charZero [CharZero k] (e : G.objects.left ≅ Spec (.of k))
    [LocallyOfFiniteType G.source.left] : Smooth G.source.left
```

**`Stacks.Groupoids.GroupoidScheme.smooth_target_left_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean#L206). The attribute's comment: “the target morphism”. References: SGA 3 XVII (5.5), “partial”.

> **[Stacks Project, Tag 04RA]: the target morphism of a groupoid scheme on a field of
> characteristic zero is smooth.** This is the previous statement transported along the inverse,
> which is an automorphism of the scheme of arrows carrying the source morphism to the target
> morphism.

```lean
theorem smooth_target_left_of_charZero [CharZero k] (e : G.objects.left ≅ Spec (.of k))
    [LocallyOfFiniteType G.source.left] : Smooth G.target.left
```

## Tag 04RB, a lemma

[Tag 04RB](https://stacks.math.columbia.edu/tag/04RB) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.smooth_source_left_of_isReduced_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean#L222). The attribute's comment: “the source morphism”.

> **[Stacks Project, Tag 04RB]: the source morphism of a groupoid scheme with reduced scheme of
> arrows on a perfect field is smooth.** If the scheme of objects of a groupoid scheme is the
> spectrum of a perfect field, the source morphism is locally of finite type and the scheme of
> arrows is reduced, then the source morphism is smooth.
>
> The sheaf of differentials `Ω_{R/U}` is free by
> `Stacks.Groupoids.GroupoidScheme.exists_free_iso_relativeDifferentials_source_left`, and a
> reduced scheme locally of finite type over a perfect field whose differentials are locally free
> is smooth by [Stacks Project, Tag 04QP].

```lean
theorem smooth_source_left_of_isReduced_of_perfectField [PerfectField k]
    (e : G.objects.left ≅ Spec (.of k)) [IsReduced G.arrows.left]
    [LocallyOfFiniteType G.source.left] : Smooth G.source.left
```

**`Stacks.Groupoids.GroupoidScheme.smooth_target_left_of_isReduced_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Smooth.lean#L234). The attribute's comment: “the target morphism”.

> **[Stacks Project, Tag 04RB]: the target morphism of a groupoid scheme with reduced scheme of
> arrows on a perfect field is smooth.** This is the previous statement transported along the
> inverse, which is an automorphism of the scheme of arrows carrying the source morphism to the
> target morphism.

```lean
theorem smooth_target_left_of_isReduced_of_perfectField [PerfectField k]
    (e : G.objects.left ≅ Spec (.of k)) [IsReduced G.arrows.left]
    [LocallyOfFiniteType G.source.left] : Smooth G.target.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.10, Tag 04LL](https://stacks.math.columbia.edu/tag/04LL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
