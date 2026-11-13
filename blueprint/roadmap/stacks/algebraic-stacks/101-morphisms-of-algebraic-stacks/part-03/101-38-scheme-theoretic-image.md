---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsSchemeTheoreticImage, AlgebraicGeometry.Stack.hasSchemeTheoreticImage_comp_iff, AlgebraicGeometry.Stack.eq_of_isSchemeTheoreticImage_comp, AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_le, AlgebraicGeometry.Stack.factorsThroughSubstack_schemeTheoreticImageCandidate, AlgebraicGeometry.Stack.hasSchemeTheoreticImage, AlgebraicGeometry.Stack.le_inverseImage_of_isSchemeTheoreticImage, AlgebraicGeometry.Stack.schemeTheoreticImageMap
statement: formalized
proof: formalized
---

# 101.38 Scheme theoretic image

Section 101.38 of the Stacks Project, [Tag 0CMH](https://stacks.math.columbia.edu/tag/0CMH). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CMI, a definition

[Tag 0CMI](https://stacks.math.columbia.edu/tag/0CMI) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsSchemeTheoreticImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L155). References: EGA I (9.5.3).

> **Stacks 0CMI.** A property of the objects of `𝒴` is *the scheme theoretic image* of a
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` when it cuts out a closed substack of `𝒴`
> through which `f` factors, and is contained in every closed substack of `𝒴` through which `f`
> factors.

```lean
def IsSchemeTheoreticImage {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (P : ObjectProperty 𝒴.val.val.obj) : Prop
```

## Tag 0CMJ, a lemma

[Tag 0CMJ](https://stacks.math.columbia.edu/tag/0CMJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasSchemeTheoreticImage_comp_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L250). The attribute's comment: “existence\_iff”.

> **Stacks 0CMJ**, the existence assertion. Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic
> stacks over `S` and let `g : 𝒲 ⟶ 𝒳` be a surjective, flat 1-morphism locally of finite
> presentation. Then the scheme theoretic image of `f` exists if and only if the scheme theoretic
> image of `g ≫ f` exists.

```lean
theorem hasSchemeTheoreticImage_comp_iff {𝒲 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒲 ⟶ 𝒳)
    (hsurj : IsSurjective B S hS g)
    (hflat : AlgebraicStacks.IsFlat B S hS g)
    (hlfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g) :
    HasSchemeTheoreticImage f ↔ HasSchemeTheoreticImage (g ≫ f)
```

**`AlgebraicGeometry.Stack.eq_of_isSchemeTheoreticImage_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L264). The attribute's comment: “images\_equal”.

> **Stacks 0CMJ**, the agreement of the two images. Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of
> algebraic stacks over `S` and let `g : 𝒲 ⟶ 𝒳` be a surjective, flat 1-morphism locally of finite
> presentation. If `P` is the scheme theoretic image of `f` and `Q` is the scheme theoretic image of
> `g ≫ f`, then `P = Q`.

```lean
theorem eq_of_isSchemeTheoreticImage_comp {𝒲 𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒲 ⟶ 𝒳)
    (hsurj : IsSurjective B S hS g)
    (hflat : AlgebraicStacks.IsFlat B S hS g)
    (hlfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    {P Q : ObjectProperty 𝒴.val.val.obj} (hP : IsSchemeTheoreticImage f P)
    (hQ : IsSchemeTheoreticImage (g ≫ f) Q) : P = Q
```

## Tag 0CPU, a lemma

[Tag 0CPU](https://stacks.math.columbia.edu/tag/0CPU) in the Stacks Project.

**`AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean#L94). The attribute's comment: “minimality of the candidate image”.

> Minimality of the candidate image: the intersection of the closed substacks through which `f`
> factors is contained in each of them.

```lean
theorem schemeTheoreticImageCandidate_le {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    {Q : ObjectProperty 𝒴.val.val.obj} (hQ : IsClosedSubstack 𝒴 Q)
    (hfac : FactorsThroughSubstack f Q) : schemeTheoreticImageCandidate f ≤ Q
```

**`AlgebraicGeometry.Stack.factorsThroughSubstack_schemeTheoreticImageCandidate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean#L144). The attribute's comment: “the candidate image factors f”.

> The factorization through the candidate image: `f` factors through the intersection of the
> closed substacks of `𝒴` through which it factors, because factoring through a strictly full
> subcategory is a condition on the objects in the image of `f`.

```lean
theorem factorsThroughSubstack_schemeTheoreticImageCandidate
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    FactorsThroughSubstack f (schemeTheoreticImageCandidate f)
```

**`AlgebraicGeometry.Stack.hasSchemeTheoreticImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageExistence.lean#L201).

> **Stacks 0CPU.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. Then the
> scheme theoretic image of `f` exists: there is a smallest closed substack of `𝒴` through which
> `f` factors, namely `AlgebraicGeometry.Stack.schemeTheoreticImageCandidate f`.

```lean
theorem hasSchemeTheoreticImage {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    HasSchemeTheoreticImage f
```

## Tag 0CPV, a lemma

[Tag 0CPV](https://stacks.math.columbia.edu/tag/0CPV) in the Stacks Project.

**`AlgebraicGeometry.Stack.le_inverseImage_of_isSchemeTheoreticImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L570). The attribute's comment: “containment”.

> **Stacks 0CPV**, the containment that induces the morphism. Let a commutative square of
> algebraic stacks over `S` be given, with horizontal 1-morphisms `f₁ : 𝒳₁ ⟶ 𝒴₁`, `f₂ : 𝒳₂ ⟶ 𝒴₂`
> and vertical ones `a : 𝒳₁ ⟶ 𝒳₂`, `b : 𝒴₁ ⟶ 𝒴₂`, and let `Pᵢ` be the scheme theoretic image of
> `fᵢ`. Then `P₁` is contained in the preimage of `P₂` under `b`.
>
> The preimage of `P₂` cuts out a closed substack of `𝒴₁`
> (`AlgebraicGeometry.Stack.isClosedSubstack_inverseImage`) through which `f₁` factors
> (`AlgebraicGeometry.Stack.factorsThroughSubstack_inverseImage`), so the minimality of the scheme
> theoretic image applies to it.

```lean
theorem le_inverseImage_of_isSchemeTheoreticImage {f₁ : 𝒳₁ ⟶ 𝒴₁} {f₂ : 𝒳₂ ⟶ 𝒴₂} {a : 𝒳₁ ⟶ 𝒳₂}
    {b : 𝒴₁ ⟶ 𝒴₂} (sq : f₁ ≫ b ≅ a ≫ f₂) {P₁ : ObjectProperty 𝒴₁.val.val.obj}
    {P₂ : ObjectProperty 𝒴₂.val.val.obj} (h₁ : IsSchemeTheoreticImage f₁ P₁)
    (h₂ : IsSchemeTheoreticImage f₂ P₂) :
    P₁ ≤ P₂.inverseImage b.hom.hom.toFunctor
```

**`AlgebraicGeometry.Stack.schemeTheoreticImageMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 583](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L583). The attribute's comment: “induced\_morphism”.

> **Stacks 0CPV**, the induced 1-morphism. The 1-morphism `b : 𝒴₁ ⟶ 𝒴₂` of a commutative
> square of algebraic stacks carries the scheme theoretic image of `f₁` into the scheme theoretic
> image of `f₂`, and therefore induces a 1-morphism `𝒵₁ ⟶ 𝒵₂` between them.

```lean
def schemeTheoreticImageMap {f₁ : 𝒳₁ ⟶ 𝒴₁} {f₂ : 𝒳₂ ⟶ 𝒴₂} {a : 𝒳₁ ⟶ 𝒳₂} {b : 𝒴₁ ⟶ 𝒴₂}
    (sq : f₁ ≫ b ≅ a ≫ f₂) {P₁ : ObjectProperty 𝒴₁.val.val.obj}
    {P₂ : ObjectProperty 𝒴₂.val.val.obj} (h₁ : IsSchemeTheoreticImage f₁ P₁)
    (h₂ : IsSchemeTheoreticImage f₂ P₂) :
    fullSubcategoryAlgebraicStack 𝒴₁ P₁ h₁.isAlgebraicStack ⟶
      fullSubcategoryAlgebraicStack 𝒴₂ P₂ h₂.isAlgebraicStack
```

**`AlgebraicGeometry.Stack.schemeTheoreticImageMap_comp_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L595). The attribute's comment: “inclusion\_square”.

> **Stacks 0CPV**, the right-hand square of the induced diagram: the induced 1-morphism
> `𝒵₁ ⟶ 𝒵₂` composed with the inclusion `𝒵₂ ⟶ 𝒴₂` is the inclusion `𝒵₁ ⟶ 𝒴₁` followed by `b`.

```lean
theorem schemeTheoreticImageMap_comp_inclusion {f₁ : 𝒳₁ ⟶ 𝒴₁} {f₂ : 𝒳₂ ⟶ 𝒴₂} {a : 𝒳₁ ⟶ 𝒳₂}
    {b : 𝒴₁ ⟶ 𝒴₂} (sq : f₁ ≫ b ≅ a ≫ f₂) {P₁ : ObjectProperty 𝒴₁.val.val.obj}
    {P₂ : ObjectProperty 𝒴₂.val.val.obj} (h₁ : IsSchemeTheoreticImage f₁ P₁)
    (h₂ : IsSchemeTheoreticImage f₂ P₂) :
    schemeTheoreticImageMap sq h₁ h₂ ≫ fullSubcategoryInclusion 𝒴₂ P₂ h₂.isAlgebraicStack =
      fullSubcategoryInclusion 𝒴₁ P₁ h₁.isAlgebraicStack ≫ b
```

**`AlgebraicGeometry.Stack.schemeTheoreticImageMapFactorizationSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean, line 611](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImage.lean#L611). The attribute's comment: “factorization\_square”.

> **Stacks 0CPV**, the left-hand square of the induced diagram. Let `kᵢ : 𝒳ᵢ ⟶ 𝒵ᵢ` be
> factorizations of `fᵢ` through the scheme theoretic images. Then the induced 1-morphism
> `𝒵₁ ⟶ 𝒵₂` makes the square with `a : 𝒳₁ ⟶ 𝒳₂` 2-commute.
>
> Both composites `𝒳₁ ⟶ 𝒵₂ ⟶ 𝒴₂` are 2-isomorphic, by the given square and the two
> factorizations, and the inclusion of `𝒵₂` is fully faithful, so the 2-isomorphism descends to
> `𝒵₂`.

```lean
noncomputable def schemeTheoreticImageMapFactorizationSquare {f₁ : 𝒳₁ ⟶ 𝒴₁} {f₂ : 𝒳₂ ⟶ 𝒴₂}
    {a : 𝒳₁ ⟶ 𝒳₂} {b : 𝒴₁ ⟶ 𝒴₂} (sq : f₁ ≫ b ≅ a ≫ f₂)
    {P₁ : ObjectProperty 𝒴₁.val.val.obj} {P₂ : ObjectProperty 𝒴₂.val.val.obj}
    (h₁ : IsSchemeTheoreticImage f₁ P₁) (h₂ : IsSchemeTheoreticImage f₂ P₂)
    (k₁ : 𝒳₁ ⟶ fullSubcategoryAlgebraicStack 𝒴₁ P₁ h₁.isAlgebraicStack)
    (k₂ : 𝒳₂ ⟶ fullSubcategoryAlgebraicStack 𝒴₂ P₂ h₂.isAlgebraicStack)
    (e₁ : k₁ ≫ fullSubcategoryInclusion 𝒴₁ P₁ h₁.isAlgebraicStack ≅ f₁)
    (e₂ : k₂ ≫ fullSubcategoryInclusion 𝒴₂ P₂ h₂.isAlgebraicStack ≅ f₂) :
    k₁ ≫ schemeTheoreticImageMap sq h₁ h₂ ≅ a ≫ k₂
```

## Tag 0CMK, a lemma

[Tag 0CMK](https://stacks.math.columbia.edu/tag/0CMK) in the Stacks Project.

**`AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_le_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean#L150). The attribute's comment: “containment”.

> **The easy containment of Stacks 0CMK, for any 2-commutative square.** Let `f : 𝒳 ⟶ 𝒴` and
> `b : 𝒴' ⟶ 𝒴` be 1-morphisms of algebraic stacks over `S` and let `sq` be a 2-commutative square
> over them, with
> apex `sq.pt` and legs `sq.fst : sq.pt ⟶ 𝒴'` and `sq.snd : sq.pt ⟶ 𝒳`. Then the intersection of
> the closed substacks of `𝒴'` through which `sq.fst` factors is contained in the preimage under
> `b` of the intersection of the closed substacks of `𝒴` through which `f` factors.
>
> Let `Q` be a closed substack of `𝒴` through which `f` factors. Its preimage under `b` is a closed
> substack of `𝒴'` (`AlgebraicGeometry.Stack.isClosedSubstack_inverseImage`) through which `sq.fst`
> factors (`AlgebraicGeometry.Stack.factorsThroughSubstack_inverseImage`, which is where the
> 2-commutativity of the square is used), so the candidate image of `sq.fst` is contained in it by
> its own minimality. As `Q` ranges over the closed substacks of `𝒴` through which `f` factors this
> says exactly that an object of the candidate image of `sq.fst` has its image under `b` in the
> candidate image of `f`.

```lean
public theorem schemeTheoreticImageCandidate_le_inverseImage (f : 𝒳 ⟶ 𝒴) (b : 𝒴' ⟶ 𝒴)
    (sq : Bicategory.TwoCommSq b f) :
    schemeTheoreticImageCandidate sq.fst ≤
      (schemeTheoreticImageCandidate f).inverseImage b.hom.hom.toFunctor
```

**`AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_inverseImage_fullSubcategoryInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean#L174). The attribute's comment: “closed\_substack\_case”.

> **Stacks 0CMK for the inclusion of a closed substack.** Let `P` cut out a closed substack of
> `𝒴₂` and let `b : 𝒴₁ ⟶ 𝒴₂` be any 1-morphism of algebraic stacks over `S`. The base change of the
> inclusion of that substack along `b` is the inclusion of the preimage of `P`, by
> `AlgebraicGeometry.Stack.inverseImageSquare_fst`, and the square realising it is a 2-fibre product
> by `AlgebraicGeometry.Stack.isTwoFibreProduct_inverseImageSquare`. Then the scheme theoretic image
> of that base change is the preimage under `b` of the scheme theoretic image of the inclusion.
>
> Both sides are computed by
> `AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_fullSubcategoryInclusion`: a closed
> substack is the scheme theoretic image of its own inclusion, and the preimage of a closed substack
> is a closed substack. Neither flatness of `b` nor quasi-compactness of the inclusion is used.

```lean
public theorem schemeTheoreticImageCandidate_inverseImage_fullSubcategoryInclusion
    {𝒴₁ 𝒴₂ : AlgebraicStacks.{u, w} B S hS} (b : 𝒴₁ ⟶ 𝒴₂)
    {P : ObjectProperty 𝒴₂.val.val.obj} [P.IsClosedUnderIsomorphisms]
    (hP : IsClosedSubstack 𝒴₂ P)
    (hPalg : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒴₂ P)) :
    schemeTheoreticImageCandidate (inverseImageSquare b P hPalg).fst =
      (schemeTheoreticImageCandidate (fullSubcategoryInclusion 𝒴₂ P hPalg)).inverseImage
        b.hom.hom.toFunctor
```

**`AlgebraicGeometry.Stack.isSchemeTheoreticImage_inverseImage_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean, line 777](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImageFlatBaseChange.lean#L777). References: EGA IV (2.3.2), “more general”.

> **Stacks 0CMK.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact 1-morphism of algebraic stacks over `S`
> and let `b : 𝒴' ⟶ 𝒴` be a flat 1-morphism. Then formation of the scheme theoretic image commutes
> with the base change along `b`: if `P` is the scheme theoretic image of `f`, then its inverse
> image under `b` is the scheme theoretic image of the base change
> `f' : 𝒳 ×_𝒴 𝒴' ⟶ 𝒴'` (the first projection of the canonical 2-fibre product square).
>
> The containment of the image of `f'` in the inverse image of `P` holds for any square
> (`AlgebraicGeometry.Stack.schemeTheoreticImageCandidate_le_inverseImage`). For the converse, the
> flat-local image of `f` — the closed substack of `𝒴` cut out by the scheme theoretic images of
> the base changes of `f` to the smooth affine charts of `𝒴`, which descend by the invariance of
> the proof of Stacks 0CMK
> (`AlgebraicGeometry.Stack.chartImageSubfunctor_le_chartSubfunctor_flatLocalImage`) — is a closed
> substack through which `f` factors, so it contains `P`, and its inverse image under `b` lies in
> the image of `f'` (`AlgebraicGeometry.Stack.inverseImage_flatLocalImage_le`).

```lean
theorem isSchemeTheoreticImage_inverseImage_of_isFlat (f : 𝒳 ⟶ 𝒴) (b : 𝒴' ⟶ 𝒴)
    (hf : IsQuasiCompactMorphism B S hS f) (hb : AlgebraicStacks.IsFlat B S hS b)
    {P : ObjectProperty 𝒴.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    IsSchemeTheoreticImage (twoFibreProductSquareAlgebraicStacks B S hS b f).fst
      (P.inverseImage b.hom.hom.toFunctor)
```

## Tag 0CML, a lemma

[Tag 0CML](https://stacks.math.columbia.edu/tag/0CML) in the Stacks Project.

**`AlgebraicGeometry.Stack.range_pointsMap_eq_closure_of_isSchemeTheoreticImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImagePointsClosure.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImagePointsClosure.lean#L129).

> **Stacks 0CML.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact 1-morphism of algebraic stacks over `S`
> and let `P` cut out its scheme theoretic image `𝒵 ⊆ 𝒴` (Stacks 0CMI). Then the points of `𝒵` are
> the closure in `|𝒴|` of the image of `|f|`.
>
> The closure lies in `|𝒵|` for any `f`: `f` factors through `𝒵`, whose points are closed by
> **Stacks 0H20**. Conversely, let `z` be a point of `𝒵`, and choose a smooth chart
> `v : (Sch/V)_fppf ⟶ 𝒴` with `V` affine through its image, and a point `η` of `V` over it. The
> point `(z, η)` lifts to `𝒵 ×_𝒴 V` (**Stacks 04XH**), so `η` comes from a field-valued point
> `t : Spec K ⟶ V` at which `P` holds. As `f` is quasi-compact, `𝒳 ×_𝒴 V` is quasi-compact and has
> a smooth surjective presentation by an affine `A`, with composite `g : A ⟶ V`. The scheme
> theoretic image of `f` lies in the closed substack cut out by the scheme theoretic images of the
> base changes of `f` to the smooth affine charts (the descent of the proof of **Stacks 0CMK**), and
> that image along `v` lies in the scheme theoretic image of `g` (**Stacks 0CMJ**, in the form of
> Stacks 06QA). So `t` factors through the scheme theoretic image of the quasi-compact `g`, and `η`
> lies in the closure of the image of `g` (**Stacks 082Z**, read on schemes). The map
> `|V| ⟶ |𝒴|` is continuous and carries the image of `g` into the image of `|f|`, the square
> `A ⟶ 𝒳 ×_𝒴 V` commuting, so it carries `η` into the closure of the image of `|f|`.

```lean
theorem range_pointsMap_eq_closure_of_isSchemeTheoreticImage
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsQuasiCompactMorphism B S hS f)
    {P : ObjectProperty 𝒴.val.val.obj} (hP : IsSchemeTheoreticImage f P) :
    Set.range (AlgebraicStacks.pointsMap B S hS
        (fullSubcategoryInclusion 𝒴 P hP.isAlgebraicStack)) =
      @closure _ (pointTopology B S hS 𝒴.val)
        (Set.range (AlgebraicStacks.pointsMap B S hS f))
```

## Tag 0CPW, a lemma

[Tag 0CPW](https://stacks.math.columbia.edu/tag/0CPW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_fst_of_isSchemeTheoreticImage_partialSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImagePartialSection.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeTheoreticImagePartialSection.lean#L369).

> **Stacks 0CPW.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is
> representable by algebraic spaces and separated, let `𝒱 ⊆ 𝒴` be an open substack such that
> `𝒱 ⟶ 𝒴` is quasi-compact, and let `s : 𝒱 ⟶ 𝒳` be a 1-morphism with `f ∘ s ≅ id_𝒱`, i.e. with a
> 2-isomorphism `s ≫ f ≅ (𝒱 ⟶ 𝒴)`. Let `P` cut out the scheme theoretic image `𝒴'` of `s`
> (Stacks 0CMI). Then `𝒴' ⟶ 𝒴` is an isomorphism over `𝒱`: the projection `𝒴' ×_𝒴 𝒱 ⟶ 𝒱` is an
> equivalence of categories.
>
> `s` is quasi-compact by **Stacks 050Y**, as `s ≫ f` is 2-isomorphic to the quasi-compact
> `𝒱 ⟶ 𝒴` and `f` is quasi-separated. The projection has a section, so it is essentially surjective
> (`AlgebraicGeometry.Stack.essSurj_fst_partialSectionImageSquare`). It is faithful because `f` is,
> being representable by algebraic spaces. It is full because every object of `𝒴' ×_𝒴 𝒱`, read in
> `𝒱 ×_𝒴 𝒳`, is isomorphic to the image of an object of `𝒱` under the graph of `s`
> (`AlgebraicGeometry.Stack.exists_iso_partialSectionGraph_obj`, which is where **Stacks 0CMK** and
> the separatedness of `f` enter), and the graph is a section of the projection to `𝒱`.

```lean
theorem isEquivalence_fst_of_isSchemeTheoreticImage_partialSection
    (hrep : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hf : AlgebraicStacks.IsSeparated B S hS f)
    (hVqc : IsQuasiCompactMorphism B S hS ι[V]) (hsec : s ≫ f ≅ ι[V])
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsSchemeTheoreticImage s P) :
    Functor.IsEquivalence (twoFibreProductSquareAlgebraicStacks B S hS ι[V]
      (fullSubcategoryInclusion 𝒳 P hP.isAlgebraicStack ≫ f)).fst.hom.hom.toFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.38, Tag 0CMH](https://stacks.math.columbia.edu/tag/0CMH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
