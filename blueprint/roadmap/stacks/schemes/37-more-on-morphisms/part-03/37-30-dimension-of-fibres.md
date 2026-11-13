---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_nonempty_open_fiberDimension_eq, AlgebraicGeometry.Scheme.Hom.fiberDimension, AlgebraicGeometry.Scheme.Hom.fiberDimension_eq_of_isPullback, AlgebraicGeometry.isLocallyConstructible_fiberDimension_eq, AlgebraicGeometry.lowerSemicontinuous_fiberDimension, AlgebraicGeometry.upperSemicontinuous_fiberDimension, AlgebraicGeometry.isLocallyConstant_fiberDimension
statement: formalized
proof: formalized
---

# 37.30 Dimension of fibres

Section 37.30 of the Stacks Project, [Tag 05F6](https://stacks.math.columbia.edu/tag/05F6). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05F7, a lemma

[Tag 05F7](https://stacks.math.columbia.edu/tag/05F7) in the Stacks Project.

**`AlgebraicGeometry.exists_nonempty_open_fiberDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/GenericConstancy.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/GenericConstancy.lean#L232). References: EGA IV (9.5.6), “dim X\_s = n near η”.

> **Stacks Project, Tag 05F7.** Let `f : X ⟶ Y` be a morphism of finite type with `Y`
> irreducible with generic point `η`. If the generic fibre has dimension `n`, then the fibres over
> some nonempty open subset of `Y` all have dimension `n`.

```lean
public theorem exists_nonempty_open_fiberDimension_eq {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IrreducibleSpace Y] [LocallyOfFiniteType f] [QuasiCompact f] (n : ℕ) (η : Y)
    (hη : IsGenericPoint η Set.univ) (hdim : f.fiberDimension η = (n : WithBot ℕ∞)) :
    ∃ V : Y.Opens, (V : Set Y).Nonempty ∧ ∀ y ∈ V, f.fiberDimension y = (n : WithBot ℕ∞)
```

## Tag 05F8, a lemma

[Tag 05F8](https://stacks.math.columbia.edu/tag/05F8) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.fiberDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Basic.lean#L74). The attribute's comment: “the function `n_{X/Y}`”. References: EGA IV (14.2.4).

> The dimension-of-fibres function of a morphism of schemes assigns to a point of the target
> the dimension of the scheme-theoretic fibre over it. Points outside the image of the morphism
> have empty fibre, hence dimension `⊥`.

```lean
public noncomputable def fiberDimension (f : X ⟶ Y) : Y → WithBot ℕ∞
```

**`AlgebraicGeometry.Scheme.Hom.fiberDimension_eq_of_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Basic.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Basic.lean#L152). The attribute's comment: “the base-change formula `n_{X'/Y'} = n_{X/Y} ∘ g`”.

> **Stacks Project, Tag 05F8.** The dimension-of-fibres function of a morphism locally of
> finite type is unchanged by base change: for a pullback square with `f` locally of finite type,
> the dimension-of-fibres function of the base change is the composite of that of `f` with the
> morphism of bases.

```lean
public lemma fiberDimension_eq_of_isPullback {X' Y' : Scheme.{u}} {g' : X' ⟶ X} {f' : X' ⟶ Y'}
    {f : X ⟶ Y} {g : Y' ⟶ Y} (hsq : IsPullback g' f' f g) [LocallyOfFiniteType f] :
    f'.fiberDimension = f.fiberDimension ∘ g
```

## Tag 05F9, a lemma

[Tag 05F9](https://stacks.math.columbia.edu/tag/05F9) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_fiberDimension_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Constructible.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/Constructible.lean#L257). References: EGA IV (9.2.6.1); EGA IV (9.5.5), “Z = X, max dimension”; SGA 3 VIB (4.1), “(ii)”.

> **Stacks Project, Tag 05F9.** For a morphism of schemes of finite presentation, every level
> set of the dimension-of-fibres function is locally constructible in the target.

```lean
public theorem isLocallyConstructible_fiberDimension_eq {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : FinitePresentation f) (n : WithBot ℕ∞) :
    IsLocallyConstructible {y : Y | f.fiberDimension y = n}
```

## Tag 0D4H, a lemma

[Tag 0D4H](https://stacks.math.columbia.edu/tag/0D4H) in the Stacks Project.

**`AlgebraicGeometry.lowerSemicontinuous_fiberDimension`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/LowerSemicontinuity.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/LowerSemicontinuity.lean#L112).

> **Stacks Project, Tag 0D4H.** The dimension-of-fibres function of a flat morphism of finite
> presentation is lower semicontinuous.

```lean
public lemma lowerSemicontinuous_fiberDimension {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f]
    (hf : FinitePresentation f) : LowerSemicontinuous f.fiberDimension
```

## Tag 0D4I, a lemma

[Tag 0D4I](https://stacks.math.columbia.edu/tag/0D4I) in the Stacks Project.

**`AlgebraicGeometry.upperSemicontinuous_fiberDimension`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UpperSemicontinuity.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/UpperSemicontinuity.lean#L102). References: EGA IV (13.1.5), “universally closed”.

> **Stacks Project, Tag 0D4I.** The dimension-of-fibres function of a universally closed
> morphism of schemes locally of finite type is upper semicontinuous. In particular this holds for
> a proper morphism, which is the source's statement.

```lean
public lemma upperSemicontinuous_fiberDimension {X Y : Scheme.{u}} (f : X ⟶ Y)
    [UniversallyClosed f] [LocallyOfFiniteType f] :
    UpperSemicontinuous f.fiberDimension
```

## Tag 0D4J, a lemma

[Tag 0D4J](https://stacks.math.columbia.edu/tag/0D4J) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstant_fiberDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/LocallyConstant.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/LocallyConstant.lean#L95). References: EGA IV (14.2.5), “flat fin. pres. case”; EGA IV (13.2.12), “(ii), special case”; SGA 3 VIB (4.3), “special case”.

> **Stacks Project, Tag 0D4J.** The dimension-of-fibres function of a proper, flat morphism of
> schemes of finite presentation is locally constant.

```lean
public theorem isLocallyConstant_fiberDimension {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f]
    [Flat f] (hfp : FinitePresentation f) : IsLocallyConstant f.fiberDimension
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.30, Tag 05F6](https://stacks.math.columbia.edu/tag/05F6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
