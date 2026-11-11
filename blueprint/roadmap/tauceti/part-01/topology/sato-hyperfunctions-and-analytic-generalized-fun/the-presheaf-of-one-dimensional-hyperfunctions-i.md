---
declaration: theorem
origin: cited
lean: TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated
statement: formalized
proof: formalized
---

# The presheaf of one-dimensional hyperfunctions is separated

a section that vanishes on
the members of an open cover vanishes.

```lean
TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated :
  CategoryTheory.Presheaf.IsSeparated (Opens.grothendieckTopology ↑↧ℝ)
    TauCeti.Hyperfunction.oneDimBoundaryPresheaf
```

## Depends on

- [TauCeti.Hyperfunction.OneDimBoundaryQuotient](tauceti-hyperfunction-onedimboundaryquotient.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/OneDimensional.html#TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated).

## Sources

- [Tau Ceti documentation: `TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/OneDimensional.html#TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated)
- [Source of `TauCeti.Hyperfunction.oneDimBoundaryPresheaf_isSeparated` in TauCeti/Analysis/Hyperfunction/OneDimensional.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Hyperfunction/OneDimensional.lean#L313)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Hyperfunctions/STATUS.md)
