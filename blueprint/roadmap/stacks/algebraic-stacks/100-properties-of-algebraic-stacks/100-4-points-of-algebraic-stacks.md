---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FieldValuedPoint.HasCommonExtension, AlgebraicGeometry.Stack.pointsMap, AlgebraicGeometry.Stack.pointsMap_eq_of_basedNatTrans, AlgebraicGeometry.Stack.pointsMap_comp, AlgebraicGeometry.Stack.pointsEquivOfBasedEquivalence, AlgebraicGeometry.Stack.spacePointMap_id_bijective, AlgebraicGeometry.Stack.FieldValuedPoint.hasCommonExtension_equivalence, AlgebraicGeometry.Stack.points
statement: formalized
proof: formalized
---

# 100.4 Points of algebraic stacks

Section 100.4 of the Stacks Project, [Tag 04XE](https://stacks.math.columbia.edu/tag/04XE). 10 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04XE, the section

[Tag 04XE](https://stacks.math.columbia.edu/tag/04XE) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.FieldValuedPoint.HasCommonExtension`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L170), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L653) (StacksFrontier): “the equivalence of morphisms from spectra of fields: a common refinement”.
- [`AlgebraicGeometry.Stack.pointsMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L309), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L655) (StacksFrontier): “the induced map |f| : |𝒳| → |𝒴| of a 1-morphism”.
- [`AlgebraicGeometry.Stack.pointsMap_eq_of_basedNatTrans`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L337), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L657) (StacksFrontier): “2-isomorphic 1-morphisms induce the same map on points, so a 2-commutative square of stacks gives a commutative square of sets”.
- [`AlgebraicGeometry.Stack.pointsMap_comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L346), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L660) (StacksFrontier): “the map on points of a composite is the composite of the maps”.
- [`AlgebraicGeometry.Stack.pointsEquivOfBasedEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L662) (StacksFrontier): “an equivalence 𝒳 → 𝒴 induces a bijection |𝒳| → |𝒴|”.
- [`AlgebraicGeometry.Stack.spacePointMap_id_bijective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L261), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L664) (StacksFrontier): “agreement with the points of an algebraic space (Definition 03BU)”.

## Tag 04XF, a lemma

