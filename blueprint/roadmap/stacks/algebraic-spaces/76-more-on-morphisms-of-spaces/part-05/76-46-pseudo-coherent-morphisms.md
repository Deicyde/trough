---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsPseudoCoherent, AlgebraicGeometry.Space.IsPseudoCoherentAt, AlgebraicGeometry.Space.isPseudoCoherent_baseChange_of_isFlat, AlgebraicGeometry.Space.isPseudoCoherent_comp, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isPseudoCoherent, AlgebraicGeometry.Space.isPseudoCoherent_of_isFlat_of_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.isPseudoCoherent_of_comp, AlgebraicGeometry.Space.isPseudoCoherent_iff_isLocallyOfFiniteType
statement: formalized
proof: formalized
---

# 76.46 Pseudo-coherent morphisms

Section 76.46 of the Stacks Project, [Tag 06BQ](https://stacks.math.columbia.edu/tag/06BQ). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06BR, a definition

[Tag 06BR](https://stacks.math.columbia.edu/tag/06BR) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPseudoCoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Basic.lean#L69). The attribute's comment: “part (1): pseudo-coherent morphism”.

> **Stacks 06BR, part (1).** A morphism of algebraic spaces over `S` is
> *pseudo-coherent* when every commuting square of étale scheme charts induces a
> pseudo-coherent scheme morphism.

```lean
abbrev IsPseudoCoherent (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsPseudoCoherentAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Basic.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Basic.lean#L77). The attribute's comment: “part (2): pseudo-coherent at a point”.

> **Stacks 06BR, part (2).** A morphism of algebraic spaces over `S` is
> *pseudo-coherent at* a point `x` of its source when it is pseudo-coherent on an open
> subspace of the source containing `x`.

```lean
abbrev IsPseudoCoherentAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 06BS, a lemma

[Tag 06BS](https://stacks.math.columbia.edu/tag/06BS) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_baseChange_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FlatBaseChange.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FlatBaseChange.lean#L234).

> **Stacks 06BS.** A flat base change of a pseudo-coherent morphism of algebraic spaces over `S`
> is pseudo-coherent: in a cartesian square with `g : Y ⟶ Z` pseudo-coherent and `f : X ⟶ Z` flat,
> the base change `g' : Y' ⟶ X` of `g` along `f` is pseudo-coherent.

```lean
theorem isPseudoCoherent_baseChange_of_isFlat
    {X Y Y' Z : AlgebraicSpaces B S hS} {f : X ⟶ Z} {g : Y ⟶ Z} {f' : Y' ⟶ Y} {g' : Y' ⟶ X}
    (sq : IsPullback f' g' g f) (hflat : IsFlat B S hS f.hom)
    (hf : IsPseudoCoherent B S hS g.hom) :
    IsPseudoCoherent B S hS g'.hom
```

## Tag 06BT, a lemma

[Tag 06BT](https://stacks.math.columbia.edu/tag/06BT) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Composition.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Composition.lean#L95).

> **Stacks 06BT.** A composition of pseudo-coherent morphisms of algebraic spaces over `S` is
> pseudo-coherent.
>
> This is the case at pseudo-coherence of Stacks 0AML, the composition law for an every-étale-chart
> property, whose inputs are Stacks 0681 and étale locality on the source and target.

```lean
theorem isPseudoCoherent_comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsPseudoCoherent B S hS f) (hg : IsPseudoCoherent B S hS g) :
    IsPseudoCoherent B S hS (f ≫ g)
```

## Tag 06BU, a lemma

[Tag 06BU](https://stacks.math.columbia.edu/tag/06BU) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean#L55).

> **Stacks 06BU.** A pseudo-coherent morphism of algebraic spaces over `S` is locally of
> finite presentation.

```lean
theorem isLocallyOfFinitePresentation_of_isPseudoCoherent (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsPseudoCoherent B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 06BV, a lemma

[Tag 06BV](https://stacks.math.columbia.edu/tag/06BV) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_of_isFlat_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean#L65).

> **Stacks 06BV.** A flat morphism of algebraic spaces over `S` which is locally of
> finite presentation is pseudo-coherent.

```lean
theorem isPseudoCoherent_of_isFlat_of_isLocallyOfFinitePresentation (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f) :
    IsPseudoCoherent B S hS f
```

## Tag 06BW, a lemma

[Tag 06BW](https://stacks.math.columbia.edu/tag/06BW) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Composition.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Composition.lean#L111). References: SGA 6 III (1.14), “partial”.

> **Stacks 06BW.** A morphism of algebraic spaces over `S` between two algebraic spaces
> pseudo-coherent over a base algebraic space is pseudo-coherent.
>
> An étale atlas of the base is lifted twice to produce a square of étale charts of `f` whose chart
> of the source is surjective, and the scheme-level cancellation of Stacks 0683 applies to the two
> factors of the induced chart morphism of `f ≫ g`.

```lean
theorem isPseudoCoherent_of_comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsPseudoCoherent B S hS (f ≫ g)) (hg : IsPseudoCoherent B S hS g) :
    IsPseudoCoherent B S hS f
```

## Tag 06BX, a lemma

[Tag 06BX](https://stacks.math.columbia.edu/tag/06BX) in the Stacks Project.

**`AlgebraicGeometry.Space.isPseudoCoherent_iff_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Noetherian.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Noetherian.lean#L50). References: SGA 6 III (1.3), “Y loc. noetherian case”.

> **Stacks 06BX.** For a morphism of algebraic spaces over `S` whose target is locally
> Noetherian, pseudo-coherence is equivalent to being locally of finite type.

```lean
theorem isPseudoCoherent_iff_isLocallyOfFiniteType (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hYNoetherian : HasEtaleLocalProperty B S hS Y
      (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (f : X ⟶ Y) :
    IsPseudoCoherent B S hS f ↔ IsLocallyOfFiniteType B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.46, Tag 06BQ](https://stacks.math.columbia.edu/tag/06BQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
