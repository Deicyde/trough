---
declaration: theorem
origin: cited
lean: TauCeti.sub_one_mul_padicValNat_factorial_pow, TauCeti.padicValNat_factorial_eq_add_sum
statement: formalized
proof: formalized
---

# Legendre's formula for `(pᵏ)!`

Since `pᵏ` has base-`p` digit sum one,
`(p - 1) v_p((pᵏ)!) = pᵏ - 1`.

```lean
TauCeti.sub_one_mul_padicValNat_factorial_pow (p : ℕ) [hp : Fact (Nat.Prime p)] (k : ℕ) :
  (p - 1) * padicValNat p (p ^ k).factorial = p ^ k - 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sub_one_mul_padicValNat_factorial_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Factorial.html#TauCeti.sub_one_mul_padicValNat_factorial_pow).

## Other forms

**Legendre's formula, truncated at level `h`.** Formalized in Tau Ceti as [`TauCeti.padicValNat_factorial_eq_add_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Factorial.html#TauCeti.padicValNat_factorial_eq_add_sum).

```lean
TauCeti.padicValNat_factorial_eq_add_sum (p : ℕ) [Fact (Nat.Prime p)] (n h : ℕ) :
  padicValNat p n.factorial =
    padicValNat p (n / p ^ h).factorial + ∑ k ∈ Finset.range h, n / p ^ (k + 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.sub_one_mul_padicValNat_factorial_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Factorial.html#TauCeti.sub_one_mul_padicValNat_factorial_pow)
- [Source of `TauCeti.sub_one_mul_padicValNat_factorial_pow` in TauCeti/NumberTheory/Padics/Factorial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Factorial.lean#L69)
