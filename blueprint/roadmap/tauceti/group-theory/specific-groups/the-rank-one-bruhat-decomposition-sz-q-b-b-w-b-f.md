---
declaration: theorem
origin: cited
lean: TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset
statement: formalized
proof: formalized
---

# The rank-one Bruhat decomposition `Sz(q) = B ∪ B w B`, for `m ≠ 0`

```lean
TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset (m : ℕ) (hm : m ≠ 0)
  (g : ↥(TauCeti.suzukiGroup m)) :
  g ∈ TauCeti.Suzuki.borelSubgroupOf m ∨
    g ∈
      DoubleCoset.doubleCoset (TauCeti.Suzuki.weylOf m) ↑(TauCeti.Suzuki.borelSubgroupOf m)
        ↑(TauCeti.Suzuki.borelSubgroupOf m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy--Binet for `2 × 2` minors](../../linear-algebra/matrix/cauchy-binet-for-2-2-minors.md)
- [The finite-field generation theorem](the-finite-field-generation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Simple.html#TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset).

## Sources

- [Tau Ceti documentation: `TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Simple.html#TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset)
- [Source of `TauCeti.Suzuki.mem_borelSubgroupOf_or_mem_doubleCoset` in TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/SpecificGroups/CFSG/Suzuki/Simple.lean#L83)
