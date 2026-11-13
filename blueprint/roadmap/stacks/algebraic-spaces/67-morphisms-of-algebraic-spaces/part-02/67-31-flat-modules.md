---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFlatOverAt_exists_chartDiagram_iff_isFlatOverAtGeometricPoint, AlgebraicGeometry.Space.IsFlatOver, AlgebraicGeometry.Space.IsFlatOverAtPoint, AlgebraicGeometry.Space.isFlatOver_iff_forall_isFlatOverAtPoint, AlgebraicGeometry.Space.isFlatOver_modulePullback_of_isFinitePresentationOnSite, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_modulePullback, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_modulePullback, AlgebraicGeometry.Space.isFlatOver_modulePullback
statement: formalized
proof: formalized
---

# 67.31 Flat modules

Section 67.31 of the Stacks Project, [Tag 05VT](https://stacks.math.columbia.edu/tag/05VT). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05VU, a lemma

[Tag 05VU](https://stacks.math.columbia.edu/tag/05VU) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverAt_exists_chartDiagram_iff_isFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAtGeometricPointEquiv.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAtGeometricPointEquiv.lean#L276).

> **Stacks 05VU.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let `F` be a
> quasi-coherent `𝒪_X`-module and let `x̄` be a geometric point of `X`.  The following are
> equivalent:
>
> 1. there is a commuting square of étale scheme charts `U ⟶ V` over `f` and a point `u` of `U`
>    above the image of `x̄` in `|X|` at which the restriction of `F` to `U` is flat over `V`;
> 2. the geometric stalk `F_{x̄}` is flat over the étale local ring `𝒪_{Y, ȳ}`, where
>    `ȳ = f ∘ x̄`.
>
> Condition (1) is `AlgebraicGeometry.Space.IsFlatOverAtOnChartDiagram`, the ringed-space
> predicate of Stacks 08KT on the square, the condition "above `x`" being
> `AlgebraicGeometry.Space.ChartPoint`; condition (2) is
> `AlgebraicGeometry.Space.IsFlatOverAtGeometricPoint`.  Condition (2) mentions no chart, so the
> equivalence also says that condition (1) does not depend on the chosen square or point.

```lean
theorem isFlatOverAt_exists_chartDiagram_iff_isFlatOverAtGeometricPoint
    {Xs Ys : AlgebraicSpaces B S hS} (f : Xs ⟶ Ys)
    (F : Modules.{u, u} B S hS Xs.1 Xs.2) [F.IsQuasicoherentOnSite]
    (xbar : GeometricPoint B S hS Xs.1) :
    (∃ (d : ChartDiagram B S hS Xs.1 Ys.1 f.hom) (u : chartScheme d.U),
        ChartPoint B S hS d.U.obj.left d.U.obj.hom u xbar.image ∧
        IsFlatOverAtOnChartDiagram B S hS Xs.2 F d u) ↔
      IsFlatOverAtGeometricPoint B S hS f F xbar
```

## Tag 05VV, a definition

[Tag 05VV](https://stacks.math.columbia.edu/tag/05VV) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFlatOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModule.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModule.lean#L101). The attribute's comment: “flatness over the target”.

> **Stacks 05VV.** An `𝒪_X`-module is *flat over* `Y` along `f : X ⟶ Y` when, on every
> commuting square of étale scheme charts of `f`, its restriction to the chart of `X` is flat
> over the chart of `Y`.

```lean
noncomputable abbrev IsFlatOver (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X hX) : Prop
```

**`AlgebraicGeometry.Space.IsFlatOverAtPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModule.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModule.lean#L131). The attribute's comment: “flatness over the target at a point of |X|”.

> **Stacks 05VV at a point of `|X|`.** An `𝒪_X`-module is *flat over* `Y` *at* a point `x` of
> `|X|` when, on some commuting square of étale scheme charts of `f` and at some point of the
> chart of `X` lying over `x`, the restriction of `F` to that chart is flat over the chart of `Y`
> at that point, in the stalkwise sense of Stacks 08KT part (1) for ringed spaces.
>
> Quantifying existentially over the charts is what the source does: this is condition (1) of
> Stacks 05VU, which that lemma identifies with the geometric-stalk condition (2) at `x`.  That
> lemma is *not* unavailable in this development — it is registered, for a quasi-coherent module,
> as `AlgebraicGeometry.Space.isFlatOverAt_exists_chartDiagram_iff_isFlatOverAtGeometricPoint` of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAtGeometricPointEquiv.lean`, which is downstream
> of this file; so the identification, and with it the independence of the chosen square, is made
> there and not here.  The consequence this definition's consumers want is
> `AlgebraicGeometry.Space.isFlatOverAtPoint_iff_isFlatOverAtOnChartDiagram` of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatModulePointChartIndependence.lean`: the condition may
> be read on any one square through the point.
>
> This is the pointwise form of `AlgebraicGeometry.Space.IsFlatOver`, which asks the same
> ringed-space condition at *every* point of *every* chart square; the global predicate restricts
> to this one at every chart point, which is
> `AlgebraicGeometry.Space.isFlatOverAtPoint_of_isFlatOver`; that the global predicate is exactly
> the conjunction of this one over all `x` of `|X|` is
> `AlgebraicGeometry.Space.isFlatOver_iff_forall_isFlatOverAtPoint` of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAllPoints.lean`, again downstream of this file
> because the converse direction rests on the chart independence.

```lean
noncomputable def IsFlatOverAtPoint (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X hX) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.isFlatOver_iff_forall_isFlatOverAtPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAllPoints.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAllPoints.lean#L89). The attribute's comment: “the all-x characterisation, for a quasi-coherent module”.

> **Stacks 05VV, the all-`x` characterisation.** For a quasi-coherent `𝒪_X`-module `F`,
> flatness of `F` over `Y` in the every-chart sense of `AlgebraicGeometry.Space.IsFlatOver` holds
> exactly when `F` is flat over `Y` at every point of `|X|` in the pointwise sense of
> `AlgebraicGeometry.Space.IsFlatOverAtPoint`, which is condition (1) of Stacks 05VU at that
> point.  This is the form in which the source states the definition: `F` is flat over `Y` when
> the equivalent conditions of Stacks 05VU hold at every point of `|X|`.
>
> The forward direction holds for an arbitrary `𝒪_X`-module; quasi-coherence is what makes the
> pointwise condition chart-independent and so is needed only for the converse.

```lean
theorem isFlatOver_iff_forall_isFlatOverAtPoint {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    IsFlatOver B S hS X.2 f.hom F ↔
      ∀ x : points B S hS X.1, IsFlatOverAtPoint B S hS X.2 f.hom F x
```

## Tag 05VW, a lemma

[Tag 05VW](https://stacks.math.columbia.edu/tag/05VW) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOver_modulePullback_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFinitePresentationStability.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFinitePresentationStability.lean#L104). The attribute's comment: “the final assertion for a module of finite presentation”.

> **Stacks 05VW, the final assertion, for a module of finite presentation.**  In a cartesian
> square of algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> the inverse image of an `𝒪_X`-module of finite presentation flat over `Y` is flat over `Y'`.
>
> This is `AlgebraicGeometry.Space.isFlatOver_modulePullback`, whose two quasi-coherence instances
> finite presentation supplies: the module is quasi-coherent because it is of finite presentation,
> and its inverse image is of finite presentation by
> `AlgebraicGeometry.Space.isFinitePresentationOnSite_modulePullback`, hence quasi-coherent for the
> same reason.

```lean
theorem isFlatOver_modulePullback_of_isFinitePresentationOnSite
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : SheafOfModules.IsFinitePresentationOnSite F)
    (hflat : IsFlatOver B S hS X.2 f.hom F) :
    IsFlatOver B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F)
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean#L125). The attribute's comment: “part (1): the pullback of a module flat over the target at a point is flat over the new target at every point above it”.

> **Stacks 05VW, part (1).**  In a cartesian square of algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> let `x̄'` be a geometric point of `X'` and let `F` be an `𝒪_X`-module flat over `Y` at the image
> `x̄` of `x̄'`.  Then the pullback `(g')^* F` is flat over `Y'` at `x̄'`.
>
> At the geometric stalks this is base change of flatness over a pushout of rings: the stalk of
> `(g')^* F` at `x̄'` is `𝒪_{X', x̄'} ⊗_{𝒪_{X, x̄}} F_{x̄}` by Stacks 05VQ, and `𝒪_{X', x̄'}` is flat
> over `𝒪_{X, x̄} ⊗_{𝒪_{Y, ȳ}} 𝒪_{Y', ȳ'}`, so flatness of `F_{x̄}` over `𝒪_{Y, ȳ}` passes to
> flatness of the base change over `𝒪_{Y', ȳ'}`.

```lean
theorem isFlatOverAtGeometricPoint_modulePullback
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    (x' : GeometricPoint B S hS X'.1)
    (hF : IsFlatOverAtGeometricPoint B S hS f F (geometricPointMap g'.hom x')) :
    IsFlatOverAtGeometricPoint B S hS f' ((modulePullback B S hS g').obj F) x'
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean#L212). The attribute's comment: “part (2): relative flatness of a module at a point descends along a base change flat at the image point”.

> **Stacks 05VW, part (2).**  In a cartesian square of algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> let `x̄'` be a geometric point of `X'`, let `F` be an `𝒪_X`-module and suppose that `g` is flat
> at the image `ȳ'` of `x̄'` in `Y'`.  If the pullback `(g')^* F` is flat over `Y'` at `x̄'`, then
> `F` is flat over `Y` at the image `x̄` of `x̄'`.
>
> Flatness of `g` at `ȳ'` makes `(g')^* F` flat over `Y` at `x̄'` by Stacks 05VX, part (1); over
> the étale local rings that reads as flatness of `𝒪_{X', x̄'} ⊗_{𝒪_{X, x̄}} F_{x̄}` over
> `𝒪_{Y, ȳ}` through Stacks 05VQ.  The same flatness of `g` makes `𝒪_{X, x̄} → 𝒪_{X', x̄'}` flat,
> and it is a local homomorphism of local rings, hence faithfully flat; so flatness of `F_{x̄}`
> over `𝒪_{Y, ȳ}` follows by Stacks 0584 (2).

```lean
theorem isFlatOverAtGeometricPoint_of_modulePullback
    {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    (x' : GeometricPoint B S hS X'.1)
    (hg : IsFlatAt B S hS g.hom (geometricPointMap f'.hom x').image)
    (hF : IsFlatOverAtGeometricPoint B S hS f' ((modulePullback B S hS g').obj F) x') :
    IsFlatOverAtGeometricPoint B S hS f F (geometricPointMap g'.hom x')
```

**`AlgebraicGeometry.Space.isFlatOver_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChange.lean#L309). The attribute's comment: “the final assertion: the pullback of a quasi-coherent module flat over the target is flat over the new target”.

> **Stacks 05VW, the final assertion.**  In a cartesian square of algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> the pullback of a quasi-coherent `𝒪_X`-module flat over `Y` is flat over `Y'`.
>
> Chartwise flatness of Stacks 05VV is flatness of the geometric stalks over the étale local rings
> of the base at every geometric point, by Stacks 05VU, and that pointwise condition is carried by
> the base change at each geometric point of `X'`.

```lean
theorem isFlatOver_modulePullback {X Y X' Y' : AlgebraicSpaces B S hS} {g' : X' ⟶ X}
    {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (hpb : IsPullback g' f' f g)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    [((modulePullback B S hS g').obj F).IsQuasicoherentOnSite]
    (hF : IsFlatOver B S hS X.2 f.hom F) :
    IsFlatOver B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F)
```

**`AlgebraicGeometry.Space.mem_flatLocus_modulePullback_of_mem_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean#L109). The attribute's comment: “part (1) read at a point of the point space of Stacks 03BU, flatness at a point being membership of the relative flat locus of Stacks 0DLR”.

> **Stacks 05VW, part (1), at a point of the point space.**  In a cartesian square of
> algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> let `F` be a quasi-coherent `𝒪_X`-module and let `x'` be a point of `|X'|`.  If `F` is flat over
> `Y` at the image of `x'` in `|X|`, then the inverse image `(g')^*F` is flat over `Y'` at `x'`,
> flatness at a point being membership of the relative flat locus of Stacks 0DLR.
>
> A geometric point of `X'` above `x'` exists by Stacks 04XE, flatness at a point is flatness of
> the geometric stalk there by
> `AlgebraicGeometry.Space.mem_flatLocus_iff_isFlatOverAtGeometricPoint`, and the implication
> between the two geometric-stalk conditions is part (1) of Stacks 05VW,
> `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_modulePullback`.  The inverse image is
> quasi-coherent by Stacks 03GA.

```lean
theorem mem_flatLocus_modulePullback_of_mem_flatLocus {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y}
    {g : Y' ⟶ Y} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x' : points B S hS X'.1)
    (hx : pointsMap B S hS X'.1 g'.hom x' ∈ flatLocus B S hS X.2 f.hom F) :
    x' ∈ flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F)
```

**`AlgebraicGeometry.Space.mem_flatLocus_of_mem_flatLocus_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean#L148). The attribute's comment: “part (2) read at a point of the point space of Stacks 03BU, flatness at a point being membership of the relative flat locus of Stacks 0DLR”.

> **Stacks 05VW, part (2), at a point of the point space.**  In a cartesian square of
> algebraic spaces
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> let `F` be a quasi-coherent `𝒪_X`-module, let `x'` be a point of `|X'|` and suppose that `g` is
> flat at the image of `x'` in `|Y'|`.  If the inverse image `(g')^*F` is flat over `Y'` at `x'`,
> then `F` is flat over `Y` at the image of `x'` in `|X|`, flatness at a point being membership of
> the relative flat locus of Stacks 0DLR.
>
> The proof is that of part (1) read in the opposite direction: a geometric point of `X'` above
> `x'` exists by Stacks 04XE, flatness at a point is flatness of the geometric stalk there by
> `AlgebraicGeometry.Space.mem_flatLocus_iff_isFlatOverAtGeometricPoint`, and the implication
> between the two geometric-stalk conditions is part (2) of Stacks 05VW,
> `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_modulePullback`.  The inverse image is
> quasi-coherent by Stacks 03GA.

```lean
theorem mem_flatLocus_of_mem_flatLocus_modulePullback {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y}
    {g : Y' ⟶ Y} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (x' : points B S hS X'.1)
    (hg : IsFlatAt B S hS g.hom (pointsMap B S hS X'.1 f'.hom x'))
    (hx : x' ∈ flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F)) :
    pointsMap B S hS X'.1 g'.hom x' ∈ flatLocus B S hS X.2 f.hom F
```

**`AlgebraicGeometry.Space.isFlatOverAtPoint_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleBaseChangePoint.lean#L199). The attribute's comment: “parts (1) and (2) at a point of |X'|, flatness at a point being Stacks 05VV (1), and the final assertion, for a quasi-coherent module”.

> **Stacks 05VW.**  Let
>
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
>
> be a cartesian square of algebraic spaces over `S`, let `F` be a quasi-coherent `𝒪_X`-module
> and write `F' = (g')^*F`.  For every point `x'` of `|X'|` with image `x` in `|X|`:
>
> 1. if `F` is flat over `Y` at `x`, then `F'` is flat over `Y'` at `x'`;
> 2. if `g` is flat at the image `f'(x')` of `x'` in `|Y'|` and `F'` is flat over `Y'` at `x'`,
>    then `F` is flat over `Y` at `x`;
>
> and in particular, if `F` is flat over `Y`, then `F'` is flat over `Y'`.
>
> Flatness of a module over the target at a point of the point space is
> `AlgebraicGeometry.Space.IsFlatOverAtPoint` of Stacks 05VV, flatness over the target is
> `AlgebraicGeometry.Space.IsFlatOver` of Stacks 05VV, and flatness of `g` at a point is
> `AlgebraicGeometry.Space.IsFlatAt` of Stacks 03ML part (2).
>
> At a point, a geometric point of `X'` above `x'` exists by Stacks 0488 part (1), flatness at a
> point is flatness of the geometric stalk there by Stacks 05VU,
> `AlgebraicGeometry.Space.mem_flatLocus_iff_isFlatOverAtGeometricPoint`, and the two parts are
> then `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_modulePullback` and
> `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_modulePullback`.  The final assertion is
> `AlgebraicGeometry.Space.isFlatOver_modulePullback`, the quasi-coherence of `F'` it asks for
> being Stacks 03GA,
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePullback_of_isQuasicoherentOnSite`, so that
> nothing beyond quasi-coherence of `F` is assumed.

```lean
theorem isFlatOverAtPoint_baseChange {g' : X' ⟶ X} {f' : X' ⟶ Y'}
    {f : X ⟶ Y} {g : Y' ⟶ Y} (hpb : IsPullback g' f' f g) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] :
    (∀ x' : points B S hS X'.1,
        IsFlatOverAtPoint B S hS X.2 f.hom F (pointsMap B S hS X'.1 g'.hom x') →
          IsFlatOverAtPoint B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) x') ∧
      (∀ x' : points B S hS X'.1, IsFlatAt B S hS g.hom (pointsMap B S hS X'.1 f'.hom x') →
        IsFlatOverAtPoint B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) x' →
          IsFlatOverAtPoint B S hS X.2 f.hom F (pointsMap B S hS X'.1 g'.hom x')) ∧
      (IsFlatOver B S hS X.2 f.hom F →
        IsFlatOver B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F))
```

## Tag 05VX, a lemma

[Tag 05VX](https://stacks.math.columbia.edu/tag/05VX) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean#L119). The attribute's comment: “part (1): flatness of a module at a point composes with flatness of the base”.

> If an `𝒪_X`-module `F` is flat at a geometric point `x̄` of `X` over `Y` and `Y` is flat
> over `Z` at the image `ȳ` of `x̄`, then `F` is flat at `x̄` over `Z`.
>
> Over the étale local rings this is transitivity of flatness: `F_{x̄}` is flat over `𝒪_{Y, ȳ}`
> and `𝒪_{Y, ȳ}` is flat over `𝒪_{Z, z̄}`.

```lean
theorem isFlatOverAtGeometricPoint_comp {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (F : Modules.{u, m} B S hS X.1 X.2)
    (xbar : GeometricPoint B S hS X.1)
    (hF : IsFlatOverAtGeometricPoint B S hS f F xbar)
    (hg : IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image) :
    IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar
```

**`AlgebraicGeometry.Space.isFlatAt_of_isFaithfullyFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean#L137). The attribute's comment: “part (3): flatness of the base at a point descends from a faithfully flat geometric stalk”.

> If the geometric stalk `F_{x̄}` of an `𝒪_X`-module at a geometric point `x̄` of `X` is a
> faithfully flat module over the étale local ring `𝒪_{Y, ȳ}` of the image `ȳ` of `x̄`, and `F` is
> flat at `x̄` over `Z`, then `Y` is flat over `Z` at `ȳ`.
>
> Over the étale local rings this is flat permanence (Stacks 039V): `F_{x̄}` is flat over
> `𝒪_{Z, z̄}` and faithfully flat over `𝒪_{Y, ȳ}`, hence `𝒪_{Y, ȳ}` is flat over `𝒪_{Z, z̄}`.

```lean
theorem isFlatAt_of_isFaithfullyFlatOverAtGeometricPoint {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (F : Modules.{u, m} B S hS X.1 X.2)
    (xbar : GeometricPoint B S hS X.1)
    (hff : IsFaithfullyFlatOverAtGeometricPoint B S hS f F xbar)
    (hfg : IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar) :
    IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image
```

**`AlgebraicGeometry.Space.isFlatAt_of_nontrivial_fibre_of_isFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleComposition.lean#L159). The attribute's comment: “part (2): flatness of the base at a point descends from a module flat over both and with nonzero fibre at a representative of the point”.

> Let `F` be an `𝒪_X`-module and let `x̄` be a geometric point of `X` with image `ȳ` in `Y`.
> If `F` is flat at `x̄` over `Y`, the fibre of `F` at `x̄` is nonzero and `F` is flat at `x̄` over
> `Z`, then `Y` is flat over `Z` at `ȳ`.
>
> The fibre of `F` at `x̄` is the quotient `F_{x̄} ⧸ 𝔪_{x̄} F_{x̄}` of the geometric stalk by the
> maximal ideal of `𝒪_{X, x̄}`; it is the pullback `x̄^* F` of `F` along `x̄`, regarded as a
> representative of its image point with values in an algebraically closed field.  Since
> `𝒪_{Y, ȳ} → 𝒪_{X, x̄}` is a local homomorphism, nonvanishing of that fibre forces the fibre of
> `F_{x̄}` over `𝒪_{Y, ȳ}` to be nonzero as well, so that `F_{x̄}` is a faithfully flat
> `𝒪_{Y, ȳ}`-module (Stacks 00HP) and part (3) applies.

```lean
theorem isFlatAt_of_nontrivial_fibre_of_isFlatOverAtGeometricPoint
    {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (F : Modules.{u, m} B S hS X.1 X.2)
    (xbar : GeometricPoint B S hS X.1)
    (hf : IsFlatOverAtGeometricPoint B S hS f F xbar)
    (hfibre :
      letI := isLocalRing_etaleLocalRing B S hS X.1 X.2 xbar
      Nontrivial ((geometricModuleStalk B S hS X xbar F) ⧸
        (IsLocalRing.maximalIdeal (etaleLocalRing B S hS X.1 xbar)) •
          (⊤ : Submodule (etaleLocalRing B S hS X.1 xbar)
            (geometricModuleStalk B S hS X xbar F))))
    (hfg : IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar) :
    IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image
```

## Tag 05VY, a lemma

[Tag 05VY](https://stacks.math.columbia.edu/tag/05VY) in the Stacks Project.

**`AlgebraicGeometry.Space.relativeFlatnessPermanence_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeFlatnessAlongFlatPullback.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeFlatnessAlongFlatPullback.lean#L91).

> **Stacks 05VY.**  Let `S` be a scheme contained in the big fppf site `B`, let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over `S`, let `G` be a
> quasi-coherent `𝒪_Y`-module and let `x` be a point of `|X|`, with image `y` in `|Y|`.  Then:
>
> 1. if `f` is flat at `x`, then `G` is flat over `Z` at `y` if and only if `f^*G` is flat over
>    `Z` at `x`;
> 2. in particular, if `f` is surjective and flat, then `G` is flat over `Z` if and only if
>    `f^*G` is flat over `Z`.
>
> A geometric point above `x` turns each side of (1) into the geometric-stalk condition (2) of
> Stacks 05VU; there the stalk of `f^*G` is `𝒪_{X, x̄} ⊗_{𝒪_{Y, ȳ}} G_ȳ` by Stacks 05VQ and
> `𝒪_{Y, ȳ} ⟶ 𝒪_{X, x̄}` is faithfully flat, so the equivalence is Stacks 0584 (2).  For (2) the
> morphism `f` is flat at every point, and surjectivity of `|X| → |Y|` puts a point of `|X|`
> above every point of `|Y|`.

```lean
theorem relativeFlatnessPermanence_modulePullback (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (G : Modules.{u, u} B S hS Y.1 Y.2) [G.IsQuasicoherentOnSite] (x : points B S hS X.1) :
    (IsFlatAt B S hS f.hom x →
        (IsFlatOverAtPoint B S hS Y.2 g.hom G (pointsMap B S hS X.1 f.hom x) ↔
          IsFlatOverAtPoint B S hS X.2 (f ≫ g).hom ((modulePullback B S hS f).obj G) x)) ∧
      (IsSurjective B S hS f.hom → IsFlat B S hS f.hom →
        (IsFlatOver B S hS Y.2 g.hom G ↔
          IsFlatOver B S hS X.2 (f ≫ g).hom ((modulePullback B S hS f).obj G)))
```

## Tag 0CVU, a lemma

[Tag 0CVU](https://stacks.math.columbia.edu/tag/0CVU) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_of_isFlatOver_of_fullSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleUniversallyOpen.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleUniversallyOpen.lean#L123). References: EGA IV (11.3.1), “f|U open”; EGA IV (2.4.6); EGA IV (15.2.1), “more general”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is locally of finite
> presentation and let `𝓕` be an `𝒪_X`-module which, on charts, is quasi-coherent, of finite type,
> of full support and flat over `Y`. Then `f` is universally open.

```lean
theorem universallyOpen_of_isFlatOver_of_fullSupport
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X hX)
    (hf : IsLocallyOfFinitePresentation B S hS f)
    (hqc : IsQuasicoherentOnCharts B S hS hX F) (hft : IsFiniteTypeOnCharts B S hS hX F)
    (hsupp : HasFullSupportOnCharts B S hS hX F) (hflat : IsFlatOver B S hS hX f F) :
    UniversallyOpen B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.31, Tag 05VT](https://stacks.math.columbia.edu/tag/05VT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