[Tag 04XF](https://stacks.math.columbia.edu/tag/04XF) in the Stacks Project.

**`AlgebraicGeometry.Stack.FieldValuedPoint.hasCommonExtension_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Points.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L250).

> **Stacks 04XF.** Common field-valued refinement is an equivalence relation on the
> field-valued points of a category fibred in groupoids.

```lean
theorem hasCommonExtension_equivalence
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {𝒳 : BasedCategory.{v, t} (BigFppfOver B S hS)}
    (h𝒳 : 𝒳.p.IsFiberedInGroupoids) :
    Equivalence (HasCommonExtension (𝒳 := 𝒳))
```

## Tag 04XG, a definition

[Tag 04XG](https://stacks.math.columbia.edu/tag/04XG) in the Stacks Project.

**`AlgebraicGeometry.Stack.points`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Points.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Points.lean#L273).

> **Stacks 04XG.** The points of a category fibred in groupoids, in particular of an
> algebraic stack, are the equivalence classes of its field-valued points.

```lean
abbrev points (h𝒳 : 𝒳.p.IsFiberedInGroupoids) : Type (max (u + 1) t)
```

## Tag 04XH, a lemma

[Tag 04XH](https://stacks.math.columbia.edu/tag/04XH) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_point_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsFibreProduct.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsFibreProduct.lean#L249). The attribute's comment: “for a 2-fibre product of categories fibred in groupoids”.

> **Points of a 2-fibre product of categories fibred in groupoids**: a point of `𝒵` and a
> point of `𝒳` with the same image in `|𝒴|` lift to a point of any 2-fibre product of
> `g : 𝒵 ⟶ 𝒴` and `f : 𝒳 ⟶ 𝒴`.

```lean
theorem exists_point_of_isTwoFibreProduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒵 𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    {g : 𝒵 ⟶ 𝒴} {f : 𝒳 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (z : points B S hS 𝒵.val 𝒵.property) (x : points B S hS 𝒳.val 𝒳.property)
    (h : pointsMap B S hS 𝒵.val 𝒵.property 𝒴.property g.hom z =
      pointsMap B S hS 𝒳.val 𝒳.property 𝒴.property f.hom x) :
    ∃ p : points B S hS P.pt.val P.pt.property,
      pointsMap B S hS P.pt.val P.pt.property 𝒵.property P.fst.hom p = z ∧
        pointsMap B S hS P.pt.val P.pt.property 𝒳.property P.snd.hom p = x
```

**`AlgebraicGeometry.Stack.exists_point_of_isTwoFibreProduct_algebraicStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsFibreProductAlgebraicStack.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsFibreProductAlgebraicStack.lean#L102).

> **Stacks 04XH.** Let `g : 𝒵 ⟶ 𝒴` and `f : 𝒳 ⟶ 𝒴` be 1-morphisms of algebraic stacks over
> `S` and let `P` be a 2-fibre product of that cospan in the 2-category of algebraic stacks. A
> point of `𝒵` and a point of `𝒳` with the same image in `|𝒴|` lift to a point of `P`; that is,
> the canonical map `|P| ⟶ |𝒵| ×_{|𝒴|} |𝒳|` is surjective.

```lean
theorem exists_point_of_isTwoFibreProduct_algebraicStacks
    {𝒵 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {g : 𝒵 ⟶ 𝒴} {f : 𝒳 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (z : points B S hS 𝒵.val.val (Classical.choose 𝒵.property))
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (h : pointsMap B S hS 𝒵.val.val (Classical.choose 𝒵.property)
          (Classical.choose 𝒴.property) g.hom.hom z =
        pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
          (Classical.choose 𝒴.property) f.hom.hom x) :
    ∃ p : points B S hS P.pt.val.val (Classical.choose P.pt.property),
      pointsMap B S hS P.pt.val.val (Classical.choose P.pt.property)
          (Classical.choose 𝒵.property) P.fst.hom.hom p = z ∧
        pointsMap B S hS P.pt.val.val (Classical.choose P.pt.property)
          (Classical.choose 𝒳.property) P.snd.hom.hom p = x
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_point_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveBaseChange.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveBaseChange.lean#L129).

> **Stacks 04XH** for a 2-fibre product in the 2-category of algebraic stacks: a point of `𝒵`
> and a point of `𝒳` with the same image in `|𝒴|` lift to a point of any 2-fibre product of
> `g : 𝒵 ⟶ 𝒴` and `f : 𝒳 ⟶ 𝒴`.
>
> This is the same proposition as
> `AlgebraicGeometry.Stack.exists_point_of_isTwoFibreProduct_algebraicStacks`, which writes the
> points and the maps on points in longhand instead of through the abbreviations
> `AlgebraicGeometry.Stack.AlgebraicStacks.points` and
> `AlgebraicGeometry.Stack.AlgebraicStacks.pointsMap`.

```lean
theorem exists_point_of_isTwoFibreProduct {g : 𝒵 ⟶ 𝒴} {f : 𝒳 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (z : points B S hS 𝒵) (x : points B S hS 𝒳)
    (h : pointsMap B S hS g z = pointsMap B S hS f x) :
    ∃ p : points B S hS P.pt,
      pointsMap B S hS P.fst p = z ∧ pointsMap B S hS P.snd p = x
```

## Tag 04XI, a lemma

[Tag 04XI](https://stacks.math.columbia.edu/tag/04XI) in the Stacks Project.

**`AlgebraicGeometry.Stack.pointsMap_surjective_iff_isRelativelySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsSurjective.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsSurjective.lean#L143).

> **Stacks 04XI.** A 1-morphism of algebraic stacks over `S` which is representable by
> algebraic spaces is surjective — the relative property of Stacks 03YK at surjectivity of
> morphisms of algebraic spaces — exactly when the map it induces on points is surjective.

```lean
theorem pointsMap_surjective_iff_isRelativelySurjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    Function.Surjective
        (pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
          (Classical.choose 𝒴.property) f.hom.hom) ↔
      HasRelativeProperty B S hS (Space.surjectiveMorphismProperty B S hS) f.hom hf
```

## Tag 04XJ, a lemma

[Tag 04XJ](https://stacks.math.columbia.edu/tag/04XJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.GroupoidPresentation.range_pointsMap_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsGroupoidPresentation.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsGroupoidPresentation.lean#L435). The attribute's comment: “part 1: the image of |R| → |U| × |U| is an equivalence relation”.

> **Stacks 04XJ, the equivalence relation.** Let `𝒳 = [U/R]` be a presentation of a category
> `𝒳` over the big fppf site of `S` which is fibred in groupoids. Then the image of
> `|R| ⟶ |U| × |U|` is an equivalence relation on `|U|`, namely the kernel of the map
> `|p| : |U| ⟶ |𝒳|` induced by the presenting 1-morphism.

```lean
theorem range_pointsMap_source_target (P : GroupoidPresentation B S hS 𝒳)
    (h𝒳 : 𝒳.p.IsFiberedInGroupoids) :
    Set.range (fun r : arrowSpacePoints P.groupoid ↦
        (sourcePointsMap P.groupoid r, targetPointsMap P.groupoid r)) =
      {q : objectSpacePoints P.groupoid × objectSpacePoints P.groupoid |
        (Setoid.ker (P.presentingPointsMap h𝒳)).r q.1 q.2}
```

**`AlgebraicGeometry.Stack.GroupoidPresentation.pointsQuotientEquivOfPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsGroupoidPresentation.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsGroupoidPresentation.lean#L454). The attribute's comment: “part 2: |X| is the quotient of |U| by that relation”.

> **Stacks 04XJ, the quotient.** Let `𝒳 = [U/R]` be a presentation of a category `𝒳` over the
> big fppf site of `S` which is fibred in groupoids. Then `|𝒳|` is the quotient of `|U|` by the
> equivalence relation of
> `AlgebraicGeometry.Stack.GroupoidPresentation.range_pointsMap_source_target`, the image of
> `|R| ⟶ |U| × |U|`.

```lean
noncomputable def pointsQuotientEquivOfPresentation (P : GroupoidPresentation B S hS 𝒳)
    (h𝒳 : 𝒳.p.IsFiberedInGroupoids) :
    Quotient (Setoid.ker (P.presentingPointsMap h𝒳)) ≃ points B S hS 𝒳 h𝒳
```

## Tag 04XK, a remark

[Tag 04XK](https://stacks.math.columbia.edu/tag/04XK) in the Stacks Project.

**`AlgebraicGeometry.Stack.range_prod_pointsMapToSpace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean#L84). The attribute's comment: “image of the relation on points”.

> **The image of the relation on points.** For a 2-fibre product `R` of a chart
> `f : U ⟶ 𝒳` by an algebraic space with itself, the image of `|R| ⟶ |U| × |U|` is exactly the
> set of pairs of points of `U` with the same image in `|𝒳|`.

```lean
theorem range_prod_pointsMapToSpace_eq
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    {𝒳 : AlgebraicStacks.{u, w} B S hS}
    {p : algebraicSpaceStack.{u, w} B S hS F hF ⟶ 𝒳}
    (P : Bicategory.TwoCommSq p p) (hP : Bicategory.IsTwoFibreProduct P) :
    Set.range (fun r : AlgebraicStacks.points B S hS P.pt =>
        (pointsMapToSpace B S hS hF P.fst r, pointsMapToSpace B S hS hF P.snd r)) =
      {q : Space.points B S hS F × Space.points B S hS F |
        spacePointMap B S hS F 𝒳.val p.hom.hom q.1 =
          spacePointMap B S hS F 𝒳.val p.hom.hom q.2}
```

**`AlgebraicGeometry.Stack.equivalence_mem_range_prod_pointsMapToSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean#L113). The attribute's comment: “equivalence relation on points”.

> **The relation on points is an equivalence relation.** The image of
> `|R| ⟶ |U| × |U|` is the kernel of `|f|`.

```lean
theorem equivalence_mem_range_prod_pointsMapToSpace
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    {𝒳 : AlgebraicStacks.{u, w} B S hS}
    {p : algebraicSpaceStack.{u, w} B S hS F hF ⟶ 𝒳}
    (P : Bicategory.TwoCommSq p p) (hP : Bicategory.IsTwoFibreProduct P) :
    Equivalence (fun x y : Space.points B S hS F =>
      (x, y) ∈ Set.range (fun r : AlgebraicStacks.points B S hS P.pt =>
        (pointsMapToSpace B S hS hF P.fst r, pointsMapToSpace B S hS hF P.snd r)))
```

**`AlgebraicGeometry.Stack.spacePointsQuotientEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsQuotientOfSpaceAtlas.lean#L129). The attribute's comment: “the points of the stack as a quotient”.

> **The points of the stack as a quotient.** For a surjective chart
> `f : U ⟶ 𝒳` by an algebraic space, `|𝒳|` is the quotient of `|U|` by the kernel of `|f|`,
> which is the image of `|R| ⟶ |U| × |U|` by
> `AlgebraicGeometry.Stack.range_prod_pointsMapToSpace_eq`.

```lean
noncomputable def spacePointsQuotientEquiv
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (p : algebraicSpaceStack.{u, w} B S hS F hF ⟶ 𝒳) (hsurj : IsSurjective B S hS p) :
    Quotient (Setoid.ker (spacePointMap B S hS F 𝒳.val p.hom.hom)) ≃
      AlgebraicStacks.points B S hS 𝒳
```

## Tag 04XL, a lemma

[Tag 04XL](https://stacks.math.columbia.edu/tag/04XL) in the Stacks Project.

**`AlgebraicGeometry.Stack.spacePointMap_class`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L138). The attribute's comment: “canonical map on points”.

> The chosen quotient representative in `AlgebraicGeometry.Stack.spacePointMap` has the same
> image as any field-valued representative of the point.

```lean
theorem spacePointMap_class (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (f : (fibredCategory B S hS F).val ⥤ᵇ 𝒳.val)
    (p : Space.FieldValuedPoint B S hS F) :
    spacePointMap B S hS F 𝒳 f (p.class B S hS F) =
      pointClass B S hS 𝒳.val 𝒳.property
        (fieldValuedPointMap B S hS (fibredCategory B S hS F).val f
          (spaceFieldValuedPoint B S hS F p))
```

**`AlgebraicGeometry.Stack.existsUnique_pointTopologyFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 623](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L623). The attribute's comment: “existence and uniqueness of topology”.

> There is a unique family of topologies on the points of the algebraic stacks over `S` which
> makes every 1-morphism continuous on points and makes a 1-morphism from an algebraic space whose
> represented base changes are all flat and locally of finite presentation continuous and open on
> points.

```lean
theorem existsUnique_pointTopologyFamily :
    ∃! _t : PointTopologyFamily.{u, w} B S hS, True
```

## Tag 04Y8, a definition

[Tag 04Y8](https://stacks.math.columbia.edu/tag/04Y8) in the Stacks Project.

**`AlgebraicGeometry.Stack.pointTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsTopology.lean#L345). The attribute's comment: “the underlying topological space of an algebraic stack”.

> The topology on the points of a category fibred in groupoids over the big fppf site of `S`:
> the supremum, over all charts by algebraic spaces, of the topologies coinduced from the point
> topologies of the algebraic spaces along the canonical maps.

```lean
noncomputable def pointTopology
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)) :
    TopologicalSpace (points B S hS 𝒳.val 𝒳.property)
```

## Tag 04Y9, a lemma

[Tag 04Y9](https://stacks.math.columbia.edu/tag/04Y9) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasBasis_nhds_isOpen_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsLocallyQuasiCompact.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsLocallyQuasiCompact.lean#L97). The attribute's comment: “fundamental system of quasi-compact open neighbourhoods”.

> The quasi-compact open neighbourhoods of a point of the space of points of an algebraic
> stack over `S` are a fundamental system of neighbourhoods of that point.

```lean
theorem hasBasis_nhds_isOpen_isCompact (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (x : points B S hS 𝒳.val 𝒳.property) :
    (nhds x).HasBasis
      (fun W : Set (points B S hS 𝒳.val 𝒳.property) ↦ IsOpen W ∧ IsCompact W ∧ x ∈ W) id
```

**`AlgebraicGeometry.Stack.locallyCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsLocallyQuasiCompact.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsLocallyQuasiCompact.lean#L109). The attribute's comment: “local quasi-compactness”.

> The space of points of an algebraic stack over `S` is locally quasi-compact, that is, a
> `LocallyCompactSpace`.

```lean
theorem locallyCompactSpace (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    LocallyCompactSpace (points B S hS 𝒳.val 𝒳.property)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.4, Tag 04XE](https://stacks.math.columbia.edu/tag/04XE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
