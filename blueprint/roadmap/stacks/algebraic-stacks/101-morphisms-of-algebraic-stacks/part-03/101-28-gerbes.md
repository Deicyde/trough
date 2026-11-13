---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsGerbeOver, AlgebraicGeometry.Stack.AlgebraicStacks.IsGerbe, AlgebraicGeometry.Stack.AlgebraicStacks.exists_algebraicSpace_isGerbeOver_isoClasses, AlgebraicGeometry.Stack.AlgebraicStacks.exists_isGerbeOver_isoClassSpace, AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_isTwoFibreProduct, CategoryTheory.IsGerbeOver.comp, AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_snd_of_isSurjective_isFlat_isLfp, AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_section_of_isGerbeOver
statement: formalized
proof: formalized
---

# 101.28 Gerbes

Section 101.28 of the Stacks Project, [Tag 06QB](https://stacks.math.columbia.edu/tag/06QB). 15 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06QC, a definition

[Tag 06QC](https://stacks.math.columbia.edu/tag/06QC) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsGerbeOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Gerbe.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Gerbe.lean#L64). The attribute's comment: “gerbe over an algebraic stack”.

> **Stacks 06QC.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` makes `𝒳` a *gerbe
> over* `𝒴` when its underlying functor makes `𝒳` a gerbe over `𝒴` in the sense of Stacks 06P2,
> for the fppf topology on the big fppf site of `S`.

```lean
abbrev IsGerbeOver {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsGerbe`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Gerbe.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Gerbe.lean#L72). The attribute's comment: “gerbe”.

> **Stacks 06QC.** An algebraic stack `𝒳` over `S` *is a gerbe* when there is an algebraic
> stack `𝒴` representable by an algebraic space over `S` and a 1-morphism `𝒳 ⟶ 𝒴` making `𝒳` a
> gerbe over `𝒴`.

```lean
abbrev IsGerbe (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 06QD, a lemma

[Tag 06QD](https://stacks.math.columbia.edu/tag/06QD) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_algebraicSpace_isGerbeOver_isoClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeIsoClasses.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeIsoClasses.lean#L107).

> **Stacks 06QD.** If an algebraic stack `𝒳` over `S` is a gerbe, then the fppf sheafification
> of the presheaf `U ↦ Ob(𝒳_U)/≅` is (the universe lift of) an algebraic space `F`, and `𝒳` is a
> gerbe over the algebraic stack `𝒴` representable by `F` by a 1-morphism inducing the unit of the
> sheafification on isomorphism classes.

```lean
theorem exists_algebraicSpace_isGerbeOver_isoClasses (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsGerbe B S hS 𝒳) :
    letI : 𝒳.val.val.p.IsFibered := (CatFiberedInGroupoids.isFiberedInGroupoids 𝒳.val).isFibered
    ∃ F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS F ∧
      ∃ (e : F ⋙ uliftFunctor.{u + 1} ≅ sheafifiedIsoClasses B S hS 𝒳)
        (𝒴 : Stack.AlgebraicStacks.{u, w} B S hS) (g : 𝒳 ⟶ 𝒴), IsGerbeOver B S hS g ∧
          letI : 𝒴.val.val.p.IsFibered :=
            (CatFiberedInGroupoids.isFiberedInGroupoids 𝒴.val).isFibered
          ∃ eY : 𝒴.val.val.p.isoClassPresheaf ≅ F ⋙ uliftFunctor.{u + 1},
            Functor.isoClassMap (Functor.isFibredOneMorphism_of_isFiberedInGroupoids
              (CatFiberedInGroupoids.isFiberedInGroupoids 𝒴.val)
              (CatFiberedInGroupoids.homFunctor_comp_p g.hom)) ≫ eY.hom ≫ e.hom =
              (BigFppfOver.topology B S hS).toSheafify (isoClassPresheaf B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_isGerbeOver_isoClassSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeOverIsoClassSpace.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeOverIsoClassSpace.lean#L70).

> **Stacks 06QD.** If an algebraic stack `𝒳` over `S` is a gerbe, then the fppf sheafification
> of the presheaf `U ↦ Ob(𝒳_U)/≅` is (the universe lift of) an algebraic space `F`, and `𝒳` is a
> gerbe over `F`: there are an algebraic stack `𝒴` represented by `F` through an equivalence `E`
> over the site (Stacks 04SV) and a 1-morphism `g : 𝒳 ⟶ 𝒴` making `𝒳` a gerbe over `𝒴`, such that
> the sheafification unit sends the class of `x` to the section of `F` named by the class of
> `g(x)`.

```lean
theorem exists_isGerbeOver_isoClassSpace
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsGerbe B S hS 𝒳) :
    letI : 𝒳.val.val.p.IsFibered := (CatFiberedInGroupoids.isFiberedInGroupoids 𝒳.val).isFibered
    ∃ F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS F ∧
      ∃ (e : F ⋙ uliftFunctor.{u + 1} ≅ sheafifiedIsoClasses B S hS 𝒳)
        (𝒴 : Stack.AlgebraicStacks.{u, w} B S hS)
        (E : StacksRepresentableCFG.EquivalenceOver
          𝒴.val.val.p (presheafOfCategories (F ⋙ typeToCat)).p)
        (g : 𝒳 ⟶ 𝒴), IsGerbeOver B S hS g ∧
          letI : 𝒴.val.val.p.IsFibered :=
            (CatFiberedInGroupoids.isFiberedInGroupoids 𝒴.val).isFibered
          ∀ (U : (BigFppfOver B S hS)ᵒᵖ) (c : (isoClassPresheaf B S hS 𝒳).obj U),
            e.inv.app U (((BigFppfOver.topology B S hS).toSheafify
              (isoClassPresheaf B S hS 𝒳)).app U c) =
              ULift.up (PresheafOfCategories.elementsIsoClassEquiv F E U.unop
                ((Functor.isoClassMap (Functor.isFibredOneMorphism_of_isFiberedInGroupoids
                  (CatFiberedInGroupoids.isFiberedInGroupoids 𝒴.val)
                  (CatFiberedInGroupoids.homFunctor_comp_p g.hom))).app U c))
```

## Tag 06QE, a lemma

[Tag 06QE](https://stacks.math.columbia.edu/tag/06QE) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeBaseChange.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeBaseChange.lean#L119).

> **Stacks 06QE.** In a 2-fibre-product square of algebraic stacks over `S` with cospan
> `(f : 𝒳 ⟶ 𝒴, g : 𝒴' ⟶ 𝒴)`, if `f` makes `𝒳` a gerbe over `𝒴` then the projection to `𝒴'` makes
> the apex a gerbe over `𝒴'`.

```lean
theorem isGerbeOver_of_isTwoFibreProduct {𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴} (P : Bicategory.TwoCommSq f g)
    (hP : Bicategory.IsTwoFibreProduct P) (hf : IsGerbeOver B S hS f) :
    IsGerbeOver B S hS P.snd
```

## Tag 06R8, a lemma

[Tag 06R8](https://stacks.math.columbia.edu/tag/06R8) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsGerbeOver.comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Basic.lean#L175), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Gerbe/Basic.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Basic.lean#L230) (StacksFrontier).

## Tag 06QF, a lemma

[Tag 06QF](https://stacks.math.columbia.edu/tag/06QF) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_snd_of_isSurjective_isFlat_isLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeFppfDescent.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeFppfDescent.lean#L159).

> **Stacks 06QF.** Let
>
> ```text
> 𝒳' ⟶ 𝒳
> ↓     ↓
> 𝒴' ⟶ 𝒴
> ```
>
> be a 2-fibre-product square of algebraic stacks over `S`, given as a 2-commutative square `P`
> over the cospan `(f : 𝒳 ⟶ 𝒴, g : 𝒴' ⟶ 𝒴)` with the 2-categorical universal property, so that
> `P.pt` is `𝒳'` and `P.snd` is the base change of `f`. If `g` is surjective, flat and locally of
> finite presentation and `P.snd` makes `𝒳'` a gerbe over `𝒴'`, then `f` makes `𝒳` a gerbe over
> `𝒴`.
>
> This is the descent direction; the base-change direction is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_isTwoFibreProduct`, Stacks 06QE.

```lean
theorem isGerbeOver_of_snd_of_isSurjective_isFlat_isLfp {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴}
    (P : Bicategory.TwoCommSq f g) (hP : Bicategory.IsTwoFibreProduct P)
    (hgsurj : Stack.IsSurjective B S hS g) (hgflat : IsFlat B S hS g)
    (hglfp : IsLocallyOfFinitePresentation B S hS g)
    (hgerbe : IsGerbeOver B S hS P.snd) :
    IsGerbeOver B S hS f
```

## Tag 06QG, a lemma

[Tag 06QG](https://stacks.math.columbia.edu/tag/06QG) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_section_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatLocalSection.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatLocalSection.lean#L191). The attribute's comment: “part (3): flatness and local finite presentation of the section”.

> **A section of a gerbe over an algebraic space is flat and locally of finite presentation.**
> Let `π : 𝒳 ⟶ 𝒰` make `𝒳` a gerbe over an algebraic stack `𝒰` which is representable by an
> algebraic space, and let `x : 𝒰 ⟶ 𝒳` be a section of `π`. Then `x` is flat and locally of finite
> presentation.
>
> Together with `AlgebraicGeometry.Stack.isSurjective_of_section_of_isGerbeOver` this is **Stacks
> 06QG** part (3), at the source's generality; the three parts of the tag are assembled in
> `StacksFrontier.AlgebraicGeometry.Stacks.GerbeSectionClassifyingStack`.
>
> `AlgebraicGeometry.Stack.exists_single_cover_section_factorisation_of_isGerbeOver` produces a
> surjective, flat, locally finitely presented `q : 𝒱 ⟶ 𝒳` out of the algebraic stack of an object
> of the site together with a `γ : 𝒱 ⟶ 𝒰` with `γ ≫ x = q` on the nose, and
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_of_factorisation`
> turns such a factorisation into the conclusion by the **Stacks 06NR** step and the descent along
> `q`. The three representability data that step needs are the two instances of
> `isRepresentableByAlgebraicSpace_pt` at the cospans `(q, q)` and `(q, x)` and **Stacks 04SV** for
> the slice of the site over `V`; the leg `q` is representable by algebraic spaces by condition (3)
> of **Stacks 045G**, its source being the algebraic stack of an object of the site, and the leg `x`
> by **Stacks 045G** condition (2) through
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_isAlgebraicStack`, its source being
> representable by an algebraic space.

```lean
theorem isFlat_and_isLocallyOfFinitePresentation_section_of_isGerbeOver
    {𝒰 𝒳 : Stack.AlgebraicStacks.{u, w} B S hS}
    (π : 𝒳 ⟶ 𝒰) (x : 𝒰 ⟶ 𝒳) (hx : x ≫ π ≅ 𝟙 𝒰)
    (hπ : IsGerbeOver B S hS π)
    (h𝒰 : Stack.IsRepresentableByAlgebraicSpace B S hS 𝒰.val) :
    IsFlat B S hS x ∧ IsLocallyOfFinitePresentation B S hS x
```

**`AlgebraicGeometry.Stack.isSurjective_of_section_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeIsomGroupSection.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeIsomGroupSection.lean#L67). The attribute's comment: “part (3): surjectivity of the section”.

> Let `π : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` making `𝒳` a gerbe over `𝒴`,
> and let `x : 𝒴 ⟶ 𝒳` be a section of `π`, i.e. a 1-morphism with a 2-isomorphism
> `x ≫ π ≅ 𝟙 𝒴`. Then `x` is surjective.

```lean
theorem isSurjective_of_section_of_isGerbeOver
    (π : 𝒳 ⟶ 𝒴) (x : 𝒴 ⟶ 𝒳) (hx : x ≫ π ≅ 𝟙 𝒴)
    (hπ : AlgebraicStacks.IsGerbeOver B S hS π) :
    IsSurjective B S hS x
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_equivalenceOver_gerbeSectionClassifyingFunctor_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionCanonicalEquivalence.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionCanonicalEquivalence.lean#L194).

> **Stacks 06QG.** Let `π : 𝒳 ⟶ 𝒰` be a 1-morphism from an algebraic stack `𝒳` over `S` to the
> algebraic stack `𝒰` of an algebraic space `Z` over `S`, let `x : 𝒰 ⟶ 𝒳` be a section of `π` — a
> 1-morphism together with a 2-isomorphism `x ≫ π ≅ 𝟙 𝒰` — and let `π` make `𝒳` a gerbe over `𝒰`.
> Let `G = Isom_𝒳(x, x)` be the group algebraic space over `Z` of **Stacks 06PP**, whose group law
> is composition of automorphisms (`AlgebraicGeometry.Stack.relativeAutomorphismGroupAlgebraicSpace`
> at `π`; since `𝒰` is an algebraic space, its sections are all the automorphisms of `x`, by
> `AlgebraicGeometry.Stack.isIso_relativeAutomorphismToIsomSpace`). Then
>
> 1. the canonical 1-morphism `x_can : [Z/G] ⟶ 𝒳`
>    (`AlgebraicGeometry.Stack.AlgebraicStacks.gerbeSectionClassifyingFunctor`) out of the
>    quotient stack of the *trivial* action of `G` on `Z` is an equivalence of stacks in groupoids
>    over the big fppf site of `S`;
> 2. `G ⟶ Z` is flat and locally of finite presentation;
> 3. `x` is surjective, flat and locally of finite presentation.

```lean
theorem exists_equivalenceOver_gerbeSectionClassifyingFunctor_of_isGerbeOver
    (π : 𝒳 ⟶ Stack.algebraicSpaceStack.{u, w} B S hS Z hZ)
    (x : Stack.algebraicSpaceStack.{u, w} B S hS Z hZ ⟶ 𝒳)
    (hx : x ≫ π ≅ 𝟙 (Stack.algebraicSpaceStack.{u, w} B S hS Z hZ))
    (hπ : IsGerbeOver B S hS π) :
    letI : ModObj (Stack.relativeAutomorphismGroupAlgebraicSpace B S hS Z hZ π x).obj.X
      (𝟙_ (Over Z)) := ModObj.trivialAction _ _
    (∃ e : StacksRepresentableCFG.EquivalenceOver
        (Stack.quotientStackOfAction (⟨Z, hZ⟩ : AlgebraicSpaces B S hS)
          (Stack.relativeAutomorphismGroupAlgebraicSpace B S hS Z hZ π x).obj.X (𝟙_ _)
          (Stack.relativeAutomorphismGroupAlgebraicSpace B S hS Z hZ π x).property hZ).p
        𝒳.val.val.p,
        e.hom.functor = gerbeSectionClassifyingFunctor B S hS π x hx) ∧
      Space.IsFlat B S hS
        (Stack.relativeAutomorphismGroupAlgebraicSpace B S hS Z hZ π x).obj.X.hom ∧
      Space.IsLocallyOfFinitePresentation B S hS
        (Stack.relativeAutomorphismGroupAlgebraicSpace B S hS Z hZ π x).obj.X.hom ∧
      Stack.IsSurjective B S hS x ∧ IsFlat B S hS x ∧
        IsLocallyOfFinitePresentation B S hS x
```

**`AlgebraicGeometry.Stack.SelfIntersection.source_eq_target_selfIntersectionPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionQuotientPresentation.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionQuotientPresentation.lean#L286). The attribute's comment: “part (1): the self-intersection groupoid of a section of a gerbe has equal source and target, so the group algebraic space of part (1) acts trivially”.

> **Stacks 06QG, part (1): the action is trivial**, read on the presentation datum of
> Stacks 04T4 (4) and (5): the groupoid in algebraic spaces it builds from a section of a gerbe has
> one and the same source and target, so it is the groupoid of a group algebraic space acting
> trivially on the object space.

```lean
theorem source_eq_target_selfIntersectionPresentation
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) (π : 𝒳 ⟶ 𝒴) (hx : x ≫ π ≅ 𝟙 𝒴) :
    (selfIntersectionPresentation eU eR h𝒳).groupoid.source =
      (selfIntersectionPresentation eU eR h𝒳).groupoid.target
```

**`AlgebraicGeometry.Stack.SelfIntersection.nonempty_isEquivalenceOver_canonicalMap_of_section_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionQuotientPresentation.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeSectionQuotientPresentation.lean#L319). The attribute's comment: “part (1): the canonical 1-morphism out of the quotient stack of the self-intersection groupoid is an equivalence”.

> **Stacks 06QG, part (1): the canonical equivalence.** Let `𝒳` be an algebraic stack over `S`,
> let `π : 𝒳 ⟶ 𝒴` make `𝒳` a gerbe over `𝒴`, let `x : 𝒴 ⟶ 𝒳` be a section of `π`, let `𝒴` be
> represented by an algebraic space `U` and let the self-intersection `𝒴 ×_{x, 𝒳, x} 𝒴` be
> represented by an algebraic space `R` — which it is, by Stacks 04T4 (1). Then the canonical
> 1-morphism `x_can : [U/R] ⟶ 𝒳` of the presentation datum of Stacks 04T4 (4) and (5) is an
> equivalence over the big fppf site of `S`.
>
> Full faithfulness is Stacks 04T4 (6) and needs no hypothesis beyond the presentation data;
> essential surjectivity on each fibre is the local essential surjectivity of the section, glued by
> effective descent in the quotient stack against the `Mor`-sheaf condition on `𝒳`, and a
> 1-morphism of fibred categories which is fully faithful and essentially surjective on every fibre
> is an equivalence over the site.
>
> The source states the equivalence at the quotient stack of the trivial action of
> `G = Isom_𝒳(x, x)`. That is this equivalence: the self-intersection groupoid has equal source and
> target (`source_eq_target_selfIntersectionPresentation`), hence is the groupoid of the trivial
> action of its stabilizer group of **Stacks 0447** on the object space, and that stabilizer is
> `Isom_𝒳(x, x)` with its group law of Stacks 06PP
> (`AlgebraicGeometry.Stack.sectionAutomorphismStabilizerIso`). The passage is
> `exists_equivalenceOver_gerbeSectionClassifyingFunctor_of_isGerbeOver`, in the namespace
> `AlgebraicGeometry.Stack.AlgebraicStacks` of
> `StacksFrontier.AlgebraicGeometry.Stacks.GerbeSectionCanonicalEquivalence`, where the whole of
> Stacks 06QG is assembled.

```lean
theorem nonempty_isEquivalenceOver_canonicalMap_of_section_of_isGerbeOver
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) (π : 𝒳 ⟶ 𝒴) (hx : x ≫ π ≅ 𝟙 𝒴)
    (hπ : CategoryTheory.IsGerbeOver (BigFppfOver.topology B S hS) 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor π)) :
    Nonempty (Functor.IsEquivalenceOver
      (Stack.quotientStack (selfIntersectionPresentation eU eR h𝒳).groupoid).p
      𝒳.val.p
      (selfIntersectionPresentation eU eR h𝒳).canonicalMap.toFunctor)
```

## Tag 06QH, a lemma

[Tag 06QH](https://stacks.math.columbia.edu/tag/06QH) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_equivalenceOver_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeCharacterization.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeCharacterization.lean#L85). The attribute's comment: “(2) implies (1); the converse needs Stacks 06QG”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `U` be an algebraic space
> over `S`, let `G` be a group algebraic space flat and locally of finite presentation over `U`,
> and let `g : U ⟶ 𝒴` be surjective, flat and locally of finite presentation. If the base change
> of `f` along `g` is isomorphic, as an object over `U`, to the quotient stack `[U/G]` of the
> trivial action of `G` on `U`, then `f` makes `𝒳` a gerbe over `𝒴`.

```lean
theorem isGerbeOver_of_equivalenceOver_quotientStack
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (U : AlgebraicSpaces B S hS) (g : ofAlgebraicSpace.{u, w} B S hS U ⟶ 𝒴)
    (hgsurj : Stack.IsSurjective B S hS g) (hgflat : IsFlat B S hS g)
    (hglfp : IsLocallyOfFinitePresentation B S hS g)
    (G : Over U.obj) [GrpObj G] (hG : IsAlgebraicSpace B S hS G.left)
    (_hGflat : Space.IsFlat B S hS G.hom)
    (_hGlfp : Space.IsLocallyOfFinitePresentation B S hS G.hom)
    (A : Space.ActionGroupoidConstruction U G (𝟙_ (Over U.obj)) hG U.property)
    (P : Bicategory.TwoCommSq f g) (hP : Bicategory.IsTwoFibreProduct P)
    (e : StacksRepresentableCFG.EquivalenceOver
      (CatFiberedInGroupoids.homFunctor P.snd.hom)
      (quotientStackToBase A.groupoid).toFunctor) :
    IsGerbeOver B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_hasClassifyingFppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingCoverReduction.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingCoverReduction.lean#L157). The attribute's comment: “(2) implies (1), with clause (2) bundled”.

> **Stacks 06QH, the implication (2) ⟹ (1), packaged.** A 1-morphism of algebraic stacks over
> `S` which fppf-locally on its target is the classifying stack of a flat, locally finitely
> presented group algebraic space makes its source a gerbe over its target.
>
> This is `AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_of_equivalenceOver_quotientStack`
> with the data of clause (2) bundled into `HasClassifyingFppfCover`, which is the form a consumer
> that has clause (2) as a hypothesis — or has just produced it — can use.

```lean
theorem isGerbeOver_of_hasClassifyingFppfCover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h : HasClassifyingFppfCover.{u, w} B S hS f) :
    IsGerbeOver B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.hasClassifyingFppfCover_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingCoverReduction.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingCoverReduction.lean#L180). The attribute's comment: “(1) implies (2): the reduction along a surjective, flat, locally finitely presented base change”.

> **The reduction step of Stacks 06QH, (1) ⟹ (2): clause (2) descends along a surjective, flat,
> locally finitely presented base change.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks
> over `S` and let `h : 𝒴' ⟶ 𝒴` be surjective, flat and locally of finite presentation. If the base
> change of `f` along `h` satisfies clause (2) of Stacks 06QH, then so does `f`.
>
> This is the step by which the source's proof of (1) ⟹ (2) replaces `𝒴` first by a scheme
> smoothly covering it and then by the member of an fppf covering of that scheme: the covering
> 1-morphism `g : U ⟶ 𝒴'` produced for the base change is composed with `h`, which keeps it
> surjective (**Stacks 04ZT**), flat (**Stacks 06PX**) and locally of finite presentation
> (**Stacks 06Q3**), and the two 2-fibre-product squares are pasted (**Stacks 003Q**), the pasted
> rectangle having the *same* apex and second leg as the inner square — so the identification of
> that apex with `[U/G]` over `U` is carried over unchanged.

```lean
theorem hasClassifyingFppfCover_of_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (h : 𝒴' ⟶ 𝒴)
    (hhsurj : Stack.IsSurjective B S hS h) (hhflat : IsFlat B S hS h)
    (hhlfp : IsLocallyOfFinitePresentation B S hS h)
    (Q : Bicategory.TwoCommSq f h) (hQ : Bicategory.IsTwoFibreProduct Q)
    (hbc : HasClassifyingFppfCover.{u, w} B S hS Q.snd) :
    HasClassifyingFppfCover.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_iff_hasClassifyingFppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingFppfCover.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeClassifyingFppfCover.lean#L314).

> **Stacks 06QH.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
>
> 1. `f` makes `𝒳` a gerbe over `𝒴`;
> 2. there are an algebraic space `U` over `S`, a group algebraic space `G` over `U` which is flat
>    and locally of finite presentation over `U`, and a surjective, flat, locally finitely
>    presented 1-morphism `U ⟶ 𝒴` such that the base change `𝒳 ×_𝒴 U` is isomorphic over `U` to
>    the quotient stack `[U/G]` of the trivial action of `G` on `U`.
>
> Clause (2) is `AlgebraicGeometry.Stack.AlgebraicStacks.HasClassifyingFppfCover`.

```lean
theorem isGerbeOver_iff_hasClassifyingFppfCover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    IsGerbeOver B S hS f ↔ HasClassifyingFppfCover.{u, w} B S hS f
```

## Tag 06QI, a lemma

[Tag 06QI](https://stacks.math.columbia.edu/tag/06QI) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatness.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatness.lean#L381). The attribute's comment: “flat and locally of finite presentation”.

> **Stacks 06QI, flatness and local finite presentation.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S` which makes `𝒳` a gerbe over `𝒴` is flat and locally of finite
> presentation.
>
> Choose a surjective, flat, locally finitely presented `p : 𝒲 ⟶ 𝒳` from an algebraic space. The
> comparison `𝒲 ×_𝒳 𝒲 ⟶ 𝒲 ×_𝒴 𝒲` is a base change of the relative diagonal `Δ_f` by
> **Stacks 04Z1**, hence locally essentially surjective by Stacks 06P1 (2)(b); its composite with
> the first projection of `𝒲 ×_𝒴 𝒲` is the first projection of `𝒲 ×_𝒳 𝒲`, a base change of `p`. So
> Stacks 06NR for 1-morphisms of algebraic stacks makes the first projection
> `𝒲 ×_𝒴 𝒲 ⟶ 𝒲` flat and locally of finite presentation. That projection is the base change of
> `p ≫ f` along itself, and `p ≫ f` is locally essentially surjective by Stacks 06QA for `p` and
> Stacks 06P1 (2)(a); so **Stacks 045D** makes `p ≫ f` flat and locally of finite presentation,
> and **Stacks 06Q0** and **Stacks 06Q9** cancel `p`.

```lean
theorem isFlat_and_isLocallyOfFinitePresentation_of_isGerbeOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsGerbeOver B S hS f) :
    IsFlat B S hS f ∧ IsLocallyOfFinitePresentation B S hS f
```

**`AlgebraicGeometry.Stack.isSurjective_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeSurjective.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeSurjective.lean#L135). The attribute's comment: “surjective”.

> **Stacks 06QI**, surjectivity. A 1-morphism of algebraic stacks over `S` whose underlying
> functor exhibits its source as a gerbe over its target for the localized big fppf topology is
> surjective.
>
> Stacks 06P1 (2)(a) lifts an object of a fibre of the target along a covering sieve; the sieve
> contains an arrow from a field spectrum, so an object over a field lifts after a field
> extension, which is surjectivity on objects in the sense of Stacks 06D4; and Stacks 04XI
> identifies that with surjectivity of the map on points.

```lean
theorem isSurjective_of_isGerbeOver
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴)
    (hf : CategoryTheory.IsGerbeOver
      (BigFppfOver.topology B S hS)
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)) :
    IsSurjective B S hS f
```

## Tag 06QJ, a proposition

[Tag 06QJ](https://stacks.math.columbia.edu/tag/06QJ) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isGerbeOver_quotientStackToBase_overArrowStabilizerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientGerbe.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientGerbe.lean#L280). The attribute's comment: “the implication (2) implies (1): the quotient stack is a gerbe over U/(R/S)”.

> **Stacks 06QJ, the geometric half of the implication (2) `⟹` (1).** The structure arrow
> `[U/R] ⟶ X` of **Stacks 044R** of the groupoid read over `X = U/R'` makes the quotient stack a
> gerbe over `X`.
>
> The criterion is `AlgebraicGeometry.Stack.isGerbeOver_quotientStackToBase_of_locallyFull`
> (**Stacks 06PE** for the 1-morphism of **Stacks 0DUH**); its surjectivity clause is Stacks 06PG
> and its local-fullness clause is **Stacks 046O**, both in the sieve form the criterion asks
> for.

```lean
theorem isGerbeOver_quotientStackToBase_overArrowStabilizerQuotient
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (hX : IsAlgebraicSpace C S hS
      (Space.quotientSheaf (arrowStabilizerQuotientPreRelation G)).obj) :
    CategoryTheory.IsGerbeOver (BigFppfOver.topology C S hS)
      (fibredCategory C S hS (arrowStabilizerQuotientSpace G hX).obj).val.p
      (quotientStackToBase (overArrowStabilizerQuotient G hX)).toFunctor
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.mono_arrowStabilizerQuotientPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientRelation.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientRelation.lean#L396). The attribute's comment: “the implication (2) implies (1): j' = (t', s') is a monomorphism”. References: SGA 3 V (10.4), “partial”.

> **Stacks 043C part (2) for `R/S`: `j' = (t', s')` is a monomorphism.** This is the step of
> the proof of **Stacks 06QJ**, the implication (2) `⟹` (1), which makes the quotient `R' = R/S` of
> the arrow space by the stabilizer action a relation on the object space; with the
> pre-equivalence-relation clause of **Stacks 043X** it is an equivalence relation.
>
> Two sections of `R'` over a test object with the same source and the same target lift, after an
> fppf covering, to arrows of `R` with the same source and the same target, and two such arrows lie
> in a single orbit of the stabilizer: the loop `c(a, i(b))` at their common target carries one to
> the other. So they already agree in `R'`, and `R'` is an fppf sheaf.

```lean
theorem mono_arrowStabilizerQuotientPreRelation
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Mono (arrowStabilizerQuotientPreRelation G)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isEquivalenceRelation_arrowStabilizerQuotientPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientRelation.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/ArrowQuotientRelation.lean#L565). The attribute's comment: “the implication (2) implies (1): j' = (t', s') is an equivalence relation”.

> **The quotient `R' = R/S` of the arrow space by the stabilizer action is an equivalence
> relation on the object space** — **Stacks 043C** part (4). This is the step of the proof of
> **Stacks 06QJ**, the implication (2) `⟹` (1), after which the quotient `X = U/R'` is an algebraic
> space by **Stacks 04S6**.
>
> By `AlgebraicGeometry.Space.isEquivalenceRelation_iff_mono_and_isPreEquivalenceRelation` an
> equivalence relation is exactly a monomorphic pre-equivalence relation, and the two halves are
> `mono_arrowStabilizerQuotientPreRelation` and
> `isPreEquivalenceRelation_arrowStabilizerQuotientPreRelation`. Nothing is assumed.

```lean
theorem isEquivalenceRelation_arrowStabilizerQuotientPreRelation
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    CategoryTheory.IsEquivalenceRelation
      (arrowStabilizerQuotientPreRelation G).target
      (arrowStabilizerQuotientPreRelation G).source
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_inertiaProjection_of_isGerbe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeInertiaCharacterization.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeInertiaCharacterization.lean#L172). The attribute's comment: “(1) implies (2)”.

> **Stacks 06QJ, the implication (1) `⟹` (2).** If an algebraic stack `𝒳` over `S` is a gerbe,
> then the forgetful 1-morphism `I_𝒳 ⟶ 𝒳` of its inertia is flat and locally of finite
> presentation.
>
> Let `𝒳 ⟶ Y` make `𝒳` a gerbe over an algebraic space `Y` and choose a smooth groupoid presentation
> `𝒳 ≃ [U/R]` (Stacks 04T3). The composite `[U/R] ⟶ Y` is a gerbe, so for its restriction
> `ψ : U ⟶ Y` the arrows cover the related pairs `U ×_Y U`
> (`AlgebraicGeometry.Stack.isLocallySurjective_of_isGerbeOver_restrictedMorphism`), and the
> stabilizer of the groupoid is flat and locally of finite presentation
> (`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_stabilizer_of_isLocallySurjective`, the
> argument of Stacks 06PL and Stacks 06PJ). The automorphism sheaves of `𝒳` are, fppf-locally,
> these stabilizers (Stacks 044V), and flatness and local finite presentation descend
> (Stacks 041W, Stacks 041T); that is clause (2), by
> `AlgebraicGeometry.Stack.isFlat_inertiaProjection_iff_isomSpace`.

```lean
theorem isFlat_and_isLocallyOfFinitePresentation_inertiaProjection_of_isGerbe
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsGerbe B S hS 𝒳) :
    IsFlat B S hS (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳) ∧
      IsLocallyOfFinitePresentation B S hS
        (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbe_iff_isFlat_and_isLocallyOfFinitePresentation_inertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeInertiaCharacterization.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeInertiaCharacterization.lean#L224).

> **Stacks 06QJ.** An algebraic stack `𝒳` over `S` is a gerbe if and only if the forgetful
> 1-morphism `I_𝒳 ⟶ 𝒳` of its inertia is flat and locally of finite presentation.
>
> The implication (1) `⟹` (2) is
> `isFlat_and_isLocallyOfFinitePresentation_inertiaProjection_of_isGerbe`, and the implication
> (2) `⟹` (1) is `isGerbe_of_isFlat_and_isLocallyOfFinitePresentation_inertiaProjection`.

```lean
theorem isGerbe_iff_isFlat_and_isLocallyOfFinitePresentation_inertiaProjection
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    IsGerbe B S hS 𝒳 ↔
      IsFlat B S hS (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳) ∧
        IsLocallyOfFinitePresentation B S hS
          (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbe_of_isFlat_and_isLocallyOfFinitePresentation_inertiaProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeOfFlatInertia.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeOfFlatInertia.lean#L175). The attribute's comment: “(2) implies (1): an algebraic stack whose inertia projection is flat and locally of finite presentation is a gerbe”.

> An algebraic stack `𝒳` over `S` whose inertia projection `I_𝒳 ⟶ 𝒳` is flat and locally of
> finite presentation is a gerbe: there are an algebraic space `X` and a 1-morphism `𝒳 ⟶ X` making
> `𝒳` a gerbe over `X`.

```lean
theorem isGerbe_of_isFlat_and_isLocallyOfFinitePresentation_inertiaProjection
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hflat : IsFlat B S hS (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (hlfp : IsLocallyOfFinitePresentation B S hS
      (Stack.inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    IsGerbe B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isFlat_presentationStabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationStabilizerFlat.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PresentationStabilizerFlat.lean#L91). The attribute's comment: “the implication (2) implies (1): flatness of the stabilizer of a presentation”.

> If the inertia projection `ℐ_𝒳 ⟶ 𝒳` of an algebraic stack `𝒳` over `S` is flat, then for
> every presentation `[U/R] ⟶ 𝒳` the structure morphism `G ⟶ U` of the stabilizer group algebraic
> space of the presenting groupoid is a flat morphism of algebraic spaces.

```lean
theorem isFlat_presentationStabilizer
    (hflat : AlgebraicStacks.IsFlat B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    Space.IsFlat B S hS (GroupoidInAlgebraicSpaces.stabilizer P.groupoid).hom
```

**`AlgebraicGeometry.Stack.isLocallyOfFinitePresentation_presentationStabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresentationStabilizerFlat.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/PresentationStabilizerFlat.lean#L106). The attribute's comment: “the implication (2) implies (1): local finite presentation of the stabilizer of a presentation”.

> If the inertia projection `ℐ_𝒳 ⟶ 𝒳` of an algebraic stack `𝒳` over `S` is locally of finite
> presentation, then for every presentation `[U/R] ⟶ 𝒳` the structure morphism `G ⟶ U` of the
> stabilizer group algebraic space of the presenting groupoid is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_presentationStabilizer
    (hlfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
      (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    Space.IsLocallyOfFinitePresentation B S hS
      (GroupoidInAlgebraicSpaces.stabilizer P.groupoid).hom
```

## Tag 0CPR, a lemma

[Tag 0CPR](https://stacks.math.columbia.edu/tag/0CPR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_relativeDiagonal_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean#L120). The attribute's comment: “part (2): the relative diagonal is surjective, flat and locally of finite presentation”.

> **Stacks 0CPR, part (2).** If a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` makes
> `𝒳` a gerbe over `𝒴`, then its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` is surjective, flat and
> locally of finite presentation.
>
> Surjectivity is Stacks 06P1 (2)(b) read at a field-valued point
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isSurjective_relativeDiagonal_of_isGerbeOver`);
> flatness and local finite presentation hold because `Δ_f` is a section of the gerbe
> `𝒳 ×_𝒴 𝒳 ⟶ 𝒳`
> (`isFlat_and_isLocallyOfFinitePresentation_relativeDiagonal`).

```lean
theorem isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_relativeDiagonal_of_isGerbeOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsGerbeOver B S hS f) :
    Stack.IsSurjective B S hS (Stack.relativeDiagonalAlgebraicStacks B S hS f) ∧
      IsFlat B S hS (Stack.relativeDiagonalAlgebraicStacks B S hS f) ∧
      IsLocallyOfFinitePresentation B S hS (Stack.relativeDiagonalAlgebraicStacks B S hS f)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_and_isLocallyOfFinitePresentation_relativeInertiaProjection_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean#L139). The attribute's comment: “part (1): the relative inertia is flat and locally of finite presentation over the source”.

> **Stacks 0CPR, part (1).** If a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` makes
> `𝒳` a gerbe over `𝒴`, then the forgetful 1-morphism `I_{𝒳/𝒴} ⟶ 𝒳` of the relative inertia is
> flat and locally of finite presentation.
>
> The relative inertia is equivalent over the site to `𝒳 ×_{Δ_f, 𝒳 ×_𝒴 𝒳, Δ_f} 𝒳` in such a way
> that the forgetful 1-morphism becomes the first projection
> (`AlgebraicGeometry.Stack.AlgebraicStacks.relativeInertiaProjection_eq_comp_fst`), which is a base
> change of `Δ_f`; so part (2) together with **Stacks 06PY** and **Stacks 06Q4** gives the two
> properties for the projection, and they are unchanged by the comparison.

```lean
theorem isFlat_and_isLocallyOfFinitePresentation_relativeInertiaProjection_of_isGerbeOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsGerbeOver B S hS f) :
    IsFlat B S hS (Stack.relativeInertiaProjection B S hS f) ∧
      IsLocallyOfFinitePresentation B S hS (Stack.relativeInertiaProjection B S hS f)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_comparison_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean#L176). The attribute's comment: “part (3): the comparison of the two fibre products of a pair of algebraic spaces over the stacks is surjective, flat and locally of finite presentation”.

> **Stacks 0CPR, part (3).** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`
> making `𝒳` a gerbe over `𝒴`, let `T₁` and `T₂` be algebraic spaces over `S` and let
> `x_i : T_i ⟶ 𝒳` be 1-morphisms, with `y_i = x_i ≫ f`. Then the comparison 1-morphism
>
>     T₁ ×_{x₁, 𝒳, x₂} T₂ ⟶ T₁ ×_{y₁, 𝒴, y₂} T₂
>
> is surjective, flat and locally of finite presentation.
>
> By **Stacks 04Z1** that comparison is a base change of the relative diagonal `Δ_f`, which has the
> three properties by part (2), and they base change by **Stacks 04ZU**, **Stacks 06PY** and
> **Stacks 06Q4**.

```lean
theorem isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_comparison_of_isGerbeOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsGerbeOver B S hS f) (T₁ T₂ : AlgebraicSpaces B S hS)
    (x₁ : ofAlgebraicSpace.{u, w} B S hS T₁ ⟶ 𝒳)
    (x₂ : ofAlgebraicSpace.{u, w} B S hS T₂ ⟶ 𝒳) :
    Stack.IsSurjective B S hS (Stack.comparison B S hS x₁ x₂ f) ∧
      IsFlat B S hS (Stack.comparison B S hS x₁ x₂ f) ∧
      IsLocallyOfFinitePresentation B S hS (Stack.comparison B S hS x₁ x₂ f)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isomMap_isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeRelativeDiagonal.lean#L222). The attribute's comment: “part (4): the morphism of isomorphism spaces is surjective, flat and locally of finite presentation”.

> **Stacks 0CPR, part (4).** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`
> making `𝒳` a gerbe over `𝒴`, let `T` be an algebraic space over `S` and let `x₁, x₂ : T ⟶ 𝒳` be
> 1-morphisms, with `y_i = x_i ≫ f`. Then the morphism
>
>     Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)
>
> which applies `f` to an isomorphism `x₁(t) ≅ x₂(t)` is representable by algebraic spaces, and
> it is surjective, flat and locally of finite presentation: for every scheme `U` over `S` and
> every object of `Isom_𝒴(y₁, y₂)` over `U`, the morphism to `U` from the algebraic space
> representing the base change is surjective, flat and locally of finite presentation
> (**Stacks 04XB**).
>
> As in the source, `Isom_𝒳(x₁, x₂) ⟶ Isom_𝒴(y₁, y₂)` is a base change of the comparison
> `T ×_{x₁, 𝒳, x₂} T ⟶ T ×_{y₁, 𝒴, y₂} T` of part (3)
> (`AlgebraicGeometry.Stack.HigherDiagonal.isTwoFibreProduct_isomSquare`), which is a base change of
> `Δ_f` (**Stacks 050H**). The relative diagonal is representable by algebraic spaces, so its three
> properties of part (2) are its relative properties in the sense of Stacks 04XB, by **Stacks 04XI**
> for surjectivity and by **Stacks 06FM**, the assertion for representable morphisms, for flatness
> and local finite presentation; and these pass along the two base changes.

```lean
theorem isomMap_isSurjective_and_isFlat_and_isLocallyOfFinitePresentation_of_isGerbeOver
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (hf : IsGerbeOver B S hS f)
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hT : IsAlgebraicSpace B S hS T)
    (x₁ x₂ : algebraicSpaceStack.{u, w} B S hS T hT ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpaces B S hS (HigherDiagonal.isomMap B S hS f T hT x₁ x₂).hom ∧
    ∀ (U : BigFppfOver B S hS)
      (z : BigFppfOver B U.left.1 U.left.2 ⥤
        (HigherDiagonal.isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.obj)
      (_hz : z ⋙ (HigherDiagonal.isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.p =
        Over.map U.hom)
      (G : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hG : IsAlgebraicSpace B U.left.1 U.left.2 G),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (HigherDiagonal.isomStack B S hS T hT x₁ x₂).val.p
            (HigherDiagonal.isomStack B S hS T hT (x₁ ≫ f) (x₂ ≫ f)).val.p z
            (CatFiberedInGroupoids.homFunctor (HigherDiagonal.isomMap B S hS f T hT x₁ x₂)))
          (presheafOfCategories (G ⋙ typeToCat)).p) →
        Space.IsSurjective B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨G, hG⟩)).hom ∧
          Space.IsFlat B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨G, hG⟩)).hom ∧
          Space.IsLocallyOfFinitePresentation B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨G, hG⟩)).hom
