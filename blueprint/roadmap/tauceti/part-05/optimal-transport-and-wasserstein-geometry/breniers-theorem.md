---
declaration: theorem
origin: cited
lean: TauCeti.exists_isKantorovichOptimalTransportMap_gradient
statement: formalized
proof: formalized
---

# Brenier's theorem

Let `μ` and `ν` be probability measures on a finite-dimensional real
inner product space `E`, with `μ` absolutely continuous with respect to an additive Haar measure,
and suppose the optimal cost for `‖x - y‖ ^ 2 / 2` is finite, as it is for laws with finite second
moment (`TauCeti.transportCost_norm_sub_sq_div_two_ne_top`). Then there is a convex, lower
semicontinuous `u : E → EReal` that never takes the value `⊥`, is finite near `μ`-almost every
point and has differentiable real representative there, such that the gradient
`T = ∇ (fun x => (u x).toReal)`:

* is an optimal transport map from `μ` to `ν`, attaining the Kantorovich value;
* induces the unique optimal plan: a plan is optimal exactly when it is the graph plan of `T`;
* is the unique optimal transport map up to `μ`-almost everywhere equality.

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  (hμ : μ.AbsolutelyContinuous ρ)
  (hfin : TauCeti.transportCost (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) μ ν ≠ ⊤) :
  ∃ u,
    Convex ℝ {p | u p.1 ≤ ↑p.2} ∧
      LowerSemicontinuous u ∧
        (∀ (x : E), u x ≠ ⊥) ∧
          (∀ᵐ (x : E) ∂μ,
              (∀ᶠ (x' : E) in nhds x, u x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (u x').toReal) x) ∧
            TauCeti.IsKantorovichOptimalTransportMap (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2))
                μ ν (gradient fun x => (u x).toReal) ∧
              (∀ (π : MeasureTheory.Measure (E × E)),
                  TauCeti.IsOptimalCoupling (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) π μ ν ↔
                    π = TauCeti.graphPlan (gradient fun x => (u x).toReal) μ) ∧
                ∀ (S : E → E),
                  TauCeti.IsKantorovichOptimalTransportMap
                      (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) μ ν S →
                    S =ᵐ[μ] gradient fun x => (u x).toReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isKantorovichOptimalTransportMap_gradient`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient)
- [Source of `TauCeti.exists_isKantorovichOptimalTransportMap_gradient` in TauCeti/MeasureTheory/OptimalTransport/Brenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Brenier.lean#L554)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
