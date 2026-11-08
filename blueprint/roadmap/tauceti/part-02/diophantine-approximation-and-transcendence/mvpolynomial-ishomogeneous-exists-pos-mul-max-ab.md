---
declaration: theorem
origin: cited
lean: MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval
statement: formalized
proof: formalized
---

# MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval

**The Thue–Roth inequality for binary forms** (Evertse, Theorem 6.3). Let `F ∈ ℤ[X₀, X₁]` be
a binary form of degree `d` with no squared linear factor over `ℂ`, and let `κ > 2`. Then there
is `c > 0` with `|F(x, y)| ≥ c max(|x|, |y|) ^ (d - κ)` for all integers `x`, `y` with
`F(x, y) ≠ 0`. The proof is ineffective: it gives no value of `c`.

```lean
MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval {F : MvPolynomial (Fin 2) ℤ}
  {d : ℕ} (hF : F.IsHomogeneous d)
  (hsq :
    ∀ (a b : ℂ),
      (a, b) ≠ (0, 0) →
        ¬(MvPolynomial.C a * MvPolynomial.X 0 + MvPolynomial.C b * MvPolynomial.X 1) ^ 2 ∣
            (MvPolynomial.map (Int.castRingHom ℂ)) F)
  {κ : ℝ} (hκ : 2 < κ) :
  ∃ c,
    0 < c ∧
      ∀ (x y : ℤ),
        (MvPolynomial.eval ![x, y]) F ≠ 0 →
          c * max |↑x| |↑y| ^ (↑d - κ) ≤ |↑((MvPolynomial.eval ![x, y]) F)|
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg](isalgebraic-finite-setofpred-abs-sub-le-mulheigh.md)

## Lean

Formalized in Tau Ceti as [`MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval).

## Sources

- [Tau Ceti documentation: `MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval)
- [Source of `MvPolynomial.IsHomogeneous.exists_pos_mul_max_abs_rpow_le_abs_eval` in TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean#L186)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
