---
declaration: theorem
origin: cited
lean: TauCeti.gradedCartanMatrix_zigzagAlgebra
statement: formalized
proof: formalized
---

# TauCeti.gradedCartanMatrix_zigzagAlgebra

The categorical graded Cartan map of the public algebra has matrix `(1 + q²) I + q A_G`
in the vertex-projective and vertex-head class bases, including isolated vertices.

```lean
TauCeti.gradedCartanMatrix_zigzagAlgebra.{u, w} (k : Type w) [Field k] {V : Type u} [Finite V]
  (G : SimpleGraph V) [Fintype V] [DecidableEq V] [DecidableRel G.Adj] :
  TauCeti.gradedCartanMatrix (TauCeti.zigzagAlgebraIntegerGrade k G)
      (TauCeti.zigzagAlgebraGradedProjectiveClassBasis k G)
      (TauCeti.zigzagAlgebraGradedSimpleClassBasis k G) =
    (1 + LaurentPolynomial.T 2) • 1 +
      LaurentPolynomial.T 1 • SimpleGraph.adjMatrix (LaurentPolynomial ℤ) G
```

## Depends on

- [TauCeti.gradedCartanMatrix](../../part-04/grothendieck-groups-cartan-maps-and-euler-forms/tauceti-gradedcartanmatrix.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedCartanMatrix_zigzagAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/K0.html#TauCeti.gradedCartanMatrix_zigzagAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedCartanMatrix_zigzagAlgebra`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/K0.html#TauCeti.gradedCartanMatrix_zigzagAlgebra)
- [Source of `TauCeti.gradedCartanMatrix_zigzagAlgebra` in TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/K0.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/K0.lean#L277)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
