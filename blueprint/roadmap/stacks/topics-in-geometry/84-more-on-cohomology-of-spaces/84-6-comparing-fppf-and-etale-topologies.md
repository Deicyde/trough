---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtale_units_and_isZero_rightDerived, AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtale_derivedUnits, AlgebraicGeometry.BigFppfSpaceSite.isIso_etaleToFppfCohomology, AlgebraicGeometry.BigFppfSpaceSite.etaleCohomologyIso, AlgebraicGeometry.BigFppfSpaceSite.etaleCohomologyConstantIso, AlgebraicGeometry.BigFppfSpaceSite.canonicalSpaceEquivalence, AlgebraicGeometry.BigFppfSpaceSite.fppfToBigEtale_isContinuous, AlgebraicGeometry.BigFppfSpaceSite.fppfToBigEtaleMorphism
statement: formalized
proof: formalized
---

# 84.6 Comparing fppf and étale topologies

Section 84.6 of the Stacks Project, [Tag 0DGE](https://stacks.math.columbia.edu/tag/0DGE). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DGF, a lemma

[Tag 0DGF](https://stacks.math.columbia.edu/tag/0DGF) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtale_units_and_isZero_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L74).

> **Stacks 0DGF.** Let `X` be an algebraic space over `S`.
> (1) For a sheaf of sets `F` on `X_étale`, `ε_{X,*}a_X⁻¹F = π_X⁻¹F` and `a_{X,*}a_X⁻¹F = F`: the
> units `π_X⁻¹F ⟶ ε_{X,*}ε_X⁻¹π_X⁻¹F` and `F ⟶ a_{X,*}a_X⁻¹F` are isomorphisms.
> (2) For an abelian sheaf `F` on `X_étale`, `R^iε_{X,*}(a_X⁻¹F) = 0` for `i > 0`.

```lean
theorem isIso_fppfToSmallEtale_units_and_isZero_rightDerived (X : T.Spaces) :
    (IsIso (Functor.whiskerLeft (E.bigToSmallEtaleMorphism (etaleSpace T E h X)).inverseImage
        (fppfToBigEtaleMorphism T E h X).adj.unit) ∧
      IsIso (fppfToSmallEtaleMorphism T E h X).adj.unit) ∧
    ∀ (F : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace T E h X))
      AddCommGrpCat.{u + 1}) (i : ℕ), 0 < i →
      IsZero ((((Over.postEquiv (canonicalSpaceEquivalence T E h).1
        (X := X)).inverse.sheafPushforwardContinuous
        AddCommGrpCat.{u + 1} (E.bigEtaleTopology (etaleSpace T E h X))
        (BigFppfSpaceOver.topology T X)).rightDerived i).obj
          ((CategoryTheory.Sites.abelianInverseImage (fppfToSmallEtaleMorphism T E h X)).obj F))
```

## Tag 0DGG, a lemma

[Tag 0DGG](https://stacks.math.columbia.edu/tag/0DGG) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtale_derivedUnits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L101).

> **Stacks 0DGG.** For `K` in `D⁺(X_étale)` the maps `π_X⁻¹K ⟶ Rε_{X,*}a_X⁻¹K` and
> `K ⟶ Ra_{X,*}a_X⁻¹K` are isomorphisms: the units of the derived adjunctions `ε_X⁻¹ ⊣ Rε_{X,*}`
> at `π_X⁻¹K` and `a_X⁻¹ ⊣ Ra_{X,*}` at `K`.

```lean
theorem isIso_fppfToSmallEtale_derivedUnits
    (K : DerivedCategory.Plus (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem
      (etaleSpace T E h X)) AddCommGrpCat.{u + 1})) :
    IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
        (fppfToBigEtaleAbelianAdjunction T E h X)).unit.app
          ((CategoryTheory.Sites.abelianInverseImage
            (E.bigToSmallEtaleMorphism (etaleSpace T E h X))).mapDerivedCategoryPlus.obj K)) ∧
      IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
        (fppfToSmallEtaleAbelianAdjunction T E h X)).unit.app K)
```

## Tag 0DGH, a lemma

[Tag 0DGH](https://stacks.math.columbia.edu/tag/0DGH) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_etaleToFppfCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L125). The attribute's comment: “(2)”.

> **Stacks 0DGH, part (2).** For `K` in `D⁺(X_étale)`, `H^q(X_étale, K) = H^q_fppf(X, a_X⁻¹K)`
> for every `q`: the map induced on `H^q` by the canonical map
> `AlgebraicGeometry.BigFppfSpaceSite.etaleToFppfDerivedGlobalSections` is an isomorphism, naturally
> in `K`.

```lean
theorem isIso_etaleToFppfCohomology (q : ℤ) :
    IsIso (Functor.whiskerRight (etaleToFppfDerivedGlobalSections T E h X)
      (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q))
```

**`AlgebraicGeometry.BigFppfSpaceSite.etaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L166). The attribute's comment: “(1)”.

> **Stacks 0DGH, part (1).** For an abelian sheaf `F` on `X_étale`,
> `H^q(X_étale, F) = H^q_fppf(X, a_X⁻¹F)` for every `q`, by the canonical map
> `AlgebraicGeometry.BigFppfSpaceSite.etaleToFppfDerivedGlobalSections` at `F[0]`.

```lean
def etaleCohomologyIso (X : T.Spaces)
    (F : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace T E h X))
      AddCommGrpCat.{u + 1}) (q : ℕ) :
    ((etaleGlobalSections T E h X).rightDerived q).obj F ≅
      ((fppfGlobalSections T X).rightDerived q).obj
        ((CategoryTheory.Sites.abelianInverseImage (fppfToSmallEtaleMorphism T E h X)).obj F)
```

**`AlgebraicGeometry.BigFppfSpaceSite.etaleCohomologyConstantIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L177). The attribute's comment: “the example of an abelian group”.

> **The example of Stacks 0DGH.** For an abelian group `A`,
> `H^q_étale(X, A) = H^q_fppf(X, A)` for the constant sheaves.

```lean
def etaleCohomologyConstantIso (X : T.Spaces) (A : AddCommGrpCat.{u + 1}) (q : ℕ) :
    ((etaleGlobalSections T E h X).rightDerived q).obj
        ((constantSheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace T E h X))
          AddCommGrpCat.{u + 1}).obj A) ≅
      ((fppfGlobalSections T X).rightDerived q).obj
        ((constantSheaf (BigFppfSpaceOver.topology T X) AddCommGrpCat.{u + 1}).obj A)
```

## Tag 0DGI, a lemma

[Tag 0DGI](https://stacks.math.columbia.edu/tag/0DGI) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.canonicalSpaceEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L62). The attribute's comment: “identification of the underlying algebraic spaces”.

> The identification of the category of algebraic spaces a big fppf site of algebraic spaces is
> built on with the one a big étale site of algebraic spaces over the same big fppf site of schemes
> is built on, together with the facts that it is the identity on objects and on morphisms.

```lean
def canonicalSpaceEquivalence :
    { G : T.Spaces ≌ E.Spaces //
      (∀ X : T.Spaces, HEq X.1 (G.functor.obj X).1) ∧
      (∀ {X Y : T.Spaces} (f : X ⟶ Y), HEq f.hom (G.functor.map f).hom) }
```

**`AlgebraicGeometry.BigFppfSpaceSite.fppfToBigEtale_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L84). The attribute's comment: “continuity of the change-of-topology functor”.

> The identity-on-spaces functor from the big étale slice at `X` to the big fppf slice at `X`
> is continuous.

```lean
instance fppfToBigEtale_isContinuous (X : T.Spaces) :
    ((Over.postEquiv (canonicalSpaceEquivalence T E h).1 (X := X)).inverse).IsContinuous
      (E.bigEtaleTopology (etaleSpace T E h X)) (BigFppfSpaceOver.topology T X)
```

**`AlgebraicGeometry.BigFppfSpaceSite.fppfToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L134). The attribute's comment: “the fppf-to-big-étale morphism”.

> The change-of-topology morphism `ε_X` from the big fppf topos of `X` to its big étale topos,
> induced by the identity-on-spaces functor of slice categories.

```lean
def fppfToBigEtaleMorphism (X : T.Spaces) :
    MorphismOfTopoi (Sheaf (BigFppfSpaceOver.topology T X) (Type (u + 1)))
      (Sheaf (E.bigEtaleTopology (etaleSpace T E h X)) (Type (u + 1)))
```

**`AlgebraicGeometry.BigFppfSpaceSite.fppfToBigEtale_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L146). The attribute's comment: “direct image of the fppf-to-big-étale morphism”.

> The direct image of `ε_X` is restriction along the identity-on-spaces functor of slice
> categories.

```lean
def fppfToBigEtale_pushforwardIso (X : T.Spaces) :
    (fppfToBigEtaleMorphism T E h X).pushforward ≅
      ((Over.postEquiv (canonicalSpaceEquivalence T E h).1
        (X := X)).inverse).sheafPushforwardContinuous (Type (u + 1))
        (E.bigEtaleTopology (etaleSpace T E h X)) (BigFppfSpaceOver.topology T X)
```

**`AlgebraicGeometry.BigFppfSpaceSite.pullbackChangeOfTopologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L156). The attribute's comment: “canonical base-change comparison on the big sites”.

