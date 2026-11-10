---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representable_universallyInjective_iff, AlgebraicGeometry.Stack.UniversallyInjective, AlgebraicGeometry.Stack.universallyInjective_baseChange, AlgebraicGeometry.Stack.universallyInjective_comp, AlgebraicGeometry.Stack.universallyInjective_iff_isSurjective_relativeDiagonal, AlgebraicGeometry.Stack.isSurjective_relativeDiagonal_of_liftsTwoArrowsAtGeometricPoints, AlgebraicGeometry.Stack.universallyInjective_of_liftsTwoArrowsAtGeometricPoints, AlgebraicGeometry.Stack.liftsTwoArrowsAtGeometricPoints_of_isSurjective_relativeDiagonal
statement: formalized
proof: formalized
---

# 101.14 Universally injective morphisms

Section 101.14 of the Stacks Project, [Tag 0CI0](https://stacks.math.columbia.edu/tag/0CI0). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CI1, a lemma

[Tag 0CI1](https://stacks.math.columbia.edu/tag/0CI1) in the Stacks Project.

**`AlgebraicGeometry.Stack.representable_universallyInjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveCriterion.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveCriterion.lean#L62).

> **Stacks 0CI1.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by
> algebraic spaces is universally injective in the relative sense of Tag 04XB — every algebraic
> space representing a base change of `f` along a scheme-valued point of `𝒴` has universally
> injective structural morphism — exactly when, for every algebraic stack `𝒵` over `𝒴` and every
> 2-fibre product of the cospan, the map `|𝒵 ×_𝒴 𝒳| → |𝒵|` is injective.

```lean
theorem representable_universallyInjective_iff
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
        Space.UniversallyInjective B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨T, hT⟩)).hom) ↔
      UniversallyInjective B S hS f
```

## Tag 0CI2, a definition

[Tag 0CI2](https://stacks.math.columbia.edu/tag/0CI2) in the Stacks Project.

**`AlgebraicGeometry.Stack.UniversallyInjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjective.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjective.lean#L58).

> **Stacks 0CI2.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is *universally
> injective* if for every 1-morphism `g : 𝒵 ⟶ 𝒴` of algebraic stacks over `S` and every 2-fibre
> product of `(g, f)` the map `|𝒵 ×_𝒴 𝒳| → |𝒵|` induced by the projection to `𝒵` is injective.

```lean
abbrev UniversallyInjective {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CI3, a lemma

[Tag 0CI3](https://stacks.math.columbia.edu/tag/0CI3) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveBaseChange.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveBaseChange.lean#L49). References: EGA IV (11.9.14), “base change stability”.

> **Stacks 0CI3.** The base change of a universally injective 1-morphism `f : 𝒳 ⟶ 𝒴` of
> algebraic stacks over `S` along any `g : 𝒵 ⟶ 𝒴` is universally injective: in a 2-fibre-product
> square over `(g, f)`, the projection to `𝒵` is universally injective.

```lean
theorem universallyInjective_baseChange {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴) (hf : UniversallyInjective B S hS f)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P) :
    UniversallyInjective B S hS P.fst
```

## Tag 0CI4, a lemma

[Tag 0CI4](https://stacks.math.columbia.edu/tag/0CI4) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveComp.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveComp.lean#L106).

> **Stacks 0CI4.** The composite of a pair of universally injective 1-morphisms of algebraic
> stacks over `S` is universally injective.

```lean
theorem universallyInjective_comp {𝒳 𝒴 𝒵 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : UniversallyInjective B S hS f)
    (hg : UniversallyInjective B S hS g) :
    UniversallyInjective B S hS (f ≫ g)
```

## Tag 0CPN, a lemma

[Tag 0CPN](https://stacks.math.columbia.edu/tag/0CPN) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_iff_isSurjective_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveDiagonal.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveDiagonal.lean#L221). The attribute's comment: “parts (1) and (2)”.

> **Stacks 0CPN, parts (1) and (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is
> universally injective if and only if its relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` is surjective.

```lean
theorem universallyInjective_iff_isSurjective_relativeDiagonal (f : 𝒳 ⟶ 𝒴) :
    UniversallyInjective B S hS f ↔
      IsSurjective B S hS (AlgebraicStacks.relativeDiagonal B S hS f)
```

