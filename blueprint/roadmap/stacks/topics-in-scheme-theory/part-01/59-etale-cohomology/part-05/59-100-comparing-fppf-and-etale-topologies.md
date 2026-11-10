---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleInverseImage_isSheaf_fppf, AlgebraicGeometry.isIso_fppfToBigEtale_unit_app, AlgebraicGeometry.smallEtalePullbackSections_isSheaf, AlgebraicGeometry.smallEtalePullbackSectionsSheafIso, AlgebraicGeometry.bigEtaleOverTopology_le_fppfOverTopology, AlgebraicGeometry.fppfToBigEtaleMorphism, AlgebraicGeometry.fppfToBigEtale_pushforwardIso, AlgebraicGeometry.fppfToSmallEtaleMorphism
statement: formalized
proof: formalized
---

# 59.100 Comparing fppf and étale topologies

Section 59.100 of the Stacks Project, [Tag 0DDK](https://stacks.math.columbia.edu/tag/0DDK). 8 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DDL, a lemma

[Tag 0DDL](https://stacks.math.columbia.edu/tag/0DDL) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleInverseImage_isSheaf_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafConditionSmallEtale.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafConditionSmallEtale.lean#L110). The attribute's comment: “the fppf sheaf condition”.

> **Stacks 0DDL, the fppf sheaf condition.** For a sheaf of sets `F` on the small étale site
> of `S`, the presheaf underlying `π_S⁻¹F` — by the sections formula the rule
> `X ↦ Γ(X_ét, f_X⁻¹F)` — is a sheaf for the big fppf topology over `S`.
>
> By Stacks 09XN, `AlgebraicGeometry.bigEtaleToSmallEtale_inverseImage_isSheaf_fpqc`, it is a
> sheaf for the much finer fpqc topology of the chosen slice, and every chosen fppf covering
> family is an fpqc covering family.

```lean
public theorem smallEtaleInverseImage_isSheaf_fppf
    (F : Sheaf (SmallEtale.topology (associatedBigEtaleSite B) S.1 S.property)
      (Type (u + 1))) :
    Presheaf.IsSheaf (B.topology.over S)
      ((bigEtaleToSmallEtaleMorphism (associatedBigEtaleSite B) S.1 S.property).inverseImage.obj
        F).obj
```

**`AlgebraicGeometry.isIso_fppfToBigEtale_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafConditionSmallEtale.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafConditionSmallEtale.lean#L126). The attribute's comment: “the canonical fppf comparison”.

> **Stacks 0DDL, the canonical fppf comparison.** At `π_S⁻¹F` the unit of `ε_S⁻¹ ⊣ ε_{S,*}`
> is an isomorphism. Since `ε_{S,*}` is restriction along the identity functor, this identifies
> the fppf sheaf `ε_S⁻¹π_S⁻¹F` with the rule `X ↦ Γ(X_ét, f_X⁻¹F)`.
>
> By `AlgebraicGeometry.isIso_fppfToBigEtale_unit_app_iff` the assertion is exactly the fppf
> sheaf condition `AlgebraicGeometry.smallEtaleInverseImage_isSheaf_fppf`.

```lean
public theorem isIso_fppfToBigEtale_unit_app
    (F : Sheaf (SmallEtale.topology (associatedBigEtaleSite B) S.1 S.property)
      (Type (u + 1))) :
    IsIso ((fppfToBigEtaleMorphism B S).adj.unit.app
      ((bigEtaleToSmallEtaleMorphism (associatedBigEtaleSite B) S.1
        S.property).inverseImage.obj F))
```

**`AlgebraicGeometry.smallEtalePullbackSections_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafOfSmallEtaleSections.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafOfSmallEtaleSections.lean#L117). The attribute's comment: “the rule X ↦ Γ(X, f\_small⁻¹F) is an fppf sheaf, a fortiori an étale sheaf”.

> **Stacks 0DDL, the sheaf condition.** The rule `(f : X ⟶ S) ↦ Γ(X, f_small⁻¹F)` is a sheaf
> for the big fppf topology over `S`, and a fortiori for the big étale topology over `S`.

```lean
public theorem smallEtalePullbackSections_isSheaf :
    Presheaf.IsSheaf (B.topology.over S) (smallEtalePullbackSectionsPresheaf B S F) ∧
      Presheaf.IsSheaf (BigEtaleOver.topology (associatedBigEtaleSite B) S.1 S.property)
        (smallEtalePullbackSectionsPresheaf B S F)
```

**`AlgebraicGeometry.smallEtalePullbackSectionsSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafOfSmallEtaleSections.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfSheafOfSmallEtaleSections.lean#L140). The attribute's comment: “the rule is π\_S⁻¹F on (Sch/S)\_étale and ε\_S⁻¹π\_S⁻¹F on (Sch/S)\_fppf”.

> **Stacks 0DDL, the identification.** The sheaf `X ↦ Γ(X, f_small⁻¹F)` is `π_S⁻¹F` on the
> big étale site over `S` and `ε_S⁻¹π_S⁻¹F` on the big fppf site over `S`.

```lean
public def smallEtalePullbackSectionsSheafIso :
    (smallEtalePullbackSectionsEtaleSheaf B S F ≅
        (bigEtaleToSmallEtaleMorphism (associatedBigEtaleSite B) S.1 S.property).inverseImage.obj
          F) ×
      (smallEtalePullbackSectionsFppfSheaf B S F ≅
        (fppfToBigEtaleMorphism B S).inverseImage.obj
          ((bigEtaleToSmallEtaleMorphism (associatedBigEtaleSite B) S.1
            S.property).inverseImage.obj F))
```

## Tag 0DDM, a lemma

[Tag 0DDM](https://stacks.math.columbia.edu/tag/0DDM) in the Stacks Project.

**`AlgebraicGeometry.bigEtaleOverTopology_le_fppfOverTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L124). The attribute's comment: “étale coverings are fppf on the slice”.

> The big-site comparison from fppf to étale is induced by the identity
> functor on the common slice category.

```lean
public theorem bigEtaleOverTopology_le_fppfOverTopology
    (B : BigFppfSite.{u}) (X : B.Schemes) :
      BigEtaleOver.topology (associatedBigEtaleSite B) X.1 X.2 ≤
      B.topology.over X
```

**`AlgebraicGeometry.fppfToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L166). The attribute's comment: “change-of-topology morphism”.

> The morphism of topoi from fppf sheaves to big étale sheaves on the slice over `X`: its
> pushforward and inverse image are those of the identity functor of the slice category, continuous
> because every étale covering is an fppf covering.

```lean
public def fppfToBigEtaleMorphism
    (B : BigFppfSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (BigEtaleOver.topology (associatedBigEtaleSite B)
        X.1 X.2) (Type (u + 1)))
```

**`AlgebraicGeometry.fppfToBigEtale_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L194). The attribute's comment: “direct image of change of topology”.

