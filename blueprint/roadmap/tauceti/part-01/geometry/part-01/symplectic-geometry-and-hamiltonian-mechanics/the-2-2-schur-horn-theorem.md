---
declaration: theorem
origin: cited
lean: Matrix.exists_isSymm_fin_two_charpoly_eq_iff
statement: formalized
proof: formalized
---

# The `2 × 2` Schur–Horn theorem

For `l₂ ≤ l₁`, a real symmetric `2 × 2` matrix with
diagonal `(d₁, d₂)` and characteristic polynomial `(X - l₁) (X - l₂)` exists exactly when
`(d₁, d₂)` is majorized by `(l₁, l₂)`, that is, when `l₂ ≤ d₁ ≤ l₁` and `d₁ + d₂ = l₁ + l₂`. In
that case `!![d₁, b; b, d₂]` with `b = √((l₁ - d₁) (d₁ - l₂))` is such a matrix.

```lean
Matrix.exists_isSymm_fin_two_charpoly_eq_iff {l₁ l₂ d₁ d₂ : ℝ} (hl : l₂ ≤ l₁) :
  (∃ A,
      A.IsSymm ∧
        A 0 0 = d₁ ∧
          A 1 1 = d₂ ∧
            A.charpoly = (Polynomial.X - Polynomial.C l₁) * (Polynomial.X - Polynomial.C l₂)) ↔
    l₂ ≤ d₁ ∧ d₁ ≤ l₁ ∧ d₁ + d₂ = l₁ + l₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.exists_isSymm_fin_two_charpoly_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.exists_isSymm_fin_two_charpoly_eq_iff).

## Sources

- [Tau Ceti documentation: `Matrix.exists_isSymm_fin_two_charpoly_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.exists_isSymm_fin_two_charpoly_eq_iff)
- [Source of `Matrix.exists_isSymm_fin_two_charpoly_eq_iff` in TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean#L266)
