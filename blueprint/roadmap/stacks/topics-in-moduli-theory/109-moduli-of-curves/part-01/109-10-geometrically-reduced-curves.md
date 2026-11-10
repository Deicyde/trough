---
declaration: section
origin: cited
lean: AlgebraicGeometry.curvesGeomred_isOpenSubstack, AlgebraicGeometry.factors_curvesGeomred_iff, AlgebraicGeometry.factors_curvesGeomred_over_field_iff, AlgebraicGeometry.curvesGeomred_isOpenSubstack_and_factors_iff, AlgebraicGeometry.isCohenMacaulay_of_geometricallyReduced_of_topologicalKrullDim_le_one, AlgebraicGeometry.isCohenMacaulay_fiber_of_geometricallyReduced_of_topologicalKrullDim_le_one, AlgebraicGeometry.Space.isCohenMacaulay_schemeSpaceMap_of_geometricallyReduced, AlgebraicGeometry.curvesGeomred_le_curvesCM
statement: formalized
proof: formalized
---

# 109.10 Geometrically reduced curves

Section 109.10 of the Stacks Project, [Tag 0E0F](https://stacks.math.columbia.edu/tag/0E0F). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E0G, a lemma

[Tag 0E0G](https://stacks.math.columbia.edu/tag/0E0G) in the Stacks Project.

**`AlgebraicGeometry.curvesGeomred_isOpenSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean#L338). The attribute's comment: “the open substack Curves^\{geomred} of Curves”.

> **Stacks 0E0G, the open substack.** `Curves^{geomred}`, the strictly full subcategory of
> families of curves whose fibres are geometrically reduced (Stacks 0E08), is an open substack of
> `Curves`: its inclusion is representable by algebraic spaces and an open immersion.

```lean
theorem curvesGeomred_isOpenSubstack :
    ObjectProperty.IsClosedUnderIsomorphisms (IsGeometricallyReducedFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ _ (isOpenCurvesLocus_curvesGeomred B hZ).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ _ (isOpenCurvesLocus_curvesGeomred B hZ).prop_of_hom)
```

**`AlgebraicGeometry.factors_curvesGeomred_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean#L351). The attribute's comment: “part (1): the classifying morphism of a family of curves factors through Curves^\{geomred} iff the fibres of the family are geometrically reduced”.

> **Stacks 0E0G, part (1).** The classifying morphism of a family of curves `X ⟶ S` factors
> through `Curves^{geomred}` exactly when the fibres of `X ⟶ S` are geometrically reduced
> (Stacks 0E08).

```lean
theorem factors_curvesGeomred_iff (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        (IsGeometricallyReducedFamily B hZ).FullSubcategory,
        z ⋙ (IsGeometricallyReducedFamily B hZ).ι = y) ↔
      IsGeometricallyReducedFamily B hZ (y.obj (Over.mk (𝟙 U.left)))
```

**`AlgebraicGeometry.factors_curvesGeomred_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean#L367). The attribute's comment: “part (2): for a proper scheme of dimension at most one over a field, the classifying morphism factors through Curves^\{geomred} iff the scheme is geometrically reduced over the field”.

> **Stacks 0E0G, part (2).** Let `X` be a proper scheme of dimension at most one over a field
> `k` (with `Spec k` in the site, so that the classifying morphism `Spec k ⟶ Curves` of `X`
> exists). The classifying morphism of `X` factors through `Curves^{geomred}` exactly when `X` is
> geometrically reduced over `k`.

```lean
theorem factors_curvesGeomred_over_field_iff
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
    (U : BigFppfOver B integerBase hZ)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ)
    (hy : y ⋙ curvesProjectionOver B hZ = Over.map U.hom)
    (e : y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) :
    (∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
        (IsGeometricallyReducedFamily B hZ).FullSubcategory,
        z ⋙ (IsGeometricallyReducedFamily B hZ).ι = y) ↔
      IsGeometricallyReducedOver X.hom
```

**`AlgebraicGeometry.curvesGeomred_isOpenSubstack_and_factors_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedOpen.lean#L389). The attribute's comment: “the whole statement: the open substack Curves^\{geomred} and parts (1) and (2)”.

> **Stacks 0E0G.** There is an open substack `Curves^{geomred} ⊂ Curves` — the strictly full
> subcategory of families of curves with geometrically reduced fibres, whose inclusion is
> representable by algebraic spaces and an open immersion — such that (1) the classifying morphism
> of a family of curves `X ⟶ S` factors through it exactly when the fibres of `X ⟶ S` are
> geometrically reduced (Stacks 0E08), and (2) for a proper scheme `X` of dimension at most one
> over a field `k`, the classifying morphism of `X` factors through it exactly when `X` is
> geometrically reduced over `k`.

```lean
theorem curvesGeomred_isOpenSubstack_and_factors_iff :
    (ObjectProperty.IsClosedUnderIsomorphisms (IsGeometricallyReducedFamily B hZ) ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ _ (isOpenCurvesLocus_curvesGeomred B hZ).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ _ (isOpenCurvesLocus_curvesGeomred B hZ).prop_of_hom)) ∧
    (∀ (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          (IsGeometricallyReducedFamily B hZ).FullSubcategory,
          z ⋙ (IsGeometricallyReducedFamily B hZ).ι = y) ↔
        IsGeometricallyReducedFamily B hZ (y.obj (Over.mk (𝟙 U.left))))) ∧
    (∀ (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
      (X : Over (Spec (.of k))) [IsProper X.hom] (hdim : topologicalKrullDim X.left ≤ 1)
      (U : BigFppfOver B integerBase hZ)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ CurveFamily B hZ),
      y ⋙ curvesProjectionOver B hZ = Over.map U.hom →
      (y.obj (Over.mk (𝟙 U.left)) ≅ curveFamilyOfScheme X B hZ hk hdim) →
      ((∃ z : BigFppfOver B U.left.1 U.left.2 ⥤
          (IsGeometricallyReducedFamily B hZ).FullSubcategory,
          z ⋙ (IsGeometricallyReducedFamily B hZ).ι = y) ↔
        IsGeometricallyReducedOver X.hom))
```

## Tag 0E1G, a lemma

[Tag 0E1G](https://stacks.math.columbia.edu/tag/0E1G) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_of_geometricallyReduced_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GeometricallyReducedCohenMacaulay.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GeometricallyReducedCohenMacaulay.lean#L85). The attribute's comment: “the inclusion read on a curve over a field, the curves being the objects of the stack parametrized by a field-valued point”. References: EGA IV (5.7.8), “special case”.

> **A geometrically reduced curve is Cohen–Macaulay.** A scheme of dimension at most one which
> is locally of finite type and geometrically reduced over a field is Cohen–Macaulay.

```lean
theorem isCohenMacaulay_of_geometricallyReduced_of_topologicalKrullDim_le_one {k : Type u}
    [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [GeometricallyReduced f]
    [LocallyOfFiniteType f] (hX : topologicalKrullDim X ≤ 1) :
    IsCohenMacaulay X
```

**`AlgebraicGeometry.isCohenMacaulay_fiber_of_geometricallyReduced_of_topologicalKrullDim_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/GeometricallyReducedCohenMacaulay.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/GeometricallyReducedCohenMacaulay.lean#L97). The attribute's comment: “the inclusion read fibrewise on a family of curves”. References: EGA IV (5.7.8), “special case”.

> **A geometrically reduced fibre of dimension at most one is Cohen–Macaulay.** For a morphism
> of schemes which is locally of finite type with geometrically reduced fibres, every fibre of
> dimension at most one is Cohen–Macaulay.

```lean
theorem isCohenMacaulay_fiber_of_geometricallyReduced_of_topologicalKrullDim_le_one
    {X S : Scheme.{u}} (f : X ⟶ S) [GeometricallyReduced f] [LocallyOfFiniteType f] (s : S)
    (hX : topologicalKrullDim (f.fiber s) ≤ 1) :
    IsCohenMacaulay (f.fiber s)
```

**`AlgebraicGeometry.Space.isCohenMacaulay_schemeSpaceMap_of_geometricallyReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReduced.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReduced.lean#L55). The attribute's comment: “the inclusion read on the structure morphism of a family of curves over a field, whose Cohen–Macaulayness is the defining condition of the Cohen–Macaulay open substack”.

> **A geometrically reduced family of curves over a field is Cohen–Macaulay.** Let
> `g : T ⟶ U` be a morphism of the big fppf site of the integers which is flat and locally of
> finite type, whose target scheme is the spectrum of a field, and whose source scheme is
> geometrically reduced of dimension at most one. Then the induced morphism of algebraic spaces is
> Cohen–Macaulay, which is the defining condition of `Curves^{CM}`.

```lean
theorem Space.isCohenMacaulay_schemeSpaceMap_of_geometricallyReduced
    {T U : BigFppfOver B integerBase hZ} (g : T ⟶ U) (k : Type u) [Field k]
    (hU : (BigFppfOver.toScheme B integerBase hZ).obj U = Spec (.of k))
    [Flat ((BigFppfOver.toScheme B integerBase hZ).map g)]
    [LocallyOfFiniteType ((BigFppfOver.toScheme B integerBase hZ).map g)]
    [GeometricallyReduced ((BigFppfOver.toScheme B integerBase hZ).map g)]
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    Space.IsCohenMacaulay B integerBase hZ (schemeSpaceMap g).hom
```

**`AlgebraicGeometry.curvesGeomred_le_curvesCM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedSupplement.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesGeometricallyReducedSupplement.lean#L180). The attribute's comment: “the inclusion of the conditions cutting the two subcategories out of the category of families of curves”.

> `Curves^{geomred} ⊂ Curves^{CM}`: a family of curves whose fibres are geometrically reduced
> is Cohen–Macaulay.

```lean
theorem curvesGeomred_le_curvesCM :
    (show ObjectProperty (CurveFamily B hZ) from IsGeometricallyReducedCurveFamily B hZ) ≤
      (show ObjectProperty (CurveFamily B hZ) from IsCohenMacaulayFamily B hZ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.10, Tag 0E0F](https://stacks.math.columbia.edu/tag/0E0F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
