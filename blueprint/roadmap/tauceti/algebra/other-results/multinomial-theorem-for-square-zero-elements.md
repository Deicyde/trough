---
declaration: theorem
origin: cited
lean: Finset.sum_pow_of_commute_of_mul_self_eq_zero
statement: formalized
proof: formalized
---

# Multinomial theorem for square-zero elements

If the `x i` commute pairwise and square to
zero on `s`, then `(∑ i ∈ s, x i) ^ n` is `n !` times the sum, over the `n`-element subsets `t` of
`s`, of the products of the `x i` with `i ∈ t`.

```lean
Finset.sum_pow_of_commute_of_mul_self_eq_zero.{u_1, u_2} {R : Type u_1} [Semiring R] {ι : Type u_2}
  (s : Finset ι) (x : ι → R) (hc : (↑s).Pairwise (Function.onFun Commute x))
  (hx : ∀ i ∈ s, x i * x i = 0) (n : ℕ) :
  (∑ i ∈ s, x i) ^ n = n.factorial • ∑ t, (↑t).noncommProd x ⋯
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.sum_pow_of_commute_of_mul_self_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/BigOperators/Ring/SquareZero.html#Finset.sum_pow_of_commute_of_mul_self_eq_zero).

## Sources

- [Tau Ceti documentation: `Finset.sum_pow_of_commute_of_mul_self_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/BigOperators/Ring/SquareZero.html#Finset.sum_pow_of_commute_of_mul_self_eq_zero)
- [Source of `Finset.sum_pow_of_commute_of_mul_self_eq_zero` in TauCeti/Algebra/BigOperators/Ring/SquareZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BigOperators/Ring/SquareZero.lean#L77)
