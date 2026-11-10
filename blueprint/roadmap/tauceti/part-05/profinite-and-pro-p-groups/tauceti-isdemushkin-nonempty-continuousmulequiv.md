---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff
statement: formalized
proof: formalized
---

# TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff

**The classification of Demushkin groups** (Labute): two Demushkin groups are topologically
isomorphic if and only if they have the same rank and their canonical characters have the same
image. The forward direction is the invariance of both invariants under isomorphism; the
converse is `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_range_demushkinCharacter_eq`.

```lean
TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff.{u, v} {p : ℕ} [Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] {H : Type v} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  [CompactSpace H] [TotallyDisconnectedSpace H] (hG : TauCeti.IsDemushkin p G)
  (hH : TauCeti.IsDemushkin p H) :
  Nonempty (G ≃ₜ* H) ↔
    TauCeti.demushkinRank hG = TauCeti.demushkinRank hH ∧
      (TauCeti.demushkinCharacter hG).range = (TauCeti.demushkinCharacter hH).range
```

## Depends on

- [TauCeti.IsDemushkin](tauceti-isdemushkin.md)

## Proof depends on

- [The unconstrained successive-approximation theorem](the-unconstrained-successive-approximation-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff)
- [Source of `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_iff` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L230)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
