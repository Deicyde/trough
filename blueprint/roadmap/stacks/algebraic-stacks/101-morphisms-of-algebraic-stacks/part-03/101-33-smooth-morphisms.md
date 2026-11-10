---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsSmooth, AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_of_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_isSmooth, AlgebraicGeometry.Stack.smoothLocus, AlgebraicGeometry.Stack.isSmooth_quotientStackModelToBase, AlgebraicGeometry.Stack.AlgebraicStacks.isSurjective_and_isSmooth_of_isGerbeOver
statement: formalized
proof: formalized
---

# 101.33 Smooth morphisms

Section 101.33 of the Stacks Project, [Tag 075T](https://stacks.math.columbia.edu/tag/075T). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 075U, a definition

[Tag 075U](https://stacks.math.columbia.edu/tag/075U) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStack.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStack.lean#L93).

> **Stacks 075U.** A 1-morphism of algebraic stacks over `S` is *smooth* when it passes the
> existential smooth-diagram test of Stacks 06FM at smoothness of morphisms of algebraic spaces:
> there are algebraic spaces `U`, `V` over `S`, a smooth 1-morphism `a` from the category fibred in
> groupoids of `U` to the source which is surjective on objects, a smooth 1-morphism `b` from the
> one of `V` to the target, and a morphism `h : U ⟶ V` making the square 2-commute, with `h` a
> smooth morphism of algebraic spaces.

```lean
abbrev IsSmooth {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 075V, a lemma

[Tag 075V](https://stacks.math.columbia.edu/tag/075V) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStackComposition.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStackComposition.lean#L71).

> **Stacks 075V.** The composite of two smooth 1-morphisms of algebraic stacks over `S` is
> smooth: the composition remark Stacks 06FP at smoothness of morphisms of algebraic spaces, which
> is smooth local on the source-and-target by the smooth case of Stacks 06FC and stable under
> composition by Stacks 03ZD.

```lean
theorem isSmooth_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsSmooth B S hS f) (hg : IsSmooth B S hS g) :
    IsSmooth B S hS (f ≫ g)
```

## Tag 075W, a lemma

[Tag 075W](https://stacks.math.columbia.edu/tag/075W) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStackBaseChange.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothAlgebraicStackBaseChange.lean#L62).

> **Stacks 075W.** A base change of a smooth 1-morphism of algebraic stacks over `S` is
> smooth: for `f : 𝒳 ⟶ 𝒴` smooth and `g : 𝒴' ⟶ 𝒴` arbitrary, the projection to `𝒴'` of any
> 2-fibre product square over the cospan `(g, f)` is smooth.

```lean
theorem isSmooth_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (Q : Bicategory.TwoCommSq g f) (hQ : Bicategory.IsTwoFibreProduct Q)
    (hf : IsSmooth B S hS f) :
    IsSmooth B S hS Q.fst
```

## Tag 0DN7, a lemma

[Tag 0DN7](https://stacks.math.columbia.edu/tag/0DN7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothFppfDescent.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothFppfDescent.lean#L63).

> **Stacks 0DN7.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : 𝒵 ⟶ 𝒴` be surjective, flat and locally of finite presentation. If the base change
> `𝒵 ×_𝒴 𝒳 ⟶ 𝒵` of `f` along `g` is smooth, then so is `f`.

```lean
theorem isSmooth_of_baseChange
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hgs : Stack.IsSurjective B S hS g)
    (hgflat : IsFlat B S hS g)
    (hglfp : IsLocallyOfFinitePresentation B S hS g)
    (hbase : IsSmooth B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst) :
    IsSmooth B S hS f
```

## Tag 0DNP, a lemma

[Tag 0DNP](https://stacks.math.columbia.edu/tag/0DNP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismMonotone.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismMonotone.lean#L104).

> **Stacks 0DNP.** A smooth 1-morphism of algebraic stacks over `S` is locally of finite
> presentation.
>
> Stacks 075U is the existential smooth-diagram criterion at smoothness of morphisms of algebraic
> spaces, which is locally of finite presentation by **Stacks 04AJ**; monotonicity (Stacks 06PS)
> gives the existential criterion at local finite presentation, and the round trip of
> Stacks 06FM — whose smooth-locality hypothesis is the local-finite-presentation case of
> Stacks 06FC — gives the universal criterion, which is Stacks 06Q2 part (1).

```lean
theorem isLocallyOfFinitePresentation_of_isSmooth
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsSmooth B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 0DZR, a lemma

[Tag 0DZR](https://stacks.math.columbia.edu/tag/0DZR) in the Stacks Project.

**`AlgebraicGeometry.Stack.smoothLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocus.lean, line 1221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocus.lean#L1221). The attribute's comment: “the maximal open substack on which f is smooth exists and is unique, and its formation commutes with precomposition by smooth morphisms, with base change by flat morphisms locally of finite presentation, and with flat base change when f is locally of finite presentation”.

> **Stacks 0DZR.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. There is a
> maximal open substack `𝒰 ⊆ 𝒳` such that `f|_𝒰 : 𝒰 ⟶ 𝒴` is smooth — an open substack on which `f`
> is smooth containing every other one, unique by maximality. Moreover, formation of this open
> substack commutes with
>
> 1. precomposing by smooth morphisms: for `g : 𝒳' ⟶ 𝒳` smooth, the open substack of `g ≫ f` is
>    the inverse image along `g` of that of `f`;
> 2. base change by morphisms which are flat and locally of finite presentation: for any 2-fibre
>    product `P` of `f` along such a `g : 𝒴' ⟶ 𝒴`, the open substack of the base change `P.fst` is
>    the inverse image along the projection `P.snd` of that of `f`;
> 3. base change by flat morphisms, provided `f` is locally of finite presentation.
>
> The open substack is constructed from a smooth chart of `f`: the image of the smooth locus of the
> chart's morphism of algebraic spaces (**Stacks 0DZI**), read as an open substack by
> **Stacks 06FJ** (`AlgebraicGeometry.Stack.openSubstackOfPoints`). Clause (1) is descent along the
> smooth `𝒰' ⟶ 𝒳`, and clauses (2) and (3) reduce to **Stacks 0DZI** on a cartesian square of
> charts.

```lean
theorem smoothLocus {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    (∃! W : OpenSubstack 𝒳, IsSmoothLocus B S hS f W) ∧
    (∀ (𝒳' : AlgebraicStacks.{u, w} B S hS) (g : 𝒳' ⟶ 𝒳),
      AlgebraicStacks.IsSmooth B S hS g →
      ∀ (W : OpenSubstack 𝒳) (W' : OpenSubstack 𝒳'),
        IsSmoothLocus B S hS f W → IsSmoothLocus B S hS (g ≫ f) W' →
          W'.property = fun x => W.property (g.hom.hom.toFunctor.obj x)) ∧
    (∀ (𝒴' : AlgebraicStacks.{u, w} B S hS) (g : 𝒴' ⟶ 𝒴) (P : Bicategory.TwoCommSq g f),
      Bicategory.IsTwoFibreProduct P →
      AlgebraicStacks.IsFlat B S hS g → AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g →
      ∀ (W : OpenSubstack 𝒳) (W' : OpenSubstack P.pt),
        IsSmoothLocus B S hS f W → IsSmoothLocus B S hS P.fst W' →
          W'.property = fun x => W.property (P.snd.hom.hom.toFunctor.obj x)) ∧
    (AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f →
      ∀ (𝒴' : AlgebraicStacks.{u, w} B S hS) (g : 𝒴' ⟶ 𝒴) (P : Bicategory.TwoCommSq g f),
        Bicategory.IsTwoFibreProduct P → AlgebraicStacks.IsFlat B S hS g →
        ∀ (W : OpenSubstack 𝒳) (W' : OpenSubstack P.pt),
          IsSmoothLocus B S hS f W → IsSmoothLocus B S hS P.fst W' →
            W'.property = fun x => W.property (P.snd.hom.hom.toFunctor.obj x))
```

## Tag 0DLS, a lemma

[Tag 0DLS](https://stacks.math.columbia.edu/tag/0DLS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSmooth_quotientStackModelToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothQuotientStackOfAction.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothQuotientStackOfAction.lean#L156).

> **Stacks 0DLS.** Let `X ⟶ Y` be a smooth morphism of algebraic spaces over `S`, let `G` be a
> group algebraic space over `Y` which is flat and locally of finite presentation over `Y`, and let
> `G` act on `X` over `Y`. Then the quotient stack `[X/G]` is smooth over `Y`: for every algebraic
> stack `𝒳` equivalent over the big fppf site to `[X/G]`, the canonical morphism `[X/G] ⟶ Y` of
> Stacks 044R, read on `𝒳`, is a smooth 1-morphism of algebraic stacks in the sense of
> Stacks 075U.

```lean
theorem isSmooth_quotientStackModelToBase
    (Y : AlgebraicSpaces B S hS) (G X : Over Y.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace B S hS G.left) (hX : IsAlgebraicSpace B S hS X.left)
    (hXsmooth : Space.IsSmooth B S hS X.hom)
    (hGflat : Space.IsFlat B S hS G.hom)
    (hGlfp : Space.IsLocallyOfFinitePresentation B S hS G.hom)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (e : StacksRepresentableCFG.EquivalenceOver
      (quotientStack (actionGroupoid B S hS Y G X hG hX)).p 𝒳.val.val.p) :
    AlgebraicStacks.IsSmooth B S hS
      (quotientStackModelToBase.{u, w} B S hS Y G X hG hX 𝒳 e)
```

## Tag 0DN8, a lemma

[Tag 0DN8](https://stacks.math.columbia.edu/tag/0DN8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSurjective_and_isSmooth_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeSmooth.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeSmooth.lean#L105).

> **Stacks 0DN8.** Let `π : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If `𝒳` is a
> gerbe over `𝒴`, then `π` is surjective and smooth.

```lean
theorem isSurjective_and_isSmooth_of_isGerbeOver {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hf : IsGerbeOver B S hS f) :
    Stack.IsSurjective B S hS f ∧ IsSmooth B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.33, Tag 075T](https://stacks.math.columbia.edu/tag/075T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