> Base change along `f` commutes with the identity-on-spaces change-of-topology functor of
> slice categories.

```lean
def pullbackChangeOfTopologyIso {X Y : T.Spaces} (f : Y ⟶ X) :
    Over.pullback (etaleMap T E h f) ⋙
        (Over.postEquiv (canonicalSpaceEquivalence T E h).1 (X := Y)).inverse ≅
      (Over.postEquiv (canonicalSpaceEquivalence T E h).1 (X := X)).inverse ⋙
        Over.pullback f
```

**`AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L173). The attribute's comment: “the factorization through big étale”.

> The morphism `a_X` from the big fppf topos of `X` to its small étale topos: the composite of
> `ε_X` with the big-to-small étale morphism `π_X` ([Stacks, Tag 0DF3]).

```lean
def fppfToSmallEtaleMorphism (X : T.Spaces) :
    MorphismOfTopoi (Sheaf (BigFppfSpaceOver.topology T X) (Type (u + 1)))
      (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace T E h X))
        (Type (u + 1)))
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfBigEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L182). The attribute's comment: “the big fppf–big étale square”.

> The big fppf–big étale square: for a morphism `f : Y ⟶ X` of algebraic spaces the direct
> images of `ε_X ∘ f_{big, fppf}` and of `f_{big, étale} ∘ ε_Y` are canonically isomorphic.

