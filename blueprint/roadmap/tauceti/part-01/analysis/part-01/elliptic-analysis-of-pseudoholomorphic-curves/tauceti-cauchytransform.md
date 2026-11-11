---
declaration: def
origin: cited
lean: TauCeti.cauchyTransform
statement: formalized
---

# TauCeti.cauchyTransform

The planar Cauchy transform with the normalization inverting `bar∂`, using the kernel
`(w - z)⁻¹`. For rough compactly supported `Lᵖ` data the integral exists almost everywhere.

```lean
TauCeti.cauchyTransform.{u_1} {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℂ F] (f : ℂ → F)
  (w : ℂ) : F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cauchyTransform`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#TauCeti.cauchyTransform).

## Sources

- [Tau Ceti documentation: `TauCeti.cauchyTransform`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Pompeiu/Basic.html#TauCeti.cauchyTransform)
- [Source of `TauCeti.cauchyTransform` in TauCeti/Analysis/Complex/Pompeiu/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Pompeiu/Basic.lean#L96)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
