---
declaration: section
origin: cited
lean: AlgebraicGeometry.Simplicial.pointClass, AlgebraicGeometry.Simplicial.mem_pointClass_self, AlgebraicGeometry.Simplicial.pointClass_eq_of_nonempty_inter, AlgebraicGeometry.Simplicial.isCompact_relatedPoints, AlgebraicGeometry.DescentDatum.isEffective_of_iso_sigma_spec_isArtinianRing
statement: formalized
proof: formalized
---

# 85.31 An example case

Section 85.31 of the Stacks Project, [Tag 024F](https://stacks.math.columbia.edu/tag/024F). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 024G, a lemma

[Tag 024G](https://stacks.math.columbia.edu/tag/024G) in the Stacks Project.

**`AlgebraicGeometry.Simplicial.pointClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean#L135). The attribute's comment: “the subset T_y”.

> The points reached from `y` by a one-simplex whose first face is `y`.

```lean
def pointClass (Y : SimplicialObject Scheme.{u}) (y : Y _⦋0⦌) :
    Set (Y _⦋0⦌)
```

**`AlgebraicGeometry.Simplicial.mem_pointClass_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean#L142). The attribute's comment: “membership of y in T_y”.

> A point belongs to the subset of points reachable from it.

```lean
theorem mem_pointClass_self {X S : Scheme.{u}} (f : X ⟶ S)
    {Y : SimplicialObject Scheme.{u}} (π : Y ⟶ (Arrow.mk f).cechNerve)
    (hπ : NatTrans.Equifibered π) (y : Y _⦋0⦌) :
    y ∈ pointClass Y y
```

**`AlgebraicGeometry.Simplicial.pointClass_eq_of_nonempty_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean#L151). The attribute's comment: “intersecting classes are equal”.

> If two subsets of reachable points meet, they are the same subset.

```lean
theorem pointClass_eq_of_nonempty_inter {X S : Scheme.{u}} (f : X ⟶ S)
    {Y : SimplicialObject Scheme.{u}} (π : Y ⟶ (Arrow.mk f).cechNerve)
    (hπ : NatTrans.Equifibered π) (y y' : Y _⦋0⦌)
    (h : (pointClass Y y ∩ pointClass Y y').Nonempty) :
    pointClass Y y = pointClass Y y'
```

## Tag 024H, a lemma

[Tag 024H](https://stacks.math.columbia.edu/tag/024H) in the Stacks Project.

**`AlgebraicGeometry.Simplicial.isCompact_relatedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/CechNervePointClass.lean#L220).

> The vertices connected to a fixed vertex in a cartesian simplicial scheme
> over the Čech nerve of a quasi-compact morphism form a quasi-compact set.

```lean
theorem isCompact_relatedPoints {X S : Scheme.{u}} (f : X ⟶ S)
    [QuasiCompact f] {Y : SimplicialObject Scheme.{u}}
    (π : Y ⟶ (Arrow.mk f).cechNerve) (hπ : NatTrans.Equifibered π)
    (y : (Y _⦋0⦌)) :
    IsCompact {y' : (Y _⦋0⦌) | ∃ y₁ : (Y _⦋1⦌),
      (Y.δ (1 : Fin 2)).base y₁ = y ∧ (Y.δ (0 : Fin 2)).base y₁ = y'}
```

## Tag 024I, a lemma

[Tag 024I](https://stacks.math.columbia.edu/tag/024I) in the Stacks Project.

**`AlgebraicGeometry.DescentDatum.isEffective_of_iso_sigma_spec_isArtinianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ArtinianDisjointUnionDescent.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ArtinianDisjointUnionDescent.lean#L199). The attribute's comment: “effectivity of a datum carried by a disjoint union of Artinian spectra”.

> Let `f : X ⟶ S` be a quasi-compact, flat, surjective morphism of schemes and let `(V, φ)` be a
> descent datum relative to `X/S`. If `V` is a disjoint union of spectra of Artinian rings then
> `(V, φ)` is effective.

```lean
theorem isEffective_of_iso_sigma_spec_isArtinianRing [QuasiCompact f] [Flat f] [Surjective f]
    (D : DescentDatum f)
    (hV : ∃ (ι : Type u) (A : ι → CommRingCat.{u}), (∀ i, IsArtinianRing (A i)) ∧
      Nonempty (D.over.left ≅ ∐ fun i ↦ Spec (A i))) :
    DescentData.IsEffective D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.31, Tag 024F](https://stacks.math.columbia.edu/tag/024F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
