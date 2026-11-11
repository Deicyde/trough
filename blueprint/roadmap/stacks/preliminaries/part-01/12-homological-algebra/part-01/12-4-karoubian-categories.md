---
declaration: section
origin: cited
lean: CategoryTheory.IsIdempotentComplete, isIdempotentComplete_iff_idempotents_have_cokernels, isIdempotentComplete_iff', isIdempotentComplete_iff_hasBinaryProduct_proj, isIdempotentComplete_of_hasCountableProducts, isIdempotentComplete_of_hasCountableCoproducts
statement: formalized
proof: formalized
---

# 12.4 Karoubian categories

Section 12.4 of the Stacks Project, [Tag 09SF](https://stacks.math.columbia.edu/tag/09SF). 3 tags here are carried by 5 declarations of the repository (all in StacksCore) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09SG, a definition

[Tag 09SG](https://stacks.math.columbia.edu/tag/09SG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsIdempotentComplete`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsIdempotentComplete#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Idempotents/Basic.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Basic.lean#L37) (StacksCore). References: SGA 4 I (8.7.8); SGA 4 IV (7.5).

## Tag 09SH, a lemma

[Tag 09SH](https://stacks.math.columbia.edu/tag/09SH) in the Stacks Project.

**`isIdempotentComplete_iff_idempotents_have_cokernels`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Idempotents/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Basic.lean#L55). The attribute's comment: “(1) ↔ (2)”.

```lean
lemma isIdempotentComplete_iff_idempotents_have_cokernels :
    IsIdempotentComplete C ↔ ∀ {X : C} (p : X ⟶ X), p ≫ p = p → HasCokernel p
```

**`isIdempotentComplete_iff'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Idempotents/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Basic.lean#L72). The attribute's comment: “(1) ↔ (3)”.

```lean
lemma isIdempotentComplete_iff' : IsIdempotentComplete C ↔
    ∀ (Z : C) (p : Z ⟶ Z), p ≫ p = p →
    ∃ (X Y : C) (b : BinaryBicone X Y) (_ : b.IsBilimit) (e : Z ≅ b.pt),
      e.hom ≫ b.snd ≫ b.inr ≫ e.inv = p
```

**`isIdempotentComplete_iff_hasBinaryProduct_proj`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Idempotents/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Basic.lean#L87). The attribute's comment: “(1) ↔ (3)”.

> The direct-sum characterisation (Stacks 09SH (3)), phrased with the biproduct `X ⊞ Y`.

```lean
lemma isIdempotentComplete_iff_hasBinaryProduct_proj : IsIdempotentComplete C ↔
    ∀ (Z : C) (p : Z ⟶ Z), p ≫ p = p →
      ∃ (X Y : C) (_ : HasBinaryBiproduct X Y) (e : Z ≅ X ⊞ Y),
        e.hom ≫ biprod.snd ≫ biprod.inr ≫ e.inv = p
```

## Tag 05QV, a lemma

[Tag 05QV](https://stacks.math.columbia.edu/tag/05QV) in the Stacks Project.

**`isIdempotentComplete_of_hasCountableProducts`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Idempotents/Countable.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Countable.lean#L145). The attribute's comment: “(1)”.

> **Stacks 05QV(1)**: a preadditive category in which every object has a countable power, and in
> which every split epimorphism has a kernel, is idempotent complete. A kernel of an idempotent
> `p : Z ⟶ Z` is read off a kernel of its telescope `idempotentTelescope p`, an endomorphism of the
> single countable power `∏ₙ Z`; that is why no product beyond those powers is assumed.

```lean
lemma isIdempotentComplete_of_hasCountableProducts [∀ Z : C, HasProduct fun _ : ℕ => Z]
    (h : ∀ {X Y : C} (f : X ⟶ Y) [IsSplitEpi f], HasKernel f) : IsIdempotentComplete C
```

**`isIdempotentComplete_of_hasCountableCoproducts`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Idempotents/Countable.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Idempotents/Countable.lean#L155). The attribute's comment: “(2)”.

> **Stacks 05QV(2)**: a preadditive category in which every object has a countable copower, and in
> which every split monomorphism has a cokernel, is idempotent complete. This is 05QV(1) in `Cᵒᵖ`,
> where the copowers of `C` are the countable powers.

```lean
lemma isIdempotentComplete_of_hasCountableCoproducts [∀ Z : C, HasCoproduct fun _ : ℕ => Z]
    (h : ∀ {X Y : C} (f : X ⟶ Y) [IsSplitMono f], HasCokernel f) : IsIdempotentComplete C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.4, Tag 09SF](https://stacks.math.columbia.edu/tag/09SF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
