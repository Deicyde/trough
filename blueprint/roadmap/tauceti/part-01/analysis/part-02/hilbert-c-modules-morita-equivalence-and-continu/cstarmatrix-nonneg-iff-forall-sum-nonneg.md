---
declaration: theorem
origin: cited
lean: CStarMatrix.nonneg_iff_forall_sum_nonneg
statement: formalized
proof: formalized
---

# CStarMatrix.nonneg_iff_forall_sum_nonneg

A matrix over a C⋆-algebra is positive exactly when all its finite quadratic forms are
positive.

```lean
CStarMatrix.nonneg_iff_forall_sum_nonneg.{u_1, u_2} {n : Type u_1} {A : Type u_2} [Fintype n]
  [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A] {M : CStarMatrix n n A} :
  0 ≤ M ↔ ∀ (x : n → A), 0 ≤ ∑ i, ∑ j, star (x i) * M i j * x j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CStarMatrix.nonneg_iff_forall_sum_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CStarMatrix.html#CStarMatrix.nonneg_iff_forall_sum_nonneg).

## Sources

- [Tau Ceti documentation: `CStarMatrix.nonneg_iff_forall_sum_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/CStarMatrix.html#CStarMatrix.nonneg_iff_forall_sum_nonneg)
- [Source of `CStarMatrix.nonneg_iff_forall_sum_nonneg` in TauCeti/Analysis/CStarAlgebra/CStarMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/CStarMatrix.lean#L194)
- [Tau Ceti roadmap status: Hilbert C*-modules, Morita equivalence, and continuous trace](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HilbertModules/STATUS.md)
