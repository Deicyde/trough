---
declaration: theorem
origin: cited
lean: TauCeti.isLeast_lintegral_isContinuityEquation, TauCeti.wassersteinEDist_rpow_eq_sInf_lintegral_isContinuityEquation, TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le, TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le
statement: formalized
proof: formalized
---

# The Benamou–Brenier formula

For `1 ≤ p < ∞` and probability measures `μ₀`, `μ₁` on a
finite-dimensional real normed space at finite Wasserstein distance, `W_p (μ₀, μ₁) ^ p` is the
least `p`-action `∫₀¹ ∫ ‖vₜ‖ ^ p dνₜ dt` of a curve `t ↦ νₜ` of finite measures, narrowly
continuous on `[0, 1]` and joining `μ₀` to `μ₁`, solving the continuity equation with velocity `v`
on `(0, 1)`. The minimum is attained by the displacement interpolation of an optimal coupling.

```lean
TauCeti.isLeast_lintegral_isContinuityEquation.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [FiniteDimensional ℝ E] [BorelSpace E]
  {μ₀ μ₁ : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ₀]
  [MeasureTheory.IsProbabilityMeasure μ₁] {p : ENNReal} (hp : 1 ≤ p) (hp_top : p ≠ ⊤)
  (hfin : TauCeti.wassersteinEDist p μ₀ μ₁ ≠ ⊤) :
  IsLeast
    {A |
      ∃ ν v,
        TauCeti.IsContinuityEquation (fun t => ↑(ν t)) v 0 1 ∧
          ContinuousOn ν (Set.Icc 0 1) ∧
            ↑(ν 0) = μ₀ ∧
              ↑(ν 1) = μ₁ ∧ ∫⁻ (t : ℝ) in Set.Ioo 0 1, ∫⁻ (x : E), ‖v t x‖ₑ ^ p.toReal ∂↑(ν t) = A}
    (TauCeti.wassersteinEDist p μ₀ μ₁ ^ p.toReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../analysis/part-02/sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The Hopf–Lax subsolution inequality](../../analysis/part-02/pde/part-01/the-hopf-lax-subsolution-inequality.md)
- [Jensen's inequality for the conditional expectation, as an inequality of `lintegral`s](../function/jensens-inequality-for-the-conditional-expectati.md)
- [The theorem of Rockafellar and Rüschendorf](../optimal-transport/the-theorem-of-rockafellar-and-ruschendorf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLeast_lintegral_isContinuityEquation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.isLeast_lintegral_isContinuityEquation).

## Other forms

**The Benamou–Brenier formula, as an infimum.** Formalized in Tau Ceti as [`TauCeti.wassersteinEDist_rpow_eq_sInf_lintegral_isContinuityEquation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.wassersteinEDist_rpow_eq_sInf_lintegral_isContinuityEquation).

```lean
TauCeti.wassersteinEDist_rpow_eq_sInf_lintegral_isContinuityEquation.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E] [FiniteDimensional ℝ E]
  [BorelSpace E] {μ₀ μ₁ : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure μ₀]
  [MeasureTheory.IsProbabilityMeasure μ₁] {p : ENNReal} (hp : 1 ≤ p) (hp_top : p ≠ ⊤) :
  TauCeti.wassersteinEDist p μ₀ μ₁ ^ p.toReal =
    sInf
      {A |
        ∃ ν v,
          TauCeti.IsContinuityEquation (fun t => ↑(ν t)) v 0 1 ∧
            ContinuousOn ν (Set.Icc 0 1) ∧
              ↑(ν 0) = μ₀ ∧
                ↑(ν 1) = μ₁ ∧
                  ∫⁻ (t : ℝ) in Set.Ioo 0 1, ∫⁻ (x : E), ‖v t x‖ₑ ^ p.toReal ∂↑(ν t) = A}
```

**The Benamou–Brenier lower bound.** Formalized in Tau Ceti as [`TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le).

```lean
TauCeti.IsContinuityEquation.wassersteinEDist_rpow_le.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [MeasurableSpace E] [FiniteDimensional ℝ E] [BorelSpace E]
  {ν : ℝ → MeasureTheory.FiniteMeasure E} {v : ℝ → E → E} {a b : ℝ}
  (h : TauCeti.IsContinuityEquation (fun t => ↑(ν t)) v a b) (hν : ContinuousOn ν (Set.Icc a b))
  (hab : a ≤ b) [MeasureTheory.IsProbabilityMeasure ↑(ν a)] {p : ENNReal} (hp : 1 ≤ p)
  (hp_top : p ≠ ⊤) :
  TauCeti.wassersteinEDist p ↑(ν a) ↑(ν b) ^ p.toReal ≤
    ENNReal.ofReal ((b - a) ^ (p.toReal - 1)) *
      ∫⁻ (t : ℝ) in Set.Ioo a b, ∫⁻ (x : E), ‖v t x‖ₑ ^ p.toReal ∂↑(ν t)
```

**The Benamou–Brenier upper bound.** Formalized in Tau Ceti as [`TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/PlanInterpolation.html#TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le).

```lean
TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [MeasurableSpace E]
  [FiniteDimensional ℝ E] [BorelSpace E] {μ ν : MeasureTheory.Measure E}
  [MeasureTheory.IsFiniteMeasure μ] {π : MeasureTheory.Measure (E × E)} {p : ENNReal} (hp : 1 ≤ p)
  (hp_top : p ≠ ⊤) (hopt : TauCeti.IsOptimalCoupling (fun z => edist z.1 z.2 ^ p.toReal) π μ ν)
  (hfin : TauCeti.wassersteinEDist p μ ν ≠ ⊤) :
  ∃ v,
    TauCeti.IsContinuityEquation
        (fun t => MeasureTheory.Measure.map (fun z => (1 - t) • z.1 + t • z.2) π) v 0 1 ∧
      ∫⁻ (t : ℝ) in Set.Ioo 0 1,
          ∫⁻ (w : E),
            ‖v t w‖ₑ ^ p.toReal ∂MeasureTheory.Measure.map (fun z => (1 - t) • z.1 + t • z.2) π ≤
        TauCeti.wassersteinEDist p μ ν ^ p.toReal
```

## Sources

- [Tau Ceti documentation: `TauCeti.isLeast_lintegral_isContinuityEquation`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.html#TauCeti.isLeast_lintegral_isContinuityEquation)
- [Source of `TauCeti.isLeast_lintegral_isContinuityEquation` in TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/BenamouBrenier.lean#L208)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OptimalTransport/STATUS.md)
