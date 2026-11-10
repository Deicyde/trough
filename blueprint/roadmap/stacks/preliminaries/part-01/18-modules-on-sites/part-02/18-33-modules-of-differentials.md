---
declaration: section
origin: cited
lean: PresheafOfModulesOfCommRing.Derivation', Stacks.Sheaves.Differentials.universalDerivation_isUniversal, AlgebraicGeometry.SheafOfModules.existsUnique_descDerivation, AlgebraicGeometry.SheafOfModules.derivationsFunctor_isCorepresentable, AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap, AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_additive, AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_leibniz, AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_base
statement: formalized
proof: formalized
---

# 18.33 Modules of differentials

Section 18.33 of the Stacks Project, [Tag 04BJ](https://stacks.math.columbia.edu/tag/04BJ). 12 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04BK, a definition

[Tag 04BK](https://stacks.math.columbia.edu/tag/04BK) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModulesOfCommRing.Derivation'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModulesOfCommRing.Derivation'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch18.lean#L71) (StacksFrontier): “for the underlying presheaves of rings and of modules”. References: EGA IV (16.5.1), “more general”.

## Tag 04BL, a lemma

[Tag 04BL](https://stacks.math.columbia.edu/tag/04BL) in the Stacks Project.

**`Stacks.Sheaves.Differentials.universalDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsRepresentable.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialsRepresentable.lean#L115).

> Every relative derivation with values in a sheaf of modules factors through the universal
> derivation by a unique morphism of sheaves of modules.

```lean
theorem universalDerivation_isUniversal
    (F : SheafOfModules.{u} (underlyingRingSheaf O₂))
    (D : SheafDerivation O₁ O₂ φ F) :
    ∃! f : moduleOfDifferentials O₁ O₂ φ ⟶ F,
      (universalDerivation O₁ O₂ φ).postcomp f.val = D
```

**`AlgebraicGeometry.SheafOfModules.existsUnique_descDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L138). The attribute's comment: “unique-factorization form, on an arbitrary site”.

> **Stacks 04BL**, in unique-factorization form: every relative derivation with values in a
> sheaf of modules factors through the universal derivation by a unique morphism of sheaves of
> modules.

```lean
theorem existsUnique_descDerivation
    (F : _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂))
    (D : PresheafOfModulesOfCommRing.Derivation' F.val φ.hom) :
    ∃! f : moduleOfDifferentialsOfSite.{v, u, w, m} O₁ O₂ φ ⟶ F,
      (universalDerivationOfSite.{v, u, w, m} O₁ O₂ φ).postcomp f.val = D
```

**`AlgebraicGeometry.SheafOfModules.derivationsFunctor_isCorepresentable`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Differentials.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Differentials.lean#L366).

> For a homomorphism of sheaves of commutative rings, the functor
> sending a sheaf of modules to the type of relative derivations is represented by a sheaf
> of modules.

```lean
instance derivationsFunctor_isCorepresentable {C : Type u₁} [Category.{v₁} C]
    {J : GrothendieckTopology C}
    [J.HasSheafCompose (forget₂ CommRingCat.{u} RingCat.{u})]
    (O₁ O₂ : Sheaf J CommRingCat.{u}) (φ : O₁ ⟶ O₂) :
    (derivationsFunctor.{v} O₁ O₂ φ).IsCorepresentable
```

## Tag 04BM, an equation

[Tag 04BM](https://stacks.math.columbia.edu/tag/04BM) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean#L160).

> The map
> `O₂[O₂ × O₂] ⊕ O₂[O₂ × O₂] ⊕ O₂[O₁] ⟶ O₂[O₂]`
> whose three components send generators respectively to
> `[a+b]-[a]-[b]`, `[fg]-g[f]-f[g]`, and `[φ(h)]`.
>
> Here every free module presheaf and the displayed morphism have been sheafified.

```lean
noncomputable def moduleDifferentialsRelationMap
    (O₁ O₂ : Sheaf J RingCat.{u}) (φ : O₁ ⟶ O₂)
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify J AddCommGrpCat.{u}] :
    (sheafification (𝟙 O₂.obj)).obj
      ((freeObj (R := O₂.obj) (ringElementPairs O₂) ⨿
        freeObj (R := O₂.obj) (ringElementPairs O₂)) ⨿
        freeObj (R := O₂.obj) (ringElements O₁)) ⟶
    (sheafification (𝟙 O₂.obj)).obj
      (freeObj (R := O₂.obj) (ringElements O₂))
```

**`AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean#L205). The attribute's comment: “additive summand”.

> The additive summand sends `[(a,b)]` to `[a+b]-[a]-[b]`.

```lean
theorem moduleDifferentialsRelationMap_additive
    (O₁ O₂ : Sheaf J RingCat.{u}) (φ : O₁ ⟶ O₂)
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify J AddCommGrpCat.{u}]
    (X : Cᵒᵖ) (a b : O₂.obj.obj X) :
    ((sheafificationHomEquiv (𝟙 O₂.obj)
      ((sheafification (𝟙 O₂.obj)).map (coprod.inl ≫ coprod.inl) ≫
        moduleDifferentialsRelationMap O₁ O₂ φ)).app X) (ModuleCat.freeMk (a, b)) =
      sheafifiedFreeGenerator O₂ (ringElements O₂) X (a + b) -
        sheafifiedFreeGenerator O₂ (ringElements O₂) X a -
        sheafifiedFreeGenerator O₂ (ringElements O₂) X b
```

**`AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_leibniz`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean#L224). The attribute's comment: “Leibniz summand”.

> The multiplicative summand sends `[(f,g)]` to `[fg]-g[f]-f[g]`.

```lean
theorem moduleDifferentialsRelationMap_leibniz
    (O₁ O₂ : Sheaf J RingCat.{u}) (φ : O₁ ⟶ O₂)
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify J AddCommGrpCat.{u}]
    (X : Cᵒᵖ) (f g : O₂.obj.obj X) :
    ((sheafificationHomEquiv (𝟙 O₂.obj)
      ((sheafification (𝟙 O₂.obj)).map (coprod.inr ≫ coprod.inl) ≫
        moduleDifferentialsRelationMap O₁ O₂ φ)).app X) (ModuleCat.freeMk (f, g)) =
      sheafifiedFreeGenerator O₂ (ringElements O₂) X (f * g) -
        g • sheafifiedFreeGenerator O₂ (ringElements O₂) X f -
        f • sheafifiedFreeGenerator O₂ (ringElements O₂) X g
```

**`AlgebraicGeometry.SheafOfModules.moduleDifferentialsRelationMap_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RecoveryAux/ModuleDifferentialsRelationMap.lean#L243). The attribute's comment: “base-ring summand”.

> The base-ring summand sends `[h]` to `[φ(h)]`.

```lean
theorem moduleDifferentialsRelationMap_base
    (O₁ O₂ : Sheaf J RingCat.{u}) (φ : O₁ ⟶ O₂)
    [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    [HasWeakSheafify J AddCommGrpCat.{u}]
    (X : Cᵒᵖ) (h : O₁.obj.obj X) :
    ((sheafificationHomEquiv (𝟙 O₂.obj)
      ((sheafification (𝟙 O₂.obj)).map coprod.inr ≫
        moduleDifferentialsRelationMap O₁ O₂ φ)).app X) (ModuleCat.freeMk h) =
      sheafifiedFreeGenerator O₂ (ringElements O₂) X (φ.hom.app X h)
```

## Tag 04BN, a definition

[Tag 04BN](https://stacks.math.columbia.edu/tag/04BN) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.moduleOfDifferentialsOfSite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L121). The attribute's comment: “the module of differentials `Ω_{O₂/O₁}`”.

> The sheaf of relative differentials `Ω_{O₂/O₁}`: the sheaf of modules corepresenting the
> functor of relative derivations.

```lean
noncomputable abbrev moduleOfDifferentialsOfSite :
    _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂)
```

**`AlgebraicGeometry.SheafOfModules.universalDerivationOfSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L129). The attribute's comment: “the module of differentials `Ω_{O₂/O₁}`”. References: EGA IV (16.3.6), “dt”; EGA IV (16.5.3), “(i)”.

> The universal relative derivation with values in `Ω_{O₂/O₁}`.

```lean
noncomputable def universalDerivationOfSite :
    PresheafOfModulesOfCommRing.Derivation' (moduleOfDifferentialsOfSite.{v, u, w, m} O₁ O₂ φ).val
      φ.hom
```

## Tag 08TP, a lemma

[Tag 08TP](https://stacks.math.columbia.edu/tag/08TP) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.differentialsSheafificationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsSheafification.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsSheafification.lean#L396). The attribute's comment: “isomorphism”.

> **Stacks Project, Tag 08TP.** Relative differentials commute with passing from presheaves
> of commutative rings to their associated sheaves: the sheaf of differentials of `O₂^#` over
> `O₁^#` is canonically the sheaf associated to the presheaf `X ↦ Ω[O₂(X)⁄O₁(X)]`.

```lean
noncomputable def differentialsSheafificationIso (O₁ O₂ : Cᵒᵖ ⥤ CommRingCat.{u})
    (f : O₁ ⟶ O₂) :
    (derivationsFunctor.{v} (associatedCommRingSheaf J O₁) (associatedCommRingSheaf J O₂)
        (associatedCommRingSheafMap J f)).coreprX ≅
      sheafifiedObjectwiseDifferentials.{v, v₁} J f
```

**`AlgebraicGeometry.SheafOfModules.differentialsSheafificationIso_inv_unit_d`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsSheafification.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsSheafification.lean#L409). The attribute's comment: “canonicality”.

> **Stacks Project, Tag 08TP**, the canonicality of the comparison: the inverse of
> `differentialsSheafificationIso` carries the image of the objectwise universal differential
> `d b` to the sheaf-level universal derivation evaluated on the image of `b`.

```lean
lemma differentialsSheafificationIso_inv_unit_d (O₁ O₂ : Cᵒᵖ ⥤ CommRingCat.{u})
    (f : O₁ ⟶ O₂) (X : Cᵒᵖ) (b : O₂.obj X) :
    ((differentialsSheafificationIso.{v, v₁} J O₁ O₂ f).inv.val.app X)
        (objectwiseDifferentialInSheafification.{v, v₁} J f X b) =
      (derivationsFunctor.{v} (associatedCommRingSheaf J O₁) (associatedCommRingSheaf J O₂)
        (associatedCommRingSheafMap J f)).coreprx.d
          ((toAssociatedRingSheaf J O₂).app X b)
```

**`AlgebraicGeometry.SheafOfModules.isIso_objectwiseDifferentialsSheafificationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean#L134). The attribute's comment: “for sheaves of rings, as an isomorphism out of the sheafification”.

> The sheafification of the objectwise Kähler differentials is the sheaf of relative
> differentials: `objectwiseDifferentialsSheafificationHom` is an isomorphism.

```lean
theorem isIso_objectwiseDifferentialsSheafificationHom :
    IsIso (objectwiseDifferentialsSheafificationHom.{v} O₁ O₂ φ)
```

**`AlgebraicGeometry.SheafOfModules.isLocallyInjective_objectwiseDifferentialsToSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean#L193). The attribute's comment: “for sheaves of rings, local injectivity”.

> **Stacks 08TP**, injectivity half: the comparison from the objectwise Kähler differentials
> to the sheaf of relative differentials is locally injective.

```lean
theorem isLocallyInjective_objectwiseDifferentialsToSheaf :
    PresheafOfModules.IsLocallyInjective J (objectwiseDifferentialsToSheaf.{v} O₁ O₂ φ)
```

**`AlgebraicGeometry.SheafOfModules.isLocallySurjective_objectwiseDifferentialsToSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ObjectwiseDifferentialsLocallyBijective.lean#L207). The attribute's comment: “for sheaves of rings, local surjectivity”.

> **Stacks 08TP**, surjectivity half: the comparison from the objectwise Kähler differentials
> to the sheaf of relative differentials is locally surjective.

```lean
theorem isLocallySurjective_objectwiseDifferentialsToSheaf :
    PresheafOfModules.IsLocallySurjective J (objectwiseDifferentialsToSheaf.{v} O₁ O₂ φ)
```

## Tag 08TQ, a lemma

[Tag 08TQ](https://stacks.math.columbia.edu/tag/08TQ) in the Stacks Project.

**`Stacks.Sheaves.Differentials.pullbackDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean#L590). The attribute's comment: “the canonical identification, with the morphism of topoi presented by a continuous functor of the underlying sites, both sites small in the single universe of the sections of the sheaves of rings and of the modules, and the inverse image of sheaves of commutative rings assumed to exist”.

> **Stacks Project, Tag 08TQ.** For a morphism of topoi presented by a continuous functor of
> the underlying sites, the inverse image of the sheaf of relative differentials is canonically
> the sheaf of relative differentials of the inverse-image morphism of sheaves of rings.

```lean
noncomputable def pullbackDifferentialsIso :
    inverseImageModule J K F O₂ (moduleOfDifferentials O₁ O₂ φ) ≅
      moduleOfDifferentials (inverseImageRing J K F O₁) (inverseImageRing J K F O₂)
        ((F.sheafPullback CommRingCat.{u} J K).map φ)
```

**`Stacks.Sheaves.Differentials.pullbackDifferentialsIso_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean#L624). The attribute's comment: “compatibility with universal derivations”.

> **Stacks Project, Tag 08TQ.** The canonical identification carries the inverse image of the
> universal derivation to the universal derivation.

```lean
theorem pullbackDifferentialsIso_compatible :
    (inverseImageDerivation J K F φ (moduleOfDifferentials O₁ O₂ φ)
          (universalDerivation O₁ O₂ φ)).postcomp
        (pullbackDifferentialsIso J K F φ).hom.val =
      universalDerivation (inverseImageRing J K F O₁) (inverseImageRing J K F O₂)
        ((F.sheafPullback CommRingCat.{u} J K).map φ)
```

**`Stacks.Sheaves.Differentials.pullbackDifferentialsIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsInverseImage.lean#L635). The attribute's comment: “canonicity”.

> **Stacks Project, Tag 08TQ.** Compatibility with universal derivations characterises the
> canonical identification.

```lean
theorem pullbackDifferentialsIso_unique
    (e : inverseImageModule J K F O₂ (moduleOfDifferentials O₁ O₂ φ) ≅
      moduleOfDifferentials (inverseImageRing J K F O₁) (inverseImageRing J K F O₂)
        ((F.sheafPullback CommRingCat.{u} J K).map φ))
    (he : (inverseImageDerivation J K F φ (moduleOfDifferentials O₁ O₂ φ)
        (universalDerivation O₁ O₂ φ)).postcomp e.hom.val =
      universalDerivation (inverseImageRing J K F O₁) (inverseImageRing J K F O₂)
        ((F.sheafPullback CommRingCat.{u} J K).map φ)) :
    e = pullbackDifferentialsIso J K F φ
```

**`Stacks.Sheaves.RingedToposModules.inverseImageDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/InverseImageDerivations.lean, line 964](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/InverseImageDerivations.lean#L964). The attribute's comment: “for an arbitrary morphism of topoi, with the object, arrow and section universes of the two sites independent”.

> **Stacks 08TQ.** The inverse image of the sheaf of relative differentials of a homomorphism
> of sheaves of commutative rings along a morphism of topoi is the sheaf of relative differentials
> of the inverse image: `f⁻¹Ω_{P/A} ≅ Ω_{f⁻¹P/f⁻¹A}`.

```lean
noncomputable def inverseImageDifferentialsIso :
    inverseImageDifferentials f a ≅
      moduleOfDifferentialsOfSite.{v, u, max u v w, max u v w}
        (f.inverseImageRing.obj A) (f.inverseImageRing.obj P) (f.inverseImageRing.map a)
```

**`Stacks.Sheaves.RingedToposModules.homEquiv_inverseImageDifferentialsIso_hom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/InverseImageDerivations.lean, line 976](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/InverseImageDerivations.lean#L976). The attribute's comment: “compatibility with the universal derivations”.

> **Stacks 08TQ.** The identification is the one carrying the inverse image of the universal
> derivation of `Ω_{P/A}` to the universal derivation of `Ω_{f⁻¹P/f⁻¹A}`: transposing it along
> `f⁻¹ ⊣ f_*` and the universal property of `Ω_{P/A}` returns the universal derivation.

```lean
lemma homEquiv_inverseImageDifferentialsIso_hom :
    (inverseImageDifferentialsCorepresentableBy f a).homEquiv
        (inverseImageDifferentialsIso f a).hom =
      universalDerivationOfSite.{v, u, max u v w, max u v w}
        (f.inverseImageRing.obj A) (f.inverseImageRing.obj P) (f.inverseImageRing.map a)
```

## Tag 04BO, a lemma

[Tag 04BO](https://stacks.math.columbia.edu/tag/04BO) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.overDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/Differentials.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/Differentials.lean#L340). The attribute's comment: “the canonical isomorphism, with the object, arrow and section universes of the site independent”.

> **Stacks 04BO.** For a homomorphism `φ : O₁ ⟶ O₂` of sheaves of commutative rings on a site
> and an object `U` of that site, the restriction of the sheaf of relative differentials to the
> slice site over `U` is the sheaf of relative differentials of the restrictions:
> `Ω_{O₂/O₁}|_U ≅ Ω_{(O₂|_U)/(O₁|_U)}`.

```lean
noncomputable def overDifferentialsIso :
    (moduleOfDifferentialsOfSite.{v, u, max u v w, max u v w} O₁ O₂ φ).over U ≅
      moduleOfDifferentialsOfSite.{v, max u v, max u v w, max u v w}
        (O₁.over U) (O₂.over U) ((J.overPullback CommRingCat.{max u v w} U).map φ)
```

**`AlgebraicGeometry.SheafOfModules.homEquiv_overDifferentialsIso_hom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/Differentials.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/Differentials.lean#L354). The attribute's comment: “compatibility with the universal derivations”.

> **Stacks 04BO.** The identification is the one carrying the restriction of the universal
> derivation of `Ω_{O₂/O₁}` to the universal derivation of `Ω_{(O₂|_U)/(O₁|_U)}`: transposing it
> along the corepresentation of
> `AlgebraicGeometry.SheafOfModules.overDifferentialsCorepresentableBy` returns that universal
> derivation.

```lean
lemma homEquiv_overDifferentialsIso_hom :
    (overDifferentialsCorepresentableBy.{w} J U φ).homEquiv
        (overDifferentialsIso.{w} J U φ).hom =
      universalDerivationOfSite.{v, max u v, max u v w, max u v w}
        (O₁.over U) (O₂.over U) ((J.overPullback CommRingCat.{max u v w} U).map φ)
```

## Tag 08TR, a lemma

[Tag 08TR](https://stacks.math.columbia.edu/tag/08TR) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.functorialDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean#L115). The attribute's comment: “the canonical map and uniqueness”.

> **Stacks 08TR.** The canonical morphism on sheaves of relative differentials associated to a
> commutative square, together with its characterisation on local differentials.

```lean
noncomputable def functorialDifferentials {O₁ O₂ O₁' O₂' : Sheaf J CommRingCat.{w}}
    (a : O₁ ⟶ O₂) (a' : O₁' ⟶ O₂') (f₁ : O₁ ⟶ O₁') (f₂ : O₂ ⟶ O₂')
    (sq : a ≫ f₂ = f₁ ≫ a') :
    DifferentialsMapData.{v, u, w, m} a a' f₁ f₂ sq
```

**`AlgebraicGeometry.SheafOfModules.mapDifferentials_id_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean#L183). The attribute's comment: “identity law”.

> The canonical map on differentials associated to the identity square is the identity on
> every local section.

```lean
theorem mapDifferentials_id_apply {O₁ O₂ : Sheaf J CommRingCat.{w}} (a : O₁ ⟶ O₂)
    (X : Cᵒᵖ) (x : (moduleOfDifferentialsOfSite.{v, u, w, m} O₁ O₂ a).val.obj X) :
    (mapDifferentials.{v, u, w, m} a a (𝟙 O₁) (𝟙 O₂) (by simp)).val.app X x = x
```

**`AlgebraicGeometry.SheafOfModules.mapDifferentials_comp_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsFunctorial.lean#L200). The attribute's comment: “composition law”.

> Canonical maps on differentials respect composition of commutative squares, on every local
> section.

```lean
theorem mapDifferentials_comp_apply {O₁ O₂ O₁' O₂' O₁'' O₂'' : Sheaf J CommRingCat.{w}}
    (a : O₁ ⟶ O₂) (a' : O₁' ⟶ O₂') (a'' : O₁'' ⟶ O₂'')
    (f₁ : O₁ ⟶ O₁') (f₂ : O₂ ⟶ O₂') (g₁ : O₁' ⟶ O₁'') (g₂ : O₂' ⟶ O₂'')
    (sqf : a ≫ f₂ = f₁ ≫ a') (sqg : a' ≫ g₂ = g₁ ≫ a'')
    (X : Cᵒᵖ) (x : (moduleOfDifferentialsOfSite.{v, u, w, m} O₁ O₂ a).val.obj X) :
    (mapDifferentials.{v, u, w, m} a a'' (f₁ ≫ g₁) (f₂ ≫ g₂)
      (by
        calc
          a ≫ (f₂ ≫ g₂) = (a ≫ f₂) ≫ g₂ := (Category.assoc _ _ _).symm
          _ = (f₁ ≫ a') ≫ g₂ := by rw [sqf]
          _ = f₁ ≫ (a' ≫ g₂) := Category.assoc _ _ _
          _ = f₁ ≫ (g₁ ≫ a'') := by rw [sqg]
          _ = (f₁ ≫ g₁) ≫ a'' := (Category.assoc _ _ _).symm)).val.app X x =
      (mapDifferentials.{v, u, w, m} a' a'' g₁ g₂ sqg).val.app X
        ((mapDifferentials.{v, u, w, m} a a' f₁ f₂ sqf).val.app X x)
```

## Tag 08TS, a lemma

[Tag 08TS](https://stacks.math.columbia.edu/tag/08TS) in the Stacks Project.

**`Stacks.Sites.Conormal.differentialSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 888](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L888). The attribute's comment: “the canonical exact sequence of `O'₂`-modules”.

> The conormal sequence `I/I² ⟶ B ⊗_A Ω_{A/R} ⟶ Ω_{B/R} ⟶ 0`, with its middle and right
> terms expressed by the sheaves of relative differentials that corepresent derivations.

```lean
noncomputable def differentialSequence :
    ShortComplex
      (_root_.SheafOfModules.{max w u v z} (Stacks.SheafOfModules.Tensor.ringSheaf B))
```

**`Stacks.Sites.Conormal.differentialSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 928](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L928). The attribute's comment: “exactness at the middle term”. References: SGA 3 III (4.25), “exactness of (+)”.

> The transported sequence is exact at the extension of scalars of `Ω_{A/R}`.

```lean
theorem differentialSequence_exact :
    (differentialSequence.{v, u, w, z} J R A B a φ).Exact
```

**`Stacks.Sites.Conormal.differentialSequence_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 936](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L936). The attribute's comment: “exactness on the right”. References: SGA 3 III (4.25), “surjectivity in (+)”.

> The transported sequence surjects onto `Ω_{B/R}`.

```lean
theorem differentialSequence_epi :
    Epi (differentialSequence.{v, u, w, z} J R A B a φ).g
```

**`Stacks.Sites.Conormal.differentialSequence_f_class`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 946](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L946). The attribute's comment: “the rule `f ↦ d f ⊗ 1` for the leftmost map”.

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

**`Stacks.Sites.Conormal.differentialSequence_g_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 962](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L962). The attribute's comment: “the right-hand map on local differentials”.

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

**`Stacks.Sites.Conormal.differentialSequence_g_eq_mapDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L982). The attribute's comment: “the map on the right is the one of Stacks 08TR”.

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

**`Stacks.Sites.Conormal.differentialSequence_f_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L1010). The attribute's comment: “the rule `f ↦ d f ⊗ 1` characterises the leftmost map”.

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

**`Stacks.Sites.Conormal.differentialSequence_X₁_desc_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/CorepresentingConormalSequence.lean#L1057). The attribute's comment: “the leftmost term is `I/I²`, by its universal property”.

> **The leftmost term of the sequence is `I/I²`.** A morphism of sheaves of `O'₂`-modules out
> of it is the same thing as an `O₂`-linear natural family of maps `I(U) ⟶ N(U)` out of the
> kernel ideal: every such family descends to the term, uniquely, by the rule that the conormal
> class of a local section `f` of `I` goes to the value of the family at `f`. The family
> annihilates `I²` automatically, a local section of `I` acting as zero on a sheaf of
> `O'₂`-modules.

```lean
theorem differentialSequence_X₁_desc_unique
    (N : _root_.SheafOfModules.{max w u v z} (Stacks.SheafOfModules.Tensor.ringSheaf B))
    (ρ : IdealRestriction.{v, u, w, z} φ N) :
    ∃! g : (differentialSequence.{v, u, w, z} J R A B a φ).X₁ ⟶ N,
      ∀ (X : Cᵒᵖ) (x : kernelIdeal φ.hom X),
        g.val.app X (conormalClass.{v, u, w, z} J R A B a φ X x) = ρ.app X x
```

## Tag 04BP, a lemma

[Tag 04BP](https://stacks.math.columbia.edu/tag/04BP) in the Stacks Project.

**`Stacks.Sites.SquareZeroExtension.statement₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DerivationsSqZeroExtension.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DerivationsSqZeroExtension.lean#L306). References: EGA 0 (20.1.3), “action of Der”.

> **Statement 1.** For every `φ`-derivation `D`, the map `s + D : O₂ → A`
> (Definition 5) is again a section of `π`: it underlies a homomorphism of sheaves of
> `O₁`-algebras with `π ∘ (s + D) = id`.
>
> We express this by producing a `Section` whose objectwise function is `s + D`.

```lean
theorem statement₁ (s : E.Section) (D : E.Derivation) :
    ∃ s' : E.Section, ∀ (U : Cᵒᵖ) (a : E.O₂.obj U), s'.app U a = E.addDeriv s D U a
```

**`Stacks.Sites.SquareZeroExtension.statement₂_bijection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DerivationsSqZeroExtension.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DerivationsSqZeroExtension.lean#L383). References: EGA 0 (20.1.3), “section case (u = id)”.

> **Statement 2 (the bijection / torsor).** Fixing a section `s`, the map
> `D ↦ s + D` is a bijection from `φ`-derivations to sections of `π`, with inverse
> `s' ↦ s' - s`.  We package the bijection as an explicit `Equiv` between
> `Der_{O₁}(O₂, F)` and the sections of `π`, characterized on underlying objectwise
> functions by `s + D` and `s' - s`.  This exhibits the set of sections of `π` as a
> torsor under (an affine space over) `Der_{O₁}(O₂, F)`.

```lean
theorem statement₂_bijection (s : E.Section) :
    ∃ e : E.Derivation ≃ E.Section,
      (∀ (D : E.Derivation) (U : Cᵒᵖ) (a : E.O₂.obj U),
        (e D).app U a = E.addDeriv s D U a) ∧
      (∀ (s' : E.Section) (U : Cᵒᵖ) (a : E.O₂.obj U),
        (e.symm s').toFun U a = E.subSection s s' U a)
```

## Tag 04BQ, a definition

[Tag 04BQ](https://stacks.math.columbia.edu/tag/04BQ) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.Derivation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean#L73). The attribute's comment: “a Y-derivation is an f♯-derivation”. References: EGA IV (16.5.1), “more general”.

> **Stacks 04BQ, part (1).** A `Y`-derivation `D : 𝒪_C ⟶ F` with values in a sheaf `F` of
> `𝒪_C`-modules, for a morphism of ringed topoi `(f, f♯) : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)`: by
> definition an `f♯`-derivation, that is, a derivation of `𝒪_C` relative to the inverse-image
> form `f♯ : f⁻¹𝒪_D ⟶ 𝒪_C` of the structure map.

```lean
abbrev Derivation (F : Sheaf.targetModules.{u, v, w} X.J X.O)
```

**`AlgebraicGeometry.RingedToposHom.differentials`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean#L81). The attribute's comment: “the sheaf of differentials”.

> **Stacks 04BQ, part (2).** The sheaf of differentials `Ω_{X/Y} = Ω_f = Ω_{𝒪_C/f⁻¹𝒪_D}` of a
> morphism of ringed topoi `(f, f♯) : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)`: the sheaf of differentials of
> the inverse-image form `f⁻¹𝒪_D ⟶ 𝒪_C` of its structure map, a sheaf of `𝒪_C`-modules on the
> source site.

```lean
noncomputable abbrev differentials : Sheaf.targetModules.{u, v, w} X.J X.O
```

**`AlgebraicGeometry.RingedToposHom.universalDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean#L89). The attribute's comment: “the universal Y-derivation d_{X/Y}”.

> **Stacks 04BQ.** The universal `Y`-derivation `d_{X/Y} : 𝒪_C ⟶ Ω_{X/Y}` that the sheaf of
> differentials comes equipped with: the universal derivation of the inverse-image form of the
> structure map.

```lean
noncomputable def universalDerivation : f.Derivation f.differentials
```

**`AlgebraicGeometry.RingedToposHom.existsUnique_descDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposHomologyZero.lean#L97). The attribute's comment: “universality of d_{X/Y}”.

> **Stacks 04BQ.** `d_{X/Y}` is universal among `Y`-derivations: every `Y`-derivation with
> values in a sheaf of `𝒪_C`-modules factors through it by a unique morphism of sheaves of
> modules.

```lean
theorem existsUnique_descDerivation (F : Sheaf.targetModules.{u, v, w} X.J X.O)
    (D : f.Derivation F) :
    ∃! g : f.differentials ⟶ F, (f.universalDerivation).postcomp g.val = D
```

## Tag 04BR, a lemma

[Tag 04BR](https://stacks.math.columbia.edu/tag/04BR) in the Stacks Project.

**`Stacks.Sheaves.Differentials.statement3_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsComparisonMap.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialsComparisonMap.lean#L420). References: EGA 0 (20.5.2), “(20.5.2.4) & (20.5.2.6)”; EGA IV (16.4.3), “(16.4.3.6),(16.4.3.7)”.

> **Statement 3 (characterization and uniqueness of `c_f`).**
>
> The comparison map `c_f : f^* Ω_{X/Y} ⟶ Ω_{X'/Y'}` is *uniquely* characterized by
> the local-section property of Statement 3 (corrected
> formulation):
> `c_f ∘ (f^* d_{X/Y}(t)) = d_{X'/Y'} ∘ (f^* t)` as maps `f⁻¹ h_U^# ⟶ Ω_{X'/Y'}`.
>
> We state this directly in terms of `c_f` (not its adjoint transpose): for every
> object `U` and every local section `t ∈ O_X(U)`, `c_f` sends the pulled-back
> universal section `f^* d_{X/Y}(t)` (the image of `d_{X/Y}(t)` under the
> adjunction unit, i.e. `MorphismOverBase.pullbackDiff`, lying in
> `(f^* Ω_{X/Y})(Ff U)`) to `d_{X'/Y'}(f♯ t)` (the local section
> `d_{X'/Y'} ∘ (f^* t)` evaluated at `Ff U`).  Here `c_f` acts via its component
> `c_f.val.app (Ff U) : (f^* Ω_{X/Y})(Ff U) ⟶ Ω_{X'/Y'}(Ff U)`, so the left-hand
> side is literally `c_f` composed with the pulled-back section `f^* d_{X/Y}(t)`.
>
> Uniqueness holds because the local sections `d_{X/Y}(t)` generate `Ω_{X/Y}` as an
> `O_X`-module, so the sections `f^* d_{X/Y}(t)` generate `f^* Ω_{X/Y}` as an
> `O_{X'}`-module (Stacks Tag 04BR).

```lean
theorem statement3_unique :
    ∃! cf : f.pullΩ ⟶ X'.Ω,
      ∀ (U : X.Cᵒᵖ) (t : X.ringSheaf'.obj.obj U),
        (cf.val.app (f.Ff.op.obj U)).hom (f.pullbackDiff U t)
          = (X'.d.app (f.Ff.op.obj U)).d (f.fsharpApp U t)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.33, Tag 04BJ](https://stacks.math.columbia.edu/tag/04BJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
