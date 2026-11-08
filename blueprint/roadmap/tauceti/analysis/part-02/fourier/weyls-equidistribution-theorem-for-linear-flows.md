---
declaration: theorem
origin: cited
lean: TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral
statement: formalized
proof: formalized
---

# Weyl's equidistribution theorem for linear flows

If the velocity `ν` is nonresonant, that
is `⟪k, ν⟫ ≠ 0` for every nonzero `k ∈ ℤ^d`, then along every line `t ↦ θ + t ν` of the unit
torus the time averages `T⁻¹ ∫₀ᵀ f (θ + t ν) dt` of a continuous function `f` tend to its space
average `∫ f`.

```lean
TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral.{u_1} {d : Type u_1} [Fintype d] {ν : d → ℝ}
  (hν : ∀ (k : d → ℤ), ∑ i, ↑(k i) * ν i = 0 → k = 0) (θ : d → ℝ) (f : C(UnitAddTorus d, ℂ)) :
  Filter.Tendsto (fun T => T⁻¹ • ∫ (t : ℝ) in 0..T, f fun i => ↑(θ i + ν i * t)) Filter.atTop
    (nhds (∫ (x : UnitAddTorus d), f x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Kronecker.html#TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Kronecker.html#TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral)
- [Source of `TauCeti.UnitAddTorus.tendsto_inv_smul_intervalIntegral` in TauCeti/Analysis/Fourier/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/Kronecker.lean#L144)
