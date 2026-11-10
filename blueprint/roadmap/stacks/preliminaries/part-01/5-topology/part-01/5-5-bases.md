---
declaration: section
origin: cited
lean: TopologicalSpace.IsTopologicalBasis, TopologicalSpace.isTopologicalBasis_of_isOpen_of_nhds, TopologicalSpace.IsTopologicalBasis.isOpen_iff, TopologicalSpace.isTopologicalBasis_generateFrom, TopologicalSpace.IsTopologicalBasis.eq_generateFrom, refine_open_cover_by_basis, TopologicalSpace.generateFrom, TopologicalSpace.isTopologicalBasis_of_subbasis
statement: formalized
proof: formalized
---

# 5.5 Bases

Section 5.5 of the Stacks Project, [Tag 004O](https://stacks.math.columbia.edu/tag/004O). 6 tags here are carried by 5 declarations of the repository (4 in StacksCore and 1 in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 004P, a definition

[Tag 004P](https://stacks.math.columbia.edu/tag/004P) in the Stacks Project.

Declarations registered for the tag:

- [`TopologicalSpace.IsTopologicalBasis`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.IsTopologicalBasis#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases.lean#L10) (StacksCore).
- [`TopologicalSpace.isTopologicalBasis_of_isOpen_of_nhds`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.isTopologicalBasis_of_isOpen_of_nhds#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases.lean#L11) (StacksCore).
- [`TopologicalSpace.IsTopologicalBasis.isOpen_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.IsTopologicalBasis.isOpen_iff#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases.lean#L12) (StacksCore). References: EGA 0 (3.2.4), “more general”.

## Tag 0D5P, a lemma

[Tag 0D5P](https://stacks.math.columbia.edu/tag/0D5P) in the Stacks Project.

**`TopologicalSpace.isTopologicalBasis_generateFrom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Bases/OfCollection.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases/OfCollection.lean#L37). The attribute's comment: “existence”.

> A collection `B` of subsets of `X` which covers `X` and which refines its own pairwise
> intersections is a topological basis for the topology it generates. The intersection condition
> requires that, for all `B₁, B₂ ∈ B` and `x ∈ B₁ ∩ B₂`, some `B₃ ∈ B` satisfies
> `x ∈ B₃` and `B₃ ⊆ B₁ ∩ B₂`.

```lean
theorem isTopologicalBasis_generateFrom {X : Type*} {B : Set (Set X)}
    (hcov : ⋃₀ B = univ)
    (hinter : ∀ B₁ ∈ B, ∀ B₂ ∈ B, ∀ x ∈ B₁ ∩ B₂, ∃ B₃ ∈ B, x ∈ B₃ ∧ B₃ ⊆ B₁ ∩ B₂) :
    @IsTopologicalBasis X (generateFrom B) B
```

Declarations registered for the tag:

- [`TopologicalSpace.IsTopologicalBasis.eq_generateFrom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.IsTopologicalBasis.eq_generateFrom#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases/OfCollection.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases/OfCollection.lean#L45) (StacksCore): “uniqueness”.

## Tag 004Q, a lemma

[Tag 004Q](https://stacks.math.columbia.edu/tag/004Q) in the Stacks Project.

**`refine_open_cover_by_basis`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Bases/RefineCover.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases/RefineCover.lean#L25).

> **Stacks 004Q.** A basis refines any open covering of an open set: given a topological basis
> `ℬ` of `X` and an open covering `𝓤` of an open `U ⊆ X`, the set `V` of basis elements contained in
> some `𝓤 i` satisfies `⋃₀ V = U`.

```lean
theorem refine_open_cover_by_basis
    {X : Type*} [TopologicalSpace X]
    {ℬ : Set (Set X)} (hℬ : TopologicalSpace.IsTopologicalBasis ℬ)
    {U : Set X}
    {I : Type*} (𝓤 : I → Set X) (h𝓤 : ∀ i, IsOpen (𝓤 i)) (hU : U = ⋃ i, 𝓤 i) :
    ∃ V : Set (Set X),
      V ⊆ ℬ ∧
      ⋃₀ V = U ∧
      ∀ v ∈ V, ∃ i, v ⊆ 𝓤 i
```

## Tag 08ZI, a definition

[Tag 08ZI](https://stacks.math.columbia.edu/tag/08ZI) in the Stacks Project.

Declarations registered for the tag:

- [`TopologicalSpace.generateFrom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.generateFrom#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases.lean#L14) (StacksCore).
- [`TopologicalSpace.isTopologicalBasis_of_subbasis`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopologicalSpace.isTopologicalBasis_of_subbasis#doc) registered with `add_to_stacks` in [StacksCore/Topology/Bases.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases.lean#L15) (StacksCore).

## Tag 08ZJ, a lemma

[Tag 08ZJ](https://stacks.math.columbia.edu/tag/08ZJ) in the Stacks Project.

**`TopologicalSpace.isTopologicalBasis_sInter_image_generateFrom`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Bases/Subbasis.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases/Subbasis.lean#L36). The attribute's comment: “existence”.

> The sets `⋂₀ f`, for `f` a finite subcollection of a collection `B` of subsets of `X`, form a
> topological basis for the topology generated by `B`.

```lean
theorem isTopologicalBasis_sInter_image_generateFrom {X : Type*} (B : Set (Set X)) :
    @IsTopologicalBasis X (generateFrom B)
      ((fun f => ⋂₀ f) '' { f : Set (Set X) | f.Finite ∧ f ⊆ B })
```

**`TopologicalSpace.eq_generateFrom_of_isTopologicalBasis_sInter_image`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Bases/Subbasis.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Bases/Subbasis.lean#L44). The attribute's comment: “uniqueness”.

> If the finite intersections of a collection `B` form a basis for a topology `t`, then `t`
> is the topology generated by `B`.

```lean
theorem eq_generateFrom_of_isTopologicalBasis_sInter_image {X : Type*}
    {t : TopologicalSpace X} {B : Set (Set X)}
    (hB : @IsTopologicalBasis X t
      ((fun f => ⋂₀ f) '' { f : Set (Set X) | f.Finite ∧ f ⊆ B })) :
    t = generateFrom B
```

## Tag 0D5Q, a lemma

[Tag 0D5Q](https://stacks.math.columbia.edu/tag/0D5Q) in the Stacks Project.

**`create_map_from_subcollection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Bases/QuotientRealizing.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Bases/QuotientRealizing.lean#L77).

> **Stacks 0D5Q.** Given a collection `B` of opens covering `X` such that every pairwise
> intersection of members of `B` is a union of members of `B` contained in it, there is a continuous
> map `f : X → Y` of topological spaces such that for `U ∈ B` the image `f '' U` is open,
> `f ⁻¹' (f '' U) = U`, and the opens `f '' U` form a basis for the topology on `Y`.

```lean
theorem create_map_from_subcollection {X : Type u} [TopologicalSpace X] (B : Set (Set X))
    (hB_open : ∀ U ∈ B, IsOpen U)
    (h_cover : ⋃₀ B = Set.univ)
    (h_inter : ∀ U ∈ B, ∀ V ∈ B, U ∩ V = ⋃₀ {W ∈ B | W ⊆ U ∩ V}) :
    ∃ (Y : Type u) (τ : TopologicalSpace Y) (f : X → Y),
      @Continuous X Y _ τ f ∧
      (∀ U ∈ B, @IsOpen Y τ (f '' U)) ∧
      (∀ U ∈ B, f ⁻¹' (f '' U) = U) ∧
      @TopologicalSpace.IsTopologicalBasis Y τ ((fun U => f '' U) '' B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.5, Tag 004O](https://stacks.math.columbia.edu/tag/004O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
