---
declaration: theorem
origin: cited
lean: IsSigmaCompact.exists_openSubgroup
statement: formalized
proof: formalized
---

# σ-compact open subgroups

In a locally compact group, every σ-compact set is contained in
a σ-compact open subgroup.

```lean
IsSigmaCompact.exists_openSubgroup.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [WeaklyLocallyCompactSpace G] {s : Set G} (hs : IsSigmaCompact s) :
  ∃ H, s ⊆ ↑H ∧ IsSigmaCompact ↑H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSigmaCompact.exists_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/SigmaCompact.html#IsSigmaCompact.exists_openSubgroup).

## Sources

- [Tau Ceti documentation: `IsSigmaCompact.exists_openSubgroup`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/SigmaCompact.html#IsSigmaCompact.exists_openSubgroup)
- [Source of `IsSigmaCompact.exists_openSubgroup` in TauCeti/Topology/Algebra/Group/OpenSubgroup/SigmaCompact.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/OpenSubgroup/SigmaCompact.lean#L51)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AmenableGroups/STATUS.md)
