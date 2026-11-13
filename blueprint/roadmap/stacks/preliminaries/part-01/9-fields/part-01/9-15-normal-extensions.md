---
declaration: section
origin: cited
lean: normal_iff_forall_fieldRange_eq, normal_iff_splits_minpoly_of_adjoin_eq_top, AlgEquiv.exists_algEquiv_algebraMap_eq_of_normal, AlgHom.exists_algEquiv_extending_of_normal, card_algEquiv_le_finSepDegree, normal_iff_card_algEquiv_eq_finSepDegree
statement: formalized
proof: formalized
---

# 9.15 Normal extensions

Section 9.15 of the Stacks Project, [Tag 09HL](https://stacks.math.columbia.edu/tag/09HL). 4 tags here are carried by 6 declarations of the repository (4 in StacksCore and 2 in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09HQ, a lemma

[Tag 09HQ](https://stacks.math.columbia.edu/tag/09HQ) in the Stacks Project.

**`normal_iff_forall_fieldRange_eq`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/AlgClosed.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Normal/AlgClosed.lean#L17).

```lean
theorem normal_iff_forall_fieldRange_eq
    (F E L : Type*) [Field F] [Field E] [Field L]
    [Algebra F E] [Algebra F L] [Algebra.IsAlgebraic F E] [IsAlgClosed L] :
    Normal F E ↔ ∀ σ₁ σ₂ : E →ₐ[F] L, σ₁.fieldRange = σ₂.fieldRange
```

## Tag 0BR3, a lemma

[Tag 0BR3](https://stacks.math.columbia.edu/tag/0BR3) in the Stacks Project.

**`normal_iff_splits_minpoly_of_adjoin_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Normal/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Normal/Basic.lean#L13).

```lean
theorem normal_iff_splits_minpoly_of_adjoin_eq_top
    {F E : Type*} [Field F] [Field E] [Algebra F E]
    {s : Set E} (hs : adjoin F s = ⊤) :
    Normal F E ↔ ∀ x ∈ s, IsAlgebraic F x ∧ ((minpoly F x).map (algebraMap F E)).Splits
```

## Tag 0BME, a lemma

[Tag 0BME](https://stacks.math.columbia.edu/tag/0BME) in the Stacks Project.

**`AlgEquiv.exists_algEquiv_algebraMap_eq_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Normal/RestrictLift.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/Normal/RestrictLift.lean#L34). The attribute's comment: “(1): an automorphism of `L / K` restricts to an automorphism of `M` when `M / K` is normal”.

> **Stacks 0BME (1).** Let `L / M / K` be a tower of fields with `M / K` normal. Then every
> automorphism `τ` of `L / K` induces an automorphism `τ|_M` of `M / K`, that is, an automorphism
> of `M / K` through which `τ` acts on the image of `M` in `L`. No algebraicity of `L / K` is
> needed.

```lean
theorem AlgEquiv.exists_algEquiv_algebraMap_eq_of_normal [Normal K M] (τ : L ≃ₐ[K] L) :
    ∃ τM : M ≃ₐ[K] M, ∀ m : M, algebraMap M L (τM m) = τ (algebraMap M L m)
```

**`AlgHom.exists_algEquiv_extending_of_normal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/Normal/RestrictLift.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/Normal/RestrictLift.lean#L43). The attribute's comment: “(2): a `K`-algebra map `M → L` extends to an automorphism of `L` when `L / K` is normal”.

> **Stacks 0BME (2).** Let `L / M / K` be a tower of fields with `L / K` normal. Then every
> `K`-algebra map `σ : M → L` extends to an automorphism of `L / K`, that is, an automorphism
> `τ` of `L / K` with `τ ∘ (M → L) = σ`.

```lean
theorem AlgHom.exists_algEquiv_extending_of_normal [Normal K L] (σ : M →ₐ[K] L) :
    ∃ τ : L ≃ₐ[K] L, ∀ m : M, τ (algebraMap M L m) = σ m
```

## Tag 09HS, a lemma

[Tag 09HS](https://stacks.math.columbia.edu/tag/09HS) in the Stacks Project.

**`card_algEquiv_le_finSepDegree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableDegree.lean#L123). The attribute's comment: “inequality”.

```lean
theorem card_algEquiv_le_finSepDegree
    (F E : Type*) [Field F] [Field E] [Algebra F E] [FiniteDimensional F E] :
    card (E ≃ₐ[F] E) ≤ finSepDegree F E
```

**`normal_iff_card_algEquiv_eq_finSepDegree`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/SeparableDegree.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/SeparableDegree.lean#L130). The attribute's comment: “equality”.

```lean
theorem normal_iff_card_algEquiv_eq_finSepDegree
    (F E : Type*) [Field F] [Field E] [Algebra F E] [FiniteDimensional F E] :
    Normal F E ↔ card (E ≃ₐ[F] E) = finSepDegree F E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.15, Tag 09HL](https://stacks.math.columbia.edu/tag/09HL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
