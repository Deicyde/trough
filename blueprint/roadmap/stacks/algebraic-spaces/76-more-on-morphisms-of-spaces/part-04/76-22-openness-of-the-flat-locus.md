---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnCharts, AlgebraicGeometry.Space.isOpen_setOf_forall_isFlatOverAtGeometricPoint, AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage, AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_and_isOpen, AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_of_isFinitePresentationOnSite, AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_and_isOpen_of_isFinitePresentationOnSite
statement: formalized
proof: formalized
---

# 76.22 Openness of the flat locus

Section 76.22 of the Stacks Project, [Tag 05WU](https://stacks.math.columbia.edu/tag/05WU). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05WV, a theorem

[Tag 05WV](https://stacks.math.columbia.edu/tag/05WV) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOpen.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOpen.lean#L105). The attribute's comment: “openness of the flat locus; quasi-coherence and finite presentation of the module are read on the Zariski site of every etale scheme chart”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is locally of finite
> presentation and let `F` be an `𝒪_X`-module which is quasi-coherent of finite presentation on
> charts. The set of points of `|X|` at which `F` is flat over `Y` is open.

```lean
theorem isOpen_flatLocus_of_isFinitePresentationOnCharts (hX : IsAlgebraicSpace B S hS X)
    (f : X ⟶ Y) (F : Modules.{u, u} B S hS X hX)
    (hf : IsLocallyOfFinitePresentation B S hS f)
    (hqc : IsQuasicoherentOnCharts B S hS hX F)
    (hfp : IsFinitePresentationOnCharts B S hS hX F) :
    IsOpen (flatLocus B S hS hX f F)
```

**`AlgebraicGeometry.Space.isOpen_setOf_forall_isFlatOverAtGeometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOpen.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusOpen.lean#L176). The attribute's comment: “openness of the flat locus, read through condition (2) of Stacks 05VU; finite presentation of the module is read on the Zariski site of every etale scheme chart”.

> For a morphism of algebraic spaces locally of finite presentation and a quasi-coherent module
> which is of finite presentation on charts, the set of points of the source over which the
> geometric stalks of the module are flat over the étale local rings of the target is open.

```lean
theorem isOpen_setOf_forall_isFlatOverAtGeometricPoint (f : Xs ⟶ Ys)
    (F : Modules.{u, u} B S hS Xs.1 Xs.2) [F.IsQuasicoherentOnSite]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hfp : IsFinitePresentationOnCharts B S hS Xs.2 F) :
    IsOpen {x : points B S hS Xs.1 | ∀ xbar : GeometricPoint B S hS Xs.1,
      xbar.image = x → IsFlatOverAtGeometricPoint B S hS f F xbar}
```

## Tag 05WW, a lemma

[Tag 05WW](https://stacks.math.columbia.edu/tag/05WW) in the Stacks Project.

**`AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChange.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChange.lean#L161). The attribute's comment: “the set equality, with Stacks 05VW at a point carried as the hypothesis `h05VW`; the finite-presentation hypotheses of the source are not needed for it and enter through Stacks 05WV in flatLocus\_modulePullback\_eq\_preimage\_and\_isOpen”.

> **Stacks 05WW, the set equality.** In a cartesian square of algebraic spaces over `S` with
> `f : X ⟶ Y`, `g : Y' ⟶ Y`, `f' : X' ⟶ Y'` and `g' : X' ⟶ X` whose base morphism `g` is flat,
> the locus of points of `|X'|` at which the inverse image `(g')^*F` of a quasi-coherent
> `𝒪_X`-module is flat over `Y'` is the inverse image under `|g'| : |X'| ⟶ |X|` of the locus of
> points of `|X|` at which `F` is flat over `Y`.
>
> Both inclusions are the two implications of Stacks 05VW at a point, carried as `h05VW`: the
> inclusion `⊆` is its second implication, flatness of `g` being read pointwise by Stacks 03MM
> (`AlgebraicGeometry.Space.isFlat_iff_forall_isFlatAt`), and the inclusion `⊇` is its first.  The
> finite-presentation hypotheses of Stacks 05WW are not needed for the equality; they are what
> makes the right-hand side open, by Stacks 05WV, and are carried by
> `AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_and_isOpen`.

```lean
theorem flatLocus_modulePullback_eq_preimage
    (h05VW : IsFlatAtPointStableUnderBaseChange B S hS) {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'}
    {g' : X' ⟶ X} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hqc : IsQuasicoherentOnCharts B S hS X.2 F)
    (hg : IsFlat B S hS g.hom) :
    flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' flatLocus B S hS X.2 f.hom F
```

**`AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_and_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChange.lean#L187). The attribute's comment: “the locus on the base change is the inverse image of the open subset of Stacks 05WV, hence open; Stacks 05VW at a point is carried as the hypothesis `h05VW`”.

> **Stacks 05WW.** Let a cartesian square of algebraic spaces over `S` be given, with
> `f : X ⟶ Y`, `g : Y' ⟶ Y`, `f' : X' ⟶ Y'` and `g' : X' ⟶ X`.  Assume `g` is flat, `f` is
> locally of finite presentation, and the `𝒪_X`-module `F` is quasi-coherent of finite
> presentation on the étale scheme charts.  Then the locus of points of `|X'|` at which the
> inverse image `(g')^*F` is flat over `Y'` is the inverse image under `|g'| : |X'| ⟶ |X|` of the
> open subset of Stacks 05WV, and is therefore itself open.
>
> The equality is `AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage`, which is where
> the carried Stacks 05VW and the flatness of `g` are used.  Openness of the subset of `|X|` is
> Stacks 05WV, `AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnCharts`, which
> is where the two finite-presentation hypotheses are used, and the map on points is continuous by
> clause (2) of Stacks 03BX.

```lean
theorem flatLocus_modulePullback_eq_preimage_and_isOpen
    (h05VW : IsFlatAtPointStableUnderBaseChange B S hS) {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'}
    {g' : X' ⟶ X} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hg : IsFlat B S hS g.hom)
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hqc : IsQuasicoherentOnCharts B S hS X.2 F)
    (hfp : IsFinitePresentationOnCharts B S hS X.2 F) :
    flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) =
        pointsMap B S hS X'.1 g'.hom ⁻¹' flatLocus B S hS X.2 f.hom F ∧
      IsOpen (flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F))
```

**`AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeFinitePresentation.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeFinitePresentation.lean#L73). The attribute's comment: “the set equality; the finite-presentation hypotheses of the source enter through Stacks 05WV in flatLocus\_modulePullback\_eq\_preimage\_and\_isOpen\_of\_isFinitePresentationOnSite”.

> **Stacks 05WW, the set equality, with no hypothesis beyond the source's own.** In a
> cartesian square of algebraic spaces over `S` with `f : X ⟶ Y`, `g : Y' ⟶ Y`, `f' : X' ⟶ Y'`
> and `g' : X' ⟶ X` whose base morphism `g` is flat, the locus of points of `|X'|` at which the
> inverse image `(g')^*F` of an `𝒪_X`-module of finite presentation on the small étale site is
> flat over `Y'` is the inverse image under `|g'| : |X'| ⟶ |X|` of the locus of points of `|X|`
> at which `F` is flat over `Y`.
>
> Both inclusions are the two implications of Stacks 05VW, read at a geometric representative of
> the point: the inclusion `⊆` is
> `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_modulePullback`, flatness of `g` being
> read pointwise by Stacks 03MM (`AlgebraicGeometry.Space.isFlat_iff_forall_isFlatAt`), and the
> inclusion `⊇` is `AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_modulePullback`.  So
> nothing is carried here: `AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage` states
> the same equality for a module which is quasi-coherent only on the charts, and has to carry
> Stacks 05VW as a hypothesis because the comparison with geometric points is unavailable at that
> reading.
>
> Finite presentation of `f` is not needed for the equality, and finite presentation of `F`
> enters only as the quasi-coherence of `F` and of its inverse image under which flatness at a
> point of `|X|` agrees with flatness at a geometric point above it; the finite-presentation
> hypotheses of Stacks 05WW are what makes the right-hand side open, by Stacks 05WV, and are
> carried by `flatLocus_modulePullback_eq_preimage_and_isOpen_of_isFinitePresentationOnSite`.

```lean
theorem flatLocus_modulePullback_eq_preimage_of_isFinitePresentationOnSite
    {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'}
    {g' : X' ⟶ X} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : SheafOfModules.IsFinitePresentationOnSite F)
    (hg : IsFlat B S hS g.hom) :
    flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) =
      pointsMap B S hS X'.1 g'.hom ⁻¹' flatLocus B S hS X.2 f.hom F
```

**`AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_and_isOpen_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeFinitePresentation.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleLocusBaseChangeFinitePresentation.lean#L113). The attribute's comment: “the locus on the base change is the inverse image of the open subset of Stacks 05WV, hence open”.

> **Stacks 05WW, with no hypothesis beyond the source's own.** Let a cartesian square of
> algebraic spaces over `S` be given, with `f : X ⟶ Y`, `g : Y' ⟶ Y`, `f' : X' ⟶ Y'` and
> `g' : X' ⟶ X`.  Assume `g` is flat, `f` is locally of finite presentation, and the `𝒪_X`-module
> `F` is of finite presentation on the small étale site.  Then the locus of points of `|X'|` at
> which the inverse image `(g')^*F` is flat over `Y'` is the inverse image under
> `|g'| : |X'| ⟶ |X|` of the open subset of Stacks 05WV, and is therefore itself open.
>
> The equality is
> `AlgebraicGeometry.Space.flatLocus_modulePullback_eq_preimage_of_isFinitePresentationOnSite`,
> which is where Stacks 05VW and the flatness of `g` are used.  Openness of the subset of `|X|`
> is Stacks 05WV, `AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnCharts`,
> whose chartwise hypotheses on `F` are supplied by the finite presentation of `F` on the site,
> and the map on points is continuous by clause (2) of Stacks 03BX.

```lean
theorem flatLocus_modulePullback_eq_preimage_and_isOpen_of_isFinitePresentationOnSite
    {f : X ⟶ Y} {g : Y' ⟶ Y} {f' : X' ⟶ Y'}
    {g' : X' ⟶ X} (sq : IsPullback g'.hom f'.hom f.hom g.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hg : IsFlat B S hS g.hom)
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hF : SheafOfModules.IsFinitePresentationOnSite F) :
    flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F) =
        pointsMap B S hS X'.1 g'.hom ⁻¹' flatLocus B S hS X.2 f.hom F ∧
      IsOpen (flatLocus B S hS X'.2 f'.hom ((modulePullback B S hS g').obj F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.22, Tag 05WU](https://stacks.math.columbia.edu/tag/05WU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