```lean
def bigFppfBigEtale_pushforwardCommIso {X Y : T.Spaces} (f : Y ⟶ X) :
    ((E.bigEtaleMorphism (etaleMap T E h f)).comp (fppfToBigEtaleMorphism T E h Y)).pushforward ≅
      ((fppfToBigEtaleMorphism T E h X).comp (bigFppfMorphism T f)).pushforward
```

**`AlgebraicGeometry.BigFppfSpaceSite.bigFppfSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtale.lean#L240). The attribute's comment: “the big fppf–small étale square”.

> The big fppf–small étale square: for a morphism `f : Y ⟶ X` of algebraic spaces the direct
> images of `a_X ∘ f_{big, fppf}` and of `f_{small} ∘ a_Y` are canonically isomorphic.

```lean
def bigFppfSmallEtale_pushforwardCommIso {X Y : T.Spaces} (f : Y ⟶ X) :
    ((E.smallEtaleMorphism (etaleMap T E h f)).comp
        (fppfToSmallEtaleMorphism T E h Y)).pushforward ≅
      ((fppfToSmallEtaleMorphism T E h X).comp (bigFppfMorphism T f)).pushforward
```

## Tag 0DGJ, a lemma

[Tag 0DGJ](https://stacks.math.columbia.edu/tag/0DGJ) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtalePushforwardIsosOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleAbelianProperPushforward.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleAbelianProperPushforward.lean#L121). The attribute's comment: “(1)”.

> Let `f : Y ⟶ X` be a proper morphism of algebraic spaces over `S`, and `a = π ∘ ε` the
> comparison morphisms from the big fppf topoi to the small étale topoi of Stacks 0DGI. Then
> `a_X⁻¹ ∘ f_{small,*} = f_{big,fppf,*} ∘ a_Y⁻¹`, as functors from sheaves of sets on the small étale
> site of `Y` to sheaves of sets on the big fppf site of `X`, and likewise for abelian sheaves. Both
> isomorphisms are the canonical base change maps, the mates of the commutative square of Stacks
> 0DGI: `AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtaleBaseChange` and
> `AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtaleAbelianBaseChange`.

```lean
def fppfToSmallEtalePushforwardIsosOfIsProper
    (hf : Space.IsProper T.schemeSite S T.scheme_mem f.hom) :
    ((E.smallEtaleMorphism (etaleMap T E h f)).pushforward ⋙
        (fppfToSmallEtaleMorphism T E h X).inverseImage ≅
      (fppfToSmallEtaleMorphism T E h Y).inverseImage ⋙ (bigFppfMorphism T f).pushforward) ×
    (E.smallEtalePushforward (etaleMap T E h f) ⋙
        CategoryTheory.Sites.abelianInverseImage (fppfToSmallEtaleMorphism T E h X) ≅
      CategoryTheory.Sites.abelianInverseImage (fppfToSmallEtaleMorphism T E h Y) ⋙
        fppfAbelianPushforward T f)
