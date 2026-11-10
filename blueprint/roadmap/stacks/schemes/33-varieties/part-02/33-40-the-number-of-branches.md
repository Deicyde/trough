---
declaration: section
origin: cited
lean: AlgebraicGeometry.numberOfBranches_eq_encard_normalizationFiber, AlgebraicGeometry.numberOfGeometricBranches_eq_card_sigma_sepDegree_normalization, AlgebraicGeometry.numberOfGeometricBranches_baseChange_fieldExtension, AlgebraicGeometry.isGeometricallyUnibranchAt_iff_of_fieldExtension, IsLocalRing.IsWedge, Ring.deltaInvariant_ge_numberOfGeometricBranches_sub_one_of_strictlyHenselian, Ring.exists_isWedge_of_deltaInvariant_eq_numberOfGeometricBranches_sub_one, Ring.deltaInvariant_ge_numberOfGeometricBranches_sub_one
statement: formalized
proof: formalized
---

# 33.40 The number of branches

Section 33.40 of the Stacks Project, [Tag 0C3Z](https://stacks.math.columbia.edu/tag/0C3Z). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C1S, a lemma

[Tag 0C1S](https://stacks.math.columbia.edu/tag/0C1S) in the Stacks Project.

**`AlgebraicGeometry.numberOfBranches_eq_encard_normalizationFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationBranches.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationBranches.lean#L77). The attribute's comment: “branches”.

> The number of branches at a point equals the number of points of the normalization above it.

```lean
public theorem numberOfBranches_eq_encard_normalizationFiber
    (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    AlgebraicGeometry.numberOfBranches X x =
      Set.encard {y : Scheme.normalizationScheme X hX |
        Scheme.normalization X hX y = x}
```

**`AlgebraicGeometry.numberOfGeometricBranches_eq_card_sigma_sepDegree_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationBranches.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/NormalizationBranches.lean#L112). The attribute's comment: “geometric\_branches”.

> The number of geometric branches at a point is the sum, over the points of the normalization
> above it, of the separable degrees of the corresponding residue-field extensions, interpreted
> as the extended cardinality of the sigma type of these multiplicities.

```lean
public theorem numberOfGeometricBranches_eq_card_sigma_sepDegree_normalization
    (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (x : X) :
    AlgebraicGeometry.numberOfGeometricBranches X x =
      ENat.card (Σ y : {y : Scheme.normalizationScheme X hX //
          Scheme.normalization X hX y = x},
        letI := (((X.residueFieldCongr y.property).inv ≫
          (Scheme.normalization X hX).residueFieldMap y).hom).toAlgebra
        (Field.sepDegree (X.residueField x)
          ((Scheme.normalizationScheme X hX).residueField y)).ord.ToType)
```

## Tag 0C40, a lemma

[Tag 0C40](https://stacks.math.columbia.edu/tag/0C40) in the Stacks Project.

**`AlgebraicGeometry.numberOfGeometricBranches_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/GeometricBranchesFieldChange.lean, line 1030](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/GeometricBranchesFieldChange.lean#L1030).

> The number of geometric branches at a point of a scheme locally of finite type over a field
> is unchanged after extending the ground field and choosing a point above it.

```lean
public theorem numberOfGeometricBranches_baseChange_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y = x) :
    AlgebraicGeometry.numberOfGeometricBranches X x =
      AlgebraicGeometry.numberOfGeometricBranches
        (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}) y
```

## Tag 0C55, a lemma

[Tag 0C55](https://stacks.math.columbia.edu/tag/0C55) in the Stacks Project.

**`AlgebraicGeometry.isGeometricallyUnibranchAt_iff_of_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/GeometricBranchesFieldChange.lean, line 1125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/GeometricBranchesFieldChange.lean#L1125). References: EGA IV (6.15.7), “loc. finite type, at x”.

> **Stacks Project, Tag 0C55.** Geometric unibranchness at a point is invariant under
> extension of the ground field for a scheme locally of finite type over that field.

```lean
public theorem isGeometricallyUnibranchAt_iff_of_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y = x) :
    IsGeometricallyUnibranchAt X x ↔
      IsGeometricallyUnibranchAt
        (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}) y
```

## Tag 0C41, a definition

[Tag 0C41](https://stacks.math.columbia.edu/tag/0C41) in the Stacks Project.

**`IsLocalRing.IsWedge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Branches/Wedge.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Branches/Wedge.lean#L65).

> A local ring `A` is a wedge of the nonempty finite family
> `B` if their residue fields can be identified and `A` is isomorphic to the subring of the
> product consisting of tuples with a common residue.

```lean
public def IsWedge (A : Type u) {n : ℕ} (B : Fin (n + 1) → Type v)
    [CommRing A] [IsLocalRing A] [∀ i, CommRing (B i)] [∀ i, IsLocalRing (B i)] : Prop
```

## Tag 0C42, a lemma

[Tag 0C42](https://stacks.math.columbia.edu/tag/0C42) in the Stacks Project.

**`Ring.deltaInvariant_ge_numberOfGeometricBranches_sub_one_of_strictlyHenselian`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaBranchBound.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaBranchBound.lean#L78). The attribute's comment: “delta\_ge\_branches\_sub\_one”.

> The delta invariant of a strictly henselian reduced Nagata
> local ring is at least the number of its geometric branches minus one.

```lean
public lemma deltaInvariant_ge_numberOfGeometricBranches_sub_one_of_strictlyHenselian
    (A : Type u) [CommRing A] [IsReduced A]
    [StrictlyHenselianLocalRing A]
    (hA : IsNagataRing A) :
    Ring.deltaInvariant A ≥
      numberOfGeometricBranchesOfLocalRing A - 1
```

**`Ring.exists_isWedge_of_deltaInvariant_eq_numberOfGeometricBranches_sub_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaBranchBound.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaBranchBound.lean#L350). The attribute's comment: “equality\_implies\_wedge”.

> A strictly henselian, reduced, one-dimensional Nagata local ring attaining the lower bound
> for its delta invariant is a wedge of a nonempty finite family of strictly henselian discrete
> valuation rings.

```lean
public theorem exists_isWedge_of_deltaInvariant_eq_numberOfGeometricBranches_sub_one
    (A : Type u) [CommRing A] [IsReduced A]
    [StrictlyHenselianLocalRing A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1)
    (hdelta : Ring.deltaInvariant A =
      numberOfGeometricBranchesOfLocalRing A - 1) :
    ∃ (n : ℕ) (B : Fin (n + 1) → Type u)
      (_ : ∀ i, CommRing (B i)) (_ : ∀ i, IsDomain (B i))
      (_ : ∀ i, IsLocalRing (B i)) (_ : ∀ i, IsDiscreteValuationRing (B i))
      (_ : ∀ i, StrictlyHenselianLocalRing (B i)),
      IsLocalRing.IsWedge A B
```

## Tag 0C43, a lemma

[Tag 0C43](https://stacks.math.columbia.edu/tag/0C43) in the Stacks Project.

**`Ring.deltaInvariant_ge_numberOfGeometricBranches_sub_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaBranches/LowerBound.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/DeltaBranches/LowerBound.lean#L65).

> The delta invariant of a reduced one-dimensional Nagata local ring is at least the number
> of its geometric branches minus one.

```lean
public lemma deltaInvariant_ge_numberOfGeometricBranches_sub_one
    (A : Type*) [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    Ring.deltaInvariant A ≥
      numberOfGeometricBranchesOfLocalRing A - 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.40, Tag 0C3Z](https://stacks.math.columbia.edu/tag/0C3Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
