---
declaration: section
origin: cited
lean: PresheafOfModulesOfCommRing.Derivation', PresheafOfModulesOfCommRing.Derivation, AlgebraicGeometry.SheafOfModules.universalDerivation_isUniversal, AlgebraicGeometry.SheafOfModules.moduleOfDifferentials, AlgebraicGeometry.SheafOfModules.universalDerivation, AlgebraicGeometry.SheafOfModules.moduleOfDifferentialsIsoSectionwise, AlgebraicGeometry.SheafOfModules.pullbackDifferentialsIso, AlgebraicGeometry.SheafOfModules.inverseImageDerivation
statement: formalized
proof: formalized
---

# 17.28 Modules of differentials

Section 17.28 of the Stacks Project, [Tag 08RL](https://stacks.math.columbia.edu/tag/08RL). 14 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01UN, a definition

[Tag 01UN](https://stacks.math.columbia.edu/tag/01UN) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModulesOfCommRing.Derivation'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModulesOfCommRing.Derivation'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L61) (StacksFrontier): “for presheaves of modules over any category; Stacks' sheaf case is `F.val.Derivation' φ.hom`”. References: EGA IV (16.5.1), “more general”.
- [`PresheafOfModulesOfCommRing.Derivation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModulesOfCommRing.Derivation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L64) (StacksFrontier): “the structure: additive on sections, compatible with restriction, Leibniz rule, kills the image of `φ`”.

## Tag 08RM, a lemma

[Tag 08RM](https://stacks.math.columbia.edu/tag/08RM) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.universalDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L130). References: EGA IV (16.5.3), “(ii)”.

> **Stacks Project, Tag 08RM.** Postcomposition with the universal
> derivation gives the unique morphism from the module of relative
> differentials to any coefficient sheaf.

```lean
theorem universalDerivation_isUniversal {X : TopCat.{u}}
    {O₁ O₂ : TopCat.Sheaf CommRingCat.{max u v} X} (φ : O₁ ⟶ O₂) :
    IsUniversal.{u, v, u_1} (universalDerivation.{u, v, u_1} φ)
```

## Tag 08RP, a definition

[Tag 08RP](https://stacks.math.columbia.edu/tag/08RP) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.moduleOfDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L111). The attribute's comment: “the module of differentials”.

> The sheaf of relative differentials representing derivations along `φ`.

```lean
noncomputable def moduleOfDifferentials {X : TopCat.{u}}
    {O₁ O₂ : TopCat.Sheaf CommRingCat.{max u v} X} (φ : O₁ ⟶ O₂) :
    _root_.SheafOfModules.{max u v w} (underlyingRingSheaf O₂)
```

**`AlgebraicGeometry.SheafOfModules.universalDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L118). The attribute's comment: “the module of differentials”. References: EGA IV (16.3.6), “dt”; EGA IV (16.5.3), “(i)”.

> The universal relative derivation into `moduleOfDifferentials φ`.

```lean
noncomputable def universalDerivation {X : TopCat.{u}}
    {O₁ O₂ : TopCat.Sheaf CommRingCat.{max u v} X} (φ : O₁ ⟶ O₂) :
    SheafDerivation.{u, v, u_1} φ (moduleOfDifferentials.{u, v, u_1} φ)
```

## Tag 08TD, a lemma

[Tag 08TD](https://stacks.math.columbia.edu/tag/08TD) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.SheafOfModules.moduleOfDifferentialsIsoSectionwise`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L217), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Stalk.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Stalk.lean#L89) (StacksFrontier).

## Tag 08RQ, a lemma

[Tag 08RQ](https://stacks.math.columbia.edu/tag/08RQ) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.pullbackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L559). The attribute's comment: “the open-inclusion case: the identification of the restriction of the”.

> The canonical identification between the inverse image of the module of relative
> differentials and the module of relative differentials of the inverse-image morphism.

```lean
noncomputable def pullbackDifferentialsIso (phi : O₁ ⟶ O₂) :
    inverseImageModule f O₂ (moduleOfDifferentials phi) ≅
      moduleOfDifferentials ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi)
```

## Tag 08RR, a lemma

[Tag 08RR](https://stacks.math.columbia.edu/tag/08RR) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.inverseImageDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L456). The attribute's comment: “inverse image of the derivation”.

> The inverse image of a relative derivation, specified by its action on the images of local
> sections under the inverse-image units.

```lean
noncomputable def inverseImageDerivation
    {M : _root_.SheafOfModules.{u} (underlyingRingSheaf O₂)}
    (d : SheafDerivation phi M) :
    {δ : SheafDerivation ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi)
        (inverseImageModule f O₂ M) //
      ∀ (U : (Opens X)ᵒᵖ) (b : O₂.obj.obj U),
        δ.d (((inverseImageRingHom f O₂).hom.app U) b) =
          ((inverseImageModuleUnit f O₂ M).val.app U).hom (d.d b)}
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L483). The attribute's comment: “universality”.

> The inverse image of the universal derivation remains universal.

```lean
theorem inverseImageDerivation_isUniversal (phi : O₁ ⟶ O₂) :
    IsUniversal (inverseImageDerivation f (universalDerivation phi)).val
```

**`AlgebraicGeometry.SheafOfModules.pullbackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L559). The attribute's comment: “canonical identification”.

> The canonical identification between the inverse image of the module of relative
> differentials and the module of relative differentials of the inverse-image morphism.

```lean
noncomputable def pullbackDifferentialsIso (phi : O₁ ⟶ O₂) :
    inverseImageModule f O₂ (moduleOfDifferentials phi) ≅
      moduleOfDifferentials ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi)
```

**`AlgebraicGeometry.SheafOfModules.pullbackDifferentialsIso_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L588). The attribute's comment: “compatibility with universal derivations”.

> The canonical identification carries the inverse image of the universal derivation to the
> universal derivation.

```lean
theorem pullbackDifferentialsIso_compatible (phi : O₁ ⟶ O₂) :
    (inverseImageDerivation f (universalDerivation phi)).val.postcomp
        (pullbackDifferentialsIso f phi).hom.val =
      universalDerivation ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi)
```

**`AlgebraicGeometry.SheafOfModules.pullbackDifferentialsIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/InverseImage.lean#L597). The attribute's comment: “canonicity”.

> Compatibility with universal derivations uniquely characterizes the canonical
> identification.

```lean
theorem pullbackDifferentialsIso_unique (phi : O₁ ⟶ O₂)
    (e : inverseImageModule f O₂ (moduleOfDifferentials phi) ≅
      moduleOfDifferentials ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi))
    (he : (inverseImageDerivation f (universalDerivation phi)).val.postcomp e.hom.val =
      universalDerivation ((TopCat.Sheaf.pullback CommRingCat.{u} f).map phi)) :
    e = pullbackDifferentialsIso f phi
```

## Tag 08TE, a lemma

[Tag 08TE](https://stacks.math.columbia.edu/tag/08TE) in the Stacks Project.

**`Stacks.RelativeDifferentialStalk.stalkModuleOfDifferentialsKaehlerLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeDifferentialStalk/Sheafify.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeDifferentialStalk/Sheafify.lean#L151). The attribute's comment: “the identification”.

> **Stacks Project, Tag 08TE.** The stalk of the sheaf of relative differentials of a
> morphism of sheaves of commutative rings is the module of Kähler differentials of its stalk
> map: `Ω_{O₂/O₁, x} = Ω_{O₂,x / O₁,x}`.
>
> It is also Stacks Tag 01V0 at a point: the sheaf of relative differentials commutes with taking
> stalks.

```lean
public noncomputable def stalkModuleOfDifferentialsKaehlerLinearEquiv (x : X)
    [DecidableEq (OrderDual (TopologicalSpace.OpenNhds x))] :
    letI := algebraStalk φ.hom x
    ToType (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
        (moduleOfDifferentials.{u, u, u} φ).val.presheaf x)
      ≃ₗ[ToType (O₂.presheaf.stalk x)]
      KaehlerDifferential (ToType (O₁.presheaf.stalk x)) (ToType (O₂.presheaf.stalk x))
```

**`Stacks.RelativeDifferentialStalk.stalkModuleOfDifferentialsKaehlerLinearEquiv_germ_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeDifferentialStalk/Sheafify.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeDifferentialStalk/Sheafify.lean#L224). The attribute's comment: “compatibility with the universal derivations”.

> **Stacks Project, Tag 08TE.** The identification of the stalk of the sheaf of relative
> differentials with the Kähler differentials of the stalk map carries universal differentials to
> universal differentials.
>
> The germ at `x` of the universal relative differential of a section of `O₂` over a neighbourhood
> of `x` goes to the universal differential of the germ of that section. This is what makes the
> identification canonical.

```lean
public theorem stalkModuleOfDifferentialsKaehlerLinearEquiv_germ_d (x : X)
    [DecidableEq (OrderDual (TopologicalSpace.OpenNhds x))]
    (i : OrderDual (TopologicalSpace.OpenNhds x)) (a : nhdRing O₂.presheaf i) :
    letI := algebraStalk φ.hom x
    stalkModuleOfDifferentialsKaehlerLinearEquiv φ x
        (TopCat.Presheaf.germ (C := AddCommGrpCat.{u})
          (moduleOfDifferentials.{u, u, u} φ).val.presheaf (nhdOpen i) x (mem_nhdOpen i)
          ((universalDerivation.{u, u, u} φ).d a)) =
      KaehlerDifferential.D (ToType (O₁.presheaf.stalk x)) (ToType (O₂.presheaf.stalk x))
        (O₂.presheaf.germ (nhdOpen i) x (mem_nhdOpen i) a)
```

## Tag 08RS, a lemma

[Tag 08RS](https://stacks.math.columbia.edu/tag/08RS) in the Stacks Project.

**`Stacks.Sheaves.DifferentialsFunctorial.compDeriv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean#L117). The attribute's comment: “the composite of O\_2 -> O\_2' with d is an O\_1-derivation”.

> Given a commutative square of sheaves of commutative rings
> ```
>   O₂ --φ--> O₂'
>   ↑ι        ↑ι'
>   O₁ --ψ--> O₁'
> ```
> and a relative `ι'`-derivation `d'` with values in a sheaf of `O₂'`-modules `F`, the
> composite `d' ∘ φ` is a relative `ι`-derivation with values in `F` regarded as a sheaf of
> `O₂`-modules by restriction of scalars along `φ`.

```lean
noncomputable def compDeriv {F : SheafOfModules.{u} (Differentials.underlyingRingSheaf O₂')}
    (d' : Differentials.SheafDerivation O₁' O₂' ι' F) (φ : O₂ ⟶ O₂') (ψ : O₁ ⟶ O₁')
    (hcomm : ι ≫ φ = ψ ≫ ι') :
    Differentials.SheafDerivation O₁ O₂ ι (restrictAlong φ F)
```

**`Stacks.Sheaves.DifferentialsFunctorial.differentialMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean#L182). The attribute's comment: “the canonical map of O\_2-modules Omega\_\{O\_2/O\_1} -> Omega\_\{O\_2'/O\_1'}”. References: EGA 0 (20.5.2), “(20.5.2.3) map u''”.

> The canonical morphism of sheaves of modules between the sheaves of relative
> differentials attached to a commutative square
> ```
>   O₂ --φ--> O₂'
>   ↑ι        ↑ι'
>   O₁ --ψ--> O₁'
> ```
> of sheaves of commutative rings. It goes from `Ω_{O₂/O₁}` to `Ω_{O₂'/O₁'}` regarded as a
> sheaf of `O₂`-modules by restriction of scalars along `φ`, and is characterized by
> `differentialMap_comp_d`.

```lean
noncomputable def differentialMap (ι : O₁ ⟶ O₂) (ι' : O₁' ⟶ O₂') (φ : O₂ ⟶ O₂')
    (ψ : O₁ ⟶ O₁') (hcomm : ι ≫ φ = ψ ≫ ι') :
    Differentials.moduleOfDifferentials O₁ O₂ ι ⟶
      restrictAlong φ (Differentials.moduleOfDifferentials O₁' O₂' ι')
```

**`Stacks.Sheaves.DifferentialsFunctorial.differentialMap_comp_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean#L201). The attribute's comment: “the characterizing property d(f) |-> d(phi f) on local sections”.

> The characterizing property of `differentialMap`: on local sections it sends `d a` to
> `d' (φ a)`, where `d` and `d'` are the universal derivations of `Ω_{O₂/O₁}` and
> `Ω_{O₂'/O₁'}`.

```lean
theorem differentialMap_comp_d (ι : O₁ ⟶ O₂) (ι' : O₁' ⟶ O₂') (φ : O₂ ⟶ O₂')
    (ψ : O₁ ⟶ O₁') (hcomm : ι ≫ φ = ψ ≫ ι') {U : Cᵒᵖ} (a : O₂.obj.obj U) :
    ((differentialMap ι ι' φ ψ hcomm).val.app U).hom
        ((Differentials.universalDerivation O₁ O₂ ι).d a)
      = (Differentials.universalDerivation O₁' O₂' ι').d ((φ.hom.app U).hom a)
```

**`Stacks.Sheaves.DifferentialsFunctorial.differentialMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean#L212). The attribute's comment: “the canonical map is uniquely characterized by that property”.

> Uniqueness: a morphism of sheaves of modules satisfying the characterizing property of
> `differentialMap` is `differentialMap`.

```lean
theorem differentialMap_unique (ι : O₁ ⟶ O₂) (ι' : O₁' ⟶ O₂') (φ : O₂ ⟶ O₂')
    (ψ : O₁ ⟶ O₁') (hcomm : ι ≫ φ = ψ ≫ ι')
    (β : Differentials.moduleOfDifferentials O₁ O₂ ι ⟶
      restrictAlong φ (Differentials.moduleOfDifferentials O₁' O₂' ι'))
    (hβ : ∀ {U : Cᵒᵖ} (a : O₂.obj.obj U), (β.val.app U).hom
        ((Differentials.universalDerivation O₁ O₂ ι).d a)
      = (Differentials.universalDerivation O₁' O₂' ι').d ((φ.hom.app U).hom a)) :
    β = differentialMap ι ι' φ ψ hcomm
```

**`Stacks.Sheaves.DifferentialsFunctorial.differentialsArrowFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsFunctorial.lean#L326). The attribute's comment: “a functor on the category of arrows of sheaves of rings”.

> **Stacks Project, Tag 08RS.** The relative differentials as a functor on the category of
> arrows of sheaves of commutative rings: an arrow `ι : O₁ ⟶ O₂` is sent to `Ω_{O₂/O₁}` and a
> commutative square to the canonical map `differentialMap`, the identity and composition laws
> being `differentialMap_id` and `differentialMap_comp`.
>
> The target is the total category `ArrowModules` rather than a fixed category of modules,
> because the sheaf of rings over which `Ω_{O₂/O₁}` is linear is `O₂`, which varies with the
> arrow.

```lean
noncomputable def differentialsArrowFunctor :
    CategoryTheory.Arrow (Sheaf J CommRingCat.{u}) ⥤ ArrowModules J
```

## Tag 08TF, a lemma

[Tag 08TF](https://stacks.math.columbia.edu/tag/08TF) in the Stacks Project.

**`Stacks.Sites.Conormal.differentialSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 888](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L888). The attribute's comment: “canonical conormal sequence”.

> The conormal sequence `I/I² ⟶ B ⊗_A Ω_{A/R} ⟶ Ω_{B/R} ⟶ 0`, with its middle and right
> terms expressed by the sheaves of relative differentials that corepresent derivations.

```lean
noncomputable def differentialSequence :
    ShortComplex
      (_root_.SheafOfModules.{max w u v z} (Stacks.SheafOfModules.Tensor.ringSheaf B))
```

**`Stacks.Sites.Conormal.differentialSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 928](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L928). The attribute's comment: “exactness”. References: SGA 3 III (4.25), “exactness of (+)”.

> The transported sequence is exact at the extension of scalars of `Ω_{A/R}`.

```lean
theorem differentialSequence_exact :
    (differentialSequence.{v, u, w, z} J R A B a φ).Exact
```

**`Stacks.Sites.Conormal.differentialSequence_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 936](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L936). The attribute's comment: “surjectivity”. References: SGA 3 III (4.25), “surjectivity in (+)”.

> The transported sequence surjects onto `Ω_{B/R}`.

```lean
theorem differentialSequence_epi :
    Epi (differentialSequence.{v, u, w, z} J R A B a φ).g
```

**`Stacks.Sites.Conormal.differentialSequence_f_class`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 946](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L946). The attribute's comment: “formula on local kernel sections”.

> The left-hand map carries the conormal class of a local section of the kernel to the
> source's `d x ⊗ 1`.

```lean
theorem differentialSequence_f_class (X : Cᵒᵖ) (x : kernelIdeal φ.hom X) :
    ((differentialSequence.{v, u, w, z} J R A B a φ).f.val.app X)
      (conormalClass.{v, u, w, z} J R A B a φ X x) =
      ((_root_.SheafOfModules.pullbackPushforwardAdjunction
        (underlyingRingHomForPullback J A B φ)).unit.app
          (moduleOfDifferentialsOfSite.{v, u, w, z} R A a)).val.app X
        ((universalDerivationOfSite.{v, u, w, z} R A a).d x.1)
```

**`Stacks.Sites.Conormal.differentialSequence_g_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 962](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L962). The attribute's comment: “right map on differentials”.

> The right-hand map carries `d x ⊗ 1` to the universal differential of the image of `x`.

```lean
theorem differentialSequence_g_differential (X : Cᵒᵖ) (x : A.obj.obj X) :
    ((differentialSequence.{v, u, w, z} J R A B a φ).g.val.app X)
      (((_root_.SheafOfModules.pullbackPushforwardAdjunction
        (underlyingRingHomForPullback J A B φ)).unit.app
          (moduleOfDifferentialsOfSite.{v, u, w, z} R A a)).val.app X
        ((universalDerivationOfSite.{v, u, w, z} R A a).d x)) =
      (universalDerivationOfSite.{v, u, w, z} R B (a ≫ φ)).d (φ.hom.app X x)
```

**`Stacks.Sites.Conormal.differentialSequence_g_eq_mapDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L982). The attribute's comment: “canonical right-hand map”.

> Under extension/restriction of scalars, the right-hand map is exactly the canonical map
> on relative differentials attached to the square `R → A → B` by Stacks 08TR.

```lean
theorem differentialSequence_g_eq_mapDifferentials :
    (_root_.SheafOfModules.pullbackPushforwardAdjunction
      (underlyingRingHomForPullback J A B φ)).homEquiv
      (moduleOfDifferentialsOfSite.{v, u, w, z} R A a)
        (moduleOfDifferentialsOfSite.{v, u, w, z} R B (a ≫ φ))
        (differentialSequence.{v, u, w, z} J R A B a φ).g =
      mapDifferentials.{v, u, w, z} a (a ≫ φ) (𝟙 R) φ (by simp)
```

**`Stacks.Sites.Conormal.differentialSequence_f_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L1010). The attribute's comment: “uniqueness of the conormal map”.

> The formula on local conormal classes determines the left-hand map.

```lean
theorem differentialSequence_f_unique
    (g : (differentialSequence.{v, u, w, z} J R A B a φ).X₁ ⟶
      (differentialSequence.{v, u, w, z} J R A B a φ).X₂)
    (hg : ∀ (X : Cᵒᵖ) (x : kernelIdeal φ.hom X),
      g.val.app X (conormalClass.{v, u, w, z} J R A B a φ X x) =
        ((_root_.SheafOfModules.pullbackPushforwardAdjunction
          (underlyingRingHomForPullback J A B φ)).unit.app
            (moduleOfDifferentialsOfSite.{v, u, w, z} R A a)).val.app X
          ((universalDerivationOfSite.{v, u, w, z} R A a).d x.1)) :
    g = (differentialSequence.{v, u, w, z} J R A B a φ).f
```

## Tag 08RT, a definition

[Tag 08RT](https://stacks.math.columbia.edu/tag/08RT) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceDifferentials.SDerivation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L182). The attribute's comment: “S-derivations into an O\_X-module: the set Der\_S(O\_X, F)”. References: EGA IV (16.5.1); SGA 3 VIIA (1.2.0), “more general”.

> `Der_S(𝒪_X, F)`, the type of *`S`-derivations* of a morphism of ringed spaces
> `h : X ⟶ S` with values in a sheaf of `𝒪_X`-modules `F`: a derivation of `𝒪_X` relative to
> `h⁻¹ 𝒪_S`, that is, an `inverseImageStructureMap h`-derivation in the sense of Tag 01UN.

```lean
noncomputable abbrev SDerivation (h : X ⟶ S)
    (F : SheafOfModules.{u} (structureSheafRing X))
```

**`Stacks.Sheaves.RingedSpaceDifferentials.moduleOfDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L190). The attribute's comment: “the sheaf of differentials Omega\_\{X/S} of X over S”.

> The sheaf of relative differentials `Ω_{X/S}` of a morphism of ringed spaces `h : X ⟶ S`:
> the sheaf of differentials of `𝒪_X` relative to `h⁻¹ 𝒪_S`.

```lean
noncomputable def moduleOfDifferentials (h : X ⟶ S) :
    SheafOfModules.{u} (structureSheafRing X)
```

**`Stacks.Sheaves.RingedSpaceDifferentials.universalDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L196). The attribute's comment: “the universal S-derivation d\_\{X/S} with which Omega\_\{X/S} is endowed”.

> The universal relative derivation `d_{X/S} : 𝒪_X ⟶ Ω_{X/S}`.

```lean
noncomputable def universalDerivation (h : X ⟶ S) :
    SDerivation h (moduleOfDifferentials h)
```

## Tag 01UP, a lemma

[Tag 01UP](https://stacks.math.columbia.edu/tag/01UP) in the Stacks Project.

**`Stacks.Sheaves.SquareZeroExtension.sectionsEquivDerivations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SquareZeroExtensionSections.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SquareZeroExtensionSections.lean#L259).

> **Stacks 01UP.** Relative derivations into the square-zero kernel act simply transitively
> on the algebra sections of the extension. Under the resulting bijection, the derivation
> corresponding to `t` is the pointwise difference `t - s`.

```lean
theorem sectionsEquivDerivations {X : TopCat.{u}}
    {B O A : TopCat.Sheaf CommRingCat.{max u v} X}
    (α : B ⟶ O) (β : B ⟶ A) (π : A ⟶ O)
    (s : AlgebraSection α β π)
    (I : SheafOfModules.{max u v w} (underlyingRingSheaf O))
    (hI : SquareZeroKernel α β π s I) :
    ∃ e : AlgebraSection α β π ≃ SheafDerivation α I,
      ∀ (t : AlgebraSection α β π) (U : (Opens X)ᵒᵖ) (a : O.obj.obj U),
        hI.ι U ((e t).d a) = t.hom.hom.app U a - s.hom.hom.app U a
```

## Tag 08RU, a lemma

[Tag 08RU](https://stacks.math.columbia.edu/tag/08RU) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceDifferentials.differentialMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L334).

> The canonical comparison map `c : f^* Ω_{X/S} ⟶ Ω_{X'/S'}` of sheaves of `𝒪_{X'}`-modules
> attached to a commutative diagram of morphisms of ringed spaces
> ```
>   X' --f--> X
>   |         |
>   h'        h
>   v         v
>   S' --g--> S
> ```
> It is the morphism adjoint to `pushforwardDifferentialMap`, and
> `differentialMap_isDifferentialMap` together with `differentialMap_unique` say that it is
> the unique morphism carrying the pullback of `d a` to `d (f^♯ a)` on local sections.

```lean
noncomputable def differentialMap :
    (RingedSpaceModuleAdjunction.modulePullback f).obj (moduleOfDifferentials h) ⟶
      moduleOfDifferentials h'
```

**`AlgebraicGeometry.SheafOfModules.existsUnique_compositeDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L221). The attribute's comment: “composite derivation”.

> The composite of `f^♯` with the pushforward of the universal derivation is an
> `S`-derivation, and it is the unique one whose value on every local section `a` is the
> universal derivation of `f^♯ a`.

```lean
theorem existsUnique_compositeDerivation {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S)
    (hcomm : f ≫ h = h' ≫ g) :
    ∃! D : SheafDerivation (inverseImageStructureMap h)
      ((RingedSpaceModuleAdjunction.modulePushforward f).obj
        (moduleOfDifferentials (inverseImageStructureMap h'))),
      ∀ (U : Opens X.carrier) (a : X.presheaf.obj (.op U)),
        D.d a = (universalDerivation
          (inverseImageStructureMap h')).d ((f.hom.c.app (.op U)).hom a)
```

**`AlgebraicGeometry.SheafOfModules.pushforwardDifferentialMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L288). The attribute's comment: “map to pushforward differentials”.

> The universal map `Ω_{X/S} ⟶ f_* Ω_{X'/S'}`.

```lean
noncomputable def pushforwardDifferentialMap {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S) (hcomm : f ≫ h = h' ≫ g) :
    moduleOfDifferentials (inverseImageStructureMap h) ⟶
      (RingedSpaceModuleAdjunction.modulePushforward f).obj
        (moduleOfDifferentials (inverseImageStructureMap h'))
```

**`AlgebraicGeometry.SheafOfModules.existsUnique_differentialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L314). The attribute's comment: “canonical map and uniqueness”. References: EGA IV (16.4.3), “(16.4.3.6),(16.4.3.7)”.

> The canonical morphism of differentials for a commutative square of ringed spaces exists
> and is uniquely determined by its action on differentials of local sections.

```lean
theorem existsUnique_differentialMap {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S)
    (hcomm : f ≫ h = h' ≫ g) :
    ∃! c : (RingedSpaceModuleAdjunction.modulePullback f).obj
        (moduleOfDifferentials (inverseImageStructureMap h)) ⟶
      moduleOfDifferentials (inverseImageStructureMap h'),
      IsDifferentialMap f h h' c
```

**`AlgebraicGeometry.SheafOfModules.differentialMap_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L360). The attribute's comment: “agreement under adjunction”.

> The pullback map on differentials is adjoint to the canonical map into
> pushforward differentials.

```lean
theorem differentialMap_adjoint {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S)
    (hcomm : f ≫ h = h' ≫ g) :
    (RingedSpaceModuleAdjunction.homEquiv f
      (moduleOfDifferentials (inverseImageStructureMap h'))
      (moduleOfDifferentials (inverseImageStructureMap h)))
        (differentialMap f h h' g hcomm) =
      pushforwardDifferentialMap f h h' g hcomm
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDifferentialMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L562). The attribute's comment: “inverse-image map”.

> The canonical map `f⁻¹Ω_{X/S} ⟶ Ω_{X'/S'}` of `f⁻¹𝒪_X`-modules.
> The target carries its restricted scalar action.

```lean
noncomputable def inverseImageDifferentialMap {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S) (hcomm : f ≫ h = h' ≫ g) :
    inverseImageModule f.hom.base X.sheaf
      (moduleOfDifferentials (inverseImageStructureMap h)) ⟶
        inverseImageDifferentialTarget f h'
```

**`AlgebraicGeometry.SheafOfModules.inverseImageDifferentialMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/Differentials/Functoriality.lean#L574). The attribute's comment: “inverse-image and tensor comparison”.

> The inverse-image differential map is the restriction of the scalar-extended
> map `c_f`, after the canonical tensor-unit map `f⁻¹Ω ⟶ f*Ω`.

```lean
theorem inverseImageDifferentialMap_eq {X' X S' S : RingedSpace.{u, u}}
    (f : X' ⟶ X) (h : X ⟶ S) (h' : X' ⟶ S') (g : S' ⟶ S) (hcomm : f ≫ h = h' ≫ g) :
    inverseImageDifferentialMap f h h' g hcomm =
      inverseImageToPullback f (moduleOfDifferentials (inverseImageStructureMap h)) ≫
      (_root_.SheafOfModules.restrictScalars (inverseImageStructureRingMap f)).map
        (differentialMap f h h' g hcomm)
```

## Tag 01UW, a lemma

[Tag 01UW](https://stacks.math.columbia.edu/tag/01UW) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceDifferentials.differentialMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L464).

> Functoriality, composition: the comparison map of a vertical composite of two commutative
> diagrams of ringed spaces is the composite of the comparison maps, after the canonical
> identification `(f' ≫ f)^* ⟶ f'^* (f^*)`. This is the relation `c_{f ∘ f'} = c_{f'} ∘ (f')^* c_f`
> of Tag 01UW.

```lean
theorem differentialMap_comp :
    differentialMap (f' ≫ f) h h'' (g' ≫ g) hcomm''
      = modulePullbackComparison f f' (moduleOfDifferentials h) ≫
        ((RingedSpaceModuleAdjunction.modulePullback f').map
            (differentialMap f h h' g hcomm) ≫ differentialMap f' h' h'' g' hcomm')
```

## Tag 0H79, a lemma

[Tag 0H79](https://stacks.math.columbia.edu/tag/0H79) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceDifferentials.triangleDifferentials_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 845](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L845). The attribute's comment: “exactness at the right term”. References: EGA IV (16.4.19), “surjectivity on right”.

> The canonical map to relative differentials over `Y` is an epimorphism.

```lean
theorem triangleDifferentials_epi (f : X ⟶ Y) (g : Y ⟶ S) :
    Epi (toRelativeDifferentials f g)
```

**`Stacks.Sheaves.RingedSpaceDifferentials.triangleDifferentials_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean, line 917](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedSpaceDifferentials.lean#L917). The attribute's comment: “exactness at the middle term”. References: EGA IV (16.4.19), “exactness at middle”.

> For morphisms of ringed spaces `f : X ⟶ Y` and `g : Y ⟶ S` the canonical maps form a complex
> `f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y}` which is exact at `Ω_{X/S}`. Together with
> `triangleDifferentials_epi` this is the exactness of `f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0`.

```lean
theorem triangleDifferentials_exact (f : X ⟶ Y) (g : Y ⟶ S) :
    ∃ h : differentialMap f g (f ≫ g) (𝟙 S) (by simp) ≫ toRelativeDifferentials f g = 0,
      (ShortComplex.mk _ _ h).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.28, Tag 08RL](https://stacks.math.columbia.edu/tag/08RL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
