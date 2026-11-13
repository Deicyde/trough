---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.injective_smallProetaleInverseImage, AlgebraicGeometry.ProEtale.injective_smallProetaleRestriction, AlgebraicGeometry.ProEtale.isKInjective_smallProetaleInverseImage, AlgebraicGeometry.ProEtale.isKInjective_smallProetaleRestriction, AlgebraicGeometry.ProEtale.bigSmallDerivedPushforwardIso, AlgebraicGeometry.ProEtale.derivedBigPushforwardSmallBaseChangeIso, AlgebraicGeometry.ProEtale.derivedBigPushforwardBigBaseChangeIso, AlgebraicGeometry.ProEtale.nonempty_derivedPushforward_bigSmall_baseChange_iso
statement: formalized
proof: formalized
---

# 61.17 Comparing big and small topoi

Section 61.17 of the Stacks Project, [Tag 0F66](https://stacks.math.columbia.edu/tag/0F66). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F67, a lemma

[Tag 0F67](https://stacks.math.columbia.edu/tag/0F67) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.injective_smallProetaleInverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean#L81). The attribute's comment: “injective\_pullback\_t”.

> Inverse image to the small pro-étale site of `T` preserves injective
> abelian sheaves on the big pro-étale site over `S`.

```lean
public lemma injective_smallProetaleInverseImage
    (I : Sheaf (BigProetaleOver.topology B S.obj S.property) Ab.{w})
    [Injective I] :
    Injective (((smallProetaleToBigProetaleFunctor B T S f).sheafPushforwardContinuous
      Ab.{w}
      (SmallProetale.topology B T.obj T.property)
      (BigProetaleOver.topology B S.obj S.property)).obj I)
```

**`AlgebraicGeometry.ProEtale.injective_smallProetaleRestriction`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean#L108). The attribute's comment: “injective\_restriction\_s”.

> Restricting an injective abelian sheaf from the big pro-étale site over `S`
> to the small pro-étale site of `S` preserves injectivity.

```lean
public lemma injective_smallProetaleRestriction
    (I : Sheaf (BigProetaleOver.topology B S hS) Ab.{w})
    [Injective I] :
    Injective (((SmallProetale.inclusion B S hS).sheafPushforwardContinuous
      Ab.{w}
      (SmallProetale.topology B S hS)
      (BigProetaleOver.topology B S hS)).obj I)
```

**`AlgebraicGeometry.ProEtale.isKInjective_smallProetaleInverseImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean#L133). The attribute's comment: “kinjective\_pullback\_t”.

> The inverse image of a K-injective complex of abelian sheaves from the big
> pro-étale site over `S` to the small pro-étale site of `T` is K-injective.

```lean
public lemma isKInjective_smallProetaleInverseImage
    (I : CochainComplex
      (Sheaf (BigProetaleOver.topology B S.obj S.property) AddCommGrpCat.{w}) ℤ)
    [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((((smallProetaleToBigProetaleFunctor B T S f).sheafPushforwardContinuous
        AddCommGrpCat.{w}
        (SmallProetale.topology B T.obj T.property)
        (BigProetaleOver.topology B S.obj S.property)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.ProEtale.isKInjective_smallProetaleRestriction`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Injectives.lean#L155). The attribute's comment: “kinjective\_restriction\_s”.

> Restricting a K-injective complex from the big pro-étale site over `S`
> to the small pro-étale site of `S` preserves K-injectivity.

```lean
public lemma isKInjective_smallProetaleRestriction
    (I : CochainComplex
      (Sheaf (BigProetaleOver.topology B S hS) AddCommGrpCat.{u + 1}) ℤ)
    [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((((SmallProetale.inclusion B S hS).sheafPushforwardContinuous
        AddCommGrpCat.{u + 1}
        (SmallProetale.topology B S hS)
        (BigProetaleOver.topology B S hS)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I)
```

## Tag 0F68, a lemma

[Tag 0F68](https://stacks.math.columbia.edu/tag/0F68) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigSmallDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforward.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforward.lean#L270). The attribute's comment: “big\_small\_direct\_image”.

> Restricting the derived direct image along `f` on the big pro-étale sites to the small
> pro-étale site of `S` is naturally isomorphic to taking the derived direct image along `f` on the
> small pro-étale sites of the restriction to the small pro-étale site of `T`.

```lean
public noncomputable def bigSmallDerivedPushforwardIso
    [HasDerivedCategory (BigAb B T)] [HasDerivedCategory (BigAb B S)]
    [HasDerivedCategory (SmallAb B T)] [HasDerivedCategory (SmallAb B S)]
    (Rbig : DerivedCategory (BigAb B T) ⥤ DerivedCategory (BigAb B S))
    (Rsmall : DerivedCategory (SmallAb B T) ⥤ DerivedCategory (SmallAb B S))
    (αbig : (bigPush B T S f).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ Rbig)
    (αsmall : (smallPush B T S f).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ Rsmall)
    [Rbig.IsRightDerivedFunctor αbig
      (HomologicalComplex.quasiIso (BigAb B T) (ComplexShape.up ℤ))]
    [Rsmall.IsRightDerivedFunctor αsmall
      (HomologicalComplex.quasiIso (SmallAb B T) (ComplexShape.up ℤ))] :
    Rbig ⋙ (restrict B S).mapDerivedCategory ≅
      (restrict B T).mapDerivedCategory ⋙ Rsmall
```

**`AlgebraicGeometry.ProEtale.derivedBigPushforwardSmallBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean#L244). The attribute's comment: “base\_changed\_small\_direct\_image”.

> The derived big direct image restricted to the small site of `S'` agrees
> naturally with small direct image after restriction to `T'`.

```lean
public noncomputable def derivedBigPushforwardSmallBaseChangeIso
    (h : IsPullback g' f' f g)
    (RFbig : DerivedCategory (BigAb B T) ⥤ DerivedCategory (BigAb B S))
    (αbig : (bigCocontPush B f).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RFbig)
    [RFbig.IsRightDerivedFunctor αbig
      (HomotopyCategory.quasiIso (BigAb B T) (ComplexShape.up ℤ))]
    (RFsmall : DerivedCategory (SmallAb B T') ⥤ DerivedCategory (SmallAb B S'))
    (αsmall : (smallBaseChangePush B f').mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RFsmall)
    [RFsmall.IsRightDerivedFunctor αsmall
      (HomotopyCategory.quasiIso (SmallAb B T') (ComplexShape.up ℤ))] :
    RFbig ⋙ (restriction g).mapDerivedCategory ≅
      (restriction g').mapDerivedCategory ⋙ RFsmall
```

**`AlgebraicGeometry.ProEtale.derivedBigPushforwardBigBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean#L341). The attribute's comment: “base\_changed\_big\_direct\_image”.

> The derived big direct image along `f`, pulled back to the big pro-étale site over `S'`,
> agrees naturally with the derived big direct image along `f'` of the pullback to the big
> pro-étale site over `T'`.

```lean
public noncomputable def derivedBigPushforwardBigBaseChangeIso
    (h : IsPullback g' f' f g)
    (RFbig : DerivedCategory (BigAb B T) ⥤ DerivedCategory (BigAb B S))
    (αbig : (bigCocontPush B f).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RFbig)
    [RFbig.IsRightDerivedFunctor αbig
      (HomotopyCategory.quasiIso (BigAb B T) (ComplexShape.up ℤ))]
    (RFbig' : DerivedCategory (BigAb B T') ⥤ DerivedCategory (BigAb B S'))
    (αbig' : (bigCocontPush B f').mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RFbig')
    [RFbig'.IsRightDerivedFunctor αbig'
      (HomotopyCategory.quasiIso (BigAb B T') (ComplexShape.up ℤ))] :
    RFbig ⋙ (bigInverseImage B S' S g).mapDerivedCategory ≅
      (bigInverseImage B T' T g').mapDerivedCategory ⋙ RFbig'
```

**`AlgebraicGeometry.ProEtale.nonempty_derivedPushforward_bigSmall_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/DerivedPushforwardBaseChange.lean#L381).

> **Stacks 0F68.** Let `f : T ⟶ S` be a morphism of a big pro-étale site, `g : S' ⟶ S` an
> object of the big pro-étale site of `S`, and `T'` the fibre product, with projections
> `g' : T' ⟶ T` and `f' : T' ⟶ S'`. Then, naturally in `K` in `D((Sch/T)_proet)`,
> * `(Rf_big,* K)|_{S_proet} ≅ Rf_small,* (K|_{T_proet})` in `D(S_proet)`,
> * `i_g⁻¹ (Rf_big,* K) ≅ Rf'_small,* (i_g'⁻¹ K)` in `D(S'_proet)`, and
> * `g_big⁻¹ (Rf_big,* K) ≅ Rf'_big,* (g'_big⁻¹ K)` in `D((Sch/S')_proet)`.
>
> Each derived direct image is any right derived functor of the corresponding direct image of
> abelian sheaves, given with its comparison transformation. The first equality is the second one
> for the identity of `S`.

```lean
public theorem nonempty_derivedPushforward_bigSmall_baseChange_iso
    (h : IsPullback g' f' f g)
    (RFbig : DerivedCategory (BigAb B T) ⥤ DerivedCategory (BigAb B S))
    (αbig : (bigCocontPush B f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RFbig)
    [RFbig.IsRightDerivedFunctor αbig
      (HomotopyCategory.quasiIso (BigAb B T) (ComplexShape.up ℤ))]
    (RFsmall : DerivedCategory (SmallAb B T) ⥤ DerivedCategory (SmallAb B S))
    (αsmall : (smallBaseChangePush B f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RFsmall)
    [RFsmall.IsRightDerivedFunctor αsmall
      (HomotopyCategory.quasiIso (SmallAb B T) (ComplexShape.up ℤ))]
    (RF'small : DerivedCategory (SmallAb B T') ⥤ DerivedCategory (SmallAb B S'))
    (α'small : (smallBaseChangePush B f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'small)
    [RF'small.IsRightDerivedFunctor α'small
      (HomotopyCategory.quasiIso (SmallAb B T') (ComplexShape.up ℤ))]
    (RF'big : DerivedCategory (BigAb B T') ⥤ DerivedCategory (BigAb B S'))
    (α'big : (bigCocontPush B f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'big)
    [RF'big.IsRightDerivedFunctor α'big
      (HomotopyCategory.quasiIso (BigAb B T') (ComplexShape.up ℤ))] :
    Nonempty (RFbig ⋙ (restriction (𝟙 S)).mapDerivedCategory ≅
      (restriction (𝟙 T)).mapDerivedCategory ⋙ RFsmall) ∧
    Nonempty (RFbig ⋙ (restriction g).mapDerivedCategory ≅
      (restriction g').mapDerivedCategory ⋙ RF'small) ∧
    Nonempty (RFbig ⋙ (bigInverseImage B S' S g).mapDerivedCategory ≅
      (bigInverseImage B T' T g').mapDerivedCategory ⋙ RF'big)
```

## Tag 0F69, a lemma

[Tag 0F69](https://stacks.math.columbia.edu/tag/0F69) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigProetaleCohomology_inclusionInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean#L403). The attribute's comment: “part (3)”.

> The big pro-étale cohomology over `T` of the inverse image of `M` along `f` agrees with the
> small pro-étale cohomology of `T` with coefficients in the restriction of `M` along `f`.

```lean
public noncomputable def bigProetaleCohomology_inclusionInverseImage
    (M : DerivedCategory (BigAb B S)) (n : ℤ) :
    cohomology (BigProetaleOver.topology B T.obj T.property)
        ((bigInverseImage B T S f).mapDerivedCategory.obj M) n ≃+
      cohomology (SmallProetale.topology B T.obj T.property)
        ((inclusionInverseImage B T S f).mapDerivedCategory.obj M) n
```

**`AlgebraicGeometry.ProEtale.bigProetaleCohomology_projectionInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean#L415). The attribute's comment: “part (2)”.

> Pulling a small-site complex back to the big site and then computing
> cohomology over `T` agrees with its small-site pullback along `f`.

```lean
public noncomputable def bigProetaleCohomology_projectionInverseImage
    (K : DerivedCategory (SmallAb B S)) (n : ℤ) :
    cohomology (BigProetaleOver.topology B T.obj T.property)
        ((bigInverseImage B T S f).mapDerivedCategory.obj
          ((projectionInverseImage B S).mapDerivedCategory.obj K)) n ≃+
      cohomology (SmallProetale.topology B T.obj T.property)
        ((smallInverseImage B T S f).mapDerivedCategory.obj K) n
```

**`AlgebraicGeometry.ProEtale.bigProetaleCohomology_projectionInverseImage_self`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Cohomology.lean#L429). The attribute's comment: “part (1)”.

> The big pro-étale cohomology over `S` of the inverse image of a small pro-étale complex `K`
> along the projection agrees with the small pro-étale cohomology of `K`.

```lean
public noncomputable def bigProetaleCohomology_projectionInverseImage_self
    (K : DerivedCategory (SmallAb B S)) (n : ℤ) :
    cohomology (BigProetaleOver.topology B S.obj S.property)
        ((projectionInverseImage B S).mapDerivedCategory.obj K) n ≃+
      cohomology (SmallProetale.topology B S.obj S.property) K n
```

## Tag 0F6A, a lemma

[Tag 0F6A](https://stacks.math.columbia.edu/tag/0F6A) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.proetaleCohomologicalDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/CohomologicalDescent.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/CohomologicalDescent.lean#L212).

> **Stacks 0F6A.** For a scheme `S` of a chosen big pro-étale site and a complex `K` of
> abelian sheaves on the small pro-étale site of `S`, the canonical map
> `K ⟶ Rπ_{S,*} π_S^{-1} K` is an isomorphism.

```lean
public theorem proetaleCohomologicalDescent
    (K : DerivedCategory (Sheaf (SmallProetale.topology B S hS) AddCommGrpCat.{u + 1})) :
    IsIso ((derivedProjectionAdjunction B S hS).unit.app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.17, Tag 0F66](https://stacks.math.columbia.edu/tag/0F66)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
