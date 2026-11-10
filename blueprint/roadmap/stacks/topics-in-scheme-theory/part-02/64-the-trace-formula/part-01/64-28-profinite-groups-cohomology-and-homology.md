---
declaration: section
origin: cited
lean: Stacks.GroupCohomology.normalInvariantsFunctor, Stacks.GroupCohomology.derivedNormalInvariantsFunctor, _root_.continuousGroupCohomologyFunctor, _root_.continuousGroupCohomology
statement: formalized
proof: formalized
---

# 64.28 Profinite groups, cohomology and homology

Section 64.28 of the Stacks Project, [Tag 03VI](https://stacks.math.columbia.edu/tag/03VI). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03VI, the section

[Tag 03VI](https://stacks.math.columbia.edu/tag/03VI) in the Stacks Project.

**`Stacks.GroupCohomology.normalInvariantsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean#L187). The attribute's comment: “H⁰(N, -) takes discrete Γ-modules to discrete Γ/N-modules”.

> Taking invariants under a normal subgroup `N` of a topological group `Γ` is a functor
> `H⁰(N, -)` from discrete `Γ`-modules to discrete `Γ ⧸ N`-modules.

```lean
def normalInvariantsFunctor :
    ContinuousGModule.{u, v} Γ ⥤ ContinuousGModule.{u, v} (Γ ⧸ N)
```

**`Stacks.GroupCohomology.derivedNormalInvariantsFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean#L232). The attribute's comment: “the derived functor RH⁰(N, -) of the invariants functor”.

> The right derived functor `RH⁰(N, -) : D⁺(Mod_Γ) ⥤ D⁺(Mod_{Γ⧸N})` of taking invariants
> under a normal subgroup.

```lean
abbrev derivedNormalInvariantsFunctor :
    DerivedCategory.Plus (ContinuousGModule.{u, max u v} Γ) ⥤
      DerivedCategory.Plus (ContinuousGModule.{u, max u v} (Γ ⧸ N))
```

Declarations registered for the tag:

- [`_root_.continuousGroupCohomologyFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.continuousGroupCohomologyFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean#L247) (StacksFrontier): “the cohomology functors Hⁱ(G, -) of a profinite group on discrete modules”.
- [`_root_.continuousGroupCohomology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=_root_.continuousGroupCohomology#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GroupCohomology/NormalQuotientInvariants.lean#L249) (StacksFrontier): “the cohomology groups Hⁱ(G, M) of a profinite group on a discrete module”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.28, Tag 03VI](https://stacks.math.columbia.edu/tag/03VI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
