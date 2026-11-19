---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall
statement: formalized
proof: formalized
---

# The perimeter measure has density one with respect to `Hⁿ⁻¹` at the reduced boundary

Let
`F` have dimension `n ≥ 2`, with Lebesgue measure. At every point `x` of the reduced boundary of
`s` in `Ω`,

`|Dχ_s|(closedBall x r) / (ω_{n-1} r ^ (n - 1)) → 1`     as `r → 0⁺`,

where `ω_{n-1} r ^ (n - 1)` is the volume of a closed ball of radius `r` in `ℝ^(n-1)`, the
normalization of `μHE[n - 1]`.

```lean
TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall.{u_2} {F : Type u_2}
  [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F] [MeasurableSpace F]
  [BorelSpace F] {Ω : TopologicalSpace.Opens F} {s : Set F} {x : F} (hn : 2 ≤ Module.finrank ℝ F)
  (hx : x ∈ TauCeti.reducedBoundary MeasureTheory.volume Ω s) :
  Filter.Tendsto
    (fun r =>
      (TauCeti.variationMeasure MeasureTheory.volume Ω (s.indicator 1))
          (Subtype.val ⁻¹' Metric.closedBall x r) /
        MeasureTheory.volume (Metric.closedBall 0 r))
    (nhdsWithin 0 (Set.Ioi 0)) (nhds 1)
```

## Depends on

- [TauCeti.reducedBoundary](tauceti-reducedboundary.md)
- [TauCeti.variationMeasure](tauceti-variationmeasure.md)

## Proof depends on

- [The blow-up theorem](the-blow-up-theorem.md)
- [The divergence theorem on a half-space (`TauCeti.setIntegral_setOf_inner_lt_trace_fderiv`)](../../../measure-theory/integral/part-01/the-divergence-theorem-on-a-half-space-tauceti-s.md)
- [The Gauss–Green formula, `Dχ_s = -ν_s |Dχ_s|`](the-gauss-green-formula-d-s-s-d-s.md)
- [Lebesgue's differentiation theorem](../../../measure-theory/other-results/lebesgues-differentiation-theorem.md)
- [The polar decomposition `Du = σ_u |Du|`](the-polar-decomposition-du-u-du.md)
- [TauCeti.outerNormal](tauceti-outernormal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/BlowUp.html#TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/BlowUp.html#TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall)
- [Source of `TauCeti.tendsto_variationMeasure_closedBall_div_volume_closedBall` in TauCeti/Analysis/BoundedVariation/BlowUp.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/BoundedVariation/BlowUp.lean#L960)
- [Tau Ceti roadmap status: Geometric measure theory: rectifiability, BV, and finite perimeter](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricMeasureTheory/STATUS.md)
