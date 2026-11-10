---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isProper_of_isPullback, AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_of_isPullback, AlgebraicGeometry.Space.flatPullback_properPushforward_of_isPullback, AlgebraicGeometry.Space.flatPullback_properPushforward', AlgebraicGeometry.Space.flatPullback_properPushforward_unconditional, AlgebraicGeometry.Space.properPushforward_finiteLocallyFreeCyclePullback_eq_zsmul, AlgebraicGeometry.Space.isProper_of_isFiniteLocallyFreeOfRank, AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_zero_of_isFiniteLocallyFreeOfRank
statement: formalized
proof: formalized
---

# 82.11 Push and pull

Section 82.11 of the Stacks Project, [Tag 0EPC](https://stacks.math.columbia.edu/tag/0EPC). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EPD, a lemma

[Tag 0EPD](https://stacks.math.columbia.edu/tag/0EPD) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean#L195). The attribute's comment: “first assertion: the base change of a proper morphism is proper”.

> **Stacks 0EPD, first assertion**, by way of Stacks 04WP. In a cartesian square of algebraic
> spaces over `S` the base change `f'` of a proper morphism `f` is proper.

```lean
theorem isProper_of_isPullback
    {X' X Y' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hY' : IsAlgebraicSpace B S hS Y') (hY : IsAlgebraicSpace B S hS Y)
    (sq : IsPullback g' f' f g) (hf : IsProper B S hS f) :
    IsProper B S hS f'
```

**`AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean#L242). The attribute's comment: “second assertion: the base change of a morphism flat of relative dimension r is flat of relative dimension r”.

> **Stacks 0EPD, second assertion.** In Situation 0EDT let the four corners of a cartesian
> square of algebraic spaces over `B` be good and let `g : Y' ⟶ Y` be a morphism over `B` which is
> flat of relative dimension `r`. Then the base change `g' : X' ⟶ X` is flat of relative
> dimension `r`: it is locally of finite type, flat, and of relative dimension `r`.
>
> Local finite type of `g'` is goodness of `X'/B` and the cancellation of Stacks 0462 applied to
> `g' ≫ sX = sX'`, flatness is Stacks 03MO, and the relative dimension is
> `AlgebraicGeometry.Space.hasRelativeDimension_of_isPullback`, which is part (1) of
> Stacks 04NS.

```lean
theorem isFlat_and_hasRelativeDimension_of_isPullback
    (sX' : X' ⟶ D.space) (hX' : D.IsGood sX') (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (sY' : Y' ⟶ D.space) (hY' : D.IsGood sY') (sY : Y ⟶ D.space) (hY : D.IsGood sY)
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hg'base : g' ≫ sX = sX') (hgbase : g ≫ sY = sY') (sq : IsPullback g' f' f g) (r : ℕ)
    (hgflat : IsFlat D.site D.base D.base_mem g)
    (hgr : HasRelativeDimension r D.site D.base D.base_mem g) :
    IsLocallyOfFiniteType D.site D.base D.base_mem g' ∧
      IsFlat D.site D.base D.base_mem g' ∧
        HasRelativeDimension r D.site D.base D.base_mem g'
```

**`AlgebraicGeometry.Space.flatPullback_properPushforward_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChange.lean#L644). The attribute's comment: “third assertion: the identity g^* f\_* α = f'\_* (g')^* α in Z\_\{k+r}(Y') for an arbitrary k-cycle α, at the source's hypotheses”.

> **Stacks 0EPD, third assertion.** In Situation 0EDT let the four corners of a cartesian
> square of good algebraic spaces over `B` be good, let `f : X ⟶ Y` be proper and let
> `g : Y' ⟶ Y` be flat of relative dimension `r`. Then for every `k`-cycle `α` on `X`
>
> `g^*f_*α = f'_*(g')^*α`
>
> in `Z_{k+r}(Y')`.
>
> **Nothing is carried.** The pushforward along `f'` is legitimate because `f'` is proper, which is
> the first assertion `AlgebraicGeometry.Space.isProper_of_isPullback` and appears in the
> statement; the pullback along `g'` is legitimate because `g'` is flat of relative dimension `r`,
> which is the second assertion
> `AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_of_isPullback` and is written out as the
> hypotheses `hg'flat` and `hg'r` so that the degree bookkeeping stays explicit.
>
> The two numerical inputs are proved. One is the degree count at the generic points,
> `deg(Z/Z')·m_{T'}(g^{-1}(Z')) = ∑_T m_T((g')^{-1}(Z))·deg(T/T')`, which is
> `Space.BaseChangeDegreeCount.properCycleDegree_mul_flatPullbackMult_eq_finsum_of_isProper`
> of `StacksFrontier.AlgebraicGeometry.Spaces.Chow.ProperFlatBaseChangeDegreeCount`: the source's
> route (`[Z] = [𝒪_Z]_k`, part (1) of Stacks 0EP3 on both sides, and flat base change in degree
> zero, part (1) of Stacks 073K) read at one pair of generic points. The other is that the
> left-hand side of the count is the whole coefficient of `g^*f_*[Z]` at `T'`, by
> `AlgebraicGeometry.Space.finsum_properCycleMult_mul_flatPullbackMult`. The count is bundled into
> `AlgebraicGeometry.Space.ProperFlatBaseChangeComparison` and handed to
> `AlgebraicGeometry.Space.flatPullback_properPushforward` above, which is where the passage from a
> prime cycle to an arbitrary cycle is carried out.

```lean
theorem flatPullback_properPushforward_of_isPullback (sq : IsPullback g' f' f g)
    (hfproper : IsProper D.site D.base D.base_mem f)
    (k n : ℤ) (hkn : k + (r : ℤ) = n) (α : CycleGroup D sX k) :
    flatPullbackMap D sY' hY' sY hY g hgbase r hgflat hgr k n hkn
        (properCyclePushforward D sX hX sY hY hfbase hfproper.2.1.2 k α) =
      properCyclePushforward D sX' hX' sY' hY' hf'base
        (isProper_of_isPullback D.site D.base D.base_mem hX'.1 hX.1 hY'.1 hY.1 sq hfproper).2.1.2
        n (flatPullbackMap D sX' hX' sX hX g' hg'base r hg'flat hg'r k n hkn α)
```

**`AlgebraicGeometry.Space.flatPullback_properPushforward'`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChangeGenericPoints.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChangeGenericPoints.lean#L282). The attribute's comment: “third assertion: the identity g^* f\_* α = f'\_* (g')^* α in Z\_\{k+r}(Y') for an arbitrary k-cycle α, with no comparison datum and no numerical identity carried”.

> The identity `g^*f_*α = f'_*(g')^*α` in `Z_{k+r}(Y')`, for a cartesian square of good
> algebraic spaces over `B` with `f` proper and `g` flat of relative dimension `r`, and for an
> arbitrary `k`-cycle `α` on `X`.

```lean
alias flatPullback_properPushforward'
```

**`AlgebraicGeometry.Space.flatPullback_properPushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChangeUnconditional.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperFlatBaseChangeUnconditional.lean#L246). The attribute's comment: “third assertion: the identity g^* f\_* α = f'\_* (g')^* α in Z\_\{k+r}(Y') for an arbitrary k-cycle α, at the source's hypotheses”.

> **Stacks 0EPD, third assertion.**  In Situation 0EDT let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square of good algebraic spaces over `B`, let `f : X ⟶ Y` be proper and let
> `g : Y' ⟶ Y` be flat of relative dimension `r`.  Then for every `k`-cycle `α` on `X`
>
> `g^*f_*α = f'_*(g')^*α`
>
> in `Z_{k+r}(Y')`.
>
> Nothing is assumed: the pushforward along `f'` is legitimate because `f'` is proper, which is the
> first assertion `AlgebraicGeometry.Space.isProper_of_isPullback`; the pullback along `g'` is
> legitimate because `g'` is flat of relative dimension `r`, which is the second assertion
> `AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_of_isPullback`; and both are written out
> in the statement rather than carried.  The identity itself is
> `AlgebraicGeometry.Space.flatPullback_properPushforward`, whose comparison at the generic points
> is `AlgebraicGeometry.Space.properFlatBaseChangeComparison`.
>
> A `CycleGroup` is never transported along an equality of degrees, so the identity is stated at a
> pair `k`, `n` with `k + r = n` and the degree equality as an explicit argument, which is the
> convention of `AlgebraicGeometry.Space.flatPullbackMap`.

```lean
theorem flatPullback_properPushforward_unconditional (sq : IsPullback g' f' f g)
    (hfproper : IsProper D.site D.base D.base_mem f)
    (k n : ℤ) (hkn : k + (r : ℤ) = n) (α : CycleGroup D sX k) :
    flatPullbackMap D sY' hY' sY hY g hgbase r hgflat hgr k n hkn
        (properCyclePushforward D sX hX sY hY hfbase hfproper.2.1.2 k α) =
      properCyclePushforward D sX' hX' sY' hY' hf'base
        (isProper_of_isPullback D.site D.base D.base_mem hX'.1 hX.1 hY'.1 hY.1 sq hfproper).2.1.2
        n (flatPullbackMap D sX' hX' sX hX g' hg'base r
          (isFlat_and_hasRelativeDimension_of_isPullback D sX' hX' sX hX sY' hY' sY hY hg'base
            hgbase sq r hgflat hgr).2.1
          (isFlat_and_hasRelativeDimension_of_isPullback D sX' hX' sX hX sY' hY' sY hY hg'base
            hgbase sq r hgflat hgr).2.2 k n hkn α)
```

## Tag 0EPE, a lemma

[Tag 0EPE](https://stacks.math.columbia.edu/tag/0EPE) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushforward_finiteLocallyFreeCyclePullback_eq_zsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreeConstructedPullback.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreeConstructedPullback.lean#L456). The attribute's comment: “f\_* f^* alpha = d alpha”.

> In Situation 0EDT let `X/B` and `Y/B` be good and let
> `f : X ⟶ Y` be finite locally free of degree `d`. Then
>
> `f_*f^*α = dα`
>
> for every `α ∈ Z_k(Y)`, with `f^*` the flat pullback of Stacks 0EP8
> (`AlgebraicGeometry.Space.finiteLocallyFreeCyclePullback`, whose flatness and
> relative-dimension hypotheses are the second conclusion of Stacks 0EPE) and `f_*` the proper
> pushforward of Stacks 0EP1 (whose quasi-compactness hypothesis is the first conclusion).

```lean
theorem properPushforward_finiteLocallyFreeCyclePullback_eq_zsmul
    (sX : X.obj ⟶ D.space) (hX : D.IsGood sX) (sY : Y.obj ⟶ D.space) (hY : D.IsGood sY)
    (f : X ⟶ Y) (hbase : f.hom ≫ sY = sX) (d : ℕ)
    (hf : IsFiniteLocallyFreeOfRank D.site D.base D.base_mem f d) (k : ℤ)
    (α : CycleGroup D sY k) :
    properPushforward D sX hX sY hY hbase
        (isQuasiCompact_hom_of_isFiniteLocallyFreeOfRank D f d hf) k
        ((finiteLocallyFreeCyclePullback D sX hX sY hY f hbase d hf).map k k (by simp) α) =
      (d : ℤ) • α
```

**`AlgebraicGeometry.Space.isProper_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean#L237). The attribute's comment: “f is proper”.

> **Stacks 0EPE, first conclusion.** A finite locally free morphism of degree `d` of algebraic
> spaces over `S` is proper.
>
> A finite locally free morphism is finite by Stacks 0416, and a finite morphism is proper by
> Stacks 04NZ. The goodness hypotheses of Situation 0EDT are not used, so the conclusion is drawn
> for an arbitrary morphism of algebraic spaces over `S`.

```lean
theorem isProper_of_isFiniteLocallyFreeOfRank
    (hcross : FiniteLocallyFreeRankChartComparison B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (d : ℕ)
    (hf : IsFiniteLocallyFreeOfRank B S hS f d) :
    IsProper B S hS f.hom
```

**`AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_zero_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean#L263). The attribute's comment: “f is flat of relative dimension 0”.

> **Stacks 0EPE, second conclusion.** A finite locally free morphism of degree `d` of
> algebraic spaces over `S` is flat of relative dimension `0`: it is flat and locally of finite
> type, and has relative dimension `0` at every point of its source.
>
> Flatness is Stacks 0416. For the relative dimension, the morphism is finite, hence locally
> quasi-finite and locally of finite type, and Stacks 04NV turns local quasi-finiteness into the
> vanishing of the relative dimension at every point. The goodness hypotheses of Situation 0EDT
> are not used.

```lean
theorem isFlat_and_hasRelativeDimension_zero_of_isFiniteLocallyFreeOfRank
    (hcross : FiniteLocallyFreeRankChartComparison B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (d : ℕ)
    (hf : IsFiniteLocallyFreeOfRank B S hS f d) :
    IsFlat B S hS f.hom ∧ IsLocallyOfFiniteType B S hS f.hom ∧
      HasRelativeDimension 0 B S hS f.hom
```

**`AlgebraicGeometry.Space.properPushforward_flatCyclePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPull.lean#L376). The attribute's comment: “f\_* f^* alpha = d alpha”.

> **Stacks 0EPE, third conclusion.** In Situation 0EDT let `X/B` and `Y/B` be good and let
> `f : X ⟶ Y` be finite locally free of degree `d`. Then `f_*f^*α = dα` for every `α ∈ Z_k(Y)`.
>
> Only the term of the flat pullback at `W'` itself survives in the coefficient of `f_*f^*α` at
> an integral closed subspace `W' ⊆ Y`, by
> `AlgebraicGeometry.Space.eq_cycleImageSubspace_of_mult_ne_zero`, and what is left is `α_{W'}`
> times the degree `hdeg` of the fibre over the generic point of `W'`; at a `W'` of δ-dimension
> other than `k` the coefficient of `α` there vanishes and both sides are zero.

```lean
theorem properPushforward_flatCyclePullback
    (hcross : FiniteLocallyFreeRankChartComparison D.site D.base D.base_mem)
    (sX : X.obj ⟶ D.space) (hX : D.IsGood sX) (sY : Y.obj ⟶ D.space) (hY : D.IsGood sY)
    (f : X ⟶ Y) (hbase : f.hom ≫ sY = sX) (d : ℕ)
    (hf : IsFiniteLocallyFreeOfRank D.site D.base D.base_mem f d)
    (pb : FlatCyclePullback D sX hX sY hY f.hom 0)
    (k : ℤ)
    (hdeg : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem Y.obj,
      deltaDimension D sY W = k →
      ∑ᶠ T ∈ {T : IntegralClosedSubspace D.site D.base D.base_mem X.obj |
          cycleImageSubspace D sY hY f.hom T = W},
        pb.mult W T * (cycleResidueDegree D sX hX sY hY f.hom
          (T.ambientGenericPoint D.site D.base D.base_mem) : ℤ) = (d : ℤ))
    (α : CycleGroup D sY k) :
    properPushforward D sX hX sY hY hbase
        (isQuasiCompact_of_isFiniteLocallyFreeOfRank D.site D.base D.base_mem hcross f d hf) k
        (pb.map k k (by simp) α) = (d : ℤ) • α
```

**`AlgebraicGeometry.Space.isProper_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean#L91). The attribute's comment: “f is proper”.

> **Stacks 0EPE, first conclusion.** A finite locally free morphism of algebraic spaces over
> `S` is proper.
>
> A finite locally free morphism is finite by Stacks 0416, and a finite morphism is proper by
> Stacks 04NZ. Neither the rank nor the goodness hypotheses of Situation 0EDT are used, so the
> conclusion is drawn for the unranked definition of Stacks 03ZV and an arbitrary morphism of
> algebraic spaces over `S`.

```lean
theorem isProper_of_isFiniteLocallyFree {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsFiniteLocallyFree B S hS f) :
    IsProper B S hS f.hom
```

**`AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_zero_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean#L113). The attribute's comment: “f is flat of relative dimension 0”.

> **Stacks 0EPE, second conclusion.** A finite locally free morphism of algebraic spaces
> over `S` is flat of relative dimension `0`: it is flat and locally of finite type, and has
> relative dimension `0` at every point of its source.
>
> Flatness is Stacks 0416. For the relative dimension, the morphism is finite, hence locally
> quasi-finite and locally of finite type, and Stacks 04NV turns local quasi-finiteness into the
> vanishing of the relative dimension at every point. Neither the rank nor the goodness hypotheses
> of Situation 0EDT are used.

```lean
theorem isFlat_and_hasRelativeDimension_zero_of_isFiniteLocallyFree
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsFiniteLocallyFree B S hS f) :
    IsFlat B S hS f.hom ∧ IsLocallyOfFiniteType B S hS f.hom ∧
      HasRelativeDimension 0 B S hS f.hom
```

**`AlgebraicGeometry.Space.properPushforward_flatCyclePullback_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FiniteLocallyFreePushPullUnranked.lean#L147). The attribute's comment: “f\_* f^* alpha = d alpha”.

> **Stacks 0EPE, third conclusion.** In Situation 0EDT let `X/B` and `Y/B` be good and let
> `f : X ⟶ Y` be finite locally free, with `hdeg` recording the degree `d` of its fibre over the
> generic point of every integral closed subspace of δ-dimension `k`. Then `f_*f^*α = dα` for
> every `α ∈ Z_k(Y)`.
>
> Only the term of the flat pullback at `W'` itself survives in the coefficient of `f_*f^*α` at
> an integral closed subspace `W' ⊆ Y`, by
> `AlgebraicGeometry.Space.eq_cycleImageSubspace_of_mult_ne_zero`, and what is left is `α_{W'}`
> times the degree `hdeg` of the fibre over the generic point of `W'`; at a `W'` of δ-dimension
> other than `k` the coefficient of `α` there vanishes and both sides are zero.
>
> Finite local freeness enters only through quasi-compactness, which is all the proper pushforward
> of Stacks 0EP1 asks for, so the rank of Stacks 03ZV is not imposed on `f`: the degree `d` is
> pinned by `hdeg` alone.

```lean
theorem properPushforward_flatCyclePullback_of_isFiniteLocallyFree
    (sX : X.obj ⟶ D.space) (hX : D.IsGood sX) (sY : Y.obj ⟶ D.space) (hY : D.IsGood sY)
    (f : X ⟶ Y) (hbase : f.hom ≫ sY = sX) (d : ℕ)
    (hf : IsFiniteLocallyFree D.site D.base D.base_mem f)
    (pb : FlatCyclePullback D sX hX sY hY f.hom 0)
    (k : ℤ)
    (hdeg : ∀ W : IntegralClosedSubspace D.site D.base D.base_mem Y.obj,
      deltaDimension D sY W = k →
      ∑ᶠ T ∈ {T : IntegralClosedSubspace D.site D.base D.base_mem X.obj |
          cycleImageSubspace D sY hY f.hom T = W},
        pb.mult W T * (cycleResidueDegree D sX hX sY hY f.hom
          (T.ambientGenericPoint D.site D.base D.base_mem) : ℤ) = (d : ℤ))
    (α : CycleGroup D sY k) :
    properPushforward D sX hX sY hY hbase
        (isQuasiCompact_of_isFiniteLocallyFree D.site D.base D.base_mem f hf) k
        (pb.map k k (by simp) α) = (d : ℤ) • α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.11, Tag 0EPC](https://stacks.math.columbia.edu/tag/0EPC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
