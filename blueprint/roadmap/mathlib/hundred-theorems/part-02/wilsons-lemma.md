# Wilson’s Lemma

**Wilson's Lemma**: the product of `1`, ..., `p-1` is `-1` modulo `p`.

```lean
ZMod.wilsons_lemma (p : ℕ) [Fact (Nat.Prime p)] : ↑(p - 1).factorial = -1
```

## Depends on

- [Field](../../overview/general-algebra/field-theory/field.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Rational number](../../overview/general-algebra/numbers/rational-number.md)

## Proof depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Group morphism](../../overview/general-algebra/group-theory/part-01/group-morphism.md)

## Sources

- [Mathlib documentation: `ZMod.wilsons_lemma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Wilson.html#ZMod.wilsons_lemma)
- [Source of `ZMod.wilsons_lemma` in Mathlib/NumberTheory/Wilson.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Wilson.lean#L60)
- [Freek Wiedijk's 100 theorems, no. 51](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L265)
- [1000+ theorems list: Q276082](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L318)
- [1000+ theorems project: Q276082](https://1000-plus.github.io/all.html?length=-1#Q276082)
- [Wikipedia: Wilson's theorem](https://en.wikipedia.org/wiki/Wilson's_theorem)
- [Wikidata: Q276082](https://www.wikidata.org/wiki/Q276082)
