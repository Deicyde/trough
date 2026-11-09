---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le
statement: formalized
proof: formalized
---

# Minkowski's second theorem for the unit lattice

There are units `u 0, …, u (r - 1)`, where
`r = rank K`, with linearly independent logarithmic embeddings and
`∏ i, ‖log u i‖₁ ≤ r! * regulator K`, where `‖log x‖₁` is the `ℓ¹` norm of the logarithmic
embedding of `x`. This is Minkowski's second theorem for the unit lattice and the `ℓ¹` unit ball
`logBall K`, whose volume is `2 ^ r / r!`.

```lean
TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le.{u_1} {K : Type u_1}
  [Field K] [NumberField K] :
  ∃ u,
    NumberField.Units.IsMaxRank u ∧
      ∏ i, ∑ w, |(NumberField.Units.logEmbedding K) (Additive.ofMul (u i)) w| ≤
        ↑(NumberField.Units.rank K).factorial * NumberField.Units.regulator K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Minkowski's second theorem, upper bound, in terms of the successive minima](minkowskis-second-theorem-upper-bound-in-terms-o.md)
- [ZLattice.successiveMin](zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.html#TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le)
- [Source of `TauCeti.NumberField.Units.exists_isMaxRank_prod_sum_abs_logEmbedding_le` in TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Units/FundamentalSystem.lean#L186)