```

## Tag 0CPS, a proposition

[Tag 0CPS](https://stacks.math.columbia.edu/tag/0CPS) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isGerbeOver_iff_isSurjective_isFlat_isLfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatDiagonalCharacterization.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeFlatDiagonalCharacterization.lean#L195).

> **Stacks 0CPS.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. Then `𝒳` is
> a gerbe over `𝒴` if and only if `f` and its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` are both
> surjective, flat and locally of finite presentation.
>
> The implication from the gerbe condition is **Stacks 06QI** and **Stacks 0CPR**, part (2)
> (`isSurjective_isFlat_isLfp_of_isGerbeOver`); the converse reads both clauses of the gerbe
> condition off **Stacks 06QA** applied to `f` and to `Δ_f`
> (`isGerbeOver_of_isSurjective_isFlat_isLfp`).

```lean
theorem isGerbeOver_iff_isSurjective_isFlat_isLfp
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    IsGerbeOver B S hS f ↔
      (Stack.IsSurjective B S hS f ∧ IsFlat B S hS f ∧
          IsLocallyOfFinitePresentation B S hS f) ∧
        (Stack.IsSurjective B S hS (Stack.relativeDiagonalAlgebraicStacks B S hS f) ∧
          IsFlat B S hS (Stack.relativeDiagonalAlgebraicStacks B S hS f) ∧
          IsLocallyOfFinitePresentation B S hS
            (Stack.relativeDiagonalAlgebraicStacks B S hS f))
```

