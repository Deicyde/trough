---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasFiberLocalRingDimension, AlgebraicGeometry.Space.HasRelativeDimensionAt, AlgebraicGeometry.Space.HasTranscendenceDegreeAt, AlgebraicGeometry.Space.HasRelativeDimensionLE, AlgebraicGeometry.Space.HasRelativeDimension, AlgebraicGeometry.Space.hasTranscendenceDegreeAt_comp_iff_of_isLocallyQuasiFinite, AlgebraicGeometry.Space.hasTranscendenceDegreeAt_zero_of_isFiniteTypePoint, AlgebraicGeometry.Space.dimensionAtPoint_eq_add_of_hasRelativeDimension
statement: formalized
proof: formalized
---

# 67.33 Relative dimension

Section 67.33 of the Stacks Project, [Tag 04NH](https://stacks.math.columbia.edu/tag/04NH). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04NM, a definition

[Tag 04NM](https://stacks.math.columbia.edu/tag/04NM) in the Stacks Project.

**`AlgebraicGeometry.Space.HasFiberLocalRingDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean#L81). The attribute's comment: “local\_ring\_fibre\_dimension”.

> **Stacks 04NM, dimension of the local ring of a fibre.** The local ring of the fibre of
> `f` has dimension `d` at `x`, tested on every étale chart at `x`.

```lean
abbrev HasFiberLocalRingDimension (d : ℕ∞) (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hF : IsAlgebraicSpace B S hS F) (_hG : IsAlgebraicSpace B S hS G)
    (f : F ⟶ G) (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasRelativeDimensionAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean#L92). The attribute's comment: “relative\_dimension\_at\_point”.

> **Stacks 04NM, relative dimension at a point.** A morphism of algebraic spaces has
> relative dimension `d` at `x` if its fibre has dimension `d` at the corresponding point in
> every étale chart.

```lean
abbrev HasRelativeDimensionAt (d : ℕ∞) (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : F ⟶ G) (x : points B S hS F) : Prop
```

**`AlgebraicGeometry.Space.HasTranscendenceDegreeAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionAtPoint.lean#L101). The attribute's comment: “transcendence\_degree”.

> **Stacks 04NM, transcendence degree at a point.** The transcendence degree of `x` over
> its image under `f` is `r`. For algebraic spaces this is equivalently tested on one or every
> étale scheme chart at `x`.

```lean
abbrev HasTranscendenceDegreeAt (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) (x : points B S hS F) (r : ℕ∞) :
    Prop
```

## Tag 06LR, a definition

[Tag 06LR](https://stacks.math.columbia.edu/tag/06LR) in the Stacks Project.

**`AlgebraicGeometry.Space.HasRelativeDimensionLE`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean#L150). The attribute's comment: “part (1): relative dimension at most d”.

> **Stacks 06LR, part (1).** A morphism of algebraic spaces has *relative dimension `≤ d`*
> if it has relative dimension `≤ d` at every point of its source.

```lean
abbrev HasRelativeDimensionLE (d : ℕ) (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.HasRelativeDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean#L157). The attribute's comment: “part (2): relative dimension d”.

> **Stacks 06LR, part (2).** A morphism of algebraic spaces has *relative dimension `d`* if
> it has relative dimension `d` at every point of its source.

```lean
abbrev HasRelativeDimension (d : ℕ) (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G) : Prop
```

## Tag 06RX, a lemma

[Tag 06RX](https://stacks.math.columbia.edu/tag/06RX) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTranscendenceDegreeAt_comp_iff_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean#L363).

> **Stacks 06RX.** Let `X ⟶ Y ⟶ Z` be morphisms of algebraic spaces over `S` with `X ⟶ Y`
> locally quasi-finite, and let `x` be a point of `X`. The transcendence degree of `x` over its
> image in `Z` is the transcendence degree of the image of `x` in `Y` over that same point: on
> compatible étale charts the first morphism becomes a locally quasi-finite morphism of schemes,
> which contributes a finite residue-field extension and so no transcendence degree.

```lean
theorem hasTranscendenceDegreeAt_comp_iff_of_isLocallyQuasiFinite
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocallyQuasiFinite B S hS f) (x : points B S hS X) (r : ℕ∞) :
    HasTranscendenceDegreeAt B S hS (f ≫ g) x r ↔
      HasTranscendenceDegreeAt B S hS g (pointsMap B S hS X f x) r
```

## Tag 0ECY, a lemma

[Tag 0ECY](https://stacks.math.columbia.edu/tag/0ECY) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTranscendenceDegreeAt_zero_of_isFiniteTypePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean#L409).

> **Stacks 0ECY.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, with `Y` Jacobson. Then the transcendence degree of a finite type
> point `x` of `X` over its image is zero.
>
> The Jacobson hypothesis is the étale-local property of Tag 03E6 for `JacobsonSpace`, written
> out as one surjective étale atlas by a Jacobson scheme.

```lean
theorem hasTranscendenceDegreeAt_zero_of_isFiniteTypePoint
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (hJac : ∃ (V : BigFppfOver B S hS) (b : yoneda.obj V ⟶ Y),
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) b ∧
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) b ∧
      JacobsonSpace ((BigFppfOver.toScheme B S hS).obj V))
    (x : points B S hS X) (hx : IsFiniteTypePoint B S hS X x) :
    HasTranscendenceDegreeAt B S hS f x 0
```

## Tag 0AFH, a lemma

[Tag 0AFH](https://stacks.math.columbia.edu/tag/0AFH) in the Stacks Project.

**`AlgebraicGeometry.Space.dimensionAtPoint_eq_add_of_hasRelativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/RelativeDimension.lean#L500).

> **Stacks 0AFH.** Let `f : X ⟶ Y` be a morphism of locally Noetherian algebraic spaces over
> `S` which is flat, locally of finite type and of relative dimension `d`. Then for every point
> `x` of `X` with image `y` in `Y` we have `dim_x(X) = dim_y(Y) + d`.
>
> Local Noetherianity of an algebraic space is the étale-local property of Tag 03E6 for
> `AlgebraicGeometry.IsLocallyNoetherian`, as in
> `StacksFrontier/AlgebraicGeometry/Spaces/NoetherianSpaces.lean`. The source is assumed locally
> Noetherian, as in the statement of the tag, but the hypothesis is not used: by Tag 04ZK it
> follows from local Noetherianity of the target and local finite type of `f`, which is how the
> chart of the source is seen to be locally Noetherian below.
>
> The proof reduces everything to one commuting square of surjective étale charts `α : U ⟶ V`
> over `f`, obtained by Tag 02X1 from the locally Noetherian atlas of the target. The induced
> morphism of schemes is flat and locally of finite type, being the chart morphism of a flat
> morphism locally of finite type, and its source is locally Noetherian because its target is.
> It has relative dimension `d` in the scheme sense of part (3) of Tag 02NJ: the pointed chart
> built from the canonical field-valued representative of a point `w` of `U` reads the relative
> dimension of `f` above `w` as the local dimension of the fibre of the chart morphism through
> `w`, so that local dimension is `d` at every point of `U`, and constant local fibre dimension
> over a field gives equidimensional fibres of dimension `d`. The dimension formula for the
> chart morphism is then Tag 0AFE, and its two sides are the dimensions of the two algebraic
> spaces at the corresponding points, by the chart independence of Tag 04N5.

```lean
theorem dimensionAtPoint_eq_add_of_hasRelativeDimension
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hNX : HasEtaleLocalProperty B S hS X (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (hNY : HasEtaleLocalProperty B S hS Y (fun Z : Scheme.{u} => IsLocallyNoetherian Z))
    (f : X ⟶ Y) (hflat : IsFlat B S hS f) (hft : IsLocallyOfFiniteType B S hS f)
    {d : ℕ} (hdim : HasRelativeDimension d B S hS f) (x : points B S hS X) :
    dimensionAtPoint B S hS X hX x =
      dimensionAtPoint B S hS Y hY (pointsMap B S hS X f x) + (d : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.33, Tag 04NH](https://stacks.math.columbia.edu/tag/04NH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
