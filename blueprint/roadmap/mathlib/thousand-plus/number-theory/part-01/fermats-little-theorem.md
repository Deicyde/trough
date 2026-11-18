# Fermat's little theorem

**Fermat's Little Theorem**: for all nonzero `a : ZMod p`, we have `a ^ (p - 1) = 1`.

```lean
ZMod.pow_card_sub_one_eq_one {p : ℕ} [Fact (Nat.Prime p)] {a : ZMod p} (ha : a ≠ 0) :
  a ^ (p - 1) = 1
```

## Depends on

- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Irreducible element](../../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `ZMod.pow_card_sub_one_eq_one`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.pow_card_sub_one_eq_one)
- [Source of `ZMod.pow_card_sub_one_eq_one` in Mathlib/FieldTheory/Finite/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/FieldTheory/Finite/Basic.lean#L578)
- [1000+ theorems list: Q188295](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L117)
- [1000+ theorems project: Q188295](https://1000-plus.github.io/all.html?length=-1#Q188295)
- [Wikipedia: Fermat's little theorem](https://en.wikipedia.org/wiki/Fermat's_little_theorem)
- [Wikidata: Q188295](https://www.wikidata.org/wiki/Q188295)
