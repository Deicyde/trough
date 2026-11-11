---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsLocallyQuasiFinite, AlgebraicGeometry.Space.IsQuasiFinite, AlgebraicGeometry.Space.IsQuasiFiniteAt, AlgebraicGeometry.Space.IsLocallyQuasiFinite.of_isPullback, AlgebraicGeometry.Space.IsQuasiFinite.of_isPullback, AlgebraicGeometry.Space.isOpen_setOf_isQuasiFiniteAt, AlgebraicGeometry.Space.setOf_isQuasiFiniteAt_eq_preimage_of_isPullback, AlgebraicGeometry.Space.setOf_isQuasiFiniteAt_eq_preimage_of_isPullback'
statement: formalized
proof: formalized
---

# 67.27 Quasi-finite morphisms

Section 67.27 of the Stacks Project, [Tag 03XI](https://stacks.math.columbia.edu/tag/03XI). 10 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03XJ, a definition

[Tag 03XJ](https://stacks.math.columbia.edu/tag/03XJ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyQuasiFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L97). The attribute's comment: “part (1): locally quasi-finite morphisms”.

> **Stacks 03XJ, part (1).** A morphism of algebraic spaces over `S` is *locally
> quasi-finite* when every commuting square of étale scheme charts induces a scheme morphism
> which is locally of finite type and locally quasi-finite.

```lean
abbrev IsLocallyQuasiFinite (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L105). The attribute's comment: “part (3): quasi-finite morphisms”.

> **Stacks 03XJ, part (3).** A morphism of algebraic spaces over `S` is *quasi-finite*
> when it is locally quasi-finite and quasi-compact.

```lean
abbrev IsQuasiFinite (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiFiniteAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteType.lean#L124). The attribute's comment: “part (2): quasi-finite at a point”.

> **Stacks 03XJ, part (2).** A morphism of algebraic spaces over `S` is *quasi-finite at*
> a point `x` of its source when some open subspace of the source containing `x` is locally
> quasi-finite over the target.

```lean
abbrev IsQuasiFiniteAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 0ABM, a lemma

[Tag 0ABM](https://stacks.math.columbia.edu/tag/0ABM) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyQuasiFinite.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L321). The attribute's comment: “part (3): locally quasi-finite”.

> The base change of a locally quasi-finite morphism of algebraic spaces over `S` along an
> arbitrary morphism of algebraic spaces is locally quasi-finite.
>
> The square is the one with `p` over `f`, so `p : W ⟶ Z` is the base change of
> `f : X ⟶ Y`.

```lean
theorem IsLocallyQuasiFinite.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyQuasiFinite B S hS f) :
    IsLocallyQuasiFinite B S hS p
```

**`AlgebraicGeometry.Space.IsQuasiFinite.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L338). The attribute's comment: “part (4): quasi-finite”.

> The base change of a quasi-finite morphism of algebraic spaces over `S` along an arbitrary
> morphism of algebraic spaces is quasi-finite.

```lean
theorem IsQuasiFinite.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiFinite B S hS f) :
    IsQuasiFinite B S hS p
```

**`AlgebraicGeometry.Space.isOpen_setOf_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean#L195). The attribute's comment: “part (1): the quasi-finite locus is open”.

> **Stacks 0ABM, part (1).** The set of points at which a morphism of algebraic spaces over
> `S` is quasi-finite is open in the point space of Tag 03BU. Applied to a base change `f'` of
> `f` this is the second clause of part (1), that the quasi-finite locus of `f'` is open.
>
> The source assumes `f` locally of finite type; that is not needed.

```lean
theorem isOpen_setOf_isQuasiFiniteAt (f : X ⟶ Y) :
    IsOpen {x | IsQuasiFiniteAt B S hS f x}
```

**`AlgebraicGeometry.Space.setOf_isQuasiFiniteAt_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean#L238). The attribute's comment: “part (2): the locus commutes with base change”. References: SGA 3 V (7.4), “more general”.

> **Stacks 0ABM, part (2).** For a morphism of algebraic spaces over `S` which is locally of
> finite type, the locus of quasi-finiteness of a base change is the inverse image of the locus
> of quasi-finiteness of the morphism.
>
> Compatible surjective étale charts of the cartesian square
> (`AlgebraicGeometry.Space.exists_compatible_etale_charts`) give a chart `V` of the target, a
> chart `U ⟶ V` of `f`, a chart `V' ⟶ V` of `g` and the induced chart `U' = U ×_V V' ⟶ V'` of
> the base change, with `U'` an atlas of the fibre product. A field-valued point of `U'` lying
> over the given point of `|X'|` turns the two squares into pointed étale charts of `f'` at that
> point and of `f` at its image, whose selected scheme points correspond under `U' ⟶ U`. Local
> quasi-finiteness of morphisms of schemes being étale local on the source and target
> (Stacks 04R3), quasi-finiteness at a point is the induced germ condition read in any one
> pointed chart (Stacks 04NC), so each side becomes quasi-finiteness of a morphism of schemes at
> corresponding points of a cartesian square of schemes, which is **Stacks 01TM**.

```lean
theorem setOf_isQuasiFiniteAt_eq_preimage_of_isPullback
    {X₁ X₀ Y₁ Y₀ : AlgebraicSpaces B S hS} {g' : X₁ ⟶ X₀} {f' : X₁ ⟶ Y₁} {f : X₀ ⟶ Y₀}
    {g : Y₁ ⟶ Y₀} (sq : IsPullback g' f' f g)
    (hf : IsLocallyOfFiniteType B S hS f.hom) :
    {x' | IsQuasiFiniteAt B S hS f'.hom x'} =
      pointsMap B S hS X₁.1 g'.hom ⁻¹' {x | IsQuasiFiniteAt B S hS f.hom x}
```

**`AlgebraicGeometry.Space.setOf_isQuasiFiniteAt_eq_preimage_of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocusBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocusBaseChange.lean#L111). The attribute's comment: “part (2): the quasi-finite locus commutes with base change”.

> In a cartesian square of presheaves over `S` whose corners `X`, `Y` and `Z` are algebraic
> spaces, with `f` locally of finite type, the locus in the source of the base change of `f` where
> that base change is quasi-finite is the preimage, under the projection on points, of the locus in
> the source of `f` where `f` is quasi-finite.
>
> The square is the one with `p` over `f` and `q` over `g`, so `p : W ⟶ Z` is the base change of
> `f : X ⟶ Y` and `q : W ⟶ X` is the projection.

```lean
theorem setOf_isQuasiFiniteAt_eq_preimage_of_isPullback'
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (hf : IsLocallyOfFiniteType B S hS f) :
    {x' | IsQuasiFiniteAt B S hS p x'} =
      pointsMap B S hS W q ⁻¹' {x | IsQuasiFiniteAt B S hS f x}
```

## Tag 03XK, a lemma

[Tag 03XK](https://stacks.math.columbia.edu/tag/03XK) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean#L76). The attribute's comment: “locally quasi-finite”.

> **Stacks 03XK**, the locally quasi-finite case: the composite of two locally quasi-finite
> morphisms of algebraic spaces over `S` is locally quasi-finite.
>
> Local quasi-finiteness of morphisms of schemes is étale local on the source and target
> (**Stacks 04R3**) and stable under composition, each conjunct being, so this is an instance of
> **Stacks 0AML**.

```lean
theorem isLocallyQuasiFinite_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsLocallyQuasiFinite B S hS f) (hg : IsLocallyQuasiFinite B S hS g) :
    IsLocallyQuasiFinite B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isQuasiFinite_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean#L94). The attribute's comment: “quasi-finite”.

