---
declaration: theorem
origin: cited
lean: TauCeti.gradedBracket_jacobi
statement: formalized
proof: formalized
---

# The Jacobi identity

**The Jacobi identity**, with the three terms transported to the degree `i + j + k + 2`.

```lean
TauCeti.gradedBracket_jacobi.{u} {p : ℕ} {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] {i j k : ℕ} (x : TauCeti.gradedPiece p G i) (y : TauCeti.gradedPiece p G j)
  (z : TauCeti.gradedPiece p G k) :
  (TauCeti.gradedCast p G ⋯)
          (((TauCeti.gradedBracket p G (i + j + 1) k) (((TauCeti.gradedBracket p G i j) x) y)) z) +
        (TauCeti.gradedCast p G ⋯)
          (((TauCeti.gradedBracket p G (j + k + 1) i) (((TauCeti.gradedBracket p G j k) y) z)) x) +
      (TauCeti.gradedCast p G ⋯)
        (((TauCeti.gradedBracket p G (k + i + 1) j) (((TauCeti.gradedBracket p G k i) z) x)) y) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.gradedBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/Basic.html#TauCeti.gradedBracket_jacobi).

## Sources

- [Tau Ceti documentation: `TauCeti.gradedBracket_jacobi`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/Basic.html#TauCeti.gradedBracket_jacobi)
- [Source of `TauCeti.gradedBracket_jacobi` in TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/Basic.lean#L638)
