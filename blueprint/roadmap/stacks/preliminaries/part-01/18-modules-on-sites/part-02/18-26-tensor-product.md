---
declaration: section
origin: cited
lean: PresheafOfModules.sheafificationTensorIso, PresheafOfModules.sheafificationTensorIso_hom_unit_tmul, Stacks.SheafOfModules.pullbackTensorIso, Stacks.Sheaves.RingedPoint.RingedPointSituation.stalkTensorIso, Stacks.SheafOfModules.RingedToposPullback.pullbackCoherence, CategoryTheory.SimplicialSiteSituation.componentRestrictionTensorTotalIso, AlgebraicGeometry.Space.modulePullbackTensorIso, Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isCoherentOnSite
statement: formalized
proof: formalized
---

# 18.26 Tensor product

Section 18.26 of the Stacks Project, [Tag 03EK](https://stacks.math.columbia.edu/tag/03EK). 3 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GMW, a lemma

[Tag 0GMW](https://stacks.math.columbia.edu/tag/0GMW) in the Stacks Project.

**`PresheafOfModules.sheafificationTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean, line 994](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean#L994).

> Sheafification commutes with the tensor product of presheaves of modules: there is an
> isomorphism `F⁺ ⊗_{O⁺} G⁺ ≅ (F ⊗_{p,O} G)⁺`, natural in both presheaves of modules, where the
> left-hand tensor product is the sheafification of the objectwise tensor product of the two sheaves
> of sections.

```lean
noncomputable def sheafificationTensorIso :
    Functor.prod (moduleSheafification.{v, u, w, z} J a)
          (moduleSheafification.{v, u, w, z₁} J a) ⋙
        (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, z, z₁} Osharp)) ≅
      Functor.uncurry.obj (tensorBifunctor.{v, u, w, z, z₁} O) ⋙
        moduleSheafification.{v, u, w, max z z₁} J a
```

**`PresheafOfModules.sheafificationTensorIso_hom_unit_tmul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean, line 1019](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean#L1019).

> The isomorphism `sheafificationTensorIso` sends the image, under the unit exhibiting the tensor
> product sheaf as a sheafification, of a pure tensor of two sheafification-unit images to the
> sheafification-unit image of the original pure tensor.

```lean
lemma sheafificationTensorIso_hom_unit_tmul (U : Cᵒᵖ) (x : F.obj U) (y : G.obj U) :
    Hom.app ((sheafificationTensorIso.{v, u, w, z, z₁} J a).hom.app (F, G)).val U
        (Hom.app ((PresheafOfModules.sheafificationAdjunction
            (R := Stacks.SheafOfModules.Tensor.ringSheaf Osharp)
            (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf Osharp).obj)).unit.app
            (tensorObj (((moduleSheafification.{v, u, w, z} J a).obj F)).val
              (((moduleSheafification.{v, u, w, z₁} J a).obj G)).val)) U
          (Hom.app (moduleSheafificationUnit.{v, u, w, z} J a F) U x ⊗ₜ
            Hom.app (moduleSheafificationUnit.{v, u, w, z₁} J a G) U y)) =
      Hom.app (moduleSheafificationUnit.{v, u, w, max z z₁} J a (tensorObj F G)) U (x ⊗ₜ y)
```

## Tag 03EL, a lemma

[Tag 03EL](https://stacks.math.columbia.edu/tag/03EL) in the Stacks Project.

**`Stacks.SheafOfModules.pullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensor.lean, line 1006](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensor.lean#L1006). References: SGA 4 IV (13.4), “special case”.

> **Stacks 03EL.** For a morphism of ringed topoi
> `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)`, the pullback of a tensor product of sheaves of
> `O_D`-modules is the tensor product of their pullbacks,
>
> `f^*(F ⊗_{O_D} G) ≅ f^*F ⊗_{O_C} f^*G`,
>
> naturally in `F` and in `G`. The comparison is the one determined by the chain of bijections
> `Stacks.SheafOfModules.pullbackTensorHomEquiv`, whose naturality in the sheaf of values turns it
> into a morphism of sheaves of modules and whose naturality in `F` and `G` makes that morphism a
> natural transformation.

```lean
def pullbackTensorIso :
    (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'} Y.O)) ⋙
        f.pullbackModules ≅
      Functor.prod (f.pullbackModules) (f.pullbackModules) ⋙
        (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} X.O))
```

**`Stacks.Sheaves.RingedPoint.RingedPointSituation.stalkTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointStalkTensor.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedPointStalkTensor.lean#L90). The attribute's comment: “the stalk at a point of a ringed topos commutes with the tensor product”.

> **The stalk commutes with the tensor product of sheaves of modules.** At a point `p` of a
> ringed topos `(Sh(C), O)` the module-valued stalk carries a tensor product of sheaves of
> `O`-modules to the tensor product of the stalks over `O_p`,
>
> `(F ⊗_O G)_p ≅ F_p ⊗_{O_p} G_p`,
>
> naturally in `F` and in `G`. This is Tag 03EL — the compatibility of pullback with the tensor
> product along a morphism of ringed topoi — read along the morphism out of the ringed point of
> Section 18.37, whose pullback on modules is the stalk
> (`RingedPointSituation.pullbackStalkIso`).