```

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtaleBaseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleProperPushforward.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleProperPushforward.lean#L278). The attribute's comment: “(1)”.

> **Proper base change for the big fppf topos.** For a proper morphism `f : Y ⟶ X` of algebraic
> spaces, the canonical base change map `a_X⁻¹ ∘ f_{small,*} ⟶ f_{big,fppf,*} ∘ a_Y⁻¹` of functors
> from sheaves on the small étale site of `Y` to sheaves on the big fppf site of `X` is an
> isomorphism.

```lean
theorem isIso_fppfToSmallEtaleBaseChange_of_isProper {X Y : T.Spaces} (f : Y ⟶ X)
    (hf : Space.IsProper T.schemeSite S T.scheme_mem f.hom) :
    IsIso (fppfToSmallEtaleBaseChange T E h f)
```

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtaleProperDerivedBaseChange_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L204). The attribute's comment: “(2)”.

> **Stacks 0DGJ, part (2).** For a proper morphism `f : Y ⟶ X` of algebraic spaces and `K` in
> `D⁺(Y_étale)` with torsion cohomology sheaves, `a_X⁻¹(Rf_{small,*}K) = Rf_{big,fppf,*}(a_Y⁻¹K)`:
> the comparison map `AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtaleProperDerivedBaseChange`
> is an isomorphism at `K`.

```lean
theorem isIso_fppfToSmallEtaleProperDerivedBaseChange_app
    (hf : Space.IsProper T.schemeSite S T.scheme_mem f.hom)
    (K : DerivedCategory.Plus (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem
      (etaleSpace T E h Y)) AddCommGrpCat.{u + 1}))
    (hK : BigEtaleSpaceSite.HasTorsionCohomology E (DerivedCategory.Plus.ι.obj K)) :
    IsIso ((fppfToSmallEtaleProperDerivedBaseChange T E h f).app K)
```

## Tag 0DGK, a lemma

[Tag 0DGK](https://stacks.math.columbia.edu/tag/0DGK) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_fppfToSmallEtaleDerivedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleUnconditional.lean#L149).

> **Stacks 0DGK.** For a finite morphism `f : Y ⟶ X` of algebraic spaces,
> `a_X⁻¹(Rf_{small,*}K) = Rf_{big,fppf,*}(a_Y⁻¹K)` for `K` in `D⁺(Y_étale)`: the base change map
> `AlgebraicGeometry.BigFppfSpaceSite.fppfToSmallEtaleDerivedBaseChange`, the mate of
> `Rf_{small,*} ∘ Ra_{Y,*} = Ra_{X,*} ∘ Rf_{big,fppf,*}`, is an isomorphism.

```lean
theorem isIso_fppfToSmallEtaleDerivedBaseChange
    (hf : Space.IsFinite T.schemeSite S T.scheme_mem f.hom) :
    IsIso (fppfToSmallEtaleDerivedBaseChange T E h f)
```

## Tag 0DGL, a lemma

[Tag 0DGL](https://stacks.math.columbia.edu/tag/0DGL) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isEquivalence_fppfSmallEtaleTripleFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSmallEtaleDescent.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfSmallEtaleDescent.lean#L340).

> **Fppf descent of small étale sheaves.** Let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is flat, locally of finite presentation and surjective. Then the functor
> `Sh(Y_étale) ⥤ {(G, H, α)}`, `F ↦ (f_small⁻¹F, a_Y⁻¹F, can)`, into the category of triples with
> `G ∈ Sh(X_étale)`, `H ∈ Sh((Spaces/Y)_fppf)` and `α : a_X⁻¹G ⟶ f_{big,fppf}⁻¹H` an isomorphism,
> is an equivalence of categories.
>
> The category of triples is the two-fibre product `a_X⁻¹ ⊡ f_{big,fppf}⁻¹`
> (`CategoryTheory.Limits.CategoricalPullback`), whose objects are exactly the triples, and the
> functor is `AlgebraicGeometry.BigFppfSpaceSite.fppfSmallEtaleTripleFunctor`, built from the
> canonical isomorphism `can = AlgebraicGeometry.BigFppfSpaceSite.fppfSmallEtaleInverseImageCommIso`.

```lean
theorem isEquivalence_fppfSmallEtaleTripleFunctor {X Y : T.Spaces} (f : X ⟶ Y)
    (hf : Space.IsFlat T.schemeSite S T.scheme_mem f.hom)
    (hlfp : Space.IsLocallyOfFinitePresentation T.schemeSite S T.scheme_mem f.hom)
    (hsurj : Space.IsSurjective T.schemeSite S T.scheme_mem f.hom) :
    (fppfSmallEtaleTripleFunctor T E h f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.6, Tag 0DGE](https://stacks.math.columbia.edu/tag/0DGE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
