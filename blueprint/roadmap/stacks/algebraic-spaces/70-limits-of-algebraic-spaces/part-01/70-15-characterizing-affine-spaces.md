---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAffineSpace_target_of_isFinite_of_isSurjective, AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed_of_isAffineSpace, AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction, AlgebraicGeometry.Space.isRepresentable_iff_isRepresentable_of_isIntegralHom_of_bijective, AlgebraicGeometry.Space.isClosedImmersion_of_isClosedImmersion_pullback_snd_of_bijective
statement: formalized
proof: formalized
---

# 70.15 Characterizing affine spaces

Section 70.15 of the Stacks Project, [Tag 07VQ](https://stacks.math.columbia.edu/tag/07VQ). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07VS, a lemma

[Tag 07VS](https://stacks.math.columbia.edu/tag/07VS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineSpace_target_of_isFinite_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOfFiniteSurjection.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfFiniteSurjection.lean#L484). The attribute's comment: “the target of a finite surjection from an affine algebraic space is affine”.

> **Stacks 07VS.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`. Assume that `f` is surjective and finite, and that `X` is affine. Then `Y` is affine.
>
> The proof is the source's. `Y` is separated by Stacks 05Z2 and quasi-compact, `X` being so. By
> Stacks 07VR, `X` is the limit of a directed system of algebraic spaces `X_a`, finite and of finite
> presentation over `Y`, with closed immersions as transition morphisms; such a system satisfies the
> chapter's convention (tag 07SD), its transition morphisms being monomorphisms, so by Stacks 07SQ
> some `X_a` is affine. As `f` factors through `X_a ⟶ Y`, the latter is surjective, and the case of a
> morphism of finite presentation,
> `AlgebraicGeometry.Space.isAffineSpace_of_isFinite_of_isFinitePresentation_of_isSurjective`, which
> runs through Stacks 07SU, 07SK, 084Z, 07SN, 07SQ and 07VP, concludes.

```lean
theorem isAffineSpace_target_of_isFinite_of_isSurjective
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hsurj : IsSurjective B S hS f) (hfin : IsFinite B S hS f)
    (haff : IsAffineSpace B S hS X) :
    IsAffineSpace B S hS Y
```

## Tag 07VT, a proposition

[Tag 07VT](https://stacks.math.columbia.edu/tag/07VT) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineSpace_of_isSurjective_of_universallyClosed_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjectionUnconditional.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineOfUniversallyClosedSurjectionUnconditional.lean#L212). The attribute's comment: “target of a universally closed surjection from an affine algebraic space is affine”.

> **Stacks 07VT.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`. Assume that `X` is affine and that `f` is surjective and universally closed. Then `Y` is
> affine.

```lean
theorem isAffineSpace_of_isSurjective_of_universallyClosed_of_isAffineSpace (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hsurj : IsSurjective B S hS f) (hclosed : UniversallyClosed B S hS f)
    (haff : IsAffineSpace B S hS X) :
    IsAffineSpace B S hS Y
```

## Tag 07VU, a lemma

[Tag 07VU](https://stacks.math.columbia.edu/tag/07VU) in the Stacks Project.

**`AlgebraicGeometry.IsAlgebraicSpace.isRepresentable_of_isRepresentable_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfSchemeReduction.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfSchemeReduction.lean#L173).

> **Stacks 049D, Stacks 07VU.** Let `S` be a scheme and let `X` be an algebraic space over
> `S`. If `X_red` is a scheme, then `X` is a scheme.
>
> The inclusion of the reduction is a closed immersion bijective on points, so
> `AlgebraicGeometry.Space.isRepresentable_of_isClosedImmersion_of_bijective` applies.

```lean
theorem isRepresentable_of_isRepresentable_reduction {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hred : (reduction B S hS X hX).toFunctor.IsRepresentable) :
    X.IsRepresentable
```

## Tag 07VV, a lemma

[Tag 07VV](https://stacks.math.columbia.edu/tag/07VV) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_iff_isRepresentable_of_isIntegralHom_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijectionUnconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeOfIntegralBijectionUnconditional.lean#L69). The attribute's comment: “for an integral morphism of algebraic spaces bijective on points, the source is a scheme if and only if the target is”.

> **Stacks 07VV.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`. Assume `f` is integral and induces a bijection `|X| → |Y|`. Then `X` is a scheme if
> and only if `Y` is a scheme.
>
> The implication from the source is
> `AlgebraicGeometry.Space.isRepresentable_target_of_isIntegralHom_of_bijective`, through Stacks
> 07VT, and the implication from the target is
> `AlgebraicGeometry.Space.isRepresentable_of_isIntegralHom`, which needs no bijectivity.

```lean
theorem isRepresentable_iff_isRepresentable_of_isIntegralHom_of_bijective
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsIntegralHom B S hS f) (hbij : Function.Bijective (pointsMap B S hS F f)) :
    F.IsRepresentable ↔ G.IsRepresentable
```

## Tag 08B2, a lemma

[Tag 08B2](https://stacks.math.columbia.edu/tag/08B2) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_of_isClosedImmersion_pullback_snd_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimalBaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionInfinitesimalBaseChange.lean#L125). The attribute's comment: “the whole lemma, with hypotheses (1)-(4) as in the source: `hi` (1), `hbij` (2), `hbc` (3) and `hfin` (4); the 07VU step of the proof is the proved `isRepresentable_of_isClosedImmersion_of_bijective`”.

> **Stacks 08B2.** Let `f : X ⟶ Y` and `i : Y' ⟶ Y` be morphisms of algebraic spaces over `S`.
> If `i` is a closed immersion, bijective on points, if the base change of `f` along `i` is a
> closed immersion, and if either `f` is of finite type or `i` is of finite presentation, then `f`
> is a closed immersion.
>
> This is the registered form of Stacks 08B2. The 07VU step of the source's proof is
> `AlgebraicGeometry.Space.isRepresentable_of_isClosedImmersion_of_bijective`.

```lean
theorem isClosedImmersion_of_isClosedImmersion_pullback_snd_of_bijective
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (i : Y' ⟶ Y) (hi : IsClosedImmersion B S hS i)
    (hbij : Function.Bijective (pointsMap B S hS Y' i))
    (hbc : IsClosedImmersion B S hS (pullback.snd f i))
    (hfin : IsFiniteType B S hS f ∨ IsFinitePresentation B S hS i) :
    IsClosedImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.15, Tag 07VQ](https://stacks.math.columbia.edu/tag/07VQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