> The direct image of the change-of-topology morphism is restriction of
> fppf sheaves along the identity functor on the common slice category.

```lean
public def fppfToBigEtale_pushforwardIso
    (B : BigFppfSite.{u}) (X : B.Schemes) :
    (fppfToBigEtaleMorphism B X).pushforward ≅
      (𝟭 (Over X)).sheafPushforwardContinuous (Type (u + 1))
        (BigEtaleOver.topology (associatedBigEtaleSite B) X.1 X.2)
        (B.topology.over X)
```

**`AlgebraicGeometry.fppfToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L205). The attribute's comment: “factorization through the big étale topos”.

> The comparison from the big fppf topos to the small étale topos.

```lean
public def fppfToSmallEtaleMorphism
    (B : BigFppfSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (SmallEtale.topology (associatedBigEtaleSite B)
        X.1 X.2) (Type (u + 1)))
```

**`AlgebraicGeometry.bigFppfBigEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L237). The attribute's comment: “the big fppf–big étale square”.

> The square of big fppf and big étale topoi commutes.

```lean
public def bigFppfBigEtale_pushforwardCommIso
    (B : BigFppfSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((bigEtaleMorphism (associatedBigEtaleSite B) X Y f).comp
      (fppfToBigEtaleMorphism B X)).pushforward ≅
      ((fppfToBigEtaleMorphism B Y).comp
        (bigFppfMorphism B X Y f)).pushforward
```

