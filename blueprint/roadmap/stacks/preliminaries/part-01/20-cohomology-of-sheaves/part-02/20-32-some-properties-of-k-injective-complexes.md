---
declaration: section
origin: cited
lean: ExtensionByZeroModules.isKInjective_jStar, Stacks.Cohomology.OpenSubspace.cohomologyOnOpenIsoRestriction, Stacks.Cohomology.CohomologyPresheaf.cohomologyPresheafEvaluationIsoRestriction, Stacks.Cohomology.CohomologyPresheaf.cohomologyPresheafEvaluationIso, Stacks.Cohomology.CohomologyPresheaf.sheafificationCohomologyPresheafIso, Stacks.Duality.OpenImmersion.isIso_quasiCoherentDerivedRestrictBaseChangeSquare, AlgebraicGeometry.DerivedChow.derivedPushforwardRestrictOpenIso, AlgebraicGeometry.schemeDerivedPushforwardRestrictOpenIso
statement: formalized
proof: formalized
---

# 20.32 Some properties of K-injective complexes

Section 20.32 of the Stacks Project, [Tag 0D5U](https://stacks.math.columbia.edu/tag/0D5U). 9 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08BS, a lemma

[Tag 08BS](https://stacks.math.columbia.edu/tag/08BS) in the Stacks Project.

**`ExtensionByZeroModules.isKInjective_jStar`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/RestrictionOfKInjectives.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/RestrictionOfKInjectives.lean#L54).

> Restriction to an open subspace preserves K-injective complexes of sheaves of modules.

```lean
instance isKInjective_jStar
    (I : CochainComplex (SheafOfModules.{u} O) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((jStar U O).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Tag 0D5V, a lemma

[Tag 0D5V](https://stacks.math.columbia.edu/tag/0D5V) in the Stacks Project.

**`Stacks.Cohomology.OpenSubspace.cohomologyOnOpenIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyOnAnOpenSubspace.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyOnAnOpenSubspace.lean#L251). The attribute's comment: “`H^p(U, K) ≅ H^p(U, K|_U)`, natural in `K` in `D(O_X)`, for every open `U` of a ringed space `X` and every degree `p`”.

> Degree-`p` cohomology over an open agrees naturally with degree-`p` cohomology after
> restriction to that open.  The component at `K` is the isomorphism
> `H^p(U, K) ≅ H^p(U, K|_U)`.

```lean
public noncomputable def cohomologyOnOpenIsoRestriction {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X)
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wU} (SheafOfModules.{u} (resRing U O))]
    [HasDerivedCategory.{wG} AddCommGrpCat.{u}] (p : ℤ) :
    derivedSectionsOnOpen O U ⋙ DerivedCategory.homologyFunctor AddCommGrpCat.{u} p ≅
      derivedRestriction O U ⋙ derivedSectionsOnOpenSubspace O U ⋙
        DerivedCategory.homologyFunctor AddCommGrpCat.{u} p
```

## Tag 0BKJ, a lemma

[Tag 0BKJ](https://stacks.math.columbia.edu/tag/0BKJ) in the Stacks Project.

**`Stacks.Cohomology.CohomologyPresheaf.cohomologyPresheafEvaluationIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafOnOpenSubspace.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafOnOpenSubspace.lean#L41). The attribute's comment: “values on opens: the value of the presheaf on U is H^q(U, K|_U)”.

> **Stacks Project, Tag 0BKJ, the value on an open as cohomology of the open subspace.** The
> value on `U` of the presheaf `U ↦ H^q(U, K)` is `H^q(U, K|_U)`, the degree-`q` cohomology of the
> open subspace `U` with coefficients in the derived restriction of `K`, naturally in `K`.

```lean
public def cohomologyPresheafEvaluationIsoRestriction {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X)
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wU} (SheafOfModules.{u} (resRing U O))]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    [HasDerivedCategory.{wG} AddCommGrpCat.{u}]
    (q : ℤ) :
    derivedSectionsPresheaf O ⋙
          DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) q ⋙
          PresheafOfModules.evaluation O.obj (Opposite.op U) ⋙
          forget₂ (ModuleCat.{u} (O.obj.obj (Opposite.op U))) AddCommGrpCat.{u} ≅
      derivedRestriction O U ⋙ derivedSectionsOnOpenSubspace O U ⋙
          DerivedCategory.homologyFunctor AddCommGrpCat.{u} q
