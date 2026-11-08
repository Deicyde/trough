---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.newmanLaplace_tendsto_integral, TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt
statement: formalized
proof: formalized
---

# Newman's Tauberian theorem

Let `f : ℝ → ℂ` be measurable and bounded on `[0, ∞)`, and
let `G` be holomorphic on an open set `Ω` containing the closed half-plane `0 ≤ re z`, agreeing
with the Laplace transform `∫ t in Ici 0, f t * exp (-z t)` on the open half-plane `0 < re z`.
Then `∫ t in 0..T, f t` converges to `G 0` as `T → ∞`.

```lean
TauCeti.LSeries.newmanLaplace_tendsto_integral {f : ℝ → ℂ} {G : ℂ → ℂ} {M : ℝ} {Ω : Set ℂ}
  (hf : MeasureTheory.AEStronglyMeasurable f (MeasureTheory.volume.restrict (Set.Ici 0)))
  (hbound : ∀ t ∈ Set.Ici 0, ‖f t‖ ≤ M) (hΩ : IsOpen Ω) (hcover : {z | 0 ≤ z.re} ⊆ Ω)
  (hG : DifferentiableOn ℂ G Ω)
  (hLaplace : ∀ (z : ℂ), 0 < z.re → G z = ∫ (t : ℝ) in Set.Ici 0, f t * Complex.exp (-z * ↑t)) :
  Filter.Tendsto (fun T => ∫ (t : ℝ) in 0..T, f t) Filter.atTop (nhds (G 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Holomorphy of the Laplace transform](holomorphy-of-the-laplace-transform.md)
- [Newman's estimate at a fixed radius](newmans-estimate-at-a-fixed-radius.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.newmanLaplace_tendsto_integral`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.newmanLaplace_tendsto_integral).

## Other forms

**Newman's Tauberian theorem, with a pointwise continuation hypothesis.** Formalized in Tau Ceti as [`TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt).

```lean
TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt {f : ℝ → ℂ} {G : ℂ → ℂ} {M : ℝ}
  (hf : MeasureTheory.AEStronglyMeasurable f (MeasureTheory.volume.restrict (Set.Ici 0)))
  (hbound : ∀ t ∈ Set.Ici 0, ‖f t‖ ≤ M) (hG : ∀ (z : ℂ), z.re = 0 → AnalyticAt ℂ G z)
  (hLaplace : ∀ (z : ℂ), 0 < z.re → G z = ∫ (t : ℝ) in Set.Ici 0, f t * Complex.exp (-z * ↑t)) :
  Filter.Tendsto (fun T => ∫ (t : ℝ) in 0..T, f t) Filter.atTop (nhds (G 0))
```

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.newmanLaplace_tendsto_integral`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.newmanLaplace_tendsto_integral)
- [Source of `TauCeti.LSeries.newmanLaplace_tendsto_integral` in TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean#L179)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
