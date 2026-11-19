---
declaration: theorem
origin: cited
lean: TauCeti.exists_isKantorovichOptimalTransportMap_gradient, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_forall_convex_ae_differentiableAt, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_add_one_le, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_le, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_add_one_le, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_null_lipschitz_graphs, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_le, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_forall_convex_ae_differentiableAt, TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_null_lipschitz_graphs, TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate
statement: formalized
proof: formalized
---

# Brenier's theorem

Let `μ` be a probability measure and `ν` a measure on a
finite-dimensional real inner product space `E`, with `μ` absolutely continuous with respect to an
additive Haar measure, and suppose the optimal cost for `‖x - y‖ ^ 2 / 2` is finite, as it is for
laws with finite second moment (`TauCeti.transportCost_norm_sub_sq_div_two_ne_top`); then `ν` is a
probability measure too. Then there is a convex, lower
semicontinuous `u : E → EReal` that never takes the value `⊥`, is finite near `μ`-almost every
point and has differentiable real representative there, such that the gradient
`T = ∇ (fun x => (u x).toReal)`:

* is an optimal transport map from `μ` to `ν`, attaining the Kantorovich value;
* induces the unique optimal plan: a plan is optimal exactly when it is the graph plan of `T`;
* is the unique optimal transport map up to `μ`-almost everywhere equality.

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ ν ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure] [MeasureTheory.IsProbabilityMeasure μ]
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

- [The Fenchel–Young inequality](../../analysis/part-03/convex/the-fenchel-young-inequality.md)
- [Rademacher's theorem for extended-real convex functions](../../analysis/part-03/convex/rademachers-theorem-for-extended-real-convex-fun.md)
- [Rockafellar's differentiability criterion (Rockafellar, *Convex Analysis*, Theorem 25.1)](../../analysis/part-03/convex/rockafellars-differentiability-criterion-rockafe.md)
- [Rockafellar's theorem](../optimal-transport/part-01/rockafellars-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient).

## Other forms

**Brenier's theorem.** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_forall_convex_ae_differentiableAt`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_forall_convex_ae_differentiableAt).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_forall_convex_ae_differentiableAt.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsProbabilityMeasure μ]
  (hμ_diff :
    ∀ (u : E → EReal),
      Convex ℝ {p | u p.1 ≤ ↑p.2} →
        (∀ (x : E), u x ≠ ⊥) →
          ∀ᵐ (x : E) ∂μ,
            u x ≠ ⊤ →
              (∀ᶠ (x' : E) in nhds x, u x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (u x').toReal) x)
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

**Brenier's theorem for `edist ^ 2` out of a source vanishing on Borel sets with `dimH A + 1 ≤ finrank ℝ E`.** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_add_one_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_add_one_le).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_add_one_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ ν : MeasureTheory.Measure E} {π : MeasureTheory.Measure (E × E)}
  [MeasureTheory.IsFiniteMeasure μ]
  (hμ : ∀ (A : Set E), MeasurableSet A → dimH A + 1 ≤ ↑(Module.finrank ℝ E) → μ A = 0)
  (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem for `edist ^ 2` out of a source vanishing on small sets (`dimH A ≤ finrank ℝ E - 1`).** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_le).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_dimH_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ ν : MeasureTheory.Measure E} {π : MeasureTheory.Measure (E × E)}
  [MeasureTheory.IsFiniteMeasure μ]
  (hμ : ∀ (A : Set E), MeasurableSet A → dimH A ≤ ↑(Module.finrank ℝ E - 1) → μ A = 0)
  (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem for sources vanishing on Borel sets with `dimH A + 1 ≤ finrank ℝ E`.** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_add_one_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_add_one_le).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_add_one_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ ν : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ]
  (hμ : ∀ (A : Set E), MeasurableSet A → dimH A + 1 ≤ ↑(Module.finrank ℝ E) → μ A = 0)
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

**Brenier's theorem for sources vanishing on Lipschitz hypersurfaces.** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_null_lipschitz_graphs`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_null_lipschitz_graphs).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_null_lipschitz_graphs.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsProbabilityMeasure μ]
  (hμ :
    ∀ (v : E),
      ‖v‖ = 1 →
        ∀ (K : NNReal) (g : ↥(ℝ ∙ v)ᗮ → ℝ),
          LipschitzWith K g → μ (Set.range fun w => ↑w + g w • v) = 0)
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

**Brenier's theorem for sources vanishing on small sets (`dimH A ≤ finrank ℝ E - 1`).** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_le).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_of_dimH_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ ν : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ]
  (hμ : ∀ (A : Set E), MeasurableSet A → dimH A ≤ ↑(Module.finrank ℝ E - 1) → μ A = 0)
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

**Brenier's theorem for the cost `edist ^ 2`.** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_absolutelyContinuous.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsFiniteMeasure μ] {π : MeasureTheory.Measure (E × E)}
  (hμ : μ.AbsolutelyContinuous ρ) (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem for the cost `edist ^ 2`.** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_forall_convex_ae_differentiableAt`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_forall_convex_ae_differentiableAt).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_forall_convex_ae_differentiableAt.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ ν : MeasureTheory.Measure E}
  {π : MeasureTheory.Measure (E × E)} [MeasureTheory.IsFiniteMeasure μ]
  (hμ_diff :
    ∀ (u : E → EReal),
      Convex ℝ {p | u p.1 ≤ ↑p.2} →
        (∀ (x : E), u x ≠ ⊥) →
          ∀ᵐ (x : E) ∂μ,
            u x ≠ ⊤ →
              (∀ᶠ (x' : E) in nhds x, u x' ≠ ⊤) ∧ DifferentiableAt ℝ (fun x' => (u x').toReal) x)
  (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem for the cost `edist ^ 2` out of a source vanishing on Lipschitz hypersurfaces.** Formalized in Tau Ceti as [`TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_null_lipschitz_graphs`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier/SmallSet.html#TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_null_lipschitz_graphs).

```lean
TauCeti.IsOptimalCoupling.exists_eq_graphPlan_of_null_lipschitz_graphs.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ ν : MeasureTheory.Measure E} {π : MeasureTheory.Measure (E × E)}
  [MeasureTheory.IsFiniteMeasure μ]
  (hμ :
    ∀ (v : E),
      ‖v‖ = 1 →
        ∀ (K : NNReal) (g : ↥(ℝ ∙ v)ᗮ → ℝ),
          LipschitzWith K g → μ (Set.range fun w => ↑w + g w • v) = 0)
  (h : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ 2) π μ ν)
  (hfin : TauCeti.wassersteinEDist 2 μ ν ≠ ⊤) : ∃ T, Measurable T ∧ π = TauCeti.graphPlan T μ
```

**Brenier's theorem with the inverse map.** Formalized in Tau Ceti as [`TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate).

```lean
TauCeti.exists_isKantorovichOptimalTransportMap_gradient_and_gradient_fenchelConjugate.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ ν ρ : MeasureTheory.Measure E} [ρ.IsAddHaarMeasure]
  [MeasureTheory.IsProbabilityMeasure μ] (hμ : μ.AbsolutelyContinuous ρ)
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
- [Source of `TauCeti.exists_isKantorovichOptimalTransportMap_gradient` in TauCeti/MeasureTheory/OptimalTransport/Brenier.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/OptimalTransport/Brenier.lean#L711)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OptimalTransport/STATUS.md)
