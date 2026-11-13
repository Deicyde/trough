---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsFormallySmoothOnObjects, AlgebraicGeometry.Stack.InfinitesimalLiftingDiagram, AlgebraicGeometry.Stack.isFormallySmoothOnObjects_iff_nonempty_dottedArrow, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_baseChange, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_comp, AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_iff_formallySmooth_terminalFrom, AlgebraicGeometry.Stack.exists_dottedArrow_of_isSmooth_of_isFirstOrderThickening, AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_iff_isLocallyOfFinitePresentation_and_isFormallySmoothOnObjects
statement: formalized
proof: formalized
---

# 106.8 Formally smooth morphisms

Section 106.8 of the Stacks Project, [Tag 0DNV](https://stacks.math.columbia.edu/tag/0DNV). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DNW, a definition

[Tag 0DNW](https://stacks.math.columbia.edu/tag/0DNW) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsFormallySmoothOnObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothOnObjects.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothOnObjects.lean#L53). The attribute's comment: “formal smoothness of a morphism of algebraic stacks is formal smoothness on”.

> The first-order lifting condition for a 1-morphism of categories fibred in groupoids, with
> the comparison square required to commute: the restriction along a first-order thickening of
> affine objects is the chosen pullback `CategoryTheory.Functor.pullbackFiber`.

```lean
def IsFormallySmoothOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (BigFppfOver B S hS)) (p : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0DNX, an equation

[Tag 0DNX](https://stacks.math.columbia.edu/tag/0DNX) in the Stacks Project.

**`AlgebraicGeometry.Stack.InfinitesimalLiftingDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InfinitesimalLifting.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/InfinitesimalLifting.lean#L52).

> The solid part of a 2-commutative infinitesimal lifting diagram for a
> 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S`: a first-order thickening of affine
> objects of the big fppf site of `S`, a point of `𝒳` over the smaller one, a point of `𝒴` over
> the larger one, and a 2-morphism witnessing that the square 2-commutes.

```lean
structure InfinitesimalLiftingDiagram
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS)
    (f : 𝒳 ⟶ 𝒴)
```

## Tag 0DNY, a lemma

[Tag 0DNY](https://stacks.math.columbia.edu/tag/0DNY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFormallySmoothOnObjects_iff_nonempty_dottedArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothDottedArrows.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FormallySmoothDottedArrows.lean#L638).

> **Stacks 0DNY.** A 1-morphism of algebraic stacks over `S` is formally smooth exactly when
> every infinitesimal lifting diagram for it — the solid diagram 0DNX, i.e. a first-order
> thickening of affine objects of the site together with a point of the source over the smaller
> one, a point of the target over the larger one and a 2-morphism witnessing 2-commutativity —
> admits a dotted arrow, i.e. the category of dotted arrows of Stacks 0H18 for that square is
> nonempty.

```lean
theorem isFormallySmoothOnObjects_iff_nonempty_dottedArrow
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    IsFormallySmoothOnObjects B S hS 𝒳.1 𝒴.1 f.hom ↔
      ∀ d : InfinitesimalLiftingDiagram B S hS 𝒳 𝒴 f,
        Nonempty (DottedArrow d.x d.j f.hom d.y d.γ)
```

## Tag 0H1I, a lemma

[Tag 0H1I](https://stacks.math.columbia.edu/tag/0H1I) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L199). The attribute's comment: “base change of a formally smooth morphism of algebraic stacks is formally smooth”.

> **Stacks 06D1.** Formal smoothness on objects is stable under base change.

```lean
theorem isFormallySmoothOnObjects_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒵 ⟶ 𝒴)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p) :
    Stack.IsFormallySmoothOnObjects B S hS
      (twoFibreProduct B S hS 𝒳 𝒴 𝒵 p q) 𝒵
      (twoFibreProductSnd B S hS 𝒳 𝒴 𝒵 p q)
```

## Tag 0H1J, a lemma

[Tag 0H1J](https://stacks.math.columbia.edu/tag/0H1J) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothOnObjects.lean#L413). The attribute's comment: “the case of algebraic stacks, formally smooth being formally smooth on objects”.

> **Stacks 06D2.** A composite of morphisms formally smooth on objects is formally smooth on
> objects.

```lean
theorem isFormallySmoothOnObjects_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒴 ⟶ 𝒵)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p)
    (hq : Stack.IsFormallySmoothOnObjects B S hS 𝒴 𝒵 q) :
    Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒵 (p ≫ q)
```

## Tag 0H1K, a lemma

[Tag 0H1K](https://stacks.math.columbia.edu/tag/0H1K) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_iff_formallySmooth_terminalFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothBaseChange.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Criteria/FormallySmoothBaseChange.lean#L224).

> **Stacks 0H1K.** A 1-morphism of categories fibred in groupoids over the big fppf category
> of `S` which is representable by algebraic spaces is formally smooth on objects exactly when,
> for every scheme-valued point `U` of the target, every algebraic space representing the base
> change of it along that point is formally smooth over `U`.
>
> This is Stacks 06D3,
> `AlgebraicGeometry.BigFppfOver.isFormallySmoothOnObjects_iff_isRelativelyFormallySmooth`, with
> the structural morphism of the representing space read over `U` rather than over `S`, which is
> `AlgebraicGeometry.BigFppfOver.isRelativelyFormallySmooth_iff_formallySmooth_terminalFrom`.

```lean
theorem isFormallySmoothOnObjects_iff_formallySmooth_terminalFrom (p : 𝒳 ⟶ 𝒴)
    (hp : Stack.IsRepresentableByAlgebraicSpaces B S hS p.hom) :
    Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p ↔
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
        (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (_hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
          Nonempty (StacksRepresentableCFG.EquivalenceOver
            (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
              (CatFiberedInGroupoids.homFunctor p))
            (presheafOfCategories (F ⋙ typeToCat)).p) →
          Space.FormallySmooth (terminal.from F)
```

## Tag 0DNZ, a lemma

[Tag 0DNZ](https://stacks.math.columbia.edu/tag/0DNZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_dottedArrow_of_isSmooth_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GroupoidLift/StackLift.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/GroupoidLift/StackLift.lean#L204).

> **Stacks 0DNZ.** Let `T ⟶ T'` be a first-order thickening of affine schemes, `𝒳` an algebraic
> stack whose structure morphism `f : 𝒳 ⟶ T'` is smooth, and `x : T ⟶ 𝒳` a morphism over `T'`
> (the 2-morphism `γ : j ⟶ x ≫ f`, with `j : T ⟶ T'` the morphism of represented categories
> induced by the thickening). Then there is a morphism `x' : T' ⟶ 𝒳` over `T'` with `x'|_T ≅ x`:
> a dotted arrow for the square `(x, j, f, 𝟙)`.

```lean
theorem exists_dottedArrow_of_isSmooth_of_isFirstOrderThickening
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (T T' : BigFppfOver B S hS)
    (hT : IsAffine ((BigFppfOver.toScheme B S hS).obj T))
    (hT' : IsAffine ((BigFppfOver.toScheme B S hS).obj T'))
    (i : T ⟶ T')
    (hi : Stacks.Thickenings.IsFirstOrderThickening (B.inclusion.map i.left))
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (f : 𝒳 ⟶ schemeFibredCategory B S hS T')
    (hf : HasPropertyOnSomeSmoothDiagram B S hS
      (fun {X Y} (g : X ⟶ Y) => Space.IsSmooth B S hS g) f)
    (j : schemeFibredCategory B S hS T ⟶ schemeFibredCategory B S hS T')
    (hj : j.hom.toFunctor = Over.map i)
    (x : schemeFibredCategory B S hS T ⟶ 𝒳)
    (γ : (j ≫ 𝟙 _) ⟶ (x ≫ f)) :
    Nonempty (DottedArrow x j f (𝟙 _) γ)
```

## Tag 0DP0, a lemma

[Tag 0DP0](https://stacks.math.columbia.edu/tag/0DP0) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSmooth_iff_isLocallyOfFinitePresentation_and_isFormallySmoothOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothFormallySmooth.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothFormallySmooth.lean#L343). References: EGA 0 (19.0.1), “more general”.

> **Stacks 0DP0 (infinitesimal lifting criterion).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks over `S` is smooth if and only if it is locally of finite presentation and formally
> smooth, formal smoothness of a 1-morphism of algebraic stacks being formal smoothness on
> objects (Stacks 0DNW).

```lean
theorem AlgebraicStacks.isSmooth_iff_isLocallyOfFinitePresentation_and_isFormallySmoothOnObjects
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) :
    AlgebraicStacks.IsSmooth B S hS f ↔
      AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f ∧
        IsFormallySmoothOnObjects B S hS 𝒳.1 𝒴.1 f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.8, Tag 0DNV](https://stacks.math.columbia.edu/tag/0DNV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
