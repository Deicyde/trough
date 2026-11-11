---
declaration: theorem
origin: cited
lean: TauCeti.coeff_prod_range_one_add_C_mul_X
statement: formalized
proof: formalized
---

# Cauchy's binomial theorem, in coefficient form

for `q ≠ 0`, the coefficient of `X ^ k`
in `∏_{j < n} (1 + q^(2j) X)` is `q^(k(n-1)) [n choose k]_q`.

```lean
TauCeti.coeff_prod_range_one_add_C_mul_X.{u_1} {K : Type u_1} [Semifield K] {q : K} (hq : q ≠ 0)
  (n k : ℕ) :
  (∏ j ∈ Finset.range n, (1 + Polynomial.C ((q ^ 2) ^ j) * Polynomial.X)).coeff k =
    q ^ (↑k * (↑n - 1)) * TauCeti.quantumBinomial q n k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.coeff_prod_range_one_add_C_mul_X`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Binomial.html#TauCeti.coeff_prod_range_one_add_C_mul_X).

## Sources

- [Tau Ceti documentation: `TauCeti.coeff_prod_range_one_add_C_mul_X`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/QuantumInteger/Binomial.html#TauCeti.coeff_prod_range_one_add_C_mul_X)
- [Source of `TauCeti.coeff_prod_range_one_add_C_mul_X` in TauCeti/QuantumGroups/QuantumInteger/Binomial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/QuantumGroups/QuantumInteger/Binomial.lean#L156)
