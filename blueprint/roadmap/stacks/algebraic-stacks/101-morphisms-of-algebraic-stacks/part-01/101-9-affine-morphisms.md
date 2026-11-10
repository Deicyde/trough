---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.IsAffineHom, AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_and_isAffineHom_snd, AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_snd_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableMorphism_comp_isAffineHom, AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_of_comp_of_isAffineHom_relativeDiagonal
statement: formalized
proof: formalized
---

# 101.9 Affine morphisms

Section 101.9 of the Stacks Project, [Tag 0CHP](https://stacks.math.columbia.edu/tag/0CHP). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CHQ, a definition

[Tag 0CHQ](https://stacks.math.columbia.edu/tag/0CHQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsAffineHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphism.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphism.lean#L105).

> **Stacks 0CHQ.** A 1-morphism of algebraic stacks over `S` is *affine* when it is
> representable by algebraic spaces and is affine in the sense of Stacks 04XB.

```lean
abbrev IsAffineHom (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CHR, a lemma

[Tag 0CHR](https://stacks.math.columbia.edu/tag/0CHR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_and_isAffineHom_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismBaseChange.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismBaseChange.lean#L58).

> **Stacks 0CHR.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` and let
> `g : 𝒵 ⟶ 𝒴` be an affine 1-morphism of algebraic stacks, that is (Stacks 0CHQ) one which is
> representable by algebraic spaces and affine in the sense of Stacks 04XB. If `P` is a 2-fibre
> product of the cospan `(g, f)`, then the base change `P.snd : 𝒵 ×_𝒴 𝒳 ⟶ 𝒳` is an affine
> 1-morphism of algebraic stacks: it is representable by algebraic spaces, and it is affine in the
> sense of Stacks 04XB.

```lean
theorem isRepresentableByAlgebraicSpaces_and_isAffineHom_snd
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg_rep : IsRepresentableByAlgebraicSpaces B S hS g.hom.hom)
    (hg_aff : Stack.IsAffineHom B S hS g.hom) :
    IsRepresentableByAlgebraicSpaces B S hS P.snd.hom.hom ∧
      Stack.IsAffineHom B S hS P.snd.hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_snd_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismStability.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismStability.lean#L267).

> **Stacks 0CHR.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let
> `g : 𝒵 ⟶ 𝒴` be an affine 1-morphism of algebraic stacks, and let `P` be a 2-fibre product of the
> cospan `(g, f)`. Then the base change `P.snd : 𝒵 ×_𝒴 𝒳 ⟶ 𝒳` of `g` along `f` is affine.
>
> Both halves are base-change statements: representability by algebraic spaces is Stacks 0302 and
> affineness in the sense of Stacks 04XB is Stacks 045C. The square is arbitrary, so this applies
> to any square a consumer has already exhibited as a 2-fibre product rather than only to the
> canonical one of Stacks 04T2.

```lean
theorem isAffineHom_snd_of_isTwoFibreProduct
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsAffineHom B S hS g) :
    IsAffineHom B S hS P.snd
```

## Tag 0CHS, a lemma

[Tag 0CHS](https://stacks.math.columbia.edu/tag/0CHS) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableMorphism_comp_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismRepresentableComp.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismRepresentableComp.lean#L119). The attribute's comment: “with 0CHQ read literally: representable by schemes and affine in the sense of 04XB”.

> **Stacks 0CHS, for the definition of Stacks 0CHQ read literally.** Call a 1-morphism of
> algebraic stacks over `S` affine when it is representable (by schemes, Stacks 02Y7) and affine in
> the sense of Stacks 04XB. Then a composite of two affine 1-morphisms of algebraic stacks is
> affine: representability composes by Stacks 02ZS, and affineness in the sense of Stacks 04XB
> composes by `AlgebraicGeometry.Stack.isAffineHom_comp` (Stacks 045B with Stacks 03WH and the
> implication (4) ⇒ (2) of Stacks 03WG), which applies because a representable 1-morphism is
> representable by algebraic spaces.

```lean
theorem isRepresentableMorphism_comp_isAffineHom (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) ∧ Stack.IsAffineHom B S hS f.hom)
    (hg : Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒴.val.val.p 𝒵.val.val.p
        (CatFiberedInGroupoids.homFunctor g.hom) ∧ Stack.IsAffineHom B S hS g.hom) :
    Stacks.RepresentableMorphism.IsRepresentableMorphism 𝒳.val.val.p 𝒵.val.val.p
        (CatFiberedInGroupoids.homFunctor (f ≫ g).hom) ∧
      Stack.IsAffineHom B S hS (f ≫ g).hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismStability.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineMorphismStability.lean#L285).

