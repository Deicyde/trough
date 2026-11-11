---
declaration: theorem
origin: cited
lean: TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart
statement: formalized
proof: formalized
---

# TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart

A positive diagonal matrix can dominate the flip without dominating its positive part.

```lean
TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart :
  TauCeti.MatrixOrderExample.flip ≤ TauCeti.MatrixOrderExample.diagonal (1 / 2) 3 ∧
    ¬TauCeti.MatrixOrderExample.flip⁺ ≤ TauCeti.MatrixOrderExample.diagonal (1 / 2) 3
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CStarMatrix.nonneg_iff_posSemidef](cstarmatrix-nonneg-iff-possemidef.md)
- [Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg](matrix-ishermitian-possemidef-iff-trace-nonneg-a.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart).

## Sources

- [Tau Ceti documentation: `TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart`](https://taucetiproject.org/docs/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.html#TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart)
- [Source of `TauCeti.MatrixOrderExample.flip_le_diagonal_not_posPart` in TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Examples/Analysis/CStarAlgebra/MatrixOrder.lean#L143)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
