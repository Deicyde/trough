---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representable_universalHomeomorphism_iff, AlgebraicGeometry.Stack.UniversalHomeomorphism, AlgebraicGeometry.Stack.AlgebraicStacks.UniversalHomeomorphism, AlgebraicGeometry.Stack.universalHomeomorphism_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.universalHomeomorphism_comp, AlgebraicGeometry.Stack.universalHomeomorphism_of_fppfCover
statement: formalized
proof: formalized
---

# 101.15 Universal homeomorphisms

Section 101.15 of the Stacks Project, [Tag 0CI5](https://stacks.math.columbia.edu/tag/0CI5). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CI6, a lemma

[Tag 0CI6](https://stacks.math.columbia.edu/tag/0CI6) in the Stacks Project.

**`AlgebraicGeometry.Stack.representable_universalHomeomorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismCriterion.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismCriterion.lean#L58).

> **Stacks 0CI6.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by
> algebraic spaces is a universal homeomorphism in the relative sense of Tag 04XB — every algebraic
> space representing a base change of `f` along a scheme-valued point of `𝒴` has structural
> morphism a universal homeomorphism — exactly when, for every algebraic stack `𝒵` over `𝒴`, the
> map `|𝒵 ×_𝒴 𝒳| → |𝒵|` of topological spaces is a homeomorphism.

```lean
theorem representable_universalHomeomorphism_iff
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    (∀ (U : BigFppfOver B S hS) (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.val.obj)
        (_hy : y ⋙ 𝒴.val.val.p = Over.map U.hom)
        (T : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hT : IsAlgebraicSpace B U.left.1 U.left.2 T),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p 𝒴.val.val.p y
            (CatFiberedInGroupoids.homFunctor f.hom))
          (presheafOfCategories (T ⋙ typeToCat)).p) →
        Space.UniversalHomeomorphism B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨T, hT⟩)).hom) ↔
      AlgebraicStacks.UniversalHomeomorphism B S hS f
```

## Tag 0CI7, a definition

[Tag 0CI7](https://stacks.math.columbia.edu/tag/0CI7) in the Stacks Project.

**`AlgebraicGeometry.Stack.UniversalHomeomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphism.lean#L68).

> **Stacks 0CI7.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is a *universal
> homeomorphism* if for every 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S` and every
> 2-fibre product of `(g, f)` the map `|𝒵 ×_𝒴 𝒳| → |𝒵|` induced by the projection to `𝒵` is a
> homeomorphism.

```lean
abbrev UniversalHomeomorphism {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.UniversalHomeomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismAlgebraicStack.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismAlgebraicStack.lean#L136).

> **Stacks 0CI7.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is a *universal
> homeomorphism* when, for every 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S`, the base
> change `𝒵 ×_{g, 𝒴, f} 𝒳 ⟶ 𝒵` of `f` by `g` induces a homeomorphism `|𝒵 ×_𝒴 𝒳| → |𝒵|` on the
> points of Stacks 04XG for the topology of Stacks 04XL.
>
> For a 1-morphism representable by algebraic spaces this agrees with the relative notion of
> Stacks 04XB, by **Stacks 0CI6**.

```lean
abbrev UniversalHomeomorphism {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CI8, a lemma

[Tag 0CI8](https://stacks.math.columbia.edu/tag/0CI8) in the Stacks Project.

**`AlgebraicGeometry.Stack.universalHomeomorphism_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismBaseChange.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismBaseChange.lean#L40).

> The base change of a universal homeomorphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` along any
> `g : 𝒵 ⟶ 𝒴` is a universal homeomorphism: in a 2-fibre-product square over `(g, f)`, the projection
> to `𝒵` is a universal homeomorphism.

```lean
theorem universalHomeomorphism_baseChange {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴) (hf : UniversalHomeomorphism B S hS f)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P) :
    UniversalHomeomorphism B S hS P.fst
```

## Tag 0CI9, a lemma

[Tag 0CI9](https://stacks.math.columbia.edu/tag/0CI9) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universalHomeomorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismAlgebraicStack.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismAlgebraicStack.lean#L162).

> **Stacks 0CI9.** The composite of two universal homeomorphisms of algebraic stacks over `S`
> is a universal homeomorphism.
>
> A base change of `f ≫ g` along `k` is the outer rectangle of a base change of `g` along `k`
> followed by a base change of `f` along the resulting projection, by the pasting law for 2-fibre
> products; the two legs of that rectangle are homeomorphisms on points by hypothesis, so the
> rectangle's own first leg is one too, and that condition depends only on the cospan.

```lean
theorem universalHomeomorphism_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : UniversalHomeomorphism B S hS f) (hg : UniversalHomeomorphism B S hS g) :
    UniversalHomeomorphism B S hS (f ≫ g)
```

## Tag 0DTQ, a lemma

[Tag 0DTQ](https://stacks.math.columbia.edu/tag/0DTQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.universalHomeomorphism_of_fppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismDescent.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversalHomeomorphismDescent.lean#L126).

> **Stacks 0DTQ.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : 𝒲 ⟶ 𝒴` be a surjective, flat, locally finitely presented 1-morphism from the stack of an
> algebraic space. If the base change `𝒲 ×_𝒴 𝒳 ⟶ 𝒲` of `f` along `g` is a universal
> homeomorphism, then so is `f`.

```lean
theorem universalHomeomorphism_of_fppfCover {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hW : IsAlgebraicSpace B S hS W)
    (g : algebraicSpaceStack.{u, w} B S hS W hW ⟶ 𝒴)
    (hgSurj : IsSurjective B S hS g)
    (hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hgf : UniversalHomeomorphism B S hS
      (AlgebraicStacks.twoFibreProductSquare B S hS g f).fst) :
    UniversalHomeomorphism B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.15, Tag 0CI5](https://stacks.math.columbia.edu/tag/0CI5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
