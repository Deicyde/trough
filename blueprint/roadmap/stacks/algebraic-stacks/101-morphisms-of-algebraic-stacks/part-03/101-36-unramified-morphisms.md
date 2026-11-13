---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsUnramified, AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_comp, AlgebraicGeometry.Stack.isUnramified_baseChange_of_isUnramifiedOnEveryEtaleDiagram, AlgebraicGeometry.Stack.isUnramified_snd_of_isTwoFibreProduct, AlgebraicGeometry.Stack.isUnramified_of_isEtale, AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_of_isImmersion, AlgebraicGeometry.Stack.isUnramified_tfae, AlgebraicGeometry.Stack.isUnramified_of_isUnramifiedOnEveryEtaleDiagram
statement: formalized
proof: formalized
---

# 101.36 Unramified morphisms

Section 101.36 of the Stacks Project, [Tag 0CIS](https://stacks.math.columbia.edu/tag/0CIS). 10 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CIT, a definition

[Tag 0CIT](https://stacks.math.columbia.edu/tag/0CIT) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSmoothLocalMorphism.lean#L218).

> **Stacks 0CIT.** A 1-morphism of algebraic stacks over `S` is *unramified* when it is
> Deligne–Mumford and its universal étale-smooth diagram tests are unramified morphisms of
> algebraic spaces, in the sense of `AlgebraicGeometry.Space.IsUnramified` (**Stacks 03ZH**,
> part (1)).

```lean
abbrev IsUnramified {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CIU, a lemma

[Tag 0CIU](https://stacks.math.columbia.edu/tag/0CIU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedMorphismComp.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedMorphismComp.lean#L58). The attribute's comment: “for 1-morphisms of algebraic stacks over a scheme S of the big fppf site; proved as in the source through Stacks 0CIH, with Stacks 06N3 (1) => (2) supplied by existsEtalePresentationOfIsAbsolutelyDM”.

> **Stacks 0CIU.** The composition of unramified 1-morphisms of algebraic stacks over `S` is
> unramified: for `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` unramified, so is `f ≫ g`.
>
> This is **Stacks 0CIH** at unramifiedness of morphisms of algebraic spaces, which is étale-smooth
> local on the source-and-target by **Stacks 0CG3** and stable under composition by
> **Stacks 03ZI**.

```lean
theorem isUnramified_comp
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsUnramified B S hS f) (hg : IsUnramified B S hS g) :
    IsUnramified B S hS (f ≫ g)
```

## Tag 0CIV, a lemma

[Tag 0CIV](https://stacks.math.columbia.edu/tag/0CIV) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUnramified_baseChange_of_isUnramifiedOnEveryEtaleDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedBaseChange.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedBaseChange.lean#L99). The attribute's comment: “f : X -> Y is unramified in the sense of Stacks 0CIT, g : Y' -> Y is any 1-morphism of algebraic stacks over S and R is any 2-fibre product of (g, f); the base change R.fst : R.pt -> Y' is unramified in the sense of Stacks 0CIT”.

> A base change of an unramified 1-morphism of algebraic stacks over `S` is unramified: if
> `f : 𝒳 ⟶ 𝒴` is unramified, `g : 𝒴' ⟶ 𝒴` is any 1-morphism and `R` is any 2-fibre product of
> `(g, f)`, then the projection `R.fst : R.pt ⟶ 𝒴'` is unramified in the sense of Stacks 0CIT.

```lean
theorem isUnramified_baseChange_of_isUnramifiedOnEveryEtaleDiagram
    {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (g : 𝒴' ⟶ 𝒴) (R : Bicategory.TwoCommSq g f) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : IsUnramified B S hS f) :
    IsUnramified B S hS R.fst
```

**`AlgebraicGeometry.Stack.isUnramified_snd_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedBaseChange.lean#L111). The attribute's comment: “the same statement with the 2-fibre product written as a square of (f, g): for f unramified in the sense of Stacks 0CIT and any g, the second projection R.snd is unramified”.

> If `f : 𝒳 ⟶ 𝒴` is unramified, `g : 𝒴' ⟶ 𝒴` is any 1-morphism and `R` is any 2-fibre product
> of `(f, g)`, then the projection `R.snd : R.pt ⟶ 𝒴'` is unramified in the sense of Stacks 0CIT.

```lean
theorem isUnramified_snd_of_isTwoFibreProduct
    {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (g : 𝒴' ⟶ 𝒴) (R : Bicategory.TwoCommSq f g) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : IsUnramified B S hS f) :
    IsUnramified B S hS R.snd
```

## Tag 0CIW, a lemma

[Tag 0CIW](https://stacks.math.columbia.edu/tag/0CIW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUnramified_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedAlgebraicStack.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedAlgebraicStack.lean#L37).

> An étale 1-morphism of algebraic stacks over `S` is unramified.

```lean
theorem isUnramified_of_isEtale {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : IsEtale B S hS f) : IsUnramified B S hS f
```

## Tag 0CIX, a lemma

[Tag 0CIX](https://stacks.math.columbia.edu/tag/0CIX) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionUnramified.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionUnramified.lean#L58).

> **Stacks 0CIX.** An immersion of algebraic stacks over `S`, in the sense of Stacks 04YL,
> part (3), is unramified in the sense of Stacks 0CIT.

```lean
theorem isUnramified_of_isImmersion (j : 𝒵 ⟶ 𝒳) (hj : IsImmersion B S hS j) :
    Stack.IsUnramified B S hS j
```

## Tag 0CIY, a lemma

[Tag 0CIY](https://stacks.math.columbia.edu/tag/0CIY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUnramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedCharacterizationTFAE.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedCharacterizationTFAE.lean#L52).

> **Stacks 0CIY.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent:
> 1. `f` is unramified (**Stacks 0CIT**);
> 2. `f` is DM, and for every algebraic space `V` with a 1-morphism `V ⟶ 𝒴` and every algebraic
>    space `U` with an étale 1-morphism `U ⟶ V ×_𝒴 𝒳`, the morphism `U ⟶ V` is unramified;
> 3. there are an algebraic space `W` with a surjective, flat, locally finitely presented
>    1-morphism `W ⟶ 𝒴` and an algebraic space `T` with a surjective étale 1-morphism
>    `T ⟶ 𝒳 ×_𝒴 W` such that `T ⟶ W` is unramified.

```lean
theorem isUnramified_tfae {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    [IsUnramified B S hS f, IsUnramifiedOnEveryEtaleDiagram.{u, w} B S hS f,
      HasUnramifiedEtalePresentationOverFlatCover.{u, w} B S hS f].TFAE
```

**`AlgebraicGeometry.Stack.isUnramified_of_isUnramifiedOnEveryEtaleDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedEtaleDiagram.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedEtaleDiagram.lean#L113). The attribute's comment: “the implication (2) => (1)”.

> **Stacks 0CIY, the implication (2) ⇒ (1).** A Deligne–Mumford 1-morphism of algebraic stacks
> over `S` whose every étale diagram of algebraic spaces has unramified top horizontal morphism is
> unramified in the sense of Stacks 0CIT.

```lean
theorem isUnramified_of_isUnramifiedOnEveryEtaleDiagram
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : IsUnramifiedOnEveryEtaleDiagram.{u, w} B S hS f) :
    IsUnramified B S hS f
```

**`AlgebraicGeometry.Stack.isUnramifiedOnEveryEtaleDiagram_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedEtaleDiagramForward.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedEtaleDiagramForward.lean#L85). The attribute's comment: “the implication (1) => (2)”.

> **Stacks 0CIY, the implication (1) ⇒ (2).** An unramified 1-morphism of algebraic stacks is
> DM and every étale diagram of algebraic spaces over it has unramified top horizontal morphism.

```lean
theorem isUnramifiedOnEveryEtaleDiagram_of_isUnramified
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} (hf : IsUnramified B S hS f) :
    IsUnramifiedOnEveryEtaleDiagram.{u, w} B S hS f
```

**`AlgebraicGeometry.Stack.isDM_of_surjectiveEtalePresentation_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedFlatPresentation.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedFlatPresentation.lean#L111). The attribute's comment: “the Deligne-Mumford condition on f, which is the first conjunct of each of parts (1) and (2), from part (3); the unramifiedness of T -> W asserted by part (3) is not needed for it, and the easy direction of Stacks 06N3 that the source cites is taken in the form Stacks 06MB part (1), whose absolute Deligne-Mumford conclusion asks the big site to contain the terminal scheme”.

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `W` be an algebraic space
> with a surjective, flat, locally-of-finite-presentation 1-morphism `c : W ⟶ 𝒴`, and let the
> 2-fibre product `𝒳 ×_𝒴 W` admit a surjective étale 1-morphism from an algebraic space `T`. Then
> `f` is Deligne–Mumford.

```lean
theorem isDM_of_surjectiveEtalePresentation_flatBaseChange
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hW : IsAlgebraicSpace B S hS W)
    (c : algebraicSpaceStack.{u, w} B S hS W hW ⟶ 𝒴)
    (hcSurj : IsSurjective B S hS c)
    (hcFlat : AlgebraicStacks.IsFlat B S hS c)
    (hcLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS c)
    (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hT : IsAlgebraicSpace B S hS T)
    (t : algebraicSpaceStack.{u, w} B S hS T hT ⟶
      (twoFibreProductSquareAlgebraicStacks B S hS f c).pt)
    (htSurj : IsSurjective B S hS t)
    (htEt : IsRelativelyEtale B S hS t.hom) :
    IsDM B S hS f
```

## Tag 0H2Z, a lemma

[Tag 0H2Z](https://stacks.math.columbia.edu/tag/0H2Z) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyQuasiFinite_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedIsLocallyQuasiFinite.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedIsLocallyQuasiFinite.lean#L253).

> **Stacks 0H2Z.** An unramified 1-morphism of algebraic stacks over `S` (**Stacks 0CIT**) is
> locally quasi-finite (**Stacks 06PU**): it is quasi-DM, locally of finite type, and its fibre over
> every field-valued point of the target has discrete space of points.
>
> The three conjuncts are `AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isUnramified`,
> the existential smooth-diagram test
> `AlgebraicGeometry.Stack.AlgebraicStacks.hasPropertyOnSomeSmoothDiagram_of_isUnramified` at the
> diagram `AlgebraicGeometry.Stack.hasSurjectiveEtaleSmoothDiagram_of_isDM`, and
> `AlgebraicGeometry.Stack.discreteTopology_points_fibre_of_isUnramified`.

```lean
theorem isLocallyQuasiFinite_of_isUnramified
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsUnramified B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasiDM_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedLocallyQuasiFinite.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedLocallyQuasiFinite.lean#L121). The attribute's comment: “the quasi-DM conjunct of local quasi-finiteness, unconditionally. The local finite type conjunct is `isLocallyOfFiniteType_of_isUnramified`; the field-valued-fibre conjunct is NOT carried”.

> **The quasi-DM conjunct of Stacks 0H2Z.** An unramified 1-morphism of algebraic stacks over
> `S` is quasi-DM, with a representable relative diagonal.
>
> Unramifiedness in the sense of **Stacks 0CIT** contains the Deligne–Mumford condition, and a
> Deligne–Mumford 1-morphism is quasi-DM by **Stacks 050E**, part (2); the relative diagonal of a
> 1-morphism of algebraic stacks is always representable by algebraic spaces.

```lean
theorem isQuasiDM_of_isUnramified {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : Stack.IsUnramified B S hS f) :
    IsQuasiDMWithRepresentableDiagonal B S hS f
```

## Tag 0CIZ, a lemma

[Tag 0CIZ](https://stacks.math.columbia.edu/tag/0CIZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUnramified_of_comp_of_isDM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedPermanenceUnconditional.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedPermanenceUnconditional.lean#L58). The attribute's comment: “The whole statement, under exactly the source's hypotheses.”.

> **Stacks 0CIZ.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over
> `S`. If `f ≫ g` is unramified and `g` is Deligne–Mumford, then `f` is unramified.
>
> `f` is Deligne–Mumford by Stacks 050M. Choose a surjective smooth `W ⟶ 𝒵`, a surjective étale
> `V ⟶ 𝒴 ×_𝒵 W` and a surjective étale `U ⟶ 𝒳 ×_𝒴 V`, the last two by Stacks 0CIA (the second
> because `g` is Deligne–Mumford, the third because `f` is); then `U ⟶ W` is unramified, and
> `U ⟶ V` is unramified by Stacks 06G6.

```lean
theorem isUnramified_of_comp_of_isDM {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hfg : IsUnramified B S hS (f ≫ g)) (hg : IsDM B S hS g) :
    IsUnramified B S hS f
```

## Tag 0CJ0, a lemma

[Tag 0CJ0](https://stacks.math.columbia.edu/tag/0CJ0) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_iff_isLocallyOfFiniteType_and_isEtale_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedDiagonalCriterion.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedDiagonalCriterion.lean#L235). The attribute's comment: “both implications: unramified iff locally of finite type with etale diagonal”.

> **Stacks 0CJ0.** A 1-morphism of algebraic stacks over `S` admitting a diagram of algebraic
> spaces as in `AlgebraicGeometry.Stack.HasDiagonalDescentChart` is unramified exactly when it is
> locally of finite type and its relative diagonal is étale.
>
> Unramifiedness and local finite type are tested on the diagram's top morphism `h` of algebraic
> spaces, and étaleness of the relative diagonal is tested on the relative diagonal of `h`; the
> equivalence is then Stacks 05W1. Deligne–Mumfordness in the converse direction comes from
> étaleness of the relative diagonal, étale morphisms of algebraic spaces being unramified by
> Stacks 06CR.

```lean
theorem isUnramified_iff_isLocallyOfFiniteType_and_isEtale_relativeDiagonal
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hchart : Stack.HasDiagonalDescentChart.{u, w} B S hS f) :
    Stack.IsUnramified B S hS f ↔
      (IsLocallyOfFiniteType B S hS f ∧
        Stack.IsEtale B S hS (relativeDiagonal B S hS f))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUnramified_iff_isLocallyOfFiniteType_isEtale_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedDiagonalEtale.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UnramifiedDiagonalEtale.lean#L55).

> **Stacks 0CJ0.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is unramified if and
> only if it is locally of finite type and its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` is étale.
>
> The implication (2) ⇒ (1) is
> `isUnramified_of_isLocallyOfFiniteType_of_isEtale_relativeDiagonal`;
> (1) ⇒ (2) is
> `isLocallyOfFiniteType_and_isEtale_relativeDiagonal_of_isUnramified_of_etalePresentation`
> at the structure theorem of Stacks 06N3,
> `AlgebraicGeometry.Stack.existsEtalePresentationOfIsAbsolutelyDM`, through which Stacks 0CIA is
> available.

```lean
theorem isUnramified_iff_isLocallyOfFiniteType_isEtale_relativeDiagonal
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    Stack.IsUnramified B S hS f ↔
      (IsLocallyOfFiniteType B S hS f ∧ Stack.IsEtale B S hS (relativeDiagonal B S hS f))
```

## Tag 0CJ1, a lemma

[Tag 0CJ1](https://stacks.math.columbia.edu/tag/0CJ1) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_of_isLocallyOfFinitePresentation_of_isFlat_of_isUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleFlatUnramifiedCriterion.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleFlatUnramifiedCriterion.lean#L241). The attribute's comment: “part (2) implies part (1)”.

> **Stacks 0CJ1, (2) ⇒ (1).** A 1-morphism of algebraic stacks over `S` which is locally of
> finite presentation, flat and unramified is étale. No diagram has to be supplied.
>
> Deligne–Mumfordness is part of unramifiedness. For the universal étale-smooth test, take a
> diagram it offers: its right leg is smooth, its left leg is smooth by
> `AlgebraicGeometry.Stack.isRelativelySmooth_of_etaleSmoothDiagram` and its comparisons are smooth
> because they are étale, so the universal *smooth* test of Stacks 06FM applies to it as well. That
> gives local finite presentation of its top morphism directly, and flatness after Stacks 06FM
> turns the existential test of Stacks 06PW into the universal one; unramifiedness is the
> hypothesis at that diagram. Stacks 06LU concludes.

```lean
theorem isEtale_of_isLocallyOfFinitePresentation_of_isFlat_of_isUnramified
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hlfp : IsLocallyOfFinitePresentation B S hS f) (hflat : IsFlat B S hS f)
    (hunr : Stack.IsUnramified B S hS f) :
    Stack.IsEtale B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isEtale_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleFlatUnramifiedTFAE.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleFlatUnramifiedTFAE.lean#L66).

> **Stacks 0CJ1.** For a 1-morphism `f` of algebraic stacks over `S` the following are
> equivalent: `f` is étale; `f` is locally of finite presentation, flat and unramified; `f` is
> locally of finite presentation, flat and has étale relative diagonal.
>
> (2) ⇔ (3) is Stacks 0CJ0 together with Stacks 06Q5; (2) ⇒ (1) is Stacks 06LU on the top morphism
> of an étale-smooth diagram; (1) ⇒ (2) uses the diagram Stacks 0CIA provides for the
> Deligne–Mumford 1-morphism `f`.

```lean
theorem isEtale_tfae {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [Stack.IsEtale B S hS f,
        IsLocallyOfFinitePresentation B S hS f ∧ IsFlat B S hS f ∧ Stack.IsUnramified B S hS f,
        IsLocallyOfFinitePresentation B S hS f ∧ IsFlat B S hS f ∧
          Stack.IsEtale B S hS (relativeDiagonal B S hS f)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.36, Tag 0CIS](https://stacks.math.columbia.edu/tag/0CIS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
