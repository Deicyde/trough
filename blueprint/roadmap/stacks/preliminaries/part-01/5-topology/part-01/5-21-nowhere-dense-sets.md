---
declaration: section
origin: cited
lean: interior, IsNowhereDense, StacksLemmaCompactSubsetSpectral, IsNowhereDense.image_val, nowhere_dense_local, Topology.IsInducing.isNowhereDense_image, isClosedNowhereDense_preimage_of_isOpenMap, isClosedNowhereDense_preimage_iff_of_surjective_isOpenMap
statement: formalized
proof: formalized
---

# 5.21 Nowhere dense sets

Section 5.21 of the Stacks Project, [Tag 03HM](https://stacks.math.columbia.edu/tag/03HM). 6 tags here are carried by 4 declarations of the repository (3 in StacksCore and 1 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03HN, a definition

[Tag 03HN](https://stacks.math.columbia.edu/tag/03HN) in the Stacks Project.

Declarations registered for the tag:

- [`interior`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=interior#doc) registered with `add_to_stacks` in [StacksCore/Topology/NowhereDense/Defs.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/Defs.lean#L24) (StacksCore): “the interior of a subset”.
- [`IsNowhereDense`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsNowhereDense#doc) registered with `add_to_stacks` in [StacksCore/Topology/NowhereDense/Defs.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/Defs.lean#L25) (StacksCore): “a nowhere dense subset”.

## Tag 03HO, a lemma

[Tag 03HO](https://stacks.math.columbia.edu/tag/03HO) in the Stacks Project.

**`StacksLemmaCompactSubsetSpectral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/NowhereDense/FiniteUnion.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/NowhereDense/FiniteUnion.lean#L92).

> **Stacks 03HO**. The union of a finite collection of nowhere dense subsets of a topological
> space is nowhere dense, stated for a binary union, for a `Finset`-indexed family, and for the
> union of a `Set.Finite` family of subsets.

```lean
theorem StacksLemmaCompactSubsetSpectral :
    (∀ {X : Type*} [TopologicalSpace X] {A B : Set X},
        IsNowhereDense A → IsNowhereDense B → IsNowhereDense (A ∪ B)) ∧
    (∀ {X : Type*} [TopologicalSpace X] {ι : Type*} (s : Finset ι) (A : ι → Set X),
        (∀ i ∈ s, IsNowhereDense (A i)) → IsNowhereDense (⋃ i ∈ s, A i)) ∧
    (∀ {X : Type*} [TopologicalSpace X] {S : Set (Set X)},
        S.Finite → (∀ A ∈ S, IsNowhereDense A) → IsNowhereDense (⋃₀ S))
```

## Tag 03J0, a lemma

[Tag 03J0](https://stacks.math.columbia.edu/tag/03J0) in the Stacks Project.

Declarations registered for the tag:

- [`IsNowhereDense.image_val`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsNowhereDense.image_val#doc) registered with `add_to_stacks` in [StacksCore/Topology/NowhereDense/Subspace.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/Subspace.lean#L20) (StacksCore): “nowhere dense subsets of a subspace”.

## Tag 03HP, a lemma

[Tag 03HP](https://stacks.math.columbia.edu/tag/03HP) in the Stacks Project.

**`nowhere_dense_local`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/NowhereDense/Local.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/Local.lean#L29).

> **Stacks 03HP.** Nowhere density is local on open covers: if `{U i}` is an open cover of `X`
> and `T ∩ U i` (encoded as the preimage of `T` under the inclusion `U i → X`) is nowhere dense in
> the subspace `U i` for every `i`, then `T` is nowhere dense in `X`.

```lean
theorem nowhere_dense_local
    {X : Type*} [TopologicalSpace X]
    {ι : Type*} (U : ι → Set X)
    (hU_open : ∀ i, IsOpen (U i))
    (hU_cover : ⋃ i, U i = Set.univ)
    (T : Set X)
    (hT_local : ∀ i, IsNowhereDense ((Subtype.val : U i → X) ⁻¹' T)) :
    IsNowhereDense T
```

## Tag 03HQ, a lemma

[Tag 03HQ](https://stacks.math.columbia.edu/tag/03HQ) in the Stacks Project.

Declarations registered for the tag:

- [`Topology.IsInducing.isNowhereDense_image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsInducing.isNowhereDense_image#doc) registered with `add_to_stacks` in [StacksCore/Topology/NowhereDense/ClosedEmbedding.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/ClosedEmbedding.lean#L20) (StacksCore): “for an inducing map”.

## Tag 03HR, a lemma

[Tag 03HR](https://stacks.math.columbia.edu/tag/03HR) in the Stacks Project.

**`isClosedNowhereDense_preimage_of_isOpenMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/NowhereDense/OpenMap.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/OpenMap.lean#L32). The attribute's comment: “(1)”.

> **Stacks 03HR** (part 1). If `f : X → Y` is a continuous open map and `T ⊆ Y` is closed
> nowhere dense, then `f⁻¹(T)` is closed nowhere dense in `X`.

```lean
theorem isClosedNowhereDense_preimage_of_isOpenMap
    (f : X → Y) (hfc : Continuous f) (hfo : IsOpenMap f)
    (T : Set Y) (hT_closed : IsClosed T) (hT : IsNowhereDense T) :
    IsClosed (f ⁻¹' T) ∧ IsNowhereDense (f ⁻¹' T)
```

**`isClosedNowhereDense_preimage_iff_of_surjective_isOpenMap`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/NowhereDense/OpenMap.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/NowhereDense/OpenMap.lean#L44). The attribute's comment: “(2)”.

> **Stacks 03HR** (part 2). If `f : X → Y` is a surjective continuous open map, then `T ⊆ Y` is
> closed nowhere dense if and only if `f⁻¹(T)` is closed nowhere dense in `X`.

```lean
theorem isClosedNowhereDense_preimage_iff_of_surjective_isOpenMap
    (f : X → Y) (hfc : Continuous f) (hfo : IsOpenMap f) (hfs : Function.Surjective f)
    (T : Set Y) :
    (IsClosed T ∧ IsNowhereDense T) ↔
      (IsClosed (f ⁻¹' T) ∧ IsNowhereDense (f ⁻¹' T))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.21, Tag 03HM](https://stacks.math.columbia.edu/tag/03HM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
