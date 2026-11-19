---
declaration: def
origin: cited
lean: Complex.eulerIntegral
statement: formalized
---

# Complex.eulerIntegral

Euler's integral, normalized to represent the regularized Gauss function in
its convergence region `0 < b.re < c.re`, with `1 - z ∈ Complex.slitPlane`.
Outside that region this is only the totalized integral, not an analytic continuation.

```lean
Complex.eulerIntegral (a b c z : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.eulerIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.eulerIntegral).

## Sources

- [Tau Ceti documentation: `Complex.eulerIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.eulerIntegral)
- [Source of `Complex.eulerIntegral` in TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean#L43)
- [Tau Ceti roadmap status: The Gauss hypergeometric function](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsHypergeometric/STATUS.md)
