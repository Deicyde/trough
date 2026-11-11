---
declaration: def
origin: cited
lean: TauCeti.DenseCompactification.isLimitCommonRefinementFan
statement: formalized
---

# TauCeti.DenseCompactification.isLimitCommonRefinementFan

The common refinement is the binary product in the category of dense compactifications.

```lean
TauCeti.DenseCompactification.isLimitCommonRefinementFan.{u} {X S : AlgebraicGeometry.Scheme}
  {f : X ⟶ S} (D₁ D₂ : TauCeti.DenseCompactification f) :
  CategoryTheory.Limits.IsLimit (D₁.commonRefinementFan D₂)
```

## Depends on

- [TauCeti.Compactification](tauceti-compactification.md)
- [TauCeti.Compactification.commonRefinement](tauceti-compactification-commonrefinement.md)
- [TauCeti.DenseCompactification](tauceti-densecompactification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseCompactification.isLimitCommonRefinementFan`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.DenseCompactification.isLimitCommonRefinementFan).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseCompactification.isLimitCommonRefinementFan`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.DenseCompactification.isLimitCommonRefinementFan)
- [Source of `TauCeti.DenseCompactification.isLimitCommonRefinementFan` in TauCeti/AlgebraicGeometry/Compactification/Refinement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Compactification/Refinement.lean#L217)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
