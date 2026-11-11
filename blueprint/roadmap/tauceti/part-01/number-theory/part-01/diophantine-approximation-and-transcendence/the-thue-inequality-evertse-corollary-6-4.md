---
declaration: theorem
origin: cited
lean: MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots, MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le
statement: formalized
proof: formalized
---

# The Thue inequality (Evertse, Corollary 6.4)

Let `F ∈ ℤ[X₀, X₁]` be a binary form such
that `F(X, 1)` has at least three distinct complex zeros. Then for every bound `B`, the
inequality `0 < |F(x, y)| ≤ B` has only finitely many integer solutions. Like Roth's theorem,
the proof is ineffective.

```lean
MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots
  {F : MvPolynomial (Fin 2) ℤ} {d : ℕ} (hF : F.IsHomogeneous d)
  (hroots :
    3 ≤
      (Polynomial.map (Int.castRingHom ℂ)
              ((MvPolynomial.aeval ![Polynomial.X, 1]) F)).roots.toFinset.card)
  (B : ℤ) :
  {p | (MvPolynomial.eval ![p.1, p.2]) F ≠ 0 ∧ |(MvPolynomial.eval ![p.1, p.2]) F| ≤ B}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Thue–Roth inequality for binary forms (Evertse, Theorem 6.3)](the-thue-roth-inequality-for-binary-forms-everts.md)

## Lean

Formalized in Tau Ceti as [`MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots).

## Other forms

**The Thue inequality for square-free binary forms (Evertse, Corollary 6.4, square-free case).** Formalized in Tau Ceti as [`MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le).

```lean
MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le {F : MvPolynomial (Fin 2) ℤ} {d : ℕ}
  (hF : F.IsHomogeneous d)
  (hsq :
    ∀ (a b : ℂ),
      (a, b) ≠ (0, 0) →
        ¬(MvPolynomial.C a * MvPolynomial.X 0 + MvPolynomial.C b * MvPolynomial.X 1) ^ 2 ∣
            (MvPolynomial.map (Int.castRingHom ℂ)) F)
  (hd : 3 ≤ d) (B : ℤ) :
  {p | (MvPolynomial.eval ![p.1, p.2]) F ≠ 0 ∧ |(MvPolynomial.eval ![p.1, p.2]) F| ≤ B}.Finite
```

## Sources

- [Tau Ceti documentation: `MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots)
- [Source of `MvPolynomial.IsHomogeneous.finite_setOf_eval_ne_zero_and_abs_le_of_three_le_card_roots` in TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean#L269)
