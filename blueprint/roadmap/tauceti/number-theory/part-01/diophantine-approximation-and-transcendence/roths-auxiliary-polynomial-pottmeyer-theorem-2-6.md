---
declaration: theorem
origin: cited
lean: TauCeti.exists_roth_auxiliary_polynomial
statement: formalized
proof: formalized
---

# Roth's auxiliary polynomial (Pottmeyer, Theorem 2.6.5)

Let `α` be an algebraic number
of degree `d` in a field of characteristic zero, and let `b ≥ 1` be an integer such that `b α` is
integral over `ℤ`. Let `ε ≥ 0` and let `ι` be a finite set of `n` variables with
`2 d ≤ exp (ε² n / 2)`. For all positive integers `rᵢ`, `i ∈ ι`, there is a nonzero
`P ∈ ℤ[Xᵢ : i ∈ ι]` with `deg_{Xᵢ} P ≤ rᵢ`, whose index at `(α, …, α)` with weights `r` is at
least `(n / 2) (1 - ε)`, and whose coefficients have absolute value at most
`(12 b max(1, ⌈α⌉)) ^ (∑ᵢ rᵢ)`, where `⌈α⌉` is the house of `α`.

```lean
TauCeti.exists_roth_auxiliary_polynomial.{u_2, u_3} {ι : Type u_2} [Fintype ι] {F : Type u_3}
  [Field F] [CharZero F] {α : F} {b : ℕ} (hb : 0 < b) (hbα : IsIntegral ℤ (↑b * α)) {ε : ℝ}
  (hε : 0 ≤ ε) (hn : 2 * ↑(minpoly ℚ α).natDegree ≤ Real.exp (ε ^ 2 * ↑(Fintype.card ι) / 2))
  {r : ι → ℕ} (hr : ∀ (i : ι), r i ≠ 0) :
  ∃ P,
    P ≠ 0 ∧
      (∀ (i : ι), MvPolynomial.degreeOf i P ≤ r i) ∧
        ENNReal.ofReal (↑(Fintype.card ι) / 2 * (1 - ε)) ≤
            MvPolynomial.weightedIndex r (fun x => α) ((MvPolynomial.map (Int.castRingHom F)) P) ∧
          ∀ (m : ι →₀ ℕ), |↑(P.coeff m)| ≤ (12 * ↑b * max 1 (TauCeti.house α)) ^ ∑ i, r i
```

## Depends on

- [MvPolynomial.weightedIndex](mvpolynomial-weightedindex.md)

## Proof depends on

- [Hoeffding's lemma on the grid `{0, 1 / r, …, 1}`](../../../combinatorics/other-results/hoeffdings-lemma-on-the-grid-0-1-r-1.md)
- [Siegel's lemma over a number field, with rational integer unknowns (Evertse, Theorem 3.20)](../../part-02/number-field/siegels-lemma-over-a-number-field-with-rational.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_roth_auxiliary_polynomial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Auxiliary.html#TauCeti.exists_roth_auxiliary_polynomial).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_roth_auxiliary_polynomial`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Auxiliary.html#TauCeti.exists_roth_auxiliary_polynomial)
- [Source of `TauCeti.exists_roth_auxiliary_polynomial` in TauCeti/NumberTheory/DiophantineApproximation/Roth/Auxiliary.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/Auxiliary.lean#L213)
