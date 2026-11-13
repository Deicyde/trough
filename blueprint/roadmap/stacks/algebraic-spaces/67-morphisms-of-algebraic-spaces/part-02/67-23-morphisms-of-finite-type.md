---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsLocallyOfFiniteType, AlgebraicGeometry.Space.IsFiniteType, AlgebraicGeometry.Space.IsFiniteTypeAt, AlgebraicGeometry.Space.isLocallyOfFiniteType_comp', AlgebraicGeometry.Space.isLocallyOfFiniteType_comp, AlgebraicGeometry.Space.isFiniteType_comp, AlgebraicGeometry.Space.isFiniteType_comp', AlgebraicGeometry.Space.isLocallyOfFiniteType_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 67.23 Morphisms of finite type

Section 67.23 of the Stacks Project, [Tag 03XE](https://stacks.math.columbia.edu/tag/03XE). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03XF, a definition

[Tag 03XF](https://stacks.math.columbia.edu/tag/03XF) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyOfFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L83). The attribute's comment: “part (1): locally of finite type”. References: EGA I (6.6.2).

> **Stacks 03XF, part (1).** A morphism of algebraic spaces over `S` is *locally of
> finite type* when every commuting square of étale scheme charts induces a scheme morphism
> which is locally of finite type.

```lean
abbrev IsLocallyOfFiniteType (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsFiniteType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L90). The attribute's comment: “part (3): finite type”.

> **Stacks 03XF, part (3).** A morphism of algebraic spaces over `S` is *of finite type*
> when it is locally of finite type and quasi-compact.

```lean
abbrev IsFiniteType (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsFiniteTypeAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L114). The attribute's comment: “part (2): finite type at a point”.

> **Stacks 03XF, part (2).** A morphism of algebraic spaces over `S` is *of finite type at*
> a point `x` of its source when some open subspace of the source containing `x` is locally of
> finite type over the target.

```lean
abbrev IsFiniteTypeAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 03XG, a lemma

[Tag 03XG](https://stacks.math.columbia.edu/tag/03XG) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_comp'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePermanence.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypePermanence.lean#L55). The attribute's comment: “locally of finite type”.

> The composite `f ≫ g` of two morphisms locally of finite type is locally of finite type, as
> soon as the intermediate and final presheaves `G` and `H` are algebraic spaces over `S`.

```lean
theorem isLocallyOfFiniteType_comp' (f : F ⟶ G) (g : G ⟶ H)
    (hG : IsAlgebraicSpace B S hS G) (hH : IsAlgebraicSpace B S hS H)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L138). The attribute's comment: “locally of finite type”.

> **Stacks 03XG**, the case of being locally of finite type: the composite of two morphisms of
> algebraic spaces over `S` which are locally of finite type is locally of finite type.
>
> Being locally of finite type is étale local on the source and target (Stacks 04R3) and stable
> under composition (Stacks 01T3), so this is an instance of Stacks 0AML.

```lean
theorem isLocallyOfFiniteType_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsLocallyOfFiniteType B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isFiniteType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean#L94). The attribute's comment: “finite type”.

> **Stacks 03XG, finite type.** The composite of two morphisms of algebraic spaces over `S`
> which are of finite type is of finite type: it is locally of finite type by Stacks 03XG and
> quasi-compact by Stacks 03HG.

```lean
theorem isFiniteType_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsFiniteType B S hS f) (hg : IsFiniteType B S hS g) :
    IsFiniteType B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isFiniteType_comp'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperPermanence.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperPermanence.lean#L65). The attribute's comment: “finite type”.

> **Stacks 03XG, finite type.** The composite of two morphisms of algebraic spaces over `S`
> which are of finite type is of finite type.
>
> Algebraicity of the source is not needed and is not assumed, which is what distinguishes this
> from `AlgebraicGeometry.Space.isFiniteType_comp`.

```lean
theorem isFiniteType_comp' (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (hf : IsFiniteType B S hS f) (hg : IsFiniteType B S hS g) :
    IsFiniteType B S hS (f ≫ g)
```

## Tag 03XH, a lemma

[Tag 03XH](https://stacks.math.columbia.edu/tag/03XH) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L156). The attribute's comment: “locally of finite type”.

> **Stacks 03XH**, the case of being locally of finite type: being locally of finite type is
> stable under base change.
>
> Being locally of finite type is étale local on the source and target (Stacks 04R3) and stable
> under base change (Stacks 01T4), so this is an instance of Stacks 0AMM.

```lean
theorem isLocallyOfFiniteType_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocallyOfFiniteType B S hS f.hom)
```

**`AlgebraicGeometry.Space.isFiniteType_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperBaseChange.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperBaseChange.lean#L66). The attribute's comment: “finite type”.

> Being of finite type is stable under base change for morphisms of algebraic spaces over
> `S`.

```lean
instance isFiniteType_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsFiniteType B S hS f.hom)
```

**`AlgebraicGeometry.Space.IsLocallyOfFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L285). The attribute's comment: “locally of finite type”.

