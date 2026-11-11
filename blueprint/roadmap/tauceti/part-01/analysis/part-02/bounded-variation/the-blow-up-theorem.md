---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter
statement: formalized
proof: formalized
---

# The blow-up theorem

Let `E` have dimension `n ≥ 2`, let `μ` be an additive Haar measure,
and let `x` be a point of the reduced boundary of `s` in `Ω`, with outer normal `ν = ν_s x`. As
`r → 0⁺`, the blow-ups `(fun y => x + r • y) ⁻¹' s` converge locally in measure to the half-space
`{y | ⟪y, ν⟫ < 0}`: for every compact set `K`,

`μ((s_{x,r} ∆ {y | ⟪y, ν⟫ < 0}) ∩ K) → 0`.

```lean
TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} {Ω : TopologicalSpace.Opens E} {s : Set E} {x : E}
  [μ.IsAddHaarMeasure] (hn : 2 ≤ Module.finrank ℝ E) (hx : x ∈ TauCeti.reducedBoundary μ Ω s)
  {K : Set E} (hK : IsCompact K) :
  Filter.Tendsto
    (fun r =>
      μ
        (symmDiff ((fun y => x + r • y) ⁻¹' s) {y | inner ℝ y (TauCeti.outerNormal μ Ω s x) < 0} ∩
          K))
    (nhdsWithin 0 (Set.Ioi 0)) (nhds 0)
```

## Depends on

- [TauCeti.outerNormal](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-outernormal.md)
- [TauCeti.reducedBoundary](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-reducedboundary.md)

## Proof depends on

- [The Fréchet--Kolmogorov criterion for a family vanishing almost everywhere off a fixed bounded set](../../../measure-theory/function/part-01/the-frechet-kolmogorov-criterion-for-a-family-va.md)
- [The Gauss–Green formula, `Dχ_s = -ν_s |Dχ_s|`](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/the-gauss-green-formula-d-s-s-d-s.md)
- [Lebesgue's density theorem](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/lebesgues-density-theorem.md)
- [Lebesgue's differentiation theorem](../../../measure-theory/other-results/lebesgues-differentiation-theorem.md)
- [The polar decomposition `Du = σ_u |Du|`](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/the-polar-decomposition-du-u-du.md)
- [The Sobolev inequality for functions of bounded variation](the-sobolev-inequality-for-functions-of-bounded.md)
- [TauCeti.variationMeasure](../../part-01/geometric-measure-theory-rectifiability-bv-and-f/tauceti-variationmeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/BlowUp.html#TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter`](https://taucetiproject.org/docs/TauCeti/Analysis/BoundedVariation/BlowUp.html#TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter)
- [Source of `TauCeti.tendsto_measure_preimage_add_smul_symmDiff_setOf_inner_lt_inter` in TauCeti/Analysis/BoundedVariation/BlowUp.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/BoundedVariation/BlowUp.lean#L621)