```

**`Stacks.Cohomology.CohomologyPresheaf.cohomologyPresheafEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafSheafification.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafSheafification.lean#L213). The attribute's comment: “values on opens”.

> The value on `U` of the cohomology presheaf is `H^q(U, K)`.

```lean
public def cohomologyPresheafEvaluationIso {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X)
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    [HasDerivedCategory.{wG} AddCommGrpCat.{u}]
    (q : ℤ) :
    derivedSectionsPresheaf O ⋙
          DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) q ⋙
          PresheafOfModules.evaluation O.obj (Opposite.op U) ⋙
          forget₂ (ModuleCat.{u} (O.obj.obj (Opposite.op U))) AddCommGrpCat.{u} ≅
      Stacks.Cohomology.OpenSubspace.derivedSectionsOnOpen O U ⋙
          DerivedCategory.homologyFunctor AddCommGrpCat.{u} q
```

**`Stacks.Cohomology.CohomologyPresheaf.sheafificationCohomologyPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafSheafification.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/CohomologyPresheafSheafification.lean#L258). The attribute's comment: “associated sheaf”.

> Sheafifying the presheaf `U ↦ H^q(U, K)` gives the `q`-th cohomology sheaf of `K`, naturally
> in the derived object `K`.

```lean
public def sheafificationCohomologyPresheafIso {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    [HasDerivedCategory.{wX} (SheafOfModules.{u} O)]
    [HasDerivedCategory.{wP} (PresheafOfModules.{u} O.obj)]
    (q : ℤ) :
    derivedSectionsPresheaf O ⋙
          DerivedCategory.homologyFunctor (PresheafOfModules.{u} O.obj) q ⋙
          PresheafOfModules.sheafification (𝟙 O.obj) ≅
        DerivedCategory.homologyFunctor (SheafOfModules.{u} O) q
```

## Tag 08FE, a lemma

[Tag 08FE](https://stacks.math.columbia.edu/tag/08FE) in the Stacks Project.

**`Stacks.Duality.OpenImmersion.isIso_quasiCoherentDerivedRestrictBaseChangeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionBaseChange.lean#L324). The attribute's comment: “invertibility of Stacks.Duality.OpenImmersion.quasiCoherentDerivedRestrictBaseChangeSquare, the mate of Stacks.Duality.quasiCoherentDerivedPushforwardSquareIso across the two restriction adjunctions, on the quasi-coherent derived categories of a cartesian square of schemes whose vertical arrows are open immersions, at the locally small model. The isomorphism of functors itself is Stacks.Cohomology.derivedPushforwardRestrictIso, for ringed spaces; what is added here is that this particular canonical map is the invertible one”.

> **The comparison `(Rf_*K)|_V ⟶ Rf'_*(K|_U)` of [Stacks, Tag 08FE] is invertible on the
> quasi-coherent derived categories.**  This is the slot that
> `StacksFrontier/AlgebraicGeometry/Duality/OpenImmersion/TwistedInverseImageRestrictionConjugate.lean`
> leaves open; see the module documentation for the argument.

```lean
theorem isIso_quasiCoherentDerivedRestrictBaseChangeSquare (sq : IsPullback j' f' f j) :
    IsIso (quasiCoherentDerivedRestrictBaseChangeSquare j' f' f j hpushj' hpushf hpushf' hpushj
      (fun K i => derivedCategoryB_derivedRestrict j K.obj K.property i)
      (fun K i => derivedCategoryB_derivedRestrict j' K.obj K.property i) sq.w)
```

**`AlgebraicGeometry.DerivedChow.derivedPushforwardRestrictOpenIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PseudoCoherentThree/DerivedChowFourierMukai.lean#L198). The attribute's comment: “for the standard derived direct image and derived pullback of [Stacks, Tag 079W], at the inclusion of an open subscheme of the target of a morphism of schemes”.

> **[Stacks, Tag 08FE] at an open of the target of a morphism of schemes.**  Restricting the
> derived direct image along `q` to an open `V` of the target is the derived direct image along
> `q ∣_ V` of the restriction to `q ⁻¹ᵁ V`: "forming the total direct image commutes with
> localization".

```lean
def derivedPushforwardRestrictOpenIso :
    derivedPushforward (ofScheme q) ⋙ derivedPullback (ofScheme V.ι) ≅
      derivedPullback (ofScheme (q ⁻¹ᵁ V).ι) ⋙ derivedPushforward (ofScheme (q ∣_ V))
```

**`AlgebraicGeometry.schemeDerivedPushforwardRestrictOpenIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedPushforwardOpenBase.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedPushforwardOpenBase.lean#L84). The attribute's comment: “for schemes, at the derived direct image of Tag 079W, with restriction to an open subscheme on the restriction edges”.

> **[Stacks, Tag 08FE] for schemes.** For a Cartesian square of schemes
> ```
> X' --f'--> T
> |          |
> g'         g
> v          v
> X ---f---> S
> ```
> whose vertical sides are open immersions, the restriction to `T` of `Rf_*E` is the derived direct
> image along `f'` of the restriction of `E` to `X'`.
>
> Restriction along an open immersion is exact, so both restriction edges are the functors induced
> on derived categories and carry no derivation.

```lean
def schemeDerivedPushforwardRestrictOpenIso {X S X' T : Scheme.{u}} (f : X ⟶ S) (g : T ⟶ S)
    [IsOpenImmersion g] (f' : X' ⟶ T) (g' : X' ⟶ X) (hsq : IsPullback g' f' f g)
    (E : DerivedCategory X.Modules) :
    letI : IsOpenImmersion g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    (Scheme.Modules.restrictFunctor g).mapDerivedCategory.obj
        ((schemeDerivedPushforward f).obj E) ≅
      (schemeDerivedPushforward f').obj
        ((Scheme.Modules.restrictFunctor g').mapDerivedCategory.obj E)
```

**`AlgebraicGeometry.schemeDerivedPushforwardRestrictOpensIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedPushforwardOpenBase.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/DerivedPushforwardOpenBase.lean#L137). The attribute's comment: “for schemes, at the restriction of f to the preimage of an open of the base”.

> **[Stacks, Tag 08FE] for schemes, at an open of the base.** The restriction to an open
> `U ⊆ S` of `Rf_*E` is the derived direct image along `f ∣_ U : f ⁻¹ᵁ U ⟶ U` of the restriction of
> `E` to `f ⁻¹ᵁ U`.
>
> This is `AlgebraicGeometry.schemeDerivedPushforwardRestrictOpenIso` at the Cartesian square of
> `AlgebraicGeometry.isPullback_morphismRestrict`.

```lean
def schemeDerivedPushforwardRestrictOpensIso {X S : Scheme.{u}} (f : X ⟶ S) (U : S.Opens)
    (E : DerivedCategory X.Modules) :
    (Scheme.Modules.restrictFunctor U.ι).mapDerivedCategory.obj
        ((schemeDerivedPushforward f).obj E) ≅
      (schemeDerivedPushforward (f ∣_ U)).obj
        ((Scheme.Modules.restrictFunctor (f ⁻¹ᵁ U).ι).mapDerivedCategory.obj E)
```

**`Stacks.Cohomology.derivedPushforwardRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/KInjectiveRestriction.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/KInjectiveRestriction.lean#L925).

> **Stacks 08FE.** In a Cartesian square of ringed spaces
> ```
> U ----g---> V
> |           |
> i           j
> |           |
> v           v
> X ----f---> Y
> ```
> in which `i` and `j` are open immersions, restricting the derived direct image along `j` is
> naturally isomorphic to taking the derived direct image along `g` after restriction along `i`.
>
> The four functors are arbitrary choices of right derived functors equipped with their canonical
> units; hence the result applies in particular to the standard choices of `Rf_*`, `Rg_*`, and the
> exact restriction functors.

```lean
noncomputable def derivedPushforwardRestrictIso
    {X Y U V : RingedSpace.{u, u}}
    (f : X ⟶ Y) (i : U ⟶ X) (j : V ⟶ Y) (g : U ⟶ V)
    [SheafedSpace.IsOpenImmersion i] [SheafedSpace.IsOpenImmersion j]
    (h : IsPullback i g f j)
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing Y))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing U))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing V))]
    (Rf : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (Rg : DerivedCategory (SheafOfModules.{u} (structureSheafRing U)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing V)))
    (Ri : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing U)))
    (Rj : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing V)))
    (αf : (modulePushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αg : (modulePushforward g).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rg)
    (αi : (modulePullback i).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Ri)
    (αj : (modulePullback j).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rj)
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Ri.IsRightDerivedFunctor αi
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rj.IsRightDerivedFunctor αj
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))] :
    Rf ⋙ Rj ≅ Ri ⋙ Rg
```

**`Stacks.Cohomology.derivedPushforwardRestrictIso_isCanonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/KInjectiveRestriction.lean, line 1004](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechAndResolutions/KInjectiveRestriction.lean#L1004). The attribute's comment: “canonicality”.

> The isomorphism `derivedPushforwardRestrictIso` is the canonical one: on a
> K-injective representative it is induced by the fixed adjunction mate
> `pushforwardRestrictHomotopyMap` and by the four specified derived-functor units.

```lean
theorem derivedPushforwardRestrictIso_isCanonical
    {X Y U V : RingedSpace.{u, u}}
    (f : X ⟶ Y) (i : U ⟶ X) (j : V ⟶ Y) (g : U ⟶ V)
    [SheafedSpace.IsOpenImmersion i] [SheafedSpace.IsOpenImmersion j]
    (h : IsPullback i g f j)
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing X))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing Y))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing U))]
    [HasDerivedCategory (SheafOfModules.{u} (structureSheafRing V))]
    (Rf : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
    (Rg : DerivedCategory (SheafOfModules.{u} (structureSheafRing U)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing V)))
    (Ri : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing U)))
    (Rj : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)) ⥤
      DerivedCategory (SheafOfModules.{u} (structureSheafRing V)))
    (alpha_f : (modulePushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (alpha_g : (modulePushforward g).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rg)
    (alpha_i : (modulePullback i).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Ri)
    (alpha_j : (modulePullback j).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rj)
    [Rf.IsRightDerivedFunctor alpha_f
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor alpha_g
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Ri.IsRightDerivedFunctor alpha_i
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rj.IsRightDerivedFunctor alpha_j
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    (I : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ) (_hI : I.IsKInjective) :
    alpha_j.app (((modulePushforward f).mapHomotopyCategory
          (ComplexShape.up ℤ)).obj ((HomotopyCategory.quotient _ _).obj I)) ≫
        Rj.map (alpha_f.app ((HomotopyCategory.quotient _ _).obj I)) ≫
        (derivedPushforwardRestrictIso f i j g h Rf Rg Ri Rj
          alpha_f alpha_g alpha_i alpha_j).hom.app
            (DerivedCategory.Qh.obj ((HomotopyCategory.quotient _ _).obj I)) =
      DerivedCategory.Qh.map
          ((pushforwardRestrictHomotopyMap f i j g h.w).app
            ((HomotopyCategory.quotient _ _).obj I)) ≫
        alpha_g.app (((modulePullback i).mapHomotopyCategory
          (ComplexShape.up ℤ)).obj ((HomotopyCategory.quotient _ _).obj I)) ≫
        Rg.map (alpha_i.app ((HomotopyCategory.quotient _ _).obj I))
```

## Tag 0D5W, a lemma

[Tag 0D5W](https://stacks.math.columbia.edu/tag/0D5W) in the Stacks Project.

**`Stacks.Cohomology.DerivedSectionsLeray.isIso_lerayComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean#L428). The attribute's comment: “over an open”.

> **Stacks 0D5W, over an open.**  For a morphism `f : X ⟶ Y` of ringed spaces and an open
> `V ⊆ Y`, derived sections over `V` after derived pushforward along `f` agree with derived sections
> over `f⁻¹ V`, as functors `D(𝒪_X) ⥤ D(Γ(V, 𝒪_Y))`: the canonical Leray comparison is an
> isomorphism, with no hypothesis on `f`.

```lean
theorem isIso_lerayComparison : IsIso (lerayComparison f V)
```

**`Stacks.Cohomology.DerivedSectionsLeray.isIso_lerayComparison_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean#L454). The attribute's comment: “global sections”.

> **Stacks 0D5W, global sections.**  `R Γ(Y, -) ∘ Rf_*` and `R Γ(X, -)` agree as functors
> `D(𝒪_X) ⥤ D(Γ(Y, 𝒪_Y))`: the Leray comparison at `V = ⊤` is an isomorphism.  Its source is
> derived sections over `f⁻¹ ⊤ = ⊤`, that is global derived sections on `X`, regarded as complexes
> of `Γ(Y, 𝒪_Y)`-modules by restriction of scalars along `f^♯`.

```lean
theorem isIso_lerayComparison_top : IsIso (lerayComparison f ⊤)
```

**`Stacks.Cohomology.DerivedSectionsLeray.isIso_lerayComparison_top_and_forall_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/LerayForDerivedSections.lean#L464). The attribute's comment: “both statements, for a morphism of ringed spaces: `RΓ(Y, -) ∘ Rf_* = RΓ(X, -)`, and `RΓ(U, -) = RΓ(V, -) ∘ Rf_*` for `V ⊆ Y` open and `U = f⁻¹ V`”.

> **Stacks 0D5W**, the whole lemma, stated for an arbitrary morphism of ringed spaces
> `f : X ⟶ Y` with no further hypothesis.  The canonical Leray comparison
> `RΓ(X, -) ⟶ RΓ(Y, -) ∘ Rf_*` of functors `D(𝒪_X) ⥤ D(Γ(Y, 𝒪_Y))` is an isomorphism, and more
> generally for every open `V ⊆ Y` with `U = f⁻¹ V` the comparison
> `RΓ(U, -) ⟶ RΓ(V, -) ∘ Rf_*` of functors `D(𝒪_X) ⥤ D(Γ(V, 𝒪_Y))` is an isomorphism.

```lean
theorem isIso_lerayComparison_top_and_forall_open {X₀ Y₀ : RingedSpace.{u, u}} (g : X₀ ⟶ Y₀) :
    IsIso (lerayComparison g ⊤) ∧ ∀ W : Opens Y₀.carrier, IsIso (lerayComparison g W)
```

## Tag 0D5X, a lemma

[Tag 0D5X](https://stacks.math.columbia.edu/tag/0D5X) in the Stacks Project.

**`Stacks.Cohomology.UnboundedHigherDirectImage.preimageCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean#L76). The attribute's comment: “preimage formula”.

> Cohomology over the inverse image `f⁻¹ V` agrees with cohomology over `V` after derived
> pushforward: `H^i(f⁻¹ V, K) = H^i(V, Rf_* K)`, naturally in `K`.

```lean
def preimageCohomologyIso (V : Opens Y.carrier) (i : ℤ) :
    derivedPreimageSections f V ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i ≅
      derivedPushforward f ⋙ derivedSectionsOverOpen Y V ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.preimageCohomologyEvaluationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean#L87). The attribute's comment: “values on opens”.

> The value on an open `V ⊆ Y` of the presheaf `derivedPreimageCohomologyPresheaf` is the
> hypercohomology `H^i(f⁻¹ V, K)` of `K` over the inverse image of `V`, naturally in `K`.

```lean
def preimageCohomologyEvaluationIso (V : Opens Y.carrier) (i : ℤ) :
    derivedPushforward f ⋙
        Stacks.Cohomology.HypercohomologyEdge.derivedSectionsPresheaf (structureSheafRing Y) ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u} (structureSheafRing Y).obj) i ⋙
        PresheafOfModules.evaluation (structureSheafRing Y).obj (op V) ≅
      derivedPreimageSections f V ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} ((structureSheafRing Y).obj.obj (op V))) i
```

**`Stacks.Cohomology.UnboundedHigherDirectImage.higherDirectImageIsoSheafifyPreimageCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CohomologySheavesOfADerivedPushforward.lean#L102). The attribute's comment: “associated sheaf”.

> The `i`-th cohomology sheaf of `Rf_* K` is the sheaf associated to the presheaf
> `V ↦ H^i(f⁻¹ V, K)`, naturally in `K`.

```lean
def higherDirectImageIsoSheafifyPreimageCohomology (i : ℤ) :
    derivedPushforward f ⋙
        DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing Y)) i ≅
      derivedPushforward f ⋙
        Stacks.Cohomology.HypercohomologyEdge.derivedSectionsPresheaf (structureSheafRing Y) ⋙
        DerivedCategory.homologyFunctor (PresheafOfModules.{u} (structureSheafRing Y).obj) i ⋙
        PresheafOfModules.sheafification (𝟙 (structureSheafRing Y).obj)
```

## Tag 0D5Y, a lemma

[Tag 0D5Y](https://stacks.math.columbia.edu/tag/0D5Y) in the Stacks Project.

**`Stacks.Cohomology.UnderlyingAbelianSheaf.sectionsForgetComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UnderlyingAbelianSheafCohomology.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UnderlyingAbelianSheafCohomology.lean#L422). The attribute's comment: “part (1)”.

> **Stacks 0D5Y, part (1).** Unbounded derived sections of modules agree canonically and
> naturally with derived sections after forgetting to abelian sheaves: for every open `U ⊆ X` the
> canonical map `RΓ(U, K) ⟶ RΓ(U, K_ab)` is an isomorphism in `D(Ab)`.

```lean
public theorem sectionsForgetComparison_isIso {X : TopCat.{u}}
    (O : Sheaf (Opens.grothendieckTopology X) RingCat.{u}) (U : Opens X) :
    IsIso (sectionsForgetComparison O U)
```

**`Stacks.Cohomology.UnderlyingAbelianPushforward.pushforwardForgetComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UnderlyingAbelianSheafPushforward.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedCategory/UnderlyingAbelianSheafPushforward.lean#L309). The attribute's comment: “part (2)”.

> **Stacks 0D5Y, part (2).**  The unbounded derived pushforward of a complex of
> `𝒪_X`-modules, with the module structure forgotten, agrees canonically and naturally with the
> unbounded derived pushforward of the underlying complex of abelian sheaves:
> `Rf_* K ⟶ Rf_*(K_ab)` is an isomorphism in `D(Ab_Y)`.
>
> The morphism `f` of ringed spaces is the only argument: there is no `HasRightDerivedFunctor`
> precondition here, both derived pushforwards being supplied by the proved instances
> `abelianPushforward_hasRightDerivedFunctor` and
> `isRightDerivedFunctor_pushforwardForgetSource` above.

```lean
theorem pushforwardForgetComparison_isIso :
    IsIso (Stacks.Cohomology.UnderlyingAbelianPushforward.pushforwardForgetComparison f)
```

## Tag 08BT, a lemma

[Tag 08BT](https://stacks.math.columbia.edu/tag/08BT) in the Stacks Project.

**`Stacks.ExtensionByZero.exists_derivedJShriek_restriction_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/DerivedAdjunction.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/ExtensionByZero/DerivedAdjunction.lean#L105).

> For an open subset `U` of a ringed space `X`, extension by zero and restriction to `U` are
> exact, and the functor on unbounded derived categories induced by extension by zero is left
> adjoint to the functor induced by restriction to `U`.

```lean
theorem exists_derivedJShriek_restriction_adjunction
    (X : SheafedSpace RingCat.{u}) (U : Opens X.carrier) :
    ∃ (h₁ : (jShriek00A7 X U).Additive)
      (h₂ : PreservesFiniteLimits (jShriek00A7 X U))
      (h₃ : PreservesFiniteColimits (jShriek00A7 X U))
      (h₄ : (restMod X U).Additive)
      (h₅ : PreservesFiniteLimits (restMod X U))
      (h₆ : PreservesFiniteColimits (restMod X U)),
      letI := h₁
      letI := h₂
      letI := h₃
      letI := h₄
      letI := h₅
      letI := h₆
      Nonempty ((jShriek00A7 X U).mapDerivedCategory ⊣ (restMod X U).mapDerivedCategory)
```

## Tag 0D5Z, a lemma

[Tag 0D5Z](https://stacks.math.columbia.edu/tag/0D5Z) in the Stacks Project.

**`RingedSpaceModuleAdjunction.isKInjective_modulePushforward_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatPushforwardOfKInjectives.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/FlatPushforwardOfKInjectives.lean#L49).

> **Stacks 0D5Z.** If `f : X ⟶ Y` is a flat morphism of ringed spaces and `ℐ^•` is a
> K-injective complex of `𝒪_X`-modules, then `f_* ℐ^•` is K-injective as a complex of
> `𝒪_Y`-modules.

```lean
theorem isKInjective_modulePushforward_of_isFlat {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (hf : AlgebraicGeometry.IsFlat f)
    (I : CochainComplex (_root_.SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (hI : I.IsKInjective) :
    CochainComplex.IsKInjective
      (((modulePushforward f).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.32, Tag 0D5U](https://stacks.math.columbia.edu/tag/0D5U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