> The base change of a morphism of algebraic spaces over
> `S` which is locally of finite type along an arbitrary morphism of algebraic spaces is
> locally of finite type.
>
> The square is the one with `p` over `f`, so `p : W ⟶ Z` is the base change of
> `f : X ⟶ Y`.

```lean
theorem IsLocallyOfFiniteType.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS p
```

**`AlgebraicGeometry.Space.IsFiniteType.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L303). The attribute's comment: “finite type”.

> The base change of a morphism of algebraic spaces over
> `S` which is of finite type along an arbitrary morphism of algebraic spaces is of finite
> type.

```lean
theorem IsFiniteType.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsFiniteType B S hS f) :
    IsFiniteType B S hS p
```

## Tag 040Y, a lemma

[Tag 040Y](https://stacks.math.columbia.edu/tag/040Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteType.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteType.lean#L701). The attribute's comment: “all nine conditions (1)–(9) equivalent”.

> **Stacks 040Y.** For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the
> following nine conditions are equivalent: `f` is locally of finite type; `f` is of finite type
> at every point of `X`; the base change of `f` along every morphism from a scheme over `S` is
> locally of finite type; the same for every morphism from an affine scheme over `S`; the base
> change of `f` along some surjective étale chart of `Y` is locally of finite type; the
> composite of `f` with some surjective étale chart of `X` is locally of finite type; every
> commuting square of étale charts of `f` induces a scheme morphism which is locally of finite
> type; some such square whose chart of `X` is surjective does; and there are Zariski coverings
> of `Y` and of the inverse images in `X` of its members over which `f` is locally of finite
> type.
>
> The conditions are listed in the order of the source, so the `n`-th entry of the list is
> condition `(n)`. Schemes over `Y` are objects of the big fppf site of `S`, and condition (7)
> is literally the definition of local finite type, which is why (1) ⇔ (7) is `Iff.rfl`.

```lean
theorem isLocallyOfFiniteType_tfae (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsLocallyOfFiniteType B S hS f,
       (∀ x : points B S hS X, IsFiniteTypeAt B S hS f x),
       (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsLocallyOfFiniteType B S hS (pullback.fst g f)),
       (∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
            IsLocallyOfFiniteType B S hS (pullback.fst g f)),
       (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y), IsSurjective B S hS g ∧
          IsEtale B S hS g ∧ IsLocallyOfFiniteType B S hS (pullback.fst g f)),
       (∃ (U : BigFppfOver B S hS) (g : yoneda.obj U ⟶ X), IsSurjective B S hS g ∧
          IsEtale B S hS g ∧ IsLocallyOfFiniteType B S hS (g ≫ f)),
       HoldsOnEveryEtaleChart B S hS
         (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) f,
       HoldsOnSurjectiveEtaleChart B S hS
         (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) f,
       (∃ (I : Type u) (Yᵢ : I → Subfunctor Y), IsZariskiCover B S hS I Yᵢ ∧
          ∀ i, ∃ (J : Type u) (Xᵢⱼ : J → Subfunctor ((Yᵢ i).preimage f).toFunctor),
            IsZariskiCover B S hS J Xᵢⱼ ∧
              ∀ j, IsLocallyOfFiniteType B S hS
                ((Xᵢⱼ j).ι ≫ (Yᵢ i).fromPreimage f))]
```

## Tag 04ZK, a lemma

[Tag 04ZK](https://stacks.math.columbia.edu/tag/04ZK) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyNoetherian_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocallyNoetherianFiniteType.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocallyNoetherianFiniteType.lean#L40). References: EGA IV (1.3.3); EGA I (6.3.7), “locally Noetherian”.

> A morphism of algebraic spaces over `S` which is locally of finite type and whose target is
> locally Noetherian has locally Noetherian source.

```lean
theorem isLocallyNoetherian_of_isLocallyOfFiniteType
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (hN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)
```

## Tag 0462, a lemma

[Tag 0462](https://stacks.math.columbia.edu/tag/0462) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L206). References: EGA I (6.6.6), “(v)”; EGA IV (1.3.4), “(v)”.

> **Stacks 0462.** If a composite of morphisms of algebraic spaces over `S` is locally of
> finite type, then so is its first factor.
>
> This is also the locally-of-finite-type clause of part (1) of **Stacks 0AGC**, whose other
> clauses are in
> `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean`.

```lean
theorem isLocallyOfFiniteType_of_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hfg : IsLocallyOfFiniteType B S hS (f ≫ g)) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 06ED, a lemma

[Tag 06ED](https://stacks.math.columbia.edu/tag/06ED) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteType.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FiniteType.lean#L146).

> **Stacks 06ED.** An immersion of algebraic spaces over `S` is locally of finite type.
> Each of its represented base changes is an immersion of schemes, hence locally of finite
> type, and being locally of finite type passes from the represented base changes to the étale
> charts by the implication of Stacks 03MJ.

```lean
theorem isLocallyOfFiniteType_of_isImmersion (f : X ⟶ Y) (hf : IsImmersion B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.23, Tag 03XE](https://stacks.math.columbia.edu/tag/03XE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
