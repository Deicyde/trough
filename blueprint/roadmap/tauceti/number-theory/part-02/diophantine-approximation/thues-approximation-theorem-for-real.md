---
declaration: theorem
origin: cited
lean: TauCeti.thue_approximation_real, TauCeti.thue_approximation
statement: formalized
proof: formalized
---

# Thue's approximation theorem for real `α`

Let `α` be a real algebraic number of degree
`d ≥ 2` and let `κ > d / 2 + 1`. Then only finitely many rationals `ξ` satisfy
`|ξ - α| ≤ H(ξ) ^ (-κ)`. This is a variant of Evertse, Theorem 6.9, rather than that statement
verbatim: every degree `d ≥ 2` is allowed.

```lean
TauCeti.thue_approximation_real {α : ℝ} (hd : 2 ≤ (minpoly ℚ α).natDegree) {κ : ℝ}
  (hκ : ↑(minpoly ℚ α).natDegree / 2 + 1 < κ) : {ξ | |↑ξ - α| ≤ Height.mulHeight₁ ξ ^ (-κ)}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Thue's gap principle (Evertse, Theorem 6.14)](thues-gap-principle-evertse-theorem-6-14.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.thue_approximation_real`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.html#TauCeti.thue_approximation_real).

## Other forms

**Thue's approximation theorem, for complex `α`.** Formalized in Tau Ceti as [`TauCeti.thue_approximation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.html#TauCeti.thue_approximation).

```lean
TauCeti.thue_approximation {α : ℂ} (hd : 2 ≤ (minpoly ℚ α).natDegree) {κ : ℝ}
  (hκ : ↑(minpoly ℚ α).natDegree / 2 + 1 < κ) : {ξ | ‖↑ξ - α‖ ≤ Height.mulHeight₁ ξ ^ (-κ)}.Finite
```

## Sources

- [Tau Ceti documentation: `TauCeti.thue_approximation_real`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.html#TauCeti.thue_approximation_real)
- [Source of `TauCeti.thue_approximation_real` in TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Thue/GapPrinciple.lean#L249)
