---
declaration: section
origin: cited
lean: Stacks.Algebraization.distanceFunction, Stacks.Algebraization.nonempty_distanceSystem_of_connectedComponent_inter, Stacks.Algebraization.distanceFunction_le_two_of_zigzag, Stacks.Algebraization.exists_max_dimensionFunction_on_closed, Stacks.Algebraization.distanceFunction_ge_dimensionFunction_sub_max, Stacks.Algebraization.distanceFunction_le_closureLocalDimension, Stacks.Algebraization.distanceFunction_closedPoint_eq_coheight, Stacks.Algebraization.distanceFunction_le_of_isOpenImmersion
statement: formalized
proof: formalized
---

# 52.18 A distance function

Section 52.18 of the Stacks Project, [Tag 0EIW](https://stacks.math.columbia.edu/tag/0EIW). 4 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EIX, an equation

[Tag 0EIX](https://stacks.math.columbia.edu/tag/0EIX) in the Stacks Project.

**`Stacks.Algebraization.distanceFunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFunction.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFunction.lean#L180). The attribute's comment: “the distance function”.

> **Stacks Project, Tag 0EIX.** The distance from a closed subset of a Noetherian scheme.
> It is the minimum weight of all systems of integral closed subschemes from `Z` to `y`, or
> infinity if there is no system.

```lean
public def distanceFunction (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (y : Y) : ℕ∞
```

**`Stacks.Algebraization.nonempty_distanceSystem_of_connectedComponent_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFunction.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFunction.lean#L296). The attribute's comment: “existence of a zigzag in a connected component meeting Z”.

> In a Noetherian scheme, a point connected to the closed subset `Z` admits a finite
> zigzag of integral closed subschemes beginning in `Z` and ending at that point.

```lean
public theorem nonempty_distanceSystem_of_connectedComponent_inter
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y) (y : Y)
    (h : (connectedComponent y ∩ (Z : Set Y)).Nonempty) :
    Nonempty (DistanceSystem Y Z y)
```

**`Stacks.Algebraization.distanceFunction_le_two_of_zigzag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceZigzagTwo.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceZigzagTwo.lean#L113). The attribute's comment: “a zigzag of weight two”.

> **Stacks Project, Tag 0EIX.** In a Noetherian scheme, if a point `z` of `Z` is an
> immediate specialization of `v`, `v` an immediate specialization of `w`, and `w ⤳ c ⤳ y` is a
> strict chain of length two, then `δ^Y_Z(y) ≤ 2`.

```lean
public theorem distanceFunction_le_two_of_zigzag (Y : Scheme.{u}) [IsNoetherian Y]
    (Z : Closeds Y) {z v w c y : Y} (hz : z ∈ (Z : Set Y))
    (hvz : v ⤳ z) (hcovvz : ∀ x, v ⤳ x → x ⤳ z → x = v ∨ x = z)
    (hwv : w ⤳ v) (hcovwv : ∀ x, w ⤳ x → x ⤳ v → x = w ∨ x = v)
    (hwc : w ⤳ c) (hcy : c ⤳ y) (hwc' : w ≠ c) (hcy' : c ≠ y) :
    distanceFunction Y Z y ≤ 2
```

## Tag 0EIY, a lemma

[Tag 0EIY](https://stacks.math.columbia.edu/tag/0EIY) in the Stacks Project.

**`Stacks.Algebraization.exists_max_dimensionFunction_on_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceDimensionFunction.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceDimensionFunction.lean#L58). The attribute's comment: “dimension_function_lower_bound”.

> **Stacks Project, Tag 0EIY.** A dimension function has a maximum on a nonempty closed
> subset of a Noetherian scheme.

```lean
public theorem exists_max_dimensionFunction_on_closed
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (hZ : (Z : Set Y).Nonempty) (δ : DimensionFunction Y) :
    ∃ m : ℤ, IsGreatest (δ '' (Z : Set Y)) m
```

**`Stacks.Algebraization.distanceFunction_ge_dimensionFunction_sub_max`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceDimensionFunction.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceDimensionFunction.lean#L190). The attribute's comment: “dimension_function_lower_bound”.

> **Stacks Project, Tag 0EIY.** The distance from `Z` is at least the value of a dimension
> function minus its maximum value on `Z`.

```lean
public theorem distanceFunction_ge_dimensionFunction_sub_max
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (δ : DimensionFunction Y) (m : ℤ)
    (hm : IsGreatest (δ '' (Z : Set Y)) m) (y : Y) :
    ((δ y - m).toNat : ℕ∞) ≤ distanceFunction Y Z y
```

**`Stacks.Algebraization.distanceFunction_le_closureLocalDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceLocalDimension.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceLocalDimension.lean#L75). The attribute's comment: “le_local_dimension”.

> **Stacks Project, Tag 0EIY.** The distance to `Z` is at most the local dimension of the
> closure of `y` at any specialization `z` lying in `Z`.

```lean
public theorem distanceFunction_le_closureLocalDimension
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (y z : Y) (hzy : z ∈ closure {y}) (hzZ : z ∈ (Z : Set Y)) :
    (distanceFunction Y Z y : WithBot ℕ∞) ≤
      Order.coheight (⟨z, hzy⟩ : (closure {y} : Set Y))
```

**`Stacks.Algebraization.distanceFunction_closedPoint_eq_coheight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceLocalRing.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceLocalRing.lean#L97). The attribute's comment: “local_catenary_eq_dimension”.

> **Stacks Project, Tag 0EIY.** The distance from the closed point of a catenary Noetherian
> local spectrum is the dimension of the closure of the given prime.

```lean
public theorem distanceFunction_closedPoint_eq_coheight
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hcat : Ring.IsCatenary A) (y : PrimeSpectrum A) :
    distanceFunction (Spec (.of A))
      ⟨{IsLocalRing.closedPoint A}, IsLocalRing.isClosed_singleton_closedPoint A⟩ y =
        Order.coheight y
```

**`Stacks.Algebraization.distanceFunction_le_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceOpenRestriction.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceOpenRestriction.lean#L121). The attribute's comment: “open_restriction_ge”.

> **Stacks Project, Tag 0EIY.** Restriction to an open subscheme does not
> decrease the distance from a closed subset.

```lean
public theorem distanceFunction_le_of_isOpenImmersion
    {U Y : Scheme.{u}} (j : U ⟶ Y) [IsOpenImmersion j] [IsNoetherian Y]
    (Z : Closeds Y) (x : U) :
    letI : IsNoetherian U :=
      { toIsLocallyNoetherian := isLocallyNoetherian_of_isOpenImmersion j
        toCompactSpace := (j.isOpenEmbedding.isInducing.noetherianSpace).compactSpace }
    distanceFunction Y Z (j x) ≤ distanceFunction U (Z.preimage j.continuous) x
```

**`Stacks.Algebraization.distanceFunction_le_add_one_of_isImmediateSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSpecialization.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSpecialization.lean#L196). The attribute's comment: “immediate_specialization_bound”.

> **Stacks Project, Tag 0EIY.** An immediate specialization raises the distance from a
> closed subset by at most one when passing from the special point to the generic point.

```lean
public theorem distanceFunction_le_add_one_of_isImmediateSpecialization
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (hY : IrreducibleClosedsCodim.IsCatenarySpace Y)
    {y' y : Y} (h : IsImmediateSpecialization y' y) :
    distanceFunction Y Z y' ≤ distanceFunction Y Z y + 1
```

**`Stacks.Algebraization.distanceFunction_le_of_zigzag_specializations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSpecialization.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSpecialization.lean#L225). The attribute's comment: “zigzag_bound”.

> **Stacks Project, Tag 0EIY.** In a zigzag starting in `Z`, each immediate leftward
> specialization increases the possible distance by at most one.

```lean
public theorem distanceFunction_le_of_zigzag_specializations
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y)
    (hY : IrreducibleClosedsCodim.IsCatenarySpace Y)
    (k : ℕ) (y : Fin (k + 1) → Y) (y' : Fin k → Y)
    (hzero : y ⟨0, Nat.zero_lt_succ k⟩ ∈ (Z : Set Y))
    (hleft : ∀ i : Fin k, IsImmediateSpecialization (y' i) (y (Fin.castSucc i)))
    (hright : ∀ i : Fin k, y' i ⤳ y (Fin.succ i)) :
    distanceFunction Y Z (y (Fin.last k)) ≤ (k : ℕ∞)
```

**`Stacks.Algebraization.distanceFunction_sublevel_stableUnderSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSublevel.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSublevel.lean#L267). The attribute's comment: “sublevel_specialization_stable”.

> **Stacks Project, Tag 0EIY.** Sublevel sets of the distance from a closed subset of a
> Noetherian scheme are stable under specialization.

```lean
public theorem distanceFunction_sublevel_stableUnderSpecialization
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y) (k : ℕ∞) :
    StableUnderSpecialization {y : Y | distanceFunction Y Z y ≤ k}
```

**`Stacks.Algebraization.distanceFunction_eq_zero_iff_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceVanishing.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceVanishing.lean#L78). The attribute's comment: “zero_iff_mem”.

> **Stacks Project, Tag 0EIY.** A point has distance zero from a closed subset precisely
> when it lies in that subset.

```lean
public theorem distanceFunction_eq_zero_iff_mem (Y : Scheme.{u}) [IsNoetherian Y]
    (Z : Closeds Y) (y : Y) :
    distanceFunction Y Z y = 0 ↔ y ∈ (Z : Set Y)
```

## Tag 0EIZ, a lemma

[Tag 0EIZ](https://stacks.math.columbia.edu/tag/0EIZ) in the Stacks Project.

**`Stacks.Algebraization.distanceFunction_add_trdeg_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFiniteType.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceFiniteType.lean#L1075).

> **Stacks Project, Tag 0EIZ.** For a finite type morphism with fibres of dimension at
> most `e`, the distance at the image point is at most the distance at the source point
> plus `e` minus the residue-field transcendence degree.

```lean
public theorem distanceFunction_add_trdeg_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsNoetherian Y]
    [LocallyOfFiniteType f] [QuasiCompact f]
    (hY : Scheme.IsUniversallyCatenary Y)
    (I : Y.IdealSheafData) (e : ℕ)
    (he : ∀ y : Y, topologicalKrullDim (f.fiber y) ≤ (e : WithBot ℕ∞))
    (x : X) :
    let : IsNoetherian X :=
      { toIsLocallyNoetherian := LocallyOfFiniteType.isLocallyNoetherian f
        toCompactSpace := QuasiCompact.compactSpace_of_compactSpace f }
    let := (f.residueFieldMap x).hom.toAlgebra
    distanceFunction Y I.support (f x) +
        Cardinal.toENat (Algebra.trdeg (Y.residueField (f x)) (X.residueField x)) ≤
      distanceFunction X (I.comap f).support x + (e : ℕ∞)
```

## Tag 0EJ1, an example

[Tag 0EJ1](https://stacks.math.columbia.edu/tag/0EJ1) in the Stacks Project.

**`Stacks.Algebraization.distanceFunction_eq_topologicalKrullDim_add_curveChainDistance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceCurveChain.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceCurveChain.lean#L594). The attribute's comment: “A generalization of case (1) is if Y is of finite type over a field and Z = {z} is a closed point. Then δ_Z(y) = δ(y) + t where t is the minimum length of a chain of curves connecting z to a closed point of the closure of {y}.”.

> **Stacks Project, Tag 0EJ1, closing sentence.** Let `Y` be of finite type over a field and
> `Z = {z}` a closed point. Then `δ_Z(y) = δ(y) + t`, where `δ(y) = dim closure {y}` is the usual
> dimension function and `t` is the minimum length of a chain of curves connecting `z` to a closed
> point of `closure {y}`.
>
> Both sides may be infinite: `t = ∞` when no chain of curves exists, which happens exactly when
> `z` and `y` lie in different connected components, and then `δ_Z(y) = ∞` as well. The equality is
> read in `WithBot ℕ∞`, where `dim closure {y}` lives.

```lean
public theorem distanceFunction_eq_topologicalKrullDim_add_curveChainDistance
    {k : Type u} [Field k] (f : Y ⟶ Spec (CommRingCat.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] (z y : Y) (hz : IsClosed ({z} : Set Y)) :
    let : IsNoetherian Y :=
      { toIsLocallyNoetherian := LocallyOfFiniteType.isLocallyNoetherian f
        toCompactSpace := QuasiCompact.compactSpace_of_compactSpace f }
    ((distanceFunction Y (⟨{z}, hz⟩ : Closeds Y) y : ℕ∞) : WithBot ℕ∞) =
      topologicalKrullDim (closure ({y} : Set Y)) +
        ((curveChainDistance Y z (closure {y}) : ℕ∞) : WithBot ℕ∞)
```

**`Stacks.Algebraization.distanceFunction_eq_sub_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean#L106). The attribute's comment: “subvariety_specializes”.

> **Stacks Project, Tag 0EJ1, case (2b).** If `y ⤳ ζ`, i.e. the subvariety `closure {ζ}` is
> contained in `closure {y}`, the distance from `closure {ζ}` to `y` is `δ(y) - δ(ζ)`.

```lean
public theorem distanceFunction_eq_sub_of_specializes
    (Y : Scheme.{u}) [IsNoetherian Y] (δ : DimensionFunction Y) (ζ y : Y) (h : y ⤳ ζ) :
    distanceFunction Y (⟨closure {ζ}, isClosed_closure⟩ : Closeds Y) y =
      ((δ y - δ ζ).toNat : ℕ∞)
```

**`Stacks.Algebraization.distanceFunction_eq_of_isClosed_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean#L149). The attribute's comment: “closed_point_specializes”.

> **Stacks Project, Tag 0EJ1, case (1a).** If `z` is a closed point and `y ⤳ z`, the distance
> from `{z}` to `y` is `δ(y)`.

```lean
public theorem distanceFunction_eq_of_isClosed_of_specializes
    (Y : Scheme.{u}) [IsNoetherian Y] (δ : DimensionFunction Y) (z y : Y)
    (hz : IsClosed ({z} : Set Y)) (hz0 : δ z = 0) (h : y ⤳ z) :
    distanceFunction Y (⟨{z}, hz⟩ : Closeds Y) y = ((δ y).toNat : ℕ∞)
```

**`Stacks.Algebraization.distanceFunction_eq_one_of_not_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean#L240). The attribute's comment: “subvariety_codim_small”.

> **Stacks Project, Tag 0EJ1, case (2c).** If `ζ` does not specialize to `y` and
> `δ(y) ≤ δ(ζ)`, the distance from `closure {ζ}` to `y` is `1`.

```lean
public theorem distanceFunction_eq_one_of_not_specializes
    (Y : Scheme.{u}) [IsNoetherian Y] [IrreducibleSpace Y] (δ : DimensionFunction Y) (ζ y : Y)
    (h : ¬ ζ ⤳ y) (hle : δ y ≤ δ ζ) :
    distanceFunction Y (⟨closure {ζ}, isClosed_closure⟩ : Closeds Y) y = 1
```

**`Stacks.Algebraization.distanceFunction_eq_sub_add_one_of_not_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean#L378). The attribute's comment: “subvariety_codim_large”.

> **Stacks Project, Tag 0EJ1, case (2d).** If `y` does not specialize to `ζ` and
> `δ(ζ) < δ(y)`, the distance from `closure {ζ}` to `y` is `δ(y) - δ(ζ) + 1`.

```lean
public theorem distanceFunction_eq_sub_add_one_of_not_specializes
    (Y : Scheme.{u}) [IsNoetherian Y] [IrreducibleSpace Y] (δ : DimensionFunction Y) (ζ y : Y)
    (h : ¬ y ⤳ ζ) (hlt : δ ζ < δ y) :
    distanceFunction Y (⟨closure {ζ}, isClosed_closure⟩ : Closeds Y) y =
      ((δ y - δ ζ).toNat : ℕ∞) + 1
```

**`Stacks.Algebraization.distanceFunction_eq_add_one_of_not_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceSubvariety.lean#L394). The attribute's comment: “closed_point_not_specializes”.

> **Stacks Project, Tag 0EJ1, case (1b).** If `z` is a closed point and `y` does not
> specialize to `z`, the distance from `{z}` to `y` is `δ(y) + 1`.

```lean
public theorem distanceFunction_eq_add_one_of_not_specializes
    (Y : Scheme.{u}) [IsNoetherian Y] [IrreducibleSpace Y] (δ : DimensionFunction Y) (z y : Y)
    (hz : IsClosed ({z} : Set Y)) (hz0 : δ z = 0) (h : ¬ y ⤳ z) :
    distanceFunction Y (⟨{z}, hz⟩ : Closeds Y) y = ((δ y).toNat : ℕ∞) + 1
```

**`Stacks.Algebraization.distanceFunction_eq_zero_of_closure_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DistanceVanishing.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DistanceVanishing.lean#L110). The attribute's comment: “subvariety_contains_w”.

> **Stacks Project, Tag 0EJ1.** The distance to a closed subset containing the closure of a
> point is zero.

```lean
public theorem distanceFunction_eq_zero_of_closure_subset
    (Y : Scheme.{u}) [IsNoetherian Y] (Z : Closeds Y) (y : Y)
    (h : closure ({y} : Set Y) ⊆ (Z : Set Y)) :
    distanceFunction Y Z y = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.18, Tag 0EIW](https://stacks.math.columbia.edu/tag/0EIW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
