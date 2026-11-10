---
declaration: section
origin: cited
lean: AlgebraicGeometry.injective_smallEtaleRestriction, AlgebraicGeometry.injective_smallEtaleRestrictionAlong, AlgebraicGeometry.isKInjective_smallEtaleRestriction, AlgebraicGeometry.isKInjective_smallEtaleRestrictionAlong, AlgebraicGeometry.smallEtaleRestrictionPushforwardIso, AlgebraicGeometry.bigEtaleRestrictionPushforwardIso, AlgebraicGeometry.smallEtaleRestrictionPushforwardModules_eq, AlgebraicGeometry.smallEtaleModulePullbackProjectionIso
statement: formalized
proof: formalized
---

# 59.99 Comparing big and small topoi

Section 59.99 of the Stacks Project, [Tag 0757](https://stacks.math.columbia.edu/tag/0757). 6 tags here are carried by 31 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0758, a lemma

[Tag 0758](https://stacks.math.columbia.edu/tag/0758) in the Stacks Project.

**`AlgebraicGeometry.injective_smallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean#L200). The attribute's comment: “injective\_restrict\_s”.

> **Stacks Project, Tag 0758.** Restriction of an injective abelian sheaf
> from the big étale site over `S` to the small étale site of `S` is injective.

```lean
public theorem injective_smallEtaleRestriction
    (S : Scheme.{u}) (hS : B.Contains S)
    (I : Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1})
    [Injective I] :
    Injective (((SmallEtale.inclusion B S hS).sheafPushforwardContinuous
      Ab.{u + 1} (SmallEtale.topology B S hS)
      (BigEtaleOver.topology B S hS)).obj I)
```

**`AlgebraicGeometry.injective_smallEtaleRestrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean#L212). The attribute's comment: “injective\_restrict\_t”.

> **Stacks Project, Tag 0758.** Restriction to the small étale site of an
> object of the big étale site preserves injectivity of abelian sheaves.

```lean
public theorem injective_smallEtaleRestrictionAlong
    (T S : B.Scheme) (f : T ⟶ S)
    (I : Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
    [Injective I] :
    Injective
      (((smallEtaleToBigEtaleFunctor B T S f).sheafPushforwardContinuous
        Ab.{u + 1} (SmallEtale.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property)).obj I)
```

**`AlgebraicGeometry.isKInjective_smallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean#L225). The attribute's comment: “kinjective\_restrict\_s”.

> **Stacks Project, Tag 0758.** Restriction of a K-injective complex of
> abelian sheaves from the big étale site to the small étale site is K-injective.

```lean
public theorem isKInjective_smallEtaleRestriction
    (S : Scheme.{u}) (hS : B.Contains S)
    (I : CochainComplex (Sheaf (BigEtaleOver.topology B S hS) Ab.{u + 1}) ℤ)
    [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((((SmallEtale.inclusion B S hS).sheafPushforwardContinuous
        Ab.{u + 1} (SmallEtale.topology B S hS)
        (BigEtaleOver.topology B S hS)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.isKInjective_smallEtaleRestrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Restriction.lean#L239). The attribute's comment: “kinjective\_restrict\_t”.

> **Stacks Project, Tag 0758.** Restriction to the small étale site of an
> object of the big étale site preserves K-injectivity of abelian sheaf complexes.

```lean
public theorem isKInjective_smallEtaleRestrictionAlong
    (T S : B.Scheme) (f : T ⟶ S)
    (I : CochainComplex (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1}) ℤ)
    [I.IsKInjective] :
    CochainComplex.IsKInjective
      ((((smallEtaleToBigEtaleFunctor B T S f).sheafPushforwardContinuous
        Ab.{u + 1} (SmallEtale.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property)).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I)
```

## Tag 0759, an equation

[Tag 0759](https://stacks.math.columbia.edu/tag/0759) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleRestrictionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DirectImage.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DirectImage.lean#L65). The attribute's comment: “arbitrary\_coefficients”.

> For a sheaf `ℱ` on the big étale site over `T` with values in any category, the restriction
> `(f_{big, *}ℱ)|_{S_étale}` of its direct image along `f` agrees naturally with the direct image
> `f_{small, *}(ℱ|_{T_étale})` of its restriction.

```lean
public noncomputable def smallEtaleRestrictionPushforwardIso (A : Type w) [Category.{w'} A] :
    (Over.pullback f).sheafPushforwardContinuous A
        (BigEtaleOver.topology B S.obj S.property)
        (BigEtaleOver.topology B T.obj T.property) ⋙
      (SmallEtale.inclusion B S.obj S.property).sheafPushforwardContinuous A
        (SmallEtale.topology B S.obj S.property)
        (BigEtaleOver.topology B S.obj S.property) ≅
    (SmallEtale.inclusion B T.obj T.property).sheafPushforwardContinuous A
        (SmallEtale.topology B T.obj T.property)
        (BigEtaleOver.topology B T.obj T.property) ⋙
      (smallEtaleBaseChange B f).sheafPushforwardContinuous A
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigEtaleRestrictionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DirectImage.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DirectImage.lean#L112). The attribute's comment: “direct\_images\_of\_topoi”.

> The direct image along the morphism of topoi `f_big` followed by restriction along the
> projection `π_S` agrees naturally with restriction along `π_T` followed by the direct image along
> `f_small`.

```lean
public noncomputable def bigEtaleRestrictionPushforwardIso :
    (bigEtaleMorphism B T S f).pushforward ⋙
        (bigEtaleToSmallEtaleMorphism B S.obj S.property).pushforward ≅
      (bigEtaleToSmallEtaleMorphism B T.obj T.property).pushforward ⋙
        (smallEtaleBaseChange B f).sheafPushforwardContinuous (Type (u + 1))
          (SmallEtale.topology B S.obj S.property)
          (SmallEtale.topology B T.obj T.property)
```

**`AlgebraicGeometry.smallEtaleRestrictionPushforwardModules_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean#L277). The attribute's comment: “sheaves of `𝒪`-modules on the big and small étale sites of schemes, at the module universe `u + 1` of the étale cohomology comparisons of Stacks 0DDH”.

> Restriction to the small étale site of `S` of the direct image along `f_big` of a sheaf of
> `𝒪`-modules is the direct image along `f_small` of its restriction to the small étale site of
> `T`:
> `(f_{big,*}ℱ)|_{S_étale} = f_{small,*}(ℱ|_{T_étale})`, as an equality of functors.

```lean
public theorem smallEtaleRestrictionPushforwardModules_eq :
    Stacks.SheafOfModules.inverseImage.{u + 1}
          (SmallEtale.topology B T.obj T.property)
          (BigEtaleOver.topology B T.obj T.property)
          (SmallEtale.inclusion B T.obj T.property)
          (BigEtaleOver.structureSheaf B T.obj T.property) ⋙
        smallEtaleModulePushforward B T S f =
      bigEtaleModulePushforward B T S f ⋙
        Stacks.SheafOfModules.inverseImage.{u + 1}
          (SmallEtale.topology B S.obj S.property)
          (BigEtaleOver.topology B S.obj S.property)
          (SmallEtale.inclusion B S.obj S.property)
          (BigEtaleOver.structureSheaf B S.obj S.property)
```

**`AlgebraicGeometry.smallEtaleModulePullbackProjectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModulePullback.lean#L350). The attribute's comment: “inverse images of sheaves of `𝒪`-modules on the big and small étale sites of schemes, at the module universe `u + 1` of the étale cohomology comparisons of Stacks 0DDH”.

> The mate of `AlgebraicGeometry.smallEtaleRestrictionPushforwardModules_eq` on inverse images
> of sheaves of `𝒪`-modules on the big and small étale sites of schemes:
> `π_T^* ∘ f_small^* ≅ f_big^* ∘ π_S^*`, that is `f_big^{-1}(π_S^*K) ≅ π_T^*(f_small^*K)`, where
> `π^*` is the lower shriek of Stacks 0797 along the small étale inclusion and `f_big^*` is the
> inverse image of Stacks 04CC part (2).

```lean
public def smallEtaleModulePullbackProjectionIso :
    smallEtaleModulePullbackLarge B T S f ⋙
        Stacks.SheafOfModules.lowerShriek.{u + 1}
          (SmallEtale.topology B T.obj T.property)
          (BigEtaleOver.topology B T.obj T.property)
          (SmallEtale.inclusion B T.obj T.property)
          (BigEtaleOver.structureSheaf B T.obj T.property) ≅
      Stacks.SheafOfModules.lowerShriek.{u + 1}
          (SmallEtale.topology B S.obj S.property)
          (BigEtaleOver.topology B S.obj S.property)
          (SmallEtale.inclusion B S.obj S.property)
          (BigEtaleOver.structureSheaf B S.obj S.property) ⋙
        bigEtaleInverseImageModules B T S f
```

**`AlgebraicGeometry.bigEtalePullbackProjectionPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean#L130). The attribute's comment: “inverse images”.

> **The inverse-image square of Stacks 0759.** Pulling a sheaf on the small étale site of `S`
> back to the big étale site over `S` and then restricting along `f` agrees with pulling it back to
> the small étale site of `T` and then up to the big étale site over `T`:
> `f_{big}^{-1}π_S^{-1} ≅ π_T^{-1}f_{small}^{-1}`.
>
> This is the mate of `AlgebraicGeometry.smallEtaleRestrictionPushforwardIso`: all four functors are
> left adjoints of the four restrictions appearing there, and uniqueness of left adjoints transports
> the isomorphism.

```lean
public def bigEtalePullbackProjectionPullbackIso :
    (SmallEtale.inclusion B S.obj S.property).sheafPullback A
        (SmallEtale.topology B S.obj S.property)
        (BigEtaleOver.topology B S.obj S.property) ⋙
      (Over.map f).sheafPushforwardContinuous A
        (BigEtaleOver.topology B T.obj T.property)
        (BigEtaleOver.topology B S.obj S.property) ≅
    (smallEtaleBaseChange B f).sheafPullback A
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property) ⋙
      (SmallEtale.inclusion B T.obj T.property).sheafPullback A
        (SmallEtale.topology B T.obj T.property)
        (BigEtaleOver.topology B T.obj T.property)
```

## Tag 075A, a lemma

[Tag 075A](https://stacks.math.columbia.edu/tag/075A) in the Stacks Project.

**`AlgebraicGeometry.bigEtaleDerivedPushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/BaseChange.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/BaseChange.lean#L125). The attribute's comment: “big\_site\_base\_change\_abelian”.

> Base change for the derived direct image of abelian sheaves on big étale sites.

```lean
public noncomputable def bigEtaleDerivedPushforwardBaseChangeIso
    (D : CartesianBaseChangeSituation.{u})
    [HasSheafify (BigEtaleOver.topology D.B D.T.obj D.T.property) Ab.{u + 1}]
    [HasSheafify (BigEtaleOver.topology D.B D.S.obj D.S.property) Ab.{u + 1}]
    [HasSheafify (BigEtaleOver.topology D.B D.T'.obj D.T'.property) Ab.{u + 1}]
    [HasSheafify (BigEtaleOver.topology D.B D.S'.obj D.S'.property) Ab.{u + 1}]
    [HasDerivedCategory.{wT} (Sheaf (BigEtaleOver.topology D.B D.T.obj D.T.property) Ab.{u + 1})]
    [HasDerivedCategory.{wS} (Sheaf (BigEtaleOver.topology D.B D.S.obj D.S.property) Ab.{u + 1})]
    [HasDerivedCategory.{wT'} (Sheaf (BigEtaleOver.topology D.B D.T'.obj D.T'.property) Ab.{u + 1})]
    [HasDerivedCategory.{wS'} (Sheaf (BigEtaleOver.topology D.B D.S'.obj D.S'.property) Ab.{u + 1})]
    [(Over.map D.g.hom).IsContinuous
      (BigEtaleOver.topology D.B D.S'.obj D.S'.property)
      (BigEtaleOver.topology D.B D.S.obj D.S.property)]
    [(Over.map D.g').IsContinuous
      (BigEtaleOver.topology D.B D.T'.obj D.T'.property)
      (BigEtaleOver.topology D.B D.T.obj D.T.property)]
    [((Over.map D.f).sheafPushforwardCocontinuous Ab.{u + 1}
      (BigEtaleOver.topology D.B D.T.obj D.T.property)
      (BigEtaleOver.topology D.B D.S.obj D.S.property)).Additive]
    [((Over.map D.f').sheafPushforwardCocontinuous Ab.{u + 1}
      (BigEtaleOver.topology D.B D.T'.obj D.T'.property)
      (BigEtaleOver.topology D.B D.S'.obj D.S'.property)).Additive]
    [((Over.map D.g.hom).sheafPushforwardContinuous Ab.{u + 1}
      (BigEtaleOver.topology D.B D.S'.obj D.S'.property)
      (BigEtaleOver.topology D.B D.S.obj D.S.property)).Additive]
    [((Over.map D.g').sheafPushforwardContinuous Ab.{u + 1}
      (BigEtaleOver.topology D.B D.T'.obj D.T'.property)
      (BigEtaleOver.topology D.B D.T.obj D.T.property)).Additive]
    (Rf : DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.T.obj D.T.property) Ab.{u + 1}) ⥤
      DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.S.obj D.S.property) Ab.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.T'.obj D.T'.property) Ab.{u + 1}) ⥤
      DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.S'.obj D.S'.property) Ab.{u + 1}))
    (Rg : DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.S.obj D.S.property) Ab.{u + 1}) ⥤
      DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.S'.obj D.S'.property) Ab.{u + 1}))
    (Rg' : DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.T.obj D.T.property) Ab.{u + 1}) ⥤
      DerivedCategory (Sheaf (BigEtaleOver.topology D.B D.T'.obj D.T'.property) Ab.{u + 1}))
    (αf : homotopyToDerived
      ((Over.map D.f).sheafPushforwardCocontinuous Ab.{u + 1}
        (BigEtaleOver.topology D.B D.T.obj D.T.property)
        (BigEtaleOver.topology D.B D.S.obj D.S.property)) ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : homotopyToDerived
      ((Over.map D.f').sheafPushforwardCocontinuous Ab.{u + 1}
        (BigEtaleOver.topology D.B D.T'.obj D.T'.property)
        (BigEtaleOver.topology D.B D.S'.obj D.S'.property)) ⟶ DerivedCategory.Qh ⋙ Rf')
    (αg : homotopyToDerived
      ((Over.map D.g.hom).sheafPushforwardContinuous Ab.{u + 1}
        (BigEtaleOver.topology D.B D.S'.obj D.S'.property)
        (BigEtaleOver.topology D.B D.S.obj D.S.property)) ⟶ DerivedCategory.Qh ⋙ Rg)
    (αg' : homotopyToDerived
      ((Over.map D.g').sheafPushforwardContinuous Ab.{u + 1}
        (BigEtaleOver.topology D.B D.T'.obj D.T'.property)
        (BigEtaleOver.topology D.B D.T.obj D.T.property)) ⟶ DerivedCategory.Qh ⋙ Rg')
    [Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    [Rg'.IsRightDerivedFunctor αg' (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))] :
    Rf ⋙ Rg ≅ Rg' ⋙ Rf'
```

**`AlgebraicGeometry.bigSmallEtaleDerivedPushforwardRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L178). The attribute's comment: “part (1)”.

> For a morphism `f : T ⟶ S` of schemes and `K` in the unbounded derived category
> `D((Sch/T)_étale)` of abelian sheaves on the big étale site,
> `(Rf_{big, *}K)|_{S_étale} = Rf_{small, *}(K|_{T_étale})` in `D(S_étale)`, naturally in `K`.

```lean
def bigSmallEtaleDerivedPushforwardRestrictionIso :
    bigEtaleDerivedPushforward B f ⋙ (smallEtaleAbelianRestriction B S).mapDerivedCategory ≅
      (smallEtaleAbelianRestriction B T).mapDerivedCategory ⋙ smallEtaleDerivedPushforward B f
```

**`AlgebraicGeometry.bigEtaleDerivedPushforwardInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L282). The attribute's comment: “part (5)”.

> Let `f : T ⟶ S` be a morphism of schemes, `g : S' ⟶ S` an object of `(Sch/S)_étale` and
> `T' = T ×_S S'` with projections `f' : T' ⟶ S'` and `g' : T' ⟶ T`. For `K` in `D((Sch/T)_étale)`,
> `g_big^{-1}(Rf_{big, *}K) = Rf'_{big, *}((g'_big)^{-1}K)` in `D((Sch/S')_étale)`, naturally in `K`.

```lean
def bigEtaleDerivedPushforwardInverseImageIso :
    bigEtaleDerivedPushforward D.B D.f ⋙
        (bigEtaleAbelianInverseImage D.B D.gHom).mapDerivedCategory ≅
      (bigEtaleAbelianInverseImage D.B D.g').mapDerivedCategory ⋙
        bigEtaleDerivedPushforward D.B D.f'
```

**`AlgebraicGeometry.smallEtaleDerivedPushforwardRestrictionAlongIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L323). The attribute's comment: “part (3)”.

> In the situation of part (5), for `K` in `D((Sch/T)_étale)`,
> `i_g^{-1}(Rf_{big, *}K) = Rf'_{small, *}(i_{g'}^{-1}K)` in `D(S'_étale)`, naturally in `K`.

```lean
def smallEtaleDerivedPushforwardRestrictionAlongIso :
    bigEtaleDerivedPushforward D.B D.f ⋙
        (smallEtaleAbelianRestrictionAlong D.B D.gHom).mapDerivedCategory ≅
      (smallEtaleAbelianRestrictionAlong D.B D.g').mapDerivedCategory ⋙
        smallEtaleDerivedPushforward D.B D.f'
```

**`AlgebraicGeometry.bigSmallEtaleDerivedModulePushforwardRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L498). The attribute's comment: “part (2)”.

> For a morphism `f : T ⟶ S` of schemes and `K` in the unbounded derived category
> `D((Sch/T)_étale, 𝒪)` of `𝒪`-modules on the big étale site,
> `(Rf_{big, *}K)|_{S_étale} = Rf_{small, *}(K|_{T_étale})` in `D(Mod(S_étale, 𝒪_S))`, naturally in
> `K`.

```lean
def bigSmallEtaleDerivedModulePushforwardRestrictionIso :
    Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := bigEtaleOverRingedTopos B T)
        (Y := bigEtaleOverRingedTopos B S) (bigEtaleRingedToposHom B f) ⋙
        (bigToSmallEtaleRingedToposHom B S).pushforwardModules.mapDerivedCategory ≅
      (bigToSmallEtaleRingedToposHom B T).pushforwardModules.mapDerivedCategory ⋙
        Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := smallEtaleRingedTopos B T)
          (Y := smallEtaleRingedTopos B S) (smallEtaleRingedToposHom B f)
```

**`AlgebraicGeometry.bigEtaleDerivedModulePushforwardInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L643). The attribute's comment: “part (6)”.

> Let `f : T ⟶ S` be a morphism of schemes, `g : S' ⟶ S` an object of `(Sch/S)_étale` and
> `T' = T ×_S S'` with projections `f' : T' ⟶ S'` and `g' : T' ⟶ T`. For `K` in
> `D((Sch/T)_étale, 𝒪)`, `g_big^*(Rf_{big, *}K) = Rf'_{big, *}((g'_big)^*K)` in
> `D((Sch/S')_étale, 𝒪)`, naturally in `K`.

```lean
def bigEtaleDerivedModulePushforwardInverseImageIso :
    Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := bigEtaleOverRingedTopos D.B D.T)
        (Y := bigEtaleOverRingedTopos D.B D.S) (bigEtaleRingedToposHom D.B D.f) ⋙
        (bigEtaleModuleInverseImage D.B D.gHom).mapDerivedCategory ≅
      (bigEtaleModuleInverseImage D.B D.g').mapDerivedCategory ⋙
        Stacks.Cohomology.DerivedPushforward.derivedPushforward
          (X := bigEtaleOverRingedTopos D.B D.T') (Y := bigEtaleOverRingedTopos D.B D.S')
          (bigEtaleRingedToposHom D.B D.f')
```

**`AlgebraicGeometry.smallEtaleDerivedModulePushforwardRestrictionAlongIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean, line 693](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedPushforwardRestriction.lean#L693). The attribute's comment: “part (4)”.

> In the situation of part (6), for `K` in `D((Sch/T)_étale, 𝒪)`,
> `i_g^*(Rf_{big, *}K) = Rf'_{small, *}(i_{g'}^*K)` in `D(Mod(S'_étale, 𝒪_{S'}))`, naturally in `K`.

```lean
def smallEtaleDerivedModulePushforwardRestrictionAlongIso :
    Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := bigEtaleOverRingedTopos D.B D.T)
        (Y := bigEtaleOverRingedTopos D.B D.S) (bigEtaleRingedToposHom D.B D.f) ⋙
        (smallEtaleModuleRestrictionAlong D.B D.gHom).mapDerivedCategory ≅
      (smallEtaleModuleRestrictionAlong D.B D.g').mapDerivedCategory ⋙
        Stacks.Cohomology.DerivedPushforward.derivedPushforward
          (X := smallEtaleRingedTopos D.B D.T') (Y := smallEtaleRingedTopos D.B D.S')
          (smallEtaleRingedToposHom D.B D.f')
```

## Tag 0DDH, a lemma

[Tag 0DDH](https://stacks.math.columbia.edu/tag/0DDH) in the Stacks Project.

**`AlgebraicGeometry.bigSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Cohomology.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/Cohomology.lean#L183). The attribute's comment: “big\_small\_abelian”.

> The canonical comparison of big-site cohomology over `T` with small-site
> cohomology of the restricted complex, natural in the unbounded derived object.
> Applying degree-`n` homology gives the equality of groups in Stacks 0DDH.

```lean
public noncomputable def bigSmallEtaleCohomologyIso
    [HasSheafify (SmallEtale.topology B T.obj T.property) Ab.{u + 1}]
    [HasSheafify (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1}]
    [((bigEtaleSections B T S f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).HasRightDerivedFunctor
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))]
    [((smallEtaleRestriction B T S f).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasRightDerivedFunctor
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))]
    [((Sheaf.Γ (SmallEtale.topology B T.obj T.property) Ab.{u + 1}).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasRightDerivedFunctor
        (HomotopyCategory.quasiIso
          (Sheaf (SmallEtale.topology B T.obj T.property) Ab.{u + 1})
          (ComplexShape.up ℤ))] :
    (((bigEtaleSections B T S f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))) ≅
    ((((smallEtaleRestriction B T S f).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))) ⋙
    (((Sheaf.Γ (SmallEtale.topology B T.obj T.property) Ab.{u + 1}).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (SmallEtale.topology B T.obj T.property) Ab.{u + 1})
          (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.bigSmallEtaleModuleSectionsCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean#L215). The attribute's comment: “part (6)”.

> **Stacks 0DDH, part (6).** Let `f : T ⟶ S` be a morphism of a big étale site and let `M` be
> an unbounded complex of sheaves of `𝒪`-modules on the big étale site over `S`. Cohomology over
> the object `T ⟶ S` agrees with cohomology on the small étale site of `T` of `i_f^*M`, naturally
> in `M`:
> `H^n_étale(T, M) = H^n(T_étale, i_f^*M)`.
>
> Both sides are computed, as in the source, by the right derived functors of sections on the
> derived categories of modules. The proof is the comparison on underlying abelian complexes,
> `AlgebraicGeometry.bigSmallEtaleModuleCohomologyIso`, transported by Stacks 0D6J on both sites
> (`AlgebraicGeometry.derivedBigEtaleModuleSectionsIso` and
> `AlgebraicGeometry.derivedSmallEtaleModuleGlobalSectionsIso`).

```lean
public def bigSmallEtaleModuleSectionsCohomologyIso :
    derivedBigEtaleModuleSections B T S f ≅
      (smallEtaleModuleRestriction B T S f).mapDerivedCategory ⋙
        derivedSmallEtaleModuleGlobalSections B T
```

**`AlgebraicGeometry.bigSmallEtaleModuleProjectionPullbackSectionsCohomologyIsoSelf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean#L233). The attribute's comment: “part (2)”.

> **Stacks 0DDH, part (2).** Let `S` be an object of a big étale site and let `K` be an
> unbounded complex of sheaves of `𝒪_{S_étale}`-modules. Cohomology on the big étale site of `S`
> of the derived pullback `Lπ_S^*K` agrees with cohomology of `K` on the small étale site of `S`,
> naturally in `K`:
> `H^n_étale(S, Lπ_S^*K) = H^n(S_étale, K)`.
>
> Both sides are computed, as in the source, by the right derived functors of sections on the
> derived categories of modules. The proof is the comparison on underlying abelian complexes,
> `AlgebraicGeometry.bigSmallEtaleModuleProjectionPullbackCohomologyIsoSelf`, transported by
> Stacks 0D6J on both sites.

```lean
public def bigSmallEtaleModuleProjectionPullbackSectionsCohomologyIsoSelf :
    derivedSmallEtaleModuleProjectionPullback B S ⋙ derivedBigEtaleModuleSections B S S (𝟙 S) ≅
      derivedSmallEtaleModuleGlobalSections B S
```

**`AlgebraicGeometry.bigSmallEtaleModuleProjectionPullbackSectionsCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleSectionsCohomology.lean#L251). The attribute's comment: “part (4)”.

> **Stacks 0DDH, part (4).** Let `f : T ⟶ S` be a morphism of a big étale site and let `K` be
> an unbounded complex of sheaves of `𝒪_{S_étale}`-modules. Cohomology over the object `T ⟶ S` of
> the big étale site of `S` of the derived pullback `Lπ_S^*K` agrees with cohomology on the small
> étale site of `T` of the derived small étale pullback `Lf_small^*K`, naturally in `K`:
> `H^n_étale(T, Lπ_S^*K) = H^n(T_étale, Lf_small^*K)`.
>
> Both sides are computed, as in the source, by the right derived functors of sections on the
> derived categories of modules. The proof is the comparison on underlying abelian complexes,
> `AlgebraicGeometry.bigSmallEtaleModuleProjectionPullbackCohomologyIso`, transported by
> Stacks 0D6J on both sites.

```lean
public def bigSmallEtaleModuleProjectionPullbackSectionsCohomologyIso :
    derivedSmallEtaleModuleProjectionPullback B S ⋙ derivedBigEtaleModuleSections B T S f ≅
      derivedSmallEtaleModulePullback B T S f ⋙ derivedSmallEtaleModuleGlobalSections B T
```

**`AlgebraicGeometry.bigSmallEtaleProjectionPullbackCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean#L349). The attribute's comment: “part (3)”.

> **Stacks 0DDH, part (3).** Let `f : T ⟶ S` be a morphism of a big étale site and let `K` be
> an unbounded complex of abelian sheaves on the small étale site of `S`. Cohomology over the
> object `T ⟶ S` of the big étale site of `S` of the pullback `π_S^{-1}K` agrees with cohomology
> on the small étale site of `T` of `f_{small}^{-1}K`, naturally in `K`:
> `H^n_étale(T, π_S^{-1}K) = H^n(T_étale, f_{small}^{-1}K)`.
>
> Both `π_S^{-1}` and `f_{small}^{-1}` are exact, so no derived functor of them intervenes: the
> statement is between the two unbounded derived section functors precomposed with the functors the
> two pullbacks induce on derived categories.
>
> The proof is part (5), `AlgebraicGeometry.bigSmallEtaleCohomologyIso`, followed by
> `AlgebraicGeometry.smallEtaleRestrictionProjectionPullbackIso`: the derived functor of the exact
> `i_f^{-1}` is the functor it induces on derived categories, and composing that with `π_S^{-1}`'s
> gives the one induced by `f_{small}^{-1}`.

```lean
public def bigSmallEtaleProjectionPullbackCohomologyIso :
    (projectionPullback.{u, u + 1} B S.obj S.property).mapDerivedCategory ⋙
      (((bigEtaleSections B T S f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
            (ComplexShape.up ℤ))) ≅
    (smallEtaleAbelianInverseImage B T S f).mapDerivedCategory ⋙
      (((Sheaf.Γ (SmallEtale.topology B T.obj T.property) Ab.{u + 1}).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (SmallEtale.topology B T.obj T.property) Ab.{u + 1})
            (ComplexShape.up ℤ)))
```

**`AlgebraicGeometry.bigSmallEtaleProjectionPullbackCohomologyIsoSelf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean#L400). The attribute's comment: “part (1)”.

> **Stacks 0DDH, part (1).** For an unbounded complex `K` of abelian sheaves on the small étale
> site of `S`, cohomology of the pullback `π_S^{-1}K` on the big étale site of `S` agrees with
> cohomology of `K` on the small étale site of `S`, naturally in `K`:
> `H^n_étale(S, π_S^{-1}K) = H^n(S_étale, K)`.
>
> This is part (3) at the identity morphism of `S`, where `f_{small}^{-1}` is the identity functor
> by `AlgebraicGeometry.smallEtaleSheafPullbackIdIso` (Stacks 021J).

```lean
public def bigSmallEtaleProjectionPullbackCohomologyIsoSelf :
    (projectionPullback.{u, u + 1} B S.obj S.property).mapDerivedCategory ⋙
      (((bigEtaleSections B S S (𝟙 S)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
            (ComplexShape.up ℤ))) ≅
    (((Sheaf.Γ (SmallEtale.topology B S.obj S.property) Ab.{u + 1}).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (SmallEtale.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ)))
```

**`AlgebraicGeometry.bigSmallEtaleDerivedSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProjectionPullback.lean#L435). The attribute's comment: “part (5)”.

> **Stacks 0DDH, part (5).** Let `f : T ⟶ S` be a morphism of a big étale site and let `M` be
> an unbounded complex of abelian sheaves on the big étale site over `S`. Cohomology over the
> object `T ⟶ S` of the big étale site of `S` agrees with cohomology on the small étale site of
> `T` of the restriction `i_f^{-1}M`, naturally in `M`:
> `H^n_étale(T, M) = H^n(T_étale, i_f^{-1}M)`.
>
> This is `AlgebraicGeometry.bigSmallEtaleCohomologyIso` with nothing assumed: the three derived
> functors in the statement exist, the derived functor of the exact `i_f^{-1}` by
> `AlgebraicGeometry.hasRightDerivedFunctor_smallEtaleRestriction`, and the derived sections
> functors `RΓ(T → S, -)` and `RΓ(T_étale, -)` by
> `AlgebraicGeometry.hasRightDerivedFunctor_bigEtaleSections` and
> `AlgebraicGeometry.hasRightDerivedFunctor_smallEtaleGlobalSections`, from the K-injective
> resolutions of the two Grothendieck abelian categories of sheaves.

```lean
public def bigSmallEtaleDerivedSectionsIso :
    (((bigEtaleSections B T S f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))) ≅
    ((((smallEtaleRestriction B T S f).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (BigEtaleOver.topology B S.obj S.property) Ab.{u + 1})
          (ComplexShape.up ℤ))) ⋙
    (((Sheaf.Γ (SmallEtale.topology B T.obj T.property) Ab.{u + 1}).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (SmallEtale.topology B T.obj T.property) Ab.{u + 1})
          (ComplexShape.up ℤ))))
```

## Tag 0DDI, a lemma

[Tag 0DDI](https://stacks.math.columbia.edu/tag/0DDI) in the Stacks Project.

**`AlgebraicGeometry.projectionPullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean#L155). The attribute's comment: “exactness of inverse image”.

> Extension from the small to the big étale site is exact.

```lean
theorem projectionPullback_exact :
    exactFunctor _ _ (projectionPullback.{u, v} B S hS)
```

**`AlgebraicGeometry.projectionInverseImage_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean#L203). The attribute's comment: “exactness of inverse image, stated with no adjunction assumed”.

> The inverse image with no adjunction assumed, `AlgebraicGeometry.projectionInverseImage`, is
> exact.

```lean
theorem projectionInverseImage_exact :
    exactFunctor _ _ (projectionInverseImage.{u, v} B S hS)
```

**`AlgebraicGeometry.projectionRestriction_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean#L209). The attribute's comment: “exactness of direct image”.

> Restriction from the big to the small étale site is exact.

```lean
theorem projectionRestriction_exact :
    exactFunctor _ _ (projectionRestriction.{u, v} B S hS)
```

**`AlgebraicGeometry.projectionDerivedUnit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean#L257). The attribute's comment: “derived unit is an isomorphism”.

> The derived unit of the projection adjunction is an isomorphism:
> cohomology on the small étale site agrees with cohomology on the big one.

```lean
theorem projectionDerivedUnit_isIso :
    IsIso (projectionDerivedUnit.{u, v} B S hS)
```

**`AlgebraicGeometry.projectionInverseImageDerivedUnit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/CohomologicalDescent.lean#L319). The attribute's comment: “derived unit is an isomorphism, stated with no adjunction assumed”.

> For every `K` in `D(S_étale)` the map `K ⟶ Rπ_{S,*} π_S⁻¹ K` is an isomorphism, with the
> inverse image `projectionInverseImage` taken with no adjunction assumed. Both functors are exact
> (`projectionInverseImage_exact`, `projectionRestriction_exact`), so their derived functors are the
> induced functors on derived categories.

```lean
theorem projectionInverseImageDerivedUnit_isIso :
    IsIso (projectionInverseImageDerivedUnit.{u, v} B S hS)
```

## Tag 0DDJ, a lemma

[Tag 0DDJ](https://stacks.math.columbia.edu/tag/0DDJ) in the Stacks Project.

**`AlgebraicGeometry.isIso_bigSmallEtaleBaseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean#L70). The attribute's comment: “(1)”.

> **Stacks 0DDJ (1).** Let `f : T ⟶ S` be a proper morphism of a big étale site. Then
> `π_S⁻¹ ∘ f_{small,*} = f_{big,*} ∘ π_T⁻¹` as functors from sheaves of sets on `T_étale` to sheaves
> of sets on `(Sch/S)_étale`: the canonical base change map
> `AlgebraicGeometry.bigSmallEtaleBaseChange` is an isomorphism.

```lean
public theorem isIso_bigSmallEtaleBaseChange_of_isProper [IsProper (B.inclusion.map f)] :
    IsIso (bigSmallEtaleBaseChange B (Type (u + 1)) f (bigEtaleProjectionAdjunction B T)
      (bigEtaleProjectionAdjunction B S))
```

**`AlgebraicGeometry.isIso_bigSmallEtaleDerivedBaseChange_app_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean#L105). The attribute's comment: “(2)”.

> **Stacks 0DDJ (2).** Let `f : T ⟶ S` be a proper morphism of a big étale site. Then
> `π_S⁻¹ Rf_{small,*} K = Rf_{big,*} π_T⁻¹ K` for every `K` in `D^+(T_étale)` whose cohomology
> sheaves are torsion: the canonical base change map
> `AlgebraicGeometry.bigSmallEtaleDerivedBaseChange` is invertible at `K`. Here `Rf_{small,*}` and
> `Rf_{big,*}` are any right derived functors of the direct images of abelian sheaves along `f`.

```lean
public theorem isIso_bigSmallEtaleDerivedBaseChange_app_of_isProper
    [IsProper (B.inclusion.map f)]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B T.obj T.property) AddCommGrpCat.{u + 1}))
    (n : ℤ) (hK : K.IsGE n)
    (hT : Stacks.Torsion.torsionCohomologyProperty.{u + 1}
      (SmallEtale.topology B T.obj T.property) K) :
    IsIso ((bigSmallEtaleDerivedBaseChange B f RfSmall RfBig αSmall αBig).app K)
```

**`AlgebraicGeometry.isIso_bigSmallEtaleDerivedBaseChange_app_toSheaf_of_isProper_zmod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean#L121). The attribute's comment: “(3)”.

> **Stacks 0DDJ (3).** Let `f : T ⟶ S` be a proper morphism of a big étale site and `n ≥ 1`.
> Then `π_S⁻¹ Rf_{small,*} K = Rf_{big,*} π_T⁻¹ K` for every `K` in `D(T_étale, ℤ/nℤ)`, the
> unbounded derived category of sheaves of modules over the constant sheaf of rings `ℤ/nℤ`: the
> canonical base change map `AlgebraicGeometry.bigSmallEtaleDerivedBaseChange` is invertible at
> the underlying abelian complex of `K`.

```lean
public theorem isIso_bigSmallEtaleDerivedBaseChange_app_toSheaf_of_isProper_zmod
    [IsProper (B.inclusion.map f)] {n : ℕ} (hn : 0 < n)
    (E : DerivedCategory (SheafOfModules.{u + 1} (zmodRingSheaf.{u + 1}
      (SmallEtale.topology B T.obj T.property) n))) :
    IsIso ((bigSmallEtaleDerivedBaseChange B f RfSmall RfBig αSmall αBig).app
      ((SheafOfModules.toSheaf _).mapDerivedCategory.obj E))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isIso_bigSmallEtaleDerivedBaseChange_of_isFinite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/DerivedProperDirectImage.lean#L191), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperDirectImageCommutation.lean#L77) (StacksFrontier): “(4)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.99, Tag 0757](https://stacks.math.columbia.edu/tag/0757)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