> **Stacks 03XK**, the quasi-finite case: the composite of two quasi-finite morphisms of
> algebraic spaces over `S` is quasi-finite.
>
> Quasi-finiteness is local quasi-finiteness together with quasi-compactness, and the latter is
> stable under composition by **Stacks 03HG**.

```lean
theorem isQuasiFinite_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H) (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsQuasiFinite B S hS f) (hg : IsQuasiFinite B S hS g) :
    IsQuasiFinite B S hS (f ≫ g)
```

## Tag 03XL, a lemma

[Tag 03XL](https://stacks.math.columbia.edu/tag/03XL) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyQuasiFinite.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L321). The attribute's comment: “locally quasi-finite”.

> The base change of a locally quasi-finite morphism of algebraic spaces over `S` along an
> arbitrary morphism of algebraic spaces is locally quasi-finite.
>
> The square is the one with `p` over `f`, so `p : W ⟶ Z` is the base change of
> `f : X ⟶ Y`.

```lean
theorem IsLocallyQuasiFinite.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyQuasiFinite B S hS f) :
    IsLocallyQuasiFinite B S hS p
```

**`AlgebraicGeometry.Space.IsQuasiFinite.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteBaseChange.lean#L338). The attribute's comment: “quasi-finite”.

> The base change of a quasi-finite morphism of algebraic spaces over `S` along an arbitrary
> morphism of algebraic spaces is quasi-finite.

```lean
theorem IsQuasiFinite.of_isPullback
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y}
    (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsQuasiFinite B S hS f) :
    IsQuasiFinite B S hS p
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean#L109). The attribute's comment: “locally quasi-finite”.

> **Stacks 03XL**, the locally quasi-finite case: being locally quasi-finite is stable under
> base change.
>
> Local quasi-finiteness of morphisms of schemes is étale local on the source and target
> (**Stacks 04R3**) and stable under base change, each conjunct being, so this is an instance of
> **Stacks 0AMM**.

