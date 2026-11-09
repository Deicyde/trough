# Tychonoff's theorem

**Tychonoff's theorem**: product of compact sets is compact.

```lean
isCompact_pi_infinite.{u_1, u_2} {ι : Type u_1} {X : ι → Type u_2}
  [(i : ι) → TopologicalSpace (X i)] {s : (i : ι) → Set (X i)} :
  (∀ (i : ι), IsCompact (s i)) → IsCompact {x | ∀ (i : ι), x i ∈ s i}
```

## Depends on

- [Compactness in terms of filters](../../../overview/topology/general-topology/part-01/compactness-in-terms-of-filters.md)

## Proof depends on

- [Limit of a map with respect to filters](../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Sources

- [Mathlib documentation: `isCompact_pi_infinite`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Compactness/Compact.html#isCompact_pi_infinite)
- [Source of `isCompact_pi_infinite` in Mathlib/Topology/Compactness/Compact.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Compactness/Compact.lean#L1160)
- [1000+ theorems list: Q1137014](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1395)
- [1000+ theorems project: Q1137014](https://1000-plus.github.io/all.html?length=-1#Q1137014)
- [Wikipedia: Tychonoff's theorem](https://en.wikipedia.org/wiki/Tychonoff's_theorem)
- [Wikidata: Q1137014](https://www.wikidata.org/wiki/Q1137014)
