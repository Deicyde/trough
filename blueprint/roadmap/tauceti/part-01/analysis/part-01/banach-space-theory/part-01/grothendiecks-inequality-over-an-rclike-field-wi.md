---
declaration: theorem
origin: cited
lean: Matrix.norm_sum_sum_mul_inner_le_sixteen_mul
statement: formalized
proof: formalized
---

# Grothendieck's inequality over an `RCLike` field, with constant `κ_𝕜 = 16`

if
`‖∑ i, ∑ j, a i j * s i * t j‖ ≤ C` for all scalars of norm at most one, then
`‖∑ i, ∑ j, a i j * ⟪u i, v j⟫‖ ≤ 16 * C` for all families of vectors of norm at most one in any
inner product space over `𝕜`. Over `ℝ`, `Matrix.abs_sum_sum_mul_inner_le_eight_mul` gives the
constant `8`.

```lean
Matrix.norm_sum_sum_mul_inner_le_sixteen_mul.{u_1, u_2, u_3, u_4} {ι : Type u_1} {κ : Type u_2}
  [Fintype ι] [Fintype κ] {𝕜 : Type u_3} [RCLike 𝕜] {E : Type u_4} [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] (a : Matrix ι κ 𝕜) {C : ℝ}
  (h :
    ∀ (s : ι → 𝕜) (t : κ → 𝕜),
      (∀ (i : ι), ‖s i‖ ≤ 1) → (∀ (j : κ), ‖t j‖ ≤ 1) → ‖∑ i, ∑ j, a i j * s i * t j‖ ≤ C)
  {u : ι → E} {v : κ → E} (hu : ∀ (i : ι), ‖u i‖ ≤ 1) (hv : ∀ (j : κ), ‖v j‖ ≤ 1) :
  ‖∑ i, ∑ j, a i j * inner 𝕜 (u i) (v j)‖ ≤ 16 * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`](grothendiecks-inequality-over-the-reals-with-con.md)

## Lean

Formalized in Tau Ceti as [`Matrix.norm_sum_sum_mul_inner_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.norm_sum_sum_mul_inner_le_sixteen_mul).

## Sources

- [Tau Ceti documentation: `Matrix.norm_sum_sum_mul_inner_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.norm_sum_sum_mul_inner_le_sixteen_mul)
- [Source of `Matrix.norm_sum_sum_mul_inner_le_sixteen_mul` in TauCeti/Analysis/Matrix/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/Grothendieck.lean#L206)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