```lean
instance isLocallyQuasiFinite_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocallyQuasiFinite B S hS f.hom)
```

**`AlgebraicGeometry.Space.isQuasiFinite_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteMorphismProperty.lean#L125). The attribute's comment: “quasi-finite”.

> **Stacks 03XL**, the quasi-finite case: being quasi-finite is stable under base change.
>
> Quasi-finiteness is local quasi-finiteness together with quasi-compactness, and the latter is
> stable under base change by **Stacks 03HF**.

```lean
instance isQuasiFinite_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsQuasiFinite B S hS f.hom)
```

## Tag 06RW, a lemma

[Tag 06RW](https://stacks.math.columbia.edu/tag/06RW) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_forall_discreteTopology_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 1426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L1426).

> **Stacks 06RW.** A morphism of algebraic spaces over `S` which is locally of finite type is
> locally quasi-finite exactly when, for every field-valued point of its target, the point space
> of the fibre over that point is discrete.
>
> For the forward implication the fibre over a field-valued point is locally quasi-finite over
> the field spectrum by Stacks 03XL, so its étale charts are discrete schemes; an étale chart is
> open and surjective on points, hence the point space of the fibre is discrete.
>
> For the converse a commuting square of étale charts of `f` is compared with the fibre product
> of the chart of the target along `f`, and each point of the chart of the target is handled
> through its canonical residue-field representative: the fibre of the morphism of the site over
> that point is a chart of the corresponding fibre of `f`, which is discrete, so the morphism of
> the site has no nontrivial specialization in that fibre and is therefore locally quasi-finite
> by [Stacks Project, Tag 01TH].

```lean
theorem isLocallyQuasiFinite_iff_forall_discreteTopology_fibre
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hft : IsLocallyOfFiniteType B S hS f) :
    IsLocallyQuasiFinite B S hS f ↔
      ∀ p : FieldValuedPoint B S hS Y,
        DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f))
