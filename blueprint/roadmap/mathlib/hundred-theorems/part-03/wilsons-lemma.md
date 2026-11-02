---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ZMod.wilsons_lemma
mathlib_file: Mathlib/NumberTheory/Wilson.lean
---

# Wilson’s Lemma

**Wilson's Lemma**: the product of `1`, ..., `p-1` is `-1` modulo `p`.

```lean
ZMod.wilsons_lemma (p : ℕ) [Fact (Nat.Prime p)] : ↑(p - 1).factorial = -1
```

## Depends on

- [Euclid's' algorithm](../../overview/general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)
- [Field](../../overview/general-algebra/field-theory/field.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Bezout’s Theorem](bezouts-theorem.md)
- [Characteristic p](../../overview/general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Group](../../overview/general-algebra/group-theory/part-01/group.md)
- [Ring morphism](../../overview/general-algebra/rings/ring-morphism.md)
- [Set](../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `ZMod.wilsons_lemma`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Wilson.html#ZMod.wilsons_lemma)
- [Source of `ZMod.wilsons_lemma` in Mathlib/NumberTheory/Wilson.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/Wilson.lean#L60)
- [Freek Wiedijk's 100 theorems, no. 51](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L265)
- [1000+ theorems list: Q276082](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L318)
- [1000+ theorems project: Q276082](https://1000-plus.github.io/?length=-1#Q276082)
- [Wikipedia: Wilson's theorem](https://en.wikipedia.org/wiki/Wilson's_theorem)
- [Wikidata: Q276082](https://www.wikidata.org/wiki/Q276082)
