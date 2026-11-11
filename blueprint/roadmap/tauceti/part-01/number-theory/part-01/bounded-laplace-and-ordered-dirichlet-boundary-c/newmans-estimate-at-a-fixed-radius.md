---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le
statement: formalized
proof: formalized
---

# Newman's estimate at a fixed radius

Let `f` be measurable and bounded by `M` on
`[0, ∞)`, and let `G` be holomorphic on an open set `Ω` containing the closed half-plane
`0 ≤ re z` and equal to the Laplace transform of `f` on `0 < re z`. For every `R > 0` and
`ε > 0`, eventually in `T`, `‖G 0 - ∫ t in 0..T, f t‖ ≤ 2 M / R + ε`.

```lean
TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le {f : ℝ → ℂ} {G : ℂ → ℂ} {M R : ℝ}
  {Ω : Set ℂ}
  (hf : MeasureTheory.AEStronglyMeasurable f (MeasureTheory.volume.restrict (Set.Ici 0)))
  (hbound : ∀ t ∈ Set.Ici 0, ‖f t‖ ≤ M) (hΩ : IsOpen Ω) (hcover : {z | 0 ≤ z.re} ⊆ Ω)
  (hG : DifferentiableOn ℂ G Ω)
  (hLaplace : ∀ (z : ℂ), 0 < z.re → G z = ∫ (t : ℝ) in Set.Ici 0, f t * Complex.exp (-z * ↑t))
  (hR : 0 < R) {ε : ℝ} (hε : 0 < ε) :
  ∀ᶠ (T : ℝ) in Filter.atTop, ‖G 0 - ∫ (t : ℝ) in 0..T, f t‖ ≤ 2 * M / R + ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The detour contribution in Newman's argument vanishes in the limit](the-detour-contribution-in-newmans-argument-vani.md)
- [The detour inside the continuation domain](the-detour-inside-the-continuation-domain.md)
- [Newman's contour identity](newmans-contour-identity.md)
- [Newman's left detour](newmans-left-detour.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le)
- [Source of `TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le` in TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean#L153)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
