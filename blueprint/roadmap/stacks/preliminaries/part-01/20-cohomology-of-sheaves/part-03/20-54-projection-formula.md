---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.OnSpace.injective_tensorSheaf_of_finiteLocallyFree, Stacks.ProjectionFormula.derivedPushforwardTensorRightRingedSpacePlusIso, Stacks.ProjectionFormula.higherDirectImageProjectionFormulaRingedSpaceIso, Stacks.AffineProjectionFormula.isIso_projectionFormulaMap_of_isFiniteLocallyFree_class_ringedSpace, Stacks.Duality.projectionFormulaMap, Stacks.Duality.projectionFormulaMap_naturality, Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap, Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap_natural_left
statement: formalized
proof: formalized
---

# 20.54 Projection formula

Section 20.54 of the Stacks Project, [Tag 01E6](https://stacks.math.columbia.edu/tag/01E6). 6 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01E7, a lemma

[Tag 01E7](https://stacks.math.columbia.edu/tag/01E7) in the Stacks Project.

**`Stacks.SheafOfModules.OnSpace.injective_tensorSheaf_of_finiteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/InjectiveTensor.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/InjectiveTensor.lean#L53).

> Tensoring an injective sheaf of modules with a finite locally free sheaf of modules preserves
> injectivity.

```lean
theorem injective_tensorSheaf_of_finiteLocallyFree
    (I E : SheafOfModules.{u} (structureSheafRing X))
    [Injective I] [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E] :
    Injective ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (E)).obj (I)))
```

## Tag 01E8, a lemma

[Tag 01E8](https://stacks.math.columbia.edu/tag/01E8) in the Stacks Project.

**`Stacks.ProjectionFormula.derivedPushforwardTensorRightRingedSpacePlusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectionFormula/HigherDirectImageRingedSpace.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectionFormula/HigherDirectImageRingedSpace.lean#L246). The attribute's comment: “the D⁺ clause: for a morphism of ringed spaces f : X ⟶ Y and a finite locally free 𝒪_Y-module ℰ, the isomorphism ℰ ⊗_{𝒪_Y} Rf_*ℱ ≅ Rf_*(f^*ℰ ⊗_{𝒪_X} ℱ) in D^+(Y), functorial in ℱ”. References: EGA 0 (12.2.3), “more general”; SGA 6 III (5.8), “special case”.

> **The `D⁺` clause of [Stacks, Tag 01E8]**: for a morphism of **ringed spaces** `f : X ⟶ Y` and
> a **finite locally free** `𝒪_Y`-module `ℰ`,
>
> `D(- ⊗_{𝒪_X} f^*ℰ) ⋙ Rf_* ≅ Rf_* ⋙ D(- ⊗_{𝒪_Y} ℰ)`
>
> as functors `D⁺(𝒪_X) ⥤ D⁺(𝒪_Y)`: the projection formula in the bounded below derived category,
> for an arbitrary morphism of ringed spaces, every object of `D⁺(𝒪_X)` and `ℰ` of arbitrary
> rank.

```lean
def derivedPushforwardTensorRightRingedSpacePlusIso :
    (tensorRightSheaf X ((pullbackFunctor f).obj E)).mapDerivedCategoryPlus ⋙
        (pushforwardFunctor f).rightDerivedFunctorPlus ≅
      (pushforwardFunctor f).rightDerivedFunctorPlus ⋙
        (tensorRightSheaf Y E).mapDerivedCategoryPlus
```

**`Stacks.ProjectionFormula.higherDirectImageProjectionFormulaRingedSpaceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectionFormula/HigherDirectImageRingedSpace.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectionFormula/HigherDirectImageRingedSpace.lean#L298). The attribute's comment: “the higher direct image clause: for a morphism of ringed spaces f : X ⟶ Y, an 𝒪_X-module ℱ and a finite locally free 𝒪_Y-module ℰ, the isomorphisms R^n f_*(ℱ ⊗_{𝒪_X} f^*ℰ) ≅ R^n f_*ℱ ⊗_{𝒪_Y} ℰ for every integer n; the tag's q ≥ 0 is the case n = (q : ℤ)”. References: EGA 0 (12.2.3), “partial”.

> **The higher direct image clause of [Stacks, Tag 01E8]**: for a morphism of **ringed spaces**
> `f : X ⟶ Y`, an arbitrary `𝒪_X`-module `ℱ` and a **finite locally free** `𝒪_Y`-module `ℰ`,
>
> `R^n f_*(ℱ ⊗_{𝒪_X} f^*ℰ) ≅ (R^n f_*ℱ) ⊗_{𝒪_Y} ℰ`
>
> for every integer `n`; the tag's `q ≥ 0` is the case `n = (q : ℤ)`.

```lean
def higherDirectImageProjectionFormulaRingedSpaceIso
    (F : SheafOfModules.{u} (structureRingSheaf X)) (n : ℤ) :
    ((pushforwardFunctor f).rightDerivedPlus n).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} X.sheaf).obj F).obj
          ((pullbackFunctor f).obj E)) ≅
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} Y.sheaf).obj
        (((pushforwardFunctor f).rightDerivedPlus n).obj F)).obj E
