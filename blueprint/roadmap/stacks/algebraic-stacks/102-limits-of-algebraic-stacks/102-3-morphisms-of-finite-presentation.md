---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsLimitPreserving, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isLimitPreserving, AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProductSnd, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_twoFibreProductSnd, AlgebraicGeometry.Stack.isLimitPreserving_comp, AlgebraicGeometry.Stack.isLimitPreserving_tfae, AlgebraicGeometry.Stack.isLimitPreservingOnObjects_iff_isLocallyOfFinitePresentation, AlgebraicGeometry.Stack.isFullyFaithfulOnAffineLimits_iff_isEquivalence_squareDiagonalComparison
statement: formalized
proof: formalized
---

# 102.3 Morphisms of finite presentation

Section 102.3 of the Stacks Project, [Tag 0CMQ](https://stacks.math.columbia.edu/tag/0CMQ). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CMR, a definition

[Tag 0CMR](https://stacks.math.columbia.edu/tag/0CMR) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsLimitPreserving`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphism.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphism.lean#L138).

> **Stacks 0CMR.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big
> fppf category of `S` is *limit preserving* when, for every cofiltered inverse system of affine
> schemes over `S` whose image in schemes has a limiting cone, the canonical square
>
> `colim 𝒳_{Uᵢ} ⟶ 𝒳_U`, `colim 𝒴_{Uᵢ} ⟶ 𝒴_U`
>
> of fibre categories, with vertical maps induced by `f`, is a 2-fibre product.
>
> The square is the determinate one: the vertical map out of the colimit is the colimit of the
> componentwise maps `AlgebraicGeometry.Stack.splitFiberMap` of strict split fibres, and the
> filling 2-cell is, on every colimit generator, the canonical base-change comparison of the
> fibred 1-morphism underlying `f`.

```lean
abbrev IsLimitPreserving (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CMS, a lemma

[Tag 0CMS](https://stacks.math.columbia.edu/tag/0CMS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismObjects.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismObjects.lean#L77).

> **Stacks 0CMS.** A limit preserving 1-morphism of categories fibred in groupoids over the big
> fppf category of `S` is limit preserving on objects: every object over an affine inverse limit,
> with a cartesian comparison to an object at a finite stage, descends to a later stage.

```lean
theorem isLimitPreservingOnObjects_of_isLimitPreserving
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, vX, u + 1, uX}
      (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsLimitPreserving.{u, v, w, uX, vX} B S hS f) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, vX, uX}
      B S hS 𝒳 𝒴 f
```

## Tag 0CMT, a lemma

[Tag 0CMT](https://stacks.math.columbia.edu/tag/0CMT) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingBaseChangeCoherence.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingBaseChangeCoherence.lean#L646).

> **Stacks 0CMT.** The base change `p' : 𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of a limit preserving 1-morphism `p` of
> categories fibred in groupoids over the big fppf category of a scheme `S` is limit preserving.
>
> Both conditions are properties of `AlgebraicGeometry.Stack.canonicalSquare` -- of `p'` for the
> conclusion and of `p` for the hypothesis -- by
> `AlgebraicGeometry.Stack.isLimitPreserving_iff_isTwoFibreProduct_canonicalSquare`, and the two
> squares are 2-cartesian together by
> `AlgebraicGeometry.Stack.isEquivalence_squareComparison_canonicalSquare_twoFibreProductSnd`. The
> input the source leaves implicit is that filtered colimits of categories commute with 2-fibre
> products, which is what identifies `colim (𝒳 ×_𝒴 𝒵)_{Uᵢ}` with
> `colim 𝒳_{Uᵢ} ×_{colim 𝒴_{Uᵢ}} colim 𝒵_{Uᵢ}`.

```lean
theorem isLimitPreserving_twoFibreProductSnd
    (hp : IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS p) :
    IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS
      (BigFppfOver.twoFibreProductSnd.{u, v, w} B S hS 𝒳 𝒴 𝒵 p q)
```

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingBaseChangeObjects.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingBaseChangeObjects.lean#L52). The attribute's comment: “limit preservation on objects of the base change”.

> The base change along `q` of a limit preserving 1-morphism `p` of categories fibred in
> groupoids over the big fppf category of `S` is limit preserving on objects: every object of
> `𝒳 ×_𝒴 𝒵` over an affine inverse limit, with a cartesian comparison to an object of `𝒵` at a
> finite stage, descends to a later stage.

```lean
theorem isLimitPreservingOnObjects_twoFibreProductSnd
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒵 ⟶ 𝒴)
    (hp : IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS p) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, v, w} B S hS
      (BigFppfOver.twoFibreProduct B S hS 𝒳 𝒴 𝒵 p q) 𝒵
      (BigFppfOver.twoFibreProductSnd B S hS 𝒳 𝒴 𝒵 p q)
```

