---
declaration: def
origin: cited
lean: TauCeti.outerNormal
statement: formalized
---

# TauCeti.outerNormal

The **measure-theoretic outer normal** `ν_s x` of `s` in `Ω`: minus the limit, as `r → 0⁺`,
of the averages of the polar density of `Dχ_s` over `closedBall x r` against `|Dχ_s|`. At points
of the reduced boundary it is a unit vector (`TauCeti.norm_outerNormal`), and
`Dχ_s = -ν_s |Dχ_s|`
(`TauCeti.integral_trace_fderiv_mul_indicator_eq_integral_inner_outerNormal`). Elsewhere its
value carries no meaning.

```lean
TauCeti.outerNormal.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E)
  (Ω : TopologicalSpace.Opens E) (s : Set E) (x : E) : E
```

## Depends on

- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.outerNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.outerNormal).

## Sources

- [Tau Ceti documentation: `TauCeti.outerNormal`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/ReducedBoundary.html#TauCeti.outerNormal)
- [Source of `TauCeti.outerNormal` in TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/ReducedBoundary.lean#L101)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
