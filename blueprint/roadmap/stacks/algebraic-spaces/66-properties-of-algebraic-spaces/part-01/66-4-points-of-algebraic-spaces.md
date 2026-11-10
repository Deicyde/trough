---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.points, AlgebraicGeometry.Space.FieldValuedPoint.hasCommonExtension_trans, AlgebraicGeometry.Space.FieldValuedPoint.class_eq_class_iff, AlgebraicGeometry.Space.bijective_pointsToScheme, AlgebraicGeometry.Space.exists_pointsULift_of_isPullback, AlgebraicGeometry.Space.exists_points_of_isPullback, AlgebraicGeometry.Space.exists_point_of_isPullback_presheaf, AlgebraicGeometry.Space.exists_point_of_isPullback
statement: formalized
proof: formalized
---

# 66.4 Points of algebraic spaces

Section 66.4 of the Stacks Project, [Tag 03BT](https://stacks.math.columbia.edu/tag/03BT). 12 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03BU, a definition

[Tag 03BU](https://stacks.math.columbia.edu/tag/03BU) in the Stacks Project.

**`AlgebraicGeometry.Space.points`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Points.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Points.lean#L222). The attribute's comment: “set of points”.

> **Stacks 03BU.** Points of an algebraic space are equivalence classes of its
> field-valued points.

```lean
abbrev points : Type (u + 1)
```

**`AlgebraicGeometry.Space.FieldValuedPoint.hasCommonExtension_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Points.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Points.lean#L232). The attribute's comment: “equivalence of field-valued points”.

> **Stacks 03BU.** Common extension is transitive: two extensions of a field-valued point
> can be amalgamated over that point.

```lean
theorem FieldValuedPoint.hasCommonExtension_trans
    {p q r : FieldValuedPoint B S hS F}
    (hpq : FieldValuedPoint.HasCommonExtension B S hS F p q)
    (hqr : FieldValuedPoint.HasCommonExtension B S hS F q r) :
    FieldValuedPoint.HasCommonExtension B S hS F p r
```

**`AlgebraicGeometry.Space.FieldValuedPoint.class_eq_class_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Points.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Points.lean#L276). The attribute's comment: “equality of points”.

> **Stacks 03BU.** Two field-valued representatives define the same point exactly when
> they admit a common field-valued extension.

```lean
theorem FieldValuedPoint.class_eq_class_iff
    (p q : FieldValuedPoint B S hS F) :
    p.class B S hS F = q.class B S hS F ↔
      FieldValuedPoint.HasCommonExtension B S hS F p q
```

## Tag 03BV, a lemma

[Tag 03BV](https://stacks.math.columbia.edu/tag/03BV) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_pointsToScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsRepresentable.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsRepresentable.lean#L184).

> The points of a scheme, viewed as an algebraic space through its functor
> of points, are in canonical one-to-one correspondence with the points of the representing
> scheme, the correspondence being `AlgebraicGeometry.Space.pointsToScheme`.

```lean
theorem bijective_pointsToScheme (U : BigFppfOver B S hS) :
    Function.Bijective (pointsToScheme B S hS U)
```

## Tag 03H4, a lemma

[Tag 03H4](https://stacks.math.columbia.edu/tag/03H4) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_pointsULift_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedEtaleOpenPoints.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedEtaleOpenPoints.lean#L118). The attribute's comment: “for a value universe independent of the universe of the schemes”.

> **Stacks 03H4** for presheaves with values in a universe `max w u` independent of the
> universe `u` of the schemes: a point of one middle term of a cartesian square and a point of
> the other with the same image in the base are the images of a common point of the fibre
> product. This is `AlgebraicGeometry.Space.exists_point_of_isPullbackULift` with the two
> middle terms in the order of `AlgebraicGeometry.Space.exists_points_of_isPullback`.

```lean
theorem exists_pointsULift_of_isPullback
    {W X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max w u)}
    {p : W ⟶ X} {q : W ⟶ Z} {f : X ⟶ Y} {g : Z ⟶ Y} (sq : IsPullback p q f g)
    (a : pointsULift.{w} B S hS X) (b : pointsULift.{w} B S hS Z)
    (hab : pointsMapULift B S hS X f a = pointsMapULift B S hS Z g b) :
    ∃ v : pointsULift.{w} B S hS W,
      pointsMapULift B S hS W p v = a ∧ pointsMapULift B S hS W q v = b
```

**`AlgebraicGeometry.Space.exists_points_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsBaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsBaseChange.lean#L116).

> The comparison map from the points of a fibre product of presheaves to the fibre product
> of the point sets is surjective: a point of `X` and a point of `Z` with the same image in `Y`
> are the images of a common point of a presheaf `W` sitting in a cartesian square over them.

```lean
theorem exists_points_of_isPullback {p : W ⟶ X} {q : W ⟶ Z} {f : X ⟶ Y} {g : Z ⟶ Y}
    (sq : IsPullback p q f g) (a : points B S hS X) (b : points B S hS Z)
    (hab : pointsMap B S hS X f a = pointsMap B S hS Z g b) :
    ∃ w : points B S hS W,
      pointsMap B S hS W p w = a ∧ pointsMap B S hS W q w = b
```

**`AlgebraicGeometry.Space.exists_point_of_isPullback_presheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsOfPullback.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsOfPullback.lean#L63).

> **Stacks 03H4.** Compatible points of the two middle terms of a cartesian square of
> presheaves on the big fppf site of `S` lift to a point of its upper left corner.
>
> This is surjectivity of `|Z ×_Y X| → |Z| ×_{|Y|} |X|`, stated elementwise for an arbitrary
> cartesian square of presheaves. The companion statement for a cartesian square in the category
> of algebraic spaces is `AlgebraicGeometry.Space.exists_point_of_isPullback`.

```lean
theorem exists_point_of_isPullback_presheaf
    {W Z X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (z : points B S hS Z) (x : points B S hS X)
    (h : pointsMap B S hS Z g z = pointsMap B S hS X f x) :
    ∃ w : points B S hS W,
      pointsMap B S hS W p w = z ∧ pointsMap B S hS W q w = x
```

**`AlgebraicGeometry.Space.exists_point_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsPullback.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsPullback.lean#L36).

> In a cartesian square of algebraic spaces over `S`, a point of `Z` and a
> point of `X` with the same image in `Y` are the two images of a point of `W`.

```lean
theorem exists_point_of_isPullback (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {W Z X Y : AlgebraicSpaces B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (z : points B S hS Z.1) (x : points B S hS X.1)
    (h : pointsMap B S hS Z.1 g.hom z = pointsMap B S hS X.1 f.hom x) :
    ∃ w : points B S hS W.1,
      pointsMap B S hS W.1 p.hom w = z ∧ pointsMap B S hS W.1 q.hom w = x
```

## Tag 03H5, a lemma

[Tag 03H5](https://stacks.math.columbia.edu/tag/03H5) in the Stacks Project.

**`AlgebraicGeometry.Space.presheafSurjective_iff_isSurjective_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveOnPoints.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveOnPoints.lean#L292).

> A morphism from a scheme over `S` to an algebraic space over `S` is surjective, in the sense
> that every represented base change of it is a surjective morphism of schemes, if and only if the
> induced map on points is surjective.

```lean
theorem presheafSurjective_iff_isSurjective_yoneda (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) (T : BigFppfOver B S hS) (f : yoneda.obj T ⟶ F) :
    (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f ↔ IsSurjective B S hS f
```

## Tag 03BW, a lemma

[Tag 03BW](https://stacks.math.columbia.edu/tag/03BW) in the Stacks Project.

**`AlgebraicGeometry.Space.Presentation.pointsRelation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean#L72). The attribute's comment: “image equivalence relation”.

> **Stacks 03BW.** Two points of the presenting scheme are related by the relation scheme
> exactly when they have the same image in the algebraic space.

```lean
theorem pointsRelation_iff (P : Presentation B S hS F hF)
    (x y : points B S hS (yoneda.obj P.U)) :
    P.pointsRelation x y ↔
      pointsMap B S hS (yoneda.obj P.U) P.toSpace x =
        pointsMap B S hS (yoneda.obj P.U) P.toSpace y
```

**`AlgebraicGeometry.Space.Presentation.pointsMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean#L95). The attribute's comment: “surjectivity on points”.

> **Stacks 03BW.** The atlas of a presentation is surjective on points.

```lean
theorem pointsMap_surjective (P : Presentation B S hS F hF) :
    Function.Surjective (pointsMap B S hS (yoneda.obj P.U) P.toSpace)
```

Declarations registered for the tag:

- [`Setoid.ker`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Setoid.ker#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean#L51) (StacksFrontier): “equivalence relation on points”. References: SGA 3 IV (3.3.1), “category of sets”; SGA 4 I (10.9), “special case”.
- [`Setoid.quotientKerEquivOfSurjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Setoid.quotientKerEquivOfSurjective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Points.lean#L54) (StacksFrontier): “canonical quotient equivalence”.

## Tag 03BX, a lemma

[Tag 03BX](https://stacks.math.columbia.edu/tag/03BX) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_pointTopologyFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsTopologyUnique.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsTopologyUnique.lean#L293).

> **Stacks 03BX.** There is a unique family of topologies on the points of the algebraic
> spaces over `S` which is the scheme topology on a scheme, makes every morphism of algebraic
> spaces continuous on points, and makes an étale morphism from a scheme open on points.

```lean
theorem existsUnique_pointTopologyFamily :
    ∃! _t : PointTopologyFamily B S hS, True
```

## Tag 03BY, a definition

[Tag 03BY](https://stacks.math.columbia.edu/tag/03BY) in the Stacks Project.

**`AlgebraicGeometry.Space.pointTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsTopology.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsTopology.lean#L79). The attribute's comment: “the underlying topological space of an algebraic space”.

> The topology on the points of a presheaf on the big fppf site of `S`: a set of points
> is open when its preimage under every scheme-valued point is scheme open.

```lean
def pointTopology (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) :
    TopologicalSpace (points B S hS F)
```

## Tag 03BZ, a lemma

[Tag 03BZ](https://stacks.math.columbia.edu/tag/03BZ) in the Stacks Project.

**`AlgebraicGeometry.Space.openSubspacesOrderIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean#L397). The attribute's comment: “part (1)”.

> The order isomorphism from the open subspaces of an algebraic space over `S` to the open
> subsets of its space of points, sending an open subspace to the image of its point set.

```lean
noncomputable def openSubspacesOrderIso (hF : IsAlgebraicSpace B S hS F) :
    {G : Subfunctor F // IsOpenSubspace B S hS G} ≃o
      TopologicalSpace.Opens (points B S hS F)
```

**`AlgebraicGeometry.Space.openSubspacesOrderIso_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean#L408). The attribute's comment: “part (1)”.

> The open subset of points attached to an open subspace is the image of its points.

```lean
theorem openSubspacesOrderIso_apply (hF : IsAlgebraicSpace B S hS F)
    (G : {G : Subfunctor F // IsOpenSubspace B S hS G}) :
    (openSubspacesOrderIso B S hS F hF G).1 =
      Set.range (pointsMap B S hS G.1.toFunctor G.1.ι)
```

**`AlgebraicGeometry.Space.existsUnique_openSubspacesOrderIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceCorrespondence.lean#L419). The attribute's comment: “part (1)”.

> Taking the image of the points of an open subspace is an inclusion-preserving bijection
> from the open subspaces of an algebraic space over `S` to the open subsets of its space of
> points, and it is the unique order isomorphism doing so.

```lean
theorem existsUnique_openSubspacesOrderIso (hF : IsAlgebraicSpace B S hS F) :
    ∃! e : {G : Subfunctor F // IsOpenSubspace B S hS G} ≃o
      TopologicalSpace.Opens (points B S hS F),
      ∀ G, (e G).1 = Set.range (pointsMap B S hS G.1.toFunctor G.1.ι)
```

**`AlgebraicGeometry.Space.openSubspacesOrderIso_and_isZariskiCover_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceZariskiSite.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspaceZariskiSite.lean#L66).

> **Stacks Tag 03BZ.** Let `X` be an algebraic space over `S`.
>
> Part (1): taking the image of the point set is an inclusion-preserving bijection from the open
> subspaces of `X` to the open subsets of `|X|`; it is the unique order isomorphism doing so.
>
> Part (2): a family of open subspaces of `X` is a Zariski covering exactly when the images of
> the point sets of its members cover `|X|`.
>
> Together these identify the small Zariski site of `X` with the site attached to the topological
> space `|X|`.

```lean
theorem openSubspacesOrderIso_and_isZariskiCover_iff
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F) :
    (∃! e : {G : Subfunctor F // IsOpenSubspace B S hS G} ≃o
        TopologicalSpace.Opens (points B S hS F),
        ∀ G, (e G).1 = Set.range (pointsMap B S hS G.1.toFunctor G.1.ι)) ∧
      ∀ (I : Type u) (X : I → Subfunctor F), (∀ i, IsOpenSubspace B S hS (X i)) →
        (IsZariskiCover B S hS I X ↔
          (⋃ i, Set.range (pointsMap B S hS (X i).toFunctor (X i).ι)) = Set.univ)
```

**`AlgebraicGeometry.Space.isZariskiCover_iff_iUnion_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringPoints.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringPoints.lean#L443). The attribute's comment: “zariski\_coverings”.

> Open subspaces cover an algebraic space in the Zariski topology if and only
> if their images on the space of points cover all points.

```lean
theorem isZariskiCover_iff_iUnion_points
    (hF : IsAlgebraicSpace B S hS F) (I : Type u)
    (U : I → Subfunctor F)
    (hU : ∀ i, IsOpenSubspace B S hS (U i)) :
    IsZariskiCover B S hS I U ↔
      (⋃ i, Set.range (pointsMap B S hS (U i).toFunctor (U i).ι)) =
        Set.univ
```

**`AlgebraicGeometry.Space.isCovering_iff_iSup_openSubspacesOrderIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringPoints.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringPoints.lean#L457). The attribute's comment: “zariski\_coverings”.

> Via the canonical identification with open subsets of the point space,
> covering families of the small Zariski site are precisely open covers.

```lean
theorem isCovering_iff_iSup_openSubspacesOrderIso
    (hF : IsAlgebraicSpace B S hS F)
    (E : Covering.{u + 1, u + 1, u} (OpenSubspaces B S hS F)) :
    let : TopologicalSpace (points B S hS F) :=
      pointTopology B S hS F
    OpenSubspaces.IsCovering B S hS F E ↔
      (⨆ i, openSubspacesOrderIso B S hS F hF
        (E.2.X i)) =
        openSubspacesOrderIso B S hS F hF E.1
```

## Tag 03IE, a lemma

[Tag 03IE](https://stacks.math.columbia.edu/tag/03IE) in the Stacks Project.

**`AlgebraicGeometry.Space.factorsThrough_openSubspace_iff_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FactorThroughOpenSubspace.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FactorThroughOpenSubspace.lean#L52).

> A morphism of algebraic spaces factors through an open subspace if and only
> if its map on points has image in the point set of that subspace.

```lean
theorem factorsThrough_openSubspace_iff_points
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (U : Subfunctor X) (hU : IsOpenSubspace B S hS U)
    (f : Y ⟶ X) :
    (∃ g : Y ⟶ U.toFunctor, g ≫ U.ι = f) ↔
      (Set.range (pointsMap B S hS Y f) ⊆
        Set.range (pointsMap B S hS U.toFunctor U.ι))
```

## Tag 06NF, a lemma

[Tag 06NF](https://stacks.math.columbia.edu/tag/06NF) in the Stacks Project.

**`AlgebraicGeometry.Space.factorThroughEtaleImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L90). The attribute's comment: “induced morphism”.

> The morphism from a scheme to the open subspace corresponding to the image
> of its étale map.

```lean
noncomputable def factorThroughEtaleImage :
    yoneda.obj U ⟶ X'.toFunctor
```

**`AlgebraicGeometry.Space.factorThroughEtaleImage_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L99). The attribute's comment: “factorization”.

> The induced morphism composes with the inclusion to give the original
> étale map.

```lean
theorem factorThroughEtaleImage_comp :
    factorThroughEtaleImage B S hS hX U f X' hX' hX'image ≫ X'.ι = f
```

**`AlgebraicGeometry.Space.surjective_factor_through_etaleImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L107). The attribute's comment: “surjective”.

> The induced map to the image open subspace is surjective.

```lean
theorem surjective_factor_through_etaleImage
    (f' : yoneda.obj U ⟶ X'.toFunctor) (hfactor : f' ≫ X'.ι = f) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f'
```

**`AlgebraicGeometry.Space.etale_factor_through_etaleImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L132). The attribute's comment: “étale”.

> The induced map to the image open subspace is étale.

```lean
theorem etale_factor_through_etaleImage
    (f' : yoneda.obj U ⟶ X'.toFunctor) (hfactor : f' ≫ X'.ι = f) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f'
```

**`AlgebraicGeometry.Space.isEtaleEquivalenceRelation_etaleImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L162). The attribute's comment: “étale equivalence relation”.

> The kernel pair of an étale scheme morphism is an étale equivalence
> relation on its source.

```lean
theorem isEtaleEquivalenceRelation_etaleImage
    {R : BigFppfOver B S hS} (s t : R ⟶ U)
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f) :
    Stacks.Groupoids.IsEtaleEquivalenceRelation
      (prod.lift ((Over.post B.inclusion).map s)
        ((Over.post B.inclusion).map t))
```

**`AlgebraicGeometry.Space.isCoequalizer_factor_through_etaleImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L186). The attribute's comment: “presentation as a quotient”.

> The image open subspace is the fppf sheaf quotient of `U` by the kernel
> pair of the original map.

```lean
theorem isCoequalizer_factor_through_etaleImage
    {R : BigFppfOver B S hS} (s t : R ⟶ U)
    (hR : IsPullback (yoneda.map s) (yoneda.map t) f f)
    (f' : yoneda.obj U ⟶ X'.toFunctor) (hfactor : f' ≫ X'.ι = f) :
    let J := BigFppfOver.topology B S hS
    ∃ (hRsh : Presheaf.IsSheaf J (yoneda.obj R))
      (hUsh : Presheaf.IsSheaf J (yoneda.obj U)),
      let RF : Sheaf J (Type u) := ⟨yoneda.obj R, hRsh⟩
      let UF : Sheaf J (Type u) := ⟨yoneda.obj U, hUsh⟩
      let XF : Sheaf J (Type u) := ⟨X'.toFunctor, hX'.1.isSheaf⟩
      let sf : RF ⟶ UF := ⟨yoneda.map s⟩
      let tf : RF ⟶ UF := ⟨yoneda.map t⟩
      let ff : UF ⟶ XF := ⟨f'⟩
      let w : sf ≫ ff = tf ≫ ff := by
        apply Sheaf.hom_ext
        change yoneda.map s ≫ f' = yoneda.map t ≫ f'
        exact (isPullback_of_factors_comp_mono X'.ι hfactor hfactor hR).w
      Nonempty (IsColimit (Cofork.ofπ ff w))
```

**`AlgebraicGeometry.Space.isOpenSubspace_etale_surjective_lift_openSubspaceOfPoints_range_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringAffineCharts.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiCoveringAffineCharts.lean#L174). The attribute's comment: “factorisation: induced morphism, factorization, surjective, étale”.

> **Stacks 06NF, the whole of its factorisation clause.** Let `U` be an object of the big
> fppf category over `S` and `f : h_U ⟶ X` an étale morphism to an algebraic space over `S`.
> Then the subspace `X'` of `X` cut out by the image of `|U|` is an open subspace, and `f`
> factors through it by a morphism which is surjective — both on point sets and after every
> represented base change — and étale.
>
> The four assertions correspond exactly to the four declarations into which the source's
> sentence "*then `f` factors through a surjective étale morphism `f' : U → X'`*" is split: the
> induced morphism, which here is the canonical `CategoryTheory.Subfunctor.lift` and so needs no
> choice; the factorisation `f' ≫ X'.ι = f`, which is `CategoryTheory.Subfunctor.lift_ι` and
> holds by `rfl`; surjectivity; and étaleness. That `X'` is an open subspace with point set the
> image of `|U|` is the source's own appeal to Tag 03BZ, and is
> `AlgebraicGeometry.Space.isOpenSubspace_openSubspaceOfPoints` together with
> `AlgebraicGeometry.Space.range_pointsMap_ι_openSubspaceOfPoints`.
>
> **What is not proved.** The source's second sentence — that `R = U ×_X U` equals `U ×_{X'} U`,
> that it is an étale equivalence relation, and that `X'` is the quotient `U/R` — is not
> addressed. So the covering set of Tag 06NF is incomplete and the attribute carries a part
> string naming only the factorisation clause. Closing the rest needs Tag 0262, whose three
> parts are proved in
> `StacksFrontier.AlgebraicGeometry.Spaces.Presentation.KernelPair`.

```lean
theorem isOpenSubspace_etale_surjective_lift_openSubspaceOfPoints_range_yoneda
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ X)
    (hf : (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    IsOpenSubspace B S hS
        (openSubspaceOfPoints B S hS X
          (Set.range (pointsMap B S hS (yoneda.obj U) f))) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf
        (Subfunctor.lift f (range_le_openSubspaceOfPoints_range_pointsMap f)) ∧
      Function.Surjective (pointsMap B S hS (yoneda.obj U)
        (Subfunctor.lift f (range_le_openSubspaceOfPoints_range_pointsMap f))) ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf
        (Subfunctor.lift f (range_le_openSubspaceOfPoints_range_pointsMap f))
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.PullbackCone.isLimitOfFactors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.PullbackCone.isLimitOfFactors#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleImageSubspace.lean#L59) (StacksFrontier): “kernel pair”.

## Tag 0H2X, a lemma

[Tag 0H2X](https://stacks.math.columbia.edu/tag/0H2X) in the Stacks Project.

**`AlgebraicGeometry.Space.FieldValuedPoint.existsUnique_factor_of_class_eq_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/MonomorphismPoints.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/MonomorphismPoints.lean#L62).

> **Stacks 0H2X.** Two representatives of the same point factor uniquely through a
> representative whose map to the algebraic space is a monomorphism.

```lean
theorem FieldValuedPoint.existsUnique_factor_of_class_eq_of_mono
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F)
    (p q : FieldValuedPoint B S hS F)
    [Mono (yonedaEquiv.symm p.value)]
    (h : p.class B S hS F = q.class B S hS F) :
    ∃! f : q.siteObject B S hS F ⟶ p.siteObject B S hS F,
      F.map f.op p.value = q.value
```

## Tag 03E1, a lemma

[Tag 03E1](https://stacks.math.columbia.edu/tag/03E1) in the Stacks Project.

**`AlgebraicGeometry.Space.iso_of_mono_of_point_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/MonomorphismPoints.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/MonomorphismPoints.lean#L112).

> **Stacks 03E1.** Monomorphic field-valued representatives of the same point are
> isomorphic over the algebraic space.

```lean
theorem iso_of_mono_of_point_eq
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F)
    (p q : FieldValuedPoint B S hS F)
    [Mono (yonedaEquiv.symm p.value)] [Mono (yonedaEquiv.symm q.value)]
    (heq : p.class B S hS F = q.class B S hS F) :
    ∃ e : p.siteObject B S hS F ≅ q.siteObject B S hS F,
      F.map e.hom.op q.value = p.value
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.4, Tag 03BT](https://stacks.math.columbia.edu/tag/03BT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
