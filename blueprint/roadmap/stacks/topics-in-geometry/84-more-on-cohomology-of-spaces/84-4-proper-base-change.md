---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.unit_comp_smallToposDescentMap, AlgebraicGeometry.Space.unit_equalizes, AlgebraicGeometry.Space.nonempty_isLimit_unitFork_of_isProper_isSurjective, AlgebraicGeometry.Space.isIso_globalSectionsRestriction_closedFibre_of_henselianPair, AlgebraicGeometry.Space.isIso_globalSectionsRestriction_closedFibre_of_henselianLocalRing, AlgebraicGeometry.Space.isIso_properBaseChangeMap_of_isProper, AlgebraicGeometry.Space.bijective_geometricFibreSectionsMap_of_isProper, AlgebraicGeometry.BigEtaleSpaceSite.isIso_spacesEtaleDerivedBaseChange_app_singleFunctor_of_isProper
statement: formalized
proof: formalized
---

# 84.4 Proper base change

Section 84.4 of the Stacks Project, [Tag 0DFW](https://stacks.math.columbia.edu/tag/0DFW). 9 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DFX, a lemma

[Tag 0DFX](https://stacks.math.columbia.edu/tag/0DFX) in the Stacks Project.

**`AlgebraicGeometry.Space.unit_comp_smallToposDescentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleDescentFork.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleDescentFork.lean#L92). The attribute's comment: “the unit equalizes the two restrictions”.

> **Stacks 0DFX.** The unit of `f` followed by the restriction along `p` is the unit of
> `p ≫ f`.
>
> Applied to the two projections `p₁, p₂ : Y ×_X Y ⟶ Y` of a self-intersection, where
> `p₁ ≫ f = p₂ ≫ f`, this says that the unit equalizes the two restrictions to `Y ×_X Y`.

```lean
theorem unit_comp_smallToposDescentMap {P Y X : AlgebraicSpaces B S hS}
    (p : P ⟶ Y) (f : Y ⟶ X)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1))) :
    (smallToposMorphism B S hS f).adj.unit.app F ≫ smallToposDescentMap B S hS p f F =
      (smallToposMorphism B S hS (p ≫ f)).adj.unit.app F
```

**`AlgebraicGeometry.Space.unit_equalizes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleDescentUnit.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleDescentUnit.lean#L135). The attribute's comment: “the unit equalizes the two restrictions”.

> **Stacks 0DFX.** The fork of Stacks 0DFX commutes: the adjunction unit
> `F ⟶ f_* f⁻¹ F` has equal composites with the two restriction maps `f_* f⁻¹ F ⟶ g_* g⁻¹ F`
> coming from the two projections of `Y ×_X Y`, where `g` is its structure morphism to `X`.
> Neither surjectivity nor properness of `f` is needed for this.

```lean
theorem unit_equalizes {Y X : AlgebraicSpaces B S hS} (f : Y ⟶ X)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type (u + 1))) :
    let P := AlgebraicSpaces.fiberProduct B S hS f f
    let p₁ : P ⟶ Y := ObjectProperty.homMk (pullback.fst f.hom f.hom)
    let p₂ : P ⟶ Y := ObjectProperty.homMk (pullback.snd f.hom f.hom)
    let g : P ⟶ X := p₁ ≫ f
    (smallToposMorphism B S hS f).adj.unit.app F ≫
        descentMapOver B S hS p₁ f g rfl F =
      (smallToposMorphism B S hS f).adj.unit.app F ≫
        descentMapOver B S hS p₂ f g
          (AlgebraicSpaces.isPullback_fiberProduct B S hS f f).w.symm F
```

