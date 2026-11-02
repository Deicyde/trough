---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ZMod.erdos_ginzburg_ziv
mathlib_file: Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.lean
---

# Erdős–Ginzburg–Ziv theorem

The **Erdős–Ginzburg–Ziv theorem** for `ℤ/nℤ`.

Any sequence of at least `2 * n - 1` elements of `ZMod n` contains a subsequence of `n` elements
whose sum is zero.

```lean
ZMod.erdos_ginzburg_ziv.{u_1} {ι : Type u_1} {n : ℕ} {s : Finset ι} (a : ι → ZMod n)
  (hs : 2 * n - 1 ≤ s.card) : ∃ t ⊆ s, t.card = n ∧ ∑ i ∈ t, a i = 0
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic p](../../general-algebra/field-theory/characteristic-p.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Euclid's' algorithm](../../general-algebra/divisibility-in-integral-domains/euclids-algorithm.md)
- [Field](../../general-algebra/field-theory/field.md)
- [Irreducible element](../../general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Polynomial in several indeterminates](../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Sources

- [Mathlib documentation: `ZMod.erdos_ginzburg_ziv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.html#ZMod.erdos_ginzburg_ziv)
- [Source of `ZMod.erdos_ginzburg_ziv` in Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.lean#L178)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L551)
- [1000+ theorems list: Q716171](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L765)
- [1000+ theorems project: Q716171](https://1000-plus.github.io/all.html?length=-1#Q716171)
- [Wikipedia: Erdős–Ginzburg–Ziv theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ginzburg%E2%80%93Ziv_theorem)
- [Wikidata: Q716171](https://www.wikidata.org/wiki/Q716171)
