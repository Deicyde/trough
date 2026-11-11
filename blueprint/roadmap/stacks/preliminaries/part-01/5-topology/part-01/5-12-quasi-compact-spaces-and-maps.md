---
declaration: section
origin: cited
lean: IsClosed.isCompact, IsCompact.isClosed, SeparatedNhds.of_isCompact_isCompact, CompactSpace.iInter_nonempty, IsSpectralMap.isRetrocompact_range, isCompact_range, IsClosed.exists_closed_singleton, isCompact_closedPoints
statement: formalized
proof: formalized
---

# 5.12 Quasi-compact spaces and maps

Section 5.12 of the Stacks Project, [Tag 0059](https://stacks.math.columbia.edu/tag/0059). 13 tags here are carried by 6 declarations of the repository (3 in StacksCore and 3 in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 005C, a lemma

[Tag 005C](https://stacks.math.columbia.edu/tag/005C) in the Stacks Project.

Declarations registered for the tag:

- [`IsClosed.isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosed.isCompact#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/ClosedSubsets.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ClosedSubsets.lean#L22) (StacksCore): “a closed subset of a quasi-compact space is quasi-compact”.

## Tag 08YB, a lemma

[Tag 08YB](https://stacks.math.columbia.edu/tag/08YB) in the Stacks Project.

Declarations registered for the tag:

- [`IsCompact.isClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCompact.isClosed#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/Hausdorff.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/Hausdorff.lean#L22) (StacksCore): “(1)”.
- [`SeparatedNhds.of_isCompact_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SeparatedNhds.of_isCompact_isCompact#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/Hausdorff.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/Hausdorff.lean#L23) (StacksCore): “(2)”. References: SGA 4 Vbis (4.1.4), “case A ∩ B = ∅”.

## Tag 08YC, a lemma

[Tag 08YC](https://stacks.math.columbia.edu/tag/08YC) in the Stacks Project.

Declarations registered for the tag:

- [`IsClosed.isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosed.isCompact#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/ClosedInHausdorff.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ClosedInHausdorff.lean#L20) (StacksCore): “a closed subset of a quasi-compact space is quasi-compact”.
- [`IsCompact.isClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCompact.isClosed#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/ClosedInHausdorff.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ClosedInHausdorff.lean#L21) (StacksCore): “a quasi-compact subset of a Hausdorff space is closed”.

## Tag 005D, a lemma

[Tag 005D](https://stacks.math.columbia.edu/tag/005D) in the Stacks Project.

Declarations registered for the tag:

- [`CompactSpace.iInter_nonempty`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CompactSpace.iInter_nonempty#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/FiniteIntersection.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/FiniteIntersection.lean#L20) (StacksCore): “the finite intersection property in a quasi-compact space”. References: EGA 0 (2.1.3), “partial”.

## Tag 04Z9, a lemma

[Tag 04Z9](https://stacks.math.columbia.edu/tag/04Z9) in the Stacks Project.

**`IsSpectralMap.isRetrocompact_range`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Compact/Image.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/Image.lean#L29). The attribute's comment: “part (2)”. References: EGA IV (1.2.7), “partial”.

> **Stacks 04Z9** (part 2). If `f : X → Y` is continuous and quasi-compact as a map, then its
> image `f(X)` is retrocompact in `Y`: it meets every quasi-compact open in a quasi-compact set.

```lean
theorem IsSpectralMap.isRetrocompact_range
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    {f : X → Y} (hf : IsSpectralMap f) :
    IsRetrocompact (Set.range f)
```

Declarations registered for the tag:

- [`isCompact_range`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCompact_range#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/Image.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/Image.lean#L24) (StacksCore): “(1)”.

## Tag 005E, a lemma

[Tag 005E](https://stacks.math.columbia.edu/tag/005E) in the Stacks Project.

Declarations registered for the tag:

- [`IsClosed.exists_closed_singleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosed.exists_closed_singleton#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/ClosedPoints.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ClosedPoints.lean#L20) (StacksCore): “the case of the whole space, which is closed and assumed nonempty”. References: EGA 0 (2.1.3), “partial”; EGA IV (5.1.11), “quasi-compact schemes”.

## Tag 08ZM, a lemma

[Tag 08ZM](https://stacks.math.columbia.edu/tag/08ZM) in the Stacks Project.

**`isCompact_closedPoints`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Compact/ClosedPointsKolmogorov.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ClosedPointsKolmogorov.lean#L29).

> **Stacks 08ZM.** Let `X` be a quasi-compact Kolmogorov (`T₀`) topological space. Then the set
> `closedPoints X` of closed points of `X` is quasi-compact.
>
> Every point specializes to a closed point in its closure, so compactness descends from `X` to
> `closedPoints X`.

```lean
theorem isCompact_closedPoints (X : Type*) [TopologicalSpace X] [CompactSpace X] [T0Space X] :
    IsCompact (closedPoints X)
```

## Tag 005F, a lemma

[Tag 005F](https://stacks.math.columbia.edu/tag/005F) in the Stacks Project.

**`connectedComponent_eq_iInter_isClopen_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/ClopenIntersection.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/ClopenIntersection.lean#L26).

> Let `X` be a topological space that is quasi-compact, admits a basis of quasi-compact open
> sets, and is such that the intersection of any two quasi-compact open sets is quasi-compact. Then
> for every `x : X` the connected component of `x` equals the intersection of all clopen subsets of
> `X` containing `x`.

```lean
theorem connectedComponent_eq_iInter_isClopen_of_compactSpace
    {X : Type u} [TopologicalSpace X] [CompactSpace X]
    {B : Set (Set X)} (hB : IsTopologicalBasis B)
    (hBqc : ∀ U ∈ B, IsCompact U)
    (hqcInter :
      ∀ ⦃U V : Set X⦄, IsOpen U → IsCompact U → IsOpen V → IsCompact V → IsCompact (U ∩ V))
    (x : X) :
    connectedComponent x = ⋂ Z : { Z : Set X // IsClopen Z ∧ x ∈ Z }, (Z : Set X)
```

## Tag 08ZN, a lemma

[Tag 08ZN](https://stacks.math.columbia.edu/tag/08ZN) in the Stacks Project.

Declarations registered for the tag:

- [`connectedComponent_eq_iInter_isClopen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=connectedComponent_eq_iInter_isClopen#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/ComponentsHausdorff.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/ComponentsHausdorff.lean#L22) (StacksCore): “the connected component is the intersection of the clopen neighbourhoods”.

## Tag 04PL, a lemma

[Tag 04PL](https://stacks.math.columbia.edu/tag/04PL) in the Stacks Project.

**`main_theorem04PL`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Connected/ClopenIntersectionCompact.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Connected/ClopenIntersectionCompact.lean#L97).

> **Stacks 04PL**.
> If `X` is quasi-compact, has a basis of quasi-compact opens, and the intersection of two
> quasi-compact opens is quasi-compact, then a subset `T ⊆ X` is an intersection of clopen
> subsets if and only if `T` is closed and is a union of connected components of `X`.

```lean
theorem main_theorem04PL
    [CompactSpace X]
    (hbasis : PrespectralSpace X)
    (hinter : QuasiSeparatedSpace X)
    (T : Set X) :
    IsIntersectionOfClopens T ↔ (IsClosed T ∧ IsUnionOfConnectedComponents T)
```

## Tag 04ZA, a lemma

[Tag 04ZA](https://stacks.math.columbia.edu/tag/04ZA) in the Stacks Project.

**`noetherianSpace_isRetrocompact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Noetherian/Retrocompact.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Noetherian/Retrocompact.lean#L29). The attribute's comment: “part (2)”. References: EGA IV (1.8.1), “special case”.

> **Stacks 04ZA** (part 2). Every subset of a Noetherian topological space is retrocompact:
> its intersection with any quasi-compact open is quasi-compact.

```lean
theorem noetherianSpace_isRetrocompact (X : Type*) [TopologicalSpace X]
    [TopologicalSpace.NoetherianSpace X] (E : Set X) : IsRetrocompact E
```

Declarations registered for the tag:

- [`TopologicalSpace.NoetherianSpace.compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.NoetherianSpace.compactSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Noetherian/Retrocompact.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Noetherian/Retrocompact.lean#L23) (StacksCore): “(1)”. References: EGA 0 (2.2.4), “first assertion”.

## Tag 04ZB, a lemma

[Tag 04ZB](https://stacks.math.columbia.edu/tag/04ZB) in the Stacks Project.

**`noetherianSpace_of_isLocallyNoetherianSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/QuasiCompactLocally.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Noetherian/QuasiCompactLocally.lean#L20).

> A quasi-compact locally Noetherian topological space is Noetherian.

```lean
theorem noetherianSpace_of_isLocallyNoetherianSpace (X : Type*) [TopologicalSpace X]
    [CompactSpace X] (hX : IsLocallyNoetherianSpace X) : NoetherianSpace X
```

## Tag 08ZP, a lemma

[Tag 08ZP](https://stacks.math.columbia.edu/tag/08ZP) in the Stacks Project.

Declarations registered for the tag:

- [`compactSpace_generateFrom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=compactSpace_generateFrom#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/AlexanderSubbase.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Compact/AlexanderSubbase.lean#L22) (StacksCore): “the Alexander subbase theorem”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.12, Tag 0059](https://stacks.math.columbia.edu/tag/0059)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
