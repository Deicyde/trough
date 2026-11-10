---
declaration: section
origin: cited
lean: CategoryTheory.DottedArrow, CategoryTheory.DottedArrow.Hom, AlgebraicGeometry.Stack.isSetoidCategory_dottedArrow_of_isSeparated_relativeDiagonal, CategoryTheory.instGroupoidDottedArrow, AlgebraicGeometry.Stack.nonempty_dottedArrow_equivalence_of_forall_exists_whiskerLeft, AlgebraicGeometry.Stack.nonempty_dottedArrow_iff_exists_diagonal, CategoryTheory.DottedArrowBaseChange.dottedArrows_baseChange_equivalence, CategoryTheory.DottedArrow.toWithFactorization_isEquivalence
statement: formalized
proof: formalized
---

# 101.39 Valuative criteria

Section 101.39 of the Stacks Project, [Tag 0CL9](https://stacks.math.columbia.edu/tag/0CL9). 14 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CLA, a definition

[Tag 0CLA](https://stacks.math.columbia.edu/tag/0CLA) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.DottedArrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L41) (StacksFrontier): “dotted arrows”.
- [`CategoryTheory.DottedArrow.Hom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L102), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L42) (StacksFrontier): “morphisms of dotted arrows”.

## Tag 0CLC, a lemma

[Tag 0CLC](https://stacks.math.columbia.edu/tag/0CLC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSetoidCategory_dottedArrow_of_isSeparated_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDottedGroupoid.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionDottedGroupoid.lean#L318). The attribute's comment: “setoid”.

> **Stacks 0CLC, the setoid assertion.** If the relative diagonal `Δ_f` of a 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is separated in the sense of Stacks 04XB, then the
> category of dotted arrows of every valuative diagram for `f` is a setoid.
>
> The category is a groupoid because the 2-category of categories fibred in groupoids is locally
> groupoidal, so only the triviality of automorphisms is at issue. The two compatibility conditions
> on an automorphism `θ` of a dotted arrow say that `θ` lies in the relative inertia of `f` and is
> trivial at the generic point; separatedness of `Δ_f` makes the neutral section of the relative
> inertia a closed immersion, and
> `AlgebraicGeometry.Stack.eq_id_of_isClosedImmersion_relativeInertiaNeutralSection` concludes,
> the spectrum of a valuation ring being reduced and its generic point dominant.

```lean
theorem isSetoidCategory_dottedArrow_of_isSeparated_relativeDiagonal (f : 𝒳 ⟶ 𝒴)
    (hf : IsSeparated B S hS (relativeDiagonal.{u, u, u + 1} B S hS 𝒳.val 𝒴.val f.hom))
    (D : ValuativeDiagram B S hS 𝒳 𝒴 f) :
    IsSetoidCategory (CategoryTheory.DottedArrow D.x D.j f.hom D.y D.γ)
```

Declarations registered for the tag:

- [`CategoryTheory.instGroupoidDottedArrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Defs.lean#L169), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L43) (StacksFrontier): “groupoid”.

## Tag 0CLD, a lemma

[Tag 0CLD](https://stacks.math.columbia.edu/tag/0CLD) in the Stacks Project.

**`AlgebraicGeometry.Stack.nonempty_dottedArrow_equivalence_of_forall_exists_whiskerLeft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean#L175). The attribute's comment: “1 of 2: independence of the witness”.

> When the inertia `I_𝒴 ⟶ 𝒴` is proper, the category of
> dotted arrows of a valuative diagram is independent, up to a noncanonical equivalence, of the
> 2-morphism witnessing the 2-commutativity.

```lean
theorem nonempty_dottedArrow_equivalence_of_forall_exists_whiskerLeft
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hI : IsProper B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒴).hom)
    (D : ValuativeDiagram B S hS 𝒳 𝒴 f)
    (γ γ' : (D.j ≫ D.y) ⟶ (D.x ≫ f.hom)) :
    Nonempty (CategoryTheory.DottedArrow D.x D.j f.hom D.y γ ≌
      CategoryTheory.DottedArrow D.x D.j f.hom D.y γ')
```

**`AlgebraicGeometry.Stack.nonempty_dottedArrow_iff_exists_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean#L191). The attribute's comment: “2 of 2: existence for some and hence every witness”.

> When the inertia `I_𝒴 ⟶ 𝒴` is proper, a dotted arrow of a valuative diagram exists — for
> one and hence for every witnessing 2-morphism — exactly when there is a diagonal 1-morphism
> `a : Spec R ⟶ 𝒳` with 2-morphisms `a ∘ j ⟶ x` and `y ⟶ f ∘ a`, with no condition relating
> them to the witness.

```lean
theorem nonempty_dottedArrow_iff_exists_diagonal
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hI : IsProper B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒴).hom)
    (D : ValuativeDiagram B S hS 𝒳 𝒴 f)
    (γ : (D.j ≫ D.y) ⟶ (D.x ≫ f.hom)) :
    Nonempty (CategoryTheory.DottedArrow D.x D.j f.hom D.y γ) ↔
      ∃ a : schemeFibredCategory B S hS D.whole ⟶ 𝒳.1,
        Nonempty ((D.j ≫ a) ⟶ D.x) ∧ Nonempty (D.y ⟶ (a ≫ f.hom))
```

## Tag 0CLE, a lemma

[Tag 0CLE](https://stacks.math.columbia.edu/tag/0CLE) in the Stacks Project.

**`CategoryTheory.DottedArrowBaseChange.dottedArrows_baseChange_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/NonExercises/DottedArrowsBaseChange.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrowsBaseChange.lean#L306).

> **Stacks 0CLE.** The category of dotted arrows is invariant under base change along a
> $2$-cartesian square.
>
> Split a $2$-commutative rectangle into a left square, filled by `γ'`, and a right square,
> filled by `φ` and assumed $2$-cartesian. Then the category of dotted arrows of the left square
> is equivalent to the category of dotted arrows of the outer rectangle, whose filler is the
> pasting of `γ'` and `φ`.

```lean
theorem dottedArrows_baseChange_equivalence
    {S T X X' Y Y' : B}
    (j : S ⟶ T) (x' : S ⟶ X') (q : X' ⟶ X) (p : X' ⟶ Y')
    (f : X ⟶ Y) (y' : T ⟶ Y') (g : Y' ⟶ Y)
    (φ : (p ≫ g) ≅ (q ≫ f)) (γ' : (j ≫ y') ≅ (x' ≫ p))
    (hcart : IsTwoCartesian q p f g φ) :
    Nonempty (CategoryTheory.DottedArrow x' j p y' γ'.hom ≌
      CategoryTheory.DottedArrow (x' ≫ q) j f (y' ≫ g)
          ((α_ j y' g).symm ≪≫ whiskerRightIso γ' g ≪≫ (α_ x' p g) ≪≫
            whiskerLeftIso x' φ ≪≫ (α_ x' q f).symm).hom)
```

## Tag 0CLF, a lemma

[Tag 0CLF](https://stacks.math.columbia.edu/tag/0CLF) in the Stacks Project.

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

Declarations registered for the tag:

- [`CategoryTheory.DottedArrow.toWithFactorization_isEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L400), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L44) (StacksFrontier): “equivalence with the intermediate category”.
- [`CategoryTheory.DottedArrow.compose_isFiberedInGroupoids`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L778), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L46) (StacksFrontier): “fibration over the lower dotted-arrow category”.
- [`CategoryTheory.DottedArrow.fiber_categoryIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DottedArrows/Composition.lean#L624), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/NonExercises/DottedArrows.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/NonExercises/DottedArrows.lean#L48) (StacksFrontier): “fibre categories are upper dotted-arrow categories”.

## Tag 0CLG, a definition

[Tag 0CLG](https://stacks.math.columbia.edu/tag/0CLG) in the Stacks Project.

**`AlgebraicGeometry.Stack.ValuativeCriterion.Uniqueness`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean#L97).

> A 1-morphism of algebraic stacks satisfies the *uniqueness part of the
> valuative criterion* when, for every valuative diagram for it, the category of dotted arrows
> is either empty or a setoid with exactly one isomorphism class.

```lean
abbrev Uniqueness
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CLH, a lemma

[Tag 0CLH](https://stacks.math.columbia.edu/tag/0CLH) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionUniqueness_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionBaseChange.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionBaseChange.lean#L198).

> **Stacks 0CLH.** A base change of a 1-morphism of algebraic stacks satisfying the uniqueness
> part of the valuative criterion satisfies it as well.
>
> The base change of `f : 𝒳 ⟶ 𝒴` along `g : 𝒴' ⟶ 𝒴` is the first projection of a 2-fibre product
> `P` of the cospan `(g, f)`.

```lean
theorem valuativeCriterionUniqueness_baseChange
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : ValuativeCriterion.Uniqueness B S hS f) :
    ValuativeCriterion.Uniqueness B S hS P.fst
```

## Tag 0CLI, a lemma

[Tag 0CLI](https://stacks.math.columbia.edu/tag/0CLI) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionUniqueness_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniqueness.lean#L111).

> The composition of two 1-morphisms of algebraic stacks satisfying the
> uniqueness part of the valuative criterion satisfies it as well.

```lean
theorem valuativeCriterionUniqueness_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : ValuativeCriterion.Uniqueness B S hS f)
    (hg : ValuativeCriterion.Uniqueness B S hS g) :
    ValuativeCriterion.Uniqueness B S hS (f ≫ g)
```

## Tag 0CLJ, a lemma

[Tag 0CLJ](https://stacks.math.columbia.edu/tag/0CLJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionUniqueness_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniquenessPoints.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionUniquenessPoints.lean#L522).

> **Stacks 0CLJ.** For a 1-morphism of algebraic stacks representable by algebraic spaces, the
> uniqueness part of the valuative criterion holds exactly when it holds for every base change to
> an algebraic space along a scheme-valued point of the target.
>
> The base change is described exactly as in Stacks 02ZW: for an object `U` of the site and a
> scheme-valued point `y` of `𝒴` over `U`, it is the first projection of the 2-fibre product
> `U ×_𝒴 𝒳`, and the condition is imposed on the structure morphism of *any* algebraic space `F`
> over `U` equivalent to it over the site of `U`. Quantifying over all such `F` rather than over a
> chosen one spares a consumer the transport along a comparison equivalence.

```lean
theorem valuativeCriterionUniqueness_iff_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    ValuativeCriterion.Uniqueness B S hS f ↔
      ∀ U : BigFppfOver B S hS,
        let 𝒰 := BigFppfOver B U.left.1 U.left.2
        let p𝒰 : 𝒰 ⥤ BigFppfOver B S hS := Over.map U.hom
        ∀ (y : 𝒰 ⥤ 𝒴.val.val.obj) (_hy : y ⋙ 𝒴.val.val.p = p𝒰) (F : 𝒰ᵒᵖ ⥤ Type u)
          (_hF : IsAlgebraicSpace B U.left.1 U.left.2 F)
          (_e : StacksRepresentableCFG.EquivalenceOver
            (TwoFibreProductOver.fst p𝒰 𝒳.val.val.p 𝒴.val.val.p y f.hom.hom.toFunctor)
            (presheafOfCategories (F ⋙ typeToCat)).p)
          (p : F ⟶ yoneda.obj (Over.mk (𝟙 (B.obj U.left.2)))),
          Space.ValuativeCriterion.Uniqueness p
```

## Tag 0CLK, a definition

[Tag 0CLK](https://stacks.math.columbia.edu/tag/0CLK) in the Stacks Project.

**`AlgebraicGeometry.Stack.ValuativeCriterion.Existence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterion.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterion.lean#L420).

> A 1-morphism of algebraic stacks satisfies the *existence part of the valuative criterion* when
> every valuative square for it admits a dotted arrow after an extension of the fraction field and
> passage to a dominating valuation ring.

```lean
abbrev Existence (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CLL, a lemma

[Tag 0CLL](https://stacks.math.columbia.edu/tag/0CLL) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionExistence_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionBaseChange.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionBaseChange.lean#L244).

> **Stacks 0CLL.** A base change of a 1-morphism of algebraic stacks satisfying the existence
> part of the valuative criterion satisfies it as well.
>
> The base change of `f : 𝒳 ⟶ 𝒴` along `g : 𝒴' ⟶ 𝒴` is the first projection of a 2-fibre product
> `P` of the cospan `(g, f)`.

```lean
theorem valuativeCriterionExistence_baseChange
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hf : ValuativeCriterion.Existence B S hS f) :
    ValuativeCriterion.Existence B S hS P.fst
```

## Tag 0CLM, a lemma

[Tag 0CLM](https://stacks.math.columbia.edu/tag/0CLM) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionExistence_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterion.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterion.lean#L497).

> The composition of two 1-morphisms of algebraic stacks satisfying the existence part of the
> valuative criterion satisfies it as well.

```lean
theorem valuativeCriterionExistence_comp
    {𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : ValuativeCriterion.Existence B S hS f)
    (hg : ValuativeCriterion.Existence B S hS g) :
    ValuativeCriterion.Existence B S hS (f ≫ g)
```

## Tag 0CLN, a lemma

[Tag 0CLN](https://stacks.math.columbia.edu/tag/0CLN) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionExistence_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionExistencePoints.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionExistencePoints.lean#L730).

> **Stacks 0CLN.** For a 1-morphism of algebraic stacks representable by algebraic spaces, the
> existence part of the valuative criterion holds exactly when it holds for every base change to an
> algebraic space along a scheme-valued point of the target.
>
> The base change is described exactly as in Stacks 02ZW: for an object `U` of the site and a
> scheme-valued point `y` of `𝒴` over `U`, it is the first projection of the 2-fibre product
> `U ×_𝒴 𝒳`, and the condition is imposed on the structure morphism of *any* algebraic space `F`
> over `U` equivalent to it over the site of `U`. Quantifying over all such `F` rather than over a
> chosen one spares a consumer the transport along a comparison equivalence.

```lean
theorem valuativeCriterionExistence_iff_baseChange (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    ValuativeCriterion.Existence B S hS f ↔
      ∀ U : BigFppfOver B S hS,
        let 𝒰 := BigFppfOver B U.left.1 U.left.2
        let p𝒰 : 𝒰 ⥤ BigFppfOver B S hS := Over.map U.hom
        ∀ (y : 𝒰 ⥤ 𝒴.val.val.obj) (_hy : y ⋙ 𝒴.val.val.p = p𝒰) (F : 𝒰ᵒᵖ ⥤ Type u)
          (_hF : IsAlgebraicSpace B U.left.1 U.left.2 F)
          (_e : StacksRepresentableCFG.EquivalenceOver
            (TwoFibreProductOver.fst p𝒰 𝒳.val.val.p 𝒴.val.val.p y f.hom.hom.toFunctor)
            (presheafOfCategories (F ⋙ typeToCat)).p)
          (p : F ⟶ yoneda.obj (Over.mk (𝟙 (B.obj U.left.2)))),
          Space.ValuativeCriterion.Existence p
```

## Tag 0CLP, a lemma

[Tag 0CLP](https://stacks.math.columbia.edu/tag/0CLP) in the Stacks Project.

**`AlgebraicGeometry.Stack.valuativeCriterionUniqueness_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionClosedImmersion.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionClosedImmersion.lean#L135). The attribute's comment: “uniqueness”.

> **Stacks 0CLP, the uniqueness part.** A closed immersion of algebraic stacks over `S`
> satisfies the uniqueness part of the valuative criterion (**Stacks 0CLG**).
>
> By Stacks 0CLJ it is enough that every presheaf representing a base change of `f` along a
> scheme-valued point of `𝒴` have structural morphism satisfying the uniqueness criterion for
> presheaves; those presheaves have at most one section over every object by
> `AlgebraicGeometry.Stack.subsingleton_baseChange_of_isClosedImmersion`, so every morphism out of
> them is a monomorphism.

```lean
theorem valuativeCriterionUniqueness_of_isClosedImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsClosedImmersion B S hS f) :
    ValuativeCriterion.Uniqueness B S hS f
```

**`AlgebraicGeometry.Stack.valuativeCriterionExistence_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionClosedImmersion.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ValuativeCriterionClosedImmersion.lean#L160). The attribute's comment: “existence”.

> **Stacks 0CLP, the existence part.** A closed immersion of algebraic stacks over `S` satisfies
> the existence part of the valuative criterion (**Stacks 0CLK**).
>
> By Stacks 0CLN it is enough that every presheaf representing a base change of `f` along a
> scheme-valued point of `𝒴` have structural morphism satisfying the existence criterion for
> presheaves. The closed immersion condition of Stacks 04YL is a condition on the structural
> morphism of the lower-shriek extension of that presheaf, and
> `AlgebraicGeometry.Space.valuativeCriterionExistence_of_isClosedImmersion_relocalizeToYoneda`
> turns it into the existence criterion for every morphism from the presheaf to the terminal
> presheaf on the site of the point — which is the shape Stacks 0CLN asks for.

```lean
theorem valuativeCriterionExistence_of_isClosedImmersion (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsClosedImmersion B S hS f) :
    ValuativeCriterion.Existence B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.39, Tag 0CL9](https://stacks.math.columbia.edu/tag/0CL9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
