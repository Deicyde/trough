---
declaration: theorem
origin: cited
lean: TauCeti.exists_isKantorovichOptimalTransportMap_gradient, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate
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

## Proof depends on

- [The Fenchel–Young inequality](../../analysis/part-02/convex/the-fenchel-young-inequality.md)
- [Rademacher's theorem for extended-real convex functions](../../analysis/part-02/convex/rademachers-theorem-for-extended-real-convex-fun.md)
- [Rockafellar's theorem](../optimal-transport/part-01/rockafellars-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient).

## Other forms

**Brenier's theorem for the cost `edist ^ 2`.** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsFiniteMeasure μ] {π : MeasureTheory.Measure (E × E)}
  (hμ : μ.AbsolutelyContinuous ρ) (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem with the inverse map.** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure]
  {μ ν : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] (hμ : μ.AbsolutelyContinuous ρ)
  (hν : ν.AbsolutelyContinuous ρ)
  (hfin : TauCeti.transportCost (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) μ ν ≠ ⊤) :
  ∃ u,
    Convex ℝ {p | u p.1 ≤ ↑p.2} ∧
      LowerSemicontinuous u ∧
        (∀ (x : E), u x ≠ ⊥) ∧
          (∀ᵐ (x : E) ∂μ,
              (∀ᶠ (x' : E) in nhds x, u x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (u x').toReal) x) ∧
            (∀ᵐ (y : E) ∂ν,
                (∀ᶠ (y' : E) in nhds y, TauCeti.fenchelConjugate (innerₗ E) u y' ≠ ⊤) ∧
                  DifferentiableAt ℝ (fun y' => (TauCeti.fenchelConjugate (innerₗ E) u y').toReal)
                    y) ∧
              TauCeti.IsKantorovichOptimalTransportMap
                  (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) μ ν
                  (gradient fun x => (u x).toReal) ∧
                TauCeti.IsKantorovichOptimalTransportMap
                    (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) ν μ
                    (gradient fun y => (TauCeti.fenchelConjugate (innerₗ E) u y).toReal) ∧
                  ((gradient fun y => (TauCeti.fenchelConjugate (innerₗ E) u y).toReal) ∘
                        gradient fun x => (u x).toReal) =ᵐ[μ]
                      id ∧
                    ((gradient fun x => (u x).toReal) ∘
                        gradient fun y => (TauCeti.fenchelConjugate (innerₗ E) u y).toReal) =ᵐ[ν]
                      id
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isKantorovichOptimalTransportMap_gradient`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient)
- [Source of `TauCeti.exists_isKantorovichOptimalTransportMap_gradient` in TauCeti/MeasureTheory/OptimalTransport/Brenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Brenier.lean#L554)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