```

**`Stacks.AffineProjectionFormula.isIso_projectionFormulaMap_of_isFiniteLocallyFree_class_ringedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectionFormula/LocalityRingedSpace.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectionFormula/LocalityRingedSpace.lean#L417). The attribute's comment: “the q = 0 clause: for a morphism of ringed spaces f, an arbitrary module 𝒢 on the source and a finite locally free module ℋ on the target, the projection formula map f_*𝒢 ⊗ ℋ ⟶ f_*(𝒢 ⊗ f^*ℋ) is an isomorphism”.

> **The projection formula for an arbitrary morphism of ringed spaces at a finite locally free
> module on the target**, finite local freeness being the class of [Stacks, Tag 01C6]: for `𝒢` an
> arbitrary `𝒪_Z`-module and `ℋ` a finite locally free `𝒪_X`-module, the canonical map
> `f_*𝒢 ⊗_{𝒪_X} ℋ ⟶ f_*(𝒢 ⊗_{𝒪_Z} f^*ℋ)` is an isomorphism.
>
> This is `isIso_projectionFormulaMap_of_isFiniteLocallyFree_ringedSpace` with its pointwise
> input supplied by `exists_moduleRestriction_iso_free_of_isFiniteLocallyFree`.

```lean
theorem isIso_projectionFormulaMap_of_isFiniteLocallyFree_class_ringedSpace
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} H] :
    IsIso (projectionFormulaMap f G H)
```

## Tag 0B53, an equation

[Tag 0B53](https://stacks.math.columbia.edu/tag/0B53) in the Stacks Project.

**`Stacks.Duality.projectionFormulaMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L167). The attribute's comment: “the map”.

> **The projection-formula map** `K ⊗ᴸ_{𝒪_Y} Rf_*E ⟶ Rf_*(Lf^*K ⊗ᴸ_{𝒪_X} E)`: the adjoint
> transpose, for the adjunction `Lf^* ⊣ Rf_*` on the quasi-coherent derived categories, of the
> oplax monoidality of `Lf^*` followed by the counit of that adjunction in the pushforward factor.
> Its invertibility is [Stacks, Tag 08EU].

```lean
def projectionFormulaMap (E : quasiCoherentDerivedCategory X)
    (K : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor Y).obj K).obj
        ((quasiCoherentDerivedPushforward f hpush).obj E) ⟶
      (quasiCoherentDerivedPushforward f hpush).obj
        (((quasiCoherentDerivedTensor X).obj
          ((quasiCoherentDerivedPullback' f).obj K)).obj E)
```

**`Stacks.Duality.projectionFormulaMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L180). The attribute's comment: “naturality”.

> The projection-formula map is natural in both arguments.

```lean
theorem projectionFormulaMap_naturality {E E' : quasiCoherentDerivedCategory X}
    {K K' : quasiCoherentDerivedCategory Y} (φ : E ⟶ E') (h : K ⟶ K') :
    (((quasiCoherentDerivedTensor Y).map h).app
          ((quasiCoherentDerivedPushforward f hpush).obj E) ≫
        ((quasiCoherentDerivedTensor Y).obj K').map
          ((quasiCoherentDerivedPushforward f hpush).map φ)) ≫
      projectionFormulaMap f hpush α E' K' =
    projectionFormulaMap f hpush α E K ≫
      (quasiCoherentDerivedPushforward f hpush).map
        (((quasiCoherentDerivedTensor X).map
            ((quasiCoherentDerivedPullback' f).map h)).app E ≫
          ((quasiCoherentDerivedTensor X).obj
            ((quasiCoherentDerivedPullback' f).obj K')).map φ)
```

**`Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean#L164). The attribute's comment: “the map”.

> **The derived projection-formula morphism**
> `Rf_*E ⊗^L_{𝒪_Y} K ⟶ Rf_*(E ⊗^L_{𝒪_X} Lf^*K)`: the adjoint transpose of the derived
> pullback-tensor comparison of Stacks 079U followed by the counit of `Lf^* ⊣ Rf_*` in the left
> tensor factor.  It is defined for arbitrary `E ∈ D(𝒪_X)` and `K ∈ D(𝒪_Y)`.

```lean
def projectionFormulaMap
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj E)).obj K ⟶
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj E).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj K))
```

**`Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean#L197). The attribute's comment: “naturality in the source complex”.

