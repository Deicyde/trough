---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: QuotientGroup.quotientKerEquivRange
mathlib_file: Mathlib/GroupTheory/QuotientGroup/Basic.lean
---

# First isomorphism theorem

**Noether's first isomorphism theorem** (a definition): the canonical isomorphism between
`G/(ker φ)` to `range φ`.

```lean
QuotientGroup.quotientKerEquivRange.{u, v} {G : Type u} [Group G] {H : Type v} [Group H]
  (φ : G →* H) : G ⧸ φ.ker ≃* ↥φ.range
```

The 1000+ list (Q1065966) also cites `QuotientGroup.quotientInfEquivProdNormalQuotient`, `QuotientGroup.quotientQuotientEquivQuotient`.

## Depends on

- [Group morphism](group-morphism.md)
- [Quotient group](quotient-group.md)

## Sources

- [Mathlib documentation: `QuotientGroup.quotientKerEquivRange`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivRange)
- [Source of `QuotientGroup.quotientKerEquivRange` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L130)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L44)
- [1000+ theorems list: Q1065966](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1291)
- [1000+ theorems list: Q1187646](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1491)
- [1000+ theorems project: Q1065966](https://1000-plus.github.io/all.html?length=-1#Q1065966)
- [Wikipedia: Isomorphism theorem](https://en.wikipedia.org/wiki/Isomorphism_theorem)
- [Wikidata: Q1065966](https://www.wikidata.org/wiki/Q1065966)
- [1000+ theorems project: Q1187646](https://1000-plus.github.io/all.html?length=-1#Q1187646)
- [Wikipedia: Fundamental theorem on homomorphisms](https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms)
- [Wikidata: Q1187646](https://www.wikidata.org/wiki/Q1187646)
