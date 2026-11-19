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

- [Newman's contour identity](newmans-contour-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le)
- [Source of `TauCeti.LSeries.eventually_norm_sub_intervalIntegral_le` in TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean#L153)
