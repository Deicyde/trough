---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleCechSpectralSequence, AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfCechSpectralSequence
statement: formalized
proof: formalized
---

# 96.20 Cohomology on algebraic stacks

Section 96.20 of the Stacks Project, [Tag 06XI](https://stacks.math.columbia.edu/tag/06XI). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06XJ, a proposition

[Tag 06XJ](https://stacks.math.columbia.edu/tag/06XJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleCechSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean#L266). The attribute's comment: “part (1): the étale spectral sequence of a presentation which is representable by algebraic spaces, surjective and smooth”.

> **Stacks 06XJ, part (1).** Let `f : 𝒰 ⟶ 𝒳` be a `1`-morphism of algebraic stacks which is
> representable by algebraic spaces, surjective and smooth, and let `𝓕` be an abelian sheaf on the
> étale site of `𝒳`. Then there is a first-quadrant spectral sequence
> `E₁^{p,q} = H^q_étale(𝒰ₚ, fₚ⁻¹𝓕) ⇒ H^{p+q}_étale(𝒳, 𝓕)`, where
> `𝒰ₚ = 𝒰 ×_𝒳 ⋯ ×_𝒳 𝒰` (`p + 1` factors) is the degree `p` term of the relative Čech nerve of `f`
> and `fₚ : 𝒰ₚ ⟶ 𝒳` its projection; the first page, the first-quadrant vanishing and the
> convergence to the étale cohomology of `𝓕` are the fields of
> `Stacks.RelativeCech.SpectralSequenceData`.

```lean
theorem exists_etaleCechSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hsmooth : IsSmooth B S hS f)
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.etale)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.SpectralSequenceData B S hS 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) SiteKind.etale 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfCechSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean#L285). The attribute's comment: “part (2): the fppf spectral sequence of a presentation which is representable by algebraic spaces, surjective, flat and locally of finite presentation”.

> **Stacks 06XJ, part (2).** Let `f : 𝒰 ⟶ 𝒳` be a `1`-morphism of algebraic stacks which is
> representable by algebraic spaces, surjective, flat and locally of finite presentation, and let
> `𝓕` be an abelian sheaf on (the fppf site of) `𝒳`. Then there is a first-quadrant spectral
> sequence `E₁^{p,q} = H^q_fppf(𝒰ₚ, fₚ⁻¹𝓕) ⇒ H^{p+q}_fppf(𝒳, 𝓕)`, where
> `𝒰ₚ = 𝒰 ×_𝒳 ⋯ ×_𝒳 𝒰` (`p + 1` factors) is the degree `p` term of the relative Čech nerve of `f`
> and `fₚ : 𝒰ₚ ⟶ 𝒳` its projection; the first page, the first-quadrant vanishing and the
> convergence to the fppf cohomology of `𝓕` are the fields of
> `Stacks.RelativeCech.SpectralSequenceData`.

```lean
theorem exists_fppfCechSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hflat : IsFlat B S hS f)
    (hlfp : IsLocallyOfFinitePresentation B S hS f)
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.fppf)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.SpectralSequenceData B S hS 𝒳.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) SiteKind.fppf 𝓕)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.20, Tag 06XI](https://stacks.math.columbia.edu/tag/06XI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
