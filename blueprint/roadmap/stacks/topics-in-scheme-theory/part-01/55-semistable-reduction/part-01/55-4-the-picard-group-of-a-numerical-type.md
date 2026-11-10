---
declaration: section
origin: cited
lean: AlgebraicGeometry.NumericalType.picardGroup, AlgebraicGeometry.NumericalType.rank_picardGroup, Module.Finite.quotient, AlgebraicGeometry.NumericalType.picardGroup_embeds_intersectionCokernel, AlgebraicGeometry.NumericalType.contractPicardMap, AlgebraicGeometry.NumericalType.contractPicardMap_mk, AlgebraicGeometry.NumericalType.contractPicardMap_injective, AlgebraicGeometry.NumericalType.two_smul_mem_contractPicardMap_range
statement: formalized
proof: formalized
---

# 55.4 The Picard group of a numerical type

Section 55.4 of the Stacks Project, [Tag 0C7G](https://stacks.math.columbia.edu/tag/0C7G). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C7H, a definition

[Tag 0C7H](https://stacks.math.columbia.edu/tag/0C7H) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.picardGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Defs.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Defs.lean#L56).

> The Picard group of a numerical type, namely the cokernel of its relation
> matrix.

```lean
public abbrev picardGroup (T : NumericalType)
```

## Tag 0C7I, a lemma

[Tag 0C7I](https://stacks.math.columbia.edu/tag/0C7I) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.rank_picardGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Rank.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Rank.lean#L177). The attribute's comment: “rank one”.

> The Picard group of a numerical type has rank one.

```lean
public theorem rank_picardGroup (T : NumericalType) :
    Module.rank ℤ (picardGroup T) = 1
```

Declarations registered for the tag:

- [`Module.Finite.quotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.quotient#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Rank.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Rank.lean#L33) (StacksFrontier): “finite generation”. References: EGA 0 (5.2.1), “special case”; SGA 6 I (3.2), “special case”.

## Tag 0CE7, a lemma

[Tag 0CE7](https://stacks.math.columbia.edu/tag/0CE7) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.picardGroup_embeds_intersectionCokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Defs.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Defs.lean#L111).

> The Picard group of a numerical type embeds in the cokernel of its
> integral intersection matrix.

```lean
public theorem picardGroup_embeds_intersectionCokernel (T : NumericalType) :
    ∃ f : picardGroup T →+ intersectionCokernel T, Function.Injective f
```

## Tag 0C7J, a lemma

[Tag 0C7J](https://stacks.math.columbia.edu/tag/0C7J) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.contractPicardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean#L476). The attribute's comment: “the induced homomorphism”.

> The Picard-group homomorphism induced by contracting the final minus-one
> component.

```lean
public noncomputable def contractPicardMap (T : NumericalType)
    (h : IsMinusOneIndex T (lastIndex T)) :
    picardGroup T →+ picardGroup (contractLast T h).val
```

**`AlgebraicGeometry.NumericalType.contractPicardMap_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean#L487). The attribute's comment: “formula on representatives”.

> On cokernel representatives, the contraction homomorphism is induced by the
> coordinate map `p`.

```lean
public theorem contractPicardMap_mk (T : NumericalType)
    (h : IsMinusOneIndex T (lastIndex T))
    (x : Fin T.componentCount → ℤ) :
    contractPicardMap T h (Submodule.Quotient.mk x) =
      Submodule.Quotient.mk (contractPicardRepresentative T h x)
```

**`AlgebraicGeometry.NumericalType.contractPicardMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean#L496). The attribute's comment: “injectivity”.

> Contraction of a minus-one component induces an injection on Picard groups.

```lean
public theorem contractPicardMap_injective (T : NumericalType)
    (h : IsMinusOneIndex T (lastIndex T)) :
    Function.Injective (contractPicardMap T h)
```

**`AlgebraicGeometry.NumericalType.two_smul_mem_contractPicardMap_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/Contraction.lean#L565). The attribute's comment: “elementary abelian two-group cokernel”.

> The cokernel of the Picard-group map induced by contraction has exponent two.

```lean
public theorem two_smul_mem_contractPicardMap_range (T : NumericalType)
    (h : IsMinusOneIndex T (lastIndex T))
    (x : picardGroup (contractLast T h).val) :
    2 • x ∈ (contractPicardMap T h).range
```

## Tag 0C7K, a lemma

[Tag 0C7K](https://stacks.math.columbia.edu/tag/0C7K) in the Stacks Project.

**`AlgebraicGeometry.NumericalType.picardGroup_addEquiv_int_of_genus_nonpos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/GenusNonpos.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SemistableReduction/PicardGroup/GenusNonpos.lean#L241).

> A numerical type of nonpositive genus has infinite cyclic Picard group.

```lean
public theorem picardGroup_addEquiv_int_of_genus_nonpos (T : NumericalType)
    (hT : genus T ≤ 0) : Nonempty (picardGroup T ≃+ ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.4, Tag 0C7G](https://stacks.math.columbia.edu/tag/0C7G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
