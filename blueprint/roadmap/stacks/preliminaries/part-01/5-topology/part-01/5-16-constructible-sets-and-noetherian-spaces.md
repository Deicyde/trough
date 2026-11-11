---
declaration: section
origin: cited
lean: constructible_iff_finite_union_locally_closed, isConstructibleSet_preimage, constructible_iff_dichotomy_irreducible_closed, Topology.IsConstructible.mem_nhds_iff_forall_subset_closure_inter, Topology.isOpen_iff_inter_irreducible_closed
statement: formalized
proof: formalized
---

# 5.16 Constructible sets and Noetherian spaces

Section 5.16 of the Stacks Project, [Tag 053X](https://stacks.math.columbia.edu/tag/053X). 5 tags here are carried by 5 declarations of the repository (1 in StacksCore and 4 in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 005L, a lemma

[Tag 005L](https://stacks.math.columbia.edu/tag/005L) in the Stacks Project.

**`constructible_iff_finite_union_locally_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/Constructible.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Noetherian/Constructible.lean#L33). References: EGA 0 (9.1.7); EGA 0 (9.2.1), “first assertion”; EGA IV (1.8.1), “special case”; EGA IV (10.1.1), “global comparison”.

> **Stacks 005L.** In a Noetherian topological space `X`, a subset `E ⊆ X` is constructible if
> and only if it is a finite union of locally closed subsets of `X`.

```lean
theorem constructible_iff_finite_union_locally_closed
    [TopologicalSpace.NoetherianSpace X] (E : Set X) :
    IsConstructibleSet E ↔ IsFiniteUnionLocallyClosed E
```

## Tag 053Y, a lemma

[Tag 053Y](https://stacks.math.columbia.edu/tag/053Y) in the Stacks Project.

**`isConstructibleSet_preimage`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Topology/Noetherian/ConstructiblePreimage.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Topology/Noetherian/ConstructiblePreimage.lean#L27). References: EGA 0 (9.2.1), “more general”; EGA IV (1.8.2), “special case”.

> **Stacks 053Y.** Let `f : X → Y` be a continuous map from a Noetherian topological space. If
> `E ⊆ Y` is constructible in `Y`, then `f ⁻¹' E` is constructible in `X`: preimages preserve opens,
> and retrocompactness is automatic in a Noetherian space.

```lean
theorem isConstructibleSet_preimage
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    [TopologicalSpace.NoetherianSpace X]
    {f : X → Y} (hf : Continuous f) {E : Set Y}
    (hE : Topology.IsConstructible E) :
    Topology.IsConstructible (f ⁻¹' E)
```

## Tag 053Z, a lemma

[Tag 053Z](https://stacks.math.columbia.edu/tag/053Z) in the Stacks Project.

**`constructible_iff_dichotomy_irreducible_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/ConstructibleDichotomy.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Noetherian/ConstructibleDichotomy.lean#L220). References: EGA 0 (9.2.3); EGA 0 (9.2.2), “necessity”; EGA 0 (9.3.2), “special case”; EGA IV (9.2.5), “more general”; SGA 1 IV (6.1).

> Let `X` be a Noetherian topological space and let `E ⊆ X`. Then `E` is
> constructible if and only if for every irreducible closed `Z ⊆ X` the intersection `E ∩ Z` either
> contains a nonempty open of `Z` or fails to be dense in `Z`.

```lean
theorem constructible_iff_dichotomy_irreducible_closed
    [TopologicalSpace.NoetherianSpace X] (E : Set X) :
    IsConstructibleSet E ↔
      ∀ Z : Set X, IsIrreducible Z → IsClosed Z →
        ContainsNonemptyOpenOf E Z ∨ ¬ IsDenseIn E Z
```

## Tag 0540, a lemma

[Tag 0540](https://stacks.math.columbia.edu/tag/0540) in the Stacks Project.

**`Topology.IsConstructible.mem_nhds_iff_forall_subset_closure_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Constructible/NoetherianNeighbourhood.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Constructible/NoetherianNeighbourhood.lean#L174). References: EGA 0 (9.2.5).

> **Stacks 0540.** In a Noetherian topological space, a constructible subset `E` is a
> neighbourhood of a point `x` if and only if `E ∩ Y` is dense in `Y` for every irreducible closed
> subset `Y` containing `x`.

```lean
theorem IsConstructible.mem_nhds_iff_forall_subset_closure_inter [NoetherianSpace X] {E : Set X}
    (hE : IsConstructible E) (x : X) :
    E ∈ 𝓝 x ↔ ∀ Y : Set X, IsClosed Y → IsIrreducible Y → x ∈ Y → Y ⊆ closure (E ∩ Y)
```

## Tag 0541, a lemma

[Tag 0541](https://stacks.math.columbia.edu/tag/0541) in the Stacks Project.

**`Topology.isOpen_iff_inter_irreducible_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Noetherian/OpenViaIrreducibleClosed.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Noetherian/OpenViaIrreducibleClosed.lean#L146). References: EGA 0 (9.2.6).

> **Stacks 0541.** A subset `E` of a Noetherian topological space is open if and only if, for
> every irreducible closed subset `Y`, the intersection `E ∩ Y` is empty or contains a nonempty
> open subset of `Y`, that is, a set `V ∩ Y` with `V` open in `X` and `V ∩ Y` nonempty.

```lean
theorem isOpen_iff_inter_irreducible_closed [NoetherianSpace X] (E : Set X) :
    IsOpen E ↔ ∀ Y : Set X, IsClosed Y → IsIrreducible Y →
      E ∩ Y = ∅ ∨ ∃ V : Set X, IsOpen V ∧ (V ∩ Y).Nonempty ∧ V ∩ Y ⊆ E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 5.16, Tag 053X](https://stacks.math.columbia.edu/tag/053X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