## Tag 06QK, a lemma

[Tag 06QK](https://stacks.math.columbia.edu/tag/06QK) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_gerbeOver_reducedLocallyNoetherianWithUniquePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedSingletonStackGerbe.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedSingletonStackGerbe.lean#L109). The attribute's comment: “The field cover of Stacks 06MP (1) implies (2), the flatness and local finite presentation of the inertia and their fppf descent, Stacks 06QJ (2) implies (1), the gerbe 1-morphism being surjective, flat and locally of finite presentation by Stacks 06QI, and the conclusion about the base by Stacks 06MP (2) implies (1) applied to the composite from the field spectrum”.

> **Stacks 06QK.** Let `𝒵` be a reduced, locally Noetherian algebraic stack over `S` whose
> space of points is a singleton. Then there is an algebraic stack `Z` over `S` which is
> representable by an algebraic space, a 1-morphism `π : 𝒵 ⟶ Z` making `𝒵` a gerbe over `Z`, and
> `Z` is again reduced, locally Noetherian with a single point.

```lean
theorem exists_gerbeOver_reducedLocallyNoetherianWithUniquePoint
    (𝒵 : Stack.AlgebraicStacks.{u, w} B S hS)
    (h𝒵 : Stack.IsReducedLocallyNoetherianWithUniquePoint B S hS 𝒵) :
    ∃ Z : Stack.AlgebraicStacks.{u, w} B S hS,
      IsRepresentableByAlgebraicSpace B S hS Z.val ∧
        (∃ π : 𝒵 ⟶ Z, IsGerbeOver B S hS π) ∧
          Stack.IsReducedLocallyNoetherianWithUniquePoint B S hS Z
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_gerbeOver_reducedLocallyNoetherianWithUniquePoint_unconditional`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedSingletonStackGerbeUnconditional.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedSingletonStackGerbeUnconditional.lean#L52). The attribute's comment: “unconditional. The field cover of Stacks 06MP (1) implies (2), the flatness and local finite presentation of the inertia and their fppf descent, Stacks 06QJ (2) implies (1) cited from GerbeOfFlatInertia, the gerbe 1-morphism being surjective, flat and locally of finite presentation by Stacks 06QI, and the conclusion about the base by Stacks 06MP (2) implies (1) applied to the composite from the field spectrum”.

> Let `𝒵` be a reduced, locally Noetherian algebraic stack over `S` whose space of points is a
> singleton. Then there is an algebraic stack `Z` over `S` which is representable by an algebraic
> space, a 1-morphism `π : 𝒵 ⟶ Z` making `𝒵` a gerbe over `Z`, and `Z` is again reduced, locally
> Noetherian with a single point.

```lean
alias exists_gerbeOver_reducedLocallyNoetherianWithUniquePoint_unconditional
```

## Tag 06R9, a lemma

[Tag 06R9](https://stacks.math.columbia.edu/tag/06R9) in the Stacks Project.

**`AlgebraicGeometry.Stack.universalHomeomorphism_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeUniversalHomeo.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeUniversalHomeo.lean#L191).

> **Stacks 06R9.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` which exhibits `𝒳` as
> a gerbe over `𝒴` is a universal homeomorphism in the sense of Stacks 0CI7.
>
> The gerbe condition base changes (Stacks 06QE), so each projection `|𝒵 ×_𝒴 𝒳| → |𝒵|` is a
> homeomorphism by `AlgebraicGeometry.Stack.isHomeomorph_pointsMap_of_isGerbeOver`.

```lean
theorem universalHomeomorphism_of_isGerbeOver {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsGerbeOver B S hS f) :
    UniversalHomeomorphism B S hS f
```

## Tag 0DQL, a lemma

[Tag 0DQL](https://stacks.math.columbia.edu/tag/0DQL) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiCompactMorphism_diagonal_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactDiagonalGerbe.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactDiagonalGerbe.lean#L485).

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which makes `𝒳` a gerbe over
> `𝒴`. If the diagonal of `𝒳` is quasi-compact, then so is the diagonal of `𝒴`.

```lean
theorem isQuasiCompactMorphism_diagonal_of_isGerbeOver (f : 𝒳 ⟶ 𝒴)
    (hf : IsGerbeOver B S hS f)
    (hΔ : Stack.IsQuasiCompactMorphism B S hS (diagonal B S hS 𝒳)) :
    Stack.IsQuasiCompactMorphism B S hS (diagonal B S hS 𝒴)
```

## Tag 06RA, a lemma

[Tag 06RA](https://stacks.math.columbia.edu/tag/06RA) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_isGerbe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbeExistence.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbeExistence.lean#L187).

> **Stacks 06RA.** An algebraic stack over `S` which is a gerbe (**Stacks 06QC**) satisfies
> condition (1) of **Stacks 06MT** at every point of its space of points; that is, its residual
> gerbe exists at every point.
>
> A gerbe comes with a 1-morphism `f : 𝒳 ⟶ 𝒴` to an algebraic stack representable by an algebraic
> space which makes `𝒳` a gerbe over `𝒴`. Condition (1) holds for `𝒴` at the image of the point by
> `AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_isRepresentableByAlgebraicSpace`, and
> transports back along `f` by the existence clause of **Stacks 0H24**.

```lean
theorem hasSingletonPointMonomorphism_of_isGerbe
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : AlgebraicStacks.IsGerbe B S hS 𝒳)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property)) :
    HasSingletonPointMonomorphism B S hS 𝒳 x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.28, Tag 06QB](https://stacks.math.columbia.edu/tag/06QB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
