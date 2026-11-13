---
declaration: section
origin: cited
lean: Stacks.SpaceTorsor.Action.IsTorsor, Stacks.SpaceTorsor.TorsorHom, Stacks.SpaceTorsor.PresheafOfGroups.trivialAction, Stacks.SpaceTorsor.torsor_trivial_iff_global_section, Stacks.Cohomology.SheafTorsor.torsorCohomologyClassification, Stacks.Cohomology.SheafTorsor.torsorClassEquivSheafCohomologyOne
statement: formalized
proof: formalized
---

# 20.4 First cohomology and torsors

Section 20.4 of the Stacks Project, [Tag 02FN](https://stacks.math.columbia.edu/tag/02FN). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02FO, a definition

[Tag 02FO](https://stacks.math.columbia.edu/tag/02FO) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.SpaceTorsor.Action.IsTorsor`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PresheavesOfGroupsAndActions.lean#L190), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean#L39) (StacksFrontier): “the torsor condition on an action”.
- [`Stacks.SpaceTorsor.TorsorHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PresheavesOfGroupsAndActions.lean#L209), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean#L40) (StacksFrontier): “an equivariant morphism of torsors”.
- [`Stacks.SpaceTorsor.PresheafOfGroups.trivialAction`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PresheavesOfGroupsAndActions.lean#L241), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/Defs.lean#L41) (StacksFrontier): “the action defining the trivial torsor”.

## Tag 02FP, a lemma

[Tag 02FP](https://stacks.math.columbia.edu/tag/02FP) in the Stacks Project.

**`Stacks.SpaceTorsor.torsor_trivial_iff_global_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PresheavesOfGroupsAndActions.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/PresheavesOfGroupsAndActions.lean#L261).

> Let `X` be a topological space, `G` a sheaf of (possibly non-commutative) groups on `X`, and
> `F` a sheaf of sets with an action `a` of `G` making it a `G`-torsor. Then `F` is trivial if and
> only if `F(X)` is nonempty.

```lean
theorem torsor_trivial_iff_global_section
    {X : Type u} [TopologicalSpace X]
    (G : SheafOfGroups.{u, v} X) (F : SheafOfSets.{u, v} X)
    (a : Action G.toPresheafOfGroups F.toPresheafOfSets)
    (htorsor : a.IsTorsor) :
    a.IsTrivial ↔ Nonempty (F.obj ⊤)
```

## Tag 02FQ, a lemma

[Tag 02FQ](https://stacks.math.columbia.edu/tag/02FQ) in the Stacks Project.

**`Stacks.Cohomology.SheafTorsor.torsorCohomologyClassification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/FirstCohomologyClassification/Classification.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/FirstCohomologyClassification/Classification.lean#L502). References: EGA IV (16.5.15), “abelian sheaf of groups”.

> **Stacks Project, Tag 02FQ.** The canonical classification, with the
> transition-cocycle, trivial-torsor and contracted-product laws.

```lean
noncomputable def torsorCohomologyClassification (X : TopCat.{u})
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{max u v}]
    (H : TopCat.Sheaf AddCommGrpCat.{max u v} X) :
    TorsorCohomologyClassification X H
```

**`Stacks.Cohomology.SheafTorsor.torsorClassEquivSheafCohomologyOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Torsors/FirstCohomologyClassification/Classification.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/Torsors/FirstCohomologyClassification/Classification.lean#L512). The attribute's comment: “the canonical bijection”. References: EGA IV (16.5.15), “abelian sheaf of groups”; SGA 4½ Cycle (1.1.1), “topological space”; SGA 4½ Arcata (1.6.6), “topological space”.

> The canonical bijection between torsor classes and first sheaf cohomology.

```lean
noncomputable def torsorClassEquivSheafCohomologyOne (X : TopCat.{u})
    [HasSheafify (Opens.grothendieckTopology X) AddCommGrpCat.{max u v}]
    (H : TopCat.Sheaf AddCommGrpCat.{max u v} X) :
    TorsorClass X H ≃ sheafCohomologyOne X H
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.4, Tag 02FN](https://stacks.math.columbia.edu/tag/02FN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
