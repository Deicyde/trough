---
declaration: theorem
origin: cited
lean: TauCeti.dense_setOf_closedZpowers_lieExp_eq_top
statement: formalized
proof: formalized
---

# Kronecker's theorem in the Lie algebra

In a compact connected commutative Lie group, the
derivations `X` whose exponential is a topological generator form a dense subset of the Lie
algebra.

```lean
TauCeti.dense_setOf_closedZpowers_lieExp_eq_top.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) {G : Type u_3} [TopologicalSpace G] [ChartedSpace H G] [Group G]
  [FiniteDimensional ℝ E] [LieGroup I (↑⊤) G] [T2Space G] [IsMulCommutative G]
  [IsTopologicalGroup G] [CompactSpace G] [PreconnectedSpace G] :
  Dense {X | TauCeti.closedZpowers (lieExp X) = ⊤}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's identity in the algebra of smooth functions](../manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../manifold/part-02/hadamards-lemma.md)
- [Kronecker's criterion](kroneckers-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dense_setOf_closedZpowers_lieExp_eq_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.html#TauCeti.dense_setOf_closedZpowers_lieExp_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.dense_setOf_closedZpowers_lieExp_eq_top`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.html#TauCeti.dense_setOf_closedZpowers_lieExp_eq_top)
- [Source of `TauCeti.dense_setOf_closedZpowers_lieExp_eq_top` in TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.lean#L112)
