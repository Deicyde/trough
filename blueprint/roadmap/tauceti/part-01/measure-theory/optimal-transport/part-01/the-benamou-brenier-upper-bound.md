---
declaration: theorem
origin: cited
lean: TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le
statement: formalized
proof: formalized
---

# The Benamou–Brenier upper bound

Let `1 ≤ p < ∞`, and let `π` be an optimal coupling of a
finite measure `μ` and a measure `ν` on `E` for the cost `d(x, y) ^ p`, at finite Wasserstein
distance `W_p (μ, ν)`. Then the displacement interpolation, the laws `μₜ` of
`(1 - t) • x + t • y` under `π`, solves the continuity equation on `(0, 1)` with a velocity field
of `p`-action at most `W_p (μ, ν) ^ p`: `∫₀¹ ∫ ‖vₜ‖ ^ p dμₜ dt ≤ W_p (μ, ν) ^ p`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jensen's inequality for the conditional expectation, as an inequality of `lintegral`s](../../function/part-01/jensens-inequality-for-the-conditional-expectati.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/PlanInterpolation.html#TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/PlanInterpolation.html#TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le)
- [Source of `TauCeti.exists_isContinuityEquation_map_smul_fst_add_smul_snd_of_isOptimalCoupling_le` in TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/PlanInterpolation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/ContinuityEquation/PlanInterpolation.lean#L209)
