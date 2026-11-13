---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAlgebraicSpace_prod, AlgebraicGeometry.AlgebraicSpaces.isLimitBinaryFanProduct, AlgebraicGeometry.isAlgebraicSpace_of_isPullback, AlgebraicGeometry.isAlgebraicSpace_pullback_of_representable_diagonal, AlgebraicGeometry.AlgebraicSpaces, AlgebraicGeometry.isAlgebraicSpace_pullback, AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct
statement: formalized
proof: formalized
---

# 65.7 Fibre products of algebraic spaces

Section 65.7 of the Stacks Project, [Tag 04T8](https://stacks.math.columbia.edu/tag/04T8). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02X0, a lemma

[Tag 02X0](https://stacks.math.columbia.edu/tag/02X0) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean#L111). The attribute's comment: “the product is an algebraic space”.

> The presheaf product of two algebraic spaces over `S` is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_prod (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) :
    IsAlgebraicSpace B S hS (F ⨯ G)
```

**`AlgebraicGeometry.AlgebraicSpaces.isLimitBinaryFanProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean#L143). The attribute's comment: “the universal property”.

> The presheaf product of two algebraic spaces over `S`, with the two presheaf projections, is
> a product in the category of algebraic spaces over `S`.

```lean
noncomputable def isLimitBinaryFanProduct (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F G : AlgebraicSpaces B S hS) :
    IsLimit (BinaryFan.mk
      (ObjectProperty.homMk (prod.fst : F.obj ⨯ G.obj ⟶ F.obj) : product B S hS F G ⟶ F)
      (ObjectProperty.homMk (prod.snd : F.obj ⨯ G.obj ⟶ G.obj) :
        product B S hS F G ⟶ G))
```

## Tag 04T9, a lemma

[Tag 04T9](https://stacks.math.columbia.edu/tag/04T9) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicSpace_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreProduct.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreProduct.lean#L129).

> Let `F` and `G` be algebraic spaces over `S`, let `H` be an fppf sheaf on the big fppf site of
> `S` whose diagonal is representable, and let `f : F ⟶ H` and `g : G ⟶ H`. Then a fibre product
> `Z` of `f` and `g` is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_of_isPullback
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hHsheaf : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H)
    (hHdiag : yoneda.relativelyRepresentable (diag H))
    {f : F ⟶ H} {g : G ⟶ H} {p : Z ⟶ F} {q : Z ⟶ G} (hZ : IsPullback p q f g) :
    IsAlgebraicSpace B S hS Z
```

**`AlgebraicGeometry.isAlgebraicSpace_pullback_of_representable_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreProduct.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreProduct.lean#L165). The attribute's comment: “the chosen presheaf fibre product”.

> The chosen presheaf fibre product of two algebraic spaces over an fppf sheaf with
> representable diagonal is an algebraic space.

```lean
theorem isAlgebraicSpace_pullback_of_representable_diagonal
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ H) (g : G ⟶ H)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : Presheaf.IsSheaf (BigFppfOver.topology B S hS) H)
    (hdiag : yoneda.relativelyRepresentable (diag H)) :
    IsAlgebraicSpace B S hS (pullback f g)
```

## Tag 02X2, a lemma

[Tag 02X2](https://stacks.math.columbia.edu/tag/02X2) in the Stacks Project.

**`AlgebraicGeometry.AlgebraicSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L265). The attribute's comment: “the category of algebraic spaces over the base”.

> **Stacks 02X2.** The category of algebraic spaces over a scheme `S` of a big fppf site:
> the full subcategory of presheaves on the big fppf site of `S` whose objects are algebraic
> spaces over `S`.

```lean
abbrev AlgebraicSpaces (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.isAlgebraicSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L350). The attribute's comment: “algebraicity of the fibre product”.

> **Stacks 02X2.** The presheaf fibre product of two algebraic spaces over an algebraic
> space is an algebraic space.

```lean
theorem isAlgebraicSpace_pullback {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ H) (g : G ⟶ H) (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H) :
    IsAlgebraicSpace B S hS (pullback f g)
```

**`AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L403). The attribute's comment: “universal property among algebraic spaces”.

> **Stacks 02X2.** The presheaf fibre product of two algebraic spaces is a fibre product
> in the category of algebraic spaces over the base.

```lean
theorem isPullback_fiberProduct {F G H : AlgebraicSpaces B S hS} (f : F ⟶ H) (g : G ⟶ H) :
    IsPullback (ObjectProperty.homMk (pullback.fst f.hom g.hom) : fiberProduct B S hS f g ⟶ F)
      (ObjectProperty.homMk (pullback.snd f.hom g.hom) : fiberProduct B S hS f g ⟶ G) f g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.7, Tag 04T8](https://stacks.math.columbia.edu/tag/04T8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
