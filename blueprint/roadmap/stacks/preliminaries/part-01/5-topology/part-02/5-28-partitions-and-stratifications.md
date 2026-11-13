---
declaration: section
origin: cited
lean: IsTopologicalPartition, local_Refines, IsGoodPartition, IsStratification, LocallyFinite, closedZ_of_locallyFiniteStratification, locallyFiniteStratification_of_closedZ, exists_finite_stratification_refining_finite_partition
statement: formalized
proof: formalized
---

# 5.28 Partitions and stratifications

Section 5.28 of the Stacks Project, [Tag 09XY](https://stacks.math.columbia.edu/tag/09XY). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09XZ, a definition

[Tag 09XZ](https://stacks.math.columbia.edu/tag/09XZ) in the Stacks Project.

**`IsTopologicalPartition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Partition.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/Partition.lean#L63).

> **Stacks 09XZ**.
> A *topological partition* of `X` is a set-theoretic partition of `X` all of whose
> parts are locally closed.

```lean
def IsTopologicalPartition (c : Set (Set X)) : Prop
```

**`local_Refines`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Partition.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/Partition.lean#L70).

> **Stacks 09XZ**.
> A collection `P` of subsets of `X` *refines* a collection `Q` when every member of
> `P` is contained in some member of `Q`.

```lean
def local_Refines (P Q : Set (Set X)) : Prop
```

## Tag 09Y0, a definition

[Tag 09Y0](https://stacks.math.columbia.edu/tag/09Y0) in the Stacks Project.

**`IsGoodPartition`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L82).

> **Stacks 09Y0**.
> A *good stratification* of the topological space `α` is a partition `X : I → Set α` of `α`
> (into pairwise disjoint locally closed parts covering `α`) such that for all `i, j` with
> `X i ∩ closure (X j) ≠ ∅` we have `X i ⊆ closure (X j)`.

```lean
structure IsGoodPartition (X : I → Set α) : Prop
```

## Tag 09Y1, a definition

[Tag 09Y1](https://stacks.math.columbia.edu/tag/09Y1) in the Stacks Project.

**`IsStratification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L103).

> **Stacks 09Y1**.
> A family `X : I → Set α`, with `I` a partially ordered set, is a
> *stratification* if it is a partition and for every `j` the closure of `X j` is
> contained in `⋃ (i ≤ j) X i`. The parts `X i` are the *strata*.

```lean
structure IsStratification [PartialOrder I] (X : I → Set α) : Prop
```

## Tag 0BDS, a definition

[Tag 0BDS](https://stacks.math.columbia.edu/tag/0BDS) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyFinite#doc) registered with `add_to_stacks` in [StacksCore/Topology/Stratification/LocallyFiniteFamily.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Topology/Stratification/LocallyFiniteFamily.lean#L22) (StacksCore): “a locally finite collection of subsets”. References: EGA IV (3.1.6), “more general”; EGA IV (21.10.1), “partial”.

## Tag 09Y2, a remark

[Tag 09Y2](https://stacks.math.columbia.edu/tag/09Y2) in the Stacks Project.

**`closedZ_of_locallyFiniteStratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L181). The attribute's comment: “(1)”.

> **Stacks 09Y2** (1).
> Let `X` be a locally finite stratification of `α` with partial order `≤` on `I`,
> and for each `i` let `Z i = ⋃ (j ≤ i) X j`. Then each `Z i` is closed, and for
> all `i, j` one has `Z i ∩ Z j = ⋃ (k ≤ i ∧ k ≤ j) Z k`.

```lean
theorem closedZ_of_locallyFiniteStratification [PartialOrder I] {X : I → Set α}
    (h : IsLocallyFiniteStratification X)
    (Z : I → Set α) (hZ : ∀ i, Z i = ⋃ j ∈ {j | j ≤ i}, X j) :
    (∀ i, IsClosed (Z i)) ∧
    (∀ i j, Z i ∩ Z j = ⋃ k ∈ {k | k ≤ i ∧ k ≤ j}, Z k)
```

**`locallyFiniteStratification_of_closedZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L254). The attribute's comment: “(2)”.

> **Stacks 09Y2** (2).
> Let `I` be a partially ordered set and `{Z i}` a family of closed subsets of `α`
> that cover `α`, are locally finite, and satisfy
> `Z i ∩ Z j = ⋃ (k ≤ i ∧ k ≤ j) Z k`. Then the sets `X i = Z i \ ⋃ (j < i) Z j`,
> with the partial order `≤` on `I`, form a locally finite stratification of
> `α`.

```lean
theorem locallyFiniteStratification_of_closedZ [PartialOrder I] {Z : I → Set α}
    (hclosed : ∀ i, IsClosed (Z i))
    (hcover : ⋃ i, Z i = Set.univ)
    (hlf : LocallyFinite Z)
    (hint : ∀ i j, Z i ∩ Z j = ⋃ k ∈ {k | k ≤ i ∧ k ≤ j}, Z k)
    (X : I → Set α) (hX : ∀ i, X i = Z i \ ⋃ j ∈ {j | j < i}, Z j) :
    IsLocallyFiniteStratification X
```

## Tag 09Y3, a lemma

[Tag 09Y3](https://stacks.math.columbia.edu/tag/09Y3) in the Stacks Project.

**`exists_finite_stratification_refining_finite_partition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/RefinePartition.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/RefinePartition.lean#L337).

> **Stacks 09Y3**.
> Every finite partition of a topological space by locally closed subsets is refined
> by a finite stratification.

```lean
theorem exists_finite_stratification_refining_finite_partition
    {X : Type*} [TopologicalSpace X] {ι : Type*} [Finite ι] (P : TopPartition X ι) :
    ∃ (κ : Type) (_ : Finite κ) (_ : PartialOrder κ) (S : TopStratification X κ),
      S.toTopPartition.Refines P
```

## Tag 09Y4, a lemma

[Tag 09Y4](https://stacks.math.columbia.edu/tag/09Y4) in the Stacks Project.

**`exists_finiteStratification_refining_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/RefineConstructible.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/RefineConstructible.lean#L449).

> **Stacks 09Y4**.
> If a topological space `X` is covered by a finite family `T₁, …, Tₙ` of
> constructible subsets, then there exists a finite stratification `X = ⨆ Xᵢ` such
> that each stratum is constructible and each `Tₖ` is a union of strata.

```lean
theorem exists_finiteStratification_refining_constructible
    {n : ℕ} (T : Fin n → Set X)
    (hT : ∀ k, Topology.IsConstructible (T k))
    (_hcover : ⋃ k, T k = Set.univ) :
    ∃ (𝒮 : FiniteStratification X),
      (∀ i, Topology.IsConstructible (𝒮.S i)) ∧
      (∀ k, ∃ I : Set 𝒮.ι, T k = ⋃ i ∈ I, 𝒮.S i)
```

## Tag 09Y5, a lemma

[Tag 09Y5](https://stacks.math.columbia.edu/tag/09Y5) in the Stacks Project.

**`main_theorem09Y5`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/PartitionRefinement.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Stratification/PartitionRefinement.lean#L481).

> Let `X` be a Noetherian topological space. Any finite partition of `X` can be refined by a
> finite good stratification of `X`.

```lean
theorem main_theorem09Y5 (X : Type u) [TopologicalSpace X]
    [TopologicalSpace.NoetherianSpace X]
    (P : TopPartitionOpenCover.{u, v} X) (hP : P.IsFinite) :
    ∃ P' : TopPartitionOpenCover.{u, u} X,
      P'.IsFinite ∧ P'.IsGood ∧ P'.Refines P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.28, Tag 09XY](https://stacks.math.columbia.edu/tag/09XY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
