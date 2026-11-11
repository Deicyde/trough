---
declaration: theorem
origin: cited
lean: CStarMatrix.gram_nonneg
statement: formalized
proof: formalized
---

# CStarMatrix.gram_nonneg

The Gram matrix of a finite family in a right Hilbert C⋆-module is positive.

```lean
CStarMatrix.gram_nonneg.{u_1, u_2, u_3} {A : Type u_1} {E : Type u_2} {n : Type u_3}
  [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A] [AddCommGroup E]
  [_root_.Module ℂ E] [SMul Aᵐᵒᵖ E] [Norm E] [CStarModule Aᵐᵒᵖ E] [Fintype n] (x : n → E) :
  0 ≤ CStarMatrix.gram A x
```

## Depends on

- [CStarMatrix.gram](cstarmatrix-gram.md)

## Proof depends on

- [CStarMatrix.nonneg_iff_forall_sum_nonneg](cstarmatrix-nonneg-iff-forall-sum-nonneg.md)

## Lean

Formalized in Tau Ceti as [`CStarMatrix.gram_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Gram.html#CStarMatrix.gram_nonneg).

## Sources

- [Tau Ceti documentation: `CStarMatrix.gram_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Gram.html#CStarMatrix.gram_nonneg)
- [Source of `CStarMatrix.gram_nonneg` in TauCeti/Analysis/CStarAlgebra/Module/Gram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Module/Gram.lean#L77)
- [Tau Ceti roadmap status: Hilbert C*-modules, Morita equivalence, and continuous trace](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HilbertModules/STATUS.md)
