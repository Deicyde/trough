---
declaration: theorem
origin: cited
lean: TauCeti.IsOptimalCoupling.abs_integral_inner_le
statement: formalized
proof: formalized
---

# Cauchy–Schwarz for the pairing

For an optimal coupling `γ` of two laws `μ` and `ν` of
`P₂(E)` for the quadratic cost and `ξ ∈ L²(μ; E)`, `|∫ ⟪ξ x, y - x⟫ dγ| ≤ ‖ξ‖ W₂(μ, ν)`.

```lean
TauCeti.IsOptimalCoupling.abs_integral_inner_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [MeasurableSpace E] [BorelSpace E] [SecondCountableTopology E] [InnerProductSpace ℝ E]
  {γ : MeasureTheory.Measure (E × E)} [CompleteSpace E] {μ ν : TauCeti.WassersteinSpace 2 E}
  (hγ : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) γ ↑↑μ ↑↑ν)
  (ξ : ↥(MeasureTheory.Lp E 2 ↑↑μ)) :
  |∫ (z : E × E), inner ℝ (↑↑ξ z.1) (z.2 - z.1) ∂γ| ≤ ‖ξ‖ * dist μ ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.abs_integral_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/EulerLagrange.html#TauCeti.IsOptimalCoupling.abs_integral_inner_le).

## Sources

- [Tau Ceti documentation: `TauCeti.IsOptimalCoupling.abs_integral_inner_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/EulerLagrange.html#TauCeti.IsOptimalCoupling.abs_integral_inner_le)
- [Source of `TauCeti.IsOptimalCoupling.abs_integral_inner_le` in TauCeti/MeasureTheory/OptimalTransport/Wasserstein/EulerLagrange.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Wasserstein/EulerLagrange.lean#L223)
