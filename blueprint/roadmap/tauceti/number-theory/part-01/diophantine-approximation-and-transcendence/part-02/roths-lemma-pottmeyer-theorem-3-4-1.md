---
declaration: theorem
origin: cited
lean: TauCeti.weightedIndex_le_of_logHeight_le, MvPolynomial.weightedIndex_toMvPolynomial_le, Polynomial.rootMultiplicity_mul_logHeight₁_le
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

- [MvPolynomial.weightedIndex](../part-01/mvpolynomial-weightedindex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.weightedIndex_le_of_logHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.html#TauCeti.weightedIndex_le_of_logHeight_le).

## Other forms

**Roth's lemma in one variable, index form.** Formalized in Tau Ceti as [`MvPolynomial.weightedIndex_toMvPolynomial_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.html#MvPolynomial.weightedIndex_toMvPolynomial_le).

```lean
MvPolynomial.weightedIndex_toMvPolynomial_le.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {σ : Type u_2} (r : σ → ℕ) (a : σ → K) (i : σ) {P : Polynomial K} (hP : P ≠ 0)
  (hr : P.natDegree ≤ r i) {s : ℝ} (hs : 0 < s)
  (h :
    s⁻¹ * (P.logHeight + ↑(Module.finrank ℚ K) * ↑(r i) * Real.log 2) ≤
      ↑(r i) * Height.logHeight₁ (a i)) :
  MvPolynomial.weightedIndex r a ((Polynomial.toMvPolynomial i) P) ≤ ENNReal.ofReal s
```

**Roth's lemma in one variable, multiplicity form.** Formalized in Tau Ceti as [`Polynomial.rootMultiplicity_mul_logHeight₁_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.html#Polynomial.rootMultiplicity_mul_logHeight%E2%82%81_le).

```lean
Polynomial.rootMultiplicity_mul_logHeight₁_le.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (P : Polynomial K) (β : K) :
  ↑(Polynomial.rootMultiplicity β P) * Height.logHeight₁ β ≤
    P.logHeight + ↑(Module.finrank ℚ K) * ↑P.natDegree * Real.log 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.weightedIndex_le_of_logHeight_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.html#TauCeti.weightedIndex_le_of_logHeight_le)
- [Source of `TauCeti.weightedIndex_le_of_logHeight_le` in TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/IndexEstimate.lean#L333)
