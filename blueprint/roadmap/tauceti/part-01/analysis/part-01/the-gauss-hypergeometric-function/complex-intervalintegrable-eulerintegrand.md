---
declaration: theorem
origin: cited
lean: Complex.intervalIntegrable_eulerIntegrand
statement: formalized
proof: formalized
---

# Complex.intervalIntegrable_eulerIntegrand

Euler's integrand is interval integrable throughout its classical parameter
region, for every argument off the cut `[1, ∞)`.

```lean
Complex.intervalIntegrable_eulerIntegrand (a : ℂ) {b c z : ℂ} (hb : 0 < b.re) (hcb : b.re < c.re)
  (hz : 1 - z ∈ Complex.slitPlane) :
  IntervalIntegrable (fun t => ↑t ^ (b - 1) * (1 - ↑t) ^ (c - b - 1) * (1 - z * ↑t) ^ (-a))
    MeasureTheory.volume 0 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Complex.intervalIntegrable_eulerIntegrand`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.intervalIntegrable_eulerIntegrand).

## Sources

- [Tau Ceti documentation: `Complex.intervalIntegrable_eulerIntegrand`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.html#Complex.intervalIntegrable_eulerIntegrand)
- [Source of `Complex.intervalIntegrable_eulerIntegrand` in TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Hypergeometric/EulerIntegral.lean#L65)
- [Tau Ceti roadmap status: The Gauss hypergeometric function](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsHypergeometric/STATUS.md)
