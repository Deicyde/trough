---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyOfFinitePresentation, AlgebraicGeometry.Stack.AlgebraicStacks.IsFinitePresentation, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_of_isFinitePresentation, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isLocallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 101.27 Morphisms of finite presentation

Section 101.27 of the Stacks Project, [Tag 06Q1](https://stacks.math.columbia.edu/tag/06Q1). 17 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06Q2, a definition

[Tag 06Q2](https://stacks.math.columbia.edu/tag/06Q2) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyOfFinitePresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationAlgebraicStack.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationAlgebraicStack.lean#L96). The attribute's comment: “part (1): locally of finite presentation”.

> **Stacks 06Q2, part (1).** A 1-morphism of algebraic stacks over `S` is *locally of finite
> presentation* when it passes the universal smooth-diagram test of Stacks 06FM at local finite
> presentation of morphisms of algebraic spaces: every 2-commutative square of algebraic spaces
> over `f` whose two vertical 1-morphisms are smooth and whose every comparison 1-morphism to a
> 2-fibre product is smooth has its top horizontal morphism locally of finite presentation.

```lean
abbrev IsLocallyOfFinitePresentation {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsFinitePresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationAlgebraicStack.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationAlgebraicStack.lean#L104). The attribute's comment: “part (2): finite presentation”.

> **Stacks 06Q2, part (2).** A 1-morphism of algebraic stacks over `S` is *of finite
> presentation* when it is locally of finite presentation, quasi-compact and quasi-separated.

```lean
abbrev IsFinitePresentation {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06Q3, a lemma

[Tag 06Q3](https://stacks.math.columbia.edu/tag/06Q3) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean#L144). The attribute's comment: “locally of finite presentation”.

> **Stacks 06Q3**, the local assertion. The composite of two 1-morphisms of algebraic stacks
> over `S` which are locally of finite presentation is locally of finite presentation.
>
> Stacks 06Q2 part (1) is condition (1) of Stacks 06FM at local finite presentation of morphisms of
> algebraic spaces, so this is Stacks 06FP at that property, transported across the equivalence of
> conditions (1) and (2) of Stacks 06FM. Local finite presentation is smooth local on the
> source-and-target by **Stacks 06FC** and stable under composition by **Stacks 03XQ**.

```lean
theorem isLocallyOfFinitePresentation_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsLocallyOfFinitePresentation B S hS f)
    (hg : IsLocallyOfFinitePresentation B S hS g) :
    IsLocallyOfFinitePresentation B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean#L162). The attribute's comment: “finite presentation”.

> **Stacks 06Q3**, the global assertion. The composite of two 1-morphisms of algebraic stacks
> over `S` of finite presentation is of finite presentation.
>
> Being of finite presentation is being locally of finite presentation together with being
> quasi-compact and quasi-separated (Stacks 06Q2, part (2)); the first conjunct composes by the
> local assertion above, the second by **Stacks 050W** and the third by **Stacks 050K**.

```lean
theorem isFinitePresentation_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsFinitePresentation B S hS f) (hg : IsFinitePresentation B S hS g) :
    IsFinitePresentation B S hS (f ≫ g)
```

## Tag 06Q4, a lemma

[Tag 06Q4](https://stacks.math.columbia.edu/tag/06Q4) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationBaseChangeAlgebraicStack.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationBaseChangeAlgebraicStack.lean#L101). The attribute's comment: “locally of finite presentation”.

> **Stacks 06Q4**, the local assertion. A base change of a 1-morphism of algebraic stacks over
> `S` which is locally of finite presentation is locally of finite presentation: if `P` is a 2-fibre
> product of the cospan `(g, f)` and `f` is locally of finite presentation, then the projection
> `P.fst` is locally of finite presentation.
>
> This is the base-change remark **Stacks 06FQ** at local finite presentation of morphisms of
> algebraic spaces, transported across the equivalence of conditions (1) and (2) of **Stacks 06FM**,
> since Stacks 06Q2 part (1) is the universal criterion where Stacks 06FQ concludes about the
> existential one. Local finite presentation is smooth local on the source-and-target by
> **Stacks 06FC** and stable under base change by **Stacks 03XR**.

```lean
theorem isLocallyOfFinitePresentation_baseChange
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    IsLocallyOfFinitePresentation B S hS P.fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationBaseChangeAlgebraicStack.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationBaseChangeAlgebraicStack.lean#L127). The attribute's comment: “finite presentation”.

> **Stacks 06Q4**, the global assertion. A base change of a 1-morphism of algebraic stacks over
> `S` of finite presentation is of finite presentation.
>
> Being of finite presentation is being locally of finite presentation together with being
> quasi-compact and quasi-separated (Stacks 06Q2, part (2)); the first conjunct base changes by the
> local assertion above, the second by **Stacks 050V** and the third by **Stacks 050F**.

```lean
theorem isFinitePresentation_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsFinitePresentation B S hS f) :
    IsFinitePresentation B S hS P.fst
```

## Tag 06Q5, a lemma

[Tag 06Q5](https://stacks.math.columbia.edu/tag/06Q5) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessPresentationToType.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessPresentationToType.lean#L38). The attribute's comment: “finite presentation implies finite type”.

> A 1-morphism of algebraic stacks over `S` of finite presentation is of finite type.

```lean
theorem isFiniteType_of_isFinitePresentation
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsFinitePresentation B S hS f) :
    IsFiniteType B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean#L69). The attribute's comment: “first assertion”.

> A 1-morphism of algebraic stacks over `S` which is locally of finite presentation is locally
> of finite type.

```lean
theorem isLocallyOfFiniteType_of_isLocallyOfFinitePresentation
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴}
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 0DQJ, a lemma

[Tag 0DQJ](https://stacks.math.columbia.edu/tag/0DQJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationNoetherian.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationNoetherian.lean#L120). The attribute's comment: “part (1)”. References: SGA 3 VIA (2.5.4), “more general”.

> **Stacks 0DQJ, part (1).** A 1-morphism of algebraic stacks over `S` which is locally of
> finite type and whose target is locally Noetherian is locally of finite presentation. Local
> Noetherianity of an algebraic stack over `S` is the smooth-scheme-atlas criterion of
> **Stacks 04YG** at `AlgebraicGeometry.IsLocallyNoetherian`.
>
> Local finite type is the universal smooth-diagram test of **Stacks 06FM**, so the equivalence of
> its conditions (1) and (2) gives a diagram of algebraic spaces over `f` with smooth vertical
> 1-morphisms, left vertical 1-morphism surjective on objects, and top horizontal morphism `h`
> locally of finite type. The right vertical 1-morphism is a smooth algebraic-space chart of the
> target, so its source is locally Noetherian by **Stacks 04YF**, and **Stacks 06G4** part (1)
> makes `h` locally of finite presentation; the same diagram read backwards across Stacks 06FM at
> local finite presentation is the conclusion.

```lean
theorem isLocallyOfFinitePresentation_of_isLocallyOfFiniteType
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hY : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationNoetherian.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationNoetherian.lean#L166). The attribute's comment: “part (2)”.

> **Stacks 0DQJ, part (2).** A 1-morphism of algebraic stacks over `S` which is of finite type
> and quasi-separated and whose target is locally Noetherian is of finite presentation.
>
> Being of finite presentation is being locally of finite presentation, quasi-compact and
> quasi-separated (**Stacks 06Q2** part (2)) and being of finite type is being locally of finite
> type together with quasi-compactness (**Stacks 06FS** part (2)), so only the first conjunct has
> content and that is part (1).

```lean
theorem isFinitePresentation_of_isFiniteType
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hY : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴)
    (hf : IsFiniteType B S hS f)
    (hqs : Stack.AlgebraicStacks.IsQuasiSeparated B S hS f) :
    IsFinitePresentation B S hS f
```

## Tag 06Q6, a lemma

[Tag 06Q6](https://stacks.math.columbia.edu/tag/06Q6) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCancellation.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCancellation.lean#L269).

> Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over `S`. If `f ≫ g` is
> locally of finite presentation and `g` is locally of finite type, then `f` is locally of finite
> presentation.

```lean
theorem isLocallyOfFinitePresentation_of_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 0CMG, a lemma

[Tag 0CMG](https://stacks.math.columbia.edu/tag/0CMG) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalFinitePresentation.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalFinitePresentation.lean#L138). The attribute's comment: “locally of finite presentation”.

> **Stacks 0CMG, first assertion.** The relative diagonal of a 1-morphism of algebraic stacks
> over `S` which is locally of finite type is locally of finite presentation.
>
> The first projection of the 2-fibre product undoes the diagonal, is a base change of `f` and is
> therefore locally of finite type by Stacks 06FU, so Stacks 06Q6 cancels it against the identity
> of `𝒳`.

```lean
theorem isLocallyOfFinitePresentation_relativeDiagonal
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFinitePresentation B S hS (relativeDiagonal B S hS f)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinitePresentation_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalFinitePresentation.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalFinitePresentation.lean#L159). The attribute's comment: “finite presentation”.

> **Stacks 0CMG, second assertion.** The relative diagonal of a quasi-separated 1-morphism of
> algebraic stacks over `S` which is locally of finite type is of finite presentation.
>
> Local finite presentation is the first assertion; quasi-compactness of the diagonal is part (2)
> of Stacks 04Z0 read off quasi-separatedness of `f`; and quasi-separatedness of the diagonal is
> Section 04XB quasi-compactness of the second diagonal, which is part (2) of Stacks 04YZ at the
> same hypothesis, together with Section 04XB quasi-separatedness of the second diagonal, which is
> unconditional by part (4) of Stacks 04YQ and Stacks 03KK.

```lean
theorem isFinitePresentation_relativeDiagonal
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsLocallyOfFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    IsFinitePresentation B S hS (relativeDiagonal B S hS f)
```

## Tag 06Q7, a lemma

[Tag 06Q7](https://stacks.math.columbia.edu/tag/06Q7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFiniteness.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFiniteness.lean#L128).

> **Stacks 06Q7.** An open immersion of algebraic stacks over `S` is locally of finite
> presentation.
>
> By Stacks 04YL the 1-morphism is representable by algebraic spaces and every algebraic space
> representing a base change of it along a scheme-valued point of the target has open immersion
> structural morphism, hence by Stacks 06CN has structural morphism locally of finite
> presentation. That is the relative property of Stacks 03YK at local finite presentation of
> morphisms of algebraic spaces, which Stacks 06FM equates with the universal smooth-diagram test
> defining local finite presentation of the 1-morphism.

```lean
theorem isLocallyOfFinitePresentation_of_isOpenImmersion
    (f : 𝒳 ⟶ 𝒴) (hf : IsOpenImmersion B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 0CPP, a lemma

[Tag 0CPP](https://stacks.math.columbia.edu/tag/0CPP) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_fppfCoverStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyFppfCoverGeneral.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyFppfCoverGeneral.lean#L134).

> **Stacks 0CPP.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under base change and local on the target for the fppf precoverage, let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over `S` representable by algebraic spaces, and let `g : 𝒵 ⟶ 𝒴` be
> surjective, flat and locally of finite presentation. Then `f` has the relative property `P` of
> Stacks 03YK if and only if the projection to `𝒵` of a 2-fibre product of the cospan `(g, f)` has
> it.
>
> Unlike **Stacks 06TY** the cover `g` is not assumed representable by algebraic spaces.

```lean
theorem hasRelativeProperty_iff_of_fppfCoverStack
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, u} B S hS)]
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hSurj : IsSurjective B S hS g)
    (hFlat : AlgebraicStacks.IsFlat B S hS g)
    (hLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (Q : Bicategory.TwoCommSq g f)
    (hQ : Bicategory.IsTwoFibreProduct Q) :
    HasRelativeProperty B S hS P f.hom hf ↔
      ∃ hfst : IsRepresentableByAlgebraicSpaces B S hS Q.fst.hom.hom,
        HasRelativeProperty B S hS P Q.fst.hom hfst
```

## Tag 0DN6, a lemma

[Tag 0DN6](https://stacks.math.columbia.edu/tag/0DN6) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasProperty_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FppfDescentProperty.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FppfDescentProperty.lean#L248).

> Let `P` be smooth local on the source-and-target, with fppf local restriction to algebraic
> spaces, and let `g : 𝒵 ⟶ 𝒴` be surjective, flat and locally of finite presentation. If the base
> change `𝒵 ×_𝒴 𝒳 ⟶ 𝒵` of `f : 𝒳 ⟶ 𝒴` along `g` has `P`, then `f` has `P`.

```lean
theorem hasProperty_of_baseChange
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : Space.IsSmoothLocalOnSourceAndTarget B S hS P)
    [hlocal : (spaceProperty B S hS P).IsLocalAtTarget
      (Space.Topology.fppf.precoverage.{u, v} B S hS)]
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hgsurj : IsSurjective B S hS g)
    (hgflat : AlgebraicStacks.IsFlat B S hS g)
    (hglfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hbase : HasPropertyOnSomeSmoothDiagram B S hS P
      (twoFibreProductSquareAlgebraicStacks B S hS g f).fst.hom) :
    HasPropertyOnSomeSmoothDiagram B S hS P f.hom
```

## Tag 06Q8, a lemma

[Tag 06Q8](https://stacks.math.columbia.edu/tag/06Q8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationFppfDescent.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationFppfDescent.lean#L64).

> **Stacks 06Q8.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : 𝒵 ⟶ 𝒴` be surjective, flat and locally of finite presentation. If the base change
> `𝒵 ×_𝒴 𝒳 ⟶ 𝒵` of `f` along `g` is locally of finite presentation, then so is `f`.

```lean
theorem isLocallyOfFinitePresentation_of_baseChange
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hgs : Stack.IsSurjective B S hS g)
    (hgflat : IsFlat B S hS g)
    (hglfp : IsLocallyOfFinitePresentation B S hS g)
    (hbase : IsLocallyOfFinitePresentation B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 06Q9, a lemma

[Tag 06Q9](https://stacks.math.columbia.edu/tag/06Q9) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFinitePresentation_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationDescentComposition.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FinitePresentationDescentComposition.lean#L294).

> **Stacks 06Q9.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over
> `S`. If `f ≫ g` is locally of finite presentation and `f` is surjective, flat and locally of
> finite presentation, then `g` is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_of_comp_of_fppf
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hfsurj : Stack.IsSurjective B S hS f)
    (hfflat : IsFlat B S hS f)
    (hflfp : IsLocallyOfFinitePresentation B S hS f) :
    IsLocallyOfFinitePresentation B S hS g
```

## Tag 06QA, a lemma

[Tag 06QA](https://stacks.math.columbia.edu/tag/06QA) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_fppfCovering_fibre_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveFlatFppfLocalSections.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveFlatFppfLocalSections.lean#L332).

> **Stacks 06QA.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` which is
> surjective, flat and locally of finite presentation. Then for every object `U` of the big fppf
> site of `S` and every object `y` of the fibre of `𝒴` over `U` there is an fppf covering of `U`
> such that over every member of it `y` is isomorphic to the image of an object of `𝒳`.
>
> The covering is a covering sieve of the big fppf topology of `S`, and the isomorphism over a
> member `k : V ⟶ U` is a morphism `f(x) ⟶ y` lying over `k`, which in a category fibred in
> groupoids is exactly an isomorphism `f(x) ≅ y|_V` of the fibre over `V`. The covering produced is
> a one-member one; see
> `AlgebraicGeometry.Stack.exists_scheme_lift_of_isSurjective_isFlat_isLfp`.

```lean
theorem exists_fppfCovering_fibre_lift
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hsurj : IsSurjective B S hS f)
    (hflat : AlgebraicStacks.IsFlat B S hS f)
    (hlfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f) :
    ∀ (U : BigFppfOver B S hS) (y : 𝒴.val.val.p.Fiber U),
      ∃ R ∈ BigFppfOver.topology B S hS U,
        ∀ ⦃V : BigFppfOver B S hS⦄ ⦃k : V ⟶ U⦄, R.arrows k →
          ∃ (x : 𝒳.val.val.obj) (α : (CatFiberedInGroupoids.homFunctor f.hom).obj x ⟶ y.1),
            𝒴.val.val.p.IsHomLift k α
```

## Tag 07AN, a lemma

[Tag 07AN](https://stacks.math.columbia.edu/tag/07AN) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_fppfCovering_family_fibre_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/JointlySurjectiveFlatFppfLocalSections.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/JointlySurjectiveFlatFppfLocalSections.lean#L275). The attribute's comment: “the covering family and the index map”.

> **Stacks 07AN.** Let `f j : 𝒳 j ⟶ 𝒴`, `j ∈ J`, be a family of 1-morphisms of algebraic stacks
> over `S` which are each flat and locally of finite presentation and which are jointly surjective,
> that is `|𝒴| = ⋃ j, |f j|(|𝒳 j|)`. Then for every object `U` of the big fppf site of `S` and every
> object `y` of the fibre of `𝒴` over `U` there are an fppf covering `{U i → U}_{i ∈ I}` of `U`, a
> map `a : I → J` and, for every `i`, an object of `𝒳 (a i)` over `U i` whose image is isomorphic to
> the restriction of `y` to `U i`.
>
> The covering is given as a family of morphisms `m i : W i ⟶ U.left` of the underlying category of
> the site which are flat, locally of finite presentation and jointly surjective on the underlying
> schemes — which is what an fppf covering of `U` is. The isomorphism over a member is rendered as a
> morphism from the image of the object to `y` lying over that member, which in a category fibred in
> groupoids is exactly an isomorphism in the fibre.

```lean
theorem exists_fppfCovering_family_fibre_lift {J : Type v}
    {𝒳 : J → AlgebraicStacks.{u, w} B S hS} {𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒳 j ⟶ 𝒴)
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒴)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (U : BigFppfOver B S hS) (y : 𝒴.val.val.p.Fiber U) :
    ∃ (I : Type (u + 1)) (W : I → B.Schemes) (m : ∀ i, W i ⟶ U.left) (a : I → J),
      (∀ i, Flat (B.inclusion.map (m i))) ∧
        (∀ i, LocallyOfFinitePresentation (B.inclusion.map (m i))) ∧
          (∀ x : (B.inclusion.obj U.left), ∃ i, x ∈ Set.range (B.inclusion.map (m i))) ∧
            ∀ i, ∃ (x : (𝒳 (a i)).val.val.obj)
              (α : (CatFiberedInGroupoids.homFunctor (f (a i)).hom).obj x ⟶ y.1),
              𝒴.val.val.p.IsHomLift
                (Over.homMk (m i) rfl :
                  (Over.mk (m i ≫ U.hom) : BigFppfOver B S hS) ⟶ U) α
```

**`AlgebraicGeometry.Stack.exists_fppfCovering_fibre_lift_of_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/JointlySurjectiveFlatFppfLocalSections.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/JointlySurjectiveFlatFppfLocalSections.lean#L327). The attribute's comment: “the covering sieve form”.

> **Stacks 07AN, with the covering as a covering sieve.** Under the hypotheses of
> `AlgebraicGeometry.Stack.exists_fppfCovering_family_fibre_lift` there is a covering sieve of `U`
> for the big fppf topology of `S` such that over every arrow of it the object `y` is isomorphic to
> the image of an object of `𝒳 j` for some `j`.
>
> The index `j` is produced per arrow of the sieve rather than by a map out of the index set of a
> covering family, since a sieve carries no family; see
> `AlgebraicGeometry.Stack.exists_fppfCovering_family_fibre_lift` for the family form.

```lean
theorem exists_fppfCovering_fibre_lift_of_family {J : Type v}
    {𝒳 : J → AlgebraicStacks.{u, w} B S hS} {𝒴 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒳 j ⟶ 𝒴)
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒴)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (U : BigFppfOver B S hS) (y : 𝒴.val.val.p.Fiber U) :
    ∃ R ∈ BigFppfOver.topology B S hS U,
      ∀ ⦃V : BigFppfOver B S hS⦄ ⦃k : V ⟶ U⦄, R.arrows k →
        ∃ (j : J) (x : (𝒳 j).val.val.obj)
          (α : (CatFiberedInGroupoids.homFunctor (f j).hom).obj x ⟶ y.1),
          𝒴.val.val.p.IsHomLift k α
```

## Tag 06R7, a lemma

[Tag 06R7](https://stacks.math.columbia.edu/tag/06R7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isOpenMap_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatOpenPointsAlgebraicStack.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatOpenPointsAlgebraicStack.lean#L100).

> **Stacks 06R7.** A flat 1-morphism of algebraic stacks over `S` which is locally of finite
> presentation induces an open map on the topological spaces of points of Stacks 04XG and
> Stacks 04XL.

```lean
theorem isOpenMap_pointsMap {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hflat : IsFlat B S hS f) (hlfp : IsLocallyOfFinitePresentation B S hS f) :
    @IsOpenMap _ _ (Stack.pointTopology B S hS 𝒳.val) (Stack.pointTopology B S hS 𝒴.val)
      (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom)
```

## Tag 0DQK, a lemma

[Tag 0DQK](https://stacks.math.columbia.edu/tag/0DQK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactMorphism_of_isQuasiCompactMorphism_fst_of_stack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactFppfDescent.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasiCompactFppfDescent.lean#L107).

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : 𝒵 ⟶ 𝒴` be a surjective, flat, locally finitely presented 1-morphism of algebraic stacks.
> If the base change `𝒵 ×_𝒴 𝒳 ⟶ 𝒵` of `f` along `g` is quasi-compact, then `f` is
> quasi-compact.

```lean
theorem isQuasiCompactMorphism_of_isQuasiCompactMorphism_fst_of_stack
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (hgsurj : IsSurjective B S hS g)
    (hgflat : AlgebraicStacks.IsFlat B S hS g)
    (hglfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hbase : IsQuasiCompactMorphism B S hS P.fst) :
    IsQuasiCompactMorphism B S hS f
```

## Tag 0CPQ, a lemma

[Tag 0CPQ](https://stacks.math.columbia.edu/tag/0CPQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSeparated_of_isSeparated_comp_of_universallyInjective_of_isSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SeparationUniversallyInjectiveCoverCorrected.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SeparationUniversallyInjectiveCoverCorrected.lean#L196). The attribute's comment: “corrected form; the statement as written is false, see Stacks.Examples.not\_forall\_isSeparated\_of\_isSeparated\_comp\_of\_universallyInjective. The added assumption is that the relative diagonal of g is separated, which is strictly weaker than g separated and holds whenever g is representable by algebraic spaces; the counterexample violates exactly it”.

> **Stacks 0CPQ, corrected: `g` with separated diagonal.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be
> 1-morphisms of algebraic stacks over `S`. If `f` is surjective, flat, locally of finite
> presentation and universally injective, if `f ≫ g` is separated, and if the relative diagonal
> `Δ_g : 𝒴 ⟶ 𝒴 ×_𝒵 𝒴` is separated in the sense of Properties of Stacks, Section 04XB, then `g`
> is separated.
>
> The added hypothesis is on `g`, not on `f`, and it is strictly weaker than the conclusion, which
> asks `Δ_g` to be proper. It is exactly what the published statement is missing: the comparison
> 1-morphism `i : 𝒳 ×_𝒴 𝒳 ⟶ 𝒳 ×_𝒵 𝒳` is a base change of `Δ_g` (Stacks 050H), so it is separated,
> and then part (3) of Stacks 050M cancels it out of the proper `Δ_{f ≫ g} = Δ_f ≫ i`, making `Δ_f`
> proper, in particular universally closed; the published route through Stacks 0CPN, Stacks 08AJ
> and Stacks 0CPP then goes through
> (`AlgebraicGeometry.Stack.AlgebraicStacks`
> `.isSeparated_of_isSeparated_comp_of_universallyInjective_of_universallyClosed_relativeDiagonal`).
> Without it the statement fails, the obstruction being separatedness of `i`:
> `Stacks.Examples.not_forall_isSeparated_of_isSeparated_comp_of_universallyInjective`. It holds
> whenever `g` is representable by algebraic spaces,
> `AlgebraicGeometry.Stack.AlgebraicStacks`
> `.isSeparated_of_isSeparated_comp_of_universallyInjective_of_isRepresentableByAlgebraicSpaces`.

```lean
theorem isSeparated_of_isSeparated_comp_of_universallyInjective_of_isSeparated_diagonal
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfSurj : Stack.IsSurjective B S hS f)
    (hfFlat : IsFlat B S hS f)
    (hfLfp : IsLocallyOfFinitePresentation B S hS f)
    (hfUI : Stack.UniversallyInjective B S hS f)
    (hh : IsSeparated B S hS (f ≫ g))
    (hΔg : Stack.IsSeparated.{u, u, u + 1} B S hS
      (Stack.relativeDiagonal.{u, u, u + 1} B S hS 𝒴.val 𝒵.val g.hom)) :
    IsSeparated B S hS g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.27, Tag 06Q1](https://stacks.math.columbia.edu/tag/06Q1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
