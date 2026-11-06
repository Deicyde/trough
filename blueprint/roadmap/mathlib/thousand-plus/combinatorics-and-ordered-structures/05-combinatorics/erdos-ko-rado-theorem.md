# Erdős–Ko–Rado theorem

The **Erdős–Ko–Rado theorem**.

The maximum size of an intersecting family in `α` where all sets have size `r` is bounded by
`(card α - 1).choose (r - 1)`. This bound is sharp.

```lean
Finset.erdos_ko_rado {n : ℕ} {𝒜 : Finset (Finset (Fin n))} {r : ℕ} (h𝒜 : (↑𝒜).Intersecting)
  (h₂ : Set.Sized r ↑𝒜) (h₃ : r ≤ n / 2) : 𝒜.card ≤ (n - 1).choose (r - 1)
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Kruskal-Katona theorem](../../../overview/combinatorics/set-families/kruskal-katona-theorem.md)

## Sources

- [Mathlib documentation: `Finset.erdos_ko_rado`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/KruskalKatona.html#Finset.erdos_ko_rado)
- [Source of `Finset.erdos_ko_rado` in Mathlib/Combinatorics/SetFamily/KruskalKatona.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/KruskalKatona.lean#L342)
- [1000+ theorems list: Q718875](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L771)
- [1000+ theorems project: Q718875](https://1000-plus.github.io/all.html?length=-1#Q718875)
- [Wikipedia: Erdős–Ko–Rado theorem](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ko%E2%80%93Rado_theorem)
- [Wikidata: Q718875](https://www.wikidata.org/wiki/Q718875)
