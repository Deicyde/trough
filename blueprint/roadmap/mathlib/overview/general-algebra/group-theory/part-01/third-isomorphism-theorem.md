---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: QuotientGroup.quotientQuotientEquivQuotient
mathlib_file: Mathlib/GroupTheory/QuotientGroup/Basic.lean
---

# Third isomorphism theorem

**Noether's third isomorphism theorem** for groups: `(G / N) / (M / N) ≃* G / M`.

```lean
QuotientGroup.quotientQuotientEquivQuotient.{u} {G : Type u} [Group G] (N : Subgroup G)
  [nN : N.Normal] (M : Subgroup G) [nM : M.Normal] (h : N ≤ M) :
  (G ⧸ N) ⧸ Subgroup.map (QuotientGroup.mk' N) M ≃* G ⧸ M
```

## Depends on

- [Group morphism](group-morphism.md)
- [Quotient group](quotient-group.md)

## Sources

- [Mathlib documentation: `QuotientGroup.quotientQuotientEquivQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientQuotientEquivQuotient)
- [Source of `QuotientGroup.quotientQuotientEquivQuotient` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L342)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L46)
- [1000+ theorems list: Q3527189](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2525)
- [1000+ theorems project: Q3527189](https://1000-plus.github.io/?length=-1#Q3527189)
- [Wikipedia: Lattice theorem](https://en.wikipedia.org/wiki/Lattice_theorem)
- [Wikidata: Q3527189](https://www.wikidata.org/wiki/Q3527189)
