---
declaration: theorem
origin: cited
lean: Complex.summable_norm_regularizedHGFun
statement: formalized
proof: formalized
---

# Complex.summable_norm_regularizedHGFun

When there are at most as many upper as lower parameters, the regularized hypergeometric
series converges absolutely at every `z`.

```lean
Complex.summable_norm_regularizedHGFun {a b : Multiset ℂ} (h : a.card ≤ b.card) (z : ℂ) :
  Summable fun n => ‖Complex.regularizedHGFunCoeff a b n * z ^ n‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.summable_norm_regularizedHGFun`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.html#Complex.summable_norm_regularizedHGFun).

## Sources

- [Tau Ceti documentation: `Complex.summable_norm_regularizedHGFun`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.html#Complex.summable_norm_regularizedHGFun)
- [Source of `Complex.summable_norm_regularizedHGFun` in TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean#L74)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
