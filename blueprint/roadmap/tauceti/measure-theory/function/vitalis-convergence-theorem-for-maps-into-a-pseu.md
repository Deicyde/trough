---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable, TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_uniformIntegrable
statement: formalized
proof: formalized
---

# Vitali's convergence theorem for maps into a pseudometric space

Let `1 ≤ p < ∞`, let
`μ` be a finite measure, and let the almost-everywhere measurable maps `T n, T₀ : X → Y` have
finite `p`-th moment about a point `y₀`. Then `dist (T n x) (T₀ x)` tends to `0` in `Lᵖ(μ)` if
and only if `T n` converges to `T₀` in `μ`-measure and the family `dist (T n ·) y₀` is uniformly
integrable in `Lᵖ(μ)`.

```lean
TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [PseudoMetricSpace Y] [MeasurableSpace X] [MeasurableSpace Y]
  [OpensMeasurableSpace Y] [SecondCountableTopology Y] {μ : MeasureTheory.Measure X} {p : ENNReal}
  [MeasureTheory.IsFiniteMeasure μ] {T : ℕ → X → Y} {T₀ : X → Y} {y₀ : Y} (hp : 1 ≤ p) (hp' : p ≠ ⊤)
  (hT : ∀ (n : ℕ), AEMeasurable (T n) μ) (hT₀ : AEMeasurable T₀ μ)
  (hTp : ∀ (n : ℕ), MeasureTheory.MemLp (fun x => dist (T n x) y₀) p μ)
  (hT₀p : MeasureTheory.MemLp (fun x => dist (T₀ x) y₀) p μ) :
  Filter.Tendsto (fun n => MeasureTheory.eLpNorm (fun x => dist (T n x) (T₀ x)) p μ) Filter.atTop
      (nhds 0) ↔
    MeasureTheory.TendstoInMeasure μ T Filter.atTop T₀ ∧
      MeasureTheory.UnifIntegrable (fun n x => dist (T n x) y₀) p μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/UniformIntegrable.html#TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable).

## Other forms

**Vitali's convergence theorem for maps into a pseudometric space, with `MeasureTheory.UniformIntegrable`.** Formalized in Tau Ceti as [`TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_uniformIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/UniformIntegrable.html#TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_uniformIntegrable).

```lean
TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_uniformIntegrable.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [PseudoMetricSpace Y] [MeasurableSpace X] [MeasurableSpace Y]
  [OpensMeasurableSpace Y] [SecondCountableTopology Y] {μ : MeasureTheory.Measure X} {p : ENNReal}
  [MeasureTheory.IsFiniteMeasure μ] {T : ℕ → X → Y} {T₀ : X → Y} {y₀ : Y} (hp : 1 ≤ p) (hp' : p ≠ ⊤)
  (hT : ∀ (n : ℕ), AEMeasurable (T n) μ) (hT₀ : AEMeasurable T₀ μ)
  (hTp : ∀ (n : ℕ), MeasureTheory.MemLp (fun x => dist (T n x) y₀) p μ)
  (hT₀p : MeasureTheory.MemLp (fun x => dist (T₀ x) y₀) p μ) :
  Filter.Tendsto (fun n => MeasureTheory.eLpNorm (fun x => dist (T n x) (T₀ x)) p μ) Filter.atTop
      (nhds 0) ↔
    MeasureTheory.TendstoInMeasure μ T Filter.atTop T₀ ∧
      MeasureTheory.UniformIntegrable (fun n x => dist (T n x) y₀) p μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/UniformIntegrable.html#TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable)
- [Source of `TauCeti.tendsto_eLpNorm_dist_iff_tendstoInMeasure_and_unifIntegrable` in TauCeti/MeasureTheory/Function/UniformIntegrable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/UniformIntegrable.lean#L166)