**`AlgebraicGeometry.bigFppfSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/FppfToEtaleSquares.lean#L291). The attribute's comment: “the big fppf–small étale square”.

> The square of big fppf and small étale topoi commutes.

```lean
public def bigFppfSmallEtale_pushforwardCommIso
    (B : BigFppfSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((smallEtaleMorphism B f).comp
        (fppfToSmallEtaleMorphism B X)).pushforward ≅
      ((fppfToSmallEtaleMorphism B Y).comp
        (bigFppfMorphism B X Y f)).pushforward
```

## Tag 0DDN, a lemma

[Tag 0DDN](https://stacks.math.columbia.edu/tag/0DDN) in the Stacks Project.

**`AlgebraicGeometry.isIso_bigFppfSmallEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperFppfDirectImage.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperFppfDirectImage.lean#L79).

> **Stacks 0DDN.** Let `f : X ⟶ Y` be a proper morphism of the big fppf site. Then the base
> change map `a_Y⁻¹ ∘ f_{small,*} ⟶ f_{big,fppf,*} ∘ a_X⁻¹` is an isomorphism.

```lean
public theorem isIso_bigFppfSmallEtaleBaseChange [IsProper (B.inclusion.map f)] :
    IsIso (bigFppfSmallEtaleBaseChange B f)
```

## Tag 0DEU, a lemma

[Tag 0DEU](https://stacks.math.columbia.edu/tag/0DEU) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isEquivalence_fppfSmallEtaleTripleFunctor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/FppfDescent.lean#L464), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/FppfDescentUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/FppfDescentUnconditional.lean#L60) (StacksFrontier).

## Tag 0F0H, a lemma

[Tag 0F0H](https://stacks.math.columbia.edu/tag/0F0H) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.fppfEtaleWeakSerre_isWeakSerreClass`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/Situation.lean#L223), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean#L31) (StacksFrontier): “`𝒜'_X` is a weak Serre subcategory”.
- [`AlgebraicGeometry.fppfEtaleFinite_baseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/Situation.lean#L233), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean#L34) (StacksFrontier): “property (0EZ4) of Situation 0EZ3”.
- [`AlgebraicGeometry.fppfEtaleWeakSerre_overMapPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/Situation.lean#L264), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean#L36) (StacksFrontier): “property (0EZ5) of Situation 0EZ3”.
- [`AlgebraicGeometry.fppfEtaleWeakSerre_isSheaf_fppf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/Situation.lean#L321), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean#L39) (StacksFrontier): “property (0EZ6) of Situation 0EZ3”.
- [`AlgebraicGeometry.fppfCovering_refinement_etale_finite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/Situation.lean#L333), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/SituationTags.lean#L42) (StacksFrontier): “property (0EZ8) of Situation 0EZ3”.

## Tag 0DDS, a lemma

[Tag 0DDS](https://stacks.math.columbia.edu/tag/0DDS) in the Stacks Project.

**`AlgebraicGeometry.isIso_fppfSmallEtaleDerivedDirectImageBaseChange_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean#L316). The attribute's comment: “(4)”.

> For a finite morphism `f : X ⟶ Y` of the big fppf site and `K` in `D⁺(X_étale)`,
>
> `a_Y⁻¹(Rf_{small,*}K) = Rf_{big,fppf,*}(a_X⁻¹K)`:
>
> the base change map `AlgebraicGeometry.fppfSmallEtaleDerivedDirectImageBaseChange` is an
> isomorphism.

```lean
theorem isIso_fppfSmallEtaleDerivedDirectImageBaseChange_of_isFinite {X Y : B.Schemes}
    (f : X ⟶ Y) [IsFinite (B.inclusion.map f)]
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) Ab.{u + 1})) :
    IsIso (fppfSmallEtaleDerivedDirectImageBaseChange f K)
```

**`AlgebraicGeometry.isIso_fppfSmallEtaleDerivedDirectImageBaseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean#L335). The attribute's comment: “(5)”.

> **Stacks 0DDS (5).** For a proper morphism `f : X ⟶ Y` of the big fppf site and `K` in
> `D⁺(X_étale)` with torsion cohomology sheaves,
>
> `a_Y⁻¹(Rf_{small,*}K) = Rf_{big,fppf,*}(a_X⁻¹K)`:
>
> the base change map `AlgebraicGeometry.fppfSmallEtaleDerivedDirectImageBaseChange` is an
> isomorphism. Its first factor is invertible by Stacks 0DDJ (2), proper base change, and its
> second by Stacks 0EZF (2).

```lean
theorem isIso_fppfSmallEtaleDerivedDirectImageBaseChange_of_isProper {X Y : B.Schemes}
    (f : X ⟶ Y) [IsProper (B.inclusion.map f)]
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso (fppfSmallEtaleDerivedDirectImageBaseChange f K)
```

**`AlgebraicGeometry.isIso_fppfSmallEtaleHigherDirectImageBaseChange_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean#L406). The attribute's comment: “(2)”.

> **Stacks 0DDS (2).** For a finite morphism `f : X ⟶ Y` of the big fppf site, an abelian sheaf
> `F` on `X_étale` and every `i`,
>
> `a_Y⁻¹(R^if_{small,*}F) = R^if_{big,fppf,*}(a_X⁻¹F)`:
>
> the base change map `AlgebraicGeometry.fppfSmallEtaleHigherDirectImageBaseChange` is an
> isomorphism. It is the cohomology of the derived base change map of part (4) at `F` placed in
> degree zero, read through isomorphisms.

```lean
theorem isIso_fppfSmallEtaleHigherDirectImageBaseChange_of_isFinite {X Y : B.Schemes}
    (f : X ⟶ Y) [IsFinite (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) Ab.{u + 1}) (i : ℕ) :
    IsIso (fppfSmallEtaleHigherDirectImageBaseChange f F i)
```

**`AlgebraicGeometry.fppfSmallEtale_projectionPullback_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean#L426). The attribute's comment: “(1)”.

> **Stacks 0DDS (1).** For an object `X` of the big fppf site and an abelian sheaf `F` on
> `X_étale`,
>
> `ε_{X,*}a_X⁻¹F = π_X⁻¹F` and `R^iε_{X,*}(a_X⁻¹F) = 0` for `i > 0`:
>
> the unit `π_X⁻¹F ⟶ ε_{X,*}ε_X⁻¹π_X⁻¹F = ε_{X,*}a_X⁻¹F` of `ε_X⁻¹ ⊣ ε_{X,*}` is an isomorphism, and
> the higher right derived functors of `ε_{X,*}` vanish at `a_X⁻¹F`.

```lean
theorem fppfSmallEtale_projectionPullback_comparison (X : B.Schemes)
    (F : Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) Ab.{u + 1}) :
    IsIso ((fppfBigEtaleAbelianAdjunction B X).unit.app ((fppfEtaleProjectionPullback B X).obj F)) ∧
      ∀ i : ℕ, 0 < i → IsZero (((fppfBigEtaleAbelianPushforward B X).rightDerived i).obj
        ((fppfSmallEtaleAbelianPullback B X).obj F))
```

**`AlgebraicGeometry.isIso_fppfSmallEtaleDerivedUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/DirectImageBaseChange.lean#L438). The attribute's comment: “(3)”.

> **Stacks 0DDS (3).** For an object `X` of the big fppf site and `K` in `D⁺(X_étale)` the map
> `π_X⁻¹K ⟶ Rε_{X,*}(a_X⁻¹K)`, `AlgebraicGeometry.fppfSmallEtaleDerivedUnit`, is an isomorphism.
> It is Stacks 0EZF (1) at `π_X⁻¹K`, which lies in `D⁺_{𝒜'_X}`.

```lean
theorem isIso_fppfSmallEtaleDerivedUnit (X : B.Schemes) :
    IsIso (fppfSmallEtaleDerivedUnit B X)
```

## Tag 0DDT, a lemma

[Tag 0DDT](https://stacks.math.columbia.edu/tag/0DDT) in the Stacks Project.

**`AlgebraicGeometry.isIso_fppfSmallEtaleAdjunctionDerivedUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/CohomologicalDescentUnconditional.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/CohomologicalDescentUnconditional.lean#L62).

> **Stacks 0DDT.** Let `X` be a scheme, an object of a big fppf site `B`, and
> `a_X : Sh((Sch/X)_fppf) ⟶ Sh(X_étale)` the morphism of topoi to its small étale site. For `K` in
> `D⁺(X_étale)` the map `K ⟶ Ra_{X,*}a_X^{-1}K`, the component at `K` of the derived unit of
> `a_X^{-1} ⊣ a_{X,*}` (`AlgebraicGeometry.fppfSmallEtaleAdjunctionDerivedUnit`), is an
> isomorphism.

```lean
theorem isIso_fppfSmallEtaleAdjunctionDerivedUnit_app
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) AddCommGrpCat.{u + 1})) :
    IsIso ((fppfSmallEtaleAdjunctionDerivedUnit B X).app K)
```

## Tag 0DDU, a lemma

[Tag 0DDU](https://stacks.math.columbia.edu/tag/0DDU) in the Stacks Project.

**`AlgebraicGeometry.isIso_fppfSmallEtaleCohomologyPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/EtaleFppfCohomologyEquality.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/EtaleFppfCohomologyEquality.lean#L85).

> **Stacks 0DDU.** Let `X` be a scheme and `a_X : Sh((Sch/X)_fppf) ⟶ Sh(X_étale)`. Then, for
> every `q`:
>
> 1. `H^q(X_étale, F) = H^q_fppf(X, a_X^{-1}F)` for an abelian sheaf `F` on `X_étale`, with
>    `H^q = R^qΓ` (`CategoryTheory.Functor.rightDerivedPlus`, Stacks 015A): the canonical map
>    `AlgebraicGeometry.fppfSmallEtaleCohomologyPullback` is an isomorphism;
> 2. `H^q(X_étale, K) = H^q_fppf(X, a_X^{-1}K)` for `K` in `D⁺(X_étale)`: the canonical map
>    `AlgebraicGeometry.fppfSmallEtaleHypercohomologyPullback` is an isomorphism;
>
> and, the example, `H^q_étale(X, A) = H^q_fppf(X, A)` for an abelian group `A` and its constant
> sheaves: the canonical map `AlgebraicGeometry.fppfSmallEtaleConstantCohomologyPullback` is an
> isomorphism.

```lean
theorem isIso_fppfSmallEtaleCohomologyPullbacks :
    (∀ (q : ℤ)
      (F : Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) AddCommGrpCat.{u + 1}),
        IsIso (fppfSmallEtaleCohomologyPullback B X q F)) ∧
    (∀ (q : ℤ) (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (associatedBigEtaleSite B) X.1 X.2) AddCommGrpCat.{u + 1})),
        IsIso (fppfSmallEtaleHypercohomologyPullback B X q K)) ∧
    ∀ (q : ℤ) (A : AddCommGrpCat.{u + 1}),
      IsIso (fppfSmallEtaleConstantCohomologyPullback B X q A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.100, Tag 0DDK](https://stacks.math.columbia.edu/tag/0DDK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
