---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.exists_energyDensity_le_mul_exp
statement: formalized
proof: formalized
---

# Exponential decay of the energy density of a plane vortex

A vortex on the whole plane
whose section satisfies `|α| → 1` at infinity has energy density
`|F_a|² + |d_a α|² + (1 - |α|²)²` bounded by `K exp (-c |z|)` for every rate `c < 1`.

```lean
TauCeti.Vortex.exists_energyDensity_le_mul_exp {x : ℂ → EuclideanSpace ℝ (Fin 4)}
  (hb₁ : Differentiable ℝ fun w => (x w).ofLp 0) (hb₂ : Differentiable ℝ fun w => (x w).ofLp 1)
  (hp : ContDiff ℝ 2 fun w => (x w).ofLp 2) (hq : ContDiff ℝ 2 fun w => (x w).ofLp 3)
  (hsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  (hlim :
    Filter.Tendsto (fun z => 4 * ((x z).ofLp 2 ^ 2 + (x z).ofLp 3 ^ 2)) (Filter.cocompact ℂ)
      (nhds 1))
  {c : ℝ} (hc : c < 1) :
  ∃ K, ∀ (z : ℂ), TauCeti.Vortex.energyDensity x z ≤ K * Real.exp (-(c * ‖z‖))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.exists_energyDensity_le_mul_exp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/DerivativeDecay.html#TauCeti.Vortex.exists_energyDensity_le_mul_exp).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.exists_energyDensity_le_mul_exp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/DerivativeDecay.html#TauCeti.Vortex.exists_energyDensity_le_mul_exp)
- [Source of `TauCeti.Vortex.exists_energyDensity_le_mul_exp` in TauCeti/Analysis/PDE/Vortex/DerivativeDecay.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/DerivativeDecay.lean#L310)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
