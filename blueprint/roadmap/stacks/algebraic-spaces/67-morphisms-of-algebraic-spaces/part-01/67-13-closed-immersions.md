---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.closedImmersion_quasicoherentIdeal_correspondence, AlgebraicGeometry.Space.isPullback_gysinBaseChange, CategoryTheory.Subfunctor.isPullback_preimage, AlgebraicGeometry.Space.isClosedSubspace_preimage, CategoryTheory.Subfunctor.preimage, AlgebraicGeometry.Space.isQuasiCompact_of_isClosedImmersion, AlgebraicGeometry.Space.isSeparated_of_isClosedImmersion, AlgebraicGeometry.Space.fullyFaithfulSmallEtalePushforwardOfIsClosedImmersion
statement: formalized
proof: formalized
---

# 67.13 Closed immersions

Section 67.13 of the Stacks Project, [Tag 03MA](https://stacks.math.columbia.edu/tag/03MA). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03MB, a lemma

[Tag 03MB](https://stacks.math.columbia.edu/tag/03MB) in the Stacks Project.

**`AlgebraicGeometry.Space.closedImmersion_quasicoherentIdeal_correspondence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealCorrespondence.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealCorrespondence.lean#L214).

> **Stacks 03MB.**  Let `X` be an algebraic space over `S`.
>
> 1. For every closed immersion `i : Z ⟶ X` of algebraic spaces the direct image `i_*𝒪_Z` is a
>    quasi-coherent `𝒪_X`-module, the map `i♯ : 𝒪_X ⟶ i_*𝒪_Z` is surjective — locally surjective as
>    a map of sheaves of rings, and an epimorphism of `𝒪_X`-modules — and its kernel is a
>    quasi-coherent sheaf of ideals.
> 2. The rule `Z ↦ 𝓘_Z = Ker(𝒪_X ⟶ i_*𝒪_Z)`, with `i` the inclusion of `Z`, is an
>    inclusion-reversing bijection from the closed subspaces of `X` onto the quasi-coherent sheaves
>    of ideals of `𝒪_X`.
> 3. If `Z` corresponds to `𝓘 = 𝓘_Z`, a morphism `h : Y ⟶ X` of algebraic spaces factors through
>    `Z` if and only if the map `h^*𝓘 ⟶ h^*𝒪_X = 𝒪_Y` is zero.

```lean
theorem closedImmersion_quasicoherentIdeal_correspondence :
    (∀ {Z : AlgebraicSpaces B S hS} (i : Z ⟶ X), IsClosedImmersion B S hS i.hom →
      (structureSheafPushforward B S hS i).IsQuasicoherentOnSite ∧
        Sheaf.IsLocallySurjective (structureSharp B S hS i) ∧
        Epi (pushforwardStructureProjection B S hS i) ∧
        (SheafOfModules.Submodule.ker
          (pushforwardStructureProjection B S hS i)).toSheafOfModules.IsQuasicoherentOnSite) ∧
    (∀ Z : ClosedSubspaces B S hS X.1,
      definingIdealSheaf B S hS X Z = SheafOfModules.Submodule.ker
        (pushforwardStructureProjection B S hS (ObjectProperty.homMk Z.1.ι :
          (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS) ⟶ X))) ∧
    Set.BijOn (definingIdealSheaf B S hS X) Set.univ
      {I | I.toSheafOfModules.IsQuasicoherentOnSite} ∧
    (∀ Z W : ClosedSubspaces B S hS X.1,
      Z ≤ W ↔ definingIdealSheaf B S hS X W ≤ definingIdealSheaf B S hS X Z) ∧
    ∀ (Z : ClosedSubspaces B S hS X.1) {Y : AlgebraicSpaces B S hS} (h : Y ⟶ X),
      (∃ g : Y ⟶ (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS),
          g ≫ ObjectProperty.homMk Z.1.ι = h) ↔
        (modulePullback B S hS h).map (definingIdealSheaf B S hS X Z).ι ≫
          (modulePullbackUnitIso B S hS h).hom = 0
```

## Tag 083Q, a definition

[Tag 083Q](https://stacks.math.columbia.edu/tag/083Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_gysinBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean#L201). The attribute's comment: “the square of Remark 0ER3 is cartesian”.

> **Remark 0ER3.** The square of Remark 0ER3 is cartesian: `D'` is the fibre product
> `D ×_X X'`, by Stacks 083Q.

```lean
theorem isPullback_gysinBaseChange :
    IsPullback (gysinBaseChangeHom D p hp p' hp' f E)
      (gysinBaseChangeSubspace D p hp p' hp' f E).1.ι E.1.ι f
```

**`CategoryTheory.Subfunctor.isPullback_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean#L67). The attribute's comment: “fibre-product characterization”.

> **Stacks 083Q.** The inverse image of a subfunctor along a morphism of presheaves is
> canonically the fibre product of that subfunctor with the source of the morphism.

```lean
theorem isPullback_preimage {C : Type*} [Category C] {X Y : C ⥤ Type u}
    (f : Y ⟶ X) (Z : Subfunctor X) :
    IsPullback (Z.fromPreimage f) (Z.preimage f).ι Z.ι f
```

**`AlgebraicGeometry.Space.isClosedSubspace_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean#L147). The attribute's comment: “closedness of inverse image”.

> **Stacks 083Q.** The inverse image of a closed subspace of an algebraic space along a
> morphism of algebraic spaces over `S` is a closed subspace of the source.

```lean
theorem isClosedSubspace_preimage
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : Y ⟶ X) (Z : Subfunctor X)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsClosedSubspace B S hS Z) :
    IsClosedSubspace B S hS (Z.preimage f)
```

Declarations registered for the tag:

- [`CategoryTheory.Subfunctor.preimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Subfunctor.preimage#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SubspacePreimage.lean#L62) (StacksFrontier): “inverse-image construction”.

## Tag 04CG, a lemma

[Tag 04CG](https://stacks.math.columbia.edu/tag/04CG) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiCompact_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQC.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQC.lean#L94).

> A closed immersion of algebraic spaces over `S` is quasi-compact.

```lean
theorem isQuasiCompact_of_isClosedImmersion {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : F ⟶ G)
    (_hF : IsAlgebraicSpace B S hS F) (_hG : IsAlgebraicSpace B S hS G)
    (hf : IsClosedImmersion B S hS f) :
    IsQuasiCompact B S hS f
```

## Tag 04CH, a lemma

[Tag 04CH](https://stacks.math.columbia.edu/tag/04CH) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedImmersion.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedImmersion.lean#L123).

> **Stacks 04CH.** A closed immersion of algebraic spaces over `S` is separated. Its
> relative diagonal is an isomorphism, because the morphism is a monomorphism, and an
> isomorphism of presheaves is a closed immersion.

```lean
theorem isSeparated_of_isClosedImmersion (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f) :
    IsSeparated B S hS f
```

## Tag 04E5, a lemma

[Tag 04E5](https://stacks.math.columbia.edu/tag/04E5) in the Stacks Project.

**`AlgebraicGeometry.Space.fullyFaithfulSmallEtalePushforwardOfIsClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean#L287). The attribute's comment: “part (1): full faithfulness on sheaves of sets”. References: SGA 4 VIII (6.3), “fully faithful”.

> **Stacks 04E5, part (1).** For a closed immersion `f : X ⟶ Y` of algebraic spaces over `S`,
> the direct image of sheaves of sets along the morphism of small étale topoi of Stacks 03G2,
> part (3) is fully faithful.

```lean
noncomputable def fullyFaithfulSmallEtalePushforwardOfIsClosedImmersion (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    (smallToposMorphismTypeU B S hS f).pushforward.FullyFaithful
```

**`AlgebraicGeometry.Space.smallEtalePullbackPushforwardCounitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean#L299). The attribute's comment: “part (1): inverse image is a left inverse”. References: SGA 4 VIII (5.7), “partial”.

> **Stacks 04E5, part (1).** For a closed immersion `f : X ⟶ Y` of algebraic spaces over `S`
> the inverse image of sheaves of sets is a *left inverse* of the direct image: the counit
> `f^{-1}f_*G ⟶ G` of the adjunction of the morphism of small étale topoi of Stacks 03G2, part (3)
> is an isomorphism for every sheaf `G` on the small étale site of `X`.

```lean
noncomputable def smallEtalePullbackPushforwardCounitIso (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    (smallToposMorphismTypeU B S hS f).pushforward ⋙
        (smallToposMorphismTypeU B S hS f).inverseImage ≅
      𝟭 (Sheaf (SmallEtale.topology B S hS X.1) (Type u))
```

**`AlgebraicGeometry.Space.fullyFaithfulSmallEtaleAbelianPushforwardOfIsClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean#L313). The attribute's comment: “part (2): full faithfulness on abelian sheaves”.

> **Stacks 04E5, part (2), full faithfulness.** For a closed immersion `f : X ⟶ Y` of algebraic
> spaces over `S`, the direct image of sheaves of *abelian groups* along `f` — restriction along
> the chart base-change morphism of small étale sites of Stacks 03G2, part (4) — is fully faithful.

```lean
noncomputable def fullyFaithfulSmallEtaleAbelianPushforwardOfIsClosedImmersion (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f hf.rep).toIsContinuous
    ((smallBaseChange B S hS f hf.rep).sheafPushforwardContinuous AddCommGrpCat.{w}
      (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1)).FullyFaithful
```

**`AlgebraicGeometry.Space.smallEtaleAbelianPullbackPushforwardCounitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartBaseChangeDense.lean#L328). The attribute's comment: “part (2): inverse image is a left inverse”. References: SGA 4 VIII (5.7), “partial”.

> **Stacks 04E5, part (2).** For a closed immersion `f : X ⟶ Y` of algebraic spaces over `S`
> the inverse image of sheaves of abelian groups is a *left inverse* of the direct image: the
> counit of the adjunction of `CategoryTheory.Functor.sheafAdjunctionContinuous` for chart base
> change is a natural isomorphism `f_* ⋙ f^{-1} ≅ 𝟭`. The abelian groups are taken at the
> universe `u + 1`, at which the small étale site has sheafification.

```lean
noncomputable def smallEtaleAbelianPullbackPushforwardCounitIso (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f hf.rep).toIsContinuous
    letI : ((smallBaseChange B S hS f hf.rep).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
      (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1)).IsRightAdjoint :=
      (Functor.sheafPullbackConstruction.sheafAdjunctionContinuous _ _ _ _).isRightAdjoint
    (smallBaseChange B S hS f hf.rep).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1) ⋙
      (smallBaseChange B S hS f hf.rep).sheafPullback AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1) ≅
      𝟭 (Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.Space.smallBaseChange_isCoverDense_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartCoverDensity.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartCoverDensity.lean#L258). The attribute's comment: “part (1): cover density of chart base change”.

> **Stacks 04E5, part (1).** Let `i : Z ⟶ X` be a closed immersion of algebraic spaces over a
> scheme `S`. Base change along `i` of étale scheme charts of `X` is cover dense for the small
> étale topology of `Z`: every étale chart of `Z` is covered by base changes along `i` of étale
> charts of `X`.

```lean
theorem smallBaseChange_isCoverDense_of_isClosedImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {Z X : AlgebraicSpaces B S hS} (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    (smallBaseChange B S hS i hi.rep).IsCoverDense (SmallEtale.topology B S hS Z.1)
```

**`AlgebraicGeometry.Space.smallBaseChange_isLocallyFull_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartLocalFullness.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartLocalFullness.lean#L366). The attribute's comment: “part (1), local fullness of base change on scheme charts”.

> **Stacks 04E5, part (1)**, local fullness. For a closed immersion `i : Z ⟶ X` of algebraic
> spaces over a scheme `S`, base change along `i` of étale scheme charts is a locally full functor
> from the small étale site of `X` to the small étale site of `Z`: a morphism over `Z` between the
> base changes of two étale charts of `X` is, locally on the source, the base change of a morphism
> of charts of `X`.
>
> No covering family has to be produced: the chart of
> `AlgebraicGeometry.Space.exists_isIso_smallBaseChange_map_of_isClosedImmersion` already has
> invertible base change, so the sieve it generates is the whole sieve.

```lean
theorem smallBaseChange_isLocallyFull_of_isClosedImmersion
    {Z X : AlgebraicSpaces B S hS} (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    (smallBaseChange B S hS i hi.rep).IsLocallyFull (SmallEtale.topology B S hS Z.1)
```

**`AlgebraicGeometry.Space.smallEtalePushforward_essImage_iff_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionSetSheafEssentialImage.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionSetSheafEssentialImage.lean#L224). The attribute's comment: “part (1): the essential image”.

> **Stacks 04E5, part (1), the essential image.** For a closed immersion `i : Z ⟶ X` of
> algebraic spaces over `S`, a sheaf of sets on the small étale site of `X` lies in the essential
> image of the direct image along `i` exactly when it has exactly one section over every étale
> chart of `X` whose points avoid the point set of `Z`, that is exactly when its restriction to
> `X ∖ Z` is a singleton.
>
> The forward direction is Étale Cohomology 04FX away from `Z`,
> `AlgebraicGeometry.Space.nonempty_isTerminal_smallEtaleDirectImage_obj_of_chartPreimage_eq_empty`.
> The converse is Étale Cohomology 04CA: the unit of the adjunction is invertible on the fibre at
> every geometric point of `X`, on the point set of `Z` by the triangle identity and Stacks 04K2,
> part (4), and off it because both fibres are singletons; the geometric points are a conservative
> family, and the unit of a fully faithful right adjoint is invertible exactly on its essential
> image.

```lean
theorem smallEtalePushforward_essImage_iff_of_isClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.1) (Type u)) :
    (smallToposMorphismTypeU B S hS i).pushforward.essImage F ↔
      ∀ V : SmallEtale B S hS X.1, chartPreimage B S hS i V = ∅ →
        Nonempty (IsTerminal (F.obj.obj (op V)))
```

**`AlgebraicGeometry.Space.smallEtalePushforward_essImage_iff_abelian_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ComplexesWithSupport.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ComplexesWithSupport.lean#L633). The attribute's comment: “part (2): the essential image”.

> **Stacks 04E5, part (2), the essential image.** For a closed immersion `i : Z ⟶ X` of
> algebraic spaces over `S`, an abelian sheaf on the small étale site of `X` lies in the essential
> image of the direct image along `i` exactly when its support is contained in the point set
> of `Z`.
>
> Both directions are now unconditional: the forward one is
> `AlgebraicGeometry.Space.supportOfSheaf_subset_of_essImage`, resting on Étale Cohomology 04FX
> for algebraic spaces, and the converse is
> `AlgebraicGeometry.Space.isIso_unit_app_of_supportOfSheaf_subset`, Étale Cohomology 04CA for
> algebraic spaces, together with the characterization of the essential image of a fully faithful
> right adjoint by invertibility of the unit.

```lean
theorem smallEtalePushforward_essImage_iff_abelian_of_isClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) :
    (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).essImage F ↔
      supportOfSheaf B S hS X.1 F ⊆ Set.range (pointsMap B S hS Z.1 i.hom)
```

## Tag 0DK1, a lemma

[Tag 0DK1](https://stacks.math.columbia.edu/tag/0DK1) in the Stacks Project.

**`AlgebraicGeometry.Space.stalkPushforwardIsoOfIsClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionStalkPushforward.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionStalkPushforward.lean#L114).

> **Stacks 0DK1.** Let `i : Z ⟶ X` be a closed immersion of algebraic spaces over a scheme `S`
> and let `z` be a geometric point of `Z` with image `x` in `X`. Then `(i_*F)_x = F_z` for every
> sheaf of sets `F` on the small étale site of `Z`, naturally in `F`.

```lean
def stalkPushforwardIsoOfIsClosedImmersion (hci : IsClosedImmersion B S hS i.hom)
    (z : GeometricPoint B S hS Z.1) :
    (smallToposMorphism B S hS i).pushforward ⋙
        sheafToPresheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)) ⋙
          stalkSetFunctor (geometricPointMap i.hom z) ≅
      sheafToPresheaf (SmallEtale.topology B S hS Z.1) (Type (u + 1)) ⋙
        stalkSetFunctor z
```

## Tag 04G0, a lemma

[Tag 04G0](https://stacks.math.columbia.edu/tag/04G0) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedToposHomOfSharp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean#L182). The attribute's comment: “the morphism of ringed topoi determined by `i`, `𝒜`, `ℬ` and `φ`”.

> **The morphism of ringed topoi of Stacks 04G0**, `f : (Sh(Z_étale), ℬ) ⟶ (Sh(X_étale), 𝒜)`:
> its underlying morphism of topoi is that of Stacks 03G2, part (3), and its structure map is `φ`.
>
> No hypothesis on `i` enters, so this is equally the morphism of ringed topoi of Stacks 0DK4,
> whose datum is the same `(i, φ)` in the same direction, with `i` finite instead of a closed
> immersion.

```lean
noncomputable def smallEtaleRingedToposHomOfSharp (i : Z ⟶ X)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ) :
    Stacks.Sheaves.RingedToposModules.RingedToposHom
      (smallEtaleRingedToposOfRings B S hS Z ℬ) (smallEtaleRingedToposOfRings B S hS X 𝒜)
```

**`AlgebraicGeometry.Space.tensorPushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean#L202). The attribute's comment: “the canonical map `𝓕 ⊗_𝒜 f_*𝓖 ⟶ f_*(f^*𝓕 ⊗_ℬ 𝓖)`”.

> **The canonical map of Stacks 04G0**, `𝓕 ⊗_𝒜 f_*𝓖 ⟶ f_*(f^*𝓕 ⊗_ℬ 𝓖)`: the adjoint
> transpose of `f^*(𝓕 ⊗_𝒜 f_*𝓖) = f^*𝓕 ⊗_ℬ f^*f_*𝓖 ⟶ f^*𝓕 ⊗_ℬ 𝓖`, built from the identity of
> `f^*𝓕` and the adjunction map `f^*f_*𝓖 ⟶ 𝓖`.
>
> No hypothesis on `i` enters, so this is equally the canonical map of Stacks 0DK4, which is the
> adjoint transpose of the same comparison for the same datum with `i` finite.

```lean
noncomputable def tensorPushforwardMap (i : Z ⟶ X)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ)
    (𝓕 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS X 𝒜).O))
    (𝓖 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS Z ℬ).O)) :
    ((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u} 𝒜).obj 𝓕).obj
      ((pushforwardModules (smallEtaleRingedToposHomOfSharp B S hS i φ)).obj 𝓖) ⟶
      (pushforwardModules (smallEtaleRingedToposHomOfSharp B S hS i φ)).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u} ℬ).obj
          (((smallEtaleRingedToposHomOfSharp B S hS i φ).pullbackModules).obj 𝓕)).obj 𝓖)