> The derived projection-formula morphism is natural in the derived module on the source.

```lean
theorem projectionFormulaMap_natural_left
    {E E' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (e : E ⟶ E')
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map e)).app K ≫
        projectionFormulaMap f E' K =
      projectionFormulaMap f E K ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).map e).app
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj K))
```

**`Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormula.lean#L216). The attribute's comment: “naturality in the target complex”.

> The derived projection-formula morphism is natural in the derived module on the target.

```lean
theorem projectionFormulaMap_natural_right
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    {K K' : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))}
    (k : K ⟶ K') :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj E)).map k ≫
        projectionFormulaMap f E K' =
      projectionFormulaMap f E K ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj E).map
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).map k))
```

**`Stacks.Cohomology.ProjectionFormulaPerfect.projectionFormulaTransformation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaStrictlyPerfect.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaStrictlyPerfect.lean#L128). The attribute's comment: “the map as a natural transformation in the target complex”.

> **The projection-formula morphism of [Stacks, Tag 0B53] as a natural transformation.**  Its
> component at `K` is `Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap f E K`, and
> its naturality is `projectionFormulaMap_natural_right`.

```lean
def projectionFormulaTransformation
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    projectionFormulaSource f E ⟶ projectionFormulaTarget f E
```

## Tag 0B54, a lemma

[Tag 0B54](https://stacks.math.columbia.edu/tag/0B54) in the Stacks Project.

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaLocalStrictlyPerfect.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaLocalStrictlyPerfect.lean#L138). References: SGA 6 IV (2.11.1), “more general”.

> Let `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` be a morphism of ringed spaces, let
> `E ∈ D(𝒪_X)` and let `K ∈ D(𝒪_Y)` be perfect.  Then the projection-formula morphism of
> [Stacks, Tag 0B53]
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*K)`
>
> is an isomorphism.
>
> Perfectness is `Stacks.Cohomology.PerfectComplexes.IsPerfect` of [Stacks, Tag 08CM]: `K` is
> represented by a complex which on the members of some open cover of `Y` receives a
> quasi-isomorphism from a strictly perfect complex.

```lean
theorem isIso_projectionFormulaMap_of_isPerfect
    {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    [HasSheafify (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}]
    [(Opens.grothendieckTopology X.carrier).WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasSheafify (Opens.grothendieckTopology Y.carrier) AddCommGrpCat.{u}]
    [(Opens.grothendieckTopology Y.carrier).WEqualsLocallyBijective AddCommGrpCat.{u}]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y) K) :
    IsIso (projectionFormulaMap f E K)
```

**`Stacks.Cohomology.ProjectionFormulaPerfect.isIso_projectionFormulaMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaPerfect.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaPerfect.lean#L352). The attribute's comment: “the whole tag: for an arbitrary morphism of ringed spaces f : X ⟶ Y, an arbitrary E in D(𝒪_X) and a perfect K in D(𝒪_Y), the projection-formula morphism Rf_*E ⊗ᴸ K ⟶ Rf_*(E ⊗ᴸ Lf^*K) of Tag 0B53 is invertible”. References: SGA 6 III (3.7), “special case”; SGA 6 IV (2.11.1), “more general”.

