---
declaration: theorem
origin: cited
lean: Complex.analyticOnNhd_eulerIntegral
statement: formalized
proof: formalized
---

# Complex.analyticOnNhd_eulerIntegral

Euler's normalized integral is jointly holomorphic in `(a, z)` for fixed
`0 < b.re < c.re`, on the principal cut plane in `z`.

```lean
Complex.analyticOnNhd_eulerIntegral {b c : ℂ} (hb : 0 < b.re) (hbc : b.re < c.re) :
  AnalyticOnNhd ℂ (fun p => p.1.eulerIntegral b c p.2) {p | 1 - p.2 ∈ Complex.slitPlane}
```

## Depends on

- [Complex.eulerIntegral](complex-eulerintegral.md)

## Proof depends on

- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`Complex.analyticOnNhd_eulerIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.analyticOnNhd_eulerIntegral).

## Sources

- [Tau Ceti documentation: `Complex.analyticOnNhd_eulerIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.analyticOnNhd_eulerIntegral)
- [Source of `Complex.analyticOnNhd_eulerIntegral` in TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean#L111)
- [Tau Ceti roadmap status: The Gauss hypergeometric function](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsHypergeometric/STATUS.md)
