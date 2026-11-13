---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.relativelyRepresentable_of_isLocallyQuasiFinite_isSeparated, AlgebraicGeometry.Space.isIso_of_isEtale_of_universallyInjective_of_isSurjective, AlgebraicGeometry.Space.isOpenImmersion_of_isEtale_of_universallyInjective
statement: formalized
proof: formalized
---

# 67.51 Applications

Section 67.51 of the Stacks Project, [Tag 05W4](https://stacks.math.columbia.edu/tag/05W4). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0418, a lemma

[Tag 0418](https://stacks.math.columbia.edu/tag/0418) in the Stacks Project.

**`AlgebraicGeometry.Space.relativelyRepresentable_of_isLocallyQuasiFinite_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteSeparatedRepresentable.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteSeparatedRepresentable.lean#L466).

> **Stacks 0418.** A separated, locally quasi-finite morphism of algebraic spaces over `S`
> is relatively representable along the Yoneda embedding of the big fppf site.

```lean
theorem relativelyRepresentable_of_isLocallyQuasiFinite_isSeparated
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyQuasiFinite B S hS f)
    (hs : IsSeparated B S hS f) :
    yoneda.relativelyRepresentable f
```

## Tag 05W5, a lemma

[Tag 05W5](https://stacks.math.columbia.edu/tag/05W5) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_isEtale_of_universallyInjective_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean#L95).

> **Stacks 05W5.** A morphism of algebraic spaces over `S` which is étale, universally
> injective and surjective is an isomorphism.
>
> An étale morphism is unramified, so its relative diagonal is an open immersion; together with
> universal injectivity this makes the morphism a monomorphism. An étale surjection is flat and
> locally of finite presentation, hence a one-member fppf covering of its target and so surjective
> as a map of fppf sheaves.

```lean
theorem isIso_of_isEtale_of_universallyInjective_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (he : IsEtale B S hS f) (hui : UniversallyInjective B S hS f)
    (hsurj : IsSurjective B S hS f) : IsIso f
```

**`AlgebraicGeometry.Space.isOpenImmersion_of_isEtale_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleUniversallyInjectiveOpenImmersion.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleUniversallyInjectiveOpenImmersion.lean#L47). The attribute's comment: “the open immersion clause”.

> An étale universally injective morphism of algebraic spaces over `S` is an open immersion.

```lean
theorem isOpenImmersion_of_isEtale_of_universallyInjective (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (he : IsEtale B S hS f)
    (hui : UniversallyInjective B S hS f) :
    IsOpenImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.51, Tag 05W4](https://stacks.math.columbia.edu/tag/05W4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