> **Stacks 0CHS.** A composite of two affine 1-morphisms of algebraic stacks over `S` is
> affine: representability by algebraic spaces composes by Stacks 0301, and affineness in the sense
> of Stacks 04XB composes by Stacks 045B, whose two ingredients at affineness are Stacks 03WH and
> the implication (4) ⇒ (2) of Stacks 03WG.

```lean
theorem isAffineHom_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsAffineHom B S hS f) (hg : IsAffineHom B S hS g) :
    IsAffineHom B S hS (f ≫ g)
```

## Tag 0GQE, a lemma

[Tag 0GQE](https://stacks.math.columbia.edu/tag/0GQE) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isAffineHom_of_comp_of_isAffineHom_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AffineDiagonalPermanence.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AffineDiagonalPermanence.lean#L182).

> **Stacks 0GQE.** Let
>
> ```text
>   𝒳 ----f----> 𝒴
>     \         /
>      a       b
>       \     /
>        >  𝒵 <
> ```
>
> be a 2-commutative triangle of 1-morphisms of algebraic stacks over `S`, the commutativity being
> the 2-isomorphism `comm : a ≅ f ≫ b`. If `a` is affine and the relative diagonal `Δ_b` is affine
> in the sense of Properties of Stacks, Section 04XB, then `f` is affine.
>
> *Reading the statement.* The unqualified `IsAffineHom`, in the hypothesis `ha` on `a` and in the
> conclusion on `f`, elaborates to `AlgebraicGeometry.Stack.AlgebraicStacks.IsAffineHom`, the notion
> of an affine 1-morphism of algebraic stacks of **Stacks 0CHQ** (registered in
> `StacksFrontier.AlgebraicGeometry.Stacks.AffineMorphism`). It is by definition the conjunction
> `IsRepresentableByAlgebraicSpaces B S hS q.hom.hom ∧ Stack.IsAffineHom B S hS q.hom` for `q = a`
> and for `q = f`, so it includes representability by algebraic spaces: `a` is assumed, and `f` is
> concluded, to be representable by algebraic spaces and affine in the sense of Stacks 04XB, exactly
> as in the source. The 1-morphism `relativeDiagonalAlgebraicStacks B S hS b` is the relative
> diagonal `Δ_b : 𝒴 ⟶ 𝒴 ×_{b, 𝒵, b} 𝒴`, `y ↦ (y, y, id)`. The hypothesis `hΔ` on it is written
> with the qualified `Stack.IsAffineHom`, the condition of Stacks 04XB alone, without
> representability; it is weaker than the source's hypothesis that `Δ_b` is affine, and loses
> nothing, since `Δ_b` is representable by algebraic spaces unconditionally by Stacks 04XS part (1)
> (`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_relativeDiagonal_of_isAlgebraicStack`).
>
> This is the source's proof. The 1-morphism `f` is 2-isomorphic to `Γ_f ≫ pr₂`, where
> `Γ_f : 𝒳 ⟶ 𝒳 ×_𝒵 𝒴` is the graph of `f` over `𝒵` (Stacks 050I) and
> `pr₂ : 𝒳 ×_𝒵 𝒴 ⟶ 𝒴` is the second projection of the canonical 2-fibre product of the cospan
> `(a, b)`. The projection is a base change of `a`, hence affine by **Stacks 0CHR**; the graph is
> affine by `AlgebraicGeometry.Stack.isAffineHom_graph`, which carries the hypothesis on `Δ_b`
> along the base-change square of **Stacks 04Z1**; and **Stacks 0CHS** composes the two.

```lean
theorem isAffineHom_of_comp_of_isAffineHom_relativeDiagonal
    {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (a : 𝒳 ⟶ 𝒵) (b : 𝒴 ⟶ 𝒵) (comm : a ≅ f ≫ b)
    (ha : IsAffineHom B S hS a)
    (hΔ : Stack.IsAffineHom B S hS (relativeDiagonalAlgebraicStacks B S hS b).hom) :
    IsAffineHom B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.9, Tag 0CHP](https://stacks.math.columbia.edu/tag/0CHP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