> **The projection formula for a perfect complex** [Stacks, Tag 0B54].  For a morphism of
> ringed spaces `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)`, an arbitrary `E ∈ D(𝒪_X)` and a *perfect*
> `K ∈ D(𝒪_Y)`, the projection-formula morphism
>
> `Rf_*E ⊗^L_{𝒪_Y} K ⟶ Rf_*(E ⊗^L_{𝒪_X} Lf^*K)`
>
> of [Stacks, Tag 0B53] is invertible.
>
> The base case `K = 𝒪_Y[i]⟦n⟧` of the source's dévissage is
> `Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_singleUnit_degree`
> ([Stacks, Tag 08EU] at every degree), obtained from the abstract projection formula
> `Stacks.ProjectionFormula.isIso_adjunctionTensorMap` at an invertible object, and the dévissage
> over strictly perfect complexes is `isIso_projectionFormulaMap_of_isStrictlyPerfect`.
>
> **The proof.**  A perfect `K` is the class of a perfect complex `A`, so there is an open covering
> `U` of `Y` on each member of which `A` receives a quasi-isomorphism from a strictly perfect
> complex.  Invertibility in `D(𝒪_Y)` is local on that covering
> (`Stacks.Cohomology.isIso_of_isIso_jStar_mapDerivedCategory_map`), restriction to a member is
> derived pullback along its inclusion
> (`Stacks.Cohomology.DerivedOpenImmersion.derivedPullbackOpenRestrictionIso`), and derived
> pullback of the projection-formula morphism along that inclusion is invertible as soon as the
> projection-formula morphism of the base change is
> (`isIso_derivedPullback_map_projectionFormulaMap`, which is [Stacks, Tag 0B6B] together with
> invertibility of the derived base-change map at a square of open immersions).  The base change
> is taken as the genuine fibre product `X ×_Y U` in ringed spaces, which exists because the
> inclusion of an open subspace is an open immersion, so the square is Cartesian on the nose and
> `Stacks.Cohomology.DerivedBaseChange.isIso_derivedBaseChangeMap_of_isOpenImmersions` applies.
> Upstairs the complex is strictly perfect and
> `isIso_projectionFormulaMap_derivedPullback_obj` closes it.

```lean
theorem isIso_projectionFormulaMap_of_isPerfect {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (hK : AlgebraicGeometry.RingedSpace.IsPerfect K) :
    IsIso (projectionFormulaMap f E K)
```

**`Stacks.Cohomology.ProjectionFormulaShiftedUnit.isIso_projectionFormulaMap_isStrictlyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaShiftedUnit.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaShiftedUnit.lean#L333). The attribute's comment: “the dévissage from the structure sheaf to a strictly perfect complex, now with NO hypothesis: the case K = O_Y[i] shifted by any amount, which Stacks.Cohomology.ProjectionFormulaPerfect.isIso_projectionFormulaMap_of_isStrictlyPerfect carries as the hypothesis hunit, is discharged here. What is still not covered of the tag is the reduction of a PERFECT complex to a strictly perfect one, which is local on the base and needs the base-change square of Tag 0B6B along an open immersion composed with a locality statement for invertibility of the map; so this is the tag for a strictly perfect complex, not for a perfect one”.

> **The dévissage half of [Stacks, Tag 0B54] with no hypothesis at all.**  For an arbitrary
> morphism of ringed spaces `f : X ⟶ Y`, an arbitrary `E` in `D(𝒪_X)` and a strictly perfect
> complex `P` of `𝒪_Y`-modules, the derived projection-formula morphism
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} P ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*P)`
>
> of [Stacks, Tag 0B53] is an isomorphism.
>
> This is
> `Stacks.Cohomology.ProjectionFormulaPerfect.isIso_projectionFormulaMap_of_isStrictlyPerfect` with
> its hypothesis `hunit` supplied by `isIso_projectionFormulaMap_single_shift`.

```lean
theorem isIso_projectionFormulaMap_isStrictlyPerfect
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (P : CochainComplex (OXMod.{u, u} Y) ℤ) (hP : IsStrictlyPerfect P) :
    IsIso (projectionFormulaMap f E (DerivedCategory.Q.obj P))
```

## Tag 0B55, a lemma

