---
declaration: def
origin: cited
lean: TauCeti.inverseRegularizedGamma
statement: formalized
---

# TauCeti.inverseRegularizedGamma

The inverse `P⁻¹(s, u)` of the regularized lower incomplete gamma function in its argument.

For positive `s` this is the quantile of the Gamma law with shape `s` and rate `1`. For
nonpositive `s` it is `0`; the quantile itself supplies the value `0` outside `0 < u < 1`.

```lean
TauCeti.inverseRegularizedGamma (s u : ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.inverseRegularizedGamma`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gamma/Quantile.html#TauCeti.inverseRegularizedGamma).

## Sources

- [Tau Ceti documentation: `TauCeti.inverseRegularizedGamma`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gamma/Quantile.html#TauCeti.inverseRegularizedGamma)
- [Source of `TauCeti.inverseRegularizedGamma` in TauCeti/Probability/Distributions/Gamma/Quantile.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/Gamma/Quantile.lean#L61)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
