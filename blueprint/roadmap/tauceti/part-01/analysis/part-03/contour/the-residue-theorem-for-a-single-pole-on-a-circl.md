---
declaration: theorem
origin: cited
lean: TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg, TauCeti.Contour.circleIntegral_eq_residue
statement: formalized
proof: formalized
---

# The residue theorem for a single pole on a circle

If `f` is meromorphic on the closed
disc of radius `R` about `c` and has nonnegative meromorphic order at every point of the closed
disc other than a point `z₀` of the open disc, then `∮_{|z - c| = R} f dz = 2πi · Res_{z₀} f`.

```lean
TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg {f : ℂ → ℂ} {c z₀ : ℂ}
  {R : ℝ} (hz₀ : z₀ ∈ Metric.ball c R) (hf : MeromorphicOn f (Metric.closedBall c R))
  (hord : ∀ z ∈ Metric.closedBall c R, z ≠ z₀ → 0 ≤ meromorphicOrderAt f z) :
  circleIntegral f c R = 2 * ↑Real.pi * Complex.I * TauCeti.Contour.residue f z₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg).

## Other forms

**The residue theorem for a single pole on a circle, holomorphic form.** Formalized in Tau Ceti as [`TauCeti.Contour.circleIntegral_eq_residue`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.circleIntegral_eq_residue).

```lean
TauCeti.Contour.circleIntegral_eq_residue {f : ℂ → ℂ} {c z₀ : ℂ} {R : ℝ}
  (hz₀ : z₀ ∈ Metric.ball c R) (hf : MeromorphicAt f z₀)
  (hfa : ∀ z ∈ Metric.closedBall c R, z ≠ z₀ → AnalyticAt ℂ f z) :
  circleIntegral f c R = 2 * ↑Real.pi * Complex.I * TauCeti.Contour.residue f z₀
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg)
- [Source of `TauCeti.Contour.circleIntegral_eq_residue_of_meromorphicOrderAt_nonneg` in TauCeti/Analysis/Contour/Residue/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/Residue/Theorem.lean#L361)