```lean
def stalkTensorIso :
    (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor X.O)) ⋙ s.stalkModules ≅
      Functor.prod s.stalkModules s.stalkModules ⋙
        (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor s.point.O))
```

**`Stacks.SheafOfModules.RingedToposPullback.pullbackCoherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackCoherence.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposPullbackCoherence.lean#L79). The attribute's comment: “the comparison of the pullback with the tensor product is a monoidal structure: the three coherences”.

> **The coherence of Tag 03EL, proved.** The comparison
> `f^*(F ⊗_{O_D} G) ≅ f^*F ⊗_{O_C} f^*G` is compatible with the associator and with both unitors,
> the unit object being matched by `ν : f^*O_D ≅ O_C`. The three fields are
> `Stacks.SheafOfModules.RingedToposPullback.associativity`, `leftUnitality` and `rightUnitality`;
> there is no hypothesis, and the four universes of the two ringed topoi stay independent.

```lean
theorem pullbackCoherence : PullbackCoherence f
```

**`CategoryTheory.SimplicialSiteSituation.componentRestrictionTensorTotalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean#L97). The attribute's comment: “on total complexes, for restriction to a simplicial component”.

> **Stacks 03EL on total complexes, at the component inclusion.** Restriction to the degree-`n`
> component commutes with the total tensor complex:
> `g_n^*Tot(K ⊗_O L) ≅ Tot(g_n^*K ⊗_{O_n} g_n^*L)`, the comparison on the summand of bidegree
> `(p, q)` being `g_n^*(K^p ⊗_O L^q) ≅ g_n^*K^p ⊗_{O_n} g_n^*L^q`.

```lean
def componentRestrictionTensorTotalIso
    (K L : CochainComplex (S.totalRingedTopos O).Modules ℤ) :
    (S.componentModulesRestrictionComplex O n).obj
        (HomologicalComplex.mapBifunctor K L
          (Stacks.SheafOfModules.Tensor.sheafTensor (S.totalRingedTopos O).O)
          (ComplexShape.up ℤ)) ≅
      HomologicalComplex.mapBifunctor ((S.componentModulesRestrictionComplex O n).obj K)
        ((S.componentModulesRestrictionComplex O n).obj L)
        (Stacks.SheafOfModules.Tensor.sheafTensor (S.componentRingedTopos O n).O)
        (ComplexShape.up ℤ)
```

