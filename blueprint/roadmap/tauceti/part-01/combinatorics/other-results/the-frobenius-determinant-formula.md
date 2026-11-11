---
declaration: theorem
origin: cited
lean: TauCeti.standardCount_mul_prod_factorial_betaNumber
statement: formalized
proof: formalized
---

# The Frobenius determinant formula

**The Frobenius determinant formula** for the number `f^μ` of standard Young tableaux of shape
`μ`: for any bound `r` on the number of rows, `f^μ` times the product of the factorials of the
beta-numbers is `μ.card !` times the product of their differences over the ordered pairs of rows.

The differences are differences of natural numbers, and are truncated at no ordered pair: the
beta-numbers strictly decrease across `k < l < r`.

This is the multiplicative form of `f^μ = n ! * ∏_{k < l} (β_k - β_l) / ∏_k β_k !`, and carries no
division obligation.

```lean
TauCeti.standardCount_mul_prod_factorial_betaNumber (μ : YoungDiagram) {r : ℕ}
  (hr : μ.colLen 0 ≤ r) :
  TauCeti.standardCount μ * ∏ i ∈ Finset.range r, (μ.betaNumber r i).factorial =
    μ.card.factorial *
      ∏ k ∈ Finset.range r, ∏ l ∈ Finset.Ico (k + 1) r, (μ.betaNumber r k - μ.betaNumber r l)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's formula for a determinant, in row form](../../linear-algebra/other-results/jacobis-formula-for-a-determinant-in-row-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.standardCount_mul_prod_factorial_betaNumber`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/HookLength/Formula.html#TauCeti.standardCount_mul_prod_factorial_betaNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.standardCount_mul_prod_factorial_betaNumber`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/HookLength/Formula.html#TauCeti.standardCount_mul_prod_factorial_betaNumber)
- [Source of `TauCeti.standardCount_mul_prod_factorial_betaNumber` in TauCeti/Combinatorics/Young/HookLength/Formula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Young/HookLength/Formula.lean#L260)
