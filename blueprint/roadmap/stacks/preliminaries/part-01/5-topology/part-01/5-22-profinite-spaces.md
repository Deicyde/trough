---
declaration: section
origin: cited
lean: IsProfiniteStacks, isProfiniteStacks_iff_t2_compact_totallyDisconnected_and_isProfinite, Profinite.compactSpace_t2Space_totallyDisconnectedSpace_of_isLimit, Profinite.hasLimits, TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover, isProfiniteSpacePropForm_connectedComponents
statement: formalized
proof: formalized
---

# 5.22 Profinite spaces

Section 5.22 of the Stacks Project, [Tag 08ZW](https://stacks.math.columbia.edu/tag/08ZW). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08ZX, a definition

[Tag 08ZX](https://stacks.math.columbia.edu/tag/08ZX) in the Stacks Project.

**`IsProfiniteStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Profinite/Defs.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Profinite/Defs.lean#L36).

> **Stacks 08ZX** (definition of profinite). A topological space `X` is profinite if it is
> homeomorphic to (the underlying space of) the limit of some diagram of finite discrete topological
> spaces.

```lean
def IsProfiniteStacks (X : Type u) [TopologicalSpace X] : Prop
```

## Tag 08ZY, a lemma

[Tag 08ZY](https://stacks.math.columbia.edu/tag/08ZY) in the Stacks Project.

**`isProfiniteStacks_iff_t2_compact_totallyDisconnected_and_isProfinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Profinite/LimitCharacterization.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Profinite/LimitCharacterization.lean#L29). The attribute's comment: “Both directions and the final sentence. Profinite is `IsProfiniteStacks` (Stacks 08ZX): homeomorphic to the limit of an arbitrary diagram of finite discrete spaces indexed by a small category in the universe of `X`; the cofiltered conclusion is `IsProfinite`.”.

> **Stacks 08ZY.** For a topological space `X` the following are equivalent: (1) `X` is a
> profinite space, i.e. homeomorphic to the limit of a diagram of finite discrete spaces (Stacks
> 08ZX, `IsProfiniteStacks`); (2) `X` is Hausdorff, quasi-compact and totally disconnected. If this
> is true, then `X` is a cofiltered limit of finite discrete spaces (`IsProfinite`).

```lean
theorem isProfiniteStacks_iff_t2_compact_totallyDisconnected_and_isProfinite
    (X : Type u) [TopologicalSpace X] :
    (IsProfiniteStacks X ↔ T2Space X ∧ CompactSpace X ∧ TotallyDisconnectedSpace X) ∧
      (IsProfiniteStacks X → IsProfinite X)
```

## Tag 0ET8, a lemma

[Tag 0ET8](https://stacks.math.columbia.edu/tag/0ET8) in the Stacks Project.

**`Profinite.compactSpace_t2Space_totallyDisconnectedSpace_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Profinite/Limits.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Profinite/Limits.lean#L50). The attribute's comment: “the limit is taken in `TopCat`, as an arbitrary limit cone of `F ⋙ Profinite.toTopCat`”.

> **Stacks 0ET8.** A limit of profinite spaces is profinite: for a small diagram `F` of profinite
> spaces, the point of any limit cone of the underlying diagram `F ⋙ Profinite.toTopCat` in `TopCat`
> is compact, Hausdorff and totally disconnected.
>
> This is the faithful form of the tag, with the limit taken in `TopCat`; the registration of 0ET8 on
> `Profinite.hasLimits` in the reviewed tree is the weaker categorical statement that `Profinite` has
> limits.

```lean
theorem compactSpace_t2Space_totallyDisconnectedSpace_of_isLimit {J : Type v} [SmallCategory J]
    {F : J ⥤ Profinite.{max u v}} {c : Cone (F ⋙ Profinite.toTopCat)} (hc : IsLimit c) :
    CompactSpace c.pt ∧ T2Space c.pt ∧ TotallyDisconnectedSpace c.pt
```

Declarations registered for the tag:

- [`Profinite.hasLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Profinite.hasLimits#doc) registered with `add_to_stacks` in [StacksCore/Topology/Profinite/Limits.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Profinite/Limits.lean#L21) (StacksCore): “every small diagram of profinite spaces has a limit in `Profinite`, i.e. its limit is again a profinite space”.

## Tag 08ZZ, a lemma

[Tag 08ZZ](https://stacks.math.columbia.edu/tag/08ZZ) in the Stacks Project.

Declarations registered for the tag:

- [`TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.IsOpenCover.exists_finite_nonempty_disjoint_clopen_cover#doc) registered with `add_to_stacks` in [StacksCore/Topology/Profinite/ClopenRefinement.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Profinite/ClopenRefinement.lean#L21) (StacksCore).

## Tag 0900, a lemma

[Tag 0900](https://stacks.math.columbia.edu/tag/0900) in the Stacks Project.

**`isProfiniteSpacePropForm_connectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/ComponentSpaceCompact.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Connected/ComponentSpaceCompact.lean#L60).

> **Stacks 0900.** Let `X` be a quasi-compact topological space such that every connected
> component of `X` equals the intersection of the clopen subsets of `X` containing it. Then
> `ConnectedComponents X`, with the quotient topology, is a profinite space: compact, Hausdorff and
> totally disconnected.

```lean
theorem isProfiniteSpacePropForm_connectedComponents
    (X : Type*) [TopologicalSpace X] [CompactSpace X]
    (h_clopen_inter : ∀ x : X,
      connectedComponent x = ⋂₀ {U : Set X | IsClopen U ∧ connectedComponent x ⊆ U}) :
    IsProfiniteSpacePropForm (ConnectedComponents X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.22, Tag 08ZW](https://stacks.math.columbia.edu/tag/08ZW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
