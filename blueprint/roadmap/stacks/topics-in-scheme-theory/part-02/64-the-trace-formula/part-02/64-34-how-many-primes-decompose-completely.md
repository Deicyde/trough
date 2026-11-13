---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_finite_closedPoints_frobeniusElements_topologicalClosure_eq_top
statement: formalized
proof: formalized
---

# 64.34 How many primes decompose completely?

Section 64.34 of the Stacks Project, [Tag 03W4](https://stacks.math.columbia.edu/tag/03W4). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03W5, a proposition

[Tag 03W5](https://stacks.math.columbia.edu/tag/03W5) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_closedPoints_frobeniusElements_topologicalClosure_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FrobeniusSplitting/Generation.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FrobeniusSplitting/Generation.lean#L181).

> **Stacks Project, Tag 03W5.** For a smooth, geometrically irreducible, proper curve over a
> finite field there is a finite set of closed points such that the set of **all** Frobenius elements
> at these points topologically generates the étale fundamental group.

```lean
theorem exists_finite_closedPoints_frobeniusElements_topologicalClosure_eq_top (k : Type u)
    [Field k] [Finite k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsCurve k f] [Smooth f]
    [IsProper f] [GeometricallyIrreducible f] (base : GeometricPoint X) :
    letI := FrobeniusSplitting.connectedSpace_of_isCurve f
    ∃ S : Set (closedPoints X), S.Finite ∧
      (Subgroup.closure (frobeniusElements base S)).topologicalClosure = ⊤
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.34, Tag 03W4](https://stacks.math.columbia.edu/tag/03W4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
