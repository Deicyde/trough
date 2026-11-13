---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.graphTransformation, AlgebraicGeometry.Space.graphTransformation_app_family_Z, AlgebraicGeometry.Space.graphTransformation_injective, AlgebraicGeometry.Space.graphTransformation_relative_isOpenImmersion, AlgebraicGeometry.Space.isAlgebraicSpace_relativeHom, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_relativeHomProjection, AlgebraicGeometry.Space.isAlgebraicSpace_relativeHom_and_isLocallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 99.12 Relative morphisms

Section 99.12 of the Stacks Project, [Tag 0D19](https://stacks.math.columbia.edu/tag/0D19). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D1A, a lemma

[Tag 0D1A](https://stacks.math.columbia.edu/tag/0D1A) in the Stacks Project.

**`AlgebraicGeometry.Space.graphTransformation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean#L414). The attribute's comment: “the graph transformation”.

> **Stacks 0D1A.** The *graph transformation* `Mor_Q(Z, X) ⟶ Hilb_{Z ×_Q X / Q}`: it carries a
> relative morphism `(a, b)` at a test scheme `T` to the graph of `b`, a closed subspace of
> `(Z ×_Q X)_T` which is of finite presentation, flat and proper over `T` because `z` is. It is
> natural because the graph of a restriction is the inverse image of the graph
> (`AlgebraicGeometry.Space.range_graphMap_restrict`). The source is composed with the universe lift,
> the Hilbert presheaf taking values one universe up.

```lean
def graphTransformation (hsep : IsSeparated B S hS x) (hfp : IsFinitePresentation B S hS z)
    (hflat : IsFlat B S hS z) (hproper : IsProper B S hS z) :
    relativeHom B S hS Z X Q z x hZ hX hQ ⋙ uliftFunctor.{u + 1, u} ⟶
      hilbertPresheaf (graphAmbientMap B S hS z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.graphTransformation_app_family_Z`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean#L449). The attribute's comment: “the transformation is the graph”.

> **Stacks 0D1A.** The graph transformation maps a relative morphism to its graph: the closed
> subspace of the family it produces is the range of the graph map.

```lean
theorem graphTransformation_app_family_Z (hsep : IsSeparated B S hS x)
    (hfp : IsFinitePresentation B S hS z) (hflat : IsFlat B S hS z) (hproper : IsProper B S hS z)
    (T : BigFppfOver B S hS) (p : (relativeHom B S hS Z X Q z x hZ hX hQ).obj (Opposite.op T)) :
    ((graphTransformation hZ hX hQ hsep hfp hflat hproper).app (Opposite.op T)
        (ULift.up p)).family.Z =
      Subfunctor.range (graphMap (relativeHomSections B S hS Z X Q z x hZ hX hQ T p))
```

**`AlgebraicGeometry.Space.graphTransformation_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/GraphOfRelativeMorphism.lean#L461). The attribute's comment: “injectivity”.

> **Stacks 0D1A.** The graph transformation is injective at every test scheme: two relative
> morphisms with the same graph have the same first component, and then
> `AlgebraicGeometry.Space.relativeMorphism_eq_of_range_graphMap_eq` identifies them.

```lean
theorem graphTransformation_injective (hsep : IsSeparated B S hS x)
    (hfp : IsFinitePresentation B S hS z) (hflat : IsFlat B S hS z) (hproper : IsProper B S hS z)
    (T : BigFppfOver B S hS) :
    Function.Injective
      ((graphTransformation hZ hX hQ hsep hfp hflat hproper).app (Opposite.op T))
```

## Tag 0D1B, a lemma

[Tag 0D1B](https://stacks.math.columbia.edu/tag/0D1B) in the Stacks Project.

**`AlgebraicGeometry.Space.graphTransformation_relative_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismsOpenInHilbert.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismsOpenInHilbert.lean#L416).

> The graph transformation `Mor_Q(Z, X) ⟶ Hilb_{Z ×_Q X / Q}` is representable by open
> immersions.

```lean
theorem graphTransformation_relative_isOpenImmersion (hsep : IsSeparated B S hS x)
    (hfp : IsFinitePresentation B S hS z) (hflat : IsFlat B S hS z)
    (hproper : IsProper B S hS z) :
    (MorphismProperty.inverseImage (@AlgebraicGeometry.IsOpenImmersion.{u})
        (BigFppfOver.toScheme B S hS)).relative
      (yoneda ⋙ (Functor.whiskeringRight _ _ _).obj uliftFunctor.{u + 1, u})
      (graphTransformation hZ hX hQ hsep hfp hflat hproper)
```

## Tag 0D1C, a proposition

[Tag 0D1C](https://stacks.math.columbia.edu/tag/0D1C) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_relativeHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpace.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpace.lean#L198). The attribute's comment: “algebraicity”.

> **Stacks 0D1C**, algebraicity. For `x` of finite presentation and separated and `z` of finite
> presentation, flat and proper, the relative morphism functor `Mor_Q(Z, X)` is an algebraic space
> over `S`.
>
> It is realised as an open subspace of a model of the Hilbert functor of `Z ×_Q X` over `Q` by
> Stacks 0D1A and 0D1B, and that model is an algebraic space by Stacks 0D01,
> `AlgebraicGeometry.Space.hasHilbertModelsOver_of_isAlgebraicSpace`; an open immersion is
> representable, so Stacks 02WY transfers algebraicity to the source.

```lean
theorem isAlgebraicSpace_relativeHom (hx_fp : IsFinitePresentation B S hS x)
    (hx_sep : IsSeparated B S hS x) (hz_fp : IsFinitePresentation B S hS z)
    (hz_flat : IsFlat B S hS z) (hz_proper : IsProper B S hS z) :
    IsAlgebraicSpace B S hS (relativeHom B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_relativeHomProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpace.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpace.lean#L216). The attribute's comment: “local finite presentation over the base”.

> **Stacks 0D1C**, local finite presentation over the base. For `x` of finite presentation and
> separated and `z` of finite presentation, flat and proper, the projection
> `Mor_Q(Z, X) ⟶ Q` is locally of finite presentation.
>
> The projection factors through a model of the Hilbert functor of `Z ×_Q X` over `Q`
> (`AlgebraicGeometry.Space.morToHilbertModel_comp_toBase`); the first factor is an open immersion,
> hence locally of finite presentation, and the second is locally of finite presentation by
> Stacks 0D01, `AlgebraicGeometry.Space.hasHilbertModelsOver_of_isAlgebraicSpace`.

```lean
theorem isLocallyOfFinitePresentation_relativeHomProjection
    (hx_fp : IsFinitePresentation B S hS x) (hx_sep : IsSeparated B S hS x)
    (hz_fp : IsFinitePresentation B S hS z) (hz_flat : IsFlat B S hS z)
    (hz_proper : IsProper B S hS z) :
    IsLocallyOfFinitePresentation B S hS
      (relativeHomProjection B S hS Z X Q z x hZ hX hQ)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_relativeHom_and_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpaceUnconditional.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeMorphismAlgebraicSpaceUnconditional.lean#L59).

> Let `z : Z ⟶ Q` and `x : X ⟶ Q` be morphisms of algebraic spaces over `S`. Assume `x` is of
> finite presentation and separated, and `z` is of finite presentation, flat and proper. Then
> `Mor_Q(Z, X)` is an algebraic space, and its projection to `Q` is locally of finite
> presentation.

```lean
theorem isAlgebraicSpace_relativeHom_and_isLocallyOfFinitePresentation
    {Z X Q : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (z : Z ⟶ Q) (x : X ⟶ Q)
    (hZ : IsAlgebraicSpace B S hS Z) (hX : IsAlgebraicSpace B S hS X)
    (hQ : IsAlgebraicSpace B S hS Q)
    (hx_fp : IsFinitePresentation B S hS x) (hx_sep : IsSeparated B S hS x)
    (hz_fp : IsFinitePresentation B S hS z) (hz_flat : IsFlat B S hS z)
    (hz_proper : IsProper B S hS z) :
    IsAlgebraicSpace B S hS (relativeHom B S hS Z X Q z x hZ hX hQ) ∧
      IsLocallyOfFinitePresentation B S hS
        (relativeHomProjection B S hS Z X Q z x hZ hX hQ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.12, Tag 0D19](https://stacks.math.columbia.edu/tag/0D19)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
