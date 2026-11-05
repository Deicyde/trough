---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.kruskal_katona
mathlib_file: Mathlib/Combinatorics/SetFamily/KruskalKatona.lean
---

# Kruskal-Katona theorem

The **Kruskal-Katona theorem**.

Given a set family `𝒜` consisting of `r`-sets, and `𝒞` an initial segment of the colex order of the
same size, the shadow of `𝒞` is smaller than the shadow of `𝒜`. In particular, this gives that the
minimum shadow size is achieved by initial segments of colex.

```lean
Finset.kruskal_katona {n r : ℕ} {𝒜 𝒞 : Finset (Finset (Fin n))} (h𝒜r : Set.Sized r ↑𝒜)
  (h𝒞𝒜 : 𝒞.card ≤ 𝒜.card) (h𝒞 : Finset.Colex.IsInitSeg 𝒞 r) : 𝒞.shadow.card ≤ 𝒜.shadow.card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.kruskal_katona`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/KruskalKatona.html#Finset.kruskal_katona)
- [Source of `Finset.kruskal_katona` in Mathlib/Combinatorics/SetFamily/KruskalKatona.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/KruskalKatona.lean#L264)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L521)
- [1000+ theorems list: Q3527102](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2483)
- [1000+ theorems project: Q3527102](https://1000-plus.github.io/all.html?length=-1#Q3527102)
- [Wikipedia: Kruskal–Katona theorem](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Katona_theorem)
- [Wikidata: Q3527102](https://www.wikidata.org/wiki/Q3527102)