```

**`AlgebraicGeometry.Space.isIso_tensorPushforwardMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModuleTensorPushforward.lean#L222). The attribute's comment: “invertibility, given the counit at `𝓖` and the unit at `𝓕 ⊗_𝒜 f_*𝓖`”.

> **Stacks 04G0, the invertibility clause**, reduced to the adjunction of Stacks 03D7: the
> canonical map is an isomorphism once the counit of `f^* ⊣ f_*` is invertible at `𝓖` and its unit
> is invertible at `𝓕 ⊗_𝒜 f_*𝓖`.

```lean
theorem isIso_tensorPushforwardMap (i : Z ⟶ X)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ)
    (𝓕 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS X 𝒜).O))
    (𝓖 : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
      (smallEtaleRingedToposOfRings B S hS Z ℬ).O))
    (hε : IsIso ((pullbackAdjPushforwardModules
      (smallEtaleRingedToposHomOfSharp B S hS i φ)).counit.app 𝓖))
    (hη : IsIso ((pullbackAdjPushforwardModules
        (smallEtaleRingedToposHomOfSharp B S hS i φ)).unit.app
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u} 𝒜).obj 𝓕).obj
        ((pushforwardModules (smallEtaleRingedToposHomOfSharp B S hS i φ)).obj 𝓖)))) :
    IsIso (tensorPushforwardMap B S hS i φ 𝓕 𝓖)
```

