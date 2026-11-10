---
declaration: section
origin: cited
lean: AlgebraicGeometry.NumericalType.multiplicity_mul_intersection_le, AlgebraicGeometry.NumericalType.multiplicity_mul_weight_le, AlgebraicGeometry.NumericalType.multiplicity_mul_abs_intersection_self_le, AlgebraicGeometry.NumericalType.card_non_minus_two_indices_le, AlgebraicGeometry.NumericalType.multiplicity_mul_intersection_le_genus, AlgebraicGeometry.NumericalType.componentGenus_lt_genus, AlgebraicGeometry.NumericalType.multiplicity_mul_abs_intersection_le, AlgebraicGeometry.NumericalType.finrank_picardGroup_torsionBy_le_genus
statement: formalized
proof: formalized
---

# 55.7 Bounding invariants of numerical types

Section 55.7 of the Stacks Project, [Tag 0C9T](https://stacks.math.columbia.edu/tag/0C9T). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C9U, a lemma

[Tag 0C9U](https://stacks.math.columbia.edu/tag/0C9U) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.multiplicity_mul_intersection_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L83). The attribute's comment: “intersection bound”.

> A positive intersection with a component is bounded, after multiplication by
> its multiplicity, by the absolute diagonal contribution of the other component.

```lean
public lemma multiplicity_mul_intersection_le (T : NumericalType)
    (i j : Fin T.componentCount) (hij : 0 < T.intersection i j) :
    T.multiplicity i * T.intersection i j ≤
      T.multiplicity j * |T.intersection j j|
```

**`AlgebraicGeometry.NumericalType.multiplicity_mul_weight_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L93). The attribute's comment: “weight bound”.

> The multiplicity-weight product of a component meeting another component is
> bounded by the latter component's absolute diagonal contribution.

```lean
public lemma multiplicity_mul_weight_le (T : NumericalType)
    (i j : Fin T.componentCount) (hij : 0 < T.intersection i j) :
    T.multiplicity i * T.weight i ≤
      T.multiplicity j * |T.intersection j j|
```

## Tag 0C9V, a lemma

[Tag 0C9V](https://stacks.math.columbia.edu/tag/0C9V) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.multiplicity_mul_abs_intersection_self_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L117). The attribute's comment: “bound\_diagonal”.

> At a non-minus-two index of a minimal numerical type of genus at least two,
> the multiplicity times the absolute diagonal intersection is at most six times
> the genus minus six.

```lean
public lemma multiplicity_mul_abs_intersection_self_le
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) (hn : 1 < T.componentCount)
    (j : Fin T.componentCount) (hj : ¬ IsMinusTwoIndex T j) :
    T.multiplicity j * |T.intersection j j| ≤ 6 * g - 6
```

**`AlgebraicGeometry.NumericalType.card_non_minus_two_indices_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L182). The attribute's comment: “bound\_non\_minus\_two\_indices”.

> A minimal numerical type with more than one component has at most twice its
> genus minus two non-minus-two indices.

```lean
public lemma card_non_minus_two_indices_le
    (T : NumericalType) (hminimal : IsMinimal T) (hn : 1 < T.componentCount) :
    ((Finset.univ.filter (fun i : Fin T.componentCount => ¬ IsMinusTwoIndex T i)).card : ℤ) ≤
      2 * genus T - 2
```

**`AlgebraicGeometry.NumericalType.multiplicity_mul_intersection_le_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L212). The attribute's comment: “bound\_off\_diagonal”.

> The multiplicity-weighted intersection with a non-minus-two component of a
> minimal numerical type is at most six times its genus minus six.

```lean
public lemma multiplicity_mul_intersection_le_genus
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) (hn : 1 < T.componentCount)
    (i j : Fin T.componentCount) (hj : ¬ IsMinusTwoIndex T j) :
    T.multiplicity i * T.intersection i j ≤ 6 * g - 6
```

**`AlgebraicGeometry.NumericalType.componentGenus_lt_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/BoundingInvariants.lean#L229). The attribute's comment: “component\_genus\_lt”.

> A non-minus-two component of a minimal numerical type of genus at least two
> has genus strictly less than that of the numerical type.

```lean
public lemma componentGenus_lt_genus
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) (hn : 1 < T.componentCount)
    (j : Fin T.componentCount) (hj : ¬ IsMinusTwoIndex T j) :
    T.componentGenus j < g
```

## Tag 0C9W, a lemma

[Tag 0C9W](https://stacks.math.columbia.edu/tag/0C9W) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.multiplicity_mul_abs_intersection_le`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/UniformBound/DiameterBound.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/UniformBound/DiameterBound.lean#L306).

> For a minimal numerical type of genus at least two, each multiplicity-weighted
> absolute intersection is at most 768 times its genus.

```lean
public lemma multiplicity_mul_abs_intersection_le
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) (i j : Fin T.componentCount) :
    T.multiplicity i * |T.intersection i j| ≤ 768 * g
```

## Tag 0C9X, a proposition

[Tag 0C9X](https://stacks.math.columbia.edu/tag/0C9X) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.finrank_picardGroup_torsionBy_le_genus`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean#L332). The attribute's comment: “genus bound”.

> The prime torsion of the Picard group of a numerical type has dimension
> at most its genus, provided the prime exceeds 768 times the genus.

```lean
public lemma finrank_picardGroup_torsionBy_le_genus
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (ℓ : ℕ) [Fact ℓ.Prime] (hℓ : 768 * g < (ℓ : ℤ)) :
    let P := AddSubgroup.torsionBy (picardGroup T) (ℓ : ℤ)
    let : Module (ZMod ℓ) P := AddSubgroup.torsionBy.zmodModule
    (Module.finrank (ZMod ℓ) P : ℤ) ≤ g
```

**`AlgebraicGeometry.NumericalType.finrank_picardGroup_torsionBy_le_topGenus_of_isMinimal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean#L343). The attribute's comment: “topological genus bound for minimal types”.

> For a minimal numerical type, the topological genus bounds the dimension
> of the prime torsion of its Picard group.

```lean
public lemma finrank_picardGroup_torsionBy_le_topGenus_of_isMinimal
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) (ℓ : ℕ) [Fact ℓ.Prime]
    (hℓ : 768 * g < (ℓ : ℤ)) :
    let P := AddSubgroup.torsionBy (picardGroup T) (ℓ : ℤ)
    let : Module (ZMod ℓ) P := AddSubgroup.torsionBy.zmodModule
    (Module.finrank (ZMod ℓ) P : ℤ) ≤
      (1 : ℤ) - T.componentCount + edgeCount T
```

**`AlgebraicGeometry.NumericalType.topGenus_le_genus_of_isMinimal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/ClassificationProperSubgraphs/PicardTorsion.lean#L363). The attribute's comment: “topological genus at most genus”.

> The topological genus of a minimal numerical type of genus at least two
> does not exceed its genus.

```lean
public lemma topGenus_le_genus_of_isMinimal
    (T : NumericalType) (g : ℤ) (hg : 2 ≤ g) (hgenus : genus T = g)
    (hminimal : IsMinimal T) :
    (1 : ℤ) - T.componentCount + edgeCount T ≤ g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.7, Tag 0C9T](https://stacks.math.columbia.edu/tag/0C9T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
