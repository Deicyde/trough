---
declaration: theorem
origin: cited
lean: Complex.eulerIntegral_zero
statement: formalized
proof: formalized
---

# Complex.eulerIntegral_zero

At zero argument the normalized Euler integral is the reciprocal Gamma factor.

```lean
Complex.eulerIntegral_zero (a : ℂ) {b c : ℂ} (hb : 0 < b.re) (hcb : b.re < c.re) :
  a.eulerIntegral b c 0 = (Complex.Gamma c)⁻¹
```

## Depends on

- [Complex.eulerIntegral](complex-eulerintegral.md)

## Lean

Formalized in Tau Ceti as [`Complex.eulerIntegral_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.eulerIntegral_zero).

## Sources

- [Tau Ceti documentation: `Complex.eulerIntegral_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.eulerIntegral_zero)
- [Source of `Complex.eulerIntegral_zero` in TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean#L129)
- [Tau Ceti roadmap status: The Gauss hypergeometric function](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsHypergeometric/STATUS.md)
