---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representable_universallyClosed_iff_closedMap_baseChange, AlgebraicGeometry.Stack.AlgebraicStacks.IsClosed, AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyClosed, AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_baseChange_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_comp, AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_comp, AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_tfae
statement: formalized
proof: formalized
---

# 101.13 Universally closed morphisms

Section 101.13 of the Stacks Project, [Tag 0511](https://stacks.math.columbia.edu/tag/0511). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0512, a lemma

[Tag 0512](https://stacks.math.columbia.edu/tag/0512) in the Stacks Project.

**`AlgebraicGeometry.Stack.representable_universallyClosed_iff_closedMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedCriterion.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedCriterion.lean#L551).

> **Stacks 0512.** A 1-morphism of algebraic stacks over `S` which is representable by
> algebraic spaces is universally closed — the relative property of Tag 04XB at universal
> closedness of morphisms of algebraic spaces — exactly when, for every algebraic stack `𝒵` over
> `𝒴`, the first projection of the canonical 2-fibre product of Tag 04T2 is a closed map on the
> points of Tag 04XL.

```lean
theorem representable_universallyClosed_iff_closedMap_baseChange
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    UniversallyClosed B S hS f.hom ↔
      ∀ (𝒵 : AlgebraicStacks.{u, w} B S hS) (g : 𝒵 ⟶ 𝒴),
        let P := twoFibreProductSquareAlgebraicStacks B S hS g f
        @IsClosedMap
          (points B S hS P.pt.val.val (Classical.choose P.pt.property))
          (points B S hS 𝒵.val.val (Classical.choose 𝒵.property))
          (pointTopology B S hS P.pt.val)
          (pointTopology B S hS 𝒵.val)
          (pointsMap B S hS P.pt.val.val
            (Classical.choose P.pt.property) (Classical.choose 𝒵.property)
            P.fst.hom.hom)
```

## Tag 0513, a definition

[Tag 0513](https://stacks.math.columbia.edu/tag/0513) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsClosed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean#L89). The attribute's comment: “closed”.

> **Stacks 0513, part (1).** A 1-morphism of algebraic stacks over `S` *is closed* when the
> map `|𝒳| → |𝒴|` it induces on the topological spaces of points of Stacks 04XG and 04XL is a
> closed map.

```lean
abbrev IsClosed {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.UniversallyClosed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ProperAlgebraicStack.lean#L99). The attribute's comment: “universally closed”.

> **Stacks 0513, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is
> universally closed* when, for every 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S`, the
> base change `𝒵 ×_{g, 𝒴, f} 𝒳 ⟶ 𝒵` of `f` by `g` is closed in the sense of
> `AlgebraicGeometry.Stack.AlgebraicStacks.IsClosed`.

```lean
abbrev UniversallyClosed {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0514, a lemma

[Tag 0514](https://stacks.math.columbia.edu/tag/0514) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_baseChange_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedBaseChange.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedBaseChange.lean#L95).

> **Stacks 0514.** Universal closedness is stable under base change: let `f : 𝒳 ⟶ 𝒴` be a
> universally closed 1-morphism of algebraic stacks over `S` and let `R` be a 2-fibre product
> square of the cospan `(g, f)` for some `g : 𝒴' ⟶ 𝒴`. Then the base change `R.fst : R.pt ⟶ 𝒴'`
> of `f` along `g` is universally closed.
>
> The square is arbitrary, so this applies to any square a consumer has already exhibited as a
> 2-fibre product rather than only to the canonical one of Stacks 04T2.

```lean
theorem universallyClosed_baseChange_of_isTwoFibreProduct
    {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴}
    (R : Bicategory.TwoCommSq g f) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : UniversallyClosed B S hS f) :
    UniversallyClosed B S hS R.fst
```

## Tag 0515, a lemma

[Tag 0515](https://stacks.math.columbia.edu/tag/0515) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedComposition.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedComposition.lean#L48). The attribute's comment: “closed”.

> The composite of two closed 1-morphisms of algebraic stacks over `S` is closed.

```lean
theorem isClosed_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsClosed B S hS f) (hg : IsClosed B S hS g) :
    IsClosed B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedComposition.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedComposition.lean#L62). The attribute's comment: “universally closed”.

> The composite of two universally closed 1-morphisms of algebraic stacks over `S` is
> universally closed.

```lean
theorem universallyClosed_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : UniversallyClosed B S hS f) (hg : UniversallyClosed B S hS g) :
    UniversallyClosed B S hS (f ≫ g)
```

## Tag 0CL3, a lemma

[Tag 0CL3](https://stacks.math.columbia.edu/tag/0CL3) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L477).

> **Stacks 0CL3.** For a 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` the following are
> equivalent: `f` is universally closed; every base change of `f` to a scheme of the site is closed
> on points; every base change of `f` to an affine scheme of the site is closed on points; and
> there is a smooth surjective 1-morphism from the algebraic stack of an algebraic space to `𝒴`
> along which the base change of `f` is universally closed.

```lean
theorem universallyClosed_tfae {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    List.TFAE
      [UniversallyClosed B S hS f,
        ∀ (U : BigFppfOver B S hS) (g : Stack.schemeStack.{u, w} B S hS U ⟶ 𝒴),
          IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst,
        ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
          ∀ (g : Stack.schemeStack.{u, w} B S hS U ⟶ 𝒴),
            IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst,
        ∃ (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
            (g : Stack.algebraicSpaceStack.{u, w} B S hS F hF ⟶ 𝒴),
          Stack.IsSurjective B S hS g ∧ IsSmooth B S hS g ∧
            UniversallyClosed B S hS
              (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.13, Tag 0511](https://stacks.math.columbia.edu/tag/0511)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