**`AlgebraicGeometry.Space.isIso_tensorPushforwardMap_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionTensorPushforwardIso.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionTensorPushforwardIso.lean#L127).

> **Stacks 04G0.** Let `i : Z ⟶ X` be a closed immersion of algebraic spaces over `S`, let `𝒜`
> be a sheaf of rings on `X_étale`, `ℬ` a sheaf of rings on `Z_étale` and
> `φ : 𝒜 ⟶ i_{small,*}ℬ` a homomorphism of sheaves of rings, giving a morphism of ringed topoi
> `f : (Sh(Z_étale), ℬ) ⟶ (Sh(X_étale), 𝒜)`. Then for every sheaf of `𝒜`-modules `𝓕` and every
> sheaf of `ℬ`-modules `𝓖` the canonical map
>
> `𝓕 ⊗_𝒜 f_*𝓖 ⟶ f_*(f^*𝓕 ⊗_ℬ 𝓖)`
>
> is an isomorphism.
>
> The canonical map is split into its inverse-image factor and its change-of-rings factor; the
> second is always invertible and the first is invertible because the inverse-image adjunction of a
> closed immersion has an invertible counit and a unit that is invertible at a tensor product with
> a direct image.

```lean
theorem isIso_tensorPushforwardMap_of_isClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    {𝒜 : Sheaf (SmallEtale.topology B S hS X.1) CommRingCat.{u}}
    {ℬ : Sheaf (SmallEtale.topology B S hS Z.1) CommRingCat.{u}}
    (φ : 𝒜 ⟶ (pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
      (smallToposMorphismTypeU B S hS i)).obj ℬ)
    (𝓕 : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedToposOfRings B S hS X 𝒜).O))
    (𝓖 : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedToposOfRings B S hS Z ℬ).O)) :
    IsIso (tensorPushforwardMap B S hS i φ 𝓕 𝓖)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.13, Tag 03MA](https://stacks.math.columbia.edu/tag/03MA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
