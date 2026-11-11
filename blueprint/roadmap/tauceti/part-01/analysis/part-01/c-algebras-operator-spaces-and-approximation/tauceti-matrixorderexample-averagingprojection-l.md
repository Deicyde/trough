---
declaration: theorem
origin: cited
lean: TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq
statement: formalized
proof: formalized
---

# TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq

Squaring does not preserve the order above a positive projection.

```lean
TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq :
  TauCeti.MatrixOrderExample.averagingProjection ≤ TauCeti.MatrixOrderExample.diagonal (5 / 8) 5 ∧
    ¬TauCeti.MatrixOrderExample.averagingProjection ^ 2 ≤
        TauCeti.MatrixOrderExample.diagonal (5 / 8) 5 ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CStarMatrix.nonneg_iff_posSemidef](cstarmatrix-nonneg-iff-possemidef.md)
- [Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg](matrix-ishermitian-possemidef-iff-trace-nonneg-a.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq)
- [Source of `TauCeti.MatrixOrderExample.averagingProjection_le_diagonal_not_sq` in TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean#L150)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
