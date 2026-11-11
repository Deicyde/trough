---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.openSubgroup
statement: formalized
proof: formalized
---

# An open subgroup of an infinite Demushkin group is Demushkin (Serre's exposé, §9.2)

The
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

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.html#TauCeti.IsDemushkin.openSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.html#TauCeti.IsDemushkin.openSubgroup)
- [Source of `TauCeti.IsDemushkin.openSubgroup` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/OpenSubgroup.lean#L140)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
