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
- [Integer](../../general-algebra/numbers/integer.md)
- [Ring](../../general-algebra/rings/ring.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Chevalley–Warning theorem (1000+ theorems)](../../../thousand-plus/algebra/12-field-theory-and-polynomials/chevalley-warning-theorem.md)
- [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `ZMod.erdos_ginzburg_ziv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.html#ZMod.erdos_ginzburg_ziv)
- [Source of `ZMod.erdos_ginzburg_ziv` in Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Combinatorics/Additive/ErdosGinzburgZiv.lean#L178)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L551)
- [1000+ theorems list: Q716171](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L765)
- [1000+ theorems project: Q716171](https://1000-plus.github.io/all.html?length=-1#Q716171)
- [Wikipedia: Erdős–Ginzburg–Ziv theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ginzburg%E2%80%93Ziv_theorem)
- [Wikidata: Q716171](https://www.wikidata.org/wiki/Q716171)
