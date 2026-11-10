---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsPerfect, AlgebraicGeometry.Space.IsPerfectAt, AlgebraicGeometry.Space.IsPerfect.of_isPullback_of_isFlat, AlgebraicGeometry.Space.IsPerfect.pullback_snd, AlgebraicGeometry.Space.IsPerfect.comp, AlgebraicGeometry.Space.isFlat_and_isPerfect_iff_isFlat_and_isLocallyOfFinitePresentation, AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_isProper
statement: formalized
proof: formalized
---

# 76.47 Perfect morphisms

Section 76.47 of the Stacks Project, [Tag 06BY](https://stacks.math.columbia.edu/tag/06BY). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06BZ, a definition

[Tag 06BZ](https://stacks.math.columbia.edu/tag/06BZ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPerfect`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Perfect.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Perfect.lean#L65). The attribute's comment: “part (1): perfect morphism”.

> **Stacks 06BZ, part (1).** A morphism of algebraic spaces over `S` is *perfect* when
> every commuting square of étale scheme charts induces a perfect scheme morphism.

```lean
abbrev IsPerfect (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsPerfectAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Perfect.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Perfect.lean#L73). The attribute's comment: “part (2): perfect at a point”.

> **Stacks 06BZ, part (2).** A morphism of algebraic spaces over `S` is *perfect at* a
> point `x` of its source when it is perfect on an open subspace of the source containing
> `x`.

```lean
abbrev IsPerfectAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 06C0, a lemma

[Tag 06C0](https://stacks.math.columbia.edu/tag/06C0) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPerfect.of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean#L73).

> **Stacks 06C0.** A flat base change of a perfect morphism of algebraic spaces over `S` is
> perfect: in a cartesian square with `g : Y ⟶ Z` perfect and `f : X ⟶ Z` flat, the base change
> `g' : Y' ⟶ X` of `g` along `f` is perfect.

```lean
theorem IsPerfect.of_isPullback_of_isFlat
    {X Y Y' Z : AlgebraicSpaces B S hS} {f : X ⟶ Z} {g : Y ⟶ Z} {f' : Y' ⟶ Y} {g' : Y' ⟶ X}
    (sq : IsPullback f' g' g f) (hflat : IsFlat B S hS f.hom) (hf : IsPerfect B S hS g.hom) :
    IsPerfect B S hS g'.hom
```

**`AlgebraicGeometry.Space.IsPerfect.pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean#L83). The attribute's comment: “pullback spelling”.

> **Stacks 06C0** in the `pullback` spelling: if `f : X ⟶ Y` is a perfect morphism of algebraic
> spaces over `S` and `g : Y' ⟶ Y` is flat, then the projection `X ×_Y Y' ⟶ Y'` is perfect.

```lean
theorem IsPerfect.pullback_snd {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hg : IsFlat B S hS g.hom) (hf : IsPerfect B S hS f.hom) :
    IsPerfect B S hS (Limits.pullback.snd f.hom g.hom)
```

## Tag 06C1, a lemma

[Tag 06C1](https://stacks.math.columbia.edu/tag/06C1) in the Stacks Project.

**`AlgebraicGeometry.Space.IsPerfect.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/PerfectStability.lean#L92).

> **Stacks 06C1.** A composition of perfect morphisms of algebraic spaces over `S` is
> perfect.

```lean
theorem IsPerfect.comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsPerfect B S hS f) (hg : IsPerfect B S hS g) :
    IsPerfect B S hS (f ≫ g)
```

## Tag 06C2, a lemma

[Tag 06C2](https://stacks.math.columbia.edu/tag/06C2) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_and_isPerfect_iff_isFlat_and_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/FinitePresentation.lean#L75).

> **Stacks 06C2.** A morphism of algebraic spaces over `S` is flat and perfect if and
> only if it is flat and locally of finite presentation.

```lean
theorem isFlat_and_isPerfect_iff_isFlat_and_isLocallyOfFinitePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) :
    (IsFlat B S hS f ∧ IsPerfect B S hS f) ↔
      (IsFlat B S hS f ∧ IsLocallyOfFinitePresentation B S hS f)
```

## Tag 0E4U, a lemma

[Tag 0E4U](https://stacks.math.columbia.edu/tag/0E4U) in the Stacks Project.

**`AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectProperPushforward.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectProperPushforward.lean#L255).

> **Stacks 0E4U.**  Let `S` be a scheme, let `Y` be a Noetherian algebraic space over `S`, let
> `f : X ⟶ Y` be a perfect proper morphism of algebraic spaces over `S`, and let `E` be a perfect
> object of `D(𝒪_X)`.  Then `Rf_*E` is a perfect object of `D(𝒪_Y)`.
>
> Perfectness is tested on the affine étale charts of `Y`, over which the restriction of `Rf_*E` is
> the derived direct image along the base change of `f` (Stacks 08GE), and the affine case is
> `AlgebraicGeometry.Space.isPerfect_derivedModulePushforward_of_isProper_of_isAffine`.

```lean
theorem isPerfect_derivedModulePushforward_of_isProper
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hY : IsNoetherian B S hS hZ Y.1) (hfPerfect : IsPerfect B S hS f.hom)
    (hfProper : IsProper B S hS f.hom)
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect E) :
    (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect
      ((Stacks.DerivedFunctor.totalRightDerived (modulePushforward B S hS f)).obj E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.47, Tag 06BY](https://stacks.math.columbia.edu/tag/06BY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
