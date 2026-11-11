---
declaration: theorem
origin: cited
lean: Complex.hasSum_deriv_regularizedHGFun
statement: formalized
proof: formalized
---

# Complex.hasSum_deriv_regularizedHGFun

When there are at most as many upper as lower parameters, the derivative of
`regularizedHGFun a b` is the sum of its termwise differentiated power series.

```lean
Complex.hasSum_deriv_regularizedHGFun {a b : Multiset ℂ} (h : a.card ≤ b.card) (z : ℂ) :
  HasSum (fun n => (↑n + 1) * Complex.regularizedHGFunCoeff a b (n + 1) * z ^ n)
    (deriv (Complex.regularizedHGFun a b) z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex.summable_norm_regularizedHGFun](complex-summable-norm-regularizedhgfun.md)

## Lean

Formalized in Tau Ceti as [`Complex.hasSum_deriv_regularizedHGFun`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.html#Complex.hasSum_deriv_regularizedHGFun).

## Sources

- [Tau Ceti documentation: `Complex.hasSum_deriv_regularizedHGFun`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.html#Complex.hasSum_deriv_regularizedHGFun)
- [Source of `Complex.hasSum_deriv_regularizedHGFun` in TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean#L82)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
