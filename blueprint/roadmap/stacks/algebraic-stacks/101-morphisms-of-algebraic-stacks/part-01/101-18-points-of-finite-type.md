---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isFiniteTypePoint_of_exists_isClosed_smoothChart, AlgebraicGeometry.Stack.exists_isClosed_smoothChart_of_isFiniteTypePoint, AlgebraicGeometry.Stack.exists_isClosed_smoothChart_size_le_of_isFiniteTypePoint, AlgebraicGeometry.Stack.IsFiniteTypePoint, AlgebraicGeometry.Stack.finiteTypePoints, AlgebraicGeometry.Stack.affineSmoothChartClosedPoints_eq_smoothChartClosedPoints, AlgebraicGeometry.Stack.smoothChartClosedPoints_subset_finiteTypePoints, AlgebraicGeometry.Stack.finiteTypePoints_subset_smoothChartClosedPoints
statement: formalized
proof: formalized
---

# 101.18 Points of finite type

Section 101.18 of the Stacks Project, [Tag 06FW](https://stacks.math.columbia.edu/tag/06FW). 7 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06FX, a lemma

[Tag 06FX](https://stacks.math.columbia.edu/tag/06FX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFiniteTypePoint_of_exists_isClosed_smoothChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean#L319). The attribute's comment: “condition (2) implies condition (1)”.

> **Stacks 06FX, condition (2) implies condition (1).** Let `x` be a point of an algebraic stack
> `𝒳` over `S`. If there are a scheme `U` of the site, a closed point of `U`, and a smooth
> 1-morphism from the algebraic stack of `U` to `𝒳` carrying that point to `x`, then some
> field-valued point representing `x` has a 1-morphism `Spec k ⟶ 𝒳` which is locally of finite
> type, i.e. `x` is a finite type point in the sense of Stacks 06FY.
>
> The point of `U` is the closed point, a smooth 1-morphism is locally of finite type, and
> Stacks 06G0 carries finite type points along a 1-morphism locally of finite type.

```lean
theorem isFiniteTypePoint_of_exists_isClosed_smoothChart
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (h : ∃ (U : BigFppfOver B S hS) (φ : schemeStack.{u, w} B S hS U ⟶ 𝒳)
        (z : points B S hS (schemeFibredCategory B S hS U).val
          (schemeFibredCategory B S hS U).property),
        AlgebraicStacks.IsSmooth B S hS φ ∧
          IsClosed ({pointsHomeomorphScheme B S hS U z} :
            Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
          pointsMap B S hS (schemeFibredCategory B S hS U).val
            (schemeFibredCategory B S hS U).property 𝒳.val.property φ.hom.hom z = x) :
    IsFiniteTypePoint.{u, w} B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.exists_isClosed_smoothChart_of_isFiniteTypePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean#L644). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 06FX, condition (1) implies condition (2).** A finite type point `x` of an algebraic
> stack `𝒳` over `S` (Stacks 06FY) is the image of a closed point of a scheme of the site carrying
> a smooth 1-morphism to `𝒳`.
>
> A smooth surjective scheme chart `a : U ⟶ 𝒳` has a finite type point above `x`, and by
> **Stacks 06EF** such a point is the image of a closed point of a scheme `V` étale over `U`. An
> étale morphism of schemes is smooth, so the composite `V ⟶ U ⟶ 𝒳` is smooth by **Stacks 075V**,
> and it carries that closed point to `x`.

```lean
theorem exists_isClosed_smoothChart_of_isFiniteTypePoint
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) :
    ∃ (U : BigFppfOver B S hS) (φ : schemeStack.{u, w} B S hS U ⟶ 𝒳)
      (z : points B S hS (schemeFibredCategory B S hS U).val
        (schemeFibredCategory B S hS U).property),
      AlgebraicStacks.IsSmooth B S hS φ ∧
        IsClosed ({pointsHomeomorphScheme B S hS U z} :
          Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
        pointsMap B S hS (schemeFibredCategory B S hS U).val
          (schemeFibredCategory B S hS U).property 𝒳.val.property φ.hom.hom z = x
```

**`AlgebraicGeometry.Stack.exists_isClosed_smoothChart_size_le_of_isFiniteTypePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointSmoothChart.lean#L688). The attribute's comment: “condition (1) implies condition (2), with the chart's size bounded by that of a given smooth surjective chart”.

> **Stacks 06FX, condition (1) implies condition (2), with the chart no larger than a given
> smooth surjective chart.** Let `a : U₀ ⟶ 𝒳` be a smooth surjective 1-morphism out of a scheme of
> the site. Then a finite type point `x` of `𝒳` is the image of a closed point of a scheme `U` of
> the site carrying a smooth 1-morphism to `𝒳` whose **size is at most that of `U₀`** and whose
> underlying scheme is **affine**.
>
> The proof of `AlgebraicGeometry.Stack.exists_isClosed_smoothChart_of_isFiniteTypePoint` run at
> the given chart rather than at one chosen for the occasion, and with the affine form of
> **Stacks 06EH** (`AlgebraicGeometry.Space.isFiniteTypePoint_iff_exists_isAffine_isClosed_etaleChart`)
> in place of the general one: the chart it produces is then an **affine** scheme étale over `U₀`,
> so it is quasi-compact and locally of finite type over `U₀`, and **Stacks 04T7**
> (`AlgebraicGeometry.Scheme.size_le_of_locallyOfFiniteType`) bounds its size by that of `U₀`. The
> affineness is recorded in the conclusion as well: the chart construction of **Stacks 06N3** reads
> its slicing sequence in the global functions of the chart, and on an affine chart it may do so
> with no shrinking, by
> `AlgebraicGeometry.exists_global_isRegular_ofList_eq_maximalIdeal_stalk_of_unramifiedAt`.
>
> This is the form the chart construction of **Stacks 06MF** needs: the charts it cuts out of these
> are indexed by the finite type points of `𝒳`, a set which need not be below the cofinality of the
> site's size cutoff, so their coproduct lies in the site by
> `AlgebraicGeometry.BigFppfSite.contains_sigma_of_forall_size_le` and that asks for a bound on
> their sizes which is *uniform in the point*.

```lean
theorem exists_isClosed_smoothChart_size_le_of_isFiniteTypePoint
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (U₀ : BigFppfOver B S hS)
    (a : schemeStack.{u, w} B S hS U₀ ⟶ 𝒳)
    (hasm : AlgebraicStacks.IsSmooth B S hS a) (hasurj : IsSurjective B S hS a)
    (x : points B S hS 𝒳.val.val 𝒳.val.property)
    (hx : IsFiniteTypePoint.{u, w} B S hS 𝒳 x) :
    ∃ (U : BigFppfOver B S hS) (φ : schemeStack.{u, w} B S hS U ⟶ 𝒳)
      (z : points B S hS (schemeFibredCategory B S hS U).val
        (schemeFibredCategory B S hS U).property),
      AlgebraicStacks.IsSmooth B S hS φ ∧
        IsClosed ({pointsHomeomorphScheme B S hS U z} :
          Set ((BigFppfOver.toScheme B S hS).obj U)) ∧
        pointsMap B S hS (schemeFibredCategory B S hS U).val
          (schemeFibredCategory B S hS U).property 𝒳.val.property φ.hom.hom z = x ∧
        ((BigFppfOver.toScheme B S hS).obj U).size ≤
          ((BigFppfOver.toScheme B S hS).obj U₀).size ∧
        IsAffine ((BigFppfOver.toScheme B S hS).obj U)
```

## Tag 06FY, a definition

[Tag 06FY](https://stacks.math.columbia.edu/tag/06FY) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsFiniteTypePoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointAlgebraicStack.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointAlgebraicStack.lean#L78). The attribute's comment: “finite_type_point”.

> **Stacks 06FY.** A point of an algebraic stack `𝒳` over `S` is a *finite type point* when
> some field-valued point representing it has a locally-of-finite-type 1-morphism `Spec k → 𝒳`.
>
> This is condition (1) of Stacks 06FX.

```lean
abbrev IsFiniteTypePoint (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) : Prop
```

**`AlgebraicGeometry.Stack.finiteTypePoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointAlgebraicStack.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointAlgebraicStack.lean#L88). The attribute's comment: “finite_type_points_set”.

> **Stacks 06FY.** The set `𝒳_{ft-pts}` of finite type points of an algebraic stack `𝒳`
> over `S`.

```lean
abbrev finiteTypePoints (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    Set (points B S hS 𝒳.val.val 𝒳.val.property)
```

## Tag 06FZ, a lemma

[Tag 06FZ](https://stacks.math.columbia.edu/tag/06FZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.affineSmoothChartClosedPoints_eq_smoothChartClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L191). The attribute's comment: “the union over all schemes smooth over the stack equals the union over the affine schemes smooth over it”.

> **Stacks 06FZ**, the agreement of the two ranges. The union of the images of the closed points
> of the schemes of the site smooth over an algebraic stack `𝒳` over `S` is unchanged when the
> schemes are restricted to the affine ones.
>
> A closed point of a chart `U` is a closed point of an affine open `V ⊆ U` containing it, the
> inclusion of `V` is an open immersion and hence smooth, and the composite of the induced
> 1-morphism with the chart is smooth by Stacks 075V.

```lean
theorem affineSmoothChartClosedPoints_eq_smoothChartClosedPoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    affineSmoothChartClosedPoints.{u, w} B S hS 𝒳 =
      smoothChartClosedPoints.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.smoothChartClosedPoints_subset_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L220). The attribute's comment: “the inclusion of the union over all schemes smooth over the stack in the set of finite type points, i.e. the ⊇ direction of the set equality”.

> **Stacks 06FZ**, the inclusion of the union in the set of finite type points. Every image of a
> closed point of a scheme of the site smooth over an algebraic stack `𝒳` over `S` is a finite type
> point of `𝒳` (Stacks 06FY).
>
> This is condition (2) of Stacks 06FX implying condition (1).

```lean
theorem smoothChartClosedPoints_subset_finiteTypePoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    smoothChartClosedPoints.{u, w} B S hS 𝒳 ⊆ finiteTypePoints B S hS 𝒳
```

**`AlgebraicGeometry.Stack.finiteTypePoints_subset_smoothChartClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L236). The attribute's comment: “the inclusion of the set of finite type points in the union over all schemes smooth over the stack, i.e. the ⊆ direction of the set equality”.

> **Stacks 06FZ**, the inclusion of the set of finite type points in the union. Every finite
> type point of an algebraic stack `𝒳` over `S` (Stacks 06FY) is the image of a closed point of a
> scheme of the site smooth over `𝒳`.
>
> This is the restatement as a subset relation of condition (1) of Stacks 06FX implying
> condition (2).

```lean
theorem finiteTypePoints_subset_smoothChartClosedPoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    finiteTypePoints B S hS 𝒳 ⊆ smoothChartClosedPoints.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.finiteTypePoints_eq_smoothChartClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L249). The attribute's comment: “the set equality 𝒳_{ft-pts} = ⋃_{φ : U ⟶ 𝒳 smooth} |φ|(U₀) over all schemes smooth over the stack”.

> **Stacks 06FZ**, the set equality. The set `𝒳_{ft-pts}` of finite type points of an algebraic
> stack `𝒳` over `S` is the union `⋃_{φ : U ⟶ 𝒳 smooth} |φ|(U₀)` of the images of the sets of
> closed points of the schemes of the site smooth over `𝒳`.

```lean
theorem finiteTypePoints_eq_smoothChartClosedPoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    finiteTypePoints B S hS 𝒳 = smoothChartClosedPoints.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.affineSmoothChartClosedPoints_subset_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L259). The attribute's comment: “the inclusion of the union over the affine schemes smooth over the stack in the set of finite type points, i.e. the ⊇ direction of the set equality for the affine range”.

> The union over the affine schemes of the site smooth over an algebraic stack `𝒳` over `S` is
> contained in the set of finite type points of `𝒳`.

```lean
theorem affineSmoothChartClosedPoints_subset_finiteTypePoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    affineSmoothChartClosedPoints.{u, w} B S hS 𝒳 ⊆ finiteTypePoints B S hS 𝒳
```

**`AlgebraicGeometry.Stack.finiteTypePoints_eq_affineSmoothChartClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSmoothUnion.lean#L270). The attribute's comment: “the set equality 𝒳_{ft-pts} = ⋃_{φ : U ⟶ 𝒳 smooth} |φ|(U₀) over the affine schemes smooth over the stack”.

> **Stacks 06FZ**, the set equality for the affine range. The set `𝒳_{ft-pts}` of finite type
> points of an algebraic stack `𝒳` over `S` is the union `⋃_{φ : U ⟶ 𝒳 smooth} |φ|(U₀)` of the
> images of the sets of closed points of the *affine* schemes of the site smooth over `𝒳`.

```lean
theorem finiteTypePoints_eq_affineSmoothChartClosedPoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    finiteTypePoints B S hS 𝒳 = affineSmoothChartClosedPoints.{u, w} B S hS 𝒳
```

## Tag 06G0, a lemma

[Tag 06G0](https://stacks.math.columbia.edu/tag/06G0) in the Stacks Project.

**`AlgebraicGeometry.Stack.mapsTo_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsMorphism.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsMorphism.lean#L92).

> **Stacks 06G0.** A 1-morphism of algebraic stacks over `S` which is locally of finite type
> maps the set of finite type points of its source into the set of finite type points of its
> target.
>
> A field-valued representative of a finite type point of the source has a locally-of-finite-type
> 1-morphism, and its image represents the image point; the image's 1-morphism is 2-isomorphic to
> the composite of that one with `f`, which is locally of finite type by Stacks 06FT.

```lean
theorem mapsTo_finiteTypePoints {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f) :
    Set.MapsTo
      (Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom)
      (finiteTypePoints B S hS 𝒳) (finiteTypePoints B S hS 𝒴)
```

## Tag 06G1, a lemma

[Tag 06G1](https://stacks.math.columbia.edu/tag/06G1) in the Stacks Project.

**`AlgebraicGeometry.Stack.image_finiteTypePoints_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSurjective.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsSurjective.lean#L123).

> **Stacks 06G1.** A surjective 1-morphism of algebraic stacks over `S` which is locally of
> finite type maps the set of finite type points of its source *onto* the set of finite type points
> of its target.
>
> That the image is contained in `𝒴_{ft-pts}` is **Stacks 06G0**. Conversely a finite type point of
> `𝒴` is represented by a field-valued point whose 1-morphism out of the algebraic stack of the
> spectrum of a field is locally of finite type, and that spectrum has a single point, so
> `AlgebraicGeometry.Stack.mem_image_finiteTypePoints_of_subsingleton` applies to it.

```lean
theorem image_finiteTypePoints_of_isSurjective {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsLocallyOfFiniteType B S hS f)
    (hsurj : IsSurjective B S hS f) :
    Stack.pointsMap B S hS 𝒳.val.val 𝒳.val.property 𝒴.val.property f.hom.hom ''
        finiteTypePoints B S hS 𝒳 = finiteTypePoints B S hS 𝒴
```

## Tag 06G2, a lemma

[Tag 06G2](https://stacks.math.columbia.edu/tag/06G2) in the Stacks Project.

**`AlgebraicGeometry.Stack.closure_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsDense.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsDense.lean#L153). The attribute's comment: “closed subsets, in the spelling of the scheme-level Stacks 02J4 and the algebraic-space-level Stacks 06EK: for a closed subset of the point space, the closure of its intersection with the set of finite type points is the subset itself”.

> For a closed subset `T` of the point space of an algebraic stack `𝒳`, the closure of the set
> of finite type points lying in `T` is `T` itself; that is, `T ∩ 𝒳_{ft-pts}` is dense in `T`.

```lean
theorem closure_inter_finiteTypePoints (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    letI := pointTopology B S hS 𝒳.val
    ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsClosed T →
      closure (T ∩ finiteTypePoints B S hS 𝒳) = T
```

**`AlgebraicGeometry.Stack.nonempty_inter_and_closure_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsDense.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsDense.lean#L170). The attribute's comment: “both assertions: for a locally closed subset T of the point space of an algebraic stack, T nonempty implies that T meets the set of finite type points; and in particular, for a closed subset T, the intersection of T with the set of finite type points is dense in T”.

> Let `𝒳` be an algebraic stack over `S`. Then
>
> * for any locally closed subset `T ⊆ |𝒳|` of its point space, `T ≠ ∅ → T ∩ 𝒳_{ft-pts} ≠ ∅`; and
> * in particular, for any closed subset `T ⊆ |𝒳|` the closure of `T ∩ 𝒳_{ft-pts}` is `T`, that
>   is, `T ∩ 𝒳_{ft-pts}` is dense in `T`.

```lean
theorem nonempty_inter_and_closure_inter_finiteTypePoints
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    letI := pointTopology B S hS 𝒳.val
    (∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsLocallyClosed T → T.Nonempty →
        (T ∩ finiteTypePoints B S hS 𝒳).Nonempty) ∧
      ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsClosed T →
        closure (T ∩ finiteTypePoints B S hS 𝒳) = T
```

**`AlgebraicGeometry.Stack.nonempty_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosed.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosed.lean#L188). The attribute's comment: “the first clause: a nonempty locally closed subset of the point space meets the set of finite type points. The reduced induced substack structure of Stacks 06FK on a locally closed subset is carried as the hypothesis `hsub`, since Stacks 06FK is absent from this library; the rest of the proof, including the existence of a finite type point on a nonempty algebraic stack, is proved”.

> **Stacks 06G2, first clause.** A nonempty locally closed subset of the point space of an
> algebraic stack contains a finite type point.
>
> The reduced induced substack `𝒵` of `T` is nonempty because its image on points is `T`, so it
> has a finite type point by
> `AlgebraicGeometry.Stack.exists_isFiniteTypePoint_of_nonempty`; the image of that point is a
> finite type point of `𝒳` by **Stacks 06G0** and lies in `T`.
>
> The substack is carried as `AlgebraicGeometry.Stack.HasReducedInducedSubstacks`, which stands for
> **Stacks 06FK**; everything else is proved.

```lean
theorem nonempty_inter_finiteTypePoints (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hsub : HasReducedInducedSubstacks.{u, w} B S hS 𝒳) :
    letI := pointTopology B S hS 𝒳.val
    ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsLocallyClosed T → T.Nonempty →
      (T ∩ finiteTypePoints B S hS 𝒳).Nonempty
```

**`AlgebraicGeometry.Stack.subset_closure_inter_finiteTypePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosed.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosed.lean#L213). The attribute's comment: “the second clause: for a closed subset of the point space, its intersection with the set of finite type points is dense in it. Derived from the first clause by topology alone, so it carries exactly the same Stacks 06FK hypothesis `hsub` and nothing further”.

> **Stacks 06G2, second clause.** For a closed subset `T` of the point space of an algebraic
> stack, the finite type points lying in `T` are dense in `T`.
>
> This follows from the first clause by pure topology: given `x ∈ T` and an open `V` containing
> `x`, the set `T ∩ V` is locally closed and nonempty, so it meets the set of finite type points,
> which is exactly the statement that `V` meets `T ∩ 𝒳_{ft-pts}`.

```lean
theorem subset_closure_inter_finiteTypePoints (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hsub : HasReducedInducedSubstacks.{u, w} B S hS 𝒳) :
    letI := pointTopology B S hS 𝒳.val
    ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsClosed T →
      T ⊆ closure (T ∩ finiteTypePoints B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.exists_mem_finiteTypePoints_of_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosedChart.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosedChart.lean#L46). The attribute's comment: “the first clause: a nonempty locally closed subset of the point space meets the set of finite type points”.

> A nonempty locally closed subset of the point space of an algebraic stack contains a finite
> type point.

```lean
theorem exists_mem_finiteTypePoints_of_isLocallyClosed (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    letI := pointTopology B S hS 𝒳.val
    ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsLocallyClosed T → T.Nonempty →
      (T ∩ finiteTypePoints B S hS 𝒳).Nonempty
```

**`AlgebraicGeometry.Stack.subset_closure_inter_finiteTypePoints_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosedChart.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointsLocallyClosedChart.lean#L115). The attribute's comment: “the second clause: for a closed subset of the point space, its intersection with the set of finite type points is dense in it”.

> For a closed subset `T` of the point space of an algebraic stack, the finite type points
> lying in `T` are dense in `T`.

```lean
theorem subset_closure_inter_finiteTypePoints_of_isClosed (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    letI := pointTopology B S hS 𝒳.val
    ∀ T : Set (points B S hS 𝒳.val.val 𝒳.val.property), IsClosed T →
      T ⊆ closure (T ∩ finiteTypePoints B S hS 𝒳)
```

## Tag 06G3, a lemma

[Tag 06G3](https://stacks.math.columbia.edu/tag/06G3) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFiniteTypePoint_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointResidualGerbe.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointResidualGerbe.lean#L189). The attribute's comment: “the equivalence of (1) being a finite type point, (2) admitting a locally-of-finite-type 1-morphism from a one-point algebraic stack with image the point, and (3) the residual gerbe existing with locally-of-finite-type inclusion. The implications (3) => (2) and (2) => (1) are proved; (1) => (3) is carried as the hypothesis `hForward`, since Stacks 06FI, 04ZZ and 06MX are absent from this library and it has no construction of a residual gerbe”.

> **Stacks 06G3.** For a point `x` of the point space of an algebraic stack `𝒳` over `S`, the
> following are equivalent: `x` is a finite type point; there is a one-point algebraic stack with a
> locally-of-finite-type 1-morphism to `𝒳` whose image on points is `{x}`; the residual gerbe of
> `𝒳` at `x` exists and its inclusion is locally of finite type.
>
> The implication (1) ⟹ (3) is carried as the hypothesis `hForward`; see
> `AlgebraicGeometry.Stack.ExistsLocallyOfFiniteTypeResidualGerbeOfIsFiniteTypePoint` for what it
> stands for and why. The other two implications are proved.

```lean
theorem isFiniteTypePoint_tfae (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hForward : ExistsLocallyOfFiniteTypeResidualGerbeOfIsFiniteTypePoint.{u, w} B S hS 𝒳)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) :
    [IsFiniteTypePoint.{u, w} B S hS 𝒳 x,
      HasSingletonLocallyOfFiniteTypeCoverAt.{u, w} B S hS 𝒳 x,
      HasLocallyOfFiniteTypeResidualGerbeAt.{u, w} B S hS 𝒳 x].TFAE
```

**`AlgebraicGeometry.Stack.isFiniteTypePoint_tfae_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointResidualGerbeExistence.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FiniteTypePointResidualGerbeExistence.lean#L175). The attribute's comment: “the equivalence of (1) being a finite type point, (2) admitting a locally-of-finite-type 1-morphism from a one-point algebraic stack with image the point, and (3) the residual gerbe existing with locally-of-finite-type inclusion. All three implications are proved and nothing is assumed: (1) => (3) cuts the one-point algebraic stack out of the target as the strictly full subcategory of the objects fppf-locally in the image of the field-valued point, whose inclusion is fully faithful and, by Stacks 05UM at the bootstrap theorem Stacks 04S6 part (3), representable by algebraic spaces”.

> **Stacks 06G3.** For a point `x` of the point space of an algebraic stack `𝒳` over `S`, the
> following are equivalent: `x` is a finite type point; there is a one-point algebraic stack with a
> locally-of-finite-type 1-morphism to `𝒳` whose image on points is `{x}`; the residual gerbe of
> `𝒳` at `x` exists and its inclusion is locally of finite type.
>
> All three implications are proved. (1) ⟹ (3) is
> `AlgebraicGeometry.Stack.existsLocallyOfFiniteTypeResidualGerbe`, which builds the one-point
> algebraic stack as the strictly full subcategory of the objects of `𝒳` fppf-locally in the image
> of the field-valued point of condition (1) of **Stacks 06FX**; (3) ⟹ (2) is
> `AlgebraicGeometry.Stack.hasSingletonLocallyOfFiniteTypeCoverAt_of_residualGerbe` and (2) ⟹ (1) is
> `AlgebraicGeometry.Stack.isFiniteTypePoint_of_hasSingletonLocallyOfFiniteTypeCoverAt`.

```lean
theorem isFiniteTypePoint_tfae_unconditional (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val 𝒳.val.property) :
    [IsFiniteTypePoint.{u, w} B S hS 𝒳 x,
      HasSingletonLocallyOfFiniteTypeCoverAt.{u, w} B S hS 𝒳 x,
      HasLocallyOfFiniteTypeResidualGerbeAt.{u, w} B S hS 𝒳 x].TFAE
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.18, Tag 06FW](https://stacks.math.columbia.edu/tag/06FW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
