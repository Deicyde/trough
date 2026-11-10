---
declaration: section
origin: cited
lean: CategoryTheory.Simple, CategoryTheory.isArtinianObject_iff_of_shortExact, CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject, CategoryTheory.isNoetherianObject_iff_of_shortExact, CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject, CategoryTheory.isArtinianObject_and_isNoetherianObject_iff_exists_filtration, CompositionSeries.jordan_holder
statement: formalized
proof: formalized
---

# 12.9 Jordan-Hölder

Section 12.9 of the Stacks Project, [Tag 0FCD](https://stacks.math.columbia.edu/tag/0FCD). 5 tags here are carried by 7 declarations of the repository (all in StacksCore) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FCE, a definition

[Tag 0FCE](https://stacks.math.columbia.edu/tag/0FCE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Simple`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Simple#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Simple.lean, line 7](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Simple.lean#L7) (StacksCore).

## Tag 0FCH, a lemma

[Tag 0FCH](https://stacks.math.columbia.edu/tag/0FCH) in the Stacks Project.

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L55). The attribute's comment: “=>”.

```lean
instance : CategoryTheory.isArtinianObject.IsClosedUnderQuotients (C := C)
```

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L81). The attribute's comment: “<=”.

```lean
instance : CategoryTheory.isArtinianObject.IsClosedUnderExtensions (C := C)
```

**`CategoryTheory.isArtinianObject_iff_of_shortExact`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L93).

> **Stacks 0FCH**: for a short exact sequence `0 ⟶ A₁ ⟶ A₂ ⟶ A₃ ⟶ 0` in an abelian
> category, `A₂` is Artinian if and only if `A₁` and `A₃` are Artinian.

```lean
lemma isArtinianObject_iff_of_shortExact {S : ShortComplex C} (hS : S.ShortExact) :
    IsArtinianObject S.X₂ ↔ IsArtinianObject S.X₁ ∧ IsArtinianObject S.X₃
```

Declarations registered for the tag:

- [`CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L29) (StacksCore): “=>”.

## Tag 0FCI, a lemma

[Tag 0FCI](https://stacks.math.columbia.edu/tag/0FCI) in the Stacks Project.

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L44). The attribute's comment: “=>”.

```lean
instance : CategoryTheory.isNoetherianObject.IsClosedUnderQuotients (C := C)
```

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L62). The attribute's comment: “<=”.

```lean
instance : CategoryTheory.isNoetherianObject.IsClosedUnderExtensions (C := C)
```

**`CategoryTheory.isNoetherianObject_iff_of_shortExact`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L74).

> **Stacks 0FCI**: for a short exact sequence `0 ⟶ A₁ ⟶ A₂ ⟶ A₃ ⟶ 0` in an abelian
> category, `A₂` is Noetherian if and only if `A₁` and `A₃` are Noetherian.

```lean
lemma isNoetherianObject_iff_of_shortExact {S : ShortComplex C} (hS : S.ShortExact) :
    IsNoetherianObject S.X₂ ↔ IsNoetherianObject S.X₁ ∧ IsNoetherianObject S.X₃
```

Declarations registered for the tag:

- [`CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L17) (StacksCore): “=>”. References: SGA 4 VI (1.30.1), “more general”.

## Tag 0FCJ, a lemma

[Tag 0FCJ](https://stacks.math.columbia.edu/tag/0FCJ) in the Stacks Project.

**`CategoryTheory.isArtinianObject_and_isNoetherianObject_iff_exists_filtration`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/JordanHolder.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/JordanHolder.lean#L114).

> **Stacks 0FCJ**: an object of an abelian category is Artinian and Noetherian if and
> only if it admits a finite filtration by subobjects with simple successive quotients.

```lean
lemma isArtinianObject_and_isNoetherianObject_iff_exists_filtration (X : C) :
    (IsArtinianObject X ∧ IsNoetherianObject X) ↔
      ∃ (a : ℕ → Subobject X) (n : ℕ) (hle : ∀ i, i < n → a i ≤ a (i + 1)),
        a 0 = ⊥ ∧ a n = ⊤ ∧
          ∀ i (hi : i < n), Simple (cokernel (Subobject.ofLE _ _ (hle i hi)))
```

## Tag 0FCK, a lemma

[Tag 0FCK](https://stacks.math.columbia.edu/tag/0FCK) in the Stacks Project.

Declarations registered for the tag:

- [`CompositionSeries.jordan_holder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CompositionSeries.jordan_holder#doc) registered with `add_to_stacks` in [StacksCore/Order/JordanHolder.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Order/JordanHolder.lean#L8) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.9, Tag 0FCD](https://stacks.math.columbia.edu/tag/0FCD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
