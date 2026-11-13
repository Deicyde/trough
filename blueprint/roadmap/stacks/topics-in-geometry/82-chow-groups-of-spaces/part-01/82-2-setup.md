---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.BaseSpaceDimensionSituation.IsGood, AlgebraicGeometry.Space.inducedDimensionValue, AlgebraicGeometry.Space.inducedDimensionValue_eq, AlgebraicGeometry.Space.BaseSpaceDimensionSituation.stacksSober_points_of_isGood, AlgebraicGeometry.Space.isIntegralSpace_iff_isReduced_and_irreducibleSpace_of_isGood, AlgebraicGeometry.Space.existsUnique_integralClosedSubspace_isGenericPoint_of_isGood, AlgebraicGeometry.Space.deltaDimension_eq_inducedDimensionValue, AlgebraicGeometry.Space.codimension_singleton_eq_deltaDimension
statement: formalized
proof: formalized
---

# 82.2 Setup

Section 82.2 of the Stacks Project, [Tag 0EDS](https://stacks.math.columbia.edu/tag/0EDS). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EDT, a situation

[Tag 0EDT](https://stacks.math.columbia.edu/tag/0EDT) in the Stacks Project.

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.IsGood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean#L59). The attribute's comment: “good\_space”.

> **Stacks 0EDT.** An algebraic space over the fixed base is *good* when its structure
> morphism is quasi-separated and locally of finite type.

```lean
abbrev BaseSpaceDimensionSituation.IsGood (D : BaseSpaceDimensionSituation.{u})
    {X : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u}
    (f : X ⟶ D.space) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.inducedDimensionValue`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionFunctionFiniteType.lean#L71), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean#L68) (StacksFrontier): “induced\_delta”.
- [`AlgebraicGeometry.Space.inducedDimensionValue_eq`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionFunctionFiniteType.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Setup.lean#L69) (StacksFrontier): “induced\_delta”.

## Tag 0EDU, a remark

[Tag 0EDU](https://stacks.math.columbia.edu/tag/0EDU) in the Stacks Project.

**`AlgebraicGeometry.Space.BaseSpaceDimensionSituation.stacksSober_points_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Decency.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Decency.lean#L104).

> **Stacks 0EDU.** The point space of a good algebraic space over the base of Situation 0EDT
> is sober: every irreducible closed subset of it has a unique generic point.
>
> A good algebraic space is decent, and the point space of a decent algebraic space is
> Kolmogorov by Stacks 03K3 and quasi-sober by Stacks 03K6.

```lean
theorem BaseSpaceDimensionSituation.stacksSober_points_of_isGood (f : X ⟶ D.space)
    (hgood : D.IsGood f) :
    StacksSober (points D.site D.base D.base_mem X)
```

## Tag 0EDV, a remark

[Tag 0EDV](https://stacks.math.columbia.edu/tag/0EDV) in the Stacks Project.

**`AlgebraicGeometry.Space.isIntegralSpace_iff_isReduced_and_irreducibleSpace_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralGoodSpace.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralGoodSpace.lean#L97). The attribute's comment: “integral iff reduced and irreducible”.

> **Stacks 0EDV.** A good algebraic space over the fixed base is integral exactly when it is
> reduced and its space of points is irreducible: the third condition of integrality, decency,
> holds for every good algebraic space.

```lean
theorem isIntegralSpace_iff_isReduced_and_irreducibleSpace_of_isGood (f : X ⟶ D.space)
    (hf : D.IsGood f) :
    IsIntegralSpace D.site D.base D.base_mem X ↔
      HasEtaleLocalProperty D.site D.base D.base_mem X (fun Y : Scheme.{u} => IsReduced Y) ∧
        IrreducibleSpace (points D.site D.base D.base_mem X)
```

**`AlgebraicGeometry.Space.existsUnique_integralClosedSubspace_isGenericPoint_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralGoodSpace.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntegralGoodSpace.lean#L107). The attribute's comment: “unique integral closed subspace with a given generic point”.

> **Stacks 0EDV.** Every point of a good algebraic space over the fixed base is the generic
> point of the set of points of exactly one integral closed subspace.

```lean
theorem existsUnique_integralClosedSubspace_isGenericPoint_of_isGood (f : X ⟶ D.space)
    (hf : D.IsGood f) (ξ : points D.site D.base D.base_mem X) :
    ∃! Z : IntegralClosedSubspace D.site D.base D.base_mem X,
      IsGenericPoint ξ
        (Set.range (pointsMap D.site D.base D.base_mem Z.subspace.toFunctor Z.subspace.ι))
```

## Tag 0EDW, a lemma

[Tag 0EDW](https://stacks.math.columbia.edu/tag/0EDW) in the Stacks Project.

**`AlgebraicGeometry.Space.deltaDimension_eq_inducedDimensionValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean#L396). The attribute's comment: “part (1): the common value is the induced delta function at the generic point”.

> **Stacks 0EDW, part (1).** The common value is `δ(ξ) = δ_{X/B}(ξ)`, for `ξ` the generic point
> of `|Z|`: the δ-dimension of `Z` is the value at `ξ` of the dimension function `δ_{X/B}` of
> Stacks 0EDN, the value of `δ` at the image of `ξ` plus the transcendence degree of `ξ` over that
> image, and it is a nonnegative integer.

```lean
theorem deltaDimension_eq_inducedDimensionValue :
    0 ≤ deltaDimension D sX Z ∧
      deltaDimension D sX Z = inducedDimensionValue D.site D.base D.base_mem D.delta sX
        (pointsMap D.site D.base D.base_mem Z.subspace.toFunctor Z.subspace.ι
          (Z.genericPoint D.site D.base D.base_mem))
```

**`AlgebraicGeometry.Space.codimension_singleton_eq_deltaDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean#L409). The attribute's comment: “part (3): the codimension of a closed point of the integral closed subspace is the value of the induced delta function at its generic point”.

> **Stacks 0EDW, parts (1) and (3).** Over a Jacobson base whose dimension function vanishes
> at closed points, the codimension of a closed point of the set of points of an integral closed
> subspace `Z` of a good algebraic space is the δ-dimension of `Z`, the value of `δ_{X/B}` at the
> generic point of `Z`; in particular that integer is nonnegative.

```lean
theorem codimension_singleton_eq_deltaDimension
    (z : points D.site D.base D.base_mem Z.subspace.toFunctor)
    (hz : IsClosed ({z} : Set (points D.site D.base D.base_mem Z.subspace.toFunctor))) :
    0 ≤ deltaDimension D sX Z ∧
      codimension (⟨{z}, isIrreducible_singleton, hz⟩ :
          IrreducibleCloseds (points D.site D.base D.base_mem Z.subspace.toFunctor)) =
        ((deltaDimension D sX Z).toNat : ℕ∞)
```

**`AlgebraicGeometry.Space.topologicalKrullDim_points_eq_deltaDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean#L424). The attribute's comment: “part (2): the dimension of the set of points of the integral closed subspace is the value of the induced delta function at its generic point”.

> **Stacks 0EDW, parts (1) and (2).** Over a Jacobson base whose dimension function vanishes
> at closed points, the dimension of the set of points of an integral closed subspace `Z` of a
> good algebraic space is the δ-dimension of `Z`, a nonnegative integer.

```lean
theorem topologicalKrullDim_points_eq_deltaDimension :
    0 ≤ deltaDimension D sX Z ∧
      topologicalKrullDim (points D.site D.base D.base_mem Z.subspace.toFunctor) =
        (((deltaDimension D sX Z).toNat : ℕ∞) : WithBot ℕ∞)
```

**`AlgebraicGeometry.Space.localRingDimension_eq_deltaDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean#L436). The attribute's comment: “part (4): the dimension of the local ring at a closed point is the value of the induced delta function at the generic point”.

> **Stacks 0EDW, parts (1) and (4).** Over a Jacobson base whose dimension function vanishes
> at closed points, the dimension of the local ring of an integral closed subspace `Z` of a good
> algebraic space at a closed point of `|Z|` is the δ-dimension of `Z`, a nonnegative integer.

```lean
theorem localRingDimension_eq_deltaDimension
    (z : points D.site D.base D.base_mem Z.subspace.toFunctor)
    (hz : IsClosed ({z} : Set (points D.site D.base D.base_mem Z.subspace.toFunctor))) :
    0 ≤ deltaDimension D sX Z ∧
      localRingDimension D.site D.base D.base_mem z = ((deltaDimension D sX Z).toNat : ℕ∞)
```

**`AlgebraicGeometry.Space.ringKrullDim_etaleLocalRing_eq_deltaDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/JacobsonDeltaDimension.lean#L450). The attribute's comment: “part (5): the dimension of the étale local ring at a geometric point above a closed point is the value of the induced delta function at the generic point”.

> **Stacks 0EDW, parts (1) and (5).** Over a Jacobson base whose dimension function vanishes
> at closed points, the Krull dimension of the étale local ring of an integral closed subspace `Z`
> of a good algebraic space at a geometric point above a closed point of `|Z|` is the δ-dimension
> of `Z`, a nonnegative integer.

```lean
theorem ringKrullDim_etaleLocalRing_eq_deltaDimension
    (z : points D.site D.base D.base_mem Z.subspace.toFunctor)
    (hz : IsClosed ({z} : Set (points D.site D.base D.base_mem Z.subspace.toFunctor)))
    (zbar : GeometricPoint D.site D.base D.base_mem Z.subspace.toFunctor)
    (hzbar : zbar.LiesOver z) :
    0 ≤ deltaDimension D sX Z ∧
      ringKrullDim (etaleLocalRing D.site D.base D.base_mem Z.subspace.toFunctor zbar) =
        (((deltaDimension D sX Z).toNat : ℕ∞) : WithBot ℕ∞)
```

## Tag 0EDX, a definition

[Tag 0EDX](https://stacks.math.columbia.edu/tag/0EDX) in the Stacks Project.

**`AlgebraicGeometry.Space.deltaDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/Cycles.lean#L252). The attribute's comment: “the δ-dimension of an integral closed subspace”.

> **Stacks 0EDX, for an integral closed subspace.** The *δ-dimension* of an integral closed
> subspace `Z` of a good algebraic space `X/B` is the value of `δ_{X/B}` at the generic point of
> `|Z|`.

```lean
noncomputable def deltaDimension (D : BaseSpaceDimensionSituation.{u})
    {X : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u} (sX : X ⟶ D.space)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) : ℤ
```

**`AlgebraicGeometry.Space.deltaDimensionIrreducible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean#L103). The attribute's comment: “irreducible closed subsets”.

> **Stacks 0EDX.** The `δ`-dimension of an irreducible closed subset of the space of points
> of a good algebraic space: the induced dimension function at the generic point of the
> subset.

```lean
noncomputable def deltaDimensionIrreducible (f : X ⟶ D.space) (hf : D.IsGood f)
    (T : IrreducibleCloseds (points D.site D.base D.base_mem X)) : ℤ
```

**`AlgebraicGeometry.Space.deltaDimensionClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean#L113). The attribute's comment: “closed subsets”.

> **Stacks 0EDX.** The `δ`-dimension of an arbitrary closed subset of the space of points of
> a good algebraic space: the supremum, among the extended integers, of the `δ`-dimensions of its
> irreducible components.

```lean
noncomputable def deltaDimensionClosed (f : X ⟶ D.space) (hf : D.IsGood f)
    (T : Set (points D.site D.base D.base_mem X)) (hT : IsClosed T) : EInt
```

**`AlgebraicGeometry.Space.deltaDimensionSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/DeltaDimension.lean#L124). The attribute's comment: “closed subspaces”.

> **Stacks 0EDX.** The `δ`-dimension of a closed subspace of a good algebraic space: the
> `δ`-dimension of its set of points.

```lean
noncomputable def deltaDimensionSubspace (f : X ⟶ D.space) (hf : D.IsGood f) (Z : Subfunctor X)
    (hZ : IsClosedSubspace D.site D.base D.base_mem Z) : EInt
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.2, Tag 0EDS](https://stacks.math.columbia.edu/tag/0EDS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
