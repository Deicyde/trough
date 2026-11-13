---
declaration: section
origin: cited
lean: ExtremallyDisconnected, ExtremallyDisconnected.open_closure, image_subset_closure_compl_image_compl_of_isOpen, ExtremallyDisconnected.disjoint_closure_of_disjoint_isOpen, ExtremallyDisconnected.homeoCompactToT2, exists_compact_surjective_zorn_subset, extremallyDisconnected_tfae, rainwater_lemma
statement: formalized
proof: formalized
---

# 5.26 Extremally disconnected spaces

Section 5.26 of the Stacks Project, [Tag 08YH](https://stacks.math.columbia.edu/tag/08YH). 10 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08YI, a definition

[Tag 08YI](https://stacks.math.columbia.edu/tag/08YI) in the Stacks Project.

Declarations registered for the tag:

- [`ExtremallyDisconnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ExtremallyDisconnected#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/Defs.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/Defs.lean#L20) (StacksCore): “extremally disconnected spaces”.
- [`ExtremallyDisconnected.open_closure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ExtremallyDisconnected.open_closure#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/Defs.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/Defs.lean#L21) (StacksCore): “the closure of every open subset is open”.

## Tag 08YJ, a lemma

[Tag 08YJ](https://stacks.math.columbia.edu/tag/08YJ) in the Stacks Project.

Declarations registered for the tag:

- [`image_subset_closure_compl_image_compl_of_isOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=image_subset_closure_compl_image_compl_of_isOpen#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/OpenImage.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/OpenImage.lean#L21) (StacksCore): “images of opens under a map that is onto no proper closed subset”.

## Tag 08YK, a lemma

[Tag 08YK](https://stacks.math.columbia.edu/tag/08YK) in the Stacks Project.

Declarations registered for the tag:

- [`ExtremallyDisconnected.disjoint_closure_of_disjoint_isOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ExtremallyDisconnected.disjoint_closure_of_disjoint_isOpen#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/DisjointClosures.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/DisjointClosures.lean#L19) (StacksCore): “disjoint open subsets of an extremally disconnected space have disjoint closures”.

## Tag 08YL, a lemma

[Tag 08YL](https://stacks.math.columbia.edu/tag/08YL) in the Stacks Project.

Declarations registered for the tag:

- [`ExtremallyDisconnected.homeoCompactToT2`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ExtremallyDisconnected.homeoCompactToT2#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/Surjection.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/Surjection.lean#L20) (StacksCore).

## Tag 08YM, a lemma

[Tag 08YM](https://stacks.math.columbia.edu/tag/08YM) in the Stacks Project.

Declarations registered for the tag:

- [`exists_compact_surjective_zorn_subset`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=exists_compact_surjective_zorn_subset#doc) registered with `add_to_stacks` in [StacksCore/Topology/ExtremallyDisconnected/MinimalSubset.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/ExtremallyDisconnected/MinimalSubset.lean#L24) (StacksCore): “a minimal quasi-compact subset that still surjects”.

## Tag 08YN, a proposition

[Tag 08YN](https://stacks.math.columbia.edu/tag/08YN) in the Stacks Project.

**`extremallyDisconnected_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/Characterization.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/Characterization.lean#L70).

> For a quasi-compact Hausdorff space `X` the following are equivalent: `X` is extremally
> disconnected; every continuous surjection onto `X` from a quasi-compact Hausdorff space has a
> continuous section; `X` is projective among quasi-compact Hausdorff spaces, which is Mathlib's
> `CompactT2.Projective`.

```lean
theorem extremallyDisconnected_tfae (X : Type u) [TopologicalSpace X] [CompactSpace X] [T2Space X] :
    List.TFAE
      [ ExtremallyDisconnected X,
        HasContinuousSectionFromCompactT2 X,
        CompactT2.Projective X ]
```

## Tag 090B, a lemma

[Tag 090B](https://stacks.math.columbia.edu/tag/090B) in the Stacks Project.

**`rainwater_lemma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/Rainwater.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/Rainwater.lean#L49).

> **Stacks 090B** (Rainwater's lemma). Let `f : X → X` be a surjective
> continuous selfmap of a Hausdorff topological space. If `f` is not `id_X`, then
> there exists a proper closed subset `E ⊂ X` such that `X = E ∪ f(E)`.

```lean
theorem rainwater_lemma
    {X : Type*} [TopologicalSpace X] [T2Space X]
    (f : X → X) (hf_cont : Continuous f) (hf_surj : Function.Surjective f)
    (hf_ne_id : f ≠ id) :
    ∃ E : Set X, IsClosed E ∧ E ≠ Set.univ ∧ Set.univ = E ∪ f '' E
```

## Tag 090C, an example

[Tag 090C](https://stacks.math.columbia.edu/tag/090C) in the Stacks Project.

**`stoneCech_extremallyDisconnected_of_discrete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/StoneCech.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/StoneCech.lean#L59).

> **Stacks 090C.** The Stone–Čech compactification of a discrete topological space is
> extremally disconnected.

```lean
theorem stoneCech_extremallyDisconnected_of_discrete
    (X : Type*) [TopologicalSpace X] [DiscreteTopology X] :
    ExtremallyDisconnected (StoneCech X)
```

**`stoneCech_totallyDisconnected_of_discrete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/StoneCech.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/StoneCech.lean#L67).

> **Stacks 090C.** The Stone–Čech compactification of a discrete topological space is totally
> disconnected.

```lean
theorem stoneCech_totallyDisconnected_of_discrete
    (X : Type*) [TopologicalSpace X] [DiscreteTopology X] :
    TotallyDisconnectedSpace (StoneCech X)
```

## Tag 090D, a lemma

[Tag 090D](https://stacks.math.columbia.edu/tag/090D) in the Stacks Project.

**`exists_extremallyDisconnected_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/Cover.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/Cover.lean#L92). The attribute's comment: “first statement: some extremally disconnected cover, β(X\_disc) → X; not the minimal one”.

> **Stacks 090D, first statement.** Every compact Hausdorff space `X` admits a
> continuous surjection from a compact Hausdorff extremally disconnected space, namely
> `β(X_disc) = Ultrafilter X → X`. This cover is in general not minimal; the minimal cover of
> 090D, which `minimal_cover_unique` shows is unique, is
> `exists_minimal_extremallyDisconnected_cover`.

```lean
theorem exists_extremallyDisconnected_cover
    (X : Type u) [TopologicalSpace X] [CompactSpace X] [T2Space X] :
    ∃ (X' : Type u) (_ : TopologicalSpace X') (_ : CompactSpace X')
        (_ : T2Space X') (_ : ExtremallyDisconnected X')
        (π : X' → X), Continuous π ∧ Function.Surjective π
```

**`minimal_cover_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/Cover.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/Cover.lean#L112).

> **Stacks 090D, uniqueness half.** If `π' : X' → X` and `π'' : X'' → X` are
> two minimal extremally disconnected covers of a compact Hausdorff space `X`,
> then there is a homeomorphism `X' ≃ₜ X''` lying over `X`.
>
> Here "minimal" means: no proper closed subset surjects onto `X`.

```lean
theorem minimal_cover_unique
    {X X' X'' : Type u}
    [TopologicalSpace X] [CompactSpace X] [T2Space X]
    [TopologicalSpace X'] [CompactSpace X'] [T2Space X'] [ExtremallyDisconnected X']
    [TopologicalSpace X''] [CompactSpace X''] [T2Space X''] [ExtremallyDisconnected X'']
    {π' : X' → X} (π'_cont : Continuous π') (π'_surj : Function.Surjective π')
    (π'_min : ∀ E : Set X', IsClosed E → E ≠ univ → π' '' E ≠ univ)
    {π'' : X'' → X} (π''_cont : Continuous π'') (π''_surj : Function.Surjective π'')
    (π''_min : ∀ E : Set X'', IsClosed E → E ≠ univ → π'' '' E ≠ univ) :
    ∃ φ : X' ≃ₜ X'', π'' ∘ φ = π'
```

**`exists_minimal_extremallyDisconnected_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/MinimalCover.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/MinimalCover.lean#L93). The attribute's comment: “existence of a minimal cover: the minimal closed E ⊆ β(X\_disc) mapping onto X is extremally disconnected”.

> **Stacks 090D, the minimal cover.** Let `X` be a quasi-compact Hausdorff space and let
> `π : β(X_disc) → X` be the extension of the identity of `X`, where `β(X_disc) = Ultrafilter X` is
> the Stone–Čech compactification of `X` with the discrete topology. There is a closed subset
> `E ⊆ β(X_disc)` with `π(E) = X` such that no proper closed subset of `E` maps onto `X`, and this
> `E` is extremally disconnected; thus `π|_E : E → X` is a continuous surjection
> from a quasi-compact Hausdorff extremally disconnected space, minimal in the sense of 090D.

```lean
theorem exists_minimal_extremallyDisconnected_cover
    (X : Type u) [TopologicalSpace X] [CompactSpace X] [T2Space X] :
    ∃ E : Set (Ultrafilter X), IsClosed E ∧ Ultrafilter.extend (id : X → X) '' E = univ ∧
      (∀ E' ⊆ E, IsClosed E' → Ultrafilter.extend (id : X → X) '' E' = univ → E' = E) ∧
      ExtremallyDisconnected E
```

**`exists_minimal_extremallyDisconnected_cover_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/MinimalCover.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/MinimalCover.lean#L113). The attribute's comment: “existence of a minimal cover, as a space X' → X”.

> **Stacks 090D, the minimal cover as a space.** Every quasi-compact Hausdorff space `X` admits
> a continuous surjection `π : X' → X` from a quasi-compact Hausdorff extremally disconnected space
> `X'` such that no proper closed subset of `X'` maps onto `X`. This is the minimality hypothesis of
> `minimal_cover_unique`, which makes `X'` unique up to homeomorphism over `X`.

```lean
theorem exists_minimal_extremallyDisconnected_cover_space
    (X : Type u) [TopologicalSpace X] [CompactSpace X] [T2Space X] :
    ∃ (X' : Type u) (_ : TopologicalSpace X') (_ : CompactSpace X')
        (_ : T2Space X') (_ : ExtremallyDisconnected X')
        (π : X' → X), Continuous π ∧ Surjective π ∧
          ∀ E : Set X', IsClosed E → E ≠ univ → π '' E ≠ univ
```

## Tag 090E, a remark

[Tag 090E](https://stacks.math.columbia.edu/tag/090E) in the Stacks Project.

**`minimal_cover_card_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/ExtremallyDisconnected/CoverCardinality.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/ExtremallyDisconnected/CoverCardinality.lean#L58).

> **Stacks 090E.** Let `X` be a quasi-compact Hausdorff space and let `π : X' → X` be a minimal
> quasi-compact Hausdorff extremally disconnected cover of `X`, minimality meaning that no proper
> closed subset of `X'` surjects onto `X`. If `#X ≤ κ` then `#X' ≤ 2 ^ (2 ^ κ)`.
>
> The infiniteness hypothesis `_hκ` on `κ` is present only to match the source; it is not used.

```lean
theorem minimal_cover_card_le
    {X X' : Type u}
    [TopologicalSpace X] [CompactSpace X] [T2Space X]
    [TopologicalSpace X'] [CompactSpace X'] [T2Space X'] [ExtremallyDisconnected X']
    {π : X' → X} (π_surj : Function.Surjective π)
    (π_min : ∀ E : Set X', IsClosed E → E ≠ univ → π '' E ≠ univ)
    {κ : Cardinal.{u}} (_hκ : Cardinal.aleph0 ≤ κ) (hX : Cardinal.mk X ≤ κ) :
    Cardinal.mk X' ≤ (2 : Cardinal.{u}) ^ ((2 : Cardinal.{u}) ^ κ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.26, Tag 08YH](https://stacks.math.columbia.edu/tag/08YH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
