---
declaration: theorem
origin: cited
lean: TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy
statement: formalized
proof: formalized
---

# Extensions of centralizers are discriminated by the base group

In a CSA group `G` with
the big powers property, the extension `G(u, ℤⁿ)` of the centralizer of `u ≠ 1` is discriminated
by `G` over `G`: any finite family of nonidentity elements survives under one retraction
`tᵢ ↦ u ^ kᵢ`.

```lean
TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy.{u_1} {G : Type u_1} [Group G] {u : G} {n : ℕ}
  (hBP : Group.IsBP G) (hG : Group.IsCSA G) (hu : u ≠ 1) :
  TauCeti.GroupAlgGeom.IsDiscriminatedBy TauCeti.LimitGroup.CentralizerExt.of (MonoidHom.id G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Discrimination.html#TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy).

## Sources

- [Tau Ceti documentation: `TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Discrimination.html#TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy)
- [Source of `TauCeti.LimitGroup.CentralizerExt.isDiscriminatedBy` in TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Discrimination.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/LimitGroup/CentralizerExtension/Discrimination.lean#L261)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
