---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsLocalCompleteIntersection, AlgebraicGeometry.Stack.AlgebraicStacks.IsLocalCompleteIntersection.comp, AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_baseChange_of_isFlat, AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_of_isLocalCompleteIntersection_comp_of_isSmooth
statement: formalized
proof: formalized
---

# 101.44 Local complete intersection morphisms

Section 101.44 of the Stacks Project, [Tag 0CJ2](https://stacks.math.columbia.edu/tag/0CJ2). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CJ3, a definition

[Tag 0CJ3](https://stacks.math.columbia.edu/tag/0CJ3) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocalCompleteIntersection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionMorphism.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionMorphism.lean#L71).

> **Stacks 0CJ3.** A 1-morphism of algebraic stacks over `S` is a *local complete intersection
> morphism*, or *Koszul*, when it passes the universal smooth-diagram test of Stacks 06FM at the
> local complete intersection property of morphisms of algebraic spaces: every 2-commutative square
> of algebraic spaces over `f` whose two vertical 1-morphisms are smooth and whose every comparison
> 1-morphism to a 2-fibre product is smooth has its top horizontal morphism a local complete
> intersection morphism.

```lean
abbrev IsLocalCompleteIntersection {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    Prop
```

## Tag 0CJ4, a lemma

[Tag 0CJ4](https://stacks.math.columbia.edu/tag/0CJ4) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsLocalCompleteIntersection.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionComp.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionComp.lean#L59). The attribute's comment: “composition of local complete intersection 1-morphisms of algebraic stacks”.

> **Stacks 0CJ4.** The composition of local complete intersection 1-morphisms of algebraic
> stacks over `S` is a local complete intersection 1-morphism: if `f : 𝒳 ⟶ 𝒴` and `g : 𝒴 ⟶ 𝒵` are
> Koszul, so is `f ≫ g`.
>
> This is the general composition remark **Stacks 06FP** at the Koszul property of morphisms of
> algebraic spaces, which is stable under composition by **Stacks 06C8**, as in
> `AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_comp`; the smooth locality
> on the source-and-target that argument consumes is
> `AlgebraicGeometry.Space.isLocalCompleteIntersection_isSmoothLocalOnSourceAndTarget`.

```lean
theorem IsLocalCompleteIntersection.comp
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒴 ⟶ 𝒵}
    (hf : IsLocalCompleteIntersection B S hS f)
    (hg : IsLocalCompleteIntersection B S hS g) :
    IsLocalCompleteIntersection B S hS (f ≫ g)
```

## Tag 0CJ5, a lemma

[Tag 0CJ5](https://stacks.math.columbia.edu/tag/0CJ5) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_baseChange_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionIsFlatBaseChange.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionIsFlatBaseChange.lean#L68). The attribute's comment: “registered form: flat base change of a local complete intersection 1-morphism of algebraic stacks, along any 2-fibre product of the cospan”.

> **Stacks 0CJ5.** A flat base change of a local complete intersection 1-morphism of algebraic
> stacks over `S` is a local complete intersection 1-morphism: if `Q` is a 2-fibre product of the
> cospan `(g, f)` of algebraic stacks, `g` is flat and `f` is Koszul, then the projection
> `Q.fst` to the source of `g` is Koszul.
>
> This is the flat base-change argument
> `AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_baseChange`, with the smooth
> source-and-target locality of the Koszul property of morphisms of algebraic spaces (Stacks 06FC
> at that property) supplied by
> `AlgebraicGeometry.Space.isLocalCompleteIntersection_isSmoothLocalOnSourceAndTarget`. The
> statement has exactly the source's data: the cospan leg `g` is flat in the sense of Stacks 06PW
> (`IsFlat`), `f` is a local complete intersection 1-morphism in the sense of Stacks 0CJ3
> (`IsLocalCompleteIntersection`), and `Q` is any 2-fibre product of the cospan.

```lean
theorem isLocalCompleteIntersection_baseChange_of_isFlat
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (hg : IsFlat B S hS g)
    (Q : Bicategory.TwoCommSq g f)
    (hQ : Bicategory.IsTwoFibreProduct Q)
    (hf : IsLocalCompleteIntersection B S hS f) :
    IsLocalCompleteIntersection B S hS Q.fst
```

## Tag 0CJ6, a lemma

[Tag 0CJ6](https://stacks.math.columbia.edu/tag/0CJ6) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocalCompleteIntersection_of_isLocalCompleteIntersection_comp_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionSmoothCancellation.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LocalCompleteIntersectionSmoothCancellation.lean#L167).

> **Stacks 0CJ6.** Let `f : 𝒳 ⟶ 𝒴`, `g : 𝒴 ⟶ 𝒵` and `h : 𝒳 ⟶ 𝒵` be 1-morphisms of algebraic
> stacks over `S` forming a 2-commutative triangle, `f ≫ g ≅ h`. If `g` is smooth and `h` is a
> local complete intersection morphism, then `f` is a local complete intersection morphism.
>
> Both the hypothesis on `h` and the conclusion are the universal smooth-diagram criterion of
> Stacks 06FM (Definition Stacks 0CJ3), and they are moved to the existential one by smooth
> locality on the source-and-target of the Koszul property of morphisms of algebraic spaces,
> `AlgebraicGeometry.Space.isLocalCompleteIntersection_isSmoothLocalOnSourceAndTarget`. The
> cancellation is `AlgebraicGeometry.Stack.hasPropertyOnSomeSmoothDiagram_of_comp_of_flatBaseChange`
> at the pair (Koszul, smooth), whose space-level input is Stacks 0CHL,
> `AlgebraicGeometry.Space.isLocalCompleteIntersection_of_comp_of_isSmooth`, and which uses flat
> base change of the Koszul property (Stacks 06C7) and base change of smoothness (Stacks 03ZE).

```lean
theorem isLocalCompleteIntersection_of_isLocalCompleteIntersection_comp_of_isSmooth
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (h : 𝒳 ⟶ 𝒵) (e : f ≫ g ≅ h)
    (hg : IsSmooth B S hS g) (hh : IsLocalCompleteIntersection B S hS h) :
    IsLocalCompleteIntersection B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.44, Tag 0CJ2](https://stacks.math.columbia.edu/tag/0CJ2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
