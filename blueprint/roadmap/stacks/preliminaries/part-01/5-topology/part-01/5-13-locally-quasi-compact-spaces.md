---
declaration: section
origin: cited
lean: LocallyCompactSpace, WeaklyLocallyCompactSpace.exists_compact_mem_nhds, WeaklyLocallyCompactSpace.locallyCompactSpace, BaireSpace.of_t2Space_locallyCompactSpace, dense_iInter_of_isOpen_nat, relatively_compact_refinement, exists_cover_closure_subset_and_refines, shrinking_open_covering
statement: formalized
proof: formalized
---

# 5.13 Locally quasi-compact spaces

Section 5.13 of the Stacks Project, [Tag 08ZQ](https://stacks.math.columbia.edu/tag/08ZQ). 7 tags here are carried by 4 declarations of the repository (1 in StacksCore and 3 in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0068, a definition

[Tag 0068](https://stacks.math.columbia.edu/tag/0068) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyCompactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyCompactSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/LocallyQuasiCompact.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/LocallyQuasiCompact.lean#L30) (StacksCore): “a locally quasi-compact space”.

## Tag 08ZR, a lemma

[Tag 08ZR](https://stacks.math.columbia.edu/tag/08ZR) in the Stacks Project.

Declarations registered for the tag:

- [`WeaklyLocallyCompactSpace.exists_compact_mem_nhds`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WeaklyLocallyCompactSpace.exists_compact_mem_nhds#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/LocallyHausdorff.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/LocallyHausdorff.lean#L21) (StacksCore): “every point of a locally quasi-compact space has a quasi-compact neighbourhood”.
- [`WeaklyLocallyCompactSpace.locallyCompactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=WeaklyLocallyCompactSpace.locallyCompactSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/LocallyHausdorff.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/LocallyHausdorff.lean#L23) (StacksCore): “conversely, an R₁ (in particular Hausdorff) space in which every point has a quasi-compact neighbourhood is locally quasi-compact”.

## Tag 0CQN, a lemma

[Tag 0CQN](https://stacks.math.columbia.edu/tag/0CQN) in the Stacks Project.

Declarations registered for the tag:

- [`BaireSpace.of_t2Space_locallyCompactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BaireSpace.of_t2Space_locallyCompactSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/Baire.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/Baire.lean#L23) (StacksCore): “a locally quasi-compact Hausdorff space is a Baire space”.
- [`dense_iInter_of_isOpen_nat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=dense_iInter_of_isOpen_nat#doc) registered with `add_to_stacks` in [StacksCore/Topology/Compact/Baire.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/Baire.lean#L25) (StacksCore): “a countable intersection of dense opens is dense”.

## Tag 09UV, a lemma

[Tag 09UV](https://stacks.math.columbia.edu/tag/09UV) in the Stacks Project.

**`relatively_compact_refinement`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Compact/ShrinkCover.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Compact/ShrinkCover.lean#L33).

> **Stacks 09UV.** Let `X` be a quasi-compact Hausdorff space and `U : I → Set X` an open cover.
> Then there is an open cover `V : I → Set X` with the same index set such that
> `closure (V i) ⊆ U i` for every `i`.
>
> A quasi-compact Hausdorff space is normal, so the shrinking lemma applies once the cover has been
> made point-finite: extract a finite subcover indexed by `J : Finset I` and replace `U i` by `∅`
> for `i ∉ J`.

```lean
theorem relatively_compact_refinement
    {X : Type*} [TopologicalSpace X] [T2Space X] [CompactSpace X]
    {I : Type*} (U : I → Set X) (hUopen : ∀ i, IsOpen (U i))
    (hUcov : ⋃ i, U i = Set.univ) :
    ∃ V : I → Set X, (∀ i, IsOpen (V i)) ∧ (⋃ i, V i = Set.univ) ∧
      (∀ i, closure (V i) ⊆ U i)
```

## Tag 09UW, a lemma

[Tag 09UW](https://stacks.math.columbia.edu/tag/09UW) in the Stacks Project.

**`exists_cover_closure_subset_and_refines`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/RefineCover.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/RefineCover.lean#L354).

> **Stacks 09UW**.
> Let `(U i)` be an open cover of a compact Hausdorff space `X` and let `(W i k)` be, for each
> `(p + 1)`-tuple `i` of indices, an open cover of `⋂ a, U (i a)`. Then `X` has an open cover
> `(V j)` together with a map `α` of index sets such that `closure (V j) ⊆ U (α j)` and, for
> every `(p + 1)`-tuple `j`, the intersection `⋂ a, V (j a)` is either empty or contained in
> some `W (α ∘ j) k`.
>
> The final clause is a disjunction because `K (α ∘ j)` may be empty; in that case
> `⋂ a, U (α (j a))` is empty by hypothesis, so no `k` exists, and `⋂ a, V (j a)` is empty
> too.

```lean
theorem exists_cover_closure_subset_and_refines
    {X : Type*} [TopologicalSpace X] [T2Space X] [CompactSpace X]
    {I : Type*}
    (U : I → Set X)
    (hUopen : ∀ i, IsOpen (U i))
    (hUcov : ⋃ i, U i = Set.univ)
    (p : ℕ)
    {K : (Fin (p + 1) → I) → Type*}
    (W : ∀ (i : Fin (p + 1) → I), K i → Set X)
    (hWopen : ∀ i k, IsOpen (W i k))
    (hWcov : ∀ i, (⋂ a, U (i a)) = ⋃ k, W i k) :
    ∃ (J : Type) (V : J → Set X) (α : J → I),
      (∀ j, IsOpen (V j)) ∧
      (⋃ j, V j = Set.univ) ∧
      (∀ j, closure (V j) ⊆ U (α j)) ∧
      (∀ (j : Fin (p + 1) → J),
        (⋂ a, V (j a)) = ∅ ∨
          ∃ k : K (fun a => α (j a)), (⋂ a, V (j a)) ⊆ W (fun a => α (j a)) k)
```

## Tag 09UX, a lemma

[Tag 09UX](https://stacks.math.columbia.edu/tag/09UX) in the Stacks Project.

**`shrinking_open_covering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/ShrinkCoverSubset.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/ShrinkCoverSubset.lean#L284).

> Stacks Project, Tag 09UX (Shrinking an open covering).
>
> Let `X` be a Hausdorff and locally quasi-compact (in the Stacks Project sense,
> i.e. weakly locally compact) topological space.  Let `Z ⊆ X` be a compact
> subset.  Given an open cover `U : I → Set X` of `Z`, and for each
> `(p+1)`-tuple `σ : Fin (p+1) → I` an open subset
> `W σ ⊆ ⋂ k, U (σ k)` satisfying
> `W σ ∩ Z = (⋂ k, U (σ k)) ∩ Z`, there exist open subsets `V : I → Set X`
> with `Z ⊆ ⋃ i, V i`, `closure (V i) ⊆ U i` for every `i`, and
> `⋂ k, V (σ k) ⊆ W σ` for every `(p+1)`-tuple `σ`.

```lean
theorem shrinking_open_covering
    {X : Type*} [TopologicalSpace X] [T2Space X] [WeaklyLocallyCompactSpace X]
    {Z : Set X} (hZ : IsCompact Z)
    {p : ℕ} {I : Type*}
    (U : I → Set X) (hU : ∀ i, IsOpen (U i))
    (W : (Fin (p + 1) → I) → Set X) (hW : ∀ σ, IsOpen (W σ))
    (hcov : Z ⊆ ⋃ i, U i)
    (hint : ∀ σ, W σ ∩ Z = (⋂ k, U (σ k)) ∩ Z) :
    ∃ V : I → Set X,
      (∀ i, IsOpen (V i)) ∧
      Z ⊆ ⋃ i, V i ∧
      (∀ i, closure (V i) ⊆ U i) ∧
      (∀ σ : Fin (p + 1) → I, ⋂ k, V (σ k) ⊆ W σ)
```

## Tag 0CY5, a lemma

[Tag 0CY5](https://stacks.math.columbia.edu/tag/0CY5) in the Stacks Project.

**`TopologicalSpace.exists_isOpen_refinement_of_isCompact_of_pairwiseSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Compact/ShrinkingCover.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Compact/ShrinkingCover.lean#L299).

> **Stacks 0CY5.** Let `Z` be a quasi-compact subset of a topological space `X` whose
> distinct points can be separated by disjoint opens of `X`, let `U : I → Set X` be an open
> cover of `Z`, and for each `(p+1)`-tuple `σ` of indices let `W σ` be an open set contained in
> `⋂ k, U (σ k)` and agreeing with it on `Z`. Then `Z` has an open cover `V : I → Set X` with
> `V i ⊆ U i`, with `closure (V i) ∩ Z ⊆ U i`, and with `⋂ k, V (σ k) ⊆ W σ` for every `σ`.
>
> The reduction to the finite case is by extracting a finite subcover of `Z` and extending the
> resulting family by `∅` outside it.

```lean
theorem exists_isOpen_refinement_of_isCompact_of_pairwiseSeparated
    {X : Type*} [TopologicalSpace X]
    (Z : Set X) (hZ : IsCompact Z)
    (hSep : ∀ x ∈ Z, ∀ y ∈ Z, x ≠ y →
      ∃ A B : Set X, IsOpen A ∧ IsOpen B ∧ x ∈ A ∧ y ∈ B ∧ Disjoint A B)
    (p : ℕ) (I : Type*)
    (U : I → Set X) (hU : ∀ i, IsOpen (U i))
    (W : (Fin (p + 1) → I) → Set X) (hW : ∀ σ, IsOpen (W σ))
    (hCover : Z ⊆ ⋃ i, U i)
    (hWinter : ∀ σ, W σ ∩ Z = (⋂ k, U (σ k)) ∩ Z) :
    ∃ V : I → Set X,
      (∀ i, IsOpen (V i)) ∧
      (Z ⊆ ⋃ i, V i) ∧
      (∀ i, V i ⊆ U i) ∧
      (∀ i, closure (V i) ∩ Z ⊆ U i) ∧
      (∀ σ : Fin (p + 1) → I, ⋂ k, V (σ k) ⊆ W σ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.13, Tag 08ZQ](https://stacks.math.columbia.edu/tag/08ZQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
