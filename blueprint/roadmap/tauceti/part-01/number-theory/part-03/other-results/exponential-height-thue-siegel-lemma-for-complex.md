---
declaration: theorem
origin: cited
lean: TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le
statement: formalized
proof: formalized
---

# Exponential-height Thue–Siegel lemma for complex linear forms

For nonempty `ι` and
`0 ≤ N`, if `∑ i, ‖u i j‖ ≤ exp U` for every `j` and
`(√2 * exp (N + U + V) + 1) ^ (2 * Fintype.card κ) ≤ exp (N * Fintype.card ι)`, then some nonzero
`ξ : ι → ℤ` satisfies `|(ξ i : ℝ)| ≤ exp N` for every `i` and
`‖∑ i, u i j * ξ i‖ ≤ exp (-V)` for every `j`.

```lean
TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2}
  [Fintype ι] [Nonempty ι] [Fintype κ] (u : ι → κ → ℂ) {N U V : ℝ} (hN : 0 ≤ N)
  (hU : ∀ (j : κ), ∑ i, ‖u i j‖ ≤ Real.exp U)
  (hcard :
    (√2 * Real.exp (N + U + V) + 1) ^ (2 * Fintype.card κ) ≤ Real.exp (N * ↑(Fintype.card ι))) :
  ∃ ξ, ξ ≠ 0 ∧ (∀ (i : ι), |↑(ξ i)| ≤ Real.exp N) ∧ ∀ (j : κ), ‖∑ i, u i j * ↑(ξ i)‖ ≤ Real.exp (-V)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Thue–Siegel's lemma for real linear forms](thue-siegels-lemma-for-real-linear-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le).

## Sources

- [Tau Ceti documentation: `TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ThueSiegel.html#TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le)
- [Source of `TauCeti.ThueSiegel.exists_ne_zero_int_vec_norm_le_of_exp_le` in TauCeti/NumberTheory/ThueSiegel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ThueSiegel.lean#L250)
