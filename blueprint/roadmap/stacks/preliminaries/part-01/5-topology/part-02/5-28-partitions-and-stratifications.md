---
declaration: section
origin: cited
lean: IsTopologicalPartition, local_Refines, IsGoodStratification, Stratification, LocallyFinite, closedZ_of_locallyFiniteStratification, locallyFiniteStratification_of_closedZ, exists_finite_stratification_refining_finite_partition
statement: formalized
proof: formalized
---

# 5.28 Partitions and stratifications

Section 5.28 of the Stacks Project, [Tag 09XY](https://stacks.math.columbia.edu/tag/09XY). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09XZ, a definition

[Tag 09XZ](https://stacks.math.columbia.edu/tag/09XZ) in the Stacks Project.

**`IsTopologicalPartition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Partition.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/Partition.lean#L63).

> **Stacks 09XZ**.
> A *topological partition* of `X` is a set-theoretic partition of `X` all of whose
> parts are locally closed.

```lean
def IsTopologicalPartition (c : Set (Set X)) : Prop
```

**`local_Refines`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Partition.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/Partition.lean#L70).

> **Stacks 09XZ**.
> A collection `P` of subsets of `X` *refines* a collection `Q` when every member of
> `P` is contained in some member of `Q`.

```lean
def local_Refines (P Q : Set (Set X)) : Prop
```

## Tag 09Y0, a definition

[Tag 09Y0](https://stacks.math.columbia.edu/tag/09Y0) in the Stacks Project.

**`IsGoodStratification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Good.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/Good.lean#L66).

> **Stacks 09Y0**.
> A *good stratification* of a topological space `X`, indexed by `I`, is a
> family of subsets `S : I → Set X` which forms a partition (the sets are
> pairwise disjoint, each nonempty, and their union covers `X`) and which
> satisfies the frontier condition: if `S i ∩ closure (S j) ≠ ∅`, then
> `S i ⊆ closure (S j)`.

```lean
structure IsGoodStratification {X : Type*} [TopologicalSpace X] {I : Type*}
    (S : I → Set X) : Prop
```

## Tag 09Y1, a definition

[Tag 09Y1](https://stacks.math.columbia.edu/tag/09Y1) in the Stacks Project.

**`Stratification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/Defs.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/Defs.lean#L56).

> A *stratification* of a topological space `X`, indexed by a partially ordered type `I`, is an
> indexed family `strata : I → Set X` whose members are pairwise disjoint and cover `X` (a partition
> `X = ∐_{i} X_i`), and such that the closure of each stratum is contained in the union of the
> strata at lower or equal indices.

```lean
structure Stratification (X : Type*) [TopologicalSpace X]
    (I : Type*) [PartialOrder I]
```

## Tag 0BDS, a definition

[Tag 0BDS](https://stacks.math.columbia.edu/tag/0BDS) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyFinite#doc) registered with `add_to_stacks` in [StacksCore/Topology/Stratification/LocallyFiniteFamily.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Stratification/LocallyFiniteFamily.lean#L22) (StacksCore): “a locally finite collection of subsets”. References: EGA IV (3.1.6), “more general”; EGA IV (21.10.1), “partial”.

## Tag 09Y2, a remark

[Tag 09Y2](https://stacks.math.columbia.edu/tag/09Y2) in the Stacks Project.

**`closedZ_of_locallyFiniteStratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L156). The attribute's comment: “(1)”.

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

**`locallyFiniteStratification_of_closedZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/LocallyFinite.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/LocallyFinite.lean#L229). The attribute's comment: “(2)”.

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

**`exists_finite_stratification_refining_finite_partition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/RefinePartition.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/RefinePartition.lean#L337).

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

**`exists_finiteStratification_refining_constructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/RefineConstructible.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/RefineConstructible.lean#L449).

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

**`main_theorem09Y5`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Stratification/PartitionRefinement.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Stratification/PartitionRefinement.lean#L481).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