**`AlgebraicGeometry.Space.modulePullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackTensor.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackTensor.lean#L66). The attribute's comment: “for the small étale ringed topoi of a morphism of algebraic spaces”.

> **Stacks 03EL for a morphism of algebraic spaces.** The inverse image of a tensor product of
> `𝒪_Y`-modules along `f : X ⟶ Y` is the tensor product of the inverse images,
> `f^*(G ⊗_{𝒪_Y} G') ≅ f^*G ⊗_{𝒪_X} f^*G'`.
>
> `AlgebraicGeometry.Space.modulePullback` is the inverse image of modules of the morphism of small
> étale ringed topoi of Stacks 03G8, so this is `Stacks.SheafOfModules.pullbackTensorIso` at that
> morphism, with the tensor product sheaf matched with the monoidal product by
> `AlgebraicGeometry.Space.modulesTensorObjIso` on each side.

```lean
noncomputable def modulePullbackTensorIso (f : X ⟶ Y)
    (G G' : Modules.{u, u} B S hS Y.1 Y.2) :
    (modulePullback B S hS f).obj (G ⊗ G') ≅
      (modulePullback B S hS f).obj G ⊗ (modulePullback B S hS f).obj G'
```

## Tag 03L6, a lemma

[Tag 03L6](https://stacks.math.columbia.edu/tag/03L6) in the Stacks Project.

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isCoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorCoherentOnSite.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorCoherentOnSite.lean#L70). The attribute's comment: “coherent”. References: EGA I (9.1.1), “coherent tensor”; EGA 0 (5.3.5), “tensor product”.

> **Stacks Project, Tag 03L6, coherent case.**  The tensor product of two coherent sheaves of
> modules on a ringed site is coherent.
>
> Following the source: a coherent sheaf of modules is of finite presentation, so the mixed
> finite-presentation/coherence clause applies.  The argument is run at the universe lift of the
> ringed site, where the presentation machinery of Stacks 01BW(1) is available, and transported
> back along `Stacks.SheafOfModules.CoherentLift.isCoherentOnSite_liftModule_iff` and
> `Stacks.SheafOfModules.CoherentLift.tensorLiftIso`.

```lean
theorem tensorSheaf_isCoherentOnSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    [hF : _root_.SheafOfModules.IsCoherentOnSite F]
    [hG : _root_.SheafOfModules.IsCoherentOnSite G] :
    _root_.SheafOfModules.IsCoherentOnSite
      (((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFiniteness.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFiniteness.lean#L307). The attribute's comment: “finite\_type”.

> **Stacks Project, Tag 03L6, finite type case.** The tensor product of two sheaves of
> modules of finite type on a ringed site is of finite type.

```lean
theorem tensorSheaf_isFiniteType (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    [_root_.SheafOfModules.IsFiniteType F] [_root_.SheafOfModules.IsFiniteType G] :
    _root_.SheafOfModules.IsFiniteType
      (((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isLocallyGeneratedBySectionsOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFiniteness.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFiniteness.lean#L345). The attribute's comment: “locally\_generated”.

> **Stacks Project, Tag 03L6, locally generated case.** The tensor product of two sheaves of
> modules locally generated by sections on a ringed site is locally generated by sections.

```lean
theorem tensorSheaf_isLocallyGeneratedBySectionsOnSite
    (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : _root_.SheafOfModules.IsLocallyGeneratedBySectionsOnSite F)
    (hG : _root_.SheafOfModules.IsLocallyGeneratedBySectionsOnSite G) :
    _root_.SheafOfModules.IsLocallyGeneratedBySectionsOnSite
      (((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFinitePresentation.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFinitePresentation.lean#L142). The attribute's comment: “finite\_presentation”.

> **Stacks Project, Tag 03L6, finite presentation case.** The tensor product of two sheaves of
> modules of finite presentation on a ringed site is of finite presentation.
>
> Following the source: `F` has a finite presentation over each member of a covering family and so
> does `G`; the objects admitting an arrow into a member of each family again cover, and over such
> an object the two restricted presentations are still finite and their tensor presentation
> presents the restriction of `F ⊗ G`.

```lean
theorem tensorSheaf_isFinitePresentation
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    [SheafOfModules.IsFinitePresentation F] [SheafOfModules.IsFinitePresentation G] :
    SheafOfModules.IsFinitePresentation
      (((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isCoherent_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFinitePresentationCoherence.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorFinitePresentationCoherence.lean#L191). The attribute's comment: “fp\_tensor\_coherent”.

> **Stacks Project, Tag 03L6, finite presentation against coherence.**  The tensor product of
> a sheaf of modules of finite presentation with a coherent sheaf of modules on a ringed site is
> coherent.
>
> Following the source: `F` admits a finite presentation over each member of a covering family,
> the restriction of `G` to such a member is still coherent, and the tensor product formed on the
> slice site is the restriction of the global one by
> `Stacks.SheafOfModules.TensorLocalProperties.tensorOverIso`; so
> `isCoherentOnSite_tensorSheaf_of_presentation` applies on each member, and coherence is local on
> the site.

```lean
theorem tensorSheaf_isCoherent_of_isFinitePresentation
    (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    [_root_.SheafOfModules.IsFinitePresentation F]
    [hG : _root_.SheafOfModules.IsCoherentOnSite G] :
    _root_.SheafOfModules.IsCoherentOnSite
      (((Stacks.SheafOfModules.Tensor.sheafTensor X.O).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isLocallyFreeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorLocallyFree.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorLocallyFree.lean#L562). The attribute's comment: “locally\_free”.

> **Stacks Project, Tag 03L6, part (1).** The tensor product of two locally free sheaves of
> modules on a ringed site is locally free.

```lean
theorem tensorSheaf_isLocallyFreeOnSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : SheafOfModules.IsLocallyFreeOnSite F)
    (hG : SheafOfModules.IsLocallyFreeOnSite G) :
    SheafOfModules.IsLocallyFreeOnSite
      (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor X.O))).obj
        (F, G))
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isFiniteLocallyFreeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorLocallyFree.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorLocallyFree.lean#L580). The attribute's comment: “finite\_locally\_free”.

> **Stacks Project, Tag 03L6, part (2).** The tensor product of two finite locally free
> sheaves of modules on a ringed site is finite locally free.

```lean
theorem tensorSheaf_isFiniteLocallyFreeOnSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    (F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : SheafOfModules.IsFiniteLocallyFreeOnSite F)
    (hG : SheafOfModules.IsFiniteLocallyFreeOnSite G) :
    SheafOfModules.IsFiniteLocallyFreeOnSite
      (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor X.O))).obj
        (F, G))
```

**`Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorQuasicoherentOnSite.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorQuasicoherentOnSite.lean#L108). The attribute's comment: “quasi\_coherent”. References: EGA I (9.1.1), “more general”.

> **Stacks Project, Tag 03L6, quasi-coherent case.** The tensor product of two quasi-coherent
> sheaves of modules on a ringed site is quasi-coherent.

```lean
theorem tensorSheaf_isQuasicoherentOnSite (R : Sheaf J CommRingCat.{w})
    (F G : SheafOfModules.{w} (CategoryTheory.Sheaf.toRingCat J R))
    [SheafOfModules.IsQuasicoherentOnSite F] [SheafOfModules.IsQuasicoherentOnSite G] :
    SheafOfModules.IsQuasicoherentOnSite
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} R).obj F).obj G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.26, Tag 03EK](https://stacks.math.columbia.edu/tag/03EK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
