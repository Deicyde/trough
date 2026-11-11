---
declaration: def
origin: cited
lean: TauCeti.CircleSobolev.neckGraph
statement: formalized
---

# TauCeti.CircleSobolev.neckGraph

The **neck graph** of the plumbing `xy = a`: the pairs `(F, G)` of elements of `H^s` whose
Fourier coefficients satisfy `F₋ₙ = -aⁿ Gₙ` and `G₋ₙ = -aⁿ Fₙ` for every `n > 0`. This is the
linearized node equation `F(x) + G(a / x) = const` on the neck, written in the Fourier
coefficients on its two outer boundary circles
(`CircleSobolev.hasSum_zpow_smul_coeff_of_mem_neckGraph`).

```lean
TauCeti.CircleSobolev.neckGraph.{u_1} (s : ℝ) (E : Type u_1) [NormedAddCommGroup E]
  [NormedSpace ℂ E] (a : ℂ) : Submodule ℂ (TauCeti.CircleSobolev s E × TauCeti.CircleSobolev s E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.neckGraph`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Neck.html#TauCeti.CircleSobolev.neckGraph).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.neckGraph`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Neck.html#TauCeti.CircleSobolev.neckGraph)
- [Source of `TauCeti.CircleSobolev.neckGraph` in TauCeti/Analysis/Sobolev/Circle/Neck.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Neck.lean#L362)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
