---
declaration: theorem
origin: cited
lean: TauCeti.closedZpowers_lieExp_eq_top_iff
statement: formalized
proof: formalized
---

# Kronecker's criterion

`lieExp X` is a topological generator of a connected commutative
Lie group if and only if `Λ + ℤ X` is dense in the Lie algebra, `Λ` the kernel of the
exponential.

```lean
TauCeti.closedZpowers_lieExp_eq_top_iff.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {G : Type u_3}
  [TopologicalSpace G] [ChartedSpace H G] [Group G] [FiniteDimensional ℝ E] [LieGroup I (↑⊤) G]
  [T2Space G] [IsMulCommutative G] [IsTopologicalGroup G] [PreconnectedSpace G]
  (X : LeftInvariantDerivation I G) :
  TauCeti.closedZpowers (lieExp X) = ⊤ ↔
    Dense ↑(TauCeti.lieExpAddMonoidHom.ker ⊔ AddSubgroup.zmultiples X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's identity in the algebra of smooth functions](../manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma in coordinates](../manifold/part-02/hadamards-lemma-in-coordinates.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.closedZpowers_lieExp_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.html#TauCeti.closedZpowers_lieExp_eq_top_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.closedZpowers_lieExp_eq_top_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.html#TauCeti.closedZpowers_lieExp_eq_top_iff)
- [Source of `TauCeti.closedZpowers_lieExp_eq_top_iff` in TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Lie/Exponential/CommutativeGroup/Kronecker.lean#L84)
