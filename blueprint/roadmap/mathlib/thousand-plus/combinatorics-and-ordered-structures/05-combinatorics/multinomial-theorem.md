# Multinomial theorem

The **multinomial theorem**.

```lean
Finset.sum_pow_eq_sum_piAntidiag_of_commute.{u_1, u_2} {α : Type u_1} {R : Type u_2} [DecidableEq α]
  [Semiring R] (s : Finset α) (f : α → R) (hc : (↑s).Pairwise (Function.onFun Commute f)) (n : ℕ) :
  (∑ i ∈ s, f i) ^ n =
    ∑ k ∈ s.piAntidiag n, ↑(Nat.multinomial s k) * s.noncommProd (fun i => f i ^ k i) ⋯
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.sum_pow_eq_sum_piAntidiag_of_commute`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Multinomial.html#Finset.sum_pow_eq_sum_piAntidiag_of_commute)
- [Source of `Finset.sum_pow_eq_sum_piAntidiag_of_commute` in Mathlib/Data/Nat/Choose/Multinomial.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Nat/Choose/Multinomial.lean#L269)
- [1000+ theorems list: Q619985](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L635)
- [1000+ theorems project: Q619985](https://1000-plus.github.io/all.html?length=-1#Q619985)
- [Wikipedia: Multinomial theorem](https://en.wikipedia.org/wiki/Multinomial_theorem)
- [Wikidata: Q619985](https://www.wikidata.org/wiki/Q619985)
