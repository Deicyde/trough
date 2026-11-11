---
declaration: section
origin: cited
lean: continuous_iff_le_induced, isOpen_induced_iff, isClosed_induced_iff, continuous_coinduced_rng, continuous_iff_coinduced_le, isOpen_coinduced, isClosed_coinduced, Topology.IsQuotientMap
statement: formalized
proof: formalized
---

# 5.6 Submersive maps

Section 5.6 of the Stacks Project, [Tag 0405](https://stacks.math.columbia.edu/tag/0405). 5 tags here are carried by 3 declarations of the repository (all in StacksCore) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09R8, a lemma

[Tag 09R8](https://stacks.math.columbia.edu/tag/09R8) in the Stacks Project.

Declarations registered for the tag:

- [`continuous_iff_le_induced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=continuous_iff_le_induced#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Maps/Induced.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Induced.lean#L31) (StacksFrontier): “(1) the induced topology is the weakest one making the map continuous”.
- [`isOpen_induced_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isOpen_induced_iff#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Maps/Induced.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Induced.lean#L33) (StacksFrontier): “(2) the opens are the preimages of opens”.
- [`isClosed_induced_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isClosed_induced_iff#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Maps/Induced.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/Induced.lean#L34) (StacksFrontier): “(3) the closed sets are the preimages of closed sets”.

## Tag 08ZK, a lemma

[Tag 08ZK](https://stacks.math.columbia.edu/tag/08ZK) in the Stacks Project.

Declarations registered for the tag:

- [`continuous_coinduced_rng`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=continuous_coinduced_rng#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Quotient.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Quotient.lean#L23) (StacksCore): “f is continuous for the quotient topology”.
- [`continuous_iff_coinduced_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=continuous_iff_coinduced_le#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Quotient.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Quotient.lean#L24) (StacksCore): “the quotient topology is the strongest one making f continuous”.
- [`isOpen_coinduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isOpen_coinduced#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Quotient.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Quotient.lean#L26) (StacksCore): “(2) the opens of the quotient topology”.
- [`isClosed_coinduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isClosed_coinduced#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Quotient.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Quotient.lean#L27) (StacksCore): “(3) the closed sets of the quotient topology”.

## Tag 0406, a definition

[Tag 0406](https://stacks.math.columbia.edu/tag/0406) in the Stacks Project.

Declarations registered for the tag:

- [`Topology.IsQuotientMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsQuotientMap#doc) registered with `add_to_stacks` in [StacksCore/Topology/Defs/Induced.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Defs/Induced.lean#L10) (StacksCore): “2, defined as surjective + coinducing”. References: EGA II (8.11.1); EGA IV (15.7.8); SGA 1 IX (2.1), “partial”.
- [`Topology.IsStrictMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsStrictMap#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Strict.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Strict.lean#L24) (StacksCore).
- [`Topology.isQuotientMap_iff_isStrictMap_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.isQuotientMap_iff_isStrictMap_surjective#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/Strict.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/Strict.lean#L26) (StacksCore).

## Tag 02YB, a lemma

[Tag 02YB](https://stacks.math.columbia.edu/tag/02YB) in the Stacks Project.

**`Topology.IsCoinducing.isLocallyClosed_iff_preimage`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Maps/SubmersiveOpen.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveOpen.lean#L42). The attribute's comment: “(4)”.

> **Stacks 02YB** (part 4). An open coinducing map detects locally closed subsets.

```lean
theorem Topology.IsCoinducing.isLocallyClosed_iff_preimage
    {f : X → Y} (hf : IsCoinducing f) (hopen : IsOpenMap f) (T : Set Y) :
    IsLocallyClosed T ↔ IsLocallyClosed (f ⁻¹' T)
```

Declarations registered for the tag:

- [`IsOpenMap.preimage_closure_eq_closure_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsOpenMap.preimage_closure_eq_closure_preimage#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveOpen.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveOpen.lean#L34) (StacksCore): “(1)”. References: EGA IV (2.4.11), “more general”.
- [`IsCoinducing.isClosed_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCoinducing.isClosed_preimage#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveOpen.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveOpen.lean#L36) (StacksCore): “(2)”.
- [`IsCoinducing.isOpen_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCoinducing.isOpen_preimage#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveOpen.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveOpen.lean#L38) (StacksCore): “(3)”.
- [`IsOpenMap.isQuotientMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsOpenMap.isQuotientMap#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveOpen.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveOpen.lean#L48) (StacksCore): “submersive”. References: EGA II (8.11.1), “partial”; SGA 1 IX (2.2), “a) surjective open case”.

## Tag 0AAU, a lemma

[Tag 0AAU](https://stacks.math.columbia.edu/tag/0AAU) in the Stacks Project.

**`IsClosedMap.image_closure_preimage_eq_closure`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Maps/SubmersiveClosed.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveClosed.lean#L37). The attribute's comment: “(1)”.

> **Stacks 0AAU** (part 1). A closed continuous map carries the closure of the preimage of
> a subset of its range onto the closure of that subset.

```lean
theorem IsClosedMap.image_closure_preimage_eq_closure
    (hf_closed : IsClosedMap f) (hf_cont : Continuous f) {T : Set Y}
    (hT : T ⊆ range f) :
    f '' closure (f ⁻¹' T) = closure T
```

**`isLocallyClosed_iff_preimage_isLocallyClosed`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Maps/SubmersiveClosed.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveClosed.lean#L52). The attribute's comment: “(4)”.

> **Stacks 0AAU** (part 4). For a surjective closed continuous map `f : X → Y` and any `T ⊆ Y`,
> `T` is locally closed iff `f ⁻¹' T` is locally closed.

```lean
theorem isLocallyClosed_iff_preimage_isLocallyClosed
    (hf_surj : Function.Surjective f) (hf_cont : Continuous f)
    (hf_closed : IsClosedMap f) (T : Set Y) :
    IsLocallyClosed T ↔ IsLocallyClosed (f ⁻¹' T)
```

Declarations registered for the tag:

- [`IsCoinducing.isClosed_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCoinducing.isClosed_preimage#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveClosed.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveClosed.lean#L43) (StacksCore): “(2)”.
- [`IsCoinducing.isOpen_preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsCoinducing.isOpen_preimage#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveClosed.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveClosed.lean#L45) (StacksCore): “(3)”.
- [`IsClosedMap.isQuotientMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsClosedMap.isQuotientMap#doc) registered with `add_to_stacks` in [StacksCore/Topology/Maps/SubmersiveClosed.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Maps/SubmersiveClosed.lean#L47) (StacksCore): “submersive”. References: EGA II (8.11.1), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.6, Tag 0405](https://stacks.math.columbia.edu/tag/0405)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
