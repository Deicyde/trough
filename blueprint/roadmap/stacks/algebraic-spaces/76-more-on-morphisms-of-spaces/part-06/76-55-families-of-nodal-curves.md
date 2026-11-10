---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsAtWorstNodalOfRelativeDimensionOne, AlgebraicGeometry.Space.isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange, AlgebraicGeometry.Space.isAtWorstNodalOfRelativeDimensionOne_tfae, AlgebraicGeometry.Space.exists_isGreatest_isNodalOpen_baseChange
statement: formalized
proof: formalized
---

# 76.55 Families of nodal curves

Section 76.55 of the Stacks Project, [Tag 0DSD](https://stacks.math.columbia.edu/tag/0DSD). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DSE, a definition

[Tag 0DSE](https://stacks.math.columbia.edu/tag/0DSE) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAtWorstNodalOfRelativeDimensionOne`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean#L71).

> **Stacks 0DSE.** A morphism of algebraic spaces over `S` is *at-worst-nodal of
> relative dimension one* when every commuting square of étale scheme charts induces a
> scheme morphism which is at-worst-nodal of relative dimension one.

```lean
abbrev IsAtWorstNodalOfRelativeDimensionOne (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 0DSF, a lemma

[Tag 0DSF](https://stacks.math.columbia.edu/tag/0DSF) in the Stacks Project.

**`AlgebraicGeometry.Space.isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean#L80).

> **Stacks 0DSF.** Being at-worst-nodal of relative dimension one is preserved by base
> change of morphisms of algebraic spaces over `S`.

```lean
theorem isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsAtWorstNodalOfRelativeDimensionOne B S hS f.hom)
```

## Tag 0DSG, a lemma

[Tag 0DSG](https://stacks.math.columbia.edu/tag/0DSG) in the Stacks Project.

**`AlgebraicGeometry.Space.isAtWorstNodalOfRelativeDimensionOne_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Nodal.lean#L97).

> **Stacks 0DSG.** Eight criteria for a morphism of algebraic spaces over `S` to be
> at-worst-nodal of relative dimension one: the condition may be tested after base change to
> every scheme or to every affine scheme, on one surjective étale chart of the target, on the
> composite with one surjective étale chart of the source, in every or in one surjective
> commuting square of étale charts, or over a pair of Zariski coverings.

```lean
theorem isAtWorstNodalOfRelativeDimensionOne_tfae (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsAtWorstNodalOfRelativeDimensionOne B S hS f,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAtWorstNodalOfRelativeDimensionOne B S hS (Limits.pullback.snd f g),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsAtWorstNodalOfRelativeDimensionOne B S hS (Limits.pullback.snd f g),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧
          IsAtWorstNodalOfRelativeDimensionOne B S hS (Limits.pullback.snd f g),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧
          IsAtWorstNodalOfRelativeDimensionOne B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne
            ((BigFppfOver.toScheme B S hS).map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧
          AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne
            ((BigFppfOver.toScheme B S hS).map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (Limits.pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsAtWorstNodalOfRelativeDimensionOne B S hS
            ((Xopen i j).ι ≫ Limits.pullback.snd f (Yopen i).ι)
    ]
```

## Tag 0DSH, a lemma

[Tag 0DSH](https://stacks.math.columbia.edu/tag/0DSH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isGreatest_isNodalOpen_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NodalOpenSubspace.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NodalOpenSubspace.lean#L558).

> **Stacks 0DSH.** Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is flat and locally of finite presentation. Then there is a maximal open
> subspace `X' ⊆ X` such that the restriction of `f` to `X'` is at-worst-nodal of relative
> dimension one, and formation of `X'` commutes with arbitrary base change.
>
> The maximal open subspace is `AlgebraicGeometry.Space.nodalOpenSubspace`; it is an open
> subspace on which the restriction of `f` is at-worst-nodal of relative dimension one, and it
> contains every open subspace with that property, which is the content of the `IsGreatest`
> assertion. The second assertion is that for an arbitrary morphism `g : Y' ⟶ Y` of algebraic
> spaces over `S`, the locus of the base change `X ×_Y Y' ⟶ Y'` of `f` along `g` is the inverse
> image of the locus of `f` under the projection to `X`.

```lean
theorem exists_isGreatest_isNodalOpen_baseChange {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f) :
    IsGreatest {W : Subfunctor X | IsNodalOpen B S hS f W} (nodalOpenSubspace B S hS f) ∧
      ∀ Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS Y' →
        ∀ g : Y' ⟶ Y, nodalOpenSubspace B S hS (pullback.snd f g) =
          (nodalOpenSubspace B S hS f).preimage (pullback.fst f g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.55, Tag 0DSD](https://stacks.math.columbia.edu/tag/0DSD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
