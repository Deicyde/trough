---
declaration: theorem
origin: cited
lean: Matrix.abs_sum_sum_mul_inner_le_eight_mul, Matrix.innerProductSup_le_eight_mul, Matrix.norm_sum_sum_mul_inner_le_sixteen_mul
statement: formalized
proof: formalized
---

# Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`

if
`|∑ i, ∑ j, a i j * s i * t j| ≤ C` for all real scalars of absolute value at most one, then
`|∑ i, ∑ j, a i j * ⟪u i, v j⟫| ≤ 8 * C` for all families of vectors of norm at most one in any
real inner product space.

```lean
Matrix.abs_sum_sum_mul_inner_le_eight_mul.{u_1, u_2, u_3} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] {E : Type u_3} [NormedAddCommGroup E] [InnerProductSpace ℝ E] (a : Matrix ι κ ℝ)
  {C : ℝ}
  (h :
    ∀ (s : ι → ℝ) (t : κ → ℝ),
      (∀ (i : ι), |s i| ≤ 1) → (∀ (j : κ), |t j| ≤ 1) → |∑ i, ∑ j, a i j * s i * t j| ≤ C)
  {u : ι → E} {v : κ → E} (hu : ∀ (i : ι), ‖u i‖ ≤ 1) (hv : ∀ (j : κ), ‖v j‖ ≤ 1) :
  |∑ i, ∑ j, a i j * inner ℝ (u i) (v j)| ≤ 8 * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.abs_sum_sum_mul_inner_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.abs_sum_sum_mul_inner_le_eight_mul).

## Other forms

**Grothendieck's inequality in terms of `Γ(a) = Matrix.innerProductSup a`.** Formalized in Tau Ceti as [`Matrix.innerProductSup_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.innerProductSup_le_eight_mul).

```lean
Matrix.innerProductSup_le_eight_mul.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ]
  (a : Matrix ι κ ℝ) {C : ℝ}
  (h :
    ∀ (s : ι → ℝ) (t : κ → ℝ),
      (∀ (i : ι), |s i| ≤ 1) → (∀ (j : κ), |t j| ≤ 1) → |∑ i, ∑ j, a i j * s i * t j| ≤ C) :
  a.innerProductSup ≤ 8 * C
```

**Grothendieck's inequality over an `RCLike` field, with constant `κ_𝕜 = 16`.** Formalized in Tau Ceti as [`Matrix.norm_sum_sum_mul_inner_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.norm_sum_sum_mul_inner_le_sixteen_mul).

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

## Sources

- [Tau Ceti documentation: `Matrix.abs_sum_sum_mul_inner_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Grothendieck.html#Matrix.abs_sum_sum_mul_inner_le_eight_mul)
- [Source of `Matrix.abs_sum_sum_mul_inner_le_eight_mul` in TauCeti/Analysis/Matrix/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/Grothendieck.lean#L165)
