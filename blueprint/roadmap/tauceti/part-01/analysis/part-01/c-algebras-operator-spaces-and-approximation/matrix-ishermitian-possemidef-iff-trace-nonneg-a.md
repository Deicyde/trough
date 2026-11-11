---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg
statement: formalized
proof: formalized
---

# Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg

A Hermitian `2 × 2` matrix is positive semidefinite exactly when its trace and
determinant are nonnegative.

```lean
Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  {H : Matrix (Fin 2) (Fin 2) 𝕜} (hH : H.IsHermitian) : H.PosSemidef ↔ 0 ≤ H.trace ∧ 0 ≤ H.det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/FinTwo.html#Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/PosSemidef/FinTwo.html#Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg)
- [Source of `Matrix.IsHermitian.posSemidef_iff_trace_nonneg_and_det_nonneg` in TauCeti/Analysis/Matrix/PosSemidef/FinTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/PosSemidef/FinTwo.lean#L44)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CStarAlgebras/STATUS.md)
