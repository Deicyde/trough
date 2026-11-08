---
declaration: def
origin: cited
lean: TauCeti.Compactification.commonRefinement
statement: formalized
---

# TauCeti.Compactification.commonRefinement

The common refinement of two compactifications: the scheme-theoretic closure of the source
in the fibre product of their ambient schemes over the base.

```lean
TauCeti.Compactification.commonRefinement.{u} {X S : AlgebraicGeometry.Scheme} {f : X ⟶ S}
  (C₁ C₂ : TauCeti.Compactification f) : TauCeti.DenseCompactification f
```

## Depends on

- [TauCeti.Compactification](tauceti-compactification.md)
- [TauCeti.DenseCompactification](tauceti-densecompactification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Compactification.commonRefinement`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.Compactification.commonRefinement).

## Sources

- [Tau Ceti documentation: `TauCeti.Compactification.commonRefinement`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Refinement.html#TauCeti.Compactification.commonRefinement)
- [Source of `TauCeti.Compactification.commonRefinement` in TauCeti/AlgebraicGeometry/Compactification/Refinement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Compactification/Refinement.lean#L92)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
