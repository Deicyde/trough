---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: QuotientGroup.quotientKerEquivRange, QuotientGroup.quotientInfEquivProdNormalQuotient, QuotientGroup.quotientQuotientEquivQuotient
mathlib_file: Mathlib/GroupTheory/QuotientGroup/Basic.lean
---

# First isomorphism theorem

Mathlib records this with 3 declarations.

`QuotientGroup.quotientKerEquivRange`: **Noether's first isomorphism theorem** (a definition): the canonical isomorphism between
`G/(ker φ)` to `range φ`.

```lean
QuotientGroup.quotientKerEquivRange.{u, v} {G : Type u} [Group G] {H : Type v} [Group H]
  (φ : G →* H) : G ⧸ φ.ker ≃* ↥φ.range
```

`QuotientGroup.quotientInfEquivProdNormalQuotient`: **Noether's second isomorphism theorem**: given two subgroups `H` and `N` of a group `G`,
where `N` is normal, defines an isomorphism between `H/(H ∩ N)` and `(HN)/N`.

```lean
QuotientGroup.quotientInfEquivProdNormalQuotient.{u} {G : Type u} [Group G] (H N : Subgroup G)
  [hN : N.Normal] : ↥H ⧸ N.subgroupOf H ≃* ↥(H ⊔ N) ⧸ N.subgroupOf (H ⊔ N)
```

`QuotientGroup.quotientQuotientEquivQuotient`: **Noether's third isomorphism theorem** for groups: `(G / N) / (M / N) ≃* G / M`.

```lean
QuotientGroup.quotientQuotientEquivQuotient.{u} {G : Type u} [Group G] (N : Subgroup G)
  [nN : N.Normal] (M : Subgroup G) [nM : M.Normal] (h : N ≤ M) :
  (G ⧸ N) ⧸ Subgroup.map (QuotientGroup.mk' N) M ≃* G ⧸ M
```

## Depends on

- [Group morphism](group-morphism.md)
- [Quotient group](quotient-group.md)

## Sources

- [Mathlib documentation: `QuotientGroup.quotientKerEquivRange`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientKerEquivRange)
- [Source of `QuotientGroup.quotientKerEquivRange` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L130)
- [Mathlib documentation: `QuotientGroup.quotientInfEquivProdNormalQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientInfEquivProdNormalQuotient)
- [Source of `QuotientGroup.quotientInfEquivProdNormalQuotient` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L302)
- [Mathlib documentation: `QuotientGroup.quotientQuotientEquivQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientQuotientEquivQuotient)
- [Source of `QuotientGroup.quotientQuotientEquivQuotient` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L342)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L44)
- [1000+ theorems list: Q1065966](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1291)
- [1000+ theorems list: Q1187646](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1491)
- [1000+ theorems project: Q1065966](https://1000-plus.github.io/?length=-1#Q1065966)
- [Wikipedia: Isomorphism theorem](https://en.wikipedia.org/wiki/Isomorphism_theorem)
- [Wikidata: Q1065966](https://www.wikidata.org/wiki/Q1065966)
- [1000+ theorems project: Q1187646](https://1000-plus.github.io/?length=-1#Q1187646)
- [Wikipedia: Fundamental theorem on homomorphisms](https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms)
- [Wikidata: Q1187646](https://www.wikidata.org/wiki/Q1187646)
