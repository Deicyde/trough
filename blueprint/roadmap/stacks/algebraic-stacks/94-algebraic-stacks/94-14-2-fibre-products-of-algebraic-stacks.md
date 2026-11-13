---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.isTwoFibreProduct_productSquare, AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct, AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct_of_locallySmall, AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProductSquare, AlgebraicGeometry.Stack.isTwoFibreProduct_twoFibreProductSquareAlgebraicStacks, AlgebraicGeometry.Stack.AlgebraicStacks.isFinalTwoCommSq_twoFibreProductSquare
statement: formalized
proof: formalized
---

# 94.14 2-Fibre products of algebraic stacks

Section 94.14 of the Stacks Project, [Tag 04TD](https://stacks.math.columbia.edu/tag/04TD). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04TE, a lemma

[Tag 04TE](https://stacks.math.columbia.edu/tag/04TE) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isTwoFibreProduct_productSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackEquivalence.lean#L289).

> The product `𝒳 ×_{(Sch/S)_fppf} 𝒴` of two algebraic stacks over `S` is a product in the
> 2-category of algebraic stacks over `S`: the canonical square
> `AlgebraicGeometry.Stack.AlgebraicStacks.productSquare` over the cospan of structure 1-morphisms
> to the final object is a 2-fibre product in that 2-category.

```lean
noncomputable def isTwoFibreProduct_productSquare (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS) :
    Bicategory.IsTwoFibreProduct (productSquare B S hS 𝒳 𝒴)
```

## Tag 04TF, a lemma

[Tag 04TF](https://stacks.math.columbia.edu/tag/04TF) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductAlgebraicStack.lean, line 1332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductAlgebraicStack.lean#L1332).

> **Stacks 04TF.** Let `𝒵` be a stack in groupoids over the big fppf site of `S` whose
> diagonal is representable by algebraic spaces, let `𝒳` and `𝒴` be algebraic stacks over `S` and
> let `f : 𝒳 ⟶ 𝒵`, `g : 𝒴 ⟶ 𝒵` be 1-morphisms of stacks in groupoids. Then the 2-fibre product
> `𝒳 ×_{f, 𝒵, g} 𝒴` is an algebraic stack over `S`.
>
> The hypothesis on `𝒵` is the stack clause of `AlgebraicGeometry.Stack.IsAlgebraicStack`, i.e.
> "stack in groupoids" in both renderings of Stacks 02ZJ; the sieve-indexed conjunct is what Stacks
> 04TF asks for, and it is what Stacks 026G
> (`CategoryTheory.TwoFibreProductOver.isStack_structureFunctor`) consumes.

```lean
theorem isAlgebraicStack_twoFibreProduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (f : 𝒳 ⥤ᵇ 𝒵) (g : 𝒴 ⥤ᵇ 𝒵)
    (h𝒵 : 𝒵.p.IsStack (BigFppfOver.topology B S hS) ∧
      𝒵.p.IsStackInGroupoids.{w} (BigFppfOver.topology B S hS))
    (hdiag : HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk 𝒵 h𝒵.2.isFiberedInGroupoids))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴) :
    IsAlgebraicStack.{u, w} B S hS
      (BasedCategory.ofFunctor
        (TwoFibreProductOver.structureFunctor 𝒳.p 𝒴.p 𝒵.p f.toFunctor g.toFunctor))
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct_of_locallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductAlgebraicStackLocallySmall.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductAlgebraicStackLocallySmall.lean#L206). The attribute's comment: “the two algebraic factors with locally small morphisms in any universe”.

> Let `𝒵` be a stack in groupoids over the big fppf site of `S` whose diagonal is representable
> by algebraic spaces, let `𝒳` and `𝒴` be algebraic stacks over `S` whose hom-sets are `u`-small, in
> any morphism universes, and let `f : 𝒳 ⟶ 𝒵`, `g : 𝒴 ⟶ 𝒵` be 1-morphisms. Then the 2-fibre product
> `𝒳 ×_{f, 𝒵, g} 𝒴` is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_twoFibreProduct_of_locallySmall
    (𝒳 : BasedCategory.{v₁, u + 1} (BigFppfOver B S hS))
    (𝒴 : BasedCategory.{v₂, u + 1} (BigFppfOver B S hS))
    (𝒵 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    [LocallySmall.{u} 𝒳.obj] [LocallySmall.{u} 𝒴.obj]
    (f : 𝒳 ⥤ᵇ 𝒵) (g : 𝒴 ⥤ᵇ 𝒵)
    (h𝒵 : 𝒵.p.IsStack (BigFppfOver.topology B S hS) ∧
      𝒵.p.IsStackInGroupoids.{w} (BigFppfOver.topology B S hS))
    (hdiag : HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk 𝒵 h𝒵.2.isFiberedInGroupoids))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳)
    (h𝒴 : IsAlgebraicStack.{u, w} B S hS 𝒴) :
    IsAlgebraicStack.{u, w} B S hS
      (BasedCategory.ofFunctor
        (TwoFibreProductOver.structureFunctor 𝒳.p 𝒴.p 𝒵.p f.toFunctor g.toFunctor))
```

## Tag 04T2, a lemma

[Tag 04T2](https://stacks.math.columbia.edu/tag/04T2) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProductSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean#L67).

> **Stacks 04T2, first assertion.** The apex of the canonical 2-commutative square of a
> cospan of algebraic stacks over `S` is an algebraic stack. This is
> `AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct`, Stacks 04TF, with base the common
> target, whose stack and diagonal hypotheses there are two of the clauses of its algebraicity.

```lean
theorem isAlgebraicStack_twoFibreProductSquare
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) :
    IsAlgebraicStack.{u, w} B S hS
      (CatFiberedInGroupoids.twoFibreProductSquare.{u, u, u + 1, u + 1} f.hom g.hom).pt.val
```

**`AlgebraicGeometry.Stack.isTwoFibreProduct_twoFibreProductSquareAlgebraicStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSquareAlgebraicStack.lean#L112). The attribute's comment: “2-categorical universal property”.

> **Stacks 04T2, second assertion: the 2-categorical universal property.** The canonical
> square of a cospan of algebraic stacks over `S` is a 2-fibre product in the 2-category of
> algebraic stacks, and not merely in the ambient 2-category of categories fibred in groupoids:
> the square underlying it is the canonical one there, which is a 2-fibre product
> unconditionally, and the 2-category of algebraic stacks is a full sub-2-category.
>
> This is also the **right square of Stacks 06PQ**, whose left square is
> `AlgebraicGeometry.Stack.exists_cartesianRelativeInertiaSquare`: the right square of the
> diagram there is the defining base-change square of the cospan `(π, f)`.

```lean
noncomputable def isTwoFibreProduct_twoFibreProductSquareAlgebraicStacks
    {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵) :
    Bicategory.IsTwoFibreProduct (twoFibreProductSquareAlgebraicStacks B S hS f g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isFinalTwoCommSq_twoFibreProductSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductUniversalProperty.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductUniversalProperty.lean#L166). The attribute's comment: “the 2-categorical universal property”.

> **Stacks 04T2, the 2-categorical universal property.** The canonical 2-fibre product square
> `AlgebraicGeometry.Stack.AlgebraicStacks.twoFibreProductSquare` of a cospan of algebraic stacks
> over `S` is a 2-fibre product in the sense of Stacks 003Q *in the 2-category of algebraic stacks
> over* `(Sch/S)_fppf`, not merely in the ambient 2-category of categories fibred in groupoids: a
> final object of the 2-category of 2-commutative diagrams over the cospan, any two 1-morphisms into
> it being isomorphic by a unique 2-morphism.
>
> That its apex is an algebraic stack is Stacks 04TF; see
> `AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct`.

```lean
noncomputable def isFinalTwoCommSq_twoFibreProductSquare (g : 𝒵 ⟶ 𝒴) (f : 𝒳 ⟶ 𝒴) :
    Bicategory.IsFinalTwoCommSq (twoFibreProductSquare B S hS g f)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.isAlgebraicStack_twoFibreProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductAlgebraicStack.lean#L1332), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductUniversalProperty.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductUniversalProperty.lean#L82) (StacksFrontier): “the 2-fibre product is an algebraic stack”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.14, Tag 04TD](https://stacks.math.columbia.edu/tag/04TD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
