---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation
statement: formalized
proof: formalized
---

# Serre's theorem at arbitrary rank, as an equivalence

A pro-`p` group `G` has `cd_p G ≤ 1`
if and only if it is free pro-`p` on a pointed profinite space: some subset `s` of `G` converging to
`1` has a presentation `F_p(insert 1 s, 1) → G` that is a topological isomorphism.

```lean
TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation.{u}
  {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) :
  TauCeti.cohomologicalDimensionAt p G ≤ 1 ↔
    ∃ s, TauCeti.ConvergesToOne s ∧ ∃ e, ⇑e = ⇑(hG.presentation s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.ContCohomology.dimensionShiftIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-contcohomology-dimensionshiftiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.html#TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.html#TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation)
- [Source of `TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation` in TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.lean#L105)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