## Tag 0CMU, a lemma

[Tag 0CMU](https://stacks.math.columbia.edu/tag/0CMU) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreserving_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismComposition.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismComposition.lean#L134).

> **Stacks 0CMU.** The composite of two limit preserving 1-morphisms of categories fibred in
> groupoids over the big fppf category of `S` is limit preserving: the square of Stacks 0CMR for
> the composite is the horizontal pasting of the two given 2-cartesian squares.

```lean
theorem isLimitPreserving_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, vX, u + 1, uX} (BigFppfOver B S hS)}
    (p : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : IsLimitPreserving.{u, v, w, uX, vX} B S hS p)
    (hq : IsLimitPreserving.{u, v, w, uX, vX} B S hS q) :
    IsLimitPreserving.{u, v, w, uX, vX} B S hS (p ≫ q)
```

## Tag 0CMV, a lemma

[Tag 0CMV](https://stacks.math.columbia.edu/tag/0CMV) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismObjects.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingMorphismObjects.lean#L77). The attribute's comment: “the implication (1) ⇒ (2), which holds here without the representability hypothesis that Tag 0CMV carries, and for index categories in any universe. The whole three-part equivalence is `AlgebraicGeometry.Stack.isLimitPreserving_tfae`, for index categories in the universe of the schemes”.

> **Stacks 0CMS.** A limit preserving 1-morphism of categories fibred in groupoids over the big
> fppf category of `S` is limit preserving on objects: every object over an affine inverse limit,
> with a cartesian comparison to an object at a finite stage, descends to a later stage.

```lean
theorem isLimitPreservingOnObjects_of_isLimitPreserving
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, vX, u + 1, uX}
      (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : IsLimitPreserving.{u, v, w, uX, vX} B S hS f) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, vX, uX}
      B S hS 𝒳 𝒴 f
```

**`AlgebraicGeometry.Stack.isLimitPreserving_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentableTFAE.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentableTFAE.lean#L134). The attribute's comment: “index categories in the universe of the schemes”.

> **Stacks 0CMV.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big
> fppf category of `S` which is representable by algebraic spaces the following are equivalent:
> `f` is limit preserving (Stacks 0CMR); `f` is limit preserving on objects (Stacks 06CU); and `f`
> is locally of finite presentation in the sense of Stacks 03YK, that is, every algebraic space
> representing a base change of `f` along a scheme-valued point of `𝒴` has locally finitely
> presented structural morphism.
>
> All three conditions are read for index categories in the universe of the schemes; see the
> implementation notes.

```lean
theorem isLimitPreserving_tfae (hp : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    List.TFAE
      [IsLimitPreserving.{u, u, u, u + 1, u} B S hS f,
       BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳 𝒴 f,
       ∀ (U : BigFppfOver B S hS)
         (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
         (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
         (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
         (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
         Nonempty (StacksRepresentableCFG.EquivalenceOver
           (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
             (CatFiberedInGroupoids.homFunctor f))
           (presheafOfCategories (F ⋙ typeToCat)).p) →
         Space.IsLocallyOfFinitePresentation B S hS
           (algebraicSpaceMap B S hS U
             ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj
               ⟨F, hF⟩)).hom]
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.isLimitPreservingOnObjects_iff_isLocallyOfFinitePresentation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/LimitPreservingFinitePresentation.lean#L883), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentableTFAE.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingRepresentableTFAE.lean#L90) (StacksFrontier): “the equivalence of (2) and (3), which is Stacks 06CX”.

## Tag 0CMW, a lemma

[Tag 0CMW](https://stacks.math.columbia.edu/tag/0CMW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFullyFaithfulOnAffineLimits_iff_isEquivalence_squareDiagonalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingCanonicalDiagonal.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingCanonicalDiagonal.lean#L252). The attribute's comment: “condition (2) as the diagonal of the canonical 0CMR square being an equivalence”.

> **Condition (2) of Stacks 0CMW is the diagonal of the canonical square being an
> equivalence.** The canonical functor `colim 𝒳_{Uᵢ} ⟶ 𝒳_U ×_{𝒴_U} colim 𝒴_{Uᵢ}` is fully faithful
> at every directed limit of affine schemes over `S` exactly when, at every such limit, the
> comparison of the square of relative diagonals of `AlgebraicGeometry.Stack.canonicalSquare` is an
> equivalence.
>
> This is the half of Stacks 0CMW that does not involve the diagonal 1-morphism
> `Δ : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳`: it is the category-theoretic criterion of the source's proof, applied to the
> determinate square of Stacks 0CMR.

```lean
theorem isFullyFaithfulOnAffineLimits_iff_isEquivalence_squareDiagonalComparison (f : 𝒳 ⟶ 𝒴) :
    IsFullyFaithfulOnAffineLimits.{u, v, w, uX, vX} B S hS f ↔
      ∀ (I : Type v) [Category.{w} I] [IsCofiltered I]
        (D : I ⥤ BigAffineFppf B S hS) (c : Cone D),
        IsLimit ((BigAffineFppf.toScheme B S hS).mapCone c) →
        (Cat.squareDiagonalComparison
          (canonicalSquare.{u, v, w, uX, vX} B S hS f (D ⋙ BigAffineFppf.inclusion B S hS)
            ((BigAffineFppf.inclusion B S hS).mapCone c))).IsEquivalence
```

**`AlgebraicGeometry.Stack.isFullyFaithfulOnAffineLimits_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonal.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonal.lean#L135). The attribute's comment: “condition (2) holds for a limit preserving 1-morphism”.

> **Stacks 0CMW, condition (2) for a limit preserving 1-morphism.** If the square of
> Stacks 0CMR is 2-cartesian then its comparison functor into the explicit 2-fibre product is an
> equivalence, so the canonical functor `colim 𝒳_{Uᵢ} ⟶ 𝒳_U ×_{𝒴_U} colim 𝒴_{Uᵢ}` is fully
> faithful.

```lean
theorem isFullyFaithfulOnAffineLimits_of_isLimitPreserving (f : 𝒳 ⟶ 𝒴)
    (hf : IsLimitPreserving.{u, v, w, uX, vX} B S hS f) :
    IsFullyFaithfulOnAffineLimits.{u, v, w, uX, vX} B S hS f
```

**`AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProductDiagonal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonalCriterion.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonalCriterion.lean#L293).

> **Stacks 0CMW.** The relative diagonal `Δ : 𝒳 ⟶ 𝒳 ×_{f, 𝒴, f} 𝒳` of a 1-morphism of
> categories fibred in groupoids over the big fppf category of `S` is limit preserving if and only
> if, at every directed limit `U = lim Uᵢ` of affine schemes over `S`, the canonical functor
> `colim 𝒳_{Uᵢ} ⟶ 𝒳_U ×_{𝒴_U} colim 𝒴_{Uᵢ}` is fully faithful.
>
> Both sides are properties of `AlgebraicGeometry.Stack.canonicalSquare` -- of `Δ` on the left, of
> `f` on the right -- and the two squares are equivalent, so the source's criterion
> `CategoryTheory.Limits.CategoricalPullback.fullyFaithful_squareComparison_iff` transfers between
> them.

```lean
theorem isLimitPreserving_twoFibreProductDiagonal_iff :
    IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS
        (BigFppfOver.twoFibreProductDiagonal.{u, v, w} B S hS 𝒳 𝒴 f) ↔
      IsFullyFaithfulOnAffineLimits.{u, v, w, max (u + 1) v w, max u v} B S hS f
```

**`AlgebraicGeometry.Stack.isLimitPreserving_twoFibreProductDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonalCriterion.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingDiagonalCriterion.lean#L317).

> **Stacks 0CMW, the "in particular" clause.** A limit preserving 1-morphism of categories
> fibred in groupoids has a limit preserving relative diagonal: it satisfies the full faithfulness
> condition by
> `AlgebraicGeometry.Stack.isFullyFaithfulOnAffineLimits_of_isLimitPreserving`, and that condition
> is limit preservation of the diagonal.

```lean
theorem isLimitPreserving_twoFibreProductDiagonal
    (hf : IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS f) :
    IsLimitPreserving.{u, v, w, max (u + 1) v w, max u v} B S hS
      (BigFppfOver.twoFibreProductDiagonal.{u, v, w} B S hS 𝒳 𝒴 f)
```

**`CategoryTheory.Limits.CategoricalPullback.fullyFaithful_squareComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/TwoFibreProduct/CategoricalPullbackSquareDiagonal.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/TwoFibreProduct/CategoricalPullbackSquareDiagonal.lean#L490). The attribute's comment: “the category-theoretic reduction of the equivalence (1) <=> (2)”.

> **The category-theoretic core of Stacks 0CMW.** For a 2-commutative square of categories
> whose corners `C` and `D'` are groupoids, the comparison functor `A : C' ⥤ C ×_D D'` is fully
> faithful if and only if the comparison functor `B : C' ⥤ C ×_{Δ_p, C ×_D C} (C' ×_{D'} C')` of
> the square of relative diagonals is an equivalence.

```lean
theorem fullyFaithful_squareComparison_iff [IsGroupoid C] [IsGroupoid D'] :
    ((squareComparison a u p b α).Full ∧ (squareComparison a u p b α).Faithful) ↔
      (diagonalComparison a u p b α).IsEquivalence
```

## Tag 0CMX, a lemma

[Tag 0CMX](https://stacks.math.columbia.edu/tag/0CMX) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLimitPreserving_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingOfFinitePresentation.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingOfFinitePresentation.lean#L84). The attribute's comment: “an algebraic stack locally of finite presentation over S is limit preserving, and so is its structure morphism”.

> **Stacks 0CMX.** Let `𝒳` be an algebraic stack over `S` whose structure morphism `𝒳 → S` is
> locally of finite presentation. Then `𝒳` is limit preserving in the sense of Artin's Axioms,
> Definition 07XL: for every cofiltered system of affine schemes `Tᵢ` over `S` with limit `T`, the
> comparison functor `colim 𝒳_{Tᵢ} ⥤ 𝒳_T` is an equivalence. Equivalently, the structure morphism
> `𝒳 → S` is limit preserving in the sense of Stacks 0CMR. The index categories are taken in the
> scheme universe, which is the smallness the source's directed sets have.

```lean
theorem isLimitPreserving_of_isLocallyOfFinitePresentation
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hf : IsLocallyOfFinitePresentation B S hS (structureMorphism B S hS 𝒳)) :
    Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒳.val ∧
      Stack.IsLimitPreserving.{u, u, u, u + 1, u} B S hS (structureMorphism B S hS 𝒳).hom
```

**`AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_relativelyLimitPreserving_structure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingSmoothDiagram.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingSmoothDiagram.lean#L157). The attribute's comment: “only the smooth-diagram reduction; the conclusion is not 07XL”.

> **An algebraic stack locally of finite presentation over its base has a relatively limit
> preserving smooth presentation.** This is
> `AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_relativelyLimitPreserving` at the
> structure morphism of Stacks 050D, and it is the algebraic-spaces input to the proof of
> Stacks 0CMX: the presenting algebraic space of `𝒳` is relatively limit preserving over the
> algebraic stack represented by `S`.
>
> The attribute's clause string is deliberately narrow. This statement does **not** give the
> conclusion of Stacks 0CMX, which is limit preservation of `𝒳` in the sense of Definition 07XL;
> what it carries is the tag's first step, and it is the step that consumes the tag's hypothesis —
> `Stack.AlgebraicStacks.IsLocallyOfFinitePresentation` on the structure morphism of Stacks 050D is
> used, not merely stated. Anyone reading the tag as discharged by this declaration would be
> misreading it: the conclusion here is about a smooth presentation by an algebraic space, in the
> vocabulary of Stacks 049J, and the remaining step — limit preservation of the quotient stack — is
> named with its three missing bridges in the implementation notes of this module.

```lean
theorem hasPropertyOnSomeSmoothDiagram_relativelyLimitPreserving_structure
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
      (structureMorphism B S hS 𝒳)) :
    HasPropertyOnSomeSmoothDiagram B S hS
      (fun _ _ h => RelativelyLimitPreserving.{u, u, u, u} B S hS h)
      (structureMorphism B S hS 𝒳).hom
```

## Tag 0CMY, a proposition

[Tag 0CMY](https://stacks.math.columbia.edu/tag/0CMY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLimitPreserving_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingFinitePresentationEquivalence.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingFinitePresentationEquivalence.lean#L73). The attribute's comment: “limit preserving, limit preserving on objects and locally of finite presentation are equivalent for a 1-morphism of algebraic stacks”.

> For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are equivalent:
>
> 1. `f` is limit preserving in the sense of Stacks 0CMR;
> 2. `f` is limit preserving on objects in the sense of Stacks 06CU;
> 3. `f` is locally of finite presentation in the sense of Stacks 06Q2.
>
> Index categories are taken in the universe of the schemes.

```lean
theorem isLimitPreserving_tfae {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    List.TFAE [Stack.IsLimitPreserving.{u, u, u, u + 1, u} B S hS f.hom,
      BigFppfOver.IsLimitPreservingOnObjects.{u, u, u} B S hS 𝒳.val 𝒴.val f.hom,
      IsLocallyOfFinitePresentation B S hS f]
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_isLimitPreservingOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingObjectsFinitePresentation.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/LimitPreservingObjectsFinitePresentation.lean#L299). The attribute's comment: “the implication (2) => (3) only”.

> A 1-morphism of algebraic stacks over `S` which is limit preserving on objects, at index
> categories in the universe `u` of the schemes, is locally of finite presentation.

```lean
theorem AlgebraicStacks.isLocallyOfFinitePresentation_of_isLimitPreservingOnObjects
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1}
      B S hS 𝒳.val 𝒴.val f.hom) :
    Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 102.3, Tag 0CMQ](https://stacks.math.columbia.edu/tag/0CMQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
