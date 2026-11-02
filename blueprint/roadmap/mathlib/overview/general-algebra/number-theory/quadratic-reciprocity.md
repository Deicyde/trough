---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: legendreSym.quadratic_reciprocity, jacobiSym.quadratic_reciprocity
mathlib_file: Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean
---

# Quadratic reciprocity

Mathlib records this with 2 declarations.

`legendreSym.quadratic_reciprocity`: **The Law of Quadratic Reciprocity**: if `p` and `q` are distinct odd primes, then
`(q / p) * (p / q) = (-1)^((p-1)(q-1)/4)`.

```lean
legendreSym.quadratic_reciprocity {p q : ℕ} [Fact (Nat.Prime p)] [Fact (Nat.Prime q)] (hp : p ≠ 2)
  (hq : q ≠ 2) (hpq : p ≠ q) : legendreSym q ↑p * legendreSym p ↑q = (-1) ^ (p / 2 * (q / 2))
```

`jacobiSym.quadratic_reciprocity`: The Law of Quadratic Reciprocity for the Jacobi symbol

```lean
jacobiSym.quadratic_reciprocity {a b : ℕ} (ha : Odd a) (hb : Odd b) :
  jacobiSym (↑a) b = (-1) ^ (a / 2 * (b / 2)) * jacobiSym (↑b) a
```

## Depends on

- [Euclid's' algorithm](../divisibility-in-integral-domains/euclids-algorithm.md)
- [Field](../field-theory/field.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Group morphism](../group-theory/part-01/group-morphism.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Characteristic of a ring](../field-theory/characteristic-of-a-ring.md)

## Sources

- [Mathlib documentation: `legendreSym.quadratic_reciprocity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.html#legendreSym.quadratic_reciprocity)
- [Source of `legendreSym.quadratic_reciprocity` in Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LegendreSymbol/QuadraticReciprocity.lean#L105)
- [Mathlib documentation: `jacobiSym.quadratic_reciprocity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LegendreSymbol/JacobiSymbol.html#jacobiSym.quadratic_reciprocity)
- [Source of `jacobiSym.quadratic_reciprocity` in Mathlib/NumberTheory/LegendreSymbol/JacobiSymbol.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/LegendreSymbol/JacobiSymbol.lean#L422)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L144)
- [Freek Wiedijk's 100 theorems, no. 7](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L38)
- [1000+ theorems list: Q472883](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L476)
- [1000+ theorems project: Q472883](https://1000-plus.github.io/?length=-1#Q472883)
- [Wikipedia: Quadratic reciprocity theorem](https://en.wikipedia.org/wiki/Quadratic_reciprocity_theorem)
- [Wikidata: Q472883](https://www.wikidata.org/wiki/Q472883)
