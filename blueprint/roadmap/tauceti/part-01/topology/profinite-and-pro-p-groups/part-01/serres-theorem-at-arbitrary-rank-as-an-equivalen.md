---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation, TauCeti.IsProP.nonempty_continuousMulEquiv_freeProP_of_cohomologicalDimensionAt_le_one, TauCeti.IsProP.exists_convergesToOne_continuousMulEquiv_presentation_of_cohomologicalDimensionAt_le_one
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

- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Dimension shifting in every positive degree](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Frattini criterion for a kernel](../../algebra/part-01/the-frattini-criterion-for-a-kernel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.html#TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation).

## Other forms

**Serre's theorem.** Formalized in Tau Ceti as [`TauCeti.IsProP.nonempty_continuousMulEquiv_freeProP_of_cohomologicalDimensionAt_le_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Serre.html#TauCeti.IsProP.nonempty_continuousMulEquiv_freeProP_of_cohomologicalDimensionAt_le_one).

```lean
TauCeti.IsProP.nonempty_continuousMulEquiv_freeProP_of_cohomologicalDimensionAt_le_one.{u} {p : ℕ}
  [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hfg : TauCeti.IsTopologicallyFinitelyGenerated G)
  (hcd : TauCeti.cohomologicalDimensionAt p G ≤ 1) (X : Type u) [Finite X]
  (hX : Nat.card X = TauCeti.topologicalGeneratorRankNat G hfg) :
  Nonempty (G ≃ₜ* TauCeti.freeProP p X)
```

**Serre's theorem at arbitrary rank.** Formalized in Tau Ceti as [`TauCeti.IsProP.exists_convergesToOne_continuousMulEquiv_presentation_of_cohomologicalDimensionAt_le_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.html#TauCeti.IsProP.exists_convergesToOne_continuousMulEquiv_presentation_of_cohomologicalDimensionAt_le_one).

```lean
TauCeti.IsProP.exists_convergesToOne_continuousMulEquiv_presentation_of_cohomologicalDimensionAt_le_one.{u}
  {p : ℕ} [Fact (Nat.Prime p)] {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  [CompactSpace G] [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G)
  (hcd : TauCeti.cohomologicalDimensionAt p G ≤ 1) :
  ∃ s, TauCeti.ConvergesToOne s ∧ ∃ e, ⇑e = ⇑(hG.presentation s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.html#TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation)
- [Source of `TauCeti.IsProP.cohomologicalDimensionAt_le_one_iff_exists_convergesToOne_continuousMulEquiv_presentation` in TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/Pointed/Serre.lean#L105)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
