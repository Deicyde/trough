# Cauchy's theorem (group theory)

For every prime `p` dividing the order of a finite group `G` there exists an element of order
`p` in `G`. This is known as Cauchy's theorem.

```lean
exists_prime_orderOf_dvd_card.{u_3} {G : Type u_3} [Group G] [Fintype G] (p : ℕ)
  [hp : Fact (Nat.Prime p)] (hdvd : p ∣ Fintype.card G) : ∃ x, orderOf x = p
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)

## Proof depends on

- [Decomposition into cycles with disjoint support](../../../undergraduate/group-theory/permutation-group/decomposition-into-cycles-with-disjoint-support.md)
- [Greatest common divisor](../../../overview/general-algebra/divisibility-in-integral-domains/greatest-common-divisor.md)
- [Least common multiple](../../../overview/general-algebra/divisibility-in-integral-domains/least-common-multiple.md)

## Sources

- [Mathlib documentation: `exists_prime_orderOf_dvd_card`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#exists_prime_orderOf_dvd_card)
- [Source of `exists_prime_orderOf_dvd_card` in Mathlib/GroupTheory/Perm/Cycle/Type.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/GroupTheory/Perm/Cycle/Type.lean#L488)
- [1000+ theorems list: Q1139041](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1406)
- [1000+ theorems project: Q1139041](https://1000-plus.github.io/all.html?length=-1#Q1139041)
- [Wikipedia: Cauchy's theorem (group theory)](https://en.wikipedia.org/wiki/Cauchy's_theorem_%28group_theory%29)
- [Wikidata: Q1139041](https://www.wikidata.org/wiki/Q1139041)
