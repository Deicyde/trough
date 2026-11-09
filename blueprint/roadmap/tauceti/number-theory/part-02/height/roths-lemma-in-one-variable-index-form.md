---
declaration: theorem
origin: cited
lean: MvPolynomial.weightedIndex_toMvPolynomial_le, Polynomial.rootMultiplicity_mul_logHeight₁_le
statement: formalized
proof: formalized
---

# Roth's lemma in one variable, index form

Let `P ≠ 0` be placed in the coordinate `i`,
with `deg P ≤ r i`. If `r i * h(a i) ≥ s⁻¹ * (h(P) + [K : ℚ] * r i * log 2)` for some `s > 0`,
then the index of `P` at `a` with weights `r` is at most `s`. Heights are relative. Replacing
`log 2` by a larger constant, such as Pottmeyer's `4`, only strengthens the hypothesis.

```lean
MvPolynomial.weightedIndex_toMvPolynomial_le.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {σ : Type u_2} (r : σ → ℕ) (a : σ → K) (i : σ) {P : Polynomial K} (hP : P ≠ 0)
  (hr : P.natDegree ≤ r i) {s : ℝ} (hs : 0 < s)
  (h :
    s⁻¹ * (P.logHeight + ↑(Module.finrank ℚ K) * ↑(r i) * Real.log 2) ≤
      ↑(r i) * Height.logHeight₁ (a i)) :
  MvPolynomial.weightedIndex r a ((Polynomial.toMvPolynomial i) P) ≤ ENNReal.ofReal s
```

## Depends on

- [MvPolynomial.weightedIndex](../../part-01/diophantine-approximation-and-transcendence/mvpolynomial-weightedindex.md)

## Lean

Formalized in Tau Ceti as [`MvPolynomial.weightedIndex_toMvPolynomial_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.html#MvPolynomial.weightedIndex_toMvPolynomial_le).

## Other forms

**Roth's lemma in one variable, multiplicity form.** Formalized in Tau Ceti as [`Polynomial.rootMultiplicity_mul_logHeight₁_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.html#Polynomial.rootMultiplicity_mul_logHeight%E2%82%81_le).

```lean
Polynomial.rootMultiplicity_mul_logHeight₁_le.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (P : Polynomial K) (β : K) :
  ↑(Polynomial.rootMultiplicity β P) * Height.logHeight₁ β ≤
    P.logHeight + ↑(Module.finrank ℚ K) * ↑P.natDegree * Real.log 2
```

## Sources

- [Tau Ceti documentation: `MvPolynomial.weightedIndex_toMvPolynomial_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.html#MvPolynomial.weightedIndex_toMvPolynomial_le)
- [Source of `MvPolynomial.weightedIndex_toMvPolynomial_le` in TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Polynomial/RootMultiplicity.lean#L83)
