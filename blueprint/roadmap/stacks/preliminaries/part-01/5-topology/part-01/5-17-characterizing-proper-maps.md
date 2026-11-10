---
declaration: section
origin: cited
lean: generalized_tube_lemma, StacksDraft.Topology.IsBourbakiProperMap, StacksDraft.Topology.IsQuasiProperMap, StacksDraft.Topology.IsUniversallyClosedMap, StacksDraft.Topology.IsProperMap, IsClosedMap, compactSpace_iff_forall_isClosedMap_fst, compactSpace_iff_isClosedMap_fst
statement: formalized
proof: formalized
---

# 5.17 Characterizing proper maps

Section 5.17 of the Stacks Project, [Tag 005M](https://stacks.math.columbia.edu/tag/005M). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 005N, a lemma

[Tag 005N](https://stacks.math.columbia.edu/tag/005N) in the Stacks Project.

Declarations registered for the tag:

- [`generalized_tube_lemma`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=generalized_tube_lemma#doc) registered with `add_to_stacks` in [StacksCore/Topology/Proper/TubeLemma.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Proper/TubeLemma.lean#L21) (StacksCore): “the tube lemma for a product of two quasi-compact subsets”.

## Tag 005O, a definition

[Tag 005O](https://stacks.math.columbia.edu/tag/005O) in the Stacks Project.

**`StacksDraft.Topology.IsBourbakiProperMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/Proper.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L53). The attribute's comment: “(2)”.

> **Stacks 005O (2).** `f` is *Bourbaki-proper* if `Z × X → Z × Y` is closed for every
> topological space `Z`. As in Mathlib's `isProperMap_iff_universally_closed`, `Z` is quantified
> over one universe at a time; `IsProperMap.isBourbakiProperMap` below supplies the statement in
> every universe at once.

```lean
def IsBourbakiProperMap (f : X → Y) : Prop
```

**`StacksDraft.Topology.IsQuasiProperMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/Proper.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L59). The attribute's comment: “(3)”.

> **Stacks 005O (3).** `f` is *quasi-proper* if the inverse image of every quasi-compact
> subset of `Y` is quasi-compact.

```lean
def IsQuasiProperMap (f : X → Y) : Prop
```

**`StacksDraft.Topology.IsUniversallyClosedMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/Proper.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L65). The attribute's comment: “(4)”.

> **Stacks 005O (4).** `f` is *universally closed* if for every continuous `g : Z → Y` the
> base change `f' : Z ×_Y X → Z` is a closed map.

```lean
def IsUniversallyClosedMap (f : X → Y) : Prop
```

**`StacksDraft.Topology.IsProperMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/Proper.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L73). The attribute's comment: “(5)”. References: SGA 4 Vbis (4.1.0), “proper morphism def”.

> **Stacks 005O (5).** `f` is *proper* if it is separated and universally closed. Separatedness
> is Mathlib's `IsSeparatedMap`, which Stacks 0CY1 defines by the diagonal `X → X ×_Y X` being a
> closed map; `isSeparatedMap_iff_isClosedMap` is that equivalence.

```lean
def IsProperMap (f : X → Y) : Prop
```

Declarations registered for the tag:

- [`IsClosedMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosedMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Maps/Proper.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L43) (StacksFrontier): “(1) A map is closed if the image of every closed subset is closed.”. References: EGA I (2.2.6); EGA II (7.2.1).

## Tag 005P, a lemma

[Tag 005P](https://stacks.math.columbia.edu/tag/005P) in the Stacks Project.

**`compactSpace_iff_forall_isClosedMap_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Proper/ClosedProjection.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Proper/ClosedProjection.lean#L85).

> **Stacks 005P**.
> A topological space `X` is quasi-compact (`CompactSpace X`) if and only if, for every
> topological space `Z`, the first projection `Prod.fst : Z × X → Z` is a closed map.

```lean
theorem compactSpace_iff_forall_isClosedMap_fst (X : Type u) [TopologicalSpace X] :
    CompactSpace X ↔
      ∀ (Z : Type u) [TopologicalSpace Z], IsClosedMap (Prod.fst : Z × X → Z)
```

## Tag 005Q, a remark

[Tag 005Q](https://stacks.math.columbia.edu/tag/005Q) in the Stacks Project.

**`compactSpace_iff_isClosedMap_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Proper/ClosedProjectionRemark.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Proper/ClosedProjectionRemark.lean#L25).

> **Stacks 005Q**.
> A topological space `X` is quasi-compact (`CompactSpace X`) if and only if, for every
> topological space `Z`, the first projection `Prod.fst : Z × X → Z` is a closed map.

```lean
theorem compactSpace_iff_isClosedMap_fst (X : Type) [TopologicalSpace X] :
    CompactSpace X ↔
      ∀ (Z : Type) [TopologicalSpace Z], IsClosedMap (Prod.fst : Z × X → Z)
```

## Tag 005R, a theorem

[Tag 005R](https://stacks.math.columbia.edu/tag/005R) in the Stacks Project.

**`isProperMap_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Proper/Defs.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Proper/Defs.lean#L186).

> **Stacks 005R**.
> Let `f : X → Y` be a continuous map between topological spaces. The following four
> conditions are equivalent:
>
> 1. `f` is quasi-proper and closed.
> 2. `f` is Bourbaki-proper.
> 3. `f` is universally closed.
> 4. `f` is closed and the fibre `f⁻¹{y}` is quasi-compact for every `y : Y`.

```lean
theorem isProperMap_tfae {X Y : Type u} [TopologicalSpace X] [TopologicalSpace Y]
    (f : X → Y) (hf : Continuous f) :
    [IsQuasiProper f ∧ IsClosedMap f,
     IsBourbakiProperMap.{u, u, u} f,
     IsUniversallyClosed f,
     IsClosedMap f ∧ ∀ y : Y, IsQuasiCompactSubset (f ⁻¹' {y})].TFAE
```

## Tag 08YD, a lemma

[Tag 08YD](https://stacks.math.columbia.edu/tag/08YD) in the Stacks Project.

**`StacksDraft.Topology.isUniversallyClosedMap_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/Proper.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Proper.lean#L132).

> **Stacks 08YD.** A continuous map from a quasi-compact space to a Hausdorff space is
> universally closed (Stacks 005O (4)). Mathlib supplies the two halves of the argument:
> `Continuous.isProperMap` (a continuous map from a compact space to a Hausdorff space is proper)
> and `IsProperMap.universally_closed` (proper maps are closed after any product); the lemma
> `IsProperMap.isUniversallyClosedMap` converts the product form into the source's
> fibre-product form.

```lean
theorem isUniversallyClosedMap_of_compactSpace [CompactSpace X] [T2Space Y]
    (hf : Continuous f) : IsUniversallyClosedMap.{u, v, w} f
```

Declarations registered for the tag:

- [`Continuous.isProperMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Continuous.isProperMap#doc) registered with `add_to_stacks` in [StacksCore/Topology/Proper/UniversallyClosed.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Proper/UniversallyClosed.lean#L20) (StacksCore): “a continuous map from a quasi-compact space to a Hausdorff space is proper”.
- [`IsProperMap.universally_closed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsProperMap.universally_closed#doc) registered with `add_to_stacks` in [StacksCore/Topology/Proper/UniversallyClosed.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Proper/UniversallyClosed.lean#L22) (StacksCore): “proper maps are universally closed”.

## Tag 08YE, a lemma

[Tag 08YE](https://stacks.math.columbia.edu/tag/08YE) in the Stacks Project.

Declarations registered for the tag:

- [`isHomeomorph_iff_continuous_bijective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isHomeomorph_iff_continuous_bijective#doc) registered with `add_to_stacks` in [StacksCore/Topology/Proper/Bijection.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Proper/Bijection.lean#L20) (StacksCore): “a continuous bijection out of a quasi-compact space is a homeomorphism”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.17, Tag 005M](https://stacks.math.columbia.edu/tag/005M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
