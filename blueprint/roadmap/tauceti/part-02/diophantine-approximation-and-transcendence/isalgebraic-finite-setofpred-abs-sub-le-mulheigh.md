---
declaration: theorem
origin: cited
lean: IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg
statement: formalized
proof: formalized
---

# IsAlgebraic.finite\_setOfPred\_abs\_sub\_le\_mulHeight₁\_rpow\_neg

**Roth's theorem** (Roth, 1955). If `α` is a real algebraic number and `κ > 2`, then only
finitely many rational numbers `ξ` satisfy `|ξ - α| ≤ H(ξ) ^ (-κ)`, where `H` is the
multiplicative height on `ℚ`.

```lean
IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg {α : ℝ} (hα : IsAlgebraic ℚ α) {κ : ℝ}
  (hκ : 2 < κ) : {ξ | |↑ξ - α| ≤ Height.mulHeight₁ ξ ^ (-κ)}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [MvPolynomial.weightedIndex](mvpolynomial-weightedindex.md)

## Lean

Formalized in Tau Ceti as [`IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight%E2%82%81_rpow_neg).

## Sources

- [Tau Ceti documentation: `IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.html#IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight%E2%82%81_rpow_neg)
- [Source of `IsAlgebraic.finite_setOfPred_abs_sub_le_mulHeight₁_rpow_neg` in TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/DiophantineApproximation/Roth/Theorem.lean#L172)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
