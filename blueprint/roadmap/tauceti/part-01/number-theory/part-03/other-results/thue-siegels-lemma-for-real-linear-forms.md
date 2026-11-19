---
declaration: theorem
origin: cited
lean: TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt, TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_pow_le, TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_one_le, TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_prod_le, TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_prod_lt
statement: formalized
proof: formalized
---

# Thue–Siegel's lemma for real linear forms

**Thue–Siegel's lemma for real linear forms** (Waldschmidt, Lemma 4.11), stated over any
linearly ordered field `K` with a natural floor. If `∑ i, |u i j| ≤ U` for every `j`, `0 < ℓ`, and
`ℓ ^ Fintype.card κ < (X + 1) ^ Fintype.card ι`, then some nonzero `ξ : ι → ℤ` has `|ξ i| ≤ X` for
every `i` and `|∑ i, u i j * ξ i| ≤ U * X / ℓ` for every `j`.

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt.{u_1, u_2, u_3} {ι : Type u_1}
  {κ : Type u_2} {K : Type u_3} [Fintype ι] [Fintype κ] [Field K] [LinearOrder K]
  [IsStrictOrderedRing K] [FloorSemiring K] (u : ι → κ → K) {U : K}
  (hU : ∀ (j : κ), ∑ i, |u i j| ≤ U) {X ℓ : ℕ} (hℓ : 0 < ℓ)
  (hcard : ℓ ^ Fintype.card κ < (X + 1) ^ Fintype.card ι) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |ξ i| ≤ ↑X) ∧ ∀ (j : κ), |∑ i, u i j * ↑(ξ i)| ≤ U * ↑X / ↑ℓ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt).

## Other forms

**Thue–Siegel's lemma for complex linear forms (Waldschmidt, Lemma 4.12).** Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_pow_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_pow_le).

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_pow_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2}
  [Fintype ι] [Nonempty ι] [Fintype κ] (u : ι → κ → ℂ) {U V : ℝ}
  (hU : ∀ (j : κ), ∑ i, ‖u i j‖ ≤ Real.exp U) {X : ℕ} (hX : 0 < X)
  (hcard : (√2 * ↑X * Real.exp (U + V) + 1) ^ (2 * Fintype.card κ) ≤ (↑X + 1) ^ Fintype.card ι) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |ξ i| ≤ ↑X) ∧ ∀ (j : κ), ‖∑ i, u i j * ↑(ξ i)‖ ≤ Real.exp (-V)
```

**Thue–Siegel's lemma for complex linear forms with a real height bound `B ≥ 1`.** Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_one_le).

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_one_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2}
  [Fintype ι] [Nonempty ι] [Fintype κ] (u : ι → κ → ℂ) {A ε : κ → ℝ}
  (hA : ∀ (j : κ), ∑ i, ‖u i j‖ ≤ A j) (hε : ∀ (j : κ), 0 < ε j) {B : ℝ} (hB : 1 ≤ B)
  (hcard : ∏ j, (√2 * B * (A j / ε j) + 1) ^ 2 ≤ B ^ Fintype.card ι) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |↑(ξ i)| ≤ B) ∧ ∀ (j : κ), ‖∑ i, u i j * ↑(ξ i)‖ ≤ ε j
```

**Thue–Siegel's lemma for complex linear forms, with per-form bounds.** Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_prod_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_prod_le).

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_prod_le.{u_1, u_2} {ι : Type u_1}
  {κ : Type u_2} [Fintype ι] [Nonempty ι] [Fintype κ] (u : ι → κ → ℂ) {A ε : κ → ℝ}
  (hA : ∀ (j : κ), ∑ i, ‖u i j‖ ≤ A j) (hε : ∀ (j : κ), 0 < ε j) {X : ℕ} (hX : 0 < X)
  (hcard : ∏ j, (√2 * ↑X * (A j / ε j) + 1) ^ 2 ≤ (↑X + 1) ^ Fintype.card ι) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |ξ i| ≤ ↑X) ∧ ∀ (j : κ), ‖∑ i, u i j * ↑(ξ i)‖ ≤ ε j
```

**Thue–Siegel's lemma for linear forms over an ordered field, with per-form bounds.** Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_prod_lt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_prod_lt).

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_prod_lt.{u_1, u_2, u_3} {ι : Type u_1}
  {κ : Type u_2} {K : Type u_3} [Fintype ι] [Fintype κ] [Field K] [LinearOrder K]
  [IsStrictOrderedRing K] [FloorSemiring K] (u : ι → κ → K) {U : κ → K}
  (hU : ∀ (j : κ), ∑ i, |u i j| ≤ U j) {X : ℕ} {ℓ : κ → ℕ} (hℓ : ∀ (j : κ), 0 < ℓ j)
  (hcard : ∏ j, ℓ j < (X + 1) ^ Fintype.card ι) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |ξ i| ≤ ↑X) ∧ ∀ (j : κ), |∑ i, u i j * ↑(ξ i)| ≤ U j * ↑X / ↑(ℓ j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt)
- [Source of `TauCeti.ThueSiegel.exists_ne_zero_int_vec_abs_le_of_pow_lt` in TauCeti/NumberTheory/ThueSiegel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ThueSiegel.lean#L135)
