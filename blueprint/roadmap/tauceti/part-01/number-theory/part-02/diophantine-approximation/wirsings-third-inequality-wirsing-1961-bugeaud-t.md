---
declaration: theorem
origin: cited
lean: TauCeti.div_le_algebraicApproximationExponent
statement: formalized
proof: formalized
---

# Wirsing's third inequality (Wirsing 1961; Bugeaud, Theorem 3.4)

For every `n : ℕ` and
every `ξ : ℝ`, `wₙ(ξ) / (wₙ(ξ) - n + 1) ≤ w*ₙ(ξ)` in `ℝ≥0∞`. At `wₙ(ξ) = n` this reads
`n ≤ w*ₙ(ξ)`; at `wₙ(ξ) = ⊤` the left-hand side is `⊤ / ⊤ = 0`, while
`algebraicApproximationExponent_eq_top_iff` gives `w*ₙ(ξ) = ⊤`; and when `ξ` is algebraic of
degree `D ≤ n`, truncated subtraction sets `wₙ(ξ) - n = 0` so both sides equal `D - 1`.

```lean
TauCeti.div_le_algebraicApproximationExponent (n : ℕ) (ξ : ℝ) :
  TauCeti.mahlerExponent n ξ / (TauCeti.mahlerExponent n ξ - ↑n + 1) ≤
    TauCeti.algebraicApproximationExponent n ξ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's bound for Mahler's exponent](../roths-theorem-and-the-subspace-theorem-over-numb/liouvilles-bound-for-mahlers-exponent.md)
- [Wirsing's theorem with real algebraic approximants (Wirsing 1961; Bugeaud, Theorem 3.4)](wirsings-theorem-with-real-algebraic-approximant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.div_le_algebraicApproximationExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.html#TauCeti.div_le_algebraicApproximationExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.div_le_algebraicApproximationExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.html#TauCeti.div_le_algebraicApproximationExponent)
- [Source of `TauCeti.div_le_algebraicApproximationExponent` in TauCeti/NumberTheory/DiophantineApproximation/Wirsing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DiophantineApproximation/Wirsing.lean#L601)
