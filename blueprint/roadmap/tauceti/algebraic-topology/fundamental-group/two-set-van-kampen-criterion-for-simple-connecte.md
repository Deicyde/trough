---
declaration: theorem
origin: cited
lean: TauCeti.simplyConnectedSpace_of_interior_union
statement: formalized
proof: formalized
---

# Two-set van Kampen criterion for simple connectedness

A space covered by the interiors of
two simply connected sets with path-connected intersection is simply connected.

```lean
TauCeti.simplyConnectedSpace_of_interior_union.{u_1} {X : Type u_1} [TopologicalSpace X]
  {A B : Set X} (hCover : interior A ∪ interior B = Set.univ) (hAB : IsPathConnected (A ∩ B))
  [SimplyConnectedSpace ↑A] [SimplyConnectedSpace ↑B] : SimplyConnectedSpace X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.simplyConnectedSpace_of_interior_union`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.simplyConnectedSpace_of_interior_union).

## Sources

- [Tau Ceti documentation: `TauCeti.simplyConnectedSpace_of_interior_union`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.html#TauCeti.simplyConnectedSpace_of_interior_union)
- [Source of `TauCeti.simplyConnectedSpace_of_interior_union` in TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/FundamentalGroup/VanKampen/Basic.lean#L481)
