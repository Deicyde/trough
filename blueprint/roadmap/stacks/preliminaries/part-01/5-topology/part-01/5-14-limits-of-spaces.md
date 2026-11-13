---
declaration: section
origin: cited
lean: TopCat.topCat_hasLimits, TopCat.forget_preservesLimits, TopCat.exists_eq_iUnion_preimage_of_isOpen, TopCat.exists_isOpen_subset_preimage_subset_of_isCompact, TopCat.exists_isOpen_eq_preimage_of_isCompact_of_isOpen, TopCat.isLimit_of_basis_of_preimages, Pi.compactSpace, TopCat.compactSpace_of_isLimit
statement: formalized
proof: formalized
---

# 5.14 Limits of spaces

Section 5.14 of the Stacks Project, [Tag 08ZS](https://stacks.math.columbia.edu/tag/08ZS). 6 tags here are carried by 5 declarations of the repository (4 in StacksCore and 1 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08ZT, a lemma

[Tag 08ZT](https://stacks.math.columbia.edu/tag/08ZT) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.topCat_hasLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.topCat_hasLimits#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Limits/Defs.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Limits/Defs.lean#L24) (StacksFrontier): “the category of topological spaces has limits”.
- [`TopCat.forget_preservesLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.forget_preservesLimits#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Limits/Defs.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Limits/Defs.lean#L25) (StacksFrontier): “the forgetful functor to sets preserves limits”.

## Tag 0A2P, a lemma

[Tag 0A2P](https://stacks.math.columbia.edu/tag/0A2P) in the Stacks Project.

**`TopCat.exists_eq_iUnion_preimage_of_isOpen`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean#L120).

> **Stacks 0A2P** (part 1). Let `C` be a limit cone over a cofiltered diagram `F : J ⥤ TopCat`.
> Every open subset `W` of `C.pt` is `⋃ j, C.π.app j ⁻¹' U j` for open subsets `U j ⊆ F.obj j`.
>
> The tag takes the union over a subset of the index category. The whole index category always
> works, since `U j` may be empty.

```lean
theorem exists_eq_iUnion_preimage_of_isOpen (hC : IsLimit C) {W : Set C.pt} (hW : IsOpen W) :
    ∃ U : ∀ j, Set (F.obj j), (∀ j, IsOpen (U j)) ∧ W = ⋃ j, C.π.app j ⁻¹' U j
```

**`TopCat.exists_isOpen_subset_preimage_subset_of_isCompact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean#L132).

> **Stacks 0A2P** (part 2), general form. Let `C` be a limit cone over a cofiltered diagram
> `F : J ⥤ TopCat`. If `K` is a quasi-compact subset of an open subset `W` of `C.pt`, then
> `K ⊆ C.π.app i ⁻¹' U ⊆ W` for an index `i` and an open subset `U ⊆ F.obj i`.
>
> The tag's statement, `TopCat.exists_isOpen_eq_preimage_of_isCompact_of_isOpen`, is the case
> `K = W`.

```lean
theorem exists_isOpen_subset_preimage_subset_of_isCompact (hC : IsLimit C) {K W : Set C.pt}
    (hK : IsCompact K) (hW : IsOpen W) (hKW : K ⊆ W) :
    ∃ (i : J) (U : Set (F.obj i)), IsOpen U ∧ K ⊆ C.π.app i ⁻¹' U ∧ C.π.app i ⁻¹' U ⊆ W
```

**`TopCat.exists_isOpen_eq_preimage_of_isCompact_of_isOpen`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Category/TopCat/Limits/Cofiltered.lean#L147).

> **Stacks 0A2P** (part 2). Let `C` be a limit cone over a cofiltered diagram `F : J ⥤ TopCat`.
> Every quasi-compact open subset `W` of `C.pt` is `C.π.app i ⁻¹' U` for an index `i` and an open
> subset `U ⊆ F.obj i`.
>
> This is the case `K = W` of `TopCat.exists_isOpen_subset_preimage_subset_of_isCompact`.

```lean
theorem exists_isOpen_eq_preimage_of_isCompact_of_isOpen (hC : IsLimit C) {W : Set C.pt}
    (hWc : IsCompact W) (hWo : IsOpen W) :
    ∃ (i : J) (U : Set (F.obj i)), IsOpen U ∧ W = C.π.app i ⁻¹' U
```

## Tag 0A2Q, a lemma

[Tag 0A2Q](https://stacks.math.columbia.edu/tag/0A2Q) in the Stacks Project.

**`TopCat.isLimit_of_basis_of_preimages`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Limits/RecognizeCone.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Limits/RecognizeCone.lean#L37).

> **Stacks 0A2Q.** Let `J` be a cofiltered category, let `F : J ⥤ TopCat` be a diagram of
> topological spaces, and let `c` be a cone on `F`. Assume:
> 1. the underlying type-level cone `(forget).mapCone c` is a limit cone, so `c.pt` is the
>    set-theoretic limit with projections `c.π.app j`, and
> 2. the family of preimages `c.π.app j ⁻¹' V`, for `j : J` and `V` open in `F.obj j`, is a
>    topological basis for `c.pt`.
>
> Then `c` is a limit cone in `TopCat`.

```lean
theorem isLimit_of_basis_of_preimages
    {J : Type v} [Category.{w} J] [IsCofiltered J]
    {F : J ⥤ TopCat.{u}} (c : Cone F)
    (hForget : IsLimit ((CategoryTheory.forget TopCat.{u}).mapCone c))
    (hBasis : IsTopologicalBasis
      {U : Set c.pt | ∃ (j : J) (V : Set (F.obj j)), IsOpen V ∧ U = c.π.app j ⁻¹' V}) :
    Nonempty (IsLimit c)
```

## Tag 08ZU, a theorem

[Tag 08ZU](https://stacks.math.columbia.edu/tag/08ZU) in the Stacks Project.

Declarations registered for the tag:

- [`Pi.compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Pi.compactSpace#doc) registered with `add_to_stacks` in [StacksCore/Topology/Limits/Tychonoff.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Limits/Tychonoff.lean#L22) (StacksCore): “Tychonoff's theorem: a product of quasi-compact spaces is quasi-compact”.

## Tag 08ZV, a lemma

[Tag 08ZV](https://stacks.math.columbia.edu/tag/08ZV) in the Stacks Project.

**`TopCat.compactSpace_of_isLimit`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Limits/QuasiCompactHausdorff.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Limits/QuasiCompactHausdorff.lean#L61).

> **Stacks 08ZV.** Let `F : J ⥤ TopCat` be a diagram such that every `F.obj j` is quasi-compact
> (`CompactSpace`) and Hausdorff (`T2Space`). Then the point of any limit cone over `F` is
> quasi-compact.
>
> The index category `J : Type v` with `Category.{w} J` is arbitrary and need not be small.
> The instance `TopCat.compactSpace_limit` is the case of the chosen limit `limit F`. In the Stacks
> project the index category of a limit has a set of objects (Stacks 002G), which is the case
> `J : Type u` with `SmallCategory J`.

```lean
theorem compactSpace_of_isLimit
    {J : Type v} [Category.{w} J] (F : J ⥤ TopCat.{u})
    [∀ j, CompactSpace (F.obj j)] [∀ j, T2Space (F.obj j)]
    (c : Cone F) (hc : IsLimit c) : CompactSpace c.pt
```

## Tag 0A2R, a lemma

[Tag 0A2R](https://stacks.math.columbia.edu/tag/0A2R) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.nonempty_limitCone_of_compact_t2_cofiltered_system`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.nonempty_limitCone_of_compact_t2_cofiltered_system#doc) registered with `add_to_stacks` in [StacksCore/Topology/Limits/Nonempty.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Limits/Nonempty.lean#L20) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.14, Tag 08ZS](https://stacks.math.columbia.edu/tag/08ZS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
