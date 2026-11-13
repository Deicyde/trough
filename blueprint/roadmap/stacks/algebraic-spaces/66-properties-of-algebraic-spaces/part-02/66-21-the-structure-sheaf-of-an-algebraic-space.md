---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.structurePresheaf_isSheaf, AlgebraicGeometry.Space.structureSheaf, AlgebraicGeometry.Space.pushforwardAlgebraIdAlgebraIso, AlgebraicGeometry.Space.isIso_fSharp_id, AlgebraicGeometry.Space.smallEtaleRingedToposHom, AlgebraicGeometry.Space.smallEtaleRingedToposHom_pushforward, AlgebraicGeometry.Space.smallEtaleRingedToposHom_representable, AlgebraicGeometry.Space.structureSharp_comp_chartProjectionSharpDirectImage
statement: formalized
proof: formalized
---

# 66.21 The structure sheaf of an algebraic space

Section 66.21 of the Stacks Project, [Tag 04KD](https://stacks.math.columbia.edu/tag/04KD). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03G6, a lemma

[Tag 03G6](https://stacks.math.columbia.edu/tag/03G6) in the Stacks Project.

**`AlgebraicGeometry.Space.structurePresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureSheaf.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StructureSheaf.lean#L317).

> **Stacks 03G6.** Global regular functions form a sheaf of commutative rings on the small
> étale site of an algebraic space.
>
> Stated with 03G6's own hypotheses, in their original binder order, so that dependent results apply
> it positionally; the hypothesis is discarded, and `structurePresheaf_isSheaf'` is the general
> statement.

```lean
theorem structurePresheaf_isSheaf (_hF : IsAlgebraicSpace B S hS F) :
    Presheaf.IsSheaf (SmallEtale.topology B S hS F) (structurePresheaf B S hS F)
```

## Tag 03G7, a definition

[Tag 03G7](https://stacks.math.columbia.edu/tag/03G7) in the Stacks Project.

**`AlgebraicGeometry.Space.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureSheaf.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StructureSheaf.lean#L332). The attribute's comment: “the structure sheaf of an algebraic space”.

> The structure sheaf of commutative rings on the small étale site of the algebraic space `F`.
>
> Stated with 03G6's own hypotheses, in their original binder order, so that a ringed site built on
> it applies this positionally; `structureSheaf'` is the general form, and the two are equal by
> `rfl`.

```lean
def structureSheaf (_hF : IsAlgebraicSpace B S hS F) :
    Sheaf (SmallEtale.topology B S hS F) CommRingCat.{u}
```

## Tag 03G8, a lemma

[Tag 03G8](https://stacks.math.columbia.edu/tag/03G8) in the Stacks Project.

**`AlgebraicGeometry.Space.pushforwardAlgebraIdAlgebraIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BoundedDirectImageAlgebraFactorization.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BoundedDirectImageAlgebraFactorization.lean#L254). The attribute's comment: “the identity clause at the level of algebras: (𝟙\_Y)\_* 𝒪\_Y is 𝒪\_Y”.

> **The direct image of `𝒪_Y` along the identity of `Y` is `𝒪_Y`, as an `𝒪_Y`-algebra**, with
> no anti-equivalence and no hypothesis.
>
> `AlgebraicGeometry.Space.pushforwardAlgebra` of a morphism is its structure map read as an
> algebra structure, so this is the identity clause of Stacks 03G8 — the structure map of an
> identity is an isomorphism, `AlgebraicGeometry.Space.isIso_fSharp_id` — read through
> `AlgebraicGeometry.Space.AlgebraSheaf.ofHomIso`: the inverse of that structure map carries it to
> the identity of `𝒪_Y`, which is the structure map of `AlgebraicGeometry.Space.unitAlgebra`.
>
> This is the isomorphism that `AlgebraicGeometry.Space.pushforwardAlgebraIdIso` of
> `StacksFrontier.AlgebraicGeometry.Spaces.DirectImageAlgebraFactorization` obtains from an assumed
> anti-equivalence and that
> `StacksFrontier.AlgebraicGeometry.Spaces.RelativeSpecDirectImage` carries as the hypothesis
> `hid`.

```lean
def pushforwardAlgebraIdAlgebraIso (Y : AlgebraicSpaces B S hS) :
    pushforwardAlgebra B S hS (Over.mk (𝟙 Y)) ≅ unitAlgebra B S hS Y
```

**`AlgebraicGeometry.Space.isIso_fSharp_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DirectImageAlgebraMorphism.lean#L584). The attribute's comment: “the identity clause: the structure map of an identity is an isomorphism”.

> **The identity clause of Stacks 03G8:** the structure map of the morphism of small étale
> ringed topoi of `𝟙 : A ⟶ A` is an isomorphism `𝒪_A ≅ (𝟙_A)_* 𝒪_A`.
>
> On underlying sheaves of sets this is `AlgebraicGeometry.Space.structureSharpSet_id`, which
> identifies the structure map of an identity with the canonical comparison
> `AlgebraicGeometry.Space.smallEtaleDirectImageIdIso` of the direct image along an identity with
> the identity functor; forgetting the ring operations reflects isomorphisms, so the
> `CommRingCat`-valued structure map is invertible too.
> `AlgebraicGeometry.Space.isIso_structureSharp_id` is the same statement for the `RingCat`-valued
> `AlgebraicGeometry.Space.structureSharp`, which is not the map that
> `AlgebraicGeometry.Space.pushforwardAlgebra` is built from.

```lean
theorem isIso_fSharp_id (A : AlgebraicSpaces B S hS) :
    IsIso (smallEtaleRingedToposHom B S hS (𝟙 A)).fSharp
```

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L281). The attribute's comment: “canonical morphism of ringed topoi”.

> The morphism of small étale ringed topoi induced by a morphism of algebraic spaces.

```lean
noncomputable def smallEtaleRingedToposHom (f : X ⟶ Y) :
    RingedToposHom (smallEtaleRingedTopos B S hS X) (smallEtaleRingedTopos B S hS Y)
```

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_pushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L288). The attribute's comment: “underlying geometric morphism”.

> The underlying geometric morphism of `smallEtaleRingedToposHom`.

```lean
noncomputable def smallEtaleRingedToposHom_pushforward (f : X ⟶ Y) :
    ((comparisonFunctor B S hS X).sheafPushforwardContinuous (Type u)
          (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X)) ⋙
        (smallEtaleRingedToposHom B S hS f).toToposHom.pushforward ≅
      ((spacesBaseChange B S hS f).functor.sheafPushforwardContinuous (Type u)
          (SpacesEtale.topology B S hS Y) (SpacesEtale.topology B S hS X)) ⋙
        (comparisonFunctor B S hS Y).sheafPushforwardContinuous (Type u)
          (SmallEtale.topology B S hS Y.1) (SpacesEtale.topology B S hS Y)
```

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_representable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L347). The attribute's comment: “agreement with scheme-chart base change”.

> **Stacks 03G8.** For a representable morphism of algebraic spaces the geometric direct
> image of `smallEtaleRingedToposHom` is base change of étale scheme charts.

```lean
noncomputable def smallEtaleRingedToposHom_representable (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    letI := (smallBaseChange_isMorphismOfSites B S hS f hf).toIsContinuous
    (smallEtaleRingedToposHom B S hS f).toToposHom.pushforward ≅
      (smallBaseChange B S hS f hf).sheafPushforwardContinuous (Type u)
        (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1)
```

**`AlgebraicGeometry.Space.structureSharp_comp_chartProjectionSharpDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean#L352). The attribute's comment: “part (2): the structure map is pullback along the cartesian projection”.

> **Stacks 03G8, part (2), for a representable morphism of algebraic spaces.** The structure
> map `f♯ : 𝒪_Y ⟶ f_*𝒪_X` of Stacks 03G8, followed by the identification
> `AlgebraicGeometry.Space.chartProjectionSharpDirectImage` of the sections of `f_*𝒪_X` over an
> étale chart `V` of `Y` with the regular functions on the scheme `X ×_Y V`, is pullback of
> regular functions along the cartesian projection `X ×_Y V ⟶ V` — which is the structure map of
> the morphism of small étale ringed sites of Stacks 070R, part (2).

```lean
theorem structureSharp_comp_chartProjectionSharpDirectImage (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    letI := isContinuous_smallBaseChange B S hS f hf
    structureSharp B S hS f ≫ chartProjectionSharpDirectImage B S hS f hf =
      cartesianProjectionSharp B S hS f hf
```

**`AlgebraicGeometry.Space.fSharp_comp_chartProjectionSharpDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean#L401). The attribute's comment: “part (2): the same for the structure map of the morphism of ringed topoi”.

> **Stacks 03G8, part (2), for a representable morphism of algebraic spaces, on the morphism
> of ringed topoi.** The structure map `f♯` of the morphism of small étale ringed topoi of
> Stacks 03G8, read on sheaves of not necessarily commutative rings and followed by the
> identification of the sections of `f_*𝒪_X` over an étale chart `V` of `Y` with the regular
> functions on `X ×_Y V`, is pullback of regular functions along the cartesian projection
> `X ×_Y V ⟶ V`.

```lean
theorem fSharp_comp_chartProjectionSharpDirectImage (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    letI := isContinuous_smallBaseChange B S hS f hf
    (sheafCompose (SmallEtale.topology B S hS Y.1)
            (forget₂ CommRingCat.{u} RingCat.{u})).map
          (smallEtaleRingedToposHom B S hS f).fSharp ≫
        chartProjectionSharpDirectImage B S hS f hf =
      cartesianProjectionSharp B S hS f hf
```

**`AlgebraicGeometry.Space.cartesianProjectionSharpCommRing_eq_changeOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean#L440). The attribute's comment: “part (2): for a morphism of schemes this is the Stacks 070R structure map”.

> **Stacks 03G8, part (2).** For a morphism of schemes, `f♯` of the space construction *is*
> the structure-sheaf homomorphism of Stacks 070R: the small étale site of the representable
> algebraic space `yoneda.obj T` is a site of schemes over `T` through
> `AlgebraicGeometry.Space.schemeChartToOver`, and over that presentation the map
> `AlgebraicGeometry.Space.cartesianProjectionSharpCommRing` — which
> `AlgebraicGeometry.Space.structureSharp_comp_chartProjectionSharpDirectImage` identifies with
> `f♯` — is `AlgebraicGeometry.ChangeOfSites.structureSharp`, the structure-sheaf homomorphism of
> a change-of-topologies morphism of sites, formed with the cartesian projections.

```lean
theorem cartesianProjectionSharpCommRing_eq_changeOfSites :
    letI := isContinuous_smallBaseChange B S hS (representedSpaceMap B S hS g) hg
    cartesianProjectionSharpCommRing B S hS (representedSpaceMap B S hS g) hg =
      AlgebraicGeometry.ChangeOfSites.structureSharp
        (SmallEtale.topology B S hS (yoneda.obj T))
        (SmallEtale.topology B S hS (yoneda.obj T'))
        (schemeChartToOver B S hS T) (schemeChartToOver B S hS T')
        (smallBaseChange B S hS (representedSpaceMap B S hS g) hg)
        (cartesianProjection B S hS (representedSpaceMap B S hS g) hg)
        (schemeChart_structure_isSheaf B S hS T)
        (schemeChart_structure_isSheaf B S hS T')
```

**`AlgebraicGeometry.Space.structureSharp_representedSpaceMap_eq_changeOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSchemeStructureSharp.lean#L464). The attribute's comment: “part (2): for a morphism of schemes, f♯ is the structure map of Stacks 070R”.

> **Stacks 03G8, part (2).** For a morphism of schemes `g : T' ⟶ T` over `S` the structure
> map `f♯ : 𝒪_Y ⟶ f_*𝒪_X` of Stacks 03G8, followed by the canonical identification
> `AlgebraicGeometry.Space.chartProjectionSharpDirectImage` of the sections of `f_*𝒪_{T'}` over an
> étale chart `V` of `T` with the regular functions on the scheme `T' ×_T V`, *is* the structure
> map of Stacks 070R: the map `AlgebraicGeometry.ChangeOfSites.structureSharp` of the
> change-of-topologies morphism of sites given by base change of étale charts, formed with the
> cartesian projections `T' ×_T V ⟶ V`.
>
> The identification is an isomorphism, by
> `AlgebraicGeometry.Space.isIso_chartProjectionSharpDirectImage`, so this is an equality of the
> two structure maps and not merely a factorization.

```lean
theorem structureSharp_representedSpaceMap_eq_changeOfSites :
    letI := isContinuous_smallBaseChange B S hS (representedSpaceMap B S hS g)
      (relativelyRepresentable_yoneda_map B S hS g)
    (sheafCompose (SmallEtale.topology B S hS (yoneda.obj T))
          (forget₂ CommRingCat.{u} RingCat.{u})).map
        (AlgebraicGeometry.ChangeOfSites.structureSharp
          (SmallEtale.topology B S hS (yoneda.obj T))
          (SmallEtale.topology B S hS (yoneda.obj T'))
          (schemeChartToOver B S hS T) (schemeChartToOver B S hS T')
          (smallBaseChange B S hS (representedSpaceMap B S hS g)
            (relativelyRepresentable_yoneda_map B S hS g))
          (cartesianProjection B S hS (representedSpaceMap B S hS g)
            (relativelyRepresentable_yoneda_map B S hS g))
          (schemeChart_structure_isSheaf B S hS T)
          (schemeChart_structure_isSheaf B S hS T')) =
      structureSharp B S hS (representedSpaceMap B S hS g) ≫
        chartProjectionSharpDirectImage B S hS (representedSpaceMap B S hS g)
          (relativelyRepresentable_yoneda_map B S hS g)
```

**`AlgebraicGeometry.Space.smallEtaleRingedToposHom_comp_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStructureMapComp.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStructureMapComp.lean#L561). The attribute's comment: “compatibility with composition”.

> The structure map of the composite morphism of small étale ringed topoi, followed by the
> comparison of the direct images of sheaves of commutative rings, is the structure map of the
> composite morphism of algebraic spaces.

```lean
theorem smallEtaleRingedToposHom_comp_fSharp (f : X ⟶ Y) (g : Y ⟶ Z) :
    ((smallEtaleRingedToposHom B S hS g).comp
        (smallEtaleRingedToposHom B S hS f)).fSharp ≫
        (smallEtaleRingedToposHom_compRingIso B S hS f g).hom.app
          (smallEtaleRingedTopos B S hS X).O =
      (smallEtaleRingedToposHom B S hS (f ≫ g)).fSharp
```

**`AlgebraicGeometry.Space.exists_compRingIso_isCartesianComposition_comp_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStructureMapComp.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStructureMapComp.lean#L595). The attribute's comment: “existence of the cartesian ring comparison”.

> There is an isomorphism between the direct images of sheaves of commutative rings of the
> composite of morphisms of ringed topoi and of the composite morphism of algebraic spaces which is
> induced by cartesian composition and carries the structure map of the composite to the structure
> map of the composite morphism.

```lean
theorem exists_compRingIso_isCartesianComposition_comp_fSharp (f : X ⟶ Y) (g : Y ⟶ Z) :
    ∃ i : pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
        ((smallEtaleRingedToposHom B S hS g).comp
          (smallEtaleRingedToposHom B S hS f)).toToposHom ≅
      pushforwardCommRingFunctor.{u, u, u, u + 1, u, u + 1}
        (smallEtaleRingedToposHom B S hS (f ≫ g)).toToposHom,
      IsCartesianComposition B S hS f g i ∧
        ((smallEtaleRingedToposHom B S hS g).comp
            (smallEtaleRingedToposHom B S hS f)).fSharp ≫
            i.hom.app (smallEtaleRingedTopos B S hS X).O =
          (smallEtaleRingedToposHom B S hS (f ≫ g)).fSharp
```

**`AlgebraicGeometry.Space.structureProjectionOfHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureProjectionComposition.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StructureProjectionComposition.lean#L146). The attribute's comment: “compatibility with composition at the level of modules”.

> **[Stacks Project, Tag 03G8], compatibility with composition, at the level of modules.**  For
> `f : X ⟶ Y` and `g : Y ⟶ Z` the canonical morphism `𝒪_Z ⟶ (f ≫ g)_*𝒪_X` of `𝒪_Z`-modules is the
> canonical morphism `𝒪_Z ⟶ g_*𝒪_Y` of `g`, followed by the direct image along `g` of the
> canonical morphism `𝒪_Y ⟶ f_*𝒪_X` of `f`, followed by the composition comparison
> `g_*(f_*𝒪_X) ⟶ (f ≫ g)_*𝒪_X` of direct images of [Stacks Project, Tag 03LU].
>
> The proof is the transposed one: by
> `AlgebraicGeometry.Space.structureProjectionOfHom_eq_homEquiv_structureModulePullbackMap` each
> of the three canonical morphisms is a transpose along the adjunction of
> [Stacks Project, Tag 03D7], the composition law for the comparison of inverse images is
> `AlgebraicGeometry.Space.structureModulePullbackMap_comp`, and transposing the resulting
> composite is `AlgebraicGeometry.Space.homEquiv_modulePullbackCompIso_inv_app_comp` followed by
> the two naturalities of `CategoryTheory.Adjunction.homEquiv`.

```lean
theorem structureProjectionOfHom_comp (f : X ⟶ Y) (g : Y ⟶ Z) :
    structureProjectionOfHom B S hS (f ≫ g) =
      structureProjectionOfHom B S hS g ≫
        (modulePushforward B S hS g).map (structureProjectionOfHom B S hS f) ≫
        (modulePushforwardCompIso B S hS f g).hom.app
          (SheafOfModules.unit (structureRingSheaf B S hS X))
```

**`AlgebraicGeometry.Space.isIso_structureProjectionOfHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureProjectionComposition.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StructureProjectionComposition.lean#L261). The attribute's comment: “the canonical morphism of modules of an isomorphism is an isomorphism”.

> **The canonical morphism `𝒪_Y ⟶ e_*𝒪_X` of modules of an isomorphism `e` of algebraic spaces
> is invertible.**
>
> Its underlying morphism of sheaves of sets is the structure map `e.hom♯`
> (`AlgebraicGeometry.Space.moduleSheafFunctor_map_structureProjectionOfHom`), which is invertible
> by `AlgebraicGeometry.Space.isIso_structureSharpSet`, and the underlying-sheaf functor reflects
> isomorphisms.

```lean
theorem isIso_structureProjectionOfHom (e : X ≅ Y) :
    IsIso (structureProjectionOfHom B S hS e.hom)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.schemeSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchemeAsSpace.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean, line 712](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRingedToposHom.lean#L712) (StacksFrontier): “schemes regarded as algebraic spaces”.

## Tag 0BGS, a lemma

[Tag 0BGS](https://stacks.math.columbia.edu/tag/0BGS) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_globalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedGlobalFunctions.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedGlobalFunctions.lean#L172). The attribute's comment: “global\_sections\_reduced”.

> **Stacks 0BGS.** The ring of global regular functions of a reduced algebraic space is
> reduced.  Restriction to a reduced surjective étale chart embeds it into the ring of global
> regular functions of a reduced scheme.

```lean
theorem isReduced_globalFunctions (hF : IsAlgebraicSpace B S hS F)
    (hred : HasEtaleLocalProperty B S hS F
      (fun X : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced X)) :
    _root_.IsReduced (globalFunctions B S hS F)
```

**`AlgebraicGeometry.Space.eq_zero_of_forall_zeroLocus_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedGlobalFunctions.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedGlobalFunctions.lean#L188). The attribute's comment: “zero\_of\_full\_vanishing\_locus”.

> **Stacks 0BGS.** A global regular function on a reduced algebraic space whose vanishing
> locus is all of `F` — its zero locus on every étale chart is the whole chart — is zero.  It
> vanishes on a reduced surjective étale chart, hence is zero there by
> `AlgebraicGeometry.eq_zero_of_basicOpen_eq_bot`, and restriction to that chart is injective.

```lean
theorem eq_zero_of_forall_zeroLocus_eq_univ (hF : IsAlgebraicSpace B S hS F)
    (hred : HasEtaleLocalProperty B S hS F
      (fun X : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced X))
    (f : globalFunctions B S hS F)
    (hf : ∀ U : SmallEtale B S hS F,
      ((BigFppfOver.toScheme B S hS).obj ((SmallEtale.toOver B S hS F).obj U)).zeroLocus
        {f.val (op U)} = Set.univ) :
    f = 0
```

**`AlgebraicGeometry.Space.isReduced_iff_forall_localRing_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ReducedLocalRings.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ReducedLocalRings.lean#L120). The attribute's comment: “reduced\_iff\_local\_rings\_reduced”.

> **Stacks 0BGS.** An algebraic space is reduced exactly when all of its local rings are
> reduced. Reducedness of the space is the étale-local scheme property of Stacks 03E6 — a
> reduced surjective étale scheme chart — and reducedness of its local ring at a point is the
> chart condition of `AlgebraicGeometry.Space.HasLocalRingPropertyAtPoint`.

```lean
theorem isReduced_iff_forall_localRing_isReduced (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsReduced X) ↔
      ∀ x : points B S hS F,
        HasLocalRingPropertyAtPoint B S hS F hF x
          (fun (R : Type u) => fun [CommRing R] => _root_.IsReduced R)
          isReduced_localization_etale_invariant
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.21, Tag 04KD](https://stacks.math.columbia.edu/tag/04KD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
