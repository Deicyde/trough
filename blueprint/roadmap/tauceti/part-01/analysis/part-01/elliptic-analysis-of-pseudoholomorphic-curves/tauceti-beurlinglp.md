---
declaration: def
origin: cited
lean: TauCeti.beurlingLp
statement: formalized
---

# TauCeti.beurlingLp

The Beurling operator on all of Lp, for `1 < p < ∞`, as the bounded extension from Schwartz
functions of the L² Fourier multiplier.

```lean
TauCeti.beurlingLp.{u_1} {F : Type u_1} [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] (p : ENNReal) [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ↥(MeasureTheory.Lp F p MeasureTheory.volume) →L[ℂ] ↥(MeasureTheory.Lp F p MeasureTheory.volume)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mihlin–Hörmander multiplier theorem on `Lᵖ`](../partial-differential-equations/the-mihlin-hormander-multiplier-theorem-on-lp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.beurlingLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Beurling/Basic.html#TauCeti.beurlingLp).

## Sources

- [Tau Ceti documentation: `TauCeti.beurlingLp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Beurling/Basic.html#TauCeti.beurlingLp)
- [Source of `TauCeti.beurlingLp` in TauCeti/Analysis/Complex/Wirtinger/Beurling/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Wirtinger/Beurling/Basic.lean#L196)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
