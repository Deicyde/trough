---
declaration: theorem
origin: cited
lean: TauCeti.norm_snd_add_I_smul_snd_le
statement: formalized
proof: formalized
---

# The normal Cauchy–Riemann inequality

Let `A` be an endomorphism of `ℂ × N` within `ε` of
multiplication by `i`. If the derivative `D` of a disc `(a, b)` satisfies the Cauchy–Riemann
equation `D 1 + A (D i) = 0` for `A`, its normal component satisfies
`‖∂ₛb + i ∂ₜb‖ ≤ ε ‖∂ₜ(a, b)‖`. With the structure read in the adapted chart of
`TauCeti.exists_holomorphicAdaptedChart_norm_pullbackEnd_sub_le` at a point `(a, b)` of the disc
near `(a₀, 0)`, that theorem gives `ε = C ‖b‖`, hence `‖∂ₛb + i ∂ₜb‖ ≤ C ‖b‖ ‖∂ₜ(a, b)‖` there.

```lean
TauCeti.norm_snd_add_I_smul_snd_le.{u_2} {N : Type u_2} [NormedAddCommGroup N] [NormedSpace ℂ N]
  {A : ℂ × N →L[ℝ] ℂ × N} {ε : ℝ} (hA : ‖A - Complex.I • ContinuousLinearMap.id ℝ (ℂ × N)‖ ≤ ε)
  {D : ℂ →L[ℝ] ℂ × N} (hCR : D 1 + A (D Complex.I) = 0) :
  ‖(D 1).2 + Complex.I • (D Complex.I).2‖ ≤ ε * ‖D Complex.I‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_snd_add_I_smul_snd_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/AdaptedChart.html#TauCeti.norm_snd_add_I_smul_snd_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_snd_add_I_smul_snd_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/AdaptedChart.html#TauCeti.norm_snd_add_I_smul_snd_le)
- [Source of `TauCeti.norm_snd_add_I_smul_snd_le` in TauCeti/Geometry/Symplectic/JHolomorphic/AdaptedChart.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/JHolomorphic/AdaptedChart.lean#L334)
