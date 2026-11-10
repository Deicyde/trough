---
declaration: section
origin: cited
lean: AlgebraicGeometry.finiteLocallyConstantAbelianSheafEquivalence, AlgebraicGeometry.finiteTypeLocallyConstantModuleSheafEquivalence, AlgebraicGeometry.finiteLocallyConstantSetsEquivalence, AlgebraicGeometry.finiteTypeLocallyConstantEquivContinuousModule, AlgebraicGeometry.finiteTypeLocallyConstantEquivContinuousModuleUniv, AlgebraicGeometry.finiteSmallEtaleToFiniteLocallyConstantBaseChangeIso, AlgebraicGeometry.nonempty_finiteLocallyConstantSetsEquivalence_pullbackIso, AlgebraicGeometry.nonempty_finiteLocallyConstantAbelianSheafEquivalence_pullbackIso
statement: formalized
proof: formalized
---

# 59.65 Locally constant sheaves and the fundamental group

Section 59.65 of the Stacks Project, [Tag 0DV4](https://stacks.math.columbia.edu/tag/0DV4). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DV5, a lemma

[Tag 0DV5](https://stacks.math.columbia.edu/tag/0DV5) in the Stacks Project.

**`AlgebraicGeometry.finiteLocallyConstantAbelianSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Abelian.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Abelian.lean#L69). The attribute's comment: “(2) finite locally constant sheaves of abelian groups are the finite π₁(X, x)-modules”.

> **Stacks Project, Tag 0DV5, part (2).** For a connected scheme `X` with a geometric point
> `x`, the finite locally constant sheaves of abelian groups on `X_étale` are equivalent to the
> finite `π₁(X, x)`-modules, that is, to the finite abelian groups with a continuous action of the
> étale fundamental group.
>
> Part (1) of the tag is `AlgebraicGeometry.finiteLocallyConstantSetsEquivalence` and part (3) is
> `AlgebraicGeometry.finiteTypeLocallyConstantModuleSheafEquivalence`.

```lean
public noncomputable def finiteLocallyConstantAbelianSheafEquivalence :
    (isFiniteLocallyConstantAbelianSheaf.{u, u + 1, u + 1}
        (SmallEtale.topology B X.1 X.2)).FullSubcategory ≌
      (ContinuousGAddCommGrp.isFinite.{u + 1, u + 1}
        (EtaleFundamentalGroup X.1 x)).FullSubcategory
```

**`AlgebraicGeometry.finiteTypeLocallyConstantModuleSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Modules.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Modules.lean#L82). The attribute's comment: “(3) finite type locally constant sheaves of Λ-modules, for Λ a finite ring, are the finite π₁(X, x)-modules with commuting Λ-module structure”.

> For a connected scheme `X` with a geometric point `x` and a finite ring `Λ`, the finite type
> locally constant sheaves of `Λ`-modules on `X_étale` are equivalent to the finite `Λ`-modules
> endowed with a commuting continuous action of `π₁(X, x)`.

```lean
public def finiteTypeLocallyConstantModuleSheafEquivalence :
    ObjectProperty.FullSubcategory
        (fun F : Sheaf (SmallEtale.topology B X.1 X.2) (ModuleCat.{u + 1} Λ) ↦
          IsFiniteTypeLocallyConstant Λ (SmallEtale.topology B X.1 X.2) F) ≌
      FiniteTypeContinuousModule.{r, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1 x)
```

**`AlgebraicGeometry.finiteLocallyConstantSetsEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Sets.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FundamentalGroupLocallyConstant/Sets.lean#L82). The attribute's comment: “(1) finite locally constant sheaves of sets are the finite continuous π₁(X, x)-sets”.

> For a connected scheme `X` with a geometric point `x`, the equivalence between the finite
> locally constant sheaves of sets on the small étale site of `X` and the finite sets with a
> continuous action of the étale fundamental group `π₁(X, x)`. It is
> `finiteLocallyConstantFiniteEtaleEquivalence` followed by
> `finiteEtaleEquivalenceOfIsGaloisCategory` and the change of universe
> `contActionUniverseEquivalence`.

```lean
public noncomputable def finiteLocallyConstantSetsEquivalence :
    FiniteLocallyConstantSheaf B X ≌
      ContAction FintypeCat.{u + 1} (EtaleFundamentalGroup X.1 x)
```

## Tag 0GIY, a lemma

[Tag 0GIY](https://stacks.math.columbia.edu/tag/0GIY) in the Stacks Project.

**`AlgebraicGeometry.finiteTypeLocallyConstantEquivContinuousModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchContinuousModules.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchContinuousModules.lean#L368). The attribute's comment: “the equivalence, with the geometric input carried as hypotheses. Proved here: the source's reduction along the normalization — geometric unibranchness yields the universal homeomorphism of Tag 0GIQ, at which the hypothesis on the locally constant categories is instantiated; the fundamental group comparison is derived from the hypothesis that base change on finite étale covers along the normalization is an equivalence, which is the content of Tag 0BQN, by Tag 0BQA part (2); and the category of finite type continuous modules is transported along that comparison. Carried as hypotheses, none of them proved in this library: that base change on finite étale covers along a universal homeomorphism is an equivalence (Tag 0BQN, of which only faithfulness is available, the rest resting on Tag 0BTP), that a universal homeomorphism induces an equivalence of the finite type locally constant module categories (Tag 04DZ), the existence of a lift of the geometric point to the normalization, and the tag itself for the normalization, i.e. for an integral normal scheme (Tags 0BQM, 0BTD, 0BQI, 03RV, 0245, 03QW)”.

> **Stacks Project, Tag 0GIY.** Let `X` be an irreducible, geometrically unibranch scheme, let
> `x` be a geometric point of `X` and let `Λ` be a ring. The finite type locally constant sheaves of
> `Λ`-modules on `X_étale` are equivalent to the finite `Λ`-modules endowed with a continuous
> `π₁(X, x)`-action.
>
> The source proves this by reducing to the case of an integral normal scheme along the
> normalization `ν : X^ν → X`, which is a universal homeomorphism by Tag 0GIQ precisely because `X`
> is irreducible and geometrically unibranch. That reduction is what is carried out here: the
> geometric unibranchness is used to produce the universal homeomorphism, the equivalence of the
> finite type locally constant module categories of `X` and `X^ν` is instantiated at it, the
> isomorphism `π₁(X^ν, x^ν) ≅ π₁(X, x)` is obtained from the hypothesis that base change along `ν`
> is an equivalence of finite étale covers — the content of Tag 0BQN — through Tag 0BQA part (2),
> and the tag itself for the normalization is a hypothesis. See the module docstring for the gaps by
> tag number.

```lean
public def finiteTypeLocallyConstantEquivContinuousModule
    (B : BigEtaleSite.{u}) (X : B.Scheme) [IrreducibleSpace X.obj]
    (hX : IsGeometricallyUnibranch X.obj) (x : GeometricPoint X.obj)
    (Λ : Type r) [Ring Λ]
    [∀ V : SmallEtale B X.obj X.property,
      HasWeakSheafify ((SmallEtale.topology B X.obj X.property).over V) (ModuleCat.{w} Λ)]
    (hν : B.Contains (Scheme.normalizationSchemeOfIrreducible X.obj))
    [ConnectedSpace (Scheme.normalizationSchemeOfIrreducible X.obj)]
    [∀ V : SmallEtale B (Scheme.normalizationSchemeOfIrreducible X.obj) hν,
      HasWeakSheafify
        ((SmallEtale.topology B (Scheme.normalizationSchemeOfIrreducible X.obj) hν).over V)
        (ModuleCat.{w} Λ)]
    [(finiteEtaleBaseChange (Scheme.normalizationOfIrreducible X.obj)).IsEquivalence]
    (xν : GeometricPoint (Scheme.normalizationSchemeOfIrreducible X.obj))
    (hx : xν.map (Scheme.normalizationOfIrreducible X.obj) = x)
    (hinvariance : UniversalHomeomorphism (Scheme.normalizationOfIrreducible X.obj) →
      (FiniteTypeLocallyConstantModuleCategory Λ (SmallEtale.topology B X.obj X.property) ≌
        FiniteTypeLocallyConstantModuleCategory Λ
          (SmallEtale.topology B (Scheme.normalizationSchemeOfIrreducible X.obj) hν)))
    (hnormal : FiniteTypeLocallyConstantModuleCategory Λ
        (SmallEtale.topology B (Scheme.normalizationSchemeOfIrreducible X.obj) hν) ≌
      FiniteTypeContinuousModule Λ
        (EtaleFundamentalGroup (Scheme.normalizationSchemeOfIrreducible X.obj) xν)) :
    FiniteTypeLocallyConstantModuleCategory Λ (SmallEtale.topology B X.obj X.property) ≌
      FiniteTypeContinuousModule Λ (EtaleFundamentalGroup X.obj x)
```

**`AlgebraicGeometry.finiteTypeLocallyConstantEquivContinuousModuleUniv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchEquivalence.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchEquivalence.lean#L73).

> **Stacks Project, Tag 0GIY.** Let `X` be an irreducible, geometrically unibranch scheme, let
> `x` be a geometric point of `X` and let `Λ` be a ring. The finite type locally constant sheaves of
> `Λ`-modules on `X_étale` are equivalent to the finite `Λ`-modules endowed with a continuous
> `π₁(X, x)`-action.
>
> The functor sends a sheaf `F` to its monodromy module `colim_{(A, a)} F(A)` over the pointed
> Galois covers of `X`.

```lean
public def finiteTypeLocallyConstantEquivContinuousModuleUniv (X : Scheme.{u}) [IrreducibleSpace X]
    (hX : IsGeometricallyUnibranch X) (x : GeometricPoint X) (Λ : Type r) [Ring Λ] :
    Stacks.ConstantSheaf.FiniteTypeLocallyConstantModuleCategory.{max (u + 1) r, u + 1, u, r} Λ
        X.smallEtaleTopology ≌
      Stacks.GroupCohomology.FiniteTypeContinuousModule.{r, u + 1, max (u + 1) r} Λ
        (EtaleFundamentalGroup X x)
```

## Tag 0DV6, a remark

[Tag 0DV6](https://stacks.math.columbia.edu/tag/0DV6) in the Stacks Project.

**`AlgebraicGeometry.finiteSmallEtaleToFiniteLocallyConstantBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean#L199). The attribute's comment: “the sets case, first leg: the dictionary of Stacks 03RV between the finite objects of the small etale site and the finite locally constant sheaves of sets commutes with pullback. The second leg, Stacks 0BND (3), is proved separately as AlgebraicGeometry.exists_finiteEtaleEquivalence_mapIso; the two legs are not composed here, which would need the comparison of AlgebraicGeometry.finiteSmallEtaleBaseChange with AlgebraicGeometry.finiteEtaleBaseChange across AlgebraicGeometry.finiteEtaleSiteEquivalence”.

> **Stacks Project, Tag 0DV6, the first leg of the sets case.** The inverse image of the
> finite locally constant sheaf represented by a finite étale cover is the one represented by its
> base change: the square of `AlgebraicGeometry.finiteSmallEtaleToFiniteLocallyConstant` against
> base change on the site and inverse image on sheaves commutes.
>
> The equivalence of Tag 0DV5 (1) between the finite locally constant sheaves of sets on
> `X_étale` and the finite continuous `π₁(X, x)`-sets is the composite of two legs, the dictionary
> of Tag 03RV with finite étale covers and the equivalence of Tag 0BND (1). This is the
> compatibility of the first leg with pullbacks.

```lean
public def finiteSmallEtaleToFiniteLocallyConstantBaseChangeIso :
    finiteSmallEtaleToFiniteLocallyConstant B X ⋙ finiteLocallyConstantSheafPullback B f ≅
      finiteSmallEtaleBaseChange B f ⋙ finiteSmallEtaleToFiniteLocallyConstant B Y
```

**`AlgebraicGeometry.nonempty_finiteLocallyConstantSetsEquivalence_pullbackIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean#L281). The attribute's comment: “for sheaves of sets: the equivalence of Stacks 0DV5 (1) commutes with pullback, the action being reindexed along the induced homomorphism of fundamental groups”.

> **Stacks Project, Tag 0DV6 for sheaves of sets.** Let `f : Y ⟶ X` be a morphism of connected
> schemes and let `y` be a geometric point of `Y`, with image `x = f(y)`. Then the square
>
> ```
>   finite locally constant sheaves of sets on X_étale  ──→  finite π₁(X, x)-sets
>                         │                                          │
>                      f^{-1}                                   restriction
>                         ↓                                          ↓
>   finite locally constant sheaves of sets on Y_étale  ──→  finite π₁(Y, y)-sets
> ```
>
> commutes, where the horizontal arrows are the equivalence of Stacks Tag 0DV5 (1) and the right
> vertical arrow reindexes the action along the homomorphism `π₁(Y, y) ⟶ π₁(X, x)` induced by
> `f`.
>
> The equivalence of Tag 0DV5 (1) is the composite of the dictionary of Tag 03RV with the finite
> étale covers, the equivalence of Tag 0BND (1) and a change of universe. The first factor
> commutes with pullback by
> `AlgebraicGeometry.finiteLocallyConstantFiniteEtaleEquivalenceBaseChangeIso`, the second by
> Tag 0BND (3), that is `AlgebraicGeometry.exists_finiteEtaleEquivalence_mapIso`, and the third
> on the nose. Only the existence of the comparison is asserted, because Tag 0BND (3) is
> available in that form.

```lean
public theorem nonempty_finiteLocallyConstantSetsEquivalence_pullbackIso
    [ConnectedSpace X.1] [ConnectedSpace Y.1] (y : GeometricPoint Y.1) :
    Nonempty ((finiteLocallyConstantSetsEquivalence B X (y.map f.hom)).functor ⋙
        ContAction.res FintypeCat.{u + 1} (etaleFundamentalGroupMap f.hom y) ≅
      finiteLocallyConstantSheafPullback B f ⋙
        (finiteLocallyConstantSetsEquivalence B Y y).functor)
```

**`AlgebraicGeometry.nonempty_finiteLocallyConstantAbelianSheafEquivalence_pullbackIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean#L392). The attribute's comment: “for sheaves of abelian groups: the equivalence of Stacks 0DV5 (2) commutes with pullback, the action being reindexed along the induced homomorphism of fundamental groups”.

> **Stacks Project, Tag 0DV6 for sheaves of abelian groups.** Let `f : Y ⟶ X` be a morphism of
> connected schemes and let `y` be a geometric point of `Y`, with image `x = f(y)`. Then the square
>
> ```
>   finite locally constant abelian sheaves on X_étale  ──→  finite π₁(X, x)-modules
>                         │                                          │
>                      f^{-1}                                   restriction
>                         ↓                                          ↓
>   finite locally constant abelian sheaves on Y_étale  ──→  finite π₁(Y, y)-modules
> ```
>
> commutes, where the horizontal arrows are the equivalence of Stacks Tag 0DV5 (2), the left
> vertical arrow is the inverse image of abelian sheaves
> (`AlgebraicGeometry.finiteLocallyConstantAbelianSheafPullback_comp_ι`) and the right vertical
> arrow reindexes the action along the homomorphism `π₁(Y, y) ⟶ π₁(X, x)` induced by `f`
> (`CategoryTheory.ContinuousGAddCommGrp.resIsFinite_comp_ι`).
>
> The equivalence of Tag 0DV5 (2) is the transport of commutative group objects along the
> equivalence of Tag 0DV5 (1), and the only factor of that transport which depends on the latter is
> `CategoryTheory.Functor.mapCommGrp` applied to it, so the sets case of Tag 0DV6 transports:
> `Stacks.ConstantSheaf.finiteLocallyConstantAbelianPullbackSquare`. Its two remaining inputs are
> the compatibility of each dictionary with the two vertical arrows, and for the sheaf side that is
> the identification of the inverse image of abelian sheaves with the inverse image of the
> underlying sheaves of sets together with the induced group operations,
> `Stacks.Sites.AbelianPullback.internalSheafPullbackSquare`. Only the existence of the comparison
> is asserted, because the sets case is available in that form.

```lean
public theorem nonempty_finiteLocallyConstantAbelianSheafEquivalence_pullbackIso
    [ConnectedSpace X.1] [ConnectedSpace Y.1] (y : GeometricPoint Y.1) :
    Nonempty ((finiteLocallyConstantAbelianSheafEquivalence B X (y.map f.hom)).functor ⋙
        ContinuousGAddCommGrp.resIsFinite (etaleFundamentalGroupMap f.hom y) ≅
      finiteLocallyConstantAbelianSheafPullback B f ⋙
        (finiteLocallyConstantAbelianSheafEquivalence B Y y).functor)
```

**`AlgebraicGeometry.nonempty_finiteTypeLocallyConstantModuleSheafEquivalence_pullbackIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeRepresentable.lean#L551). The attribute's comment: “for sheaves of modules over a finite ring: the equivalence of Stacks 0DV5 (3) commutes with pullback, the action being reindexed along the induced homomorphism of fundamental groups”.

> **Stacks Project, Tag 0DV6 for sheaves of modules.** Let `Λ` be a finite ring, let
> `f : Y ⟶ X` be a morphism of connected schemes and let `y` be a geometric point of `Y`, with
> image `x = f(y)`. Then the square
>
> ```
>   finite type locally constant Λ-module sheaves on X_étale  ──→  finite Λ-π₁(X, x)-modules
>                         │                                                 │
>                      f^{-1}                                          restriction
>                         ↓                                                 ↓
>   finite type locally constant Λ-module sheaves on Y_étale  ──→  finite Λ-π₁(Y, y)-modules
> ```
>
> commutes, where the horizontal arrows are the equivalence of Stacks Tag 0DV5 (3), the left
> vertical arrow is the inverse image of sheaves of `Λ`-modules
> (`AlgebraicGeometry.finiteTypeLocallyConstantModuleSheafPullback_comp_ι`) and the right vertical
> arrow reindexes the action along the homomorphism `π₁(Y, y) ⟶ π₁(X, x)` induced by `f`
> (`Stacks.GroupCohomology.finiteTypeContinuousModuleRes_comp_ι` together with
> `Stacks.GroupCohomology.continuousModuleRes_comp_ι`).
>
> The equivalence of Tag 0DV5 (3) is the equivalence of Tag 0DV5 (2) read on additive functors out
> of the one-object category of `Λ`, and the only factor of that reading which depends on the
> latter is postcomposition with it, so the abelian case of Tag 0DV6 transports:
> `CategoryTheory.scalarActionTransportSquare`. Only the existence of the comparison is asserted,
> because the abelian case is available in that form.

```lean
public theorem nonempty_finiteTypeLocallyConstantModuleSheafEquivalence_pullbackIso
    (y : GeometricPoint Y.1) :
    Nonempty ((finiteTypeLocallyConstantModuleSheafEquivalence B X (y.map f.hom) Λ).functor ⋙
        finiteTypeContinuousModuleRes Λ (etaleFundamentalGroupMap f.hom y) ≅
      finiteTypeLocallyConstantModuleSheafPullback B f Λ ⋙
        (finiteTypeLocallyConstantModuleSheafEquivalence B Y y Λ).functor)
```

**`AlgebraicGeometry.finiteTypeLocallyConstantEquivContinuousModuleUnivPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeUnibranch.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/BaseChangeUnibranch.lean#L542). The attribute's comment: “the square for the equivalence of Stacks 0GIY; the squares for the equivalences of Stacks 0DV5 are in BaseChangeRepresentable and BaseChangeEtaleSite”.

> **Stacks Project, Tag 0DV6, for the equivalence of Tag 0GIY.** Let `f : Y ⟶ X` be a morphism
> of irreducible, geometrically unibranch schemes, let `y` be a geometric point of `Y` and let `Λ`
> be a ring. The equivalences of Tag 0GIY for `X` at `f(y)` and for `Y` at `y` are compatible with
> pullback: the square
>
> ```
>   finite type loc. const. Λ-module sheaves on X_étale  ──→  finite Λ-π₁(X, f(y))-modules
>                       │                                               │
>                    f^{-1}                                        restriction
>                       ↓                                               ↓
>   finite type loc. const. Λ-module sheaves on Y_étale  ──→  finite Λ-π₁(Y, y)-modules
> ```
>
> commutes up to the natural isomorphism given here, the right-hand vertical arrow restricting the
> action along the homomorphism `π₁(Y, y) ⟶ π₁(X, f(y))` of Tag 0BND (3).
>
> The comparison sends the image of a section `s` over a pointed Galois cover `A` of `X` to the
> image of the restriction of `f^{-1}s` to a pointed Galois cover of `Y` dominating `A ×_X Y`; it is
> bijective because `f^{-1}` carries a trivialization of `F` over `A` to one of `f^{-1}F` over
> `A ×_X Y`, compatibly with the sections.

```lean
public def finiteTypeLocallyConstantEquivContinuousModuleUnivPullbackIso :
    (finiteTypeLocallyConstantEquivContinuousModuleUniv X hX (y.map f) Λ).functor ⋙
        finiteTypeContinuousModuleRes Λ (etaleFundamentalGroupMap f y) ≅
      etaleFiniteTypeLocallyConstantModulePullback f Λ ⋙
        (finiteTypeLocallyConstantEquivContinuousModuleUniv Y hY y Λ).functor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.65, Tag 0DV4](https://stacks.math.columbia.edu/tag/0DV4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