**`AlgebraicGeometry.Space.nonempty_isLimit_unitFork_of_isProper_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperSurjectiveEqualizer.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperSurjectiveEqualizer.lean#L70).

> **Stacks 0DFX.** Let `f : Y ⟶ X` be a surjective proper morphism of algebraic spaces over
> `S`, let `F` be a sheaf on `X_étale` (the spaces-étale site of `X`, Stacks 03G1), and let
> `g : Y ×_X Y ⟶ X` be the structure morphism. Then `F ⟶ f_* f⁻¹ F` is injective with image the
> equalizer of the two maps `f_* f⁻¹ F ⇉ g_* g⁻¹ F` induced by the two projections
> `Y ×_X Y ⟶ Y`: the fork formed by the unit of `f⁻¹ ⊣ f_*` and these two maps is a limit.

```lean
theorem nonempty_isLimit_unitFork_of_isProper_isSurjective {X Y : AlgebraicSpaces B S hS}
    (f : Y ⟶ X) (hs : IsSurjective B S hS f.hom) (hp : IsProper B S hS f.hom)
    (F : Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1))) :
    Nonempty (IsLimit (Fork.ofι ((spacesEtalePseudofunctorAdjunction B S hS f).unit.app F)
      ((Pseudofunctor.unit_comp_unitForkRestriction _ f (spacesChosenPullback B S hS f f)
          (spacesEtalePseudofunctorAdjunction B S hS f)
          (spacesEtalePseudofunctorAdjunction B S hS (spacesChosenPullback B S hS f f).p)
          (spacesChosenPullback B S hS f f).p₁ (spacesChosenPullback B S hS f f).hp₁ F).trans
        (Pseudofunctor.unit_comp_unitForkRestriction _ f (spacesChosenPullback B S hS f f)
          (spacesEtalePseudofunctorAdjunction B S hS f)
          (spacesEtalePseudofunctorAdjunction B S hS (spacesChosenPullback B S hS f f).p)
          (spacesChosenPullback B S hS f f).p₂ (spacesChosenPullback B S hS f f).hp₂ F).symm) :
      Fork (Pseudofunctor.unitForkRestriction _ f (spacesChosenPullback B S hS f f)
          (spacesEtalePseudofunctorAdjunction B S hS f)
          (spacesEtalePseudofunctorAdjunction B S hS (spacesChosenPullback B S hS f f).p)
          (spacesChosenPullback B S hS f f).p₁ (spacesChosenPullback B S hS f f).hp₁ F)
        (Pseudofunctor.unitForkRestriction _ f (spacesChosenPullback B S hS f f)
          (spacesEtalePseudofunctorAdjunction B S hS f)
          (spacesEtalePseudofunctorAdjunction B S hS (spacesChosenPullback B S hS f f).p)
          (spacesChosenPullback B S hS f f).p₂ (spacesChosenPullback B S hS f f).hp₂ F)))
```

## Tag 0DFY, a lemma

[Tag 0DFY](https://stacks.math.columbia.edu/tag/0DFY) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_globalSectionsRestriction_closedFibre_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperHenselianPairSections.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperHenselianPairSections.lean#L162).

> **[Stacks, Tag 0DFY].** Let `(A, I)` be a henselian pair, let `X` be an algebraic space over
> `A` whose structure morphism `f : X ⟶ Spec A` is proper, and let `i : X₀ ⟶ X` be the inclusion of
> `X₀ = X ×_{Spec A} Spec (A ⧸ I)`. For every sheaf of sets `ℱ` on `X_étale`,
> `Γ(X, ℱ) = Γ(X₀, i⁻¹ ℱ)`: restriction of global sections along `i`, natural in `ℱ`, is an
> isomorphism.

```lean
theorem isIso_globalSectionsRestriction_closedFibre_of_henselianPair (hI : HenselianPair A I)
    (hf : IsProper B (Spec (.of A)) hA f.hom) :
    IsIso (globalSectionsRestriction B (Spec (.of A)) hA (closedFibreInclusion A I hA X f))
```

## Tag 0DFZ, a lemma

[Tag 0DFZ](https://stacks.math.columbia.edu/tag/0DFZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_globalSectionsRestriction_closedFibre_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperHenselianLocalSections.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperHenselianLocalSections.lean#L51). References: SGA 4 XII (5.5), “more general”.

> **[Stacks, Tag 0DFZ].** Let `A` be a henselian local ring, let `X` be an algebraic space over
> `A` whose structure morphism `f : X ⟶ Spec A` is proper, and let `i : X₀ ⟶ X` be the inclusion of
> the fibre `X₀ = X ×_{Spec A} Spec (A ⧸ 𝔪)` of `f` over the closed point (`A ⧸ 𝔪` is the residue
> field of `A`). For every sheaf of sets `ℱ` on `X_étale`, `Γ(X, ℱ) = Γ(X₀, ℱ|_{X₀})`: restriction of
> global sections along `i`, natural in `ℱ`, is an isomorphism.

```lean
theorem isIso_globalSectionsRestriction_closedFibre_of_henselianLocalRing
    (hf : IsProper B (Spec (.of A)) hA f.hom) :
    IsIso (globalSectionsRestriction B (Spec (.of A)) hA
      (closedFibreInclusion A (maximalIdeal A) hA X f))
