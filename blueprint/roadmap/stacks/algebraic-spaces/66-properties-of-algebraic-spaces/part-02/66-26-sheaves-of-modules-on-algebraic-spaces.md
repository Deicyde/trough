---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.modulePushforward_additive, AlgebraicGeometry.Space.moduleSheafFunctor_map_compIsoCongr_hom_app, AlgebraicGeometry.Space.modulePushforwardCompIso', AlgebraicGeometry.Space.modulePullback, AlgebraicGeometry.Space.modulePullbackAdjunction, AlgebraicGeometry.Space.modulePushforwardCompIso, AlgebraicGeometry.Space.modulePullbackCompIso, AlgebraicGeometry.Space.modulePushforwardIdIso
statement: formalized
proof: formalized
---

# 66.26 Sheaves of modules on algebraic spaces

Section 66.26 of the Stacks Project, [Tag 03LT](https://stacks.math.columbia.edu/tag/03LT). 5 tags here are carried by 40 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03LU, an equation

[Tag 03LU](https://stacks.math.columbia.edu/tag/03LU) in the Stacks Project.

**`AlgebraicGeometry.Space.modulePushforward_additive`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PushforwardPresentationExact.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PushforwardPresentationExact.lean#L498). The attribute's comment: “additivity of the direct image”.

> The direct image of `𝒪`-modules along a morphism of algebraic spaces is an additive
> functor.

```lean
instance modulePushforward_additive (f : X ⟶ Y) :
    (modulePushforward B S hS f).Additive
```

**`AlgebraicGeometry.Space.moduleSheafFunctor_map_compIsoCongr_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean#L271). The attribute's comment: “the composition comparison for direct images is the geometric comparison”.

> **Stacks 03LU.**  The comparison `f_* ∘ g_* ≅ (f ≫ g)_*` of direct images of `𝒪`-modules is
> the geometric comparison `AlgebraicGeometry.Space.smallToposMorphismTypeU_comp` of Stacks 03G2,
> part (3), on underlying sheaves of sets.  The comparison appears in the transported form that
> `AlgebraicGeometry.Space.modulePushforwardCompIso_eq_compIsoCongr` identifies it with, and
> `AlgebraicGeometry.Space.modulePushforwardCompIso_hom_app_eq` is that identification at a
> single module.

```lean
theorem moduleSheafFunctor_map_compIsoCongr_hom_app (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) :
    (Sheaf.moduleSheafFunctor (structureRingSheaf B S hS Z)).map
        ((CategoryTheory.Functor.compIsoCongr
          (pushforwardModules_eq_modulePushforward B S hS f)
          (pushforwardModules_eq_modulePushforward B S hS g)
          (pushforwardModules_eq_modulePushforward B S hS (f ≫ g))
          (pushforwardModulesCompAt B S hS f g)).hom.app F) =
      (smallToposMorphismTypeU_comp B S hS f g).hom.app
        ((Sheaf.moduleSheafFunctor (structureRingSheaf B S hS X)).obj F)
```

**`AlgebraicGeometry.Space.modulePushforwardCompIso'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleCompIso.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleCompIso.lean#L153). The attribute's comment: “pushforward composition”.

> **Stacks 03LU, the composition comparison for the direct image of modules.**  The composite of
> the direct images of `𝒪`-modules along `f : X ⟶ Y` and then `g : Y ⟶ Z` is canonically isomorphic
> to the direct image along `f ≫ g`.
>
> The comparison is the composition law for the direct image of modules along a composite morphism
> of ringed topoi, followed by the transport of the direct image of modules along Stacks 03G8's
> cartesian comparison of the direct images of sheaves of sets.
>
> This is the statement in the `RingedToposHom.pushforwardModules` presentation. The same part key
> also sits on `AlgebraicGeometry.Space.modulePushforwardCompIso` of
> `StacksFrontier.AlgebraicGeometry.Spaces.SmallEtaleModulePullbackComp`, which states the same
> comparison in the library's primary `AlgebraicGeometry.Space.modulePushforward` vocabulary and
> is what consumers outside this presentation use; the two are identified by
> `AlgebraicGeometry.Space.modulePushforwardCompIso_eq_modulePushforwardCompIso'`. A tag carried by
> both is correct, not a duplication: each presentation states the clause in its own vocabulary.

```lean
noncomputable def modulePushforwardCompIso' (f : X ⟶ Y) (g : Y ⟶ Z) :
    (smallEtaleRingedToposHom B S hS f).pushforwardModules ⋙
        (smallEtaleRingedToposHom B S hS g).pushforwardModules ≅
      (smallEtaleRingedToposHom B S hS (f ≫ g)).pushforwardModules
```

**`AlgebraicGeometry.Space.modulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullback.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullback.lean#L78). The attribute's comment: “pullback”.

> The pullback `f^*G = 𝒪_X ⊗_{f⁻¹𝒪_Y} f⁻¹G` of `𝒪_Y`-modules along a morphism `f : X ⟶ Y`
> of algebraic spaces.

```lean
noncomputable def modulePullback (f : X ⟶ Y) :
    Modules.{u, u} B S hS Y.1 Y.2 ⥤ Modules.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.modulePullbackAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullback.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullback.lean#L206). The attribute's comment: “the adjunction”.

> Pullback of `𝒪`-modules along a morphism of algebraic spaces is left adjoint to the
> pushforward `AlgebraicGeometry.Space.modulePushforward`: there is a bijection
> `Hom_{𝒪_X}(f^*G, F) = Hom_{𝒪_Y}(G, f_*F)`, natural in both variables.

```lean
noncomputable def modulePullbackAdjunction (f : X ⟶ Y) :
    modulePullback B S hS f ⊣ modulePushforward B S hS f
```

**`AlgebraicGeometry.Space.modulePushforwardCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean#L366). The attribute's comment: “pushforward composition”.

> The canonical comparison `f_* ∘ g_* ≅ (f ≫ g)_*` of direct images of `𝒪`-modules along a
> composite of morphisms of algebraic spaces.
>
> Both sides have the direct image of sheaves of sets of the composite as their underlying
> sheaf, and the comparison is `AlgebraicGeometry.Space.smallToposMorphismTypeU_comp`, the
> comparison of Stacks 03G2, part (3), on it.

```lean
noncomputable def modulePushforwardCompIso (f : X ⟶ Y) (g : Y ⟶ Z) :
    modulePushforward B S hS f ⋙ modulePushforward B S hS g ≅
      modulePushforward B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.modulePushforwardCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean#L366). The attribute's comment: “the composition comparison for direct images”.

> The canonical comparison `f_* ∘ g_* ≅ (f ≫ g)_*` of direct images of `𝒪`-modules along a
> composite of morphisms of algebraic spaces.
>
> Both sides have the direct image of sheaves of sets of the composite as their underlying
> sheaf, and the comparison is `AlgebraicGeometry.Space.smallToposMorphismTypeU_comp`, the
> comparison of Stacks 03G2, part (3), on it.

```lean
noncomputable def modulePushforwardCompIso (f : X ⟶ Y) (g : Y ⟶ Z) :
    modulePushforward B S hS f ⋙ modulePushforward B S hS g ≅
      modulePushforward B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.modulePullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean#L457). The attribute's comment: “pullback composition”.

> The canonical comparison `g^* ∘ f^* ≅ (f ≫ g)^*` of inverse images of `𝒪`-modules along a
> composite of morphisms of algebraic spaces.
>
> Both functors are left adjoint to `(f ≫ g)_*`: the left-hand side by
> `AlgebraicGeometry.Space.moduleCompAdjunction`, which composes the two adjunctions and reads
> the resulting right adjoint through `modulePushforwardCompIso`, and the right-hand side by
> `AlgebraicGeometry.Space.modulePullbackAdjunction`.  The comparison is the uniqueness of a
> left adjoint, so it is the mate of the comparison of direct images.

```lean
noncomputable def modulePullbackCompIso (f : X ⟶ Y) (g : Y ⟶ Z) :
    modulePullback B S hS g ⋙ modulePullback B S hS f ≅ modulePullback B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.modulePullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackComp.lean#L457). The attribute's comment: “the composition comparison for pullbacks”.

> The canonical comparison `g^* ∘ f^* ≅ (f ≫ g)^*` of inverse images of `𝒪`-modules along a
> composite of morphisms of algebraic spaces.
>
> Both functors are left adjoint to `(f ≫ g)_*`: the left-hand side by
> `AlgebraicGeometry.Space.moduleCompAdjunction`, which composes the two adjunctions and reads
> the resulting right adjoint through `modulePushforwardCompIso`, and the right-hand side by
> `AlgebraicGeometry.Space.modulePullbackAdjunction`.  The comparison is the uniqueness of a
> left adjoint, so it is the mate of the comparison of direct images.

```lean
noncomputable def modulePullbackCompIso (f : X ⟶ Y) (g : Y ⟶ Z) :
    modulePullback B S hS g ⋙ modulePullback B S hS f ≅ modulePullback B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.modulePushforwardIdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackId.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackId.lean#L307). The attribute's comment: “the unit law for the direct image”.

> **The unit law of Stacks 03LU for the direct image**: the direct image of `𝒪`-modules along
> an identity morphism of algebraic spaces is the identity functor.
>
> The direct image of sheaves of sets along an identity is the identity functor, and the structure
> map of the identity is the corresponding identification of the structure sheaves
> (`AlgebraicGeometry.Space.structureSharpSet_id`), which is exactly the input
> `AlgebraicGeometry.RingedToposHom.pushforwardModulesIsoId` asks for.
>
> This is the datum that the `idIso` field of
> `AlgebraicGeometry.Space.ModulePushforwardCoherence` assumes.

```lean
def modulePushforwardIdIso (X : AlgebraicSpaces B S hS) :
    modulePushforward B S hS (𝟙 X) ≅ 𝟭 (Modules.{u, u} B S hS X.1 X.2)
```

**`AlgebraicGeometry.Space.modulePullbackIdIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackId.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullbackId.lean#L323). The attribute's comment: “the unit law: the inverse image of modules along an identity is the identity functor”.

> **The unit law of Stacks 03LU**: the inverse image of `𝒪`-modules along an identity morphism
> of algebraic spaces is the identity functor.
>
> The inverse image is a left adjoint of the direct image by
> `AlgebraicGeometry.Space.modulePullbackAdjunction`, the direct image along an identity is the
> identity functor by `AlgebraicGeometry.Space.modulePushforwardIdIso`, and a left adjoint of the
> identity functor is the identity functor.

```lean
def modulePullbackIdIso (X : AlgebraicSpaces B S hS) :
    modulePullback B S hS (𝟙 X) ≅ 𝟭 (Modules.{u, u} B S hS X.1 X.2)
```

**`AlgebraicGeometry.Space.modulePushforwardCompIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardCompIsoAssoc.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardCompIsoAssoc.lean#L287). The attribute's comment: “the associativity of the composition comparison for direct images”.

> **Stacks 03LU, associativity of the composition comparison for direct images.**  For three
> composable morphisms `f : W ⟶ X`, `g : X ⟶ Y`, `h : Y ⟶ Z` of algebraic spaces the two ways of
> comparing `f_* ∘ g_* ∘ h_*` with `(f ≫ g ≫ h)_*` agree.
>
> This is the `assoc` field of `AlgebraicGeometry.Space.ModulePushforwardCoherence`, so it is no
> longer a hypothesis.  It is the cocycle law at the morphisms of ringed topoi of Stacks 03G8,
> `AlgebraicGeometry.Space.pushforwardModulesCompAt_assoc`, transported along the identifications
> of the two direct images.

```lean
theorem modulePushforwardCompIso_assoc (f : W ⟶ X) (g : X ⟶ Y) (h : Y ⟶ Z) :
    isoWhiskerLeft (modulePushforward B S hS f) (modulePushforwardCompIso B S hS g h) ≪≫
        modulePushforwardCompIso B S hS f (g ≫ h) =
      (associator (modulePushforward B S hS f) (modulePushforward B S hS g)
          (modulePushforward B S hS h)).symm ≪≫
        isoWhiskerRight (modulePushforwardCompIso B S hS f g)
          (modulePushforward B S hS h) ≪≫
        modulePushforwardCompIso B S hS (f ≫ g) h
```

**`AlgebraicGeometry.Space.modulePushforwardCoherence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardIdIso.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePushforwardIdIso.lean#L45). The attribute's comment: “the pseudofunctoriality of the direct image, assembled: the identity comparison together with the associativity and the two unit laws of the composition comparison, as one datum with no hypothesis”.

> **Pseudofunctoriality of the direct image of `𝒪`-modules of Stacks 03LU, with no
> hypothesis.**  The identity datum is
> `AlgebraicGeometry.Space.modulePushforwardIdIso`, and
> `AlgebraicGeometry.Space.modulePushforwardCoherenceOfIdIso` supplies the associativity coherence
> and the two unit laws from it.

```lean
noncomputable def modulePushforwardCoherence : ModulePushforwardCoherence B S hS
```

**`AlgebraicGeometry.Space.modulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureMapSharp.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/StructureMapSharp.lean#L573). The attribute's comment: “pushforward”.

> **Stacks 03D6, part (1)**, unconditionally, and the direct-image half of Stacks 03LU: the
> direct image of `𝒪_X`-modules along a morphism of algebraic spaces, read as `𝒪_Y`-modules by
> restriction of scalars along the structure map.
>
> The inverse-image half of Stacks 03LU is
> `AlgebraicGeometry.Space.modulePullback`, and the adjunction is
> `AlgebraicGeometry.Space.modulePullbackAdjunction`
> (`StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModulePullback.lean`).  That adjunction is
> stated for the direct image of Stacks 03D6, part (1) attached to the morphism of ringed topoi,
> which is this functor up to a comparison that is not yet supplied; see the implementation notes
> of that file.

```lean
noncomputable def modulePushforward (f : X ⟶ Y) :
    Modules.{u, u} B S hS X.1 X.2 ⥤ Modules.{u, u} B S hS Y.1 Y.2
```

**`AlgebraicGeometry.RingedSite.HomGeneral.pullbackModulesToposIsoGeneral_hom_app_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RingedToposModulesPullbackToposGeneralUnit.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RingedToposModulesPullbackToposGeneralUnit.lean#L305). The attribute's comment: “the corepresentability construction of `f^*𝒪_Y ≅ 𝒪_X` for the pullback of the modules development and Mathlib's adjoint-transpose construction for the site-presented pullback agree under the comparison of the two pullbacks, for a morphism of ringed sites at independent universes”.

> **The two constructions of Stacks 03LU along a morphism of ringed sites agree.**  The
> comparison `AlgebraicGeometry.RingedSite.HomGeneral.pullbackModulesToposIsoGeneral` of the two
> pullbacks of sheaves of modules carries the corepresentability identification
> `Stacks.Sheaves.RingedToposModules.pullbackModulesObjUnitIso` of `f^*𝒪_Y ≅ 𝒪_X` to Mathlib's
> adjoint-transpose one, `SheafOfModules.pullbackObjUnitToUnit` at `f^♯`.
>
> Both are pinned by their transposes along Stacks 03D7, those two transposes are compared by
> `homEquiv_pullbackModulesToposIsoGeneral_hom_app_unit`, and they agree because both are the unit
> section of `𝒪_X`.

```lean
public theorem HomGeneral.pullbackModulesToposIsoGeneral_hom_app_unit :
    f.pullbackModulesToposIsoGeneral.hom.app
          (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf (toRingedTopos Y).O)) ≫
        SheafOfModules.pullbackObjUnitToUnit f.toRingedToposSiteHom.fSharpRing =
      (pullbackModulesObjUnitIso f.toRingedToposHom.toRingedToposModulesHom).inv
```

## Tag 03LV, a lemma

[Tag 03LV](https://stacks.math.columbia.edu/tag/03LV) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleInverseImageStructureSheafIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleInverseImageStructureSheaf.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleInverseImageStructureSheaf.lean#L154). The attribute's comment: “the canonical structure map”.

> The forward map of `AlgebraicGeometry.Space.etaleInverseImageStructureSheafIso` is the
> inverse-image form of the structure map of Stacks 03G8.  This is what makes that isomorphism the
> canonical one of Stacks 03LV rather than an arbitrary one.

```lean
theorem etaleInverseImageStructureSheafIso_hom (h : U ⟶ V) (hh : IsEtale B S hS h.hom) :
    (etaleInverseImageStructureSheafIso B S hS h hh).hom =
      (smallEtaleRingedToposHom B S hS h).fSharpInverseImage
```

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean#L166). The attribute's comment: “pullback of modules is inverse image”.

> **Stacks 03LV.** Along an étale morphism of algebraic spaces, the pullback of `𝒪_Y`-modules
> of Stacks 03LU is naturally isomorphic to the inverse image of modules with its scalars
> transported along the canonical isomorphism of structure sheaves.

```lean
noncomputable def modulePullbackIsoEtaleModuleInverseImage :
    modulePullback B S hS f ≅ etaleModuleInverseImage B S hS f hf
```

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean#L178). The attribute's comment: “canonical module comparison”.

> **Stacks 03LV.** The comparison of the pullback of modules with the inverse image sends the
> canonical image of every section of the inverse image to that same section.  This specifies the
> comparison, rather than merely asserting that the two functors are isomorphic: a scalar-unit
> twist of the natural isomorphism is excluded.

```lean
theorem modulePullbackIsoEtaleModuleInverseImage_unit_app
    (G : Modules.{u, u} B S hS Y.1 Y.2) (U : (SmallEtale B S hS X.1)ᵒᵖ)
    (m : ((inverseImageModules (smallEtaleRingedToposHom B S hS f).toToposHom
      (structureRingSheaf B S hS Y)).obj G).val.obj U) :
    ((extendScalarsFSharpAdjunction B S hS f).unit.app
          ((inverseImageModules (smallEtaleRingedToposHom B S hS f).toToposHom
            (structureRingSheaf B S hS Y)).obj G) ≫
        (SheafOfModules.restrictScalars
          (smallEtaleRingedToposModulesHom B S hS f).fSharpInverseImage).map
            ((modulePullbackIsoEtaleModuleInverseImage B S hS f hf).hom.app G)).val.app U m =
      m
```

**`AlgebraicGeometry.Space.modulePullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean#L200). The attribute's comment: “exactness”.

> **Stacks 03LV.** Pullback of sheaves of modules along an étale morphism of algebraic spaces
> is exact.  Through the comparison with the inverse image both halves are the exactness of the
> inverse image of modules of Stacks 04JC, restriction of scalars along an isomorphism being an
> equivalence.

```lean
theorem modulePullback_exact :
    exactFunctor (Modules.{u, u} B S hS Y.1 Y.2) (Modules.{u, u} B S hS X.1 X.2)
      (modulePullback B S hS f)
```

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean#L370). The attribute's comment: “the identification f^*G = G|\_\{X\_étale}”.

> **Stacks Equation 03LW, that is clause (2) of Stacks 03LV.**  Along an étale morphism
> `f : X ⟶ Y` of algebraic spaces the pullback of `𝒪_Y`-modules of Stacks 03LU is naturally
> isomorphic to étale restriction: `f^*G` is the sheaf whose sections over an étale chart `U` of
> `X` are the sections of `G` over the composite chart of `Y`.
>
> The comparison factors through the inverse image of modules by
> `AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage`, which is clause (2) of
> Stacks 03LV in its inverse-image reading.

```lean
noncomputable def modulePullbackIsoEtaleModulePullback :
    modulePullback B S hS f ≅ etaleModulePullback.{u, u} B S hS f hf
```

**`AlgebraicGeometry.Space.isIso_fSharpInverseImage_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean#L377). The attribute's comment: “the inverse image of the structure sheaf, h⁻¹𝒪\_V = 𝒪\_U”.

> **Stacks 03LV.** For an étale morphism of algebraic spaces the inverse-image form
> `f⁻¹𝒪_Y ⟶ 𝒪_X` of the structure map of the morphism of small étale ringed topoi of Stacks 03G8
> is an isomorphism.
>
> The proof exhibits it as a universal arrow: composition with it is identified with the inverse
> of the composite of `AlgebraicGeometry.Space.fMapRestrictionEquiv` with the chart correspondence
> and the adjunction, and the chartwise formula for the structure map says that the identification
> sends the structure map itself to the identity.

```lean
theorem isIso_fSharpInverseImage_of_isEtale :
    IsIso (smallEtaleRingedToposHom B S hS f).fSharpInverseImage
```

**`AlgebraicGeometry.Space.etaleStructureSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean#L424). The attribute's comment: “inverse image of the structure sheaf”.

> **Stacks 03LV.** For an étale morphism of algebraic spaces the inverse image of the
> structure sheaf of the target along the morphism of small étale ringed topoi of Stacks 03G8 is
> canonically isomorphic to the structure sheaf of the source.

```lean
noncomputable def etaleStructureSheafIso :
    (Stacks.Sheaves.ToposPushforward.inverseImageCommRingFunctor
        (smallEtaleRingedToposHom B S hS f).toToposHom).obj
      (smallEtaleRingedTopos B S hS Y).O ≅ (smallEtaleRingedTopos B S hS X).O
```

**`AlgebraicGeometry.Space.etaleStructureSheafIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleStructureSheafInverseImage.lean#L435). The attribute's comment: “canonical structure map”.

> **Stacks 03LV.** The forward map of the canonical isomorphism of structure sheaves along an
> étale morphism is the inverse-image form of the structure map; the isomorphism is not an extra
> choice.

```lean
theorem etaleStructureSheafIso_hom :
    (etaleStructureSheafIso B S hS f hf).hom =
      (smallEtaleRingedToposHom B S hS f).fSharpInverseImage
```

## Tag 03LW, an equation

[Tag 03LW](https://stacks.math.columbia.edu/tag/03LW) in the Stacks Project.

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackComparison.lean#L166). The attribute's comment: “the identification f^*G = f\_small^\{-1}G along an étale morphism”.

> **Stacks 03LV.** Along an étale morphism of algebraic spaces, the pullback of `𝒪_Y`-modules
> of Stacks 03LU is naturally isomorphic to the inverse image of modules with its scalars
> transported along the canonical isomorphism of structure sheaves.

```lean
noncomputable def modulePullbackIsoEtaleModuleInverseImage :
    modulePullback B S hS f ≅ etaleModuleInverseImage B S hS f hf
```

**`AlgebraicGeometry.Space.etaleModuleInverseImageIsoEtaleModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean#L341). The attribute's comment: “the inverse image of modules is étale restriction”.

> **Stacks' Equation 03LW**, the outer identification `G|_{X_étale} = f_{small}^{-1}G`: the
> inverse image of `𝒪_Y`-modules along an étale morphism, read over `𝒪_X` through the canonical
> isomorphism of structure sheaves, is étale restriction of modules.

```lean
noncomputable def etaleModuleInverseImageIsoEtaleModulePullback :
    etaleModuleInverseImage B S hS f hf ≅ etaleModulePullback.{u, u} B S hS f hf
```

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean#L370). The attribute's comment: “pullback of modules along an étale morphism is étale restriction”.

> **Stacks Equation 03LW, that is clause (2) of Stacks 03LV.**  Along an étale morphism
> `f : X ⟶ Y` of algebraic spaces the pullback of `𝒪_Y`-modules of Stacks 03LU is naturally
> isomorphic to étale restriction: `f^*G` is the sheaf whose sections over an étale chart `U` of
> `X` are the sections of `G` over the composite chart of `Y`.
>
> The comparison factors through the inverse image of modules by
> `AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage`, which is clause (2) of
> Stacks 03LV in its inverse-image reading.

```lean
noncomputable def modulePullbackIsoEtaleModulePullback :
    modulePullback B S hS f ≅ etaleModulePullback.{u, u} B S hS f hf
```

**`AlgebraicGeometry.Space.modulePullbackIsoEtaleModulePullback_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModulePullbackRestriction.lean#L385). The attribute's comment: “canonical module comparison”.

> **Stacks Equation 03LW, canonicity.**  The comparison of the pullback of modules with étale
> restriction sends the canonical image of a section of the inverse image of modules to the
> comparison of Stacks 03LQ applied to that section, so it introduces no twist of its own: it is
> the canonical identification and not merely some natural isomorphism of the two functors.
>
> This is `AlgebraicGeometry.Space.modulePullbackIsoEtaleModuleInverseImage_unit_app`, which pins
> the extension-of-scalars half, followed by
> `AlgebraicGeometry.Space.etaleModuleInverseImageIsoEtaleModulePullback_val_app`, which pins the
> transport half.

```lean
theorem modulePullbackIsoEtaleModulePullback_unit_app (G : Modules.{u, u} B S hS Y.1 Y.2)
    (U : (SmallEtale B S hS X.1)ᵒᵖ)
    (m : ((inverseImageModules.{u, u, u, u + 1, u, u + 1}
      (smallEtaleRingedToposHom B S hS f).toToposHom
      (structureRingSheaf B S hS Y)).obj G).val.obj U) :
    ((extendScalarsFSharpAdjunction B S hS f).unit.app
          ((inverseImageModules.{u, u, u, u + 1, u, u + 1}
            (smallEtaleRingedToposHom B S hS f).toToposHom
            (structureRingSheaf B S hS Y)).obj G) ≫
        (SheafOfModules.restrictScalars
          (smallEtaleRingedToposModulesHom B S hS f).fSharpInverseImage).map
            ((modulePullbackIsoEtaleModulePullback B S hS f hf).hom.app G)).val.app U m =
      ((etaleModuleInverseImageIsoRestrictionTransport B S hS f hf).hom.app G).val.app U m
```

## Tag 03LX, a lemma

[Tag 03LX](https://stacks.math.columbia.edu/tag/03LX) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_moduleEtaleBaseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean#L692). The attribute's comment: “the ordinary direct image, for the CANONICAL comparison map and for an ÉTALE square: g étale, not merely flat, so this is a special case of Stacks 073K part (1) and not that tag. The existing 03LX attributes carry isomorphisms with the right endpoints that are not identified with the canonical map”.

> **Stacks 03LX for the ordinary direct image, read as a statement about the canonical map, in
> the étale case.**  For a cartesian square of algebraic spaces whose bottom arrow `g` is étale,
> the canonical base-change comparison
>
> `(f_*F)|_{Y'} ⟶ f'_*(F|_{X'})`
>
> of `AlgebraicGeometry.Space.moduleEtaleBaseChangeComparison` is an isomorphism.
>
> This is what `StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardBaseChangeCanonical.lean`
> records as the single underived statement the canonical reading of Stacks 03LX and Stacks 071Z
> was owed.  It is `AlgebraicGeometry.Space.isIso_moduleBaseChangeMap_of_isEtale` conjugated into
> the étale-restriction spelling by Stacks 03LW,
> `AlgebraicGeometry.Space.modulePullbackIsoEtaleModulePullback`, which is canonical, so the
> conjugation introduces no twist.
>
> **This is the étale case and not Stacks 073K, part (1).**  Stacks 073K, part (1) asserts base
> change for `g` merely *flat* and `f` quasi-compact and quasi-separated; `hg` here is
> `AlgebraicGeometry.Space.IsEtale`, and étale is strictly stronger than flat.  So this is a
> special case of that tag and carries no attribute for it.

```lean
theorem isIso_moduleEtaleBaseChangeComparison (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) :
    IsIso (moduleEtaleBaseChangeComparison B S hS i f' f g sq hg)
```

**`AlgebraicGeometry.Space.moduleHigherPushforwardEtaleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean#L147). The attribute's comment: “the higher direct images”.

> Let
>
> ```
> X' --i--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> be a cartesian square of algebraic spaces over `S` with `g` étale.  Then for every `n` the
> `n`-th higher direct image of `𝒪_X`-modules commutes with restriction along the étale base
> change,
>
> `R^n f'_*(F|_{X'}) = (R^n f_*F)|_{Y'}`
>
> in `Mod(𝒪_{Y'})`, naturally in the `𝒪_X`-module `F`. The morphism `f` is not assumed
> representable, quasi-compact or quasi-separated, and `F` is not assumed quasi-coherent.

```lean
noncomputable def moduleHigherPushforwardEtaleBaseChangeIso (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) (n : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := hasInjectiveResolutions_modules B S hS X'.1 X'.2
    etaleModulePullback B S hS i (isEtale_of_isPullback B S hS f' i g f sq.flip hg) ⋙
        (modulePushforward B S hS f').rightDerived n ≅
      (modulePushforward B S hS f).rightDerived n ⋙ etaleModulePullback B S hS g hg
```

**`AlgebraicGeometry.Space.modulePullbackSquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardEtaleBaseChange.lean, line 820](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModulePushforwardEtaleBaseChange.lean#L820). The attribute's comment: “the footnote, with both restrictions read as the inverse image of modules (Stacks 03LW)”.

> **Stacks 03LX, the footnote.** For a commutative — in particular a cartesian — square
>
> ```
> X' --i--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> of algebraic spaces, the inverse image of modules around the square agrees:
> `(f')^*(G|_{Y'}) = (f^*G)|_{X'}` for every `𝒪_Y`-module `G`, naturally in `G`.
>
> **Both restrictions are read as the inverse image of modules**, so all four functors in the
> statement are `AlgebraicGeometry.Space.modulePullback` — the source's `G|_{Y'}` is `g^*G` and
> its `(-)|_{X'}` is `i^*`.  That is the reading of Stacks 03LW, which the source's own footnote
> invokes to derive this identity, and which this development does **not** supply: no comparison
> of `AlgebraicGeometry.Space.modulePullback` with the étale restriction
> `AlgebraicGeometry.Space.etaleModulePullback` used elsewhere in this file is proved anywhere,
> and the two are different functors (the tensor inverse image of Stacks 03D6, part (2) against
> restriction along `AlgebraicGeometry.Space.smallEtalePostcomp`).  So what is proved here is the
> footnote in the inverse-image reading, not in the restriction reading, and the attribute says so.
>
> No étaleness is used: as in the source, the comparison is the Stacks 03LU composition
> isomorphism `AlgebraicGeometry.Space.modulePullbackCompIso` for the two factorizations of the
> diagonal `X' ⟶ Y` of the square, glued by the commutativity `sq.w` of the square; only `sq.w`
> is consumed, so the cartesian hypothesis is stronger than the proof needs.  The module universe
> is the universe `u` of the structure rings, which is the only one at which
> `AlgebraicGeometry.Space.modulePullback` exists.

```lean
noncomputable def modulePullbackSquareIso (sq : IsPullback i f' f g) :
    modulePullback B S hS g ⋙ modulePullback B S hS f' ≅
      modulePullback B S hS f ⋙ modulePullback B S hS i
```

**`AlgebraicGeometry.Space.modulePushforwardEtaleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StructureSharpBaseChange.lean, line 825](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/StructureSharpBaseChange.lean#L825). The attribute's comment: “the ordinary direct image”.

> **Stacks 03LX, the ordinary direct image, unconditionally.**  Let
>
> ```
> X' --i--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> be a cartesian square of algebraic spaces over a scheme `S` contained in a big fppf site `B`,
> with `g` étale.  Then for every `𝒪_X`-module `F`
>
> `f'_*(F|_{X'}) = (f_*F)|_{Y'}`
>
> in `Mod(𝒪_{Y'})`, naturally in `F`.
>
> This is `AlgebraicGeometry.Space.modulePushforwardEtaleBaseChangeIsoOfStructureSharp` with its
> hypothesis discharged by
> `AlgebraicGeometry.Space.baseChangeStructureSharp_comp_baseChangeRingMap`.  The higher direct
> images of Stacks 03LX are not treated, so the attribute carries a part string; the footnote is
> `AlgebraicGeometry.Space.modulePullbackSquareIso`.
>
> The restriction `(-)|_{X'}` is read here as `AlgebraicGeometry.Space.etaleModulePullback`,
> restriction of modules along small étale postcomposition, which is the reading of the ordinary
> clause; the footnote is proved in the inverse-image reading instead, for the reason recorded in
> its own docstring.
>
> Inherited caveat.  The source asserts an equality, and this isomorphism has the right endpoints
> but is **not** proved to be the adjunction mate of the inverse-image identification around the
> square: that is already the standing in
> `StacksFrontier/AlgebraicGeometry/Spaces/SmallEtalePushforwardBaseChange.lean`, whose
> implementation notes record it for
> `AlgebraicGeometry.Space.smallEtalePushforwardBaseChangeIso`, and the same applies to the
> `Type u` instance of Stacks 03LR, part (1) that this isomorphism is built from.
>
> The module universe is the universe `u` of the structure rings, which is the only one at which
> `AlgebraicGeometry.Space.modulePushforward` exists.

```lean
noncomputable def modulePushforwardEtaleBaseChangeIso (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom) :
    etaleModulePullback B S hS i (isEtale_of_isPullback B S hS f' i g f sq.flip hg) ⋙
        modulePushforward B S hS f' ≅
      modulePushforward B S hS f ⋙ etaleModulePullback B S hS g hg
```

## Tag 03LY, a lemma

[Tag 03LY](https://stacks.math.columbia.edu/tag/03LY) in the Stacks Project.

**`AlgebraicGeometry.Space.chartModuleInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L241). The attribute's comment: “the chartwise pullback of modules”.

> **Stacks 03LY.** The pullback of `𝒪`-modules of Stacks 03LU along the morphism of algebraic
> spaces represented by a morphism of étale scheme charts of `X`.  This is the functor
> `f_{small}^*` in which the source states the transition isomorphisms.

```lean
noncomputable def chartModuleInverseImage {V U : SmallEtale B S hS X.1} (f : V ⟶ U) :
    Modules.{u, u} B S hS (chartSpace B S hS X U).1 (chartSpace B S hS X U).2 ⥤
      Modules.{u, u} B S hS (chartSpace B S hS X V).1 (chartSpace B S hS X V).2
```

**`AlgebraicGeometry.Space.chartModuleInverseImageComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L253). The attribute's comment: “canonical comparison of chartwise pullbacks”.

> **Stacks 03LY.** The canonical comparison of successive chartwise pullbacks of modules with
> the pullback along the composite morphism of charts: it is the composition comparison of
> Stacks 03LU, read through the equality `chartMap g ≫ chartMap f = chartMap (g ≫ f)`.
>
> It is this comparison that makes the cocycle condition
> `AlgebraicGeometry.Space.IsChartModuleCocycle` a statement rather than a type error.

```lean
noncomputable def chartModuleInverseImageComp {W V U : SmallEtale B S hS X.1} (f : V ⟶ U)
    (g : W ⟶ V) :
    chartModuleInverseImage B S hS X f ⋙ chartModuleInverseImage B S hS X g ≅
      chartModuleInverseImage B S hS X (g ≫ f)
```

**`AlgebraicGeometry.Space.chartModuleRestrictionComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L271). The attribute's comment: “compatibility of chart restriction with the chartwise pullback”.

> **Stacks 03LY.** Restriction of a module to a chart commutes canonically with further
> chartwise pullback along a morphism of charts: the composite of the structure morphism of the
> larger chart with the morphism of charts is the structure morphism of the smaller chart.

```lean
noncomputable def chartModuleRestrictionComp {V U : SmallEtale B S hS X.1} (f : V ⟶ U) :
    chartModuleRestriction B S hS X U ⋙ chartModuleInverseImage B S hS X f ≅
      chartModuleRestriction B S hS X V
```

**`AlgebraicGeometry.Space.ChartModuleGlueingData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L334). The attribute's comment: “the data (1), (2) and the cocycle condition”.

> **The data of Stacks 03LY**: a sheaf of `𝒪_U`-modules on the small étale site of every étale
> scheme chart `U` of `X`, transition isomorphisms along the chartwise pullbacks of modules, and
> the cocycle condition relating them.

```lean
structure ChartModuleGlueingData
```

**`AlgebraicGeometry.Space.chartModuleRestrictionComp_cocycle_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L446). The attribute's comment: “the cocycle condition for the chartwise restrictions of a module”.

> **Stacks 03LY, the cocycle condition for the chartwise restrictions.**  For composable
> morphisms `g : W ⟶ V` and `f : V ⟶ U` of étale scheme charts of `X` and an `𝒪_X`-module `F`, the
> transition `c_g` of the restriction family after the chartwise pullback `g^*c_f` of the
> transition `c_f` is the transition `c_{g ≫ f}`, read through the canonical comparison
> `AlgebraicGeometry.Space.chartModuleInverseImageComp`.
>
> This is the condition that `AlgebraicGeometry.Space.IsChartModuleCocycle` names, written out at
> the family of restrictions; see the discussion in the module documentation of why the term of
> that predicate's type does not follow.

```lean
theorem chartModuleRestrictionComp_cocycle_app (F : Modules.{u, u} B S hS X.1 X.2)
    {W V U : SmallEtale B S hS X.1} (f : V ⟶ U) (g : W ⟶ V) :
    (chartModuleInverseImage B S hS X g).map
          ((chartModuleRestrictionComp B S hS X f).app F).hom ≫
        ((chartModuleRestrictionComp B S hS X g).app F).hom =
      (chartModuleInverseImageComp B S hS X f g).hom.app
          ((chartModuleRestriction B S hS X U).obj F) ≫
        ((chartModuleRestrictionComp B S hS X (g ≫ f)).app F).hom
```

**`AlgebraicGeometry.Space.isChartModuleCocycle_chartModuleRestrictionTransitionFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L553). The attribute's comment: “the cocycle condition for the chartwise restrictions, as a term of the predicate”.

> **The cocycle condition of Stacks 03LY for the chartwise restrictions of an `𝒪_X`-module, as
> a term of the predicate.**  This is
> `AlgebraicGeometry.Space.chartModuleRestrictionTransitions_cocycle` transported from the
> spelling in which it is proved to the one the predicate's instantiation produces, by
> `CategoryTheory.Functor.map_comp_eq_comp_of_heq`.

```lean
theorem isChartModuleCocycle_chartModuleRestrictionTransitionFamily
    (F : Modules.{u, u} B S hS X.1 X.2) :
    IsChartModuleCocycle B S hS X (chartModuleRestrictionFamily B S hS X F)
      (chartModuleRestrictionTransitionFamily B S hS X F)
```

**`AlgebraicGeometry.Space.canonicalChartModuleGlueingData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L570). The attribute's comment: “the chartwise glueing datum of a module”.

> **The chartwise glueing datum of an `𝒪_X`-module**: its restrictions to the étale scheme
> charts of `X`, the comparisons `AlgebraicGeometry.Space.chartModuleRestrictionComp` as the
> transition isomorphisms, and the cocycle condition they satisfy.

```lean
noncomputable def canonicalChartModuleGlueingData (F : Modules.{u, u} B S hS X.1 X.2) :
    ChartModuleGlueingData B S hS X
```

**`AlgebraicGeometry.Space.chartModuleGlueingFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueing.lean#L594). The attribute's comment: “the canonical chartwise description of modules”.

> **The canonical chartwise description of `𝒪_X`-modules**: the functor sending an
> `𝒪_X`-module to the family of its restrictions to the étale scheme charts of `X`, with the
> comparisons `AlgebraicGeometry.Space.chartModuleRestrictionComp` as transitions.  That this
> functor is an equivalence is Stacks 03LY.

```lean
noncomputable def chartModuleGlueingFunctor :
    Modules.{u, u} B S hS X.1 X.2 ⥤ ChartModuleGlueingData B S hS X
```

**`AlgebraicGeometry.Space.chartModuleGlueingEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueingEquivalence.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartModuleGlueingEquivalence.lean#L476). The attribute's comment: “the equivalence of modules with chartwise glueing data”.

> A sheaf of `𝒪_X`-modules on the small étale site of an algebraic space `X` is the same thing
> as a family of `𝒪_U`-modules `F_U` on the small étale sites of the étale scheme charts `U` of
> `X`, together with isomorphisms `c_f : f^*F_U ≅ F_V` for the morphisms `f : V ⟶ U` of charts
> satisfying the cocycle condition `c_g ∘ g^*c_f = c_{g ≫ f}`: an equivalence of categories, given
> by sending a module to the family of its restrictions to the charts.

```lean
def chartModuleGlueingEquivalence :
    Modules.{u, u} B S hS X.1 X.2 ≌ ChartModuleGlueingData B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.26, Tag 03LT](https://stacks.math.columbia.edu/tag/03LT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
