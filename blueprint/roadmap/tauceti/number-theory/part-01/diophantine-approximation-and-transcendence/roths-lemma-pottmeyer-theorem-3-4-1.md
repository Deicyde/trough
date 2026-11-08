---
declaration: theorem
origin: cited
lean: TauCeti.weightedIndex_le_of_logHeight_le
statement: formalized
proof: formalized
---

# Roth's lemma (Pottmeyer, Theorem 3.4.1)

Let `P ≠ 0` be a polynomial in `n ≥ 1`
variables over a number field `K`, with partial degrees `deg_{Xᵢ} P ≤ rᵢ` for positive weights
`rᵢ` satisfying `rᵢ₊₁ ≤ σ rᵢ`, where `0 < σ ≤ 1 / 2`. If
`σ⁻¹ (h(P) + 4 n r₀ [K : ℚ]) ≤ rᵢ h(βᵢ)` for every `i`, then the index of `P` at `β` with
weights `r` is at most `2 n σ ^ (1 / 2 ^ (n - 1))`. Heights are relative logarithmic heights.

```lean
TauCeti.weightedIndex_le_of_logHeight_le.{u_1} {K : Type u_1} [Field K] [NumberField K] {n : ℕ}
  [NeZero n] {P : MvPolynomial (Fin n) K} (hP : P ≠ 0) {r : Fin n → ℕ} (hr : ∀ (i : Fin n), 0 < r i)
  (hdeg : ∀ (i : Fin n), MvPolynomial.degreeOf i P ≤ r i) {σ : ℝ} (hσ₀ : 0 < σ) (hσ : σ ≤ 1 / 2)
  (hratio : ∀ (i j : Fin n), ↑j = ↑i + 1 → ↑(r j) ≤ σ * ↑(r i)) (β : Fin n → K)
  (hβ :
    ∀ (i : Fin n),
      σ⁻¹ * (P.logHeight + 4 * ↑n * ↑(r 0) * ↑(Module.finrank ℚ K)) ≤
        ↑(r i) * Height.logHeight₁ (β i)) :
  MvPolynomial.weightedIndex r β P ≤ ENNReal.ofReal (2 * ↑n * σ ^ (1 / 2 ^ (n - 1)))
```

## Depends on

- [MvPolynomial.weightedIndex](mvpolynomial-weightedindex.md)

## Proof depends on

- [Roth's lemma in one variable, index form](../../part-02/height/roths-lemma-in-one-variable-index-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.weightedIndex_le_of_logHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.html#TauCeti.weightedIndex_le_of_logHeight_le).

## Sources

- [Tau Ceti documentation: `TauCeti.weightedIndex_le_of_logHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.html#TauCeti.weightedIndex_le_of_logHeight_le)
- [Source of `TauCeti.weightedIndex_le_of_logHeight_le` in TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.lean#L333)
