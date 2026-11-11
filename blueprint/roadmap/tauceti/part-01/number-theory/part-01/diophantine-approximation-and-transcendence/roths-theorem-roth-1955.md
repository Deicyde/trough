---
declaration: theorem
origin: cited
lean: IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg, IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_abs_sub, IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_norm_sub, IsAlgebraic.not_liouvilleWith, IsAlgebraic.exists_pos_mul_max_abs_rpow_le_norm_sub_mul
statement: formalized
proof: formalized
---

# Roth's theorem (Roth, 1955)

If `α` is a real algebraic number and `κ > 2`, then only
finitely many rational numbers `ξ` satisfy `|ξ - α| ≤ H(ξ) ^ (-κ)`, where `H` is the
multiplicative height on `ℚ`.

```lean
IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg {α : ℝ} (hα : IsAlgebraic ℚ α) {κ : ℝ}
  (hκ : 2 < κ) : {ξ | |↑ξ - α| ≤ Height.mulHeight₁ ξ ^ (-κ)}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Roth's auxiliary polynomial (Pottmeyer, Theorem 2.6.5)](roths-auxiliary-polynomial-pottmeyer-theorem-2-6.md)
- [Roth's lemma (Pottmeyer, Theorem 3.4.1)](roths-lemma-pottmeyer-theorem-3-4-1.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight%E2%82%81_rpow_neg).

## Other forms

**Roth's theorem as a lower bound (Evertse, Theorem 6.2).** Formalized in Tau Ceti as [`IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_abs_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.exists_pos_mul_mulHeight%E2%82%81_rpow_neg_le_abs_sub).

```lean
IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_abs_sub {α : ℝ} (hα : IsAlgebraic ℚ α) {κ : ℝ}
  (hκ : 2 < κ) : ∃ c, 0 < c ∧ ∀ (ξ : ℚ), ↑ξ ≠ α → c * Height.mulHeight₁ ξ ^ (-κ) ≤ |↑ξ - α|
```

**Roth's theorem.** Formalized in Tau Ceti as [`IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_norm_sub`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.exists_pos_mul_mulHeight%E2%82%81_rpow_neg_le_norm_sub).

```lean
IsAlgebraic.exists_pos_mul_mulHeight₁_rpow_neg_le_norm_sub {α : ℂ} (hα : IsAlgebraic ℚ α) {κ : ℝ}
  (hκ : 2 < κ) : ∃ c, 0 < c ∧ ∀ (ξ : ℚ), ↑ξ ≠ α → c * Height.mulHeight₁ ξ ^ (-κ) ≤ ‖↑ξ - α‖
```

**Roth's theorem in terms of Liouville exponents.** Formalized in Tau Ceti as [`IsAlgebraic.not_liouvilleWith`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.not_liouvilleWith).

```lean
IsAlgebraic.not_liouvilleWith {α : ℝ} (hα : IsAlgebraic ℚ α) {p : ℝ} (hp : 2 < p) :
  ¬LiouvilleWith p α
```

**Roth's theorem for a linear form.** Formalized in Tau Ceti as [`IsAlgebraic.exists_pos_mul_max_abs_rpow_le_norm_sub_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#IsAlgebraic.exists_pos_mul_max_abs_rpow_le_norm_sub_mul).

```lean
IsAlgebraic.exists_pos_mul_max_abs_rpow_le_norm_sub_mul {α : ℂ} (hα : IsAlgebraic ℚ α) {κ : ℝ}
  (hκ : 2 < κ) :
  ∃ c, 0 < c ∧ ∀ (x y : ℤ), ↑x - α * ↑y ≠ 0 → c * max |↑x| |↑y| ^ (1 - κ) ≤ ‖↑x - α * ↑y‖
```

## Sources

- [Tau Ceti documentation: `IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight%E2%82%81_rpow_neg)
- [Source of `IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg` in TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean#L160)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
