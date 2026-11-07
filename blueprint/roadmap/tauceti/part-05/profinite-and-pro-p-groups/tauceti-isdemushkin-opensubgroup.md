---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.openSubgroup
statement: formalized
proof: formalized
---

# TauCeti.IsDemushkin.openSubgroup

**An open subgroup of an infinite Demushkin group is Demushkin** (Serre's exposé, §9.2). The
subgroup is pro-`p` and topologically finitely generated with `G`; its `H²(U, 𝔽_p)` is
one-dimensional by `TauCeti.IsDemushkin.finrank_cohomFp_two_openSubgroup`; and its cup product is
nondegenerate because a nonzero class of `H¹(U, 𝔽_p) ≅ H¹(G, Coind_U^G 𝔽_p)` is paired
nontrivially by Tate's duality map `α₁` of `G`, a pairing which is the corestriction of a cup
product of `U`.

```lean
TauCeti.IsDemushkin.openSubgroup.{u} {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  [Infinite G] (hG : TauCeti.IsDemushkin p G) (U : OpenSubgroup G) : TauCeti.IsDemushkin p ↥↑U
```

## Depends on

- [TauCeti.IsDemushkin](tauceti-isdemushkin.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.html#TauCeti.IsDemushkin.openSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.html#TauCeti.IsDemushkin.openSubgroup)
- [Source of `TauCeti.IsDemushkin.openSubgroup` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.lean#L140)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
