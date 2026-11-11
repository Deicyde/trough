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

## Proof depends on

- [Tate's duality criterion for `cd_p G ≤ 2`](../../algebra/part-02/tates-duality-criterion-for-cd-p-g-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.html#TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.html#TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two)
- [Source of `TauCeti.IsDemushkin.cohomologicalDimensionAt_eq_two` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/CohomologicalDimension.lean#L57)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