```

## Tag 040Z, a lemma

[Tag 040Z](https://stacks.math.columbia.edu/tag/040Z) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyQuasiFinite_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 781](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L781).

> **Stacks 040Z.** Nine criteria for a morphism of algebraic spaces over `S` to be locally
> quasi-finite: pointwise quasi-finiteness, local quasi-finiteness of every base change to a
> scheme or to an affine scheme or to one surjective étale chart of the target, local
> quasi-finiteness of the composite with one surjective étale chart of the source, and local
> quasi-finiteness of the morphism of schemes in every — or in one surjective — commuting square
> of étale charts, or over a pair of Zariski coverings.

```lean
theorem locallyQuasiFinite_tfae {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsLocallyQuasiFinite B S hS f,
      ∀ x : points B S hS X, IsQuasiFiniteAt B S hS f x,
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsLocallyQuasiFinite B S hS (pullback.fst g f),
      ∀ (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          IsLocallyQuasiFinite B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧
          IsLocallyQuasiFinite B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧ IsLocallyQuasiFinite B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsLocallyQuasiFinite B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsLocallyQuasiFinite B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsLocallyQuasiFinite B S hS ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 03XM, a lemma

[Tag 03XM](https://stacks.math.columbia.edu/tag/03XM) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L498).

> **Stacks 03XM.** An immersion of algebraic spaces over `S` is locally quasi-finite.
>
> Neither the source nor the target has to be an algebraic space: the immersion property is a
> condition on the represented base changes of the morphism, and so is what the proof uses.

```lean
theorem isLocallyQuasiFinite_of_isImmersion {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (hf : IsImmersion B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

## Tag 03XN, a lemma

[Tag 03XN](https://stacks.math.columbia.edu/tag/03XN) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L417).

> **Stacks 03XN.** If a composite of morphisms of algebraic spaces over `S` is locally
> quasi-finite, then so is its first factor.
>
> Local quasi-finiteness of morphisms of schemes is étale local on the source and target
> (Stacks 04R3) and is inherited by the first factor of a composite that has it, local finite
> type by Stacks 01T8 and the fibre condition by `AlgebraicGeometry.LocallyQuasiFinite.of_comp`,
> so this is an instance of the cancellation form of Stacks 03MJ.
>
> This is also the locally-quasi-finite clause of part (1) of **Stacks 0AGC**, whose other
> clauses are in `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Immersions.lean`.

```lean
theorem isLocallyQuasiFinite_of_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hfg : IsLocallyQuasiFinite B S hS (f ≫ g)) :
    IsLocallyQuasiFinite B S hS f
```

## Tag 0ABN, a lemma

[Tag 0ABN](https://stacks.math.columbia.edu/tag/0ABN) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_setOf_mapsTo_and_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteLocus.lean#L399).

> **Stacks 0ABN.** For a morphism of algebraic spaces over `S` of finite type, only finitely
> many points of the source lying over a fixed point of the target are points at which the
> morphism is quasi-finite.
>
> Represent the point of the target by a field-valued point `Spec k ⟶ Y` and base change twice:
> once along it, and once more along the identity of `Spec k`. The second base change is a
> finite-type morphism out of an algebraic space with quasi-compact source, so it has an
> *affine* surjective étale chart `U` (Stacks 03H6), and the morphism of schemes `U ⟶ Spec k`
> it induces is of finite type with compact source, hence quasi-compact: Stacks 0AAY bounds the
> set of its quasi-finite points over the closed point of `Spec k`, and that is all of `U`
> because `Spec k` is a one-point space.
>
> A point of `|X|` over the given point at which `f` is quasi-finite lifts through both
> cartesian squares (Stacks 03H4), and quasi-finiteness travels with it because forming the
> quasi-finite locus commutes with base change
> (`AlgebraicGeometry.Space.setOf_isQuasiFiniteAt_eq_preimage_of_isPullback`). A field-valued
> representative of the lift on the chart then exhibits the point as the image of a member of
> that finite set.

```lean
theorem finite_setOf_mapsTo_and_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsFiniteType B S hS f) (y : points B S hS Y) :
    {x : points B S hS X |
      pointsMap B S hS X f x = y ∧ IsQuasiFiniteAt B S hS f x}.Finite
```

## Tag 0463, a lemma

[Tag 0463](https://stacks.math.columbia.edu/tag/0463) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiFinite.lean#L550). The attribute's comment: “local quasi-finiteness”.

> **Stacks 0463**, the local quasi-finiteness clause: a monomorphism of algebraic spaces over
> `S` which is locally of finite type is locally quasi-finite.
>
> The relative diagonal of a monomorphism is an isomorphism, hence an open immersion after every
> represented base change, so part (2) of [Stacks Project, Tag 05W1] makes the morphism
> unramified and [Stacks Project, Tag 05W0] makes it locally quasi-finite.
>
> The separatedness clause of the tag is `AlgebraicGeometry.Space.isSeparated_of_mono`, which is
> [Stacks Project, Tag 042N] and needs no finite-type hypothesis.

```lean
theorem isLocallyQuasiFinite_of_mono {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hmono : Mono f) (hft : IsLocallyOfFiniteType B S hS f) :
    IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Space.isSeparated_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedQuasiFiniteEtaleDescent.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedQuasiFiniteEtaleDescent.lean#L218). The attribute's comment: “separatedness”.

> **Stacks 042N.** A monomorphism of presheaves on the big fppf site of `S` is a separated
> morphism of algebraic spaces over `S`: its relative diagonal is an isomorphism, and an
> isomorphism is a closed immersion. The statement is made for an arbitrary morphism of presheaves
> on the big fppf site of `S`; no algebraic-space hypothesis is used.
>
> This strictly generalises `AlgebraicGeometry.Space.isSeparated_of_isIso`, which is the same
> statement for an isomorphism.

```lean
theorem isSeparated_of_mono {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (m : F ⟶ G) (hm : Mono m) :
    IsSeparated B S hS m
```

**`AlgebraicGeometry.Space.isSeparated_isLocallyQuasiFinite_of_isLocallyOfFiniteType_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean#L243).

> **Stacks 0463.** A monomorphism of algebraic spaces over `S` which is locally of finite type
> is separated and locally quasi-finite.
>
> Separatedness is [Stacks Project, Tag 042N], already available as
> `AlgebraicGeometry.Space.isSeparated_of_mono`; local quasi-finiteness goes through
> unramifiedness, which a monomorphism locally of finite type has by
> `AlgebraicGeometry.Space.isUnramified_of_isLocallyOfFiniteType_of_mono`.
>
> These are two of the three assertions of the "moreover" clause of
> [Stacks Project, Tag 05W6], reached from its condition (3); the equivalence of conditions (1)
> and (3) carries them over to condition (1), and the two unconditional equivalences below carry
> them over to conditions (2) and (4).

```lean
theorem isSeparated_isLocallyQuasiFinite_of_isLocallyOfFiniteType_mono (f : X ⟶ Y)
    (h : IsLocallyOfFiniteType B S hS f ∧ Mono f) :
    IsSeparated B S hS f ∧ IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Space.isSeparated_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeDiagonalMonomorphism.lean#L148). The attribute's comment: “separatedness”.

> **Stacks 042N.** A monomorphism of algebraic spaces over `S` is separated: its relative
> diagonal is an isomorphism, and an isomorphism is a closed immersion.
>
> The statement is made for an arbitrary morphism of presheaves on the big fppf site of `S`; no
> algebraic-space hypothesis is used.

```lean
theorem isSeparated_of_mono {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : F ⟶ G) (hg : Mono g) :
    IsSeparated B S hS g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.27, Tag 03XI](https://stacks.math.columbia.edu/tag/03XI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
