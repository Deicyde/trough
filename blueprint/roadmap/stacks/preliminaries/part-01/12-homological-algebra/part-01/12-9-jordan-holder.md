---
declaration: section
origin: cited
lean: CategoryTheory.Simple, CategoryTheory.IsArtinianCategory, CategoryTheory.IsNoetherianAbelianCategory, CategoryTheory.isArtinianObject_iff_of_shortExact, CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject, CategoryTheory.isNoetherianObject_iff_of_shortExact, CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject, CategoryTheory.isArtinianObject_and_isNoetherianObject_iff_exists_filtration
statement: formalized
proof: formalized
---

# 12.9 Jordan-Hölder

Section 12.9 of the Stacks Project, [Tag 0FCD](https://stacks.math.columbia.edu/tag/0FCD). 7 tags here are carried by 10 declarations of the repository (7 in StacksCore and 3 in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FCE, a definition

[Tag 0FCE](https://stacks.math.columbia.edu/tag/0FCE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Simple`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Simple#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Simple.lean, line 7](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Simple.lean#L7) (StacksCore).

## Tag 0FCF, a definition

[Tag 0FCF](https://stacks.math.columbia.edu/tag/0FCF) in the Stacks Project.

**`CategoryTheory.IsArtinianCategory`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/ArtinianCategory.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/ArtinianCategory.lean#L37). The attribute's comment: “part (2): an abelian category is Artinian if every object is Artinian; part (1) is mathlib's `IsArtinianObject`”.

> An abelian category is *Artinian* if every object is Artinian, i.e. satisfies the
> descending chain condition on subobjects. Unlike mathlib's `Artinian`, no smallness
> condition is imposed.

```lean
class IsArtinianCategory [Abelian C] : Prop
```

## Tag 0FCG, a definition

[Tag 0FCG](https://stacks.math.columbia.edu/tag/0FCG) in the Stacks Project.

**`CategoryTheory.IsNoetherianAbelianCategory`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Noetherian.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Noetherian.lean#L36). The attribute's comment: “(2): an abelian category is Noetherian if every object is Noetherian.”.

> An abelian category is Noetherian if every object of it is Noetherian, i.e. satisfies the
> ascending chain condition on subobjects. Unlike Mathlib's `CategoryTheory.Noetherian`, no
> smallness of the category is required.

```lean
class IsNoetherianAbelianCategory [Abelian C] : Prop
```

## Tag 0FCH, a lemma

[Tag 0FCH](https://stacks.math.columbia.edu/tag/0FCH) in the Stacks Project.

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L55). The attribute's comment: “=>”.

```lean
instance : CategoryTheory.isArtinianObject.IsClosedUnderQuotients (C := C)
```

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L81). The attribute's comment: “<=”.

```lean
instance : CategoryTheory.isArtinianObject.IsClosedUnderExtensions (C := C)
```

**`CategoryTheory.isArtinianObject_iff_of_shortExact`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L93).

> **Stacks 0FCH**: for a short exact sequence `0 ⟶ A₁ ⟶ A₂ ⟶ A₃ ⟶ 0` in an abelian
> category, `A₂` is Artinian if and only if `A₁` and `A₃` are Artinian.

```lean
lemma isArtinianObject_iff_of_shortExact {S : ShortComplex C} (hS : S.ShortExact) :
    IsArtinianObject S.X₂ ↔ IsArtinianObject S.X₁ ∧ IsArtinianObject S.X₃
```

Declarations registered for the tag:

- [`CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instIsClosedUnderSubobjectsIsArtinianObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Subobject/ArtinianObject.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/ArtinianObject.lean#L29) (StacksCore): “=>”.

## Tag 0FCI, a lemma

[Tag 0FCI](https://stacks.math.columbia.edu/tag/0FCI) in the Stacks Project.

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L44). The attribute's comment: “=>”.

```lean
instance : CategoryTheory.isNoetherianObject.IsClosedUnderQuotients (C := C)
```

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L62). The attribute's comment: “<=”.

```lean
instance : CategoryTheory.isNoetherianObject.IsClosedUnderExtensions (C := C)
```

**`CategoryTheory.isNoetherianObject_iff_of_shortExact`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L74).

> **Stacks 0FCI**: for a short exact sequence `0 ⟶ A₁ ⟶ A₂ ⟶ A₃ ⟶ 0` in an abelian
> category, `A₂` is Noetherian if and only if `A₁` and `A₃` are Noetherian.

```lean
lemma isNoetherianObject_iff_of_shortExact {S : ShortComplex C} (hS : S.ShortExact) :
    IsNoetherianObject S.X₂ ↔ IsNoetherianObject S.X₁ ∧ IsNoetherianObject S.X₃
```

Declarations registered for the tag:

- [`CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instIsClosedUnderSubobjectsIsNoetherianObject#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Subobject/NoetherianObject.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Subobject/NoetherianObject.lean#L17) (StacksCore): “=>”. References: SGA 4 VI (1.30.1), “more general”.

## Tag 0FCJ, a lemma

[Tag 0FCJ](https://stacks.math.columbia.edu/tag/0FCJ) in the Stacks Project.

**`CategoryTheory.isArtinianObject_and_isNoetherianObject_iff_exists_filtration`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/JordanHolder.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/JordanHolder.lean#L114).

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

**`CategoryTheory.Subobject.jordan_holder`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/JordanHolder.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/JordanHolder.lean#L132). The attribute's comment: “the quotient `a (i + 1) / a i` is indexed by `i : Fin n`; the Artinian and Noetherian hypothesis of Stacks follows from the filtrations by 0FCJ and is not assumed”.

> **Stacks 0FCK (Jordan–Hölder).** Let `X` be an object of an abelian category with two
> filtrations `0 = a 0 ⊆ a 1 ⊆ ⋯ ⊆ a n = X` and `0 = b 0 ⊆ b 1 ⊆ ⋯ ⊆ b m = X` by subobjects whose
> successive quotients `a (i + 1) / a i` and `b (j + 1) / b j` are simple. Then `n = m`, and there
> is a permutation `σ : Fin n ≃ Fin m` with `a (i + 1) / a i ≅ b (σ i + 1) / b (σ i)` for every `i`.
>
> Stacks indexes the quotients `Sᵢ = Aᵢ/Aᵢ₋₁` by `1 ≤ i ≤ n`; here the quotient `a (i + 1) / a i`
> is indexed by `i : Fin n`. Stacks assumes `X` satisfies the equivalent conditions of 0FCJ
> (Artinian and Noetherian); by 0FCJ (`isArtinianObject_and_isNoetherianObject_iff_exists_filtration`)
> this already follows from either filtration, so it is not assumed separately.

```lean
theorem jordan_holder (a : ℕ → Subobject X) (n : ℕ) (ha : ∀ i, i < n → a i ≤ a (i + 1))
    (ha0 : a 0 = ⊥) (han : a n = ⊤)
    (hsa : ∀ i (hi : i < n), Simple (cokernel (ofLE _ _ (ha i hi))))
    (b : ℕ → Subobject X) (m : ℕ) (hb : ∀ j, j < m → b j ≤ b (j + 1))
    (hb0 : b 0 = ⊥) (hbm : b m = ⊤)
    (hsb : ∀ j (hj : j < m), Simple (cokernel (ofLE _ _ (hb j hj)))) :
    n = m ∧ ∃ σ : Fin n ≃ Fin m, ∀ i : Fin n,
      Nonempty (cokernel (ofLE _ _ (ha i i.2)) ≅ cokernel (ofLE _ _ (hb (σ i) (σ i).2)))
```

Declarations registered for the tag:

- [`CompositionSeries.jordan_holder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CompositionSeries.jordan_holder#doc) registered with `add_to_stacks` in [StacksCore/Order/JordanHolder.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Order/JordanHolder.lean#L8) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.9, Tag 0FCD](https://stacks.math.columbia.edu/tag/0FCD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
