---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.relativeDimensionAt_eq_fiberLocalRingDimension_add_transcendenceDegreeAt, AlgebraicGeometry.Space.hasTranscendenceDegreeAt_comp, AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_le_add, AlgebraicGeometry.Space.exists_hasRelativeDimensionAt_comp_le_add, AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_of_isFlatAt, AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_of_isFlatAt_fibre, AlgebraicGeometry.Space.hasRelativeDimensionAt_iff_of_isPullback, AlgebraicGeometry.Space.exists_fiberLocalRingDimension_add_eq_of_isPullback
statement: formalized
proof: formalized
---

# 67.34 Morphisms and dimensions of fibres

Section 67.34 of the Stacks Project, [Tag 04NP](https://stacks.math.columbia.edu/tag/04NP). 8 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04NQ, a lemma

[Tag 04NQ](https://stacks.math.columbia.edu/tag/04NQ) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeDimensionAt_eq_fiberLocalRingDimension_add_transcendenceDegreeAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L313).

> **Stacks 04NQ.** For a morphism of algebraic spaces over `S` which is locally of finite
> type, the relative dimension at a point is the dimension of the local ring of the fibre there
> plus the transcendence degree of the point over its image.
>
> The three invariants of Stacks 04NM are chart conditions, so all three are read off one pointed
> étale chart at the point (Stacks 04NC); on the resulting morphism of schemes the identity is
> the dimension formula of Stacks 02FX.

```lean
theorem relativeDimensionAt_eq_fiberLocalRingDimension_add_transcendenceDegreeAt
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (f : F ⟶ G) (x : points B S hS F) (hf : IsLocallyOfFiniteType B S hS f)
    (d e r : ℕ∞) (hd : HasRelativeDimensionAt d B S hS f x)
    (he : HasFiberLocalRingDimension e B S hS hF hG f x)
    (hr : HasTranscendenceDegreeAt B S hS f x r) : d = e + r
```

## Tag 04NR, a lemma

[Tag 04NR](https://stacks.math.columbia.edu/tag/04NR) in the Stacks Project.

**`AlgebraicGeometry.Space.hasTranscendenceDegreeAt_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L354). The attribute's comment: “part (3): additivity of the transcendence degree”.

> **Additivity of the transcendence degree at a point**, part (3) of Stacks 04NR. For
> composable morphisms `f : X ⟶ Y` and `g : Y ⟶ Z` of algebraic spaces over `S` and a point `x`
> of `X`, the transcendence degree of `x` over its image under `f ≫ g` is the sum of the
> transcendence degree of `x` over `f x` and of `f x` over `g (f x)`.
>
> Compatible étale charts for the composite
> (`AlgebraicGeometry.Space.exists_compatible_etale_charts_comp`) read all three transcendence
> degrees on a single commuting pair of chart morphisms `α` and `β` of the site; on the resulting
> morphisms of schemes the three residue fields form a tower and the transcendence degree of a
> tower is additive.
>
> The source assumes `f` and `g` locally of finite type; that is not needed, neither for the
> chart comparison nor for the tower identity.

```lean
theorem hasTranscendenceDegreeAt_comp {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (x : points B S hS X)
    (r s : ℕ∞) (hr : HasTranscendenceDegreeAt B S hS f x r)
    (hs : HasTranscendenceDegreeAt B S hS g (pointsMap B S hS X f x) s) :
    HasTranscendenceDegreeAt B S hS (f ≫ g) x (r + s)
```

**`AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_le_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L477). The attribute's comment: “part (1): the relative dimension of a composite is at most the sum”.

> **Stacks 04NR, part (1).** For composable morphisms of algebraic spaces over `S` which are
> locally of finite type, the relative dimension of the composite at a point is at most the sum of
> the relative dimension of the first morphism there and of the second morphism at the image
> point.
>
> Compatible étale charts for the composite read all three relative dimensions as fibre
> dimensions of a pair of composable morphisms of schemes at one point, where the inequality is
> part of Stacks 02JS.

```lean
theorem hasRelativeDimensionAt_comp_le_add {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (x : points B S hS X)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) (d e n : ℕ∞)
    (hd : HasRelativeDimensionAt d B S hS f x)
    (he : HasRelativeDimensionAt e B S hS g (pointsMap B S hS X f x))
    (hn : HasRelativeDimensionAt n B S hS (f ≫ g) x) : n ≤ d + e
```

**`AlgebraicGeometry.Space.exists_hasRelativeDimensionAt_comp_le_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L500). The attribute's comment: “part (1): the relative dimension of a composite is at most the sum”.

> **Stacks 04NR, part (1).** The composite of two morphisms of algebraic spaces over `S` which
> are locally of finite type has a relative dimension at every point of its source, and that
> dimension is at most the sum of the relative dimensions of the two factors.

```lean
theorem exists_hasRelativeDimensionAt_comp_le_add {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (x : points B S hS X)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) (d e : ℕ∞)
    (hd : HasRelativeDimensionAt d B S hS f x)
    (he : HasRelativeDimensionAt e B S hS g (pointsMap B S hS X f x)) :
    ∃ n : ℕ∞, HasRelativeDimensionAt n B S hS (f ≫ g) x ∧ n ≤ d + e
```

**`AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L517). The attribute's comment: “part (2): equality when the first morphism is flat at the point”.

> **Stacks 04NR, part (2), special case.** The inequality of part (1) is an equality as soon as
> the first morphism is flat at the point.
>
> On compatible étale charts for the composite this is the corresponding part of Stacks 02JS,
> flatness of `f` at `x` becoming flatness of the first chart morphism at the selected scheme
> point.

```lean
theorem hasRelativeDimensionAt_comp_of_isFlatAt {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (x : points B S hS X)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) (d e : ℕ∞)
    (hd : HasRelativeDimensionAt d B S hS f x)
    (he : HasRelativeDimensionAt e B S hS g (pointsMap B S hS X f x))
    (hflat : IsFlatAt B S hS f x) :
    HasRelativeDimensionAt (d + e) B S hS (f ≫ g) x
```

**`AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_of_isFlatAt_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1057). The attribute's comment: “part (2): equality when the morphism of field-valued fibres is flat”.

> **Stacks 04NR, part (2).** The inequality of part (1) is an equality as soon as the morphism
> of field-valued fibres over the image point is flat at a point above `x`: here `Xk` and `Yk` are
> the fibres of `X` and `Y` over a field-valued representative `p` of the image of `x` in `Z`,
> presented by the two cartesian squares, `x'` is a point of `Xk` above `x`, and `Xk ⟶ Yk` is flat
> at `x'`.
>
> Relative dimension is invariant under base change (part (1) of Stacks 04NS), so all three
> relative dimensions may be read on the fibres over `p`, where the first morphism is flat at the
> chosen point and `AlgebraicGeometry.Space.hasRelativeDimensionAt_comp_of_isFlatAt` applies. The
> fibres are algebraic because they are fibre products of algebraic spaces (Stacks 02X2), and the
> two morphisms between them are locally of finite type because being so is stable under base
> change (Stacks 03XH).
>
> No chosen fibre-product objects are imposed: the two squares are cartesian squares of arbitrary
> presheaves, which is why neither fibre is assumed algebraic.

```lean
theorem hasRelativeDimensionAt_comp_of_isFlatAt_fibre
    {X Y Z Xk Yk : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z) (x : points B S hS X)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g) (d e : ℕ∞)
    (hd : HasRelativeDimensionAt d B S hS f x)
    (he : HasRelativeDimensionAt e B S hS g (pointsMap B S hS X f x))
    (p : FieldValuedPoint B S hS Z) (px : Xk ⟶ X) (py : Yk ⟶ Y)
    (qy : Yk ⟶ yoneda.obj (p.siteObject B S hS Z)) (fk : Xk ⟶ Yk) (x' : points B S hS Xk)
    (hpx : IsPullback px fk f py)
    (hpy : IsPullback py qy g (yonedaEquiv.symm p.value))
    (hx : pointsMap B S hS Xk px x' = x) (hflat : IsFlatAt B S hS fk x') :
    HasRelativeDimensionAt (d + e) B S hS (f ≫ g) x
```

## Tag 04NS, a lemma

[Tag 04NS](https://stacks.math.columbia.edu/tag/04NS) in the Stacks Project.

**`AlgebraicGeometry.Space.hasRelativeDimensionAt_iff_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L686). The attribute's comment: “part (1): invariance of the relative dimension under base change”.

> **Invariance of relative dimension under base change**, part (1) of Stacks 04NS. In a
> cartesian square of algebraic spaces over `S` whose right vertical arrow `f` is locally of
> finite type, the relative dimension of the base change `f'` at a point `x'` of its source is
> the relative dimension of `f` at the image of `x'`.
>
> Read on the compatible pointed charts of
> `AlgebraicGeometry.Space.exists_etaleChartAtPoint_pair_of_isPullback`, each side is the
> dimension of the fibre of a morphism of schemes at corresponding points of a cartesian square,
> which is part (1) of Stacks 02FY.
>
> The source assumes all four corners of the square algebraic; the fourth corner `X'` need not
> be, because the two chart conditions are compared on charts supplied as data rather than on
> charts produced from an atlas.

```lean
theorem hasRelativeDimensionAt_iff_of_isPullback {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX : IsAlgebraicSpace B S hS X) (hY' : IsAlgebraicSpace B S hS Y')
    (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x' : points B S hS X') (d : ℕ∞) :
    HasRelativeDimensionAt d B S hS f (pointsMap B S hS X' g' x') ↔
      HasRelativeDimensionAt d B S hS f' x'
```

**`AlgebraicGeometry.Space.exists_fiberLocalRingDimension_add_eq_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L784). The attribute's comment: “part (2): the gain in the dimension of the local ring of the fibre is the loss in transcendence degree”.

> **Part (2) of Stacks 04NS.** In a cartesian square of algebraic spaces over `S` whose right
> vertical arrow `f` is locally of finite type, the dimension gained by the local ring of the
> fibre at a point `x'` of the source of the base change, over its value for `f` at the image of
> `x'`, is the transcendence degree lost there; in particular the common difference is
> nonnegative, which is why it is recorded as a summand `n` rather than as a difference.
>
> The transcendence degrees are compared on the compatible pointed charts of
> `AlgebraicGeometry.Space.exists_etaleChartAtPoint_pair_of_isPullback`, where the drop is part
> (2) of Stacks 02FY for the resulting cartesian square of schemes; the sum of the two invariants
> is the relative dimension (Stacks 04NQ) and so agrees on the two sides by part (1) of Stacks
> 04NS, which turns that drop into the gain of the other invariant. The transcendence degree at
> `x'` is finite, so it cancels.

```lean
theorem exists_fiberLocalRingDimension_add_eq_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x' : points B S hS X') (e r e' r' : ℕ∞)
    (he : HasFiberLocalRingDimension e B S hS hX hY f (pointsMap B S hS X' g' x'))
    (hr : HasTranscendenceDegreeAt B S hS f (pointsMap B S hS X' g' x') r)
    (he' : HasFiberLocalRingDimension e' B S hS hX' hY' f' x')
    (hr' : HasTranscendenceDegreeAt B S hS f' x' r') :
    ∃ n : ℕ∞, e + n = e' ∧ r' + n = r
```

**`AlgebraicGeometry.Space.fiberLocalRingDimension_le_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 832](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L832). The attribute's comment: “part (2): the dimension of the local ring of the fibre does not decrease”.

> **Part (2) of Stacks 04NS.** Base change does not decrease the dimension of the local ring
> of the fibre at a point.

```lean
theorem fiberLocalRingDimension_le_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x' : points B S hS X') (e r e' r' : ℕ∞)
    (he : HasFiberLocalRingDimension e B S hS hX hY f (pointsMap B S hS X' g' x'))
    (hr : HasTranscendenceDegreeAt B S hS f (pointsMap B S hS X' g' x') r)
    (he' : HasFiberLocalRingDimension e' B S hS hX' hY' f' x')
    (hr' : HasTranscendenceDegreeAt B S hS f' x' r') : e ≤ e'
```

**`AlgebraicGeometry.Space.transcendenceDegreeAt_le_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L850). The attribute's comment: “part (2): the transcendence degree does not increase”.

> **Part (2) of Stacks 04NS.** Base change does not increase the transcendence degree of a
> point over its image.

```lean
theorem transcendenceDegreeAt_le_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x' : points B S hS X') (e r e' r' : ℕ∞)
    (he : HasFiberLocalRingDimension e B S hS hX hY f (pointsMap B S hS X' g' x'))
    (hr : HasTranscendenceDegreeAt B S hS f (pointsMap B S hS X' g' x') r)
    (he' : HasFiberLocalRingDimension e' B S hS hX' hY' f' x')
    (hr' : HasTranscendenceDegreeAt B S hS f' x' r') : r' ≤ r
```

**`AlgebraicGeometry.Space.exists_point_preserving_fiberLocalRingDimension_and_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 890](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L890). The attribute's comment: “part (3): a common lift at which both invariants are preserved”.

> **Part (3) of Stacks 04NS.** In a cartesian square of algebraic spaces over `S` whose right
> vertical arrow `f` is locally of finite type, a point `x` of `X` and a point `y'` of `Y'` with
> the same image in `Y` have a common lift `x'` to `X'` at which the dimension of the local ring
> of the fibre and the transcendence degree both take the value they take at `x` — that is, at
> which the common difference of part (2) vanishes.
>
> Some common lift exists because the point set of a fibre product surjects onto the fibre product
> of the point sets (Stacks 03H4). On the compatible pointed charts at such a lift
> (`AlgebraicGeometry.Space.exists_etaleChartAtPoint_pair_of_isPullback`) part (3) of Stacks 02FY
> replaces the scheme point selected by the chart of the base change by one lying over the same
> two points at which both invariants are preserved; the same chart with that point as its
> representative is a pointed chart at its image in `X'`, and that image is the required lift,
> because the two source charts commute with the horizontal arrow of the square.

```lean
theorem exists_point_preserving_fiberLocalRingDimension_and_trdeg
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (x : points B S hS X) (y' : points B S hS Y')
    (hxy : pointsMap B S hS X f x = pointsMap B S hS Y' g y') :
    ∃ x' : points B S hS X', pointsMap B S hS X' g' x' = x ∧
      pointsMap B S hS X' f' x' = y' ∧
      (∀ d : ℕ∞, HasFiberLocalRingDimension d B S hS hX hY f x ↔
        HasFiberLocalRingDimension d B S hS hX' hY' f' x') ∧
      (∀ r : ℕ∞, HasTranscendenceDegreeAt B S hS f x r ↔
        HasTranscendenceDegreeAt B S hS f' x' r)
```

**`AlgebraicGeometry.Space.hasRelativeDimensionAt_iff_of_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionBaseChange.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionBaseChange.lean#L167). The attribute's comment: “part (1)”.

> In a cartesian square of algebraic spaces over `S` with `f` locally of finite type, the
> relative dimension of the base change of `f` at a point of its source is the relative dimension of
> `f` at the image of that point.
>
> The square is the one with `p` over `f` and `q` over `g`, so `p : W ⟶ Z` is the base change of
> `f : X ⟶ Y` and `q : W ⟶ X` is the projection. Only `X`, `Y` and `Z` are assumed to be algebraic
> spaces.

```lean
theorem hasRelativeDimensionAt_iff_of_isPullback' (d : ℕ∞)
    {W X Z Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (hf : IsLocallyOfFiniteType B S hS f)
    (x' : points B S hS W) :
    HasRelativeDimensionAt d B S hS p x' ↔
      HasRelativeDimensionAt d B S hS f (pointsMap B S hS W q x')
```

## Tag 04NT, a lemma

[Tag 04NT](https://stacks.math.columbia.edu/tag/04NT) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_setOf_hasRelativeDimensionAt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionOpenness.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionOpenness.lean#L55).

> For a morphism of algebraic spaces over `S` which is locally of finite type, the set of
> points of the source at which the relative dimension is at most `n` is open.

```lean
theorem isOpen_setOf_hasRelativeDimensionAt_le (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f)
    (n : ℕ) :
    IsOpen {x : points B S hS F |
      ∃ d : ℕ∞, d ≤ (n : ℕ∞) ∧ HasRelativeDimensionAt d B S hS f x}
```

## Tag 04NU, a lemma

[Tag 04NU](https://stacks.math.columbia.edu/tag/04NU) in the Stacks Project.

**`AlgebraicGeometry.Space.isRetrocompact_setOf_exists_hasRelativeDimensionAt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1170).

> **Stacks 04NU.** For a morphism of algebraic spaces over `S` which is locally of finite
> presentation and a natural number `n`, the open set of Stacks 04NT — the points of the source
> at which the relative dimension is at most `n` — is retrocompact in the point space of Tag
> 03BU.
>
> As for Stacks 04NT, a surjective étale chart `a` of the source lifted from an atlas of the
> target reads the locus, point by point, as the bounded-fibre-dimension locus `Wₙ` of the
> induced morphism of schemes, which is retrocompact by Stacks 02G0. Points of a represented
> presheaf are homeomorphic to points of the representing scheme (Tag 03BX), so the preimage of
> the locus under `|a|` is retrocompact; transporting that to the locus itself uses that `|a|` is
> a continuous open surjection: a compact open `K` of the target is covered by the images of the
> preimages of finitely many affine opens of the chart contained in the open `|a| ⁻¹' K`, and on
> each of them the intersection with the locus is the image of a compact set.

```lean
theorem isRetrocompact_setOf_exists_hasRelativeDimensionAt_le (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsLocallyOfFinitePresentation B S hS f) (n : ℕ) :
    IsRetrocompact {x : points B S hS F |
      ∃ d : ℕ∞, d ≤ (n : ℕ∞) ∧ HasRelativeDimensionAt d B S hS f x}
```

## Tag 04NV, a lemma

[Tag 04NV](https://stacks.math.columbia.edu/tag/04NV) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_forall_hasRelativeDimensionAt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionQuasiFinite.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionQuasiFinite.lean#L60).

> A morphism `f : F ⟶ G` of presheaves over `S` on the big fppf site which is locally of finite
> type is locally quasi-finite exactly when it has relative dimension `0` at every point of its
> source. In particular this holds for a morphism of algebraic spaces over `S`.

```lean
theorem isLocallyQuasiFinite_iff_forall_hasRelativeDimensionAt_zero (f : F ⟶ G)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyQuasiFinite B S hS f ↔
      ∀ x : points B S hS F, HasRelativeDimensionAt 0 B S hS f x
```

## Tag 04NW, a lemma

[Tag 04NW](https://stacks.math.columbia.edu/tag/04NW) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyQuasiFinitePart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1275). The attribute's comment: “the canonical open subspace”.

> **Stacks 04NW, the canonical open subspace.** The open subspace of the source of a morphism
> of algebraic spaces over `S` which is locally of finite type cut out by the points of relative
> dimension `0`; it is an open subspace by Stacks 04NT and Stacks 03BZ.

```lean
noncomputable def locallyQuasiFinitePart (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f) :
    {U : Subfunctor F // IsOpenSubspace B S hS U}
```

**`AlgebraicGeometry.Space.mem_range_pointsMap_locallyQuasiFinitePart_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1286). The attribute's comment: “the points of the canonical open subspace”.

> **Stacks 04NW, the points of the canonical open subspace.** A point of the source lies in
> the point set of `AlgebraicGeometry.Space.locallyQuasiFinitePart` exactly when the relative
> dimension there is `0`.

```lean
theorem mem_range_pointsMap_locallyQuasiFinitePart_iff (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f)
    (x : points B S hS F) :
    x ∈ Set.range (pointsMap B S hS (locallyQuasiFinitePart B S hS hF hG f hf).1.toFunctor
        (locallyQuasiFinitePart B S hS hF hG f hf).1.ι) ↔
      HasRelativeDimensionAt 0 B S hS f x
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_locallyQuasiFinitePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1310). The attribute's comment: “local quasi-finiteness of the restriction”.

> **Stacks 04NW, local quasi-finiteness of the restriction.** The restriction of the morphism
> to `AlgebraicGeometry.Space.locallyQuasiFinitePart` is locally quasi-finite.
>
> Every point of the open subspace has relative dimension `0` for the restricted morphism,
> because relative dimension is unchanged by restricting the source to an open subspace, so this
> is Stacks 04NV for the restriction.

```lean
theorem isLocallyQuasiFinite_locallyQuasiFinitePart (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyQuasiFinite B S hS ((locallyQuasiFinitePart B S hS hF hG f hf).1.ι ≫ f)
```

**`AlgebraicGeometry.Space.exists_one_le_hasRelativeDimensionAt_of_not_mem_locallyQuasiFinitePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1327). The attribute's comment: “positive relative dimension outside the canonical open subspace”.

> **Stacks 04NW, positive relative dimension outside the canonical open subspace.** At a point
> of the source which is not in the point set of
> `AlgebraicGeometry.Space.locallyQuasiFinitePart` the relative dimension is at least `1`: a
> relative dimension exists there, and were it `0` the point would lie in that point set.

```lean
theorem exists_one_le_hasRelativeDimensionAt_of_not_mem_locallyQuasiFinitePart
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hf : IsLocallyOfFiniteType B S hS f) (x : points B S hS F)
    (hx : x ∉ Set.range (pointsMap B S hS
      (locallyQuasiFinitePart B S hS hF hG f hf).1.toFunctor
      (locallyQuasiFinitePart B S hS hF hG f hf).1.ι)) :
    ∃ d : ℕ∞, 1 ≤ d ∧ HasRelativeDimensionAt d B S hS f x
```

**`AlgebraicGeometry.Space.le_locallyQuasiFinitePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1344). The attribute's comment: “maximality of the canonical open subspace”.

> **Stacks 04NW, maximality.** Every open subspace of the source over which the morphism is
> locally quasi-finite is contained in
> `AlgebraicGeometry.Space.locallyQuasiFinitePart`; together with
> `AlgebraicGeometry.Space.isLocallyQuasiFinite_locallyQuasiFinitePart` this is what makes it
> canonical.

```lean
theorem le_locallyQuasiFinitePart (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f)
    (U : {U : Subfunctor F // IsOpenSubspace B S hS U})
    (hU : IsLocallyQuasiFinite B S hS (U.1.ι ≫ f)) :
    U ≤ locallyQuasiFinitePart B S hS hF hG f hf
```

**`AlgebraicGeometry.Space.locallyQuasiFinitePart_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1371). The attribute's comment: “compatibility with arbitrary base change”. References: SGA 3 V (7.4), “more general”.

> **Stacks 04NW, compatibility with arbitrary base change.** In a cartesian square of
> algebraic spaces over `S` whose right vertical arrow is locally of finite type, the base change
> is locally of finite type and its locally quasi-finite part is the inverse image of the locally
> quasi-finite part of the morphism.
>
> On points both sides are the relative-dimension-zero locus, and relative dimension at a point
> is invariant under base change by part (1) of Stacks 04NS.

```lean
theorem locallyQuasiFinitePart_preimage_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ hf' : IsLocallyOfFiniteType B S hS f',
      (locallyQuasiFinitePart B S hS hX' hY' f' hf').1 =
        (locallyQuasiFinitePart B S hS hX hY f hf).1.preimage g'
```

**`AlgebraicGeometry.Space.isOpenSubspace_relativeDimensionZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean#L110). The attribute's comment: “the canonical open subspace”.

> For a morphism of algebraic spaces over `S` which is locally of finite type, the locus where
> the relative dimension is zero is an open subspace of the source.

```lean
theorem isOpenSubspace_relativeDimensionZeroLocus (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f) :
    IsOpenSubspace B S hS (relativeDimensionZeroLocus B S hS f)
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_relativeDimensionZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean#L128). The attribute's comment: “local quasi-finiteness of the restriction”. References: EGA III (4.4.12), “partial”.

> A morphism of algebraic spaces over `S` which is locally of finite type is locally
> quasi-finite on the open subspace of its source where its relative dimension is zero.

```lean
theorem isLocallyQuasiFinite_relativeDimensionZeroLocus (hF : IsAlgebraicSpace B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyQuasiFinite B S hS ((relativeDimensionZeroLocus B S hS f).ι ≫ f)
```

**`AlgebraicGeometry.Space.one_le_of_hasRelativeDimensionAt_of_notMem_relativeDimensionZeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionZeroLocus.lean#L143). The attribute's comment: “relative dimension at least one outside the subspace”.

> At a point of the source which is not in the relative-dimension-zero locus, every value of
> the relative dimension of the morphism is at least `1`.

```lean
theorem one_le_of_hasRelativeDimensionAt_of_notMem_relativeDimensionZeroLocus (f : F ⟶ G)
    (x : points B S hS F)
    (hx : x ∉ Set.range (pointsMap B S hS (relativeDimensionZeroLocus B S hS f).toFunctor
      (relativeDimensionZeroLocus B S hS f).ι))
    (d : ℕ∞) (hd : HasRelativeDimensionAt d B S hS f x) : 1 ≤ d
```

## Tag 06LS, a lemma

[Tag 06LS](https://stacks.math.columbia.edu/tag/06LS) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiFiniteAt_of_dimensionAtPoint_fiber_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean, line 1470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FibreDimension.lean#L1470).

> **Stacks 06LS.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, let `p` be a field-valued point of `Y` — a morphism `Spec k ⟶ Y` from
> the spectrum of a field over `S` — and let `z` be a point of the fibre `X ×_Y Spec k` at which
> that fibre has dimension `0` in the sense of Stacks 04N5. Then `f` is quasi-finite at the image
> of `z`: after replacing `X` by an open subspace containing that image, `f` is locally
> quasi-finite.

```lean
theorem isQuasiFiniteAt_of_dimensionAtPoint_fiber_eq_zero (hX : IsAlgebraicSpace B S hS F)
    (hY : IsAlgebraicSpace B S hS G) (f : F ⟶ G) (hf : IsLocallyOfFiniteType B S hS f)
    (p : FieldValuedPoint B S hS G)
    (z : points B S hS (pullback f (yonedaEquiv.symm p.value)))
    (hz : dimensionAtPoint B S hS (pullback f (yonedaEquiv.symm p.value))
      (isAlgebraicSpace_pullback B S hS f (yonedaEquiv.symm p.value) hX
        (isAlgebraicSpace_yoneda B S hS (p.siteObject B S hS G)) hY) z = 0) :
    IsQuasiFiniteAt B S hS f
      (pointsMap B S hS (pullback f (yonedaEquiv.symm p.value))
        (pullback.fst f (yonedaEquiv.symm p.value)) z)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.34, Tag 04NP](https://stacks.math.columbia.edu/tag/04NP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
