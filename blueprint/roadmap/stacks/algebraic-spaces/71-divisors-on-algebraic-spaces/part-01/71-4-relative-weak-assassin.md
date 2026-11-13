---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isLocallyNoetherianFiber_tfae, AlgebraicGeometry.Space.isLocallyNoetherianFiberAt_iff_exists, AlgebraicGeometry.Space.IsLocallyNoetherianFiber, AlgebraicGeometry.Space.HasLocallyNoetherianFibersAtPoints, AlgebraicGeometry.Space.hasLocallyNoetherianFibersAtPoints_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.relativeWeakAssassin_tfae, AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_iff_of_mono, AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_iff_associated
statement: formalized
proof: formalized
---

# 71.4 Relative weak assassin

Section 71.4 of the Stacks Project, [Tag 0CUV](https://stacks.math.columbia.edu/tag/0CUV). 10 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CUW, a lemma

[Tag 0CUW](https://stacks.math.columbia.edu/tag/0CUW) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyNoetherianFiber_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean#L400). The attribute's comment: “conditions (1), (2) and (3)”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and a point `y` of `Y`, local
> Noetherianity of the fibre of `f` over the residue field of a point of an étale scheme chart of
> `Y` above `y` holds for some such chart exactly when it holds for every such chart, and exactly
> when the base change of `f` along some field-valued representative of `y` is locally
> Noetherian.

```lean
theorem isLocallyNoetherianFiber_tfae
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (y : points B S hS Y) :
    List.TFAE [
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y)
          (v : (BigFppfOver.toScheme B S hS).obj V),
        IsEtale B S hS g ∧
          pointsMap B S hS (yoneda.obj V) g
            ((schemePointRepresentative B S hS V v).class B S hS (yoneda.obj V)) = y ∧
          IsLocallyNoetherianFiberAt B S hS f
            (FieldValuedPoint.map B S hS (yoneda.obj V) g
              (schemePointRepresentative B S hS V v))),
      (∀ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y)
          (v : (BigFppfOver.toScheme B S hS).obj V),
        IsEtale B S hS g →
          pointsMap B S hS (yoneda.obj V) g
            ((schemePointRepresentative B S hS V v).class B S hS (yoneda.obj V)) = y →
          IsLocallyNoetherianFiberAt B S hS f
            (FieldValuedPoint.map B S hS (yoneda.obj V) g
              (schemePointRepresentative B S hS V v))),
      (∃ p : FieldValuedPoint B S hS Y,
        p.class B S hS Y = y ∧ IsLocallyNoetherianFiberAt B S hS f p)
    ]
```

**`AlgebraicGeometry.Space.isLocallyNoetherianFiberAt_iff_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean#L479). The attribute's comment: “condition (4): a monomorphic representative”.

> If a point `y` of `Y` has a field-valued representative presenting it by a monomorphism,
> then the fibre of `f` over that representative is locally Noetherian exactly when the fibre over
> some field-valued representative of `y` is.

```lean
theorem isLocallyNoetherianFiberAt_iff_exists
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (y : points B S hS Y) (p₀ : FieldValuedPoint B S hS Y)
    [Mono (fieldMorphism B S hS Y p₀)] (hp₀ : p₀.class B S hS Y = y) :
    IsLocallyNoetherianFiberAt B S hS f p₀ ↔
      ∃ p : FieldValuedPoint B S hS Y,
        p.class B S hS Y = y ∧ IsLocallyNoetherianFiberAt B S hS f p
```

## Tag 0CUX, a definition

[Tag 0CUX](https://stacks.math.columbia.edu/tag/0CUX) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyNoetherianFiber`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean#L506). The attribute's comment: “the fibre over a point”.

> The fibre of a morphism `f : X ⟶ Y` of algebraic spaces over `S` above a point `y` of `Y`
> is *locally Noetherian* when the base change of `f` along some field-valued representative of
> `y` is locally Noetherian.
>
> By `AlgebraicGeometry.Space.isLocallyNoetherianFiber_tfae` this is equivalent to the fibre
> over the residue field of a point above `y` of some, equivalently of every, étale scheme chart
> of `Y` being locally Noetherian.

```lean
abbrev IsLocallyNoetherianFiber {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (y : points B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.HasLocallyNoetherianFibersAtPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean#L518). The attribute's comment: “all fibres”.

> A morphism of algebraic spaces over `S` has *locally Noetherian fibres* when its fibre
> above every point of its target is locally Noetherian.
>
> `AlgebraicGeometry.Space.HasLocallyNoetherianFibers` is the every-chart reading of the same
> condition, quantifying instead over the points of the étale scheme charts of the target; by
> `AlgebraicGeometry.Space.isLocallyNoetherianFiber_tfae` the two agree pointwise.

```lean
abbrev HasLocallyNoetherianFibersAtPoints {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) : Prop
```

## Tag 0CUY, a lemma

[Tag 0CUY](https://stacks.math.columbia.edu/tag/0CUY) in the Stacks Project.

**`AlgebraicGeometry.Space.hasLocallyNoetherianFibersAtPoints_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Fibres/LocallyNoetherian.lean#L551).

> A morphism of algebraic spaces over `S` which is locally of finite type has locally
> Noetherian fibres: the spectrum of a field is Noetherian, so Stacks 04ZK applies to the base
> change of `f` along any field-valued representative of a point of the target.

```lean
theorem hasLocallyNoetherianFibersAtPoints_of_isLocallyOfFiniteType
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    HasLocallyNoetherianFibersAtPoints B S hS f
```

## Tag 0CUZ, a lemma

[Tag 0CUZ](https://stacks.math.columbia.edu/tag/0CUZ) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeWeakAssassin_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean#L316). The attribute's comment: “conditions (1) to (5)”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`, let `𝓕` be a quasi-coherent `𝒪_X`-module and let `x ∈ |X|`. The following are
> equivalent:
>
> 1. for some étale `V ⟶ Y` with `V` a scheme, some `v ∈ V` above `f(x)` and some `x' ∈ |X_v|`
>    above `x`, the point `x'` is weakly associated to `𝓕|_{X_v}`;
> 2. for every such `V`, `v` and `x'`, the point `x'` is weakly associated to `𝓕|_{X_v}`;
> 3. for some étale `V ⟶ Y`, some étale `U ⟶ X ×_Y V` with `U`, `V` schemes and some `u ∈ U`
>    above `x`, with image `v ∈ V`, the point `u` is weakly associated to `𝓕|_{U_v}`;
> 4. for every such `U`, `V` and `u`, the point `u` is weakly associated to `𝓕|_{U_v}`;
> 5. for some field `k`, some `Spec(k) ⟶ Y` representing `f(x)` and some `t ∈ |X_k|` above `x`,
>    the point `t` is weakly associated to `𝓕|_{X_k}`.

```lean
theorem relativeWeakAssassin_tfae (f : X ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    List.TFAE [IsWeaklyAssociatedOnSomeSchemeChartFibre B S hS f F x,
      IsWeaklyAssociatedOnEverySchemeChartFibre B S hS f F x,
      IsWeaklyAssociatedOnSomeEtaleChartSquare B S hS f F x,
      IsWeaklyAssociatedOnEveryEtaleChartSquare B S hS f F x,
      IsRelativeWeaklyAssociatedPoint B S hS f F x]
```

**`AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_iff_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean#L348). The attribute's comment: “condition (6), at a monomorphism from the spectrum of a field representing the image point”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S`, let `𝓕` be a quasi-coherent `𝒪_X`-module, let `x ∈ |X|` and let `Spec(k₀) ⟶ Y` be a
> monomorphism representing `f(x)`. Then there is a unique point `x₀ ∈ |X_{k₀}|` mapping to `x`,
> and the equivalent conditions of `AlgebraicGeometry.Space.relativeWeakAssassin_tfae` hold
> exactly when `x₀` is a weakly associated point of `𝓕|_{X_{k₀}}`.

```lean
theorem isRelativeWeaklyAssociatedPoint_iff_of_mono (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (p₀ : FieldValuedPoint B S hS Y.1) [Mono (fieldMorphism B S hS Y.1 p₀)]
    {x : points B S hS X.1} (rep : p₀.class B S hS Y.1 = pointsMap B S hS X.1 f.hom x) :
    (∃! x₀ : points B S hS (fibreAtFieldValuedPoint B S hS f p₀).1,
      pointsMap B S hS (fibreAtFieldValuedPoint B S hS f p₀).1
        (fibreAtFieldValuedPointProjection B S hS f p₀).hom x₀ = x) ∧
    ∀ x₀ : points B S hS (fibreAtFieldValuedPoint B S hS f p₀).1,
      pointsMap B S hS (fibreAtFieldValuedPoint B S hS f p₀).1
          (fibreAtFieldValuedPointProjection B S hS f p₀).hom x₀ = x →
        (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
          IsWeaklyAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f p₀)
            ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f p₀)).obj F)
            x₀)
```

**`AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_iff_associated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceRelativeWeakAssassinTFAE.lean#L530). The attribute's comment: “the locally Noetherian case: weakly associated replaced by associated in conditions (1), (2), (3), (4) and (6)”.

> Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S`, let `𝓕` be a quasi-coherent `𝒪_X`-module and let `x ∈ |X|` be such that the
> fibre of `f` over `f(x)` is locally Noetherian. Then in conditions (1), (2), (3), (4) and (6) of
> `AlgebraicGeometry.Space.relativeWeakAssassin_tfae` and
> `AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_iff_of_mono` "weakly associated" may
> be replaced by "associated": each of the resulting conditions is equivalent to `x` lying in the
> relative weak assassin `WeakAss_{X/Y}(𝓕)`.

```lean
theorem isRelativeWeaklyAssociatedPoint_iff_associated (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x : points B S hS X.1)
    (noeth : IsLocallyNoetherianFiber B S hS f.hom (pointsMap B S hS X.1 f.hom x)) :
    (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
        IsAssociatedOnSomeSchemeChartFibre B S hS f F x) ∧
      (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
        IsAssociatedOnEverySchemeChartFibre B S hS f F x) ∧
      (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
        IsAssociatedOnSomeEtaleChartSquare B S hS f F x) ∧
      (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
        IsAssociatedOnEveryEtaleChartSquare B S hS f F x) ∧
      ∀ (p₀ : FieldValuedPoint B S hS Y.1) [Mono (fieldMorphism B S hS Y.1 p₀)],
        p₀.class B S hS Y.1 = pointsMap B S hS X.1 f.hom x →
        ∀ x₀ : points B S hS (fibreAtFieldValuedPoint B S hS f p₀).1,
          pointsMap B S hS (fibreAtFieldValuedPoint B S hS f p₀).1
              (fibreAtFieldValuedPointProjection B S hS f p₀).hom x₀ = x →
            (IsRelativeWeaklyAssociatedPoint B S hS f F x ↔
              IsAssociatedPoint B S hS (fibreAtFieldValuedPoint B S hS f p₀)
                ((modulePullback B S hS (fibreAtFieldValuedPointProjection B S hS f p₀)).obj F)
                x₀)
```

## Tag 0CV0, a definition

[Tag 0CV0](https://stacks.math.columbia.edu/tag/0CV0) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeWeaklyAssociatedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityCriterion.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityCriterion.lean#L124). The attribute's comment: “the membership predicate, via condition (5) of 0CUZ; stated for every module, not only a quasi-coherent one”.

> A point `x` of `X` lies in the relative weak assassin `WeakAss_{X/Y}(F)` of an `𝒪_X`-module
> `F` along a morphism `f : X ⟶ Y` of algebraic spaces: for some field-valued representative of
> the image of `x` in `Y`, the fibre of `f` over that representative carries a point above `x`
> which is weakly associated to the restriction of `F` to the fibre.
>
> This is condition (5) of Stacks 0CUZ, the field-valued one. When the fibres of `f` are locally
> Noetherian — for instance when `f` is locally of finite type, by Stacks 0CUY — this set is
> also written `Ass_{X/Y}(F)`.

```lean
noncomputable def IsRelativeWeaklyAssociatedPoint {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (x : points B S hS X.1) : Prop
```

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityCriterion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Flat/PurityCriterion.lean#L138). The attribute's comment: “the set WeakAss\_\{X/Y}(F), which under locally Noetherian fibres is Ass\_\{X/Y}(F)”.

> The relative weak assassin `WeakAss_{X/Y}(F) ⊆ |X|` of an `𝒪_X`-module along a morphism of
> algebraic spaces. When the fibres of `f` are locally Noetherian this is the set written
> `Ass_{X/Y}(F)`.

```lean
noncomputable abbrev relativeWeaklyAssociatedPoints {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) : Set (points B S hS X.1)
```

## Tag 0CV1, a lemma

[Tag 0CV1](https://stacks.math.columbia.edu/tag/0CV1) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_tensor_modulePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceTensorPullbackLocallyNoetherian.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceTensorPullbackLocallyNoetherian.lean#L204).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, let `𝓕` be a
> quasi-coherent `𝒪_X`-module and `𝓖` a quasi-coherent `𝒪_Y`-module. Assume `𝓕` is flat over `Y`,
> that `X` and `Y` are locally Noetherian and that the fibres of `f` are locally Noetherian. Then
>
> `Ass_X(𝓕 ⊗_{𝒪_X} f^*𝓖) = {x ∈ Ass_{X/Y}(𝓕) such that f(x) ∈ Ass_Y(𝓖)}`,
>
> where `Ass` and `Ass_{X/Y}` are `AlgebraicGeometry.Space.weaklyAssociatedPoints` and
> `AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints`.

```lean
theorem weaklyAssociatedPoints_tensor_modulePullback_eq (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (G : Modules.{u, u} B S hS Y.1 Y.2)
    [hFqc : F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite]
    (hF : IsFlatOver B S hS X.2 f.hom F)
    (hLNX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hLNY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hfib : HasLocallyNoetherianFibersAtPoints B S hS f.hom) :
    weaklyAssociatedPoints B S hS X (F ⊗ (modulePullback B S hS f).obj G) =
      {x | x ∈ relativeWeaklyAssociatedPoints B S hS f F ∧
        pointsMap B S hS X.1 f.hom x ∈ weaklyAssociatedPoints B S hS Y G}
```

## Tag 0CV2, a lemma

[Tag 0CV2](https://stacks.math.columbia.edu/tag/0CV2) in the Stacks Project.

**`AlgebraicGeometry.Space.isRelativeWeaklyAssociatedPoint_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean#L199). The attribute's comment: “part (1), for the relative weak assassin of Stacks 0CV0 and with no finiteness hypothesis on f, which part (1) does not use: the two fibres are identified outright by pasting the cartesian squares”.

> In a cartesian square of algebraic spaces over `S` with vertical morphisms `f : X ⟶ Y` and
> `f' : X' ⟶ Y'` and horizontal morphisms `g : Y' ⟶ Y` and `g' : X' ⟶ X`, and for an
> `𝒪_X`-module `F` with `F' = (g')^*F`, the image under `g'` of a point of `WeakAss_{X'/Y'}(F')`
> lies in `WeakAss_{X/Y}(F)`.

```lean
theorem isRelativeWeaklyAssociatedPoint_of_baseChange
    (sq : IsPullback g'.hom f'.hom f.hom g.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    {x' : points B S hS X'.1}
    (hx' : IsRelativeWeaklyAssociatedPoint B S hS f' ((modulePullback B S hS g').obj F) x') :
    IsRelativeWeaklyAssociatedPoint B S hS f F (pointsMap B S hS X'.1 g'.hom x')
```

**`AlgebraicGeometry.Space.exists_isRelativeWeaklyAssociatedPoint_baseChange_of_pointsMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChange.lean#L252). The attribute's comment: “part (2), for the relative weak assassin of Stacks 0CV0 and with no finiteness hypothesis on f, which the proof does not use: in place of the source's appeal to Stacks 05DC the witness is carried to a representative coming from y' by the ascent of weak association along the flat surjective base change identifying the two fibres”.

> In a cartesian square of algebraic spaces over `S` with vertical morphisms `f : X ⟶ Y` and
> `f' : X' ⟶ Y'` and horizontal morphisms `g : Y' ⟶ Y` and `g' : X' ⟶ X`, and for a
> quasi-coherent `𝒪_X`-module `F` with `F' = (g')^*F`: for every point `x` of `WeakAss_{X/Y}(F)`
> and every point `y'` of `Y'` whose image in `Y` is the image of `x`, there is a point of
> `WeakAss_{X'/Y'}(F')` whose image under `g'` is `x` and whose image under `f'` is `y'`.

```lean
theorem exists_isRelativeWeaklyAssociatedPoint_baseChange_of_pointsMap_eq
    (sq : IsPullback g'.hom f'.hom f.hom g.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) {x : points B S hS X.1} {y' : points B S hS Y'.1}
    (hx : IsRelativeWeaklyAssociatedPoint B S hS f F x)
    (hy' : pointsMap B S hS Y'.1 g.hom y' = pointsMap B S hS X.1 f.hom x) :
    ∃ x' : points B S hS X'.1,
      IsRelativeWeaklyAssociatedPoint B S hS f' ((modulePullback B S hS g').obj F) x' ∧
        pointsMap B S hS X'.1 g'.hom x' = x ∧
          pointsMap B S hS X'.1 f'.hom x' = y'
```

## Tag 0CV3, a lemma

[Tag 0CV3](https://stacks.math.columbia.edu/tag/0CV3) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_modulePullback_eq_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChangePreimage.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceBaseChangePreimage.lean#L351).

> Let
>
> ```
> X' --g'--> X
> |f'        |f
> Y' --g---> Y
> ```
>
> be a cartesian square of algebraic spaces over `S`, let `F` be a quasi-coherent `𝒪_X`-module and
> put `F' = (g')^*F`. Assume that `f` is locally of finite type and that for every `y' ∈ |Y'|` the
> transcendence degree of `y'/g(y')` is `0` (Stacks 04NM). Then the relative weak assassin
> `WeakAss_{X'/Y'}(F')` of Stacks 0CV0 is the inverse image of `WeakAss_{X/Y}(F)` under `|g'|`.

```lean
theorem relativeWeaklyAssociatedPoints_modulePullback_eq_preimage
    (sq : IsPullback g'.hom f'.hom f.hom g.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (f_lft : IsLocallyOfFiniteType B S hS f.hom)
    (g_trdeg : ∀ y' : points B S hS Y'.1, HasTranscendenceDegreeAt B S hS g.hom y' 0) :
    relativeWeaklyAssociatedPoints B S hS f' ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' relativeWeaklyAssociatedPoints B S hS f F
```

## Tag 0CV4, a lemma

[Tag 0CV4](https://stacks.math.columbia.edu/tag/0CV4) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeWeaklyAssociatedPoints_modulePushforward_eq_image_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteDirectImage.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceFiniteDirectImage.lean#L226).

> **The relative weak assassin of a finite direct image.** Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over a scheme `S`, let `i : Z ⟶ X` be a finite morphism and let `G` be a
> quasi-coherent `𝒪_Z`-module. Then the relative weak assassin `WeakAss_{X/Y}(i_*G)` is the image
> under `i` of `WeakAss_{Z/Y}(G)`.

```lean
theorem relativeWeaklyAssociatedPoints_modulePushforward_eq_image_of_isFinite
    (f : X ⟶ Y) (i : Z ⟶ X)
    (hi : IsFinite B S hS i.hom) (G : Modules.{u, u} B S hS Z.1 Z.2)
    (hG : G.IsQuasicoherentOnSite) :
    relativeWeaklyAssociatedPoints B S hS f ((modulePushforward B S hS i).obj G) =
      pointsMap B S hS Z.1 i.hom '' relativeWeaklyAssociatedPoints B S hS (i ≫ f) G
```

## Tag 0CVV, a lemma

[Tag 0CVV](https://stacks.math.columbia.edu/tag/0CVV) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyConstructible_relativeAssassinContainmentLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/RepresentedFibreComparison.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/RepresentedFibreComparison.lean#L625). The attribute's comment: “the surjective etale scheme chart of X is a hypothesis rather than a construction, and so are the transfers along it of quasi-compactness and quasi-separatedness of alpha, of finite presentation of the chart restriction of F, and of quasi-compactness of U over V”.

> Let `V` be a scheme of the site, let `f : X ⟶ schemeSpace V` be a morphism of algebraic
> spaces which is locally of finite presentation, let `F` be a quasi-coherent `𝒪_X`-module and let
> `U` be an open subset of `|X|`. Let `φ : schemeSpace W ⟶ X` be a surjective étale scheme chart
> and `α : W ⟶ V` a quasi-compact and quasi-separated morphism of the site with
> `φ ≫ f = schemeSpaceMap α`, such that the chart restriction of `F` is of finite presentation
> and `φ⁻¹(U)` is quasi-compact over `V`. Then the set of points `y` of `V` over which every point
> of the relative assassin of `F` above `y` lies in `U` is locally constructible in `V`.

```lean
theorem isLocallyConstructible_relativeAssassinContainmentLocus
    {X : AlgebraicSpaces B S hS} (V W : BigFppfOver B S hS)
    (f : X ⟶ schemeSpace V) (F : Modules.{u, u} B S hS X.1 X.2)
    (U : Set (points B S hS X.1)) (hUopen : @IsOpen _ (pointTopology B S hS X.1) U)
    (φ : schemeSpace W ⟶ X)
    (hφ : IsEtale B S hS φ.hom)
    (hsurj : Function.Surjective (pointsMap B S hS (schemeSpace W).1 φ.hom))
    (α : W ⟶ V) (hα : φ ≫ f = schemeSpaceMap α)
    (hfX : IsLocallyOfFinitePresentation B S hS f.hom)
    (hαqc : QuasiCompact ((BigFppfOver.toScheme B S hS).map α))
    (hαqs : QuasiSeparated ((BigFppfOver.toScheme B S hS).map α))
    (hF : F.IsQuasicoherentOnSite)
    (hGfp : (baseChangeModule B S hS F W φ.hom).IsFinitePresentation)
    (hUqc : QuasiCompact ((chartOpenOfOpenPoints B S hS W φ U hUopen).ι ≫
      (BigFppfOver.toScheme B S hS).map α)) :
    IsLocallyConstructible (relativeAssassinContainmentLocus B S hS V f F U)
```

**`AlgebraicGeometry.Space.isLocallyConstructible_relativeAssassinContainmentLocus_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceContainmentGeneralBase.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceContainmentGeneralBase.lean#L166). The attribute's comment: “with `U → V` quasi-compact read on the point sets”.

> Let `V` be a scheme of the site, let `X` be an algebraic space of finite presentation over `V`,
> let `F` be a quasi-coherent `𝒪_X`-module of finite presentation and let `U` be an open subset of
> `|X|` whose map to `|V|` is quasi-compact. Then the set of points of `V` over which every point of
> the relative assassin of `F` above that point lies in `U` is locally constructible.
>
> Here `hUqc` is the point-level reading of "`U → V` is quasi-compact": the part of `U` lying over
> a quasi-compact open of `|V|` is quasi-compact.

```lean
theorem isLocallyConstructible_relativeAssassinContainmentLocus_of_isFinitePresentation
    {X : AlgebraicSpaces B S hS} (V : BigFppfOver B S hS)
    (f : X ⟶ schemeSpace V) (hf : IsFinitePresentation B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite F)
    (U : Set (points B S hS X.1)) (hUopen : IsOpen U)
    (hUqc : ∀ A : ((BigFppfOver.toScheme B S hS).obj V).Opens,
      IsCompact (A : Set ((BigFppfOver.toScheme B S hS).obj V)) →
      IsCompact (U ∩ (fun x =>
          schemeSpacePointToScheme B S hS V (pointsMap B S hS X.1 f.hom x)) ⁻¹'
        (A : Set ((BigFppfOver.toScheme B S hS).obj V)))) :
    IsLocallyConstructible (relativeAssassinContainmentLocus B S hS V f F U)
```

**`AlgebraicGeometry.Space.isLocallyConstructible_relativeAssassinContainmentLocus_of_isQuasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceContainmentGeneralBase.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/MorphismWeaklyAssociated/SpaceContainmentGeneralBase.lean#L246).

> Let `V` be a scheme of the site, let `X` be an algebraic space of finite presentation over `V`,
> let `F` be a quasi-coherent `𝒪_X`-module of finite presentation and let `U ⊆ X` be an open subspace
> whose morphism to `V` is quasi-compact. Then the set of points of `V` over which every point of the
> relative assassin of `F` above that point lies in `U` is locally constructible.

```lean
theorem isLocallyConstructible_relativeAssassinContainmentLocus_of_isQuasiCompact
    {X : AlgebraicSpaces B S hS} (V : BigFppfOver B S hS)
    (f : X ⟶ schemeSpace V) (hf : IsFinitePresentation B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite F)
    (U : Subfunctor X.1) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompact B S hS (U.ι ≫ f.hom)) :
    IsLocallyConstructible (relativeAssassinContainmentLocus B S hS V f F
      (Set.range (pointsMap B S hS U.toFunctor U.ι)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.4, Tag 0CUV](https://stacks.math.columbia.edu/tag/0CUV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
