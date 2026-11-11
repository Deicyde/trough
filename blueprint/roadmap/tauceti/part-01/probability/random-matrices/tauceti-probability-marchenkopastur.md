---
declaration: def
origin: cited
lean: TauCeti.Probability.marchenkoPastur
statement: formalized
---

# TauCeti.Probability.marchenkoPastur

The Marchenko–Pastur law of aspect ratio `y`: an atom at `0` plus `x⁻¹` times the semicircle
law with centre `1 + y` and variance `y`. The atom weight is written `(y - 1) / y`; for `y > 0` its
positive part is the atom mass `(1 - 1/y)₊`, which vanishes for `y ≤ 1`. At `y = 0` the weight is
`0` under Lean's convention `1 / 0 = 0`, so there is no atom and the law is `δ₁`.

```lean
TauCeti.Probability.marchenkoPastur (y : NNReal) : MeasureTheory.Measure ℝ
```

## Depends on

- [TauCeti.Probability.semicircleReal](tauceti-probability-semicirclereal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.marchenkoPastur`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/Basic.html#TauCeti.Probability.marchenkoPastur).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.marchenkoPastur`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/Basic.html#TauCeti.Probability.marchenkoPastur)
- [Source of `TauCeti.Probability.marchenkoPastur` in TauCeti/Probability/Distributions/MarchenkoPastur/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/MarchenkoPastur/Basic.lean#L66)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
