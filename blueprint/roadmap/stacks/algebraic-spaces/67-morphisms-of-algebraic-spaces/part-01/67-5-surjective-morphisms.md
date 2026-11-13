---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.surjective_iff_pointsMap_surjective_of_representable, AlgebraicGeometry.Space.IsSurjective, AlgebraicGeometry.Space.isSurjective_tfae, AlgebraicGeometry.Space.isSurjective_comp, AlgebraicGeometry.Space.isSurjective_of_isPullback
statement: formalized
proof: formalized
---

# 67.5 Surjective morphisms

Section 67.5 of the Stacks Project, [Tag 03MC](https://stacks.math.columbia.edu/tag/03MC). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03MD, a lemma

[Tag 03MD](https://stacks.math.columbia.edu/tag/03MD) in the Stacks Project.

**`AlgebraicGeometry.Space.surjective_iff_pointsMap_surjective_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Surjective.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Surjective.lean#L337).

> **Stacks 03MD.** A representable morphism of presheaves on the big fppf site of `S` is
> surjective — surjective after every representable base change — if and only if the induced map
> on points is surjective.
>
> No algebraic-space hypothesis is needed: representability of the morphism, which is part of
> surjectivity in the relative sense, is the only one used.

```lean
theorem surjective_iff_pointsMap_surjective_of_representable
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G)
    (hf : yoneda.relativelyRepresentable f) :
    (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      Function.Surjective (pointsMap B S hS F f)
```

## Tag 03ME, a definition

[Tag 03ME](https://stacks.math.columbia.edu/tag/03ME) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSurjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat.lean#L51).

> A morphism of algebraic spaces over `S` is *surjective* when the induced map `|X| → |Y|` on
> their sets of points is surjective.

```lean
abbrev IsSurjective (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 03MF, a lemma

[Tag 03MF](https://stacks.math.columbia.edu/tag/03MF) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Surjective.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Surjective.lean#L233).

> **Stacks 03MF.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following
> are equivalent:
>
> 1. `f` is surjective;
> 2. for every scheme `Z` in the site and every `Z ⟶ Y` the projection `X ×_Y Z ⟶ Z` is
>    surjective;
> 3. the same for every affine scheme `Z` in the site;
> 4. there is a scheme `V` in the site and a surjective étale `V ⟶ Y` with `X ×_Y V ⟶ V`
>    surjective;
> 5. there is a scheme `U` in the site and a surjective étale `φ : U ⟶ X` with `φ ≫ f`
>    surjective;
> 6. there is a commuting square whose vertical arrows are surjective étale charts
>    `U ⟶ X` and `V ⟶ Y` of schemes in the site and whose top arrow `U ⟶ V` is surjective;
> 7. there is a Zariski covering of `Y` by open subspaces `Y_i` with each `f⁻¹(Y_i) ⟶ Y_i`
>    surjective.

```lean
theorem isSurjective_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsSurjective B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsSurjective B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ g : yoneda.obj Z ⟶ Y, IsSurjective B S hS (pullback.snd f g),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            IsSurjective B S hS (pullback.snd f g),
        ∃ (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X),
          IsSurjective B S hS φ ∧ IsEtale B S hS φ ∧ IsSurjective B S hS (φ ≫ f),
        ∃ (U V : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X) (ψ : yoneda.obj V ⟶ Y)
            (h : yoneda.obj U ⟶ yoneda.obj V),
          φ ≫ f = h ≫ ψ ∧ IsSurjective B S hS φ ∧ IsEtale B S hS φ ∧
            IsSurjective B S hS ψ ∧ IsEtale B S hS ψ ∧ IsSurjective B S hS h,
        ∃ (I : Type u) (U : I → Subfunctor Y), IsZariskiCover B S hS I U ∧
          ∀ i, IsSurjective B S hS (pullback.snd f (U i).ι)]
```

## Tag 03MG, a lemma

[Tag 03MG](https://stacks.math.columbia.edu/tag/03MG) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean#L76).

> A composite of morphisms surjective on points is surjective on points.

```lean
theorem isSurjective_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsSurjective B S hS f) (hg : IsSurjective B S hS g) :
    IsSurjective B S hS (f ≫ g)
```

## Tag 03MH, a lemma

[Tag 03MH](https://stacks.math.columbia.edu/tag/03MH) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveOnPoints.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveOnPoints.lean#L373).

> A base change of a morphism of algebraic spaces surjective on points is surjective on
> points.

```lean
theorem isSurjective_of_isPullback {W Z X Y : AlgebraicSpaces B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f) (hg : IsSurjective B S hS g.hom) :
    IsSurjective B S hS q.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.5, Tag 03MC](https://stacks.math.columbia.edu/tag/03MC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
