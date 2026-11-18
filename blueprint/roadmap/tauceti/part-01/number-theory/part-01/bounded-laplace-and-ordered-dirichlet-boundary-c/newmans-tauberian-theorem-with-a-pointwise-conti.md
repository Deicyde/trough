---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt
statement: formalized
proof: formalized
---

# Newman's Tauberian theorem, with a pointwise continuation hypothesis

Let `f : ℝ → ℂ` be
measurable and bounded on `[0, ∞)`, and let `G` agree with the Laplace transform
`∫ t in Ici 0, f t * exp (-z t)` on the open half-plane `0 < re z` and be analytic at every point
of the imaginary axis `re z = 0`. Then `∫ t in 0..T, f t` converges to `G 0` as `T → ∞`.

Since the Laplace transform is holomorphic on `0 < re z`, this hypothesis on `G` is equivalent to
holomorphy on an open set containing the closed half-plane `0 ≤ re z`, as in
`newmanLaplace_tendsto_integral`.

```lean
TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt {f : ℝ → ℂ} {G : ℂ → ℂ} {M : ℝ}
  (hf : MeasureTheory.AEStronglyMeasurable f (MeasureTheory.volume.restrict (Set.Ici 0)))
  (hbound : ∀ t ∈ Set.Ici 0, ‖f t‖ ≤ M) (hG : ∀ (z : ℂ), z.re = 0 → AnalyticAt ℂ G z)
  (hLaplace : ∀ (z : ℂ), 0 < z.re → G z = ∫ (t : ℝ) in Set.Ici 0, f t * Complex.exp (-z * ↑t)) :
  Filter.Tendsto (fun T => ∫ (t : ℝ) in 0..T, f t) Filter.atTop (nhds (G 0))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newman's Tauberian theorem](newmans-tauberian-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt)
- [Source of `TauCeti.LSeries.newmanLaplace_tendsto_integral_of_analyticAt` in TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean#L199)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
