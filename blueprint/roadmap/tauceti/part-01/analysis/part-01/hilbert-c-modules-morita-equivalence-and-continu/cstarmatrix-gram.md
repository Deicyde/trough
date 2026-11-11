---
declaration: def
origin: cited
lean: CStarMatrix.gram
statement: formalized
---

# CStarMatrix.gram

The Gram matrix `(⟨x i, x j⟩_A)_(i,j)` of a family `x` of vectors in a right Hilbert
`A`-module `E`, given as `CStarModule Aᵐᵒᵖ E`.

```lean
CStarMatrix.gram.{u_2, u_3, u_4} {E : Type u_2} {n : Type u_3} (A : Type u_4) [Inner Aᵐᵒᵖ E]
  (x : n → E) : CStarMatrix n n A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CStarMatrix.gram`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Gram.html#CStarMatrix.gram).

## Sources

- [Tau Ceti documentation: `CStarMatrix.gram`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Module/Gram.html#CStarMatrix.gram)
- [Source of `CStarMatrix.gram` in TauCeti/Analysis/CStarAlgebra/Module/Gram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Module/Gram.lean#L47)
- [Tau Ceti roadmap status: Hilbert C*-modules, Morita equivalence, and continuous trace](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HilbertModules/STATUS.md)