**`AlgebraicGeometry.Stack.isSurjective_relativeDiagonal_of_liftsTwoArrowsAtGeometricPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean#L174). The attribute's comment: “part (3) implies part (2)”.

> **Stacks 0CPN, the implication (3) `⟹` (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> over `S` which lifts 2-arrows at geometric points has surjective relative diagonal
> `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳`.
>
> A point of `|𝒳 ×_𝒴 𝒳|` is represented over an algebraically closed field, where it is a triple
> `(x₁, x₂, β)`; condition (3) writes `β` as `f(α)`, and then `(𝟙, α)` is an arrow from
> `Δ_f(x₁) = (x₁, x₁, id)` to that triple, so the two represent the same point.

```lean
theorem isSurjective_relativeDiagonal_of_liftsTwoArrowsAtGeometricPoints (f : 𝒳 ⟶ 𝒴)
    (h₃ : LiftsTwoArrowsAtGeometricPoints B S hS f) :
    IsSurjective B S hS (AlgebraicStacks.relativeDiagonal B S hS f)
```

**`AlgebraicGeometry.Stack.universallyInjective_of_liftsTwoArrowsAtGeometricPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean#L209). The attribute's comment: “part (3) implies part (1)”.

> **Stacks 0CPN, the implication (3) `⟹` (1).** A 1-morphism of algebraic stacks over `S`
> which lifts 2-arrows at geometric points is universally injective: its relative diagonal is
> surjective, and parts (1) and (2) of Stacks 0CPN
> (`AlgebraicGeometry.Stack.universallyInjective_iff_isSurjective_relativeDiagonal`) conclude.

```lean
theorem universallyInjective_of_liftsTwoArrowsAtGeometricPoints (f : 𝒳 ⟶ 𝒴)
    (h₃ : LiftsTwoArrowsAtGeometricPoints B S hS f) :
    UniversallyInjective B S hS f
```

**`AlgebraicGeometry.Stack.liftsTwoArrowsAtGeometricPoints_of_isSurjective_relativeDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean#L251). The attribute's comment: “part (2) implies part (3)”.

> **Stacks 0CPN, the implication (2) `⟹` (3).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> over `S` whose relative diagonal `Δ_f : 𝒳 ⟶ 𝒳 ×_𝒴 𝒳` is surjective lifts 2-arrows at geometric
> points: for every algebraically closed field `k`, all `x₁, x₂ : Spec k ⟶ 𝒳` and every 2-arrow
> `β : f ∘ x₁ ⟶ f ∘ x₂` there is a 2-arrow `α : x₁ ⟶ x₂` with `β = id_f ⋆ α`.
>
> The triple `t = (x₁, x₂, β)` is a point of `𝒳 ×_𝒴 𝒳` over `Spec k`, and the fibre
> `T = 𝒳 ×_{Δ_f, 𝒳 ×_𝒴 𝒳, t} Spec k` is an algebraic space locally of finite type over `Spec k` by
> **Stacks 04XS**. Surjectivity of `Δ_f` makes `T` nonempty, and since `k` is algebraically closed
> `T` then has a `k`-point
> (`AlgebraicGeometry.Space.nonempty_obj_base_of_nonempty_points`), which is exactly the
> 2-arrow `α`.

```lean
theorem liftsTwoArrowsAtGeometricPoints_of_isSurjective_relativeDiagonal (f : 𝒳 ⟶ 𝒴)
    (h₂ : IsSurjective B S hS (AlgebraicStacks.relativeDiagonal B S hS f)) :
    LiftsTwoArrowsAtGeometricPoints B S hS f
```

**`AlgebraicGeometry.Stack.universallyInjective_iff_liftsTwoArrowsAtGeometricPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveGeometricTwoArrows.lean#L307). The attribute's comment: “parts (1) and (3)”.

> **Stacks 0CPN, parts (1) and (3).** A 1-morphism of algebraic stacks over `S` is universally
> injective if and only if it lifts 2-arrows at geometric points.

```lean
theorem universallyInjective_iff_liftsTwoArrowsAtGeometricPoints (f : 𝒳 ⟶ 𝒴) :
    UniversallyInjective B S hS f ↔ LiftsTwoArrowsAtGeometricPoints B S hS f
```

