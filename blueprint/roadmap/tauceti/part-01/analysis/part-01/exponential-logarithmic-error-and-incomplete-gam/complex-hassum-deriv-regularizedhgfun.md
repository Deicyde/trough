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
- [Source of `Complex.hasSum_deriv_regularizedHGFun` in TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/RegularizedHypergeometric.lean#L82)
- [Tau Ceti roadmap status: Exponential, logarithmic, error and incomplete Gamma functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsEiLiErfIncompleteGamma/STATUS.md)
