---
declaration: theorem
origin: cited
lean: TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae, TauCeti.IsTopologicalAddGroup.nonarchimedeanAddGroup_of_weaklyLocallyCompactSpace, TauCeti.IsTopologicalGroup.locallyCompact_totallyDisconnected_tfae, TauCeti.IsTopologicalGroup.nonarchimedeanGroup_of_weaklyLocallyCompactSpace
statement: formalized
proof: formalized
---

# Van Dantzig's theorem

For a Hausdorff topological additive group `G` the following are
equivalent:
1. `G` is locally compact and totally disconnected;
2. `G` is locally compact and nonarchimedean;
3. every neighbourhood of zero contains a compact open additive subgroup.

```lean
TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae.{u_1} {G : Type u_1}
  [AddGroup G] [TopologicalSpace G] [IsTopologicalAddGroup G] [T2Space G] :
  [LocallyCompactSpace G ∧ TotallyDisconnectedSpace G,
      LocallyCompactSpace G ∧ NonarchimedeanAddGroup G,
      ∀ U ∈ nhds 0, ∃ H, IsCompact ↑H ∧ ↑H ⊆ U].TFAE
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.html#TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae).

## Other forms

**Van Dantzig's theorem, in instance form.** Formalized in Tau Ceti as [`TauCeti.IsTopologicalAddGroup.nonarchimedeanAddGroup_of_weaklyLocallyCompactSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.html#TauCeti.IsTopologicalAddGroup.nonarchimedeanAddGroup_of_weaklyLocallyCompactSpace).

```lean
TauCeti.IsTopologicalAddGroup.nonarchimedeanAddGroup_of_weaklyLocallyCompactSpace.{u_1}
  {G : Type u_1} [AddGroup G] [TopologicalSpace G] [IsTopologicalAddGroup G]
  [ZeroDimensionalSpace G] [WeaklyLocallyCompactSpace G] : NonarchimedeanAddGroup G
```

**Van Dantzig's theorem.** Formalized in Tau Ceti as [`TauCeti.IsTopologicalGroup.locallyCompact_totallyDisconnected_tfae`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.html#TauCeti.IsTopologicalGroup.locallyCompact_totallyDisconnected_tfae).

```lean
TauCeti.IsTopologicalGroup.locallyCompact_totallyDisconnected_tfae.{u_1} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [T2Space G] :
  [LocallyCompactSpace G ∧ TotallyDisconnectedSpace G,
      LocallyCompactSpace G ∧ NonarchimedeanGroup G, ∀ U ∈ nhds 1, ∃ H, IsCompact ↑H ∧ ↑H ⊆ U].TFAE
```

**Van Dantzig's theorem, in instance form.** Formalized in Tau Ceti as [`TauCeti.IsTopologicalGroup.nonarchimedeanGroup_of_weaklyLocallyCompactSpace`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.html#TauCeti.IsTopologicalGroup.nonarchimedeanGroup_of_weaklyLocallyCompactSpace).

```lean
TauCeti.IsTopologicalGroup.nonarchimedeanGroup_of_weaklyLocallyCompactSpace.{u_1} {G : Type u_1}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [ZeroDimensionalSpace G]
  [WeaklyLocallyCompactSpace G] : NonarchimedeanGroup G
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.html#TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae)
- [Source of `TauCeti.IsTopologicalAddGroup.locallyCompact_totallyDisconnected_tfae` in TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/OpenSubgroup/Compact.lean#L143)
