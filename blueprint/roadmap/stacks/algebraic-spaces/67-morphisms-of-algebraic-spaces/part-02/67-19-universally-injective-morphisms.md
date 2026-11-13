---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.universallyInjective_iff_injective_on_field_points, AlgebraicGeometry.Space.injectiveOnFieldPoints_tfae, AlgebraicGeometry.Space.UniversallyInjective, AlgebraicGeometry.AffineLineInvolution.not_isSeparated_squaringMap, AlgebraicGeometry.AffineLineInvolution.squaringMap, AlgebraicGeometry.AffineLineInvolution.isIso_squaringMap_pullback_puncturedAffineLine, AlgebraicGeometry.AffineLineInvolution.existsUnique_pointsMap_squaringMap_eq_originPoint, AlgebraicGeometry.AffineLineInvolution.universallyInjective_squaringMap
statement: formalized
proof: formalized
---

# 67.19 Universally injective morphisms

Section 67.19 of the Stacks Project, [Tag 03MT](https://stacks.math.columbia.edu/tag/03MT). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03MU, a lemma

[Tag 03MU](https://stacks.math.columbia.edu/tag/03MU) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_iff_injective_on_field_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean#L197).

> **Stacks 03MU.** A representable transformation is universally injective if and only if
> its maps on field-valued points are injective.

```lean
theorem universallyInjective_iff_injective_on_field_points
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a : F ⟶ G) (ha : yoneda.relativelyRepresentable a) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@AlgebraicGeometry.UniversallyInjective : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)) a ↔
      ∀ (K : Type u) [Field K] (T : BigFppfOver B S hS),
        ((BigFppfOver.toScheme B S hS).obj T ≅ Spec (.of K)) →
      Function.Injective (a.app (Opposite.op T)))
```

## Tag 040X, a lemma

[Tag 040X](https://stacks.math.columbia.edu/tag/040X) in the Stacks Project.

**`AlgebraicGeometry.Space.injectiveOnFieldPoints_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyInjectiveFieldPoints.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyInjectiveFieldPoints.lean#L291).

> **Stacks 040X.** For a morphism `f : X ⟶ Y` from an algebraic space over `S` the
> following are equivalent:
>
> 1. the map `X(K) → Y(K)` is injective for every field `K` over `S`,
> 2. for every morphism `Y' ⟶ Y` of algebraic spaces over `S` the induced map
>    `|Y' ×_Y X| → |Y'|` is injective, and
> 3. the diagonal morphism `X ⟶ X ×_Y X` is surjective.

```lean
theorem injectiveOnFieldPoints_tfae (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    List.TFAE [InjectiveOnFieldPoints B S hS f, UniversallyInjective B S hS f,
      IsSurjective B S hS (pullback.diagonal f)]
```

## Tag 03MV, a definition

[Tag 03MV](https://stacks.math.columbia.edu/tag/03MV) in the Stacks Project.

**`AlgebraicGeometry.Space.UniversallyInjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean#L46).

> **Stacks 03MV.** A morphism is universally injective if every base change along an
> algebraic space induces an injective map on points.

```lean
abbrev UniversallyInjective {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 05VS, a remark

[Tag 05VS](https://stacks.math.columbia.edu/tag/05VS) in the Stacks Project.

**`AlgebraicGeometry.AffineLineInvolution.not_isSeparated_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionSquaringMap.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionSquaringMap.lean#L501). The attribute's comment: “part (5): the squaring morphism is not separated”.

> **Stacks 05VS, part (5)**, which is also the last assertion of the example of **Stacks
> 05Z6**: the squaring map `X ⟶ 𝐀¹_k` on the involution quotient is not separated. Its relative
> diagonal has the relation of Stacks 02Z1 as a represented base change, and that relation is
> not a closed immersion.

```lean
theorem not_isSeparated_squaringMap (hchar : (2 : k) ≠ 0) :
    ¬ Space.IsSeparated B (Spec (.of k)) hk (squaringMap k B hk)
```

**`AlgebraicGeometry.AffineLineInvolution.squaringMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMap.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMap.lean#L111). The attribute's comment: “part (1): the morphism X ⟶ 𝐀¹\_k squaring the coordinate”.

> **Stacks 05VS, part (1).** The canonical morphism from the involution quotient to the
> affine line, descended from squaring the coordinate: the point with coordinate `x` is sent to
> the point with coordinate `x ^ 2`. This is the morphism `X ⟶ 𝐀¹_k` of the remark.

```lean
noncomputable def squaringMap (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    (involutionQuotient k B hk).obj ⟶
      Stacks.Groupoids.points (Over.post (X := B.obj hk) B.inclusion) (affineLine k)
```

**`AlgebraicGeometry.AffineLineInvolution.isIso_squaringMap_pullback_puncturedAffineLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean#L362). The attribute's comment: “part (2): an isomorphism away from the origin”.

> **Stacks 05VS, part (2).** Over a field in which `2` is invertible, the squaring map from
> the involution quotient to the affine line is an isomorphism away from the origin: its base
> change along the inclusion of the punctured affine line is an isomorphism.

```lean
theorem isIso_squaringMap_pullback_puncturedAffineLine (hchar : (2 : k) ≠ 0)
    (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    IsIso (pullback.snd (squaringMap k B hk)
      ((Over.post (X := B.obj hk) B.inclusion).op.whiskerLeft
        (yoneda.map (puncturedAffineLineInclusion k))))
```

**`AlgebraicGeometry.AffineLineInvolution.existsUnique_pointsMap_squaringMap_eq_originPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean#L540). The attribute's comment: “part (3): exactly one point above the origin”.

> **Stacks 05VS, part (3).** Exactly one point of the involution quotient lies over the
> origin of the affine line under the morphism descended from squaring the coordinate.
>
> The quotient projection is locally surjective, hence surjective on the points of Stacks 03BU,
> so every point of the quotient over the origin comes from a point of the affine line whose
> square is the origin; such a point is the origin by
> `AlgebraicGeometry.AffineLineInvolution.eq_affineLineZero_of_square_eq`, and the image of the
> origin is the point sought. No assumption on the characteristic is needed: in characteristic
> two the relation is the diagonal and the statement is that squaring is injective on
> field-valued points.

```lean
theorem existsUnique_pointsMap_squaringMap_eq_originPoint (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    ∃! x : Space.points B (Spec (.of k)) hk (involutionQuotient k B hk).obj,
      Space.pointsMap B (Spec (.of k)) hk _ (squaringMap k B hk) x = originPoint k B hk
```

**`AlgebraicGeometry.AffineLineInvolution.universallyInjective_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/SquaringMapProperties.lean#L594). The attribute's comment: “part (4): universally injective”.

> **Stacks 05VS, part (4).** Away from characteristic two the morphism descended from
> squaring the coordinate is universally injective.
>
> Universal injectivity is tested on field-valued points by
> `AlgebraicGeometry.Space.universallyInjective_of_fieldPoints`, so it suffices to make two
> sections of the quotient over the spectrum of a field with the same square agree over a further
> field spectrum. The quotient projection is locally surjective, so after two successive
> restrictions both sections are classes of points `t₁`, `t₂` of the affine line with the same
> square. Over a field the coordinate of `t₁` is zero or a unit: in the first case the common
> square is the origin and both points are the origin, the test object being reduced; in the
> second the common square lies in the punctured line, and
> `AlgebraicGeometry.AffineLineInvolution.quotient_eq_of_square_eq` identifies the two classes.

```lean
theorem universallyInjective_squaringMap (hchar : (2 : k) ≠ 0) (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    Space.UniversallyInjective B (Spec (.of k)) hk (squaringMap k B hk)
```

## Tag 03MW, a lemma

[Tag 03MW](https://stacks.math.columbia.edu/tag/03MW) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean#L248). References: EGA IV (11.9.14), “base change stability”.

> **Stacks 03MW.** A base change of a universally injective morphism of algebraic spaces
> over `S` is universally injective.
>
> Nothing is needed beyond unwinding the definition: a base change of `Z ×_Y X ⟶ Z` along
> `k : W ⟶ Z` is a base change of `X ⟶ Y` along `k ≫ g`.

```lean
theorem universallyInjective_pullback (f : X ⟶ Y) (g : Z ⟶ Y)
    (hf : UniversallyInjective B S hS f) :
    UniversallyInjective B S hS (pullback.fst g f)
```

**`AlgebraicGeometry.Space.universallyInjective_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean#L302). References: EGA IV (11.9.14), “base change stability”.

> **Stacks 03MW** for an arbitrary cartesian square: if `IsPullback a b g f` and `f` is
> universally injective, then so is `a`.
>
> This is `AlgebraicGeometry.Space.universallyInjective_pullback` composed with the
> identification of the given square with the canonical fibre product.

```lean
theorem universallyInjective_of_isPullback (hC : IsAlgebraicSpace B S hS C)
    (hZ : IsAlgebraicSpace B S hS Z) (hT : IsAlgebraicSpace B S hS T) (f : C ⟶ T) (g : Z ⟶ T)
    (hf : UniversallyInjective B S hS f) {a : A ⟶ Z} {b : A ⟶ C}
    (hpb : IsPullback a b g f) : UniversallyInjective B S hS a
```

## Tag 03MX, a lemma

[Tag 03MX](https://stacks.math.columbia.edu/tag/03MX) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjectiveSchemeTests.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjectiveSchemeTests.lean#L362).

> **Stacks 03MX.** For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the
> following are equivalent: `f` is universally injective; the base change `Z ×_Y X ⟶ Z` of `f`
> along every morphism from a scheme over `S` is universally injective; the same for every
> morphism from an affine scheme over `S`; the same for one morphism from a scheme over `S`
> which is surjective; and the base change of `f` along each member of some Zariski covering of
> `Y` is universally injective.

```lean
theorem universallyInjective_tfae {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [UniversallyInjective B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          UniversallyInjective B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
            UniversallyInjective B S hS (pullback.snd f g),
        ∃ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsSurjective B S hS g ∧ UniversallyInjective B S hS (pullback.snd f g),
        ∃ (I : Type u) (U : I → Subfunctor Y), IsZariskiCover B S hS I U ∧
          ∀ i, UniversallyInjective B S hS (pullback.snd f (U i).ι)]
```

## Tag 03MY, a lemma

[Tag 03MY](https://stacks.math.columbia.edu/tag/03MY) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversallyInjective/Basic.lean#L277).

> **Stacks 03MY.** A composition of universally injective morphisms of algebraic spaces over
> `S` is universally injective.
>
> The base change `W ×_Z X ⟶ W` of the composite along `k : W ⟶ Z` is identified by the pasting
> isomorphism `W ×_Z X ≅ (W ×_Z Y) ×_Y X` with the composition of a base change of `X ⟶ Y` and a
> base change of `Y ⟶ Z`.

```lean
theorem universallyInjective_comp (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : UniversallyInjective B S hS f) (hg : UniversallyInjective B S hS g) :
    UniversallyInjective B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.19, Tag 03MT](https://stacks.math.columbia.edu/tag/03MT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
