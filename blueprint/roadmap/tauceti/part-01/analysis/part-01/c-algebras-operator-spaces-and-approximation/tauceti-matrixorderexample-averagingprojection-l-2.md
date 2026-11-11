---
declaration: theorem
origin: cited
lean: TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal
statement: formalized
proof: formalized
---

# TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal

Square roots preserve the order above the averaging projection.

```lean
TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal {s t : ℝ}
  (h : TauCeti.MatrixOrderExample.averagingProjection ≤ TauCeti.MatrixOrderExample.diagonal s t) :
  TauCeti.MatrixOrderExample.averagingProjection ≤
    CFC.sqrt (TauCeti.MatrixOrderExample.diagonal s t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal)
- [Source of `TauCeti.MatrixOrderExample.averagingProjection_le_sqrt_diagonal` in TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean#L136)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
