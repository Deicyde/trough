---
declaration: section
origin: cited
lean: Stacks.Curves.hasAtWorstNodalFibresOfDimensionOne_iff, AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne, AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_of_smoothOfRelativeDimension, AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne.of_isPullback, AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange, AlgebraicGeometry.nodalLocus_isGreatest, AlgebraicGeometry.nodalLocus_baseChange, AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_comp_etale
statement: formalized
proof: formalized
---

# 53.20 Families of nodal curves

Section 53.20 of the Stacks Project, [Tag 0C58](https://stacks.math.columbia.edu/tag/0C58). 12 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C59, a lemma

[Tag 0C59](https://stacks.math.columbia.edu/tag/0C59) in the Stacks Project.

**`Stacks.Curves.hasAtWorstNodalFibresOfDimensionOne_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyCriterion.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyCriterion.lean#L348). The attribute's comment: “condition (1) is `Stacks.Curves.HasAtWorstNodalFibresOfDimensionOne` and condition (2) is `AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne`”.

> **Stacks Project, Tag 0C59.**  A morphism of schemes is flat, locally of finite presentation
> with every nonempty fibre equidimensional of dimension one and with at-worst-nodal singularities
> exactly when it is syntomic of relative dimension one and the closed subscheme cut out by the
> first Fitting ideal of its relative differentials is unramified over the base.
>
> Everything except the nodal condition on the fibres is
> `AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_iff_fibres`, which reads that condition
> as condition (2) of Tag 0C4E; Tag 0C4E
> (`Stacks.Curves.hasAtWorstNodalSingularities_iff_lci_and_unramified_relativeSingularIdeal`)
> applied to a fibre trades the two.  Its hypotheses on the fibre are the equidimensionality and
> the dimension, which both sides of the equivalence provide for a nonempty fibre, and local
> finite type of the fibre's structure morphism, which follows from local finite presentation of
> `f`; over an empty fibre condition (2) holds vacuously.

```lean
theorem hasAtWorstNodalFibresOfDimensionOne_iff {X S : Scheme.{u}} (f : X ⟶ S) :
    HasAtWorstNodalFibresOfDimensionOne f ↔ IsAtWorstNodalOfRelativeDimensionOne f
```

## Tag 0C5A, a definition

[Tag 0C5A](https://stacks.math.columbia.edu/tag/0C5A) in the Stacks Project.

**`AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank136/AtWorstNodalRelativeDimensionOne.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/F6Rank136/AtWorstNodalRelativeDimensionOne.lean#L48).

> A morphism is at-worst-nodal of relative dimension one if it is syntomic of relative
> dimension one and its relative singular subscheme is unramified over the base.

```lean
public abbrev IsAtWorstNodalOfRelativeDimensionOne {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 0CD7, a lemma

[Tag 0CD7](https://stacks.math.columbia.edu/tag/0CD7) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_of_smoothOfRelativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank136/SmoothIsNodal.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/F6Rank136/SmoothIsNodal.lean#L108).

> **Stacks Project, Tag 0CD7.** A morphism of schemes smooth of relative dimension one is
> at-worst-nodal of relative dimension one: it is syntomic with one-dimensional fibres, and its
> relative singular subscheme is empty, hence unramified over the base.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_of_smoothOfRelativeDimension
    {X S : Scheme.{u}} (f : X ⟶ S) [SmoothOfRelativeDimension 1 f] :
    IsAtWorstNodalOfRelativeDimensionOne f
```

## Tag 0C5B, a lemma

[Tag 0C5B](https://stacks.math.columbia.edu/tag/0C5B) in the Stacks Project.

**`AlgebraicGeometry.IsAtWorstNodalOfRelativeDimensionOne.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyBaseChange.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyBaseChange.lean#L74).

> Let `f : X ⟶ S` be at-worst-nodal of relative dimension one. Then so is any base change
> `f' : X' ⟶ S'` of `f`, presented by an arbitrary cartesian square.

```lean
public theorem IsAtWorstNodalOfRelativeDimensionOne.of_isPullback {X' X S' S : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S} (h : IsPullback g' f' f g)
    (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    IsAtWorstNodalOfRelativeDimensionOne f'
```

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean#L101).

> **Stacks 0C5B.** A base change of a morphism which is at-worst-nodal of relative dimension
> one is again at-worst-nodal of relative dimension one.

```lean
public instance isAtWorstNodalOfRelativeDimensionOne_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsAtWorstNodalOfRelativeDimensionOne.{u} : MorphismProperty Scheme.{u})
```

## Tag 0DSC, a lemma

[Tag 0DSC](https://stacks.math.columbia.edu/tag/0DSC) in the Stacks Project.

**`AlgebraicGeometry.nodalLocus_isGreatest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocus.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocus.lean#L433). The attribute's comment: “the maximal open subscheme”.

> **Stacks Project, Tag 0DSC.** For a morphism of schemes which is flat and locally of finite
> presentation there is a maximal open subscheme of its source on which it is at-worst-nodal of
> relative dimension one: the restriction of the morphism to `nodalLocus f` is at-worst-nodal of
> relative dimension one, and every open subscheme with that property is contained in
> `nodalLocus f`.

```lean
theorem nodalLocus_isGreatest {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] :
    IsGreatest {U : X.Opens | IsAtWorstNodalOfRelativeDimensionOne (U.ι ≫ f)} (nodalLocus f)
```

**`AlgebraicGeometry.nodalLocus_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocus.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocus.lean#L443). The attribute's comment: “compatibility with base change”.

> **Stacks Project, Tag 0DSC.** Formation of the maximal at-worst-nodal open subscheme
> commutes with arbitrary base change: in a cartesian square with right edge a flat morphism `f`
> locally of finite presentation and base edge `g`, the nodal locus of the base change `f'` of `f`
> is the inverse image of the nodal locus of `f`.

```lean
theorem nodalLocus_baseChange {X' X S' S : Scheme.{u}} (g' : X' ⟶ X) (f' : X' ⟶ S') (f : X ⟶ S)
    (g : S' ⟶ S) (sq : IsPullback g' f' f g) [Flat f] [LocallyOfFinitePresentation f] :
    nodalLocus f' = g' ⁻¹ᵁ nodalLocus f
```

## Tag 0C5C, a lemma

[Tag 0C5C](https://stacks.math.columbia.edu/tag/0C5C) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_comp_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleComposition.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleComposition.lean#L152).

> **Stacks Project, Tag 0C5C.** Precomposing an at-worst-nodal morphism of relative
> dimension one with an étale morphism again gives an at-worst-nodal morphism of relative
> dimension one.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_comp_etale {X Y S : Scheme.{u}}
    (f : X ⟶ S) (g : Y ⟶ X) [Etale g] (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    IsAtWorstNodalOfRelativeDimensionOne (g ≫ f)
```

## Tag 0CD8, a lemma

[Tag 0CD8](https://stacks.math.columbia.edu/tag/0CD8) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_comp_etale_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean#L193).

> **Stacks 0CD8.** Composing a morphism which is at-worst-nodal of relative dimension one
> with an étale morphism of the base again gives a morphism which is at-worst-nodal of relative
> dimension one.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_comp_etale_base {X S' S : Scheme.{u}}
    (f : X ⟶ S') (g : S' ⟶ S) [Etale g] (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    IsAtWorstNodalOfRelativeDimensionOne (f ≫ g)
```

## Tag 0C5D, a lemma

[Tag 0C5D](https://stacks.math.columbia.edu/tag/0C5D) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_iff_of_etaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleLocalOnSource.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleLocalOnSource.lean#L188).

> **Stacks Project, Tag 0C5D.** Let `f : X ⟶ S` be a morphism of schemes and let
> `{U i ⟶ X}` be an étale covering. The following are equivalent:
>
> 1. `f` is at-worst-nodal of relative dimension one;
> 2. each `U i ⟶ S` is at-worst-nodal of relative dimension one.
>
> In other words, being at-worst-nodal of relative dimension one is étale local on the source.

```lean
public theorem isAtWorstNodalOfRelativeDimensionOne_iff_of_etaleCovering {X S : Scheme.{u}}
    (f : X ⟶ S) {ι : Type*} {U : ι → Scheme.{u}} (g : ∀ i, U i ⟶ X)
    (hg : Presieve.ofArrows U g ∈ Scheme.etalePrecoverage X) :
    IsAtWorstNodalOfRelativeDimensionOne f ↔
      ∀ i, IsAtWorstNodalOfRelativeDimensionOne (g i ≫ f)
```

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_isLocalAtSource_etale`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean#L287).

> **Stacks 0C5D.** Being at-worst-nodal of relative dimension one is étale local on the
> source: a morphism has the property exactly when all of its restrictions to the members of an
> étale covering of its source do.

```lean
public instance isAtWorstNodalOfRelativeDimensionOne_isLocalAtSource_etale :
    MorphismProperty.IsLocalAtSource
      (@IsAtWorstNodalOfRelativeDimensionOne.{u} : MorphismProperty Scheme.{u})
      Scheme.etalePrecoverage
```

## Tag 0C5E, a lemma

[Tag 0C5E](https://stacks.math.columbia.edu/tag/0C5E) in the Stacks Project.

**`AlgebraicGeometry.isAtWorstNodalOfRelativeDimensionOne_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalLocality.lean#L118).

> **Stacks 0C5E.** Being at-worst-nodal of relative dimension one is fpqc local on the
> target: a morphism has the property exactly when all of its base changes along the members of
> an fpqc covering of its target do.

```lean
public instance isAtWorstNodalOfRelativeDimensionOne_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@IsAtWorstNodalOfRelativeDimensionOne.{u} : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 0C5F, a lemma

[Tag 0C5F](https://stacks.math.columbia.edu/tag/0C5F) in the Stacks Project.

**`AlgebraicGeometry.exists_isAtWorstNodalOfRelativeDimensionOne_baseChange_of_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank136/AtWorstNodalDescentAlongLimit.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/F6Rank136/AtWorstNodalDescentAlongLimit.lean#L291).

> **Stacks Project, Tag 0C5F.** Let a scheme be the limit of a cofiltered inverse system of
> schemes with affine transition morphisms, and let `f₀ : X₀ ⟶ Y₀` be a morphism locally of finite
> presentation over a stage, with that stage and both of `X₀`, `Y₀` quasi-compact and
> quasi-separated. If the base change of `f₀` to the limit is at-worst-nodal of relative dimension
> one, then its base change to some later stage is at-worst-nodal of relative dimension one.

```lean
public theorem exists_isAtWorstNodalOfRelativeDimensionOne_baseChange_of_limitBaseChange
    {I : Type u} [Category.{u} I] (D : I ⥤ Scheme.{u}) (c : Cone D) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀) [IsCofiltered I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    (hf₀ : LocallyOfFinitePresentation f₀.left) (hc : IsLimit c)
    (hf : IsAtWorstNodalOfRelativeDimensionOne
      ((Over.pullback (c.π.app i₀)).map f₀).left) :
    ∃ (i : I) (g : i ⟶ i₀), IsAtWorstNodalOfRelativeDimensionOne
      ((Over.pullback (D.map g)).map f₀).left
```

## Tag 0CBX, a lemma

[Tag 0CBX](https://stacks.math.columbia.edu/tag/0CBX) in the Stacks Project.

**`Stacks.Curves.exists_algEquiv_adicCompletion_quotient_mvPowerSeries_of_isSplitNode`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyCompletedLocalRing.lean, line 2062](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyCompletedLocalRing.lean#L2062).

> The completion at a split node of a flat, locally finite-type family over a Noetherian
> local base is a nodal smoothing `A⟦x,y⟧/(xy-h)` over the completed base ring `A`.

```lean
theorem exists_algEquiv_adicCompletion_quotient_mvPowerSeries_of_isSplitNode
    {T S : Scheme.{u}} (f : T ⟶ S) (t : T)
    (hflat : AlgebraicGeometry.IsFlatAt f.toLRSHom.toShHom t)
    [IsNoetherianRing (S.presheaf.stalk (f t))]
    [LocallyOfFiniteType f]
    (hnode : letI := f.fiberOverSpecResidueField (f t)
      IsSplitNode (S.residueField (f t)) (f.fiber (f t)) (f.asFiber t)) :
    let R := S.presheaf.stalk (f t)
    let Q := T.presheaf.stalk t
    let A := AdicCompletion (maximalIdeal R) R
    let B := AdicCompletion (maximalIdeal Q) Q
    let φ : A →+* B := adicCompletionMap (f.stalkMap t).hom
      (maximalIdeal R) (maximalIdeal Q)
      (map_maximalIdeal_le (f.stalkMap t).hom)
    letI : Algebra A B := φ.toAlgebra
    ∃ h : A, h ∈ maximalIdeal A ∧
      Nonempty ((MvPowerSeries (Fin 2) A ⧸
        Ideal.span {MvPowerSeries.X 0 * MvPowerSeries.X 1 - MvPowerSeries.C h}) ≃ₐ[A] B)
```

## Tag 0GKA, a lemma

[Tag 0GKA](https://stacks.math.columbia.edu/tag/0GKA) in the Stacks Project.

**`Stacks.AlgebraicGeometry.NodalFamilyCohomology.isIso_c_and_isIso_c_of_isPullback_of_isAtWorstNodal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean#L266). The attribute's comment: “(a): `f_*𝒪_X = 𝒪_S`, as invertibility of `f.c`, and the same for every base change, stated for every cartesian square over `S`”.

> **[Stacks, Tag 0GKA], part (a).** Let `f : X ⟶ S` be proper and at-worst-nodal of relative
> dimension one, with geometrically connected fibres. Then `f_*𝒪_X = 𝒪_S`, i.e. the comparison
> `f.c : 𝒪_S ⟶ f_*𝒪_X` is invertible, and this holds after any base change: for every cartesian
> square `X' ⟶ X`, `f' : X' ⟶ S'`, `S' ⟶ S`, the comparison `f'.c` is invertible.
>
> This is [Stacks, Tag 0E0L]: `f` is flat and locally of finite presentation, being syntomic, and
> geometrically reduced by `geometricallyReduced_of_isAtWorstNodal`.

```lean
theorem isIso_c_and_isIso_c_of_isPullback_of_isAtWorstNodal (f : X ⟶ S) [IsProper f]
    [GeometricallyConnected f] (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    IsIso f.c ∧ ∀ {X' S' : Scheme.{u}} {g : S' ⟶ S} {g' : X' ⟶ X} {f' : X' ⟶ S'},
      IsPullback g' f' f g → IsIso f'.c
```

**`Stacks.AlgebraicGeometry.NodalFamilyCohomology.isFiniteLocallyFree_rightDerived_one_and_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean#L319). The attribute's comment: “(b): `R¹f_*𝒪_X` is finite locally free, and its formation commutes with any base change, read over every quasi-compact quasi-separated open of the base, where the base-change map of Tag 0EX3 is defined”.

> **[Stacks, Tag 0GKA], part (b).** Let `f : X ⟶ S` be proper and at-worst-nodal of relative
> dimension one, with geometrically connected fibres. Then `R¹f_*𝒪_X` is a finite locally free
> `𝒪_S`-module, and its formation commutes with any base change: over every quasi-compact and
> quasi-separated open `V ⊆ S` (for instance every affine open, or `S` itself when `S` is
> quasi-compact and quasi-separated), for every cartesian square `X'' ⟶ f⁻¹(V)`, `X'' ⟶ Y''`,
> `Y'' ⟶ V`, the canonical map `h^* R¹(f ∣_ V)_*𝒪 ⟶ R¹f''_* (h')^*𝒪` of [Stacks, Tag 0EX3] is an
> isomorphism.
>
> The base-change map of this library,
> `Stacks.AlgebraicGeometry.TopDegreeBaseChange.topDirectImageBaseChangeMap`, is defined over a
> quasi-compact quasi-separated base; commutation with base change is local on
> the base, so asking it over every such open of `S` is the source's assertion.

```lean
theorem isFiniteLocallyFree_rightDerived_one_and_isIso_baseChange (f : X ⟶ S) [IsProper f]
    [GeometricallyConnected f] (hf : IsAtWorstNodalOfRelativeDimensionOne f) :
    SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (((Scheme.Modules.pushforward f).rightDerived 1).obj
          (SheafOfModules.unit X.ringCatSheaf)) ∧
      ∀ (V : S.Opens) [CompactSpace V] [QuasiSeparatedSpace V] {X'' Y'' : Scheme.{u}}
        (h' : X'' ⟶ f ⁻¹ᵁ V) (f'' : X'' ⟶ Y'') (h : Y'' ⟶ V)
        (sq : IsPullback h' f'' (f ∣_ V) h),
        IsIso (@Stacks.AlgebraicGeometry.TopDegreeBaseChange.topDirectImageBaseChangeMap _ _
          (topDegreeSituation f hf V) (SheafOfModules.unit (f ⁻¹ᵁ V).toScheme.ringCatSheaf)
          (Stacks.AlgebraicGeometry.AffineQcohPushforward.isQuasicoherent_unit _) h' f'' h
          (Stacks.AlgebraicGeometry.TopDegreeBaseChange.toShHom_comm_of_isPullback
            (S := topDegreeSituation f hf V) h' f'' h sq))
```

**`Stacks.AlgebraicGeometry.NodalFamilyCohomology.isZero_rightDerived_of_two_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/NodalFamilyStructureSheafCohomology.lean#L342). The attribute's comment: “(c): `Rᵠf_*𝒪_X = 0` for `q ≥ 2`”.

> **[Stacks, Tag 0GKA], part (c).** Let `f : X ⟶ S` be proper and at-worst-nodal of relative
> dimension one, with geometrically connected fibres. Then `Rᵠf_*𝒪_X = 0` for every `q ≥ 2`.
>
> The fibres have dimension one, so this is [Stacks, Tag 0E7D] at `d = 1`.

```lean
theorem isZero_rightDerived_of_two_le (f : X ⟶ S) [IsProper f] [GeometricallyConnected f]
    (hf : IsAtWorstNodalOfRelativeDimensionOne f) (q : ℕ) (hq : 2 ≤ q) :
    IsZero (((Scheme.Modules.pushforward f).rightDerived q).obj
      (SheafOfModules.unit X.ringCatSheaf))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.20, Tag 0C58](https://stacks.math.columbia.edu/tag/0C58)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
