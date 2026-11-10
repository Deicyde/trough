---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraic_residueField_and_jacobsonSpace, AlgebraicGeometry.jacobsonSpace_pullback_of_large_cardinality, Stacks.AlgebraicGeometry.ClosedPointResidue.exists_cardinal_isAlgebraic_residueField_of_mem_closedPoints_baseChange
statement: formalized
proof: formalized
---

# 33.14 Change of fields and the Jacobson property

Section 33.14 of the Stacks Project, [Tag 0477](https://stacks.math.columbia.edu/tag/0477). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0478, a lemma

[Tag 0478](https://stacks.math.columbia.edu/tag/0478) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraic_residueField_and_jacobsonSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/JacobsonClosedPoints.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/JacobsonClosedPoints.lean#L77). References: SGA 4 VIII (3.13), “partial”.

> Let `X` be a scheme locally of finite type over a field `k`. Then (1) for every closed point
> `x` of `X` the extension `κ(x)/k` is algebraic, and (2) `X` is a Jacobson scheme, that is, its
> underlying space is a Jacobson space.

```lean
public theorem isAlgebraic_residueField_and_jacobsonSpace (p : X ⟶ Spec (.of k))
    [LocallyOfFiniteType p] :
    (∀ x : X, IsClosed ({x} : Set X) →
        letI : Algebra k (X.residueField x) :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ p.appTop ≫ X.Γevaluation x).hom.toAlgebra
        Algebra.IsAlgebraic k (X.residueField x)) ∧ JacobsonSpace X
```

## Tag 0479, a lemma

[Tag 0479](https://stacks.math.columbia.edu/tag/0479) in the Stacks Project.

**`AlgebraicGeometry.jacobsonSpace_pullback_of_large_cardinality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Jacobson.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Jacobson.lean#L270). The attribute's comment: “base_change_jacobson”.

> The base change of a scheme to every sufficiently large extension of its ground field is a
> Jacobson scheme.

```lean
theorem jacobsonSpace_pullback_of_large_cardinality
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    ∃ κ : Cardinal.{u}, ∀ (K : Type u) [Field K] [Algebra k K],
      κ ≤ Cardinal.mk K →
        JacobsonSpace ↑(pullback f (Spec.map (ofHom (algebraMap k K))))
```

**`Stacks.AlgebraicGeometry.ClosedPointResidue.exists_cardinal_isAlgebraic_residueField_of_mem_closedPoints_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Varieties/ClosedPointResidue.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Varieties/ClosedPointResidue.lean#L330). The attribute's comment: “closed_point_residue_algebraic”.

> For every scheme over a field, after extending the field to one of sufficiently large
> cardinality, the residue field of every closed point of the base change is algebraic over the
> extended field.

```lean
theorem exists_cardinal_isAlgebraic_residueField_of_mem_closedPoints_baseChange
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) :
    ∃ κ : Cardinal.{u}, ∀ (K : Type u) [Field K] [Algebra k K], κ ≤ Cardinal.mk K →
      ∀ x : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}),
        x ∈ closedPoints
            (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}) →
          let p := pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
          letI : (p x).asIdeal.IsPrime := (p x).isPrime
          letI := ((CommRingCat.ofHom (algebraMap K (p x).asIdeal.ResidueField)) ≫
            (Scheme.Spec.residueFieldIso (.of K) (p x)).inv ≫
            p.residueFieldMap x).hom.toAlgebra
          Algebra.IsAlgebraic K
            ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
              Scheme.{u}).residueField x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.14, Tag 0477](https://stacks.math.columbia.edu/tag/0477)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
