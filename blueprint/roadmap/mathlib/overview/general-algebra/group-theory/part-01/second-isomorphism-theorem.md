---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: QuotientGroup.quotientInfEquivProdNormalQuotient
mathlib_file: Mathlib/GroupTheory/QuotientGroup/Basic.lean
---

# Second isomorphism theorem

**Noether's second isomorphism theorem**: given two subgroups `H` and `N` of a group `G`,
where `N` is normal, defines an isomorphism between `H/(H ∩ N)` and `(HN)/N`.

```lean
QuotientGroup.quotientInfEquivProdNormalQuotient.{u} {G : Type u} [Group G] (H N : Subgroup G)
  [hN : N.Normal] : ↥H ⧸ N.subgroupOf H ≃* ↥(H ⊔ N) ⧸ N.subgroupOf (H ⊔ N)
```

## Depends on

- [Group morphism](group-morphism.md)
- [Quotient group](quotient-group.md)

## Sources

- [Mathlib documentation: `QuotientGroup.quotientInfEquivProdNormalQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Basic.html#QuotientGroup.quotientInfEquivProdNormalQuotient)
- [Source of `QuotientGroup.quotientInfEquivProdNormalQuotient` in Mathlib/GroupTheory/QuotientGroup/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/QuotientGroup/Basic.lean#L302)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L45)
