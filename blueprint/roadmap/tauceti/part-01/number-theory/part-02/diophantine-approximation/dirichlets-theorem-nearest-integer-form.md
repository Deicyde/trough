---
declaration: theorem
origin: cited
lean: Real.infinite_setOf_mul_abs_mul_sub_round_le_one, Matrix.exists_int_abs_sum_mul_sub_le, TauCeti.dirichlet_linearForm_infinite, TauCeti.infinite_linearFormApproximations_of_lt_card, Matrix.dirichlet_linearForms, Matrix.dirichlet_linearForms_infinite, TauCeti.infinite_simultaneousApproximationDenominators_inv_card
statement: formalized
proof: formalized
---

# Dirichlet's theorem, nearest-integer form

For every real `α`, infinitely many natural
numbers `q ≥ 1` satisfy `q ‖q α‖ ≤ 1`.

```lean
Real.infinite_setOf_mul_abs_mul_sub_round_le_one (α : ℝ) :
  {q | 0 < q ∧ ↑q * |↑q * α - ↑(round (↑q * α))| ≤ 1}.Infinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Minkowski's convex body theorem for the integer lattice](../../../measure-theory/group/minkowskis-convex-body-theorem-for-the-integer-l.md)

## Lean

Formalized in Tau Ceti as [`Real.infinite_setOf_mul_abs_mul_sub_round_le_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Real.infinite_setOf_mul_abs_mul_sub_round_le_one).

## Other forms

**Dirichlet's theorem for linear forms, with general bounds.** Formalized in Tau Ceti as [`Matrix.exists_int_abs_sum_mul_sub_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.exists_int_abs_sum_mul_sub_le).

```lean
Matrix.exists_int_abs_sum_mul_sub_le.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] [Nonempty κ] (A : Matrix ι κ ℝ) {P δ : ℝ} (hP : 0 ≤ P) (hδ₀ : 0 ≤ δ) (hδ₁ : δ < 1)
  (h : 1 ≤ P ^ Fintype.card κ * δ ^ Fintype.card ι) :
  ∃ y x, y ≠ 0 ∧ (∀ (j : κ), |↑(y j)| ≤ P) ∧ ∀ (i : ι), |∑ j, A i j * ↑(y j) - ↑(x i)| ≤ δ
```

**Dirichlet's theorem for one linear form, infinitely many solutions.** Formalized in Tau Ceti as [`TauCeti.dirichlet_linearForm_infinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#TauCeti.dirichlet_linearForm_infinite).

```lean
TauCeti.dirichlet_linearForm_infinite.{u_2} {κ : Type u_2} [Fintype κ] [Nonempty κ] (α : κ → ℝ)
  (hα : ∀ (y : κ → ℤ), (∃ k, ∑ j, α j * ↑(y j) = ↑k) → y = 0) :
  {p | p.2 ≠ 0 ∧ |∑ j, α j * ↑(p.2 j) - ↑p.1| ≤ ‖p.2‖ ^ (-↑(Fintype.card κ))}.Infinite
```

**Dirichlet's theorem for one linear form, infinitely many solutions.** Formalized in Tau Ceti as [`TauCeti.infinite_linearFormApproximations_of_lt_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.html#TauCeti.infinite_linearFormApproximations_of_lt_card).

```lean
TauCeti.infinite_linearFormApproximations_of_lt_card.{u_1} {ι : Type u_1} [Fintype ι] [Nonempty ι]
  {θ : ι → ℝ} (hθ : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * θ i = 0 → x = 0) {w : ℝ}
  (hw : w < ↑(Fintype.card ι)) : (TauCeti.linearFormApproximations θ w).Infinite
```

**Dirichlet's theorem for systems of linear forms.** Formalized in Tau Ceti as [`Matrix.dirichlet_linearForms`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.dirichlet_linearForms).

```lean
Matrix.dirichlet_linearForms.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι] [Fintype κ]
  [Nonempty ι] [Nonempty κ] (A : Matrix ι κ ℝ) {Q : ℝ} (hQ : 1 < Q) :
  ∃ y x,
    y ≠ 0 ∧
      (∀ (j : κ), |↑(y j)| ≤ Q) ∧
        ∀ (i : ι), |∑ j, A i j * ↑(y j) - ↑(x i)| ≤ Q ^ (-↑(Fintype.card κ) / ↑(Fintype.card ι))
```

**Dirichlet's theorem for systems of linear forms, infinitely many solutions.** Formalized in Tau Ceti as [`Matrix.dirichlet_linearForms_infinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Matrix.dirichlet_linearForms_infinite).

```lean
Matrix.dirichlet_linearForms_infinite.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] [Nonempty κ] (A : Matrix ι κ ℝ)
  (hA : ∀ (y : κ → ℤ), (∀ (i : ι), ∃ k, ∑ j, A i j * ↑(y j) = ↑k) → y = 0) :
  {p |
      p.1 ≠ 0 ∧
        ∀ (i : ι),
          |∑ j, A i j * ↑(p.1 j) - ↑(p.2 i)| ≤
            ‖p.1‖ ^ (-↑(Fintype.card κ) / ↑(Fintype.card ι))}.Infinite
```

**Dirichlet's theorem, infinitely many denominators.** Formalized in Tau Ceti as [`TauCeti.infinite_simultaneousApproximationDenominators_inv_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/SimultaneousExponent.html#TauCeti.infinite_simultaneousApproximationDenominators_inv_card).

```lean
TauCeti.infinite_simultaneousApproximationDenominators_inv_card.{u_1} {ι : Type u_1} [Fintype ι]
  (θ : ι → ℝ) : (TauCeti.simultaneousApproximationDenominators θ (↑(Fintype.card ι))⁻¹).Infinite
```

## Sources

- [Tau Ceti documentation: `Real.infinite_setOf_mul_abs_mul_sub_round_le_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.html#Real.infinite_setOf_mul_abs_mul_sub_round_le_one)
- [Source of `Real.infinite_setOf_mul_abs_mul_sub_round_le_one` in TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Dirichlet.lean#L228)
