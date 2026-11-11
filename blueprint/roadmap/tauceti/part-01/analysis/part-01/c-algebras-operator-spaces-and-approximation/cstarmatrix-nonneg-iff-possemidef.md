---
declaration: theorem
origin: cited
lean: CStarMatrix.nonneg_iff_posSemidef
statement: formalized
proof: formalized
---

# CStarMatrix.nonneg_iff_posSemidef

Positivity in the matrix C⋆-algebra is ordinary positive semidefiniteness.

```lean
CStarMatrix.nonneg_iff_posSemidef.{u_1} {n : Type u_1} [Fintype n] {M : CStarMatrix n n ℂ} :
  0 ≤ M ↔ (CStarMatrix.ofMatrix.symm M).PosSemidef
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CStarMatrix.nonneg_iff_posSemidef`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/MatrixOrder.html#CStarMatrix.nonneg_iff_posSemidef).

## Sources

- [Tau Ceti documentation: `CStarMatrix.nonneg_iff_posSemidef`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/MatrixOrder.html#CStarMatrix.nonneg_iff_posSemidef)
- [Source of `CStarMatrix.nonneg_iff_posSemidef` in TauCeti/Analysis/CStarAlgebra/MatrixOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/MatrixOrder.lean#L25)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
