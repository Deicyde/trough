---
declaration: theorem
origin: cited
lean: ProperSMul.instIsManifoldOrbitRelQuotient
statement: formalized
proof: formalized
---

# The quotient manifold theorem

The orbit space of a free proper smooth action of a
finite-dimensional Lie group `G` on a boundaryless smooth manifold `M` is a smooth manifold for
the slice charts `ProperSMul.orbitRelQuotientChartedSpace`.

```lean
ProperSMul.instIsManifoldOrbitRelQuotient.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {G : Type u_3} [TopologicalSpace G]
  [ChartedSpace H G] [Group G] [LieGroup I (↑⊤) G] {E' : Type u_4} [NormedAddCommGroup E']
  [NormedSpace ℝ E'] [FiniteDimensional ℝ E'] {H' : Type u_5} [TopologicalSpace H']
  {I' : ModelWithCorners ℝ E' H'} [I'.Boundaryless] {M : Type u_6} [TopologicalSpace M]
  [ChartedSpace H' M] [IsManifold I' (↑⊤) M] [MulAction G M] [ContMDiffSMul I I' (↑⊤) G M]
  [ProperSMul G M] [IsCancelSMul G M] :
  IsManifold (modelWithCornersSelf ℝ (ProperSMul.QuotientModelSpace E E')) (↑⊤)
    (MulAction.orbitRel.Quotient G M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The closed-subgroup theorem, with its model space](../../lie/the-closed-subgroup-theorem-with-its-model-space.md)
- [Hadamard's identity in the algebra of smooth functions](../part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../part-02/hadamards-lemma.md)
- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`ProperSMul.instIsManifoldOrbitRelQuotient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/Quotient.html#ProperSMul.instIsManifoldOrbitRelQuotient).

## Sources

- [Tau Ceti documentation: `ProperSMul.instIsManifoldOrbitRelQuotient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/GroupAction/Quotient.html#ProperSMul.instIsManifoldOrbitRelQuotient)
- [Source of `ProperSMul.instIsManifoldOrbitRelQuotient` in TauCeti/Geometry/Manifold/GroupAction/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/GroupAction/Quotient.lean#L288)