## Tag 0DTM, a lemma

[Tag 0DTM](https://stacks.math.columbia.edu/tag/0DTM) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_fiber_lift_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveAlgebraicallyClosedPoint.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveAlgebraicallyClosedPoint.lean#L685).

> Let `f : 𝒳 ⟶ 𝒴` be a universally injective 1-morphism of algebraic stacks and `y : Spec k ⟶ 𝒴`
> a morphism with `k` algebraically closed. If `y` is in the image of `|𝒳| → |𝒴|`, then there is
> `x : Spec k ⟶ 𝒳` with `y = f ∘ x`: an object `x` of the fibre of `𝒳` over the base of `y` whose
> image under `f` is isomorphic to `y` in that fibre.

```lean
theorem exists_fiber_lift_of_universallyInjective
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicGeometry.Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hf : AlgebraicGeometry.Stack.UniversallyInjective B S hS f)
    (y : AlgebraicGeometry.Stack.FieldValuedPoint B S hS 𝒴.val.val)
    [IsAlgClosed y.carrier]
    (hy : AlgebraicGeometry.Stack.pointClass B S hS 𝒴.val.val
      𝒴.val.isFiberedInGroupoids y ∈
        Set.range (AlgebraicGeometry.Stack.pointsMap B S hS 𝒳.val.val
          𝒳.val.isFiberedInGroupoids 𝒴.val.isFiberedInGroupoids f.hom.hom)) :
    ∃ x : 𝒳.val.val.p.Fiber y.base,
      Nonempty
        (((Functor.fiberMap 𝒳.val.val.p 𝒴.val.val.p
          f.hom.hom.toFunctor f.hom.hom.w y.base).obj x) ≅
          (⟨y.obj, y.over⟩ : 𝒴.val.val.p.Fiber y.base))
```

## Tag 0DTN, a lemma

[Tag 0DTN](https://stacks.math.columbia.edu/tag/0DTN) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_iff_affineBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveAffineLocal.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveAffineLocal.lean#L112).

> **Stacks 0DTN.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` is universally
> injective if and only if for every affine scheme `U` of the big fppf site over `S` and every
> 1-morphism from the algebraic stack it represents to `𝒴`, the base change of `f` is universally
> injective.
>
> The base change is an arbitrary 2-fibre product of the cospan, as in **Stacks 0CI2** itself, so
> neither side depends on a chosen model.

```lean
theorem universallyInjective_iff_affineBaseChange (f : 𝒳 ⟶ 𝒴) :
    UniversallyInjective B S hS f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : schemeStack.{u, w} B S hS U ⟶ 𝒴) (P : Bicategory.TwoCommSq g f),
          Bicategory.IsTwoFibreProduct P → UniversallyInjective B S hS P.fst
```

## Tag 0DTP, a lemma

[Tag 0DTP](https://stacks.math.columbia.edu/tag/0DTP) in the Stacks Project.

**`AlgebraicGeometry.Stack.universallyInjective_of_fppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveDescent.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyInjectiveDescent.lean#L143). References: EGA IV (11.9.14), “fppf descent clause”.

> **Stacks 0DTP.** Universal injectivity of a 1-morphism of algebraic stacks over `S` can be
> checked after base change along a surjective, flat, locally finitely presented 1-morphism from
> the stack of an algebraic space onto its target.
>
> Only surjectivity of the cover is used; see
> `AlgebraicGeometry.Stack.universallyInjective_of_isSurjective_baseChange`.

```lean
theorem universallyInjective_of_fppfCover
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hW : IsAlgebraicSpace B S hS W)
    (g : algebraicSpaceStack.{u, w} B S hS W hW ⟶ 𝒴)
    (hgSurj : IsSurjective B S hS g)
    (_hgFlat : AlgebraicStacks.IsFlat B S hS g)
    (_hgLfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS g)
    (hgf : UniversallyInjective B S hS
      (AlgebraicStacks.twoFibreProductSquare B S hS g f).fst) :
    UniversallyInjective B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.14, Tag 0CI0](https://stacks.math.columbia.edu/tag/0CI0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
