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
- [Source of `CStarMatrix.nonneg_iff_posSemidef` in TauCeti/Analysis/CStarAlgebra/MatrixOrder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/MatrixOrder.lean#L25)
- [Tau Ceti roadmap status: C*-algebras, operator spaces and approximation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CStarAlgebras/STATUS.md)