```

## Tag 0DG0, a lemma

[Tag 0DG0](https://stacks.math.columbia.edu/tag/0DG0) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_properBaseChangeMap_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperBaseChangeSmallEtale.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperBaseChangeSmallEtale.lean#L244).

> Let `S` be a scheme, let `f : X ⟶ Y` and `g : Y' ⟶ Y` be morphisms of algebraic spaces over
> `S` with `f` proper, and let
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> be cartesian, that is `X' = Y' ×_Y X` with projections `f'` and `g'`. Then for every sheaf of
> sets `ℱ` on `X_étale` the canonical map `g⁻¹ f_* ℱ ⟶ f'_* (g')⁻¹ ℱ` is an isomorphism, naturally
> in `ℱ`: the base-change map `AlgebraicGeometry.Space.properBaseChangeMap` of the small étale
> topoi is invertible.

```lean
theorem isIso_properBaseChangeMap_of_isProper (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (g : Y' ⟶ Y) (f' : X' ⟶ Y') (g' : X' ⟶ X) (sq : IsPullback g' f' f g) :
    IsIso (properBaseChangeMap B S hS f g f' g' sq)
```

## Tag 0DG1, a lemma

[Tag 0DG1](https://stacks.math.columbia.edu/tag/0DG1) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_geometricFibreSectionsMap_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperGeometricFibreSections.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/ProperGeometricFibreSections.lean#L117).

> **[Stacks, Tag 0DG1].** Let `S` be a scheme, let `f : Y ⟶ X` be a proper morphism of
> algebraic spaces over `S` and let `x̄` be a geometric point of `X`, with geometric fibre
> `Y_x̄ = Y ×_{X, x̄} Spec(k)` and projection `p : Y_x̄ ⟶ Y`. For every sheaf of sets `ℱ` on
> `Y_étale` the canonical map `(f_* ℱ)_x̄ ⟶ Γ(Y_x̄, ℱ_x̄)`, `ℱ_x̄ = p⁻¹ ℱ`, is bijective.
>
> The proof is the source's: the base-change map of the geometric fibre square is invertible by
> proper base change, Stacks 0DG0
> (`AlgebraicGeometry.Space.isIso_properBaseChangeMap_of_isProper`).

```lean
theorem bijective_geometricFibreSectionsMap_of_isProper (f : Y ⟶ X)
    (hf : IsProper B S hS f.hom) (x : GeometricPoint B S hS X.obj)
    (ℱ : Sheaf (SmallEtale.topology B S hS Y.obj) (Type (u + 1))) :
    Function.Bijective ((geometricFibreSectionsMap B S hS f x).app ℱ)
```

## Tag 0DG2, a theorem

[Tag 0DG2](https://stacks.math.columbia.edu/tag/0DG2) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigEtaleSpaceSite.isIso_spacesEtaleDerivedBaseChange_app_singleFunctor_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleTorsionDerivedPushforwardUnconditional.lean#L78), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperBaseChange.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperBaseChange.lean#L15) (StacksFrontier): “proper base change for algebraic spaces: g⁻¹ R f\_* F ≅ R f'\_* (g')⁻¹ F for f proper and F an abelian torsion sheaf”.

## Tag 0DG3, a lemma

[Tag 0DG3](https://stacks.math.columbia.edu/tag/0DG3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigEtaleSpaceSite.isIso_spacesEtaleDerivedBaseChange_app_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleTorsionDerivedPushforwardUnconditional.lean#L64), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperBaseChangeBoundedBelow.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleProperBaseChangeBoundedBelow.lean#L15) (StacksFrontier): “proper base change for algebraic spaces: g⁻¹ R f\_* E ≅ R f'\_* (g')⁻¹ E for f proper and E bounded below with torsion cohomology sheaves”.

## Tag 0DG4, a lemma

[Tag 0DG4](https://stacks.math.columbia.edu/tag/0DG4) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.abelianSheafFiberHomologyDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/GeometricPointStalkProperBaseChange.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/GeometricPointStalkProperBaseChange.lean#L62). The attribute's comment: “(2)”. References: SGA 4 XVI (2.1), “more general”; SGA 4 XVI (2.2), “more general”.

> Let `f : Y ⟶ X` be a proper morphism of algebraic spaces over a
> scheme `S` and `x̄ : Spec Ω ⟶ X` a geometric point, with geometric fibre `Y_x̄ = Y ×_X Spec Ω`
> and projection `g' : Y_x̄ ⟶ Y`. For an object `E` of `D⁺(Y_étale)` with torsion cohomology
> sheaves, `(Hⁿ(Rf_* E))_x̄ ≅ Hⁿ(RΓ(Y_x̄, E_x̄))` for every `n`, where `E_x̄ = (g')⁻¹ E`.

```lean
def abelianSheafFiberHomologyDerivedPushforwardIso
    (hf : Space.IsProper T.fppfSite S T.fppf_mem f.hom)
    (E : DerivedCategory (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
      Ab.{u + 1})) (m : ℤ) (hE : E.IsGE m) (hT : HasTorsionCohomology T E) (n : ℤ) :
    ((spacesEtaleSitePoint x).sheafFiber (A := Ab.{u + 1})).obj
      ((DerivedCategory.homologyFunctor
        (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1}) n).obj
          ((totalRightDerived (smallEtalePushforward T f)).obj E)) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((totalRightDerived (Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem
          (pullback f (geometricPointHom x))) Ab.{u + 1})).obj
        ((CategoryTheory.Sites.abelianInverseImage
          (smallEtaleMorphism T (pullback.fst f (geometricPointHom x)))).mapDerivedCategory.obj
            E))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.abelianSheafFiberRightDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/GeometricPointStalkProperBaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/GeometricPointStalkProperBaseChange.lean#L90). The attribute's comment: “(1)”. References: SGA 4 XII (5.2), “more general”; SGA 4 XVI (2.1), “more general”; SGA 4 XVI (2.2), “more general”; SGA 4½ Arcata (4.1.1), “more general”.

> Let `f : Y ⟶ X` be a proper morphism of algebraic spaces over a
> scheme `S` and `x̄ : Spec Ω ⟶ X` a geometric point, with geometric fibre `Y_x̄ = Y ×_X Spec Ω`
> and projection `g' : Y_x̄ ⟶ Y`. For a torsion abelian sheaf `F` on `Y_étale`,
> `(Rⁿf_* F)_x̄ ≅ Hⁿ_étale(Y_x̄, F_x̄)` for every `n`, where `F_x̄ = (g')⁻¹ F`.

```lean
def abelianSheafFiberRightDerivedPushforwardIso
    (hf : Space.IsProper T.fppfSite S T.fppf_mem f.hom)
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty
      (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) F) (n : ℕ) :
    ((spacesEtaleSitePoint x).sheafFiber (A := Ab.{u + 1})).obj
      (((smallEtalePushforward T f).rightDerived n).obj F) ≅
    AddCommGrpCat.of (Sheaf.H.{u + 1} ((CategoryTheory.Sites.abelianInverseImage
      (smallEtaleMorphism T (pullback.fst f (geometricPointHom x)))).obj F) n)
```

## Tag 0DG5, a lemma

[Tag 0DG5](https://stacks.math.columbia.edu/tag/0DG5) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.spacesEtaleCohomologyRestrictionMap_bijective_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesSeparablyClosedFieldExtension.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesSeparablyClosedFieldExtension.lean#L126). References: SGA 4 XII (5.4), “more general”; SGA 4 XVI (1.6), “Abelian clause”.

> **Étale cohomology of a proper algebraic space does not change under an extension of
> separably closed ground fields**. Let `K/k` be an extension of separably closed fields and
> `p : X ⟶ Spec k` a proper morphism of algebraic spaces; write `X_K = X ×_{Spec k} Spec K` with
> projection `g' : X_K ⟶ X`. Then for every torsion abelian sheaf `F` on `X_étale` and every
> `q ≥ 0` the restriction map `H^q_étale(X, F) ⟶ H^q_étale(X_K, F|_{X_K})` is bijective.
>
> The base change map `g⁻¹ R p_* E ⟶ R p_{K,*} (g')⁻¹ E` is invertible at every bounded below `E`
> with torsion cohomology sheaves by Stacks 0DG3
> (`isIso_spacesEtaleDerivedBaseChange_app_of_isProper_of_representable`, with Stacks 0A3U and
> Stacks 095T for schemes supplied).

```lean
theorem spacesEtaleCohomologyRestrictionMap_bijective_of_isSepClosed {X : T.Spaces}
    (p : X ⟶ yonedaSpace T.fppfSite S T.fppf_mem (BigFppfOver.mk T.fppfSite S T.fppf_mem hk s))
    (hp : Space.IsProper T.fppfSite S T.fppf_mem p.hom)
    [HasExt.{w} (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})]
    [HasExt.{w} (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem
      (pullback p (fieldExtensionSpaceHom T k K hk hK s))) Ab.{u + 1})]
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty
      (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) F) (q : ℕ) :
    Function.Bijective (spacesEtaleCohomologyRestrictionMap.{u, w} T
      (pullback.fst p (fieldExtensionSpaceHom T k K hk hK s)) F q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.4, Tag 0DFW](https://stacks.math.columbia.edu/tag/0DFW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
