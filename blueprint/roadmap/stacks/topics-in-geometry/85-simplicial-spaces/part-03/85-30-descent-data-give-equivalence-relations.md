---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.isEquivalenceRelation_faceMaps_of_equifibered
statement: formalized
proof: formalized
---

# 85.30 Descent data give equivalence relations

Section 85.30 of the Stacks Project, [Tag 024D](https://stacks.math.columbia.edu/tag/024D). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 024E, a lemma

[Tag 024E](https://stacks.math.columbia.edu/tag/024E) in the Stacks Project.

**`CategoryTheory.SimplicialObject.isEquivalenceRelation_faceMaps_of_equifibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/CechNerveEquivalenceRelation.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/CechNerveEquivalenceRelation.lean#L586). References: SGA 4 I (10.9), “special case”.

> If a simplicial object maps cartesianly to the Čech nerve of `f`, its two
> face maps from degree one form an internal equivalence relation.

```lean
theorem isEquivalenceRelation_faceMaps_of_equifibered {X S : C} (f : X ⟶ S)
    {Y : SimplicialObject C} (π : Y ⟶ (Arrow.mk f).cechNerve)
    (hπ : NatTrans.Equifibered π) :
    IsEquivalenceRelation (Y.δ (1 : Fin 2)) (Y.δ (0 : Fin 2))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.30, Tag 024D](https://stacks.math.columbia.edu/tag/024D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
