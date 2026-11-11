---
declaration: section
origin: cited
lean: normal_iff_forall_fieldRange_eq, normal_iff_splits_minpoly_of_adjoin_eq_top, card_algEquiv_le_finSepDegree, normal_iff_card_algEquiv_eq_finSepDegree
statement: formalized
proof: formalized
---

# 9.15 Normal extensions

Section 9.15 of the Stacks Project, [Tag 09HL](https://stacks.math.columbia.edu/tag/09HL). 3 tags here are carried by 4 declarations of the repository (all in StacksCore), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09HQ, a lemma

[Tag 09HQ](https://stacks.math.columbia.edu/tag/09HQ) in the Stacks Project.

**`normal_iff_forall_fieldRange_eq`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/AlgClosed.lean#L17).

```lean
theorem normal_iff_forall_fieldRange_eq
    (F E L : Type*) [Field F] [Field E] [Field L]
    [Algebra F E] [Algebra F L] [Algebra.IsAlgebraic F E] [IsAlgClosed L] :
    Normal F E ↔ ∀ σ₁ σ₂ : E →ₐ[F] L, σ₁.fieldRange = σ₂.fieldRange
```

## Tag 0BR3, a lemma

[Tag 0BR3](https://stacks.math.columbia.edu/tag/0BR3) in the Stacks Project.

**`normal_iff_splits_minpoly_of_adjoin_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Normal/Basic.lean#L13).

```lean
theorem normal_iff_splits_minpoly_of_adjoin_eq_top
    {F E : Type*} [Field F] [Field E] [Algebra F E]
    {s : Set E} (hs : adjoin F s = ⊤) :
    Normal F E ↔ ∀ x ∈ s, IsAlgebraic F x ∧ ((minpoly F x).map (algebraMap F E)).Splits
```

## Tag 09HS, a lemma

[Tag 09HS](https://stacks.math.columbia.edu/tag/09HS) in the Stacks Project.

**`card_algEquiv_le_finSepDegree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SeparableDegree.lean#L123). The attribute's comment: “inequality”.

```lean
theorem card_algEquiv_le_finSepDegree
    (F E : Type*) [Field F] [Field E] [Algebra F E] [FiniteDimensional F E] :
    card (E ≃ₐ[F] E) ≤ finSepDegree F E
```

**`normal_iff_card_algEquiv_eq_finSepDegree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SeparableDegree.lean#L130). The attribute's comment: “equality”.

```lean
theorem normal_iff_card_algEquiv_eq_finSepDegree
    (F E : Type*) [Field F] [Field E] [Algebra F E] [FiniteDimensional F E] :
    Normal F E ↔ card (E ≃ₐ[F] E) = finSepDegree F E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.15, Tag 09HL](https://stacks.math.columbia.edu/tag/09HL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
