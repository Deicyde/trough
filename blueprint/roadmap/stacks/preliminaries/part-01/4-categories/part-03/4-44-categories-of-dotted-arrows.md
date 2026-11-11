---
declaration: section
origin: cited
lean: CategoryTheory.DottedArrow, CategoryTheory.DottedArrow.Hom, CategoryTheory.instCategoryDottedArrow, CategoryTheory.DottedArrowBaseChange.dottedArrows_equiv, CategoryTheory.DottedArrow.toWithFactorization_isEquivalence, CategoryTheory.DottedArrow.fiber_categoryIso, CategoryTheory.DottedArrow.compose_isFiberedInGroupoids
statement: formalized
proof: formalized
---

# 4.44 Categories of dotted arrows

Section 4.44 of the Stacks Project, [Tag 0H17](https://stacks.math.columbia.edu/tag/0H17). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H18, a definition

[Tag 0H18](https://stacks.math.columbia.edu/tag/0H18) in the Stacks Project.

**`CategoryTheory.DottedArrow`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Defs.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L74).

> A **dotted arrow** for the `2`-commutative square with `x : S ⟶ X`, `j : S ⟶ T`,
> `f : X ⟶ Y`, `y : T ⟶ Y` and witnessing `2`-morphism `γ : j ≫ y ⟶ x ≫ f`: a diagonal
> `1`-morphism `a : T ⟶ X` together with `2`-morphisms `α : j ≫ a ⟶ x` and `β : y ⟶ a ≫ f`
> pasting to `γ`.

```lean
structure DottedArrow {S T X Y : B} (x : S ⟶ X) (j : S ⟶ T) (f : X ⟶ Y) (y : T ⟶ Y)
    (γ : (j ≫ y) ⟶ (x ≫ f))
```

**`CategoryTheory.DottedArrow.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Defs.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L102).

> A **morphism of dotted arrows** `(a, α, β) ⟶ (a', α', β')` is a `2`-morphism
> `θ : a ⟶ a'` such that `α = α' ∘ (θ ⋆ id_j)` and `β' = (id_f ⋆ θ) ∘ β`.

```lean
structure Hom (d d' : DottedArrow x j f y γ)
```

**`CategoryTheory.instCategoryDottedArrow`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Defs.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L136).

> The **category of dotted arrows** for the square and the witness `γ`: objects are dotted
> arrows and morphisms are morphisms of dotted arrows.

```lean
instance instCategoryDottedArrow {S T X Y : B} {x : S ⟶ X} {j : S ⟶ T} {f : X ⟶ Y} {y : T ⟶ Y}
    {γ : (j ≫ y) ⟶ (x ≫ f)} : Category (DottedArrow x j f y γ)
```

## Tag 0H1A, a lemma

[Tag 0H1A](https://stacks.math.columbia.edu/tag/0H1A) in the Stacks Project.

**`CategoryTheory.DottedArrowBaseChange.dottedArrows_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/BaseChange.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/BaseChange.lean#L622).

> **Theorem (Stacks Project, Tag 0H1A / Lemma 4.44.2).**
>
> Let `B` be a $(2,1)$-category (a bicategory in which every $2$-morphism is invertible,
> encoded by the hypothesis `hgpd`). Given a $2$-commutative diagram with an
> outer rectangle decomposed into a left square (with witness `γ'`) and a right square that
> is $2$-cartesian (with witness `φ`), the category of dotted arrows `D'` for the left square
> and the category of dotted arrows `D` for the outer rectangle (with the induced witness
> `γ = outerGamma φ γ'`) are equivalent categories.

```lean
theorem dottedArrows_equiv
    (hgpd : ∀ {A C : B} {u v : A ⟶ C} (θ : u ⟶ v), IsIso θ)
    {S T X X' Y Y' : B}
    (j : S ⟶ T) (x' : S ⟶ X') (q : X' ⟶ X) (p : X' ⟶ Y') (f : X ⟶ Y)
    (y' : T ⟶ Y') (g : Y' ⟶ Y)
    (φ : (p ≫ g) ≅ (q ≫ f)) (γ' : (j ≫ y') ≅ (x' ≫ p))
    (hcart : IsTwoCartesian q p f g φ) :
    -- `D'` : dotted arrows for the left square `(x', j, p, y')` with witness `γ'`
    -- `D`  : dotted arrows for the outer rectangle `(x' ≫ q, j, f, y' ≫ g)` with witness `γ`
    Nonempty (IsoDottedArrow x' j p y' γ' ≌
              IsoDottedArrow (x' ≫ q) j f (y' ≫ g) (outerGamma φ γ'))
```

## Tag 0H1B, a lemma

[Tag 0H1B](https://stacks.math.columbia.edu/tag/0H1B) in the Stacks Project.

**`CategoryTheory.DottedArrow.toWithFactorization_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Composition.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L400).

> `toWithFactorization` is an equivalence of categories `𝒟 ≌ 𝒟''`.

```lean
instance toWithFactorization_isEquivalence {S T X Y Z : B} (x : S ⟶ X) (j : S ⟶ T) (f : X ⟶ Y)
    (g : Y ⟶ Z) (z : T ⟶ Z) (γ : (j ≫ z) ⟶ (x ≫ f ≫ g)) :
    (toWithFactorization x j f g z γ).IsEquivalence
```

**`CategoryTheory.DottedArrow.fiber_categoryIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Composition.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L624).

> The fibre of `compose` over an object `d'` of `𝒟'` is isomorphic, as a category (a
> `CategoryIso`, not merely an equivalence), to the category of dotted arrows of the upper solid
> square, whose bottom arrow is `d'.a` and whose witness is `d'.α`.

```lean
theorem fiber_categoryIso {S T X Y Z : B}
    (x : S ⟶ X) (j : S ⟶ T) (f : X ⟶ Y) (g : Y ⟶ Z) (z : T ⟶ Z)
    (γ : (j ≫ z) ⟶ (x ≫ f ≫ g))
    (d' : DottedArrow (x ≫ f) j g z (γ ≫ (α_ x f g).inv)) :
    Nonempty (CategoryIso ((compose x j f g z γ).Fiber d')
      (DottedArrow x j f d'.a d'.α))
```

**`CategoryTheory.DottedArrow.compose_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DottedArrows/Composition.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L778).

> `compose : 𝒟'' ⥤ 𝒟'` is fibred in groupoids.

```lean
theorem compose_isFiberedInGroupoids {S T X Y Z : B} (x : S ⟶ X) (j : S ⟶ T) (f : X ⟶ Y)
    (g : Y ⟶ Z) (z : T ⟶ Z) (γ : (j ≫ z) ⟶ (x ≫ f ≫ g)) :
    (compose x j f g z γ).IsFiberedInGroupoids
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.44, Tag 0H17](https://stacks.math.columbia.edu/tag/0H17)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
