---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsRegularAt, AlgebraicGeometry.Scheme.Hom.IsRegular, AlgebraicGeometry.Scheme.Hom.regular_tfae, AlgebraicGeometry.Scheme.Hom.isRegular_of_smooth, AlgebraicGeometry.regularWithLocallyNoetherianFibers_isLocalAtTarget_fppf, AlgebraicGeometry.regularWithLocallyNoetherianFibers_isLocalAtSource_smooth
statement: formalized
proof: formalized
---

# 37.21 Regular morphisms

Section 37.21 of the Stacks Project, [Tag 07R6](https://stacks.math.columbia.edu/tag/07R6). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07R7, a definition

[Tag 07R7](https://stacks.math.columbia.edu/tag/07R7) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRegularAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/RegularMorphism.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/RegularMorphism.lean#L48). The attribute's comment: “part (1)”. References: EGA IV (6.8.1).

> **Stacks Project, Tag 07R7, part (1).** Regularity of a scheme morphism at a point.

```lean
public abbrev IsRegularAt {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsRegular`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/RegularMorphism.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/RegularMorphism.lean#L54). The attribute's comment: “part (2)”. References: EGA IV (6.8.1).

> **Stacks Project, Tag 07R7, part (2).** Regularity at every source point.

```lean
public abbrev IsRegular {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 07R8, a lemma

[Tag 07R8](https://stacks.math.columbia.edu/tag/07R8) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.regular_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/Characterization.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/Characterization.lean#L596).

> The five characterizations of a regular morphism with locally Noetherian fibres.

```lean
public theorem Scheme.Hom.regular_tfae {X Y : Scheme.{u}} (f : X ⟶ Y)
    (h : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) :
    List.TFAE [
      Scheme.Hom.IsRegular f,
      Flat f ∧ ∀ y : Y,
        IsGeometricallyRegular (f.fiberToSpecResidueField y),
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : Y.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
        IsRegularRingHom (f.appLE V U hUV).hom,
      ∃ (J : Type u) (V : J → Y.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            ∀ i, Scheme.Hom.IsRegular
              (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)),
      ∃ (J : Type u) (V : J → Y.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i,
                let hUV : U i ≤ f ⁻¹ᵁ V j := (le_iSup U i).trans hU.le
                IsRegularRingHom (f.appLE (V j) (U i) hUV).hom]
```

## Tag 07R9, a lemma

[Tag 07R9](https://stacks.math.columbia.edu/tag/07R9) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isRegular_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/Smooth.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/Smooth.lean#L41). References: EGA IV (17.5.2), “Necessity”; EGA IV (6.8.6), “Implication a) ⇒ b)”.

> A smooth morphism of schemes is regular.

```lean
public theorem Scheme.Hom.isRegular_of_smooth {X Y : Scheme.{u}} (f : X ⟶ Y) [Smooth f] :
    f.IsRegular
```

## Tag 07RA, a lemma

[Tag 07RA](https://stacks.math.columbia.edu/tag/07RA) in the Stacks Project.

**`AlgebraicGeometry.regularWithLocallyNoetherianFibers_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/FppfLocalTarget.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/FppfLocalTarget.lean#L168). The attribute's comment: “fppf local on the target”.

> **Stacks Project, Tag 07RA.** Having locally Noetherian fibres and being regular is local on
> the target for the fppf topology.

```lean
public instance regularWithLocallyNoetherianFibers_isLocalAtTarget_fppf :
    (regularWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtTarget
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.regularWithLocallyNoetherianFibers_isLocalAtSource_smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/SmoothLocalSource.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RegularMorphism/SmoothLocalSource.lean#L126). The attribute's comment: “smooth local on the source”.

> **Stacks Project, Tag 07RA.** Having locally Noetherian fibres and being regular is local on
> the source for the smooth topology.

```lean
public instance regularWithLocallyNoetherianFibers_isLocalAtSource_smooth :
    (regularWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtSource
      (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.21, Tag 07R6](https://stacks.math.columbia.edu/tag/07R6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
