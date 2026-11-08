---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two
statement: formalized
proof: formalized
---

# Tate's theorem: an infinite Demushkin group has `p`-cohomological dimension exactly `2`

The lower bound is `H²(G, 𝔽_p) ≠ 0`; the upper bound is the right exactness of `H²` on the finite
`𝔽_p[G]`-modules, which Tate's perfect duality provides.

```lean
TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two.{u} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] [Infinite G] (hG : TauCeti.IsDemushkin p G) :
  TauCeti.cohomologicalDimensionAt p G = 2
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Informally uses

- [Tate's duality map `α₁` of an infinite Demushkin group with coefficients `I(χ)/pⁱ` is bijective on every finite discrete `G`-module `M` killed by `pⁱ`](tates-duality-map-1-of-an-infinite-demushkin-gro.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.html#TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.html#TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two)
- [Source of `TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.lean#L57)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
