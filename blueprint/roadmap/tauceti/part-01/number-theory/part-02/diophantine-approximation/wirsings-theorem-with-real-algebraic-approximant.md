---
declaration: theorem
origin: cited
lean: TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max
statement: formalized
proof: formalized
---

# Wirsing's theorem with real algebraic approximants (Wirsing 1961; Bugeaud, Theorem 3.4)

For `1 ≤ n` and irrational `ξ`, every real exponent `w` strictly below
`max 1 (wₙ(ξ) / (wₙ(ξ) - n + 1))` is achieved by infinitely many **real** algebraic numbers of
degree at most `n`. When `wₙ(ξ) = ⊤`, `⊤ / ⊤ = 0` in `ℝ≥0∞`, so the `max 1 (...)` term supplies the
rational-approximant bound `w < 1`.

```lean
TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max {n : ℕ} (hn : 1 ≤ n) {ξ : ℝ}
  (hξ : Irrational ξ) {w : ℝ}
  (hw :
    ENNReal.ofReal w < max 1 (TauCeti.mahlerExponent n ξ / (TauCeti.mahlerExponent n ξ - ↑n + 1))) :
  (Complex.ofReal ⁻¹' TauCeti.algebraicApproximations n ξ w).Infinite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dirichlet's lower bound for Mahler's exponent](dirichlets-lower-bound-for-mahlers-exponent.md)
- [Liouville's bound for Mahler's exponent](../roths-theorem-and-the-subspace-theorem-over-numb/liouvilles-bound-for-mahlers-exponent.md)
- [Minkowski's linear forms theorem](../successive-minima-and-minkowskis-theorems/minkowskis-linear-forms-theorem.md)
- [Northcott's theorem for integer polynomials](../../../analysis/part-04/polynomial/northcotts-theorem-for-integer-polynomials.md)
- [Northcott's theorem for the Mahler measure](../../part-01/diophantine-approximation-and-transcendence/northcotts-theorem-for-the-mahler-measure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.html#TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max).

## Sources

- [Tau Ceti documentation: `TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.html#TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max)
- [Source of `TauCeti.infinite_preimage_ofReal_algebraicApproximations_of_lt_max` in TauCeti/NumberTheory/DiophantineApproximation/Wirsing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.lean#L442)