[Tag 0B55](https://stacks.math.columbia.edu/tag/0B55) in the Stacks Project.

**`Stacks.Cohomology.ClosedEmbeddingProjectionFormulaComplexes.complexProjectionFormulaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaComplexes.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaComplexes.lean#L270). The attribute's comment: “step 2: the projection formula holds at the level of complexes”.

> **The projection formula for a closed embedding, at the level of complexes.**  For a morphism
> of ringed spaces `f : X ⟶ Y` whose underlying continuous map is a homeomorphism onto a closed
> subset, and for *arbitrary* cochain complexes `A^•` of `𝒪_X`-modules and `B^•` of `𝒪_Y`-modules,
>
> `Tot(f_*A^• ⊗_{𝒪_Y} B^•) ≅ f_* Tot(A^• ⊗_{𝒪_X} f^*B^•)`.
>
> There is no flatness, boundedness or finiteness hypothesis on either complex.
>
> This is the complex-level step of the source's proof of [Stacks, Tag 0B55].  It is the termwise
> isomorphism `projectionBicomplexIso` on totalizations, composed with the comparison
> `Tot(f_*(-)) ⟶ f_*(Tot(-))`, which is invertible by
> `Stacks.Cohomology.ClosedEmbeddingPushforward.isIso_totalMap_modulePushforward` because `f_*`
> commutes with arbitrary direct sums.  The derived statement of [Stacks, Tag 0B55] does not follow
> from this without the identification described in the module docstring, and is not proved here.

```lean
def complexProjectionFormulaIso
    (hf : Topology.IsClosedEmbedding (ConcreteCategory.hom f.hom.base))
    (A : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (B : CochainComplex (SheafOfModules.{u} (structureSheafRing Y)) ℤ) :
    ((tensorComplex Y.sheaf).obj
        (((modulePushforward f).mapHomologicalComplex (.up ℤ)).obj A)).obj B ≅
      ((modulePushforward f).mapHomologicalComplex (.up ℤ)).obj
        (((tensorComplex X.sheaf).obj A).obj
          (((modulePullback f).mapHomologicalComplex (.up ℤ)).obj B))
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_of_isClosedEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaDerived.lean, line 871](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaDerived.lean#L871). The attribute's comment: “for an arbitrary morphism of ringed spaces whose underlying map is a homeomorphism onto a closed subset; the derived statement, with no boundedness, flatness, finiteness, quasi-coherence or support hypothesis on either complex”.

> **[Stacks, Tag 0B55].**  Let `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` be a morphism of ringed spaces whose
> underlying continuous map is a homeomorphism onto a closed subset.  Then the projection-formula
> morphism of [Stacks, Tag 0B53]
>
> `Rf_*E ⊗^𝐋_{𝒪_Y} K ⟶ Rf_*(E ⊗^𝐋_{𝒪_X} Lf^*K)`
>
> is an isomorphism for every `E` in `D(𝒪_X)` and every `K` in `D(𝒪_Y)`.
>
> The proof is the source's: represent `E` by any complex and `K` by a K-flat complex, which is
> possible by [Stacks, Tag 06YF], and transport invertibility along the two representations, which
> is legitimate by
> `Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMap_congr_left` and
> `isIso_projectionFormulaMap_congr_right`.  On representatives the morphism is `Q` of the
> complex-level projection formula up to isomorphism, which is
> `projectionFormulaMap_eq_derivedModelIso` in the namespace
> `Stacks.Cohomology.ClosedEmbeddingProjectionFormulaComplexes`.

```lean
theorem isIso_projectionFormulaMap_of_isClosedEmbedding
    (hf : Topology.IsClosedEmbedding (ConcreteCategory.hom f.hom.base))
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    IsIso (projectionFormulaMap f E K)
```

**`Stacks.Cohomology.DerivedProjectionFormula.isIso_projectionFormulaMapRight_of_isClosedEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaRightIso.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaRightIso.lean#L67). The attribute's comment: “the right-handed form: the pushforward in the right tensor factor, K ⊗^L Rf_*E ⟶ Rf_*(Lf^*K ⊗^L E), for an arbitrary morphism of ringed spaces whose underlying map is a homeomorphism onto a closed subset and arbitrary K and E”.

> **The projection formula along a closed embedding, with the pushforward in the right tensor
> factor.**  Let `f : (X, 𝒪_X) ⟶ (Y, 𝒪_Y)` be a morphism of ringed spaces whose underlying
> continuous map is a homeomorphism onto a closed subset.  Then the projection-formula morphism
>
> `K ⊗^𝐋_{𝒪_Y} Rf_*E ⟶ Rf_*(Lf^*K ⊗^𝐋_{𝒪_X} E)`
>
> is an isomorphism for every `K` in `D(𝒪_Y)` and every `E` in `D(𝒪_X)`.

```lean
theorem isIso_projectionFormulaMapRight_of_isClosedEmbedding
    (hf : Topology.IsClosedEmbedding (ConcreteCategory.hom f.hom.base))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    IsIso (projectionFormulaMapRight f K E)
```

**`Stacks.ClosedEmbeddingProjectionFormula.isIso_stalkMap_projectionFormulaMap'_of_notMemRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean#L317). The attribute's comment: “the stalk computation off the closed image: both stalks vanish there”.

> **Off the closed image the projection-formula morphism is invertible on stalks.**  This is the
> first half of the stalk verification in the source's proof of [Stacks, Tag 0B55]: for `y` outside
> the image of a homeomorphism onto a closed subset both stalks vanish, by
> `isZero_stalk_source_of_notMemRange` and `isZero_stalk_target_of_notMemRange`, and any morphism
> between zero objects is invertible.
>
> The other half, the stalk over a point of the image, is
> `isIso_stalkMap_projectionFormulaMap'_of_memRange`; together the two give
> `isIso_projectionFormulaMap'_of_isClosedEmbedding`.

```lean
theorem isIso_stalkMap_projectionFormulaMap'_of_notMemRange
    (hf : Topology.IsClosedEmbedding (ConcreteCategory.hom f.hom.base)) (y : Y.carrier)
    (hy : y ∉ Set.range (ConcreteCategory.hom f.hom.base)) :
    IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} y).map
      ((ExtensionByZeroModules.toAb (structureRingSheaf Y)).map
        (projectionFormulaMap' f G H)))
```

**`Stacks.ClosedEmbeddingProjectionFormula.isIso_stalkMap_projectionFormulaMap'_of_memRange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean#L516). The attribute's comment: “the stalk computation over a point of the image, by cancelling the base change”.

> **Over a point of the image the projection-formula morphism is invertible on stalks.**  This
> is the second half of the stalk verification in the source's proof of [Stacks, Tag 0B55], and the
> step where the mathematics sits: at `y = f x` the source stalk is `G_x ⊗_R H_{f x}` and the
> target stalk is `G_x ⊗_S (S ⊗_R H_{f x})`, and they are identified by cancelling the base change.
>
> The stalk map is `R`-linear and carries the germ of `m ⊗ k` to the germ of `m ⊗ η k` by
> `Stacks.ProjectionFormula.projectionFormulaMap'_unit_tmul`, which under the three identifications
> `stalkPushforwardEquiv`, [Stacks, Tag 01CB] and [Stacks, Tag 0098] is exactly the formula
> `m ⊗ n ↦ m ⊗ (1 ⊗ n)` that `tensorProjectionMap_bijective` recognises.

```lean
theorem isIso_stalkMap_projectionFormulaMap'_of_memRange :
    IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} (f.hom.base x)).map
      ((ExtensionByZeroModules.toAb (structureRingSheaf Y)).map
        (projectionFormulaMap' f E K)))
```

**`Stacks.ClosedEmbeddingProjectionFormula.isIso_projectionFormulaMap'_of_isClosedEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingProjectionFormulaStalks.lean#L661). The attribute's comment: “step 1: the ordinary projection formula map is invertible for a closed embedding”. References: SGA 3 VIB (11.5), “Clause (a), special case”.

> **The ordinary projection formula for a closed embedding of ringed spaces.**  For a morphism
> of ringed spaces `f : X ⟶ Y` whose underlying continuous map is a homeomorphism onto a closed
> subset, and for *arbitrary* sheaves of modules `G` on `X` and `H` on `Y`, the canonical morphism
>
> `f_*G ⊗_{𝒪_Y} H ⟶ f_*(G ⊗_{𝒪_X} f^*H)`
>
> is an isomorphism.
>
> This is step 1 of the source's proof of [Stacks, Tag 0B55].  A morphism of sheaves of modules
> which is invertible on every stalk is invertible
> (`ExtensionByZeroModules.isIso_of_stalk_isIso`), and the two stalk computations are
> `isIso_stalkMap_projectionFormulaMap'_of_memRange` on the image and
> `isIso_stalkMap_projectionFormulaMap'_of_notMemRange` off it.
>
> No local surjectivity of `𝒪_Y ⟶ f_*𝒪_X` is assumed, so the counit of `f^* ⊣ f_*` is not
> invertible and the formal argument of `Stacks.AffineProjectionFormula.isIso_projectionFormulaMap`
> is unavailable; that is why the proof goes through stalks.  The derived statement of
> [Stacks, Tag 0B55] does not follow from this without the K-flat reduction, and is not proved
> here.

```lean
theorem isIso_projectionFormulaMap'_of_isClosedEmbedding
    (hf : Topology.IsClosedEmbedding (ConcreteCategory.hom f.hom.base)) :
    IsIso (projectionFormulaMap' f G H)
```

**`Stacks.Cohomology.ClosedEmbeddingPushforward.preservesColimitsOfSize_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean#L171). The attribute's comment: “f_* commutes with direct sums: the input of the source's proof”.

> **Pushforward of sheaves of modules along a morphism of ringed spaces which is a
> homeomorphism onto a closed subset preserves all small colimits**, in particular arbitrary
> direct sums.  This is the input "`f_*` commutes with direct sums" of the source's proof of
> [Stacks, Tag 0B55]; the library had only right exactness,
> `Stacks.ClosedImmersion.preservesFiniteColimits_modulePushforward`.
>
> The statement is reduced to `preservesColimits_sheafPushforward` through the forgetful functor
> to abelian sheaves, which preserves colimits and reflects isomorphisms.

```lean
theorem preservesColimitsOfSize_modulePushforward
    (f : X ⟶ Y) (hf : Topology.IsClosedEmbedding f.hom.base) :
    PreservesColimitsOfSize.{0, 0} (modulePushforward f)
```

**`Stacks.Cohomology.ClosedEmbeddingPushforward.isIso_derivedPushforwardUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean#L203). The attribute's comment: “step 1: Rf_* is computed by applying f_* termwise”.

> **For a morphism of ringed spaces which is a homeomorphism onto a closed subset the derived
> pushforward is computed by applying `f_*` termwise**: the comparison `Qh (f_* K) ⟶ Rf_* (Qh K)`
> is invertible at every object `K` of the homotopy category, with no K-injectivity hypothesis.
>
> This is the first step of the source's proof of [Stacks, Tag 0B55].  It is
> `Stacks.Cohomology.ExactPushforwardAdjunction.isIso_derivedPushforwardUnit_app`, whose
> hypothesis of right exactness is discharged by
> `Stacks.ClosedImmersion.preservesFiniteColimits_modulePushforward`, [Stacks, Tag 08KS].

```lean
theorem isIso_derivedPushforwardUnit_app (f : X ⟶ Y)
    (hf : Topology.IsClosedEmbedding f.hom.base)
    (K : HomotopyCategory (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)) :
    IsIso ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforwardUnit f).app K)
```

**`Stacks.Cohomology.ClosedEmbeddingPushforward.isIso_totalMap_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ClosedEmbeddingPushforwardColimits.lean#L218). The attribute's comment: “f_* commutes with the totalization of an unbounded bicomplex”.

> **`f_*` commutes with the total complex of a bicomplex** when `f` is a homeomorphism onto a
> closed subset: the comparison `Tot(f_* K) ⟶ f_* Tot(K)` of
> `HomologicalComplex₂.TotalMap.totalMap` is an isomorphism.  There is no boundedness hypothesis
> on the bicomplex, which is what the source's proof of [Stacks, Tag 0B55] needs: the
> totalizations it compares are those of unbounded bicomplexes.

```lean
theorem isIso_totalMap_modulePushforward (f : X ⟶ Y)
    (hf : Topology.IsClosedEmbedding f.hom.base)
    (K : HomologicalComplex₂ (SheafOfModules.{u} (structureSheafRing X))
      (ComplexShape.up ℤ) (ComplexShape.up ℤ))
    [K.HasTotal (ComplexShape.up ℤ)]
    [HomologicalComplex₂.HasTotal
      (HomologicalComplex₂.TotalMap.mapBicomplex (modulePushforward f) K)
      (ComplexShape.up ℤ)] :
    IsIso (HomologicalComplex₂.TotalMap.totalMap (c₁₂ := ComplexShape.up ℤ)
      (modulePushforward f) K)
```

**`Stacks.Cohomology.SupportedComplexes.isIso_projectionFormulaMap_closedSubsetInclusion_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaClosedEmbeddingUnconditional.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaClosedEmbeddingUnconditional.lean#L344). The attribute's comment: “for the canonical inclusion of a closed subset, with its restricted structure sheaf; the conclusion is unconditional, but the source's hypothesis -- any morphism of ringed spaces that is a homeomorphism onto a closed subset -- is narrowed to that inclusion”.

> **[Stacks, Tag 0B55] for the inclusion of a closed subset.**  The projection-formula map of
> [Stacks, Tag 0B53]
>
> `Ri_*E ⊗^𝐋_{𝒪_X} K ⟶ Ri_*(E ⊗^𝐋_{𝒪_X|_Z} Li^*K)`
>
> is an isomorphism for arbitrary `E` in `D(𝒪_X|_Z)` and `K` in `D(𝒪_X)`, with no hypothesis on
> either beyond closedness of `Z`, which is the source's hypothesis that `i` be a homeomorphism
> onto a closed subset.
>
> This is `isIso_projectionFormulaMap_closedSubsetInclusion` with its support hypothesis supplied
> by `cohomologySupportedOn_derivedTensor_derivedPushforward_closedSubsetInclusion`.

```lean
theorem isIso_projectionFormulaMap_closedSubsetInclusion_of_isClosed
    (E : DerivedCategory (SheafOfModules.{u}
      (structureSheafRing (closedSubsetRingedSpace X Z))))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    IsIso (projectionFormulaMap (closedSubsetInclusion X Z) E K)
```

## Tag 0B6B, a remark

[Tag 0B6B](https://stacks.math.columbia.edu/tag/0B6B) in the Stacks Project.

**`Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMap_derivedBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaBaseChange.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaBaseChange.lean#L310).

> **Stacks 0B6B: the derived projection-formula map is compatible with a commutative square of
> ringed spaces.**
>
> For a commutative square `g' ≫ f = f' ≫ g` of ringed spaces and arbitrary `E ∈ D(𝒪_X)`,
> `K ∈ D(𝒪_Y)`, the diagram `ProjectionFormulaBaseChangeSquare` commutes at the derived
> projection-formula map of Stacks 0B53 for `f` and for `f'`, the derived base change map of
> Stacks 08HY and the identification `derivedPullbackSquareIso`: the comparison of Stacks 079U for
> `g`, followed by base change in the first tensor factor and by the projection-formula map for
> `f'`, equals the derived pullback along `g` of the projection-formula map for `f`, followed by
> base change and by `Rf'_*` of the comparison of Stacks 079U for `g'` and of the identification
> in the second tensor factor.
>
> There is no boundedness, flatness or quasi-coherence hypothesis on `E` and `K`, and no
> associator or symmetry of `⊗^L` is used: the diagram has binary tensor products only.

```lean
theorem projectionFormulaMap_derivedBaseChangeMap
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ProjectionFormulaBaseChangeSquare (derivedPushforward f) (derivedPushforward f')
      (derivedPullback f) (derivedPullback f') (derivedPullback g) (derivedPullback g')
      (Functor.uncurry.obj (derivedTensorProductFunctor Y.sheaf))
      (Functor.uncurry.obj (derivedTensorProductFunctor X.sheaf))
      (Functor.uncurry.obj (derivedTensorProductFunctor Y'.sheaf))
      (Functor.uncurry.obj (derivedTensorProductFunctor X'.sheaf))
      (pullbackTensorComparison g) (pullbackTensorComparison g') E K
      (projectionFormulaMap f E K)
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq
        ((Functor.uncurry.obj (derivedTensorProductFunctor X.sheaf)).obj
          (E, (derivedPullback f).obj K)))
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq E)
      ((derivedPullbackSquareIso g' f' f g sq).inv.app K)
      (projectionFormulaMap f' ((derivedPullback g').obj E) ((derivedPullback g).obj K))
```

**`Stacks.Cohomology.DerivedProjectionFormula.projectionFormulaMapRight_derivedBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaRightBaseChange.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaRightBaseChange.lean#L108). The attribute's comment: “the right-handed form: the pushforward in the right tensor factor”.

> **The right-handed projection-formula map is compatible with a commutative square of ringed
> spaces.**
>
> For a commutative square `g' ≫ f = f' ≫ g` of ringed spaces and arbitrary `E ∈ D(𝒪_X)`,
> `K ∈ D(𝒪_Y)`, the diagram `ProjectionFormulaBaseChangeSquare` commutes at the right-handed
> projection-formula map `projectionFormulaMapRight` for `f` and for `f'`, the derived base change
> map of Stacks 08HY and the identification `derivedPullbackSquareIso`, with the derived tensor
> products read with their arguments interchanged.  This is
> `projectionFormulaMap_derivedBaseChangeMap` with the pushforward in the right tensor factor.

```lean
theorem projectionFormulaMapRight_derivedBaseChangeMap
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y))) :
    ProjectionFormulaBaseChangeSquare (derivedPushforward f) (derivedPushforward f')
      (derivedPullback f) (derivedPullback f') (derivedPullback g) (derivedPullback g')
      (CategoryTheory.Prod.swap _ _ ⋙ Functor.uncurry.obj (derivedTensorProductFunctor Y.sheaf))
      (CategoryTheory.Prod.swap _ _ ⋙ Functor.uncurry.obj (derivedTensorProductFunctor X.sheaf))
      (CategoryTheory.Prod.swap _ _ ⋙ Functor.uncurry.obj (derivedTensorProductFunctor Y'.sheaf))
      (CategoryTheory.Prod.swap _ _ ⋙ Functor.uncurry.obj (derivedTensorProductFunctor X'.sheaf))
      (pullbackTensorComparisonSwap g) (pullbackTensorComparisonSwap g') E K
      (projectionFormulaMapRight f K E)
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq
        ((CategoryTheory.Prod.swap _ _ ⋙
          Functor.uncurry.obj (derivedTensorProductFunctor X.sheaf)).obj
            (E, (derivedPullback f).obj K)))
      (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g' f' f g sq E)
      ((derivedPullbackSquareIso g' f' f g sq).inv.app K)
      (projectionFormulaMapRight f' ((derivedPullback g).obj K) ((derivedPullback g').obj E))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.54, Tag 01E6](https://stacks.math.columbia.edu/tag/01E6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
