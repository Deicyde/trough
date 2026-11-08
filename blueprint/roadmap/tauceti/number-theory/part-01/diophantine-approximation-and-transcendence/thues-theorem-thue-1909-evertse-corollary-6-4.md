---
declaration: theorem
origin: cited
lean: MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots, MvPolynomial.IsHomogeneous.finite_setOf_eval_eq
statement: formalized
proof: formalized
---

# Thue's theorem (Thue 1909; Evertse, Corollary 6.4)

Let `F ∈ ℤ[X₀, X₁]` be a binary form
such that `F(X, 1)` has at least three distinct complex zeros, and let `m ≠ 0`. Then the Thue
equation `F(x, y) = m` has only finitely many integer solutions. Like Roth's theorem, the proof
is ineffective.

```lean
MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots {F : MvPolynomial (Fin 2) ℤ}
  {d : ℕ} (hF : F.IsHomogeneous d)
  (hroots :
    3 ≤
      (Polynomial.map (Int.castRingHom ℂ)
              ((MvPolynomial.aeval ![Polynomial.X, 1]) F)).roots.toFinset.card)
  {m : ℤ} (hm : m ≠ 0) : {p | (MvPolynomial.eval ![p.1, p.2]) F = m}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Thue inequality (Evertse, Corollary 6.4)](the-thue-inequality-evertse-corollary-6-4.md)

## Lean

Formalized in Tau Ceti as [`MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots).

## Other forms

**Thue's theorem for square-free binary forms (Evertse, Corollary 6.4, square-free case).** Formalized in Tau Ceti as [`MvPolynomial.IsHomogeneous.finite_setOf_eval_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_eq).

```lean
MvPolynomial.IsHomogeneous.finite_setOf_eval_eq {F : MvPolynomial (Fin 2) ℤ} {d : ℕ}
  (hF : F.IsHomogeneous d)
  (hsq :
    ∀ (a b : ℂ),
      (a, b) ≠ (0, 0) →
        ¬(MvPolynomial.C a * MvPolynomial.X 0 + MvPolynomial.C b * MvPolynomial.X 1) ^ 2 ∣
            (MvPolynomial.map (Int.castRingHom ℂ)) F)
  (hd : 3 ≤ d) {m : ℤ} (hm : m ≠ 0) : {p | (MvPolynomial.eval ![p.1, p.2]) F = m}.Finite
```

## Sources

- [Tau Ceti documentation: `MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.html#MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots)
- [Source of `MvPolynomial.IsHomogeneous.finite_setOf_eval_eq_of_three_le_card_roots` in TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/BinaryForm.lean#L319)
