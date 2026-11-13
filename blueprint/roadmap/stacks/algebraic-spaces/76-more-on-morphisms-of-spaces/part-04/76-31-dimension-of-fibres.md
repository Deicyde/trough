---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.fiberDimension_eq_dimension_pullback, AlgebraicGeometry.Space.fiberDimension_pullback_snd, AlgebraicGeometry.Space.lowerSemicontinuous_fiberDimension, AlgebraicGeometry.Space.upperSemicontinuous_fiberDimension, AlgebraicGeometry.Space.isLocallyConstant_fiberDimension
statement: formalized
proof: formalized
---

# 76.31 Dimension of fibres

Section 76.31 of the Stacks Project, [Tag 0D4L](https://stacks.math.columbia.edu/tag/0D4L). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D4M, a lemma

[Tag 0D4M](https://stacks.math.columbia.edu/tag/0D4M) in the Stacks Project.

**`AlgebraicGeometry.Space.fiberDimension_eq_dimension_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionFieldFibre.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionFieldFibre.lean#L212).

> **Stacks 0D4M.** For a morphism of algebraic spaces over `S` of finite type and a field-valued
> point `p` of its target, the fibre dimension at the point `p` represents is the dimension of the
> fibre of `f` over `p`, and it is not `⊤`.

```lean
theorem fiberDimension_eq_dimension_pullback
    (hf : IsFiniteType B S hS f) (p : FieldValuedPoint B S hS Y) :
    fiberDimension B S hS f (p.class B S hS Y) =
      dimension B S hS (pullback (yonedaEquiv.symm p.value) f)
        (isAlgebraicSpace_pullback B S hS (yonedaEquiv.symm p.value) f
          (isAlgebraicSpace_yoneda B S hS (p.siteObject B S hS Y)) hX hY) ∧
      fiberDimension B S hS f (p.class B S hS Y) ≠ ⊤
```

## Tag 0D4N, a lemma

[Tag 0D4N](https://stacks.math.columbia.edu/tag/0D4N) in the Stacks Project.

**`AlgebraicGeometry.Space.fiberDimension_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionBaseChange.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionBaseChange.lean#L58).

> **Stacks 0D4N.** The fibre-dimension function of the base change of a finite type morphism of
> algebraic spaces over `S` is the pullback of the fibre-dimension function of the morphism along
> the map on points of the morphism of targets.

```lean
theorem fiberDimension_pullback_snd {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (hf : IsFiniteType B S hS f) :
    fiberDimension B S hS (pullback.snd f g) =
      fiberDimension B S hS f ∘ pointsMap B S hS Y' g
```

## Tag 0D4P, a lemma

[Tag 0D4P](https://stacks.math.columbia.edu/tag/0D4P) in the Stacks Project.

**`AlgebraicGeometry.Space.lowerSemicontinuous_fiberDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionLowerSemicontinuity.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionLowerSemicontinuity.lean#L323).

> **Stacks 0D4P.** The fibre-dimension function of a flat morphism of algebraic spaces over `S`
> of finite presentation is lower semicontinuous on the points of its target.

```lean
theorem lowerSemicontinuous_fiberDimension
    (hflat : IsFlat B S hS f) (hfp : IsFinitePresentation B S hS f) :
    LowerSemicontinuous (fiberDimension B S hS f)
```

## Tag 0D4Q, a lemma

[Tag 0D4Q](https://stacks.math.columbia.edu/tag/0D4Q) in the Stacks Project.

**`AlgebraicGeometry.Space.upperSemicontinuous_fiberDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionUpperSemicontinuity.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionUpperSemicontinuity.lean#L94).

> **Stacks 0D4Q.** The fibre-dimension function of a proper morphism of algebraic spaces over
> `S` is upper semicontinuous on the points of its target.

```lean
theorem upperSemicontinuous_fiberDimension (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsProper B S hS f) :
    UpperSemicontinuous (fiberDimension B S hS f)
```

## Tag 0D4R, a lemma

[Tag 0D4R](https://stacks.math.columbia.edu/tag/0D4R) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyConstant_fiberDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionLocallyConstant.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/DimensionLocallyConstant.lean#L49). References: EGA IV (14.2.5), “flat fin. pres. case”.

> **Stacks 0D4R.** The fibre-dimension function of a proper flat morphism of algebraic spaces
> over `S` of finite presentation is locally constant on the points of its target.

```lean
theorem isLocallyConstant_fiberDimension (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hProper : IsProper B S hS f)
    (hFlat : IsFlat B S hS f) (hFP : IsFinitePresentation B S hS f) :
    IsLocallyConstant (fiberDimension B S hS f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.31, Tag 0D4L](https://stacks.math.columbia.edu/tag/0D4L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
