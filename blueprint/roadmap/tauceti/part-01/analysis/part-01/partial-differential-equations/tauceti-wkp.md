---
declaration: def
origin: cited
lean: TauCeti.Wkp
statement: formalized
---

# TauCeti.Wkp

The arbitrary-order, real-valued weak Sobolev space `W^{k,p}(Ω)`.  At order zero this is
`Lᵖ(Ω)`; order one is `W1p`; every further order adjoins the weak derivative of the highest
derivative field from the preceding order.

```lean
TauCeti.Wkp.{u} {E : Type u} [MeasurableSpace E] [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [BorelSpace E] (mu : MeasureTheory.Measure E) [mu.IsAddHaarMeasure]
  (Omega : TopologicalSpace.Opens E) (p : ENNReal) [Fact (1 ≤ p)] : ℕ → Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Wkp/Basic.html#TauCeti.Wkp).

## Sources

- [Tau Ceti documentation: `TauCeti.Wkp`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Wkp/Basic.html#TauCeti.Wkp)
- [Source of `TauCeti.Wkp` in TauCeti/Analysis/Sobolev/Wkp/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Wkp/Basic.lean#L144)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
