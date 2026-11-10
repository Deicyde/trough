---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyOfFiniteType, AlgebraicGeometry.Stack.AlgebraicStacks.IsFiniteType, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherian_of_isLocallyOfFiniteType
statement: formalized
proof: formalized
---

# 101.17 Morphisms of finite type

Section 101.17 of the Stacks Project, [Tag 06FR](https://stacks.math.columbia.edu/tag/06FR). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06FS, a definition

[Tag 06FS](https://stacks.math.columbia.edu/tag/06FS) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocallyOfFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean#L56). The attribute's comment: “part (1): locally of finite type”.

> A 1-morphism `f` of algebraic stacks over `S` is *locally of finite type* when every
> 2-commutative square of algebraic spaces over `f` whose two vertical 1-morphisms are smooth and
> whose every comparison 1-morphism to a 2-fibre product is smooth has its top horizontal morphism
> locally of finite type.

```lean
abbrev IsLocallyOfFiniteType {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeAlgebraicStack.lean#L63). The attribute's comment: “part (2): finite type”.

> A 1-morphism of algebraic stacks over `S` is *of finite type* when it is locally of finite
> type and quasi-compact.

```lean
abbrev IsFiniteType {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 06FT, a lemma

[Tag 06FT](https://stacks.math.columbia.edu/tag/06FT) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean#L110). The attribute's comment: “locally of finite type”.

> **Stacks 06FT**, the local assertion. The composite of two 1-morphisms of algebraic stacks
> over `S` which are locally of finite type is locally of finite type.
>
> Stacks 06FS part (1) is condition (1) of Stacks 06FM at local finite type of morphisms of
> algebraic spaces, so this is Stacks 06FP at that property, transported across the equivalence of
> conditions (1) and (2) of Stacks 06FM. Local finite type is smooth local on the
> source-and-target by **Stacks 06FC** and stable under composition by **Stacks 03XG**.

```lean
theorem isLocallyOfFiniteType_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessComposition.lean#L127). The attribute's comment: “finite type”.

> **Stacks 06FT**, the global assertion. The composite of two finite type 1-morphisms of
> algebraic stacks over `S` is of finite type.
>
> Being of finite type is being locally of finite type together with being quasi-compact
> (Stacks 06FS, part (2)); the first conjunct composes by the local assertion above and the second
> by **Stacks 050W**.

```lean
theorem isFiniteType_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsFiniteType B S hS f) (hg : IsFiniteType B S hS g) :
    IsFiniteType B S hS (f ≫ g)
```

## Tag 06FU, a lemma

[Tag 06FU](https://stacks.math.columbia.edu/tag/06FU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessBaseChange.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessBaseChange.lean#L89). The attribute's comment: “locally of finite type”.

> **Stacks 06FU**, the local assertion. A base change of a 1-morphism of algebraic stacks over
> `S` which is locally of finite type is locally of finite type: if `P` is a 2-fibre product of the
> cospan `(g, f)` and `f` is locally of finite type, then the projection `P.fst` is locally of
> finite type.
>
> This is the base-change remark **Stacks 06FQ** at local finite type of morphisms of algebraic
> spaces, transported across the equivalence of conditions (1) and (2) of **Stacks 06FM**, since
> Stacks 06FS part (1) is the universal criterion where Stacks 06FQ concludes about the existential
> one. Local finite type is smooth local on the source-and-target by **Stacks 06FC** and stable
> under base change by **Stacks 03XH**.

```lean
theorem isLocallyOfFiniteType_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS P.fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFiniteType_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FinitenessBaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FinitenessBaseChange.lean#L117). The attribute's comment: “finite type”.

> **Stacks 06FU**, the global assertion. A base change of a finite type 1-morphism of algebraic
> stacks over `S` is of finite type.
>
> Being of finite type is being locally of finite type together with being quasi-compact
> (Stacks 06FS, part (2)); the first conjunct base changes by the local assertion above and the
> second by **Stacks 050V**.

```lean
theorem isFiniteType_baseChange {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴)
    (P : Bicategory.TwoCommSq g f)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsFiniteType B S hS f) :
    IsFiniteType B S hS P.fst
```

## Tag 06FV, a lemma

[Tag 06FV](https://stacks.math.columbia.edu/tag/06FV) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFiniteness.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionFiniteness.lean#L99).

> **Stacks 06FV.** An immersion of algebraic stacks over `S` is locally of finite type.
>
> By Stacks 04YL the 1-morphism is representable by algebraic spaces and every algebraic space
> representing a base change of it along a scheme-valued point of the target has immersion
> structural morphism, hence by Stacks 06ED has structural morphism locally of finite type. That
> is the relative property of Stacks 03YK at local finite type of morphisms of algebraic spaces,
> which Stacks 06FM equates with the universal smooth-diagram test defining local finite type of
> the 1-morphism.

```lean
theorem isLocallyOfFiniteType_of_isImmersion
    (f : 𝒳 ⟶ 𝒴) (hf : IsImmersion B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 06R6, a lemma

[Tag 06R6](https://stacks.math.columbia.edu/tag/06R6) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyNoetherian_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/NoetherianAlgebraicStack.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/NoetherianAlgebraicStack.lean#L310).

> **Stacks 06R6.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`. If `f` is
> locally of finite type and `𝒴` is locally Noetherian, then `𝒳` is locally Noetherian. Local
> Noetherianity of an algebraic stack over `S` is the smooth-scheme-atlas criterion of
> **Stacks 04YG** at `AlgebraicGeometry.IsLocallyNoetherian`.
>
> The source argues with scheme charts; here the whole argument runs on algebraic-space charts,
> which is what the chapter's vocabulary already supports, and the scheme criterion is reached at
> the two ends by **Stacks 04YF**. A smooth diagram over `f` is a pair of algebraic-space charts
> `a : U ⟶ 𝒳` and `b : V ⟶ 𝒴` whose top horizontal morphism `h : U ⟶ V` is locally of finite
> type, with `a` moreover surjective on objects; `V` is then a smooth algebraic-space chart of
> `𝒴`, so it has the étale-local property of **Stacks 03E6** at local Noetherianity, and
> **Stacks 04ZK** carries that along `h` to `U`. Since `a` is a smooth surjective algebraic-space
> atlas of `𝒳`, that is the third criterion of Stacks 04YF for `𝒳`.

```lean
theorem isLocallyNoetherian_of_isLocallyOfFiniteType
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hf : IsLocallyOfFiniteType B S hS f)
    (hY : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒴) :
    HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} => IsLocallyNoetherian T) 𝒳
```

## Tag 06U7, a lemma

[Tag 06U7](https://stacks.math.columbia.edu/tag/06U7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_baseChange_algebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeFppfBaseChange.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeFppfBaseChange.lean#L123).

> **Stacks 06U7.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : W ⟶ 𝒴` be surjective, flat and locally of finite presentation, where `W` is an algebraic
> space over `S`. If the base change `W ×_𝒴 𝒳 ⟶ W` of `f` along `g` is locally of finite type,
> then so is `f`.

```lean
theorem isLocallyOfFiniteType_of_baseChange_algebraicSpace
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hW : IsAlgebraicSpace B S hS W)
    (g : Stack.algebraicSpaceStack.{u, w} B S hS W hW ⟶ 𝒴)
    (hgsurj : Stack.IsSurjective B S hS g)
    (hgflat : IsFlat B S hS g)
    (hglfp : IsLocallyOfFinitePresentation B S hS g)
    (hbase : IsLocallyOfFiniteType B S hS
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS f g).snd) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 06U8, a lemma

[Tag 06U8](https://stacks.math.columbia.edu/tag/06U8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_comp_of_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeFppfDescent.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypeFppfDescent.lean#L250).

> Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over
> `S`. If `f ≫ g` is locally of finite type and `f` is representable by algebraic spaces,
> surjective, flat and locally of finite presentation, then `g` is locally of finite type.

```lean
theorem isLocallyOfFiniteType_of_comp_of_fppf
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g))
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hfsurj : IsSurjective B S hS f)
    (hfflat : IsFlat B S hS f)
    (hflfp : IsLocallyOfFinitePresentation B S hS f) :
    IsLocallyOfFiniteType B S hS g
```

## Tag 06U9, a lemma

[Tag 06U9](https://stacks.math.columbia.edu/tag/06U9) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCancellation.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalMorphismCancellation.lean#L292).

> Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` be 1-morphisms of algebraic stacks over `S`. If `f ≫ g` is
> locally of finite type, then so is `f`.

```lean
theorem isLocallyOfFiniteType_of_comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.17, Tag 06FR](https://stacks.math.columbia.edu/tag/06FR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
