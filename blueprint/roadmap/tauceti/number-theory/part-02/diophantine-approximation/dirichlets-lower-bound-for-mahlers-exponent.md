---
declaration: theorem
origin: cited
lean: TauCeti.natCast_le_mahlerExponent, TauCeti.card_le_linearFormExponent, TauCeti.inv_card_le_simultaneousExponent
statement: formalized
proof: formalized
---

# Dirichlet's lower bound for Mahler's exponent

If `ξ` is not algebraic of degree at
most `n`, then `w_n(ξ) ≥ n`.

```lean
TauCeti.natCast_le_mahlerExponent {n : ℕ} {ξ : ℝ}
  (hξ : ¬(IsAlgebraic ℚ ξ ∧ (minpoly ℚ ξ).natDegree ≤ n)) : ↑n ≤ TauCeti.mahlerExponent n ξ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dirichlet's theorem, nearest-integer form](dirichlets-theorem-nearest-integer-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCast_le_mahlerExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.html#TauCeti.natCast_le_mahlerExponent).

## Other forms

**Dirichlet's lower bound for the linear-form exponent.** Formalized in Tau Ceti as [`TauCeti.card_le_linearFormExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.html#TauCeti.card_le_linearFormExponent).

```lean
TauCeti.card_le_linearFormExponent.{u_1} {ι : Type u_1} [Fintype ι] {θ : ι → ℝ}
  (hθ : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * θ i = 0 → x = 0) :
  ↑(Fintype.card ι) ≤ TauCeti.linearFormExponent θ
```

**Dirichlet's lower bound for the simultaneous exponent.** Formalized in Tau Ceti as [`TauCeti.inv_card_le_simultaneousExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/SimultaneousExponent.html#TauCeti.inv_card_le_simultaneousExponent).

```lean
TauCeti.inv_card_le_simultaneousExponent.{u_1} {ι : Type u_1} [Fintype ι] (θ : ι → ℝ) :
  (↑(Fintype.card ι))⁻¹ ≤ TauCeti.simultaneousExponent θ
```

## Sources

- [Tau Ceti documentation: `TauCeti.natCast_le_mahlerExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.html#TauCeti.natCast_le_mahlerExponent)
- [Source of `TauCeti.natCast_le_mahlerExponent` in TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/LinearFormExponent.lean#L679)
