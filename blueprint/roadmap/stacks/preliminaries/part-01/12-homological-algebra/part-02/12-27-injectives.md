---
declaration: section
origin: cited
lean: CategoryTheory.Injective, injective_iff_everySES_splits, subsingleton_ext_one_of_injective, CategoryTheory.Injective.instPiObj, CategoryTheory.EnoughInjectives, HasFunctorialInjectiveEmbeddings
statement: formalized
proof: formalized
---

# 12.27 Injectives

Section 12.27 of the Stacks Project, [Tag 0134](https://stacks.math.columbia.edu/tag/0134). 5 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0135, a definition

[Tag 0135](https://stacks.math.columbia.edu/tag/0135) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L18) (StacksFrontier). References: SGA 4 I (7.11).

## Tag 0136, a lemma

[Tag 0136](https://stacks.math.columbia.edu/tag/0136) in the Stacks Project.

**`injective_iff_everySES_splits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L83). The attribute's comment: “(1)⇔(3)”.

> `I` is injective iff every short exact sequence `0 ⟶ I ⟶ A ⟶ B ⟶ 0` is split.

```lean
theorem injective_iff_everySES_splits (I : 𝒜) :
    Injective I ↔ EverySESStartingAtSplits I
```

**`subsingleton_ext_one_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L90). The attribute's comment: “(1)⇒(4)”.

> If `I` is injective then `Ext¹(B, I) = 0` (encoded as `Subsingleton (Ext B I 1)`) for every
> object `B`.

```lean
theorem subsingleton_ext_one_of_injective [HasExt 𝒜]
    (I : 𝒜) (hI : Injective I) (B : 𝒜) :
    Subsingleton (Abelian.Ext B I 1)
```

## Tag 0137, a lemma

[Tag 0137](https://stacks.math.columbia.edu/tag/0137) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Injective.instPiObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Injective.instPiObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L20) (StacksFrontier).

## Tag 0138, a definition

[Tag 0138](https://stacks.math.columbia.edu/tag/0138) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.EnoughInjectives`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.EnoughInjectives#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L21) (StacksFrontier). References: EGA 0 (11.4.3); SGA 3 I (5.3.1.1); SGA 4 I (7.13); SGA 4 II (6.9); SGA 4 V (0.1.1); SGA 6 II (3.1).

## Tag 0139, a definition

[Tag 0139](https://stacks.math.columbia.edu/tag/0139) in the Stacks Project.

**`HasFunctorialInjectiveEmbeddings`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Injective/Basic.lean#L135).

> The notion of *functorial injective embeddings* for an abelian category `𝒜`: there exists a
> functor `J : 𝒜 ⥤ Arrow 𝒜` satisfying the three conditions `IsFunctorialInjectiveEmbeddings₁`,
> `IsFunctorialInjectiveEmbeddings₂`, and `IsFunctorialInjectiveEmbeddings₃`.

```lean
def HasFunctorialInjectiveEmbeddings : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.27, Tag 0134](https://stacks.math.columbia.edu/tag/0134)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
