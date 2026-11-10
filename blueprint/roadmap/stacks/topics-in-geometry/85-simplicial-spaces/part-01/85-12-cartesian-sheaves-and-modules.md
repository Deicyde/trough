---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.IsModuleFiberTransitionIso, CategoryTheory.SimplicialSiteSituation.IsCartesianDerivedModule, CategoryTheory.SimplicialSiteSituation.IsCartesianModule, AlgebraicGeometry.SimplicialScheme.IsCartesianModule, CategoryTheory.SimplicialSiteSituation.IsCartesianSheaf, CategoryTheory.SimplicialSiteSituation.IsCartesianAbSheaf, CategoryTheory.SimplicialSiteSituation.IsCartesianDerived', CategoryTheory.SimplicialSiteSituation.IsCartesianDerived
statement: formalized
proof: formalized
---

# 85.12 Cartesian sheaves and modules

Section 85.12 of the Stacks Project, [Tag 0D7G](https://stacks.math.columbia.edu/tag/0D7G). 10 tags here are carried by 39 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07TF, a definition

[Tag 07TF](https://stacks.math.columbia.edu/tag/07TF) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.IsModuleFiberTransitionIso`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianModule.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianModule.lean#L278). The attribute's comment: “part (2), for the module fibre transition of the component 2-morphism”.

> **The cartesian condition of Stacks 07TF for sheaves of modules**, expressed through the
> 2-morphism of this file: a sheaf of `O`-modules on the total site of a simplicial site is
> cartesian when every canonical transition `f_φ^*F_m ⟶ F_n` between its component restrictions,
> namely `moduleFiberTransition`, is an isomorphism.
>
> This is part (2) of the source definition; parts (1), (3) and (4) are
> `CategoryTheory.SimplicialSiteSituation.IsCartesianSheaf`, `.IsCartesianAbSheaf` and the
> derived-category conditions. The same condition stated through the transition of
> `StacksFrontier.AlgebraicGeometry.Simplicial.ComponentRingedTopos.ModuleTransition` is
> `CategoryTheory.SimplicialSiteSituation.IsCartesianModule`.

```lean
abbrev IsModuleFiberTransitionIso
    (F : SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) O)) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianDerivedModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleSystemOfObject.lean#L298). The attribute's comment: “part (4), cartesian objects of D(O): the derived transitions Lf_phi^* K_m -> K_n are isomorphisms”.

> **Stacks 07TF (4).** An object `K` of the derived category of `O`-modules on the total site
> is *cartesian* when the derived transition `Lf_φ^* K_m ⟶ K_n` of its restrictions along every
> simplex map `φ : [m] ⟶ [n]` is an isomorphism.
>
> Parts (1), (2) and (3) of the source definition are
> `CategoryTheory.SimplicialSiteSituation.IsCartesianSheaf` and `.IsCartesianAbSheaf`,
> `.IsModuleFiberTransitionIso`, and `.IsCartesianDerived'`.

```lean
abbrev IsCartesianDerivedModule (K : DerivedCategory (S.totalRingedTopos O).Modules) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransition.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransition.lean#L300). The attribute's comment: “cartesian modules”.

> **Stacks 07TF (2).** A sheaf of `O`-modules on the total site of a simplicial-site situation
> is *cartesian* if every canonical transition `f_φ^*ℱₘ ⟶ ℱₙ` between its restrictions to the
> components is an isomorphism.

```lean
abbrev IsCartesianModule (O : Sheaf S.totalTopology CommRingCat.{u})
    (M : SheafOfModules.{u} (S.totalRingSheaf O)) : Prop
```

**`AlgebraicGeometry.SimplicialScheme.IsCartesianModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiCartesianModule.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiCartesianModule.lean#L256). The attribute's comment: “part (2), for the total Zariski site of a simplicial scheme (the site of 09VL, which this development does not carry as a term of Situation 09WE), with the component modules of `ZariskiModulePushforward` and the transition of 09WF constructed here”.

> **Stacks 07TF (2) for the total Zariski site of a simplicial scheme.** A sheaf of
> `𝒪_X`-modules on the total Zariski site of a simplicial scheme `X` is *cartesian* when every
> transition `(X φ)^* F_m ⟶ F_n` is an isomorphism.

```lean
public def IsCartesianModule (X : SimplicialObject Scheme.{u}) (F : Modules X) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Cartesian.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Cartesian.lean#L54). The attribute's comment: “cartesian sheaves of sets”.

> **Stacks 07TF.** A sheaf of sets on the total site of a simplicial site is *cartesian* if
> every canonical transition `f_φ⁻¹ Fₘ ⟶ Fₙ` between its components is an isomorphism.

```lean
abbrev IsCartesianSheaf (S : SimplicialSiteSituation.{u})
    (F : Sheaf S.totalTopology (Type u)) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianAbSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Cartesian.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Cartesian.lean#L61). The attribute's comment: “cartesian sheaves of abelian groups”.

> **Stacks 07TF.** A sheaf of abelian groups on the total site of a simplicial site is
> *cartesian* if the canonical transitions of its underlying sheaf of sets are isomorphisms.

```lean
abbrev IsCartesianAbSheaf (S : SimplicialSiteSituation.{u})
    (F : Sheaf S.totalTopology Ab.{u}) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianDerived'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerived.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerived.lean#L184). The attribute's comment: “cartesian objects of the derived category”.

> **Stacks 07TF.** An object of the derived category of abelian sheaves on the total site of a
> simplicial site is *cartesian* if the canonical transition along every simplex map is an
> isomorphism.
>
> The derived categories are the standard ones and the transition is `derivedComponentTransition`;
> `CategoryTheory.SimplicialSiteSituation.IsCartesianDerived` states the condition for an arbitrary
> choice of derived categories.

```lean
abbrev IsCartesianDerived' (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.IsCartesianDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedSheaves.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedSheaves.lean#L417). The attribute's comment: “cartesian_derived_sheaf”.

> **Stacks 07TF (3).** An object of the derived category of abelian sheaves on the total site
> is cartesian when the canonical transition along every simplex map is an isomorphism.

```lean
abbrev IsCartesianDerived (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) : Prop
```

## Tag 07TG, a lemma

[Tag 07TG](https://stacks.math.columbia.edu/tag/07TG) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerivedModule_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleFaceCriterion.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedModuleFaceCriterion.lean#L167). The attribute's comment: “face criterion for objects of D(O)”.

> **Stacks 07TG (4).** An object of the derived category of `O`-modules on the total site of
> a simplicial site is cartesian if and only if the derived transition along every face map is an
> isomorphism.
>
> The simplex maps whose derived transition is invertible form a multiplicative class: the
> identity law is `isIso_derivedComponentModuleTransition_id` and the composition law is the
> cocycle condition `derivedComponentModuleTransition_comp` of Stacks 0D9P together with
> Stacks 0D6D. Every arrow of the simplex category is a composite of faces and degeneracies, and
> `SimplexCategory.δ_comp_σ_self` exhibits each degeneracy as the second factor of a composite
> that is an identity, so no separate hypothesis on the degeneracies is needed.

```lean
theorem isCartesianDerivedModule_iff_faces
    (K : DerivedCategory (S.totalRingedTopos O).Modules) :
    S.IsCartesianDerivedModule O K ↔
      ∀ (k : ℕ) (i : Fin (k + 2)),
        IsIso ((S.derivedComponentModuleTransition O (SimplexCategory.δ i)).app K)
```

**`AlgebraicGeometry.SimplicialScheme.isCartesianModule_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiCartesianModuleFaces.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiCartesianModuleFaces.lean#L285). The attribute's comment: “part (3), the criterion for sheaves of MODULES, for the total Zariski site of a simplicial scheme (the site of 09VL, which this development does not carry as a term of Situation 09WE) with the cartesian condition of `ZariskiCartesianModule`. Parts (1) and (2) of the source, for sheaves of sets and for objects of the derived category of the total site, and part (4), for the derived pullbacks, are not covered here; parts (1) and (2) for a simplicial-site situation are `CategoryTheory.SimplicialSiteSituation.isCartesianSheaf_iff_faces` and `isCartesianAbSheaf_iff_faces`”.

> **Stacks 07TG (3) for the total Zariski site of a simplicial scheme.** A sheaf of
> `𝒪_X`-modules on the total Zariski site of a simplicial scheme is cartesian if and only if the
> transition `(d^{k+1}_i)^* F_k ⟶ F_{k+1}` along every face map is an isomorphism.

```lean
public theorem isCartesianModule_iff_faces (X : SimplicialObject Scheme.{u}) (F : Modules X) :
    IsCartesianModule X F ↔
      ∀ (k : ℕ) (i : Fin (k + 2)),
        IsIso (componentModuleTransition X (SimplexCategory.δ i).op F)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerived_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedFaceCriterion.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedFaceCriterion.lean#L56). The attribute's comment: “face criterion for objects of D(C_total)”.

> **Stacks 07TG (2).** An object of the derived category of abelian sheaves on the total site
> of a simplicial site is cartesian if and only if the canonical derived transition along every
> face map is an isomorphism.

```lean
theorem isCartesianDerived_iff_faces (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    S.IsCartesianDerived K ↔
      ∀ (k : ℕ) (i : Fin (k + 2)),
        IsIso ((derivedTransition S (SimplexCategory.δ i)).app K)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianSheaf_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianFaceCriterion.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianFaceCriterion.lean#L44). The attribute's comment: “face criterion for sheaves of sets”.

> **Stacks 07TG.** A sheaf of sets on the total site of a simplicial site is cartesian if and
> only if the canonical transition along every face map is an isomorphism.

```lean
theorem isCartesianSheaf_iff_faces (F : Sheaf S.totalTopology (Type u)) :
    IsCartesianSheaf S F ↔
      ∀ (n : ℕ) (i : Fin (n + 2)),
        IsIso ((fiberTransition S (SimplexCategory.δ i)).app F)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianAbSheaf_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianFaceCriterion.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianFaceCriterion.lean#L74). The attribute's comment: “face criterion for sheaves of abelian groups”.

> **Stacks 07TG.** A sheaf of abelian groups on the total site of a simplicial site is
> cartesian if and only if the canonical transition along every face map is an isomorphism.

```lean
theorem isCartesianAbSheaf_iff_faces (F : Sheaf S.totalTopology Ab.{u}) :
    IsCartesianAbSheaf S F ↔
      ∀ (n : ℕ) (i : Fin (n + 2)),
        IsIso ((abelianFiberTransition S (SimplexCategory.δ i)).app F)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianModule_iff_faces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean#L286). The attribute's comment: “face criterion for sheaves of modules”.

> **Stacks 07TG (3).** A sheaf of `O`-modules on the total site of a simplicial site is
> cartesian if and only if the canonical transition along every face map is an isomorphism.
>
> The simplex maps whose transition is invertible form a multiplicative class, the identity and
> composition laws being the unit and cocycle laws `fiberTransitionModules_id` and
> `fiberTransitionModules_comp` of Stacks 09WF for modules. Every arrow of the simplex category is
> a composite of faces and degeneracies, and `SimplexCategory.δ_comp_σ_self` exhibits each
> degeneracy as the second factor of a composite that is an identity, so no separate hypothesis on
> the degeneracies is needed.

```lean
theorem isCartesianModule_iff_faces (M : SheafOfModules.{u} (S.totalRingSheaf O)) :
    IsCartesianModule S O M ↔
      ∀ (k : ℕ) (i : Fin (k + 2)),
        IsIso (S.fiberTransitionModules O (SimplexCategory.δ i) M)
```

## Tag 0D7H, a lemma

[Tag 0D7H](https://stacks.math.columbia.edu/tag/0D7H) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianDerivedModule_derivedPullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianDerivedModule.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianDerivedModule.lean#L138). The attribute's comment: “part (4)”.

> Let `E` be an object of `D(O_D)`. Then the derived pullback `La^*E` along the ringed
> augmentation of Stacks 0D9D is a cartesian object of `D(O)`: every derived transition
> `Lf_φ^*(La^*E)_m ⟶ (La^*E)_n` is an isomorphism.

```lean
theorem isCartesianDerivedModule_derivedPullbackModules
    (E : DerivedCategory A.augmentationRingedTopos.Modules) :
    S.IsCartesianDerivedModule A.O (A.derivedPullbackModules.obj E)
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.isCartesian_pullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianDerivedModule.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianDerivedModule.lean#L170).

> Let `a` be an augmentation of a simplicial-site situation towards a site `(D, K)`. Then every
> pullback along `a` is cartesian:
>
> 1. `a⁻¹𝒢`, for a sheaf of sets `𝒢` on `(D, K)` and for a sheaf of abelian groups `𝒢`;
> 2. `a⁻¹E`, for an object `E` of `D(D)`;
> 3. `a^*F`, for a ringed augmentation `A` of Stacks 0D9D and a sheaf of `O_D`-modules `F`;
> 4. `La^*E`, for a ringed augmentation `A` and an object `E` of `D(O_D)`.

```lean
theorem isCartesian_pullbacks (S : SimplicialSiteSituation.{u}) (D : Cat.{u, u})
    (K : GrothendieckTopology D) (a : Augmentation S D K) :
    ((∀ G : Sheaf K (Type u),
        IsCartesianSheaf S ((totalMorphismOfTopoi S D K a).inverseImage.obj G)) ∧
      ∀ G : Sheaf K Ab.{u}, IsCartesianAbSheaf S ((totalInverseImageAb S D K a).obj G)) ∧
    (∀ E : DerivedCategory (Sheaf K AddCommGrpCat.{u}),
      S.IsCartesianDerived ((derivedTotalInverseImage S D K a).obj E)) ∧
    (∀ (A : RingedAugmentation S D K a)
      (F : SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := A.augmentationRingedTopos.J)
          A.augmentationRingedTopos.O))),
      S.IsModuleFiberTransitionIso A.O (A.totalRingedHom.toModulesHom.pullbackModules.obj F)) ∧
    ∀ (A : RingedAugmentation S D K a) (E : DerivedCategory A.augmentationRingedTopos.Modules),
      S.IsCartesianDerivedModule A.O (A.derivedPullbackModules.obj E)
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianModule_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianModule.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationCartesianModule.lean#L192). The attribute's comment: “part (3)”.

> **Stacks 0D7H (3).** The pullback `a^*F` of a sheaf of `O_D`-modules along the ringed
> augmentation of Stacks 0D9D is a cartesian sheaf of `O`-modules on the total site: every
> transition `f_φ^*(a^*F)_m ⟶ (a^*F)_n` of sheaves of modules is invertible.
>
> The transition is the compositor of Stacks 03D8 followed by the transformation of pullbacks
> induced by the 2-morphism `g_n ⟶ g_m ∘ f_φ`, and that transformation is invertible after the
> pullback along the ringed augmentation by
> `CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_whiskerLeft_pullbackModulesMap`,
> which rests on Stacks 0D7H (1).

```lean
theorem isCartesianModule_pullbackModules
    (F : SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf A.augmentationRingedTopos.O)) :
    S.IsModuleFiberTransitionIso A.O ((A.totalRingedHom.toModulesHom.pullbackModules).obj F)
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.isCartesianSheaf_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesian.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesian.lean#L91). The attribute's comment: “part (1), sheaves of sets”.

> The inverse image along the total augmentation of a sheaf of sets on the augmentation site is
> a cartesian sheaf on the total site.

```lean
theorem isCartesianSheaf_inverseImage (G : Sheaf K (Type u)) :
    IsCartesianSheaf S ((inverseImage S D K a).obj G)
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.isCartesianAbSheaf_totalInverseImageAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesian.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesian.lean#L107). The attribute's comment: “part (1), sheaves of abelian groups”.

> The inverse image along the total augmentation of an abelian sheaf on the augmentation site
> is a cartesian abelian sheaf on the total site.

```lean
theorem isCartesianAbSheaf_totalInverseImageAb (G : Sheaf K Ab.{u}) :
    IsCartesianAbSheaf S ((totalInverseImageAb S D K a).obj G)
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.isCartesianDerived_derivedTotalInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesianDerived.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationCartesianDerived.lean#L53). The attribute's comment: “part (2), the derived inverse image of an object of D(D) is cartesian”.

> For an object `E` of the derived category of abelian sheaves on the augmentation site, the
> derived inverse image `a⁻¹E` is a cartesian object of the derived category of abelian sheaves on
> the total site.
>
> It suffices that every cohomology sheaf of `a⁻¹E` be cartesian
> (`isCartesianDerived_iff_forall_isCartesianAbSheaf_homology'`); those cohomology sheaves are the
> inverse images of the cohomology sheaves of `E`, since `a⁻¹` is exact, and the inverse image of
> an abelian sheaf along the augmentation is cartesian (`isCartesianAbSheaf_totalInverseImageAb`).

```lean
theorem isCartesianDerived_derivedTotalInverseImage
    (E : DerivedCategory (Sheaf K AddCommGrpCat.{u})) :
    S.IsCartesianDerived ((derivedTotalInverseImage S D K a).obj E)
```

## Tag 0D7I, a lemma

[Tag 0D7I](https://stacks.math.columbia.edu/tag/0D7I) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.cartesianAbSheafEquivCartesianAbPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianAbPairEquivalence.lean, line 1063](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianAbPairEquivalence.lean#L1063). The attribute's comment: “sheaves of abelian groups”.

> **Stacks 0D7I.** The category of cartesian sheaves of abelian groups on the total site of a
> simplicial-site situation is equivalent to the category of pairs `(ℱ, α)` consisting of a sheaf of
> abelian groups `ℱ` on the degree-zero component and an isomorphism
> `α : (f_{δ¹₁})⁻¹ℱ ≅ (f_{δ¹₀})⁻¹ℱ` of sheaves of abelian groups on the degree-one component
> satisfying the cocycle condition `(f_{δ²₁})⁻¹α = (f_{δ²₀})⁻¹α ∘ (f_{δ²₂})⁻¹α` on the degree-two
> component.

```lean
noncomputable def cartesianAbSheafEquivCartesianAbPair :
    CartesianAbSheaf S ≌ CartesianAbPair S
```

**`CategoryTheory.SimplicialSiteSituation.cartesianSheafEquivCartesianPair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianPairEquivalence.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianPairEquivalence.lean#L551). The attribute's comment: “sheaves of sets”.

> **Stacks 0D7I.** The category of cartesian sheaves of sets on the total site of a
> simplicial-site situation is equivalent to the category of pairs `(ℱ, α)` consisting of a sheaf
> of sets `ℱ` on the degree-zero component and an isomorphism `α : (f_{δ¹₁})⁻¹ℱ ≅ (f_{δ¹₀})⁻¹ℱ` of
> sheaves on the degree-one component satisfying the cocycle condition
> `(f_{δ²₁})⁻¹α = (f_{δ²₀})⁻¹α ∘ (f_{δ²₂})⁻¹α` on the degree-two component.

```lean
noncomputable def cartesianSheafEquivCartesianPair : CartesianSheaf S ≌ CartesianPair S
```

## Tag 07TH, a lemma

[Tag 07TH](https://stacks.math.columbia.edu/tag/07TH) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.cartesianModuleSheafEquivCartesianModulePair`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianModulePairEquivalence.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianModulePairEquivalence.lean#L176).

> **Stacks 07TH.** Let `S` be a simplicial-site situation and `O` a sheaf of commutative rings on
> its total site. The category of cartesian sheaves of `O`-modules is equivalent to the category of
> pairs `(ℱ, α)`, where `ℱ` is an `O₀`-module and `α : f_{δ¹₁}^*ℱ ≅ f_{δ¹₀}^*ℱ` is an isomorphism
> of `O₁`-modules such that `f_{δ²₁}^*α = f_{δ²₀}^*α ∘ f_{δ²₂}^*α` as `O₂`-module maps. The functor
> of the equivalence takes a cartesian module to its degree-zero restriction and the comparison of
> its two transitions to degree one.

```lean
def cartesianModuleSheafEquivCartesianModulePair :
    S.CartesianModuleSheaf O ≌ CartesianModulePair S O
```

## Tag 0D7J, a lemma

[Tag 0D7J](https://stacks.math.columbia.edu/tag/0D7J) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isCartesianAbSheaf_weakSerre_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerre.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerre.lean#L354). The attribute's comment: “part (1)”.

> **Stacks 0D7J (1).** The cartesian abelian sheaves on the total site of a simplicial site form
> a weak Serre subcategory of all abelian sheaves there, and colimits of systems of cartesian abelian
> sheaves are cartesian.

```lean
theorem isCartesianAbSheaf_weakSerre_colimits (S : SimplicialSiteSituation.{u}) :
    ObjectProperty.IsWeakSerreClass (IsCartesianAbSheaf S) ∧
      ∀ (J : Type*) [Category* J],
        ObjectProperty.IsClosedUnderColimitsOfShape (IsCartesianAbSheaf S) J
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianModule_isWeakSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean#L337). The attribute's comment: “part (2), cartesian modules are a weak Serre subcategory of Mod(O). The hypothesis is left exactness of the pullback of sheaves of modules along the transition morphism of each face map, which for a flat face transition is Stacks 04JC and is weaker than flatness of the face transitions, so the statement is more general than the source's; the implementation notes record why flatness itself cannot be fed in at this pullback. NOT covered here: the second sentence of part (2), that colimits of systems of cartesian O-modules are cartesian, for which the argument needs restriction of modules to a component to preserve colimits of arbitrary shape and this development has only the finite case”.

> Let `O` be a sheaf of rings on the total site of a simplicial site such that the pullback of
> sheaves of modules along the transition morphism of every face map is left exact. Then the
> cartesian `O`-modules form a weak Serre subcategory of `Mod(O)`.
>
> By Stacks 07TG (3) it is enough to test the face maps, which is why only the face transitions
> occur in the hypothesis; at a face the conditions are the zero module, which is cartesian with
> no hypothesis, and the four lemma applied to the transition read as a natural transformation of
> the two restriction functors.

```lean
theorem isCartesianModule_isWeakSerreClass
    (hflat : ∀ (k : ℕ) (i : Fin (k + 2)),
      PreservesFiniteLimits
        ((S.transitionRingedToposHom O (SimplexCategory.δ i)).toModulesHom.pullbackModules)) :
    ObjectProperty.IsWeakSerreClass (IsCartesianModule S O)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianModule_weakSerre_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianWeakSerreModules.lean#L428). The attribute's comment: “part (2)”.

> **Stacks 0D7J (2).** Let `O` be a sheaf of rings on the total site of a simplicial site such
> that the morphisms of ringed topoi `f_{δ^n_j} : (Sh(C_n), O_n) ⟶ (Sh(C_{n-1}), O_{n-1})` are
> flat. Then the cartesian `O`-modules form a weak Serre subcategory of `Mod(O)`, and colimits of
> systems of cartesian `O`-modules are cartesian.
>
> Flatness of a face transition makes its pullback of modules exact (Stacks 04JC), which is what
> the four lemma consumes; the colimit statement holds with no hypothesis.

```lean
theorem isCartesianModule_weakSerre_colimits
    (flat : ∀ (k : ℕ) (i : Fin (k + 2)),
      (S.transitionRingedToposHom O (SimplexCategory.δ i)).IsFlat) :
    ObjectProperty.IsWeakSerreClass (IsCartesianModule S O) ∧
      ∀ (J : Type*) [Category* J] [Small.{u} J],
        ObjectProperty.IsClosedUnderColimitsOfShape (IsCartesianModule S O) J
```

## Tag 0D7K, a remark

[Tag 0D7K](https://stacks.math.columbia.edu/tag/0D7K) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.cartesianModuleSheafAbelian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleAbelian.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleAbelian.lean#L556). The attribute's comment: “corrected form of the positive assertion, which is false as written (the source's hypothesis, flatness of f_{δ¹₁} and f_{δ¹₀} alone, does not suffice: see CategoryTheory.PointSimplicialSite.RatioCounterexample.exists_not_abelian_cartesianModuleSheaf); with one of f_{δ²₀}, f_{δ²₁}, f_{δ²₂} flat as well the cartesian O-modules form an abelian category, with the additive structure of Mod(O)”.

> **Stacks 0D7K, corrected form.** If the morphisms of ringed topoi `f_{δ¹₁}` and `f_{δ¹₀}` are
> flat, and so is one of the three degree-two faces `f_{δ²₀}`, `f_{δ²₁}`, `f_{δ²₂}`, then the
> cartesian `O`-modules form an abelian category, with the additive structure of `Mod(O)`; its
> cokernels are those of `Mod(O)`, and its kernels are those of the pairs of Stacks 07TH, computed
> in degree zero.
>
> The source asserts this under flatness of `f_{δ¹₁}` and `f_{δ¹₀}` alone, which is false: see
> `CategoryTheory.PointSimplicialSite.RatioCounterexample.exists_not_abelian_cartesianModuleSheaf`.
> The kernel of a morphism of pairs carries the restricted comparison isomorphism, but its cocycle
> condition lives on the degree-two component; it can be cancelled against the pullback of the
> kernel inclusion to the vertex `2` (through `δ²₁` or `δ²₀`) or to the vertex `0` (through `δ²₁`
> or `δ²₂`), which is a monomorphism as soon as one degree-two face is flat.

```lean
abbrev cartesianModuleSheafAbelian
    (h₁ : (S.transitionRingedToposHom O (SimplexCategory.δ (1 : Fin 2))).IsFlat)
    (h₀ : (S.transitionRingedToposHom O (SimplexCategory.δ (0 : Fin 2))).IsFlat)
    (h₂ : ∃ i : Fin 3, (S.transitionRingedToposHom O (SimplexCategory.δ i)).IsFlat) :
    Abelian (S.CartesianModuleSheaf O)
```

**`CategoryTheory.PointSimplicialSite.RatioCounterexample.exists_not_abelian_cartesianModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleCounterexample.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleCounterexample.lean#L483). The attribute's comment: “the positive assertion is false as written: counterexample with f_{δ¹₁} and f_{δ¹₀} flat but the cartesian O-modules not an abelian category (constant simplicial site on the point, O the cosimplicial ring of unit ratios); the corrected form is CategoryTheory.SimplicialSiteSituation.cartesianModuleSheafAbelian”.

> **Stacks 0D7K: the positive assertion is false as written.** There is a simplicial site
> (the constant simplicial site on the point, in case (A) of Stacks 09WE) and a sheaf of rings `O`
> on its total site (the cosimplicial ring of unit ratios
> `Rₙ = ℤ[xᵢ, wᵢⱼ^{±1} (i ≤ j)]/(xᵢ = wᵢⱼxⱼ, wᵢᵢ = 1)`) such that the morphisms of ringed topoi
> `f_{δ¹₁}` and `f_{δ¹₀}` are flat, but the category of cartesian `O`-modules is not abelian, for
> any choice of abelian structure: the quotient map `𝒪 ⟶ 𝒪/(x₀)` is a monomorphism and an
> epimorphism of cartesian modules, but not an isomorphism.

```lean
theorem exists_not_abelian_cartesianModuleSheaf :
    ∃ (S : SimplicialSiteSituation.{u}) (O : Sheaf S.totalTopology CommRingCat.{u}),
      (S.transitionRingedToposHom O (SimplexCategory.δ (1 : Fin 2))).IsFlat ∧
      (S.transitionRingedToposHom O (SimplexCategory.δ (0 : Fin 2))).IsFlat ∧
      IsEmpty (Abelian (S.CartesianModuleSheaf O))
```

**`CategoryTheory.PointSimplicialSite.SphereExample.exists_abelian_not_isSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleNotWeakSerre.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModuleNotWeakSerre.lean#L113). The attribute's comment: “the assertion that the category of cartesian O-modules can be abelian without being a Serre subcategory of Mod(O): an example with f_{δ¹₁}, f_{δ¹₀} flat where the cartesian O-modules form an abelian category but are neither a Serre nor a weak Serre subcategory of Mod(O). The source's remark that, when f_{δ²₀} is not flat, there is no reason for the inclusion into Mod(O) to be exact is a heuristic, not an assertion; in this example the non-flat transitions are those into degree three”.

> **Stacks 0D7K: cartesian modules can be abelian without being a Serre subcategory.** There is a
> simplicial site (the constant simplicial site on the point, in case (A) of Stacks 09WE) and a sheaf
> of rings `O` on its total site with `f_{δ¹₁}` and `f_{δ¹₀}` flat, such that the cartesian
> `O`-modules form an abelian category but are neither a Serre subcategory nor a weak Serre
> subcategory of `Mod(O)`: they are not closed under kernels in `Mod(O)`. Here `O` is the
> cosimplicial ring of functions on `Spec ℤ ⊔ (Δ[3] / ∂Δ[3])`; the non-flat transitions are those
> into degree three.

```lean
theorem exists_abelian_not_isSerreClass :
    ∃ (S : SimplicialSiteSituation.{u}) (O : Sheaf S.totalTopology CommRingCat.{u}),
      (S.transitionRingedToposHom O (SimplexCategory.δ (1 : Fin 2))).IsFlat ∧
      (S.transitionRingedToposHom O (SimplexCategory.δ (0 : Fin 2))).IsFlat ∧
      Nonempty (Abelian (S.CartesianModuleSheaf O)) ∧
      ¬ ObjectProperty.IsSerreClass (S.IsCartesianModule O) ∧
      ¬ ObjectProperty.IsWeakSerreClass (S.IsCartesianModule O)
```

**`CategoryTheory.SimplicialSiteSituation.CartesianModulePair.kernelIso_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModulePairExactness.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModulePairExactness.lean#L334). The attribute's comment: “the kernel half of the positive assertion, in degree one: under left exactness of f_{δ¹₁}^* and f_{δ¹₀}^* (which flatness of f_{δ¹₁} and f_{δ¹₀} gives by Stacks 04JC), the kernel of a morphism of the pairs of Stacks 07TH carries a comparison isomorphism restricting that of the source pair, and it is the only morphism that does. NOT covered here: the degree-two cocycle condition for that isomorphism, hence not the kernel object in the category of pairs and not the abelian structure; and not the assertion that the inclusion of cartesian O-modules into all O-modules fails to be exact, which the source states as the absence of a reason for exactness and not as a counterexample”.

> **Stacks 0D7K**, the kernel half of the positive assertion, in degree one. If the two
> degree-one pullbacks are left exact — which, for flat `f_{δ¹₁}` and `f_{δ¹₀}`, is Stacks 04JC —
> then the kernel of the degree-zero morphism of a morphism of pairs carries a comparison
> isomorphism restricting the comparison isomorphism of the source pair along the kernel
> inclusion.

```lean
theorem kernelIso_hom_comp :
    (kernelIso S O f).hom ≫
        (S.componentModulePullback O (SimplexCategory.δ (0 : Fin 2))).map (kernel.ι f.map) =
      (S.componentModulePullback O (SimplexCategory.δ (1 : Fin 2))).map (kernel.ι f.map) ≫
        A.iso.hom
```

**`CategoryTheory.SimplicialSiteSituation.CartesianModulePair.map_comp_cokernelIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModulePairExactness.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianModulePairExactness.lean#L378). The attribute's comment: “the cokernel half of the positive assertion, in degree one, and with no flatness hypothesis at all, the pullback of modules being right exact unconditionally: the cokernel of a morphism of the pairs of Stacks 07TH carries a comparison isomorphism corestricting that of the target pair, and it is the only morphism that does. NOT covered here: the degree-two cocycle condition for that isomorphism, hence not the cokernel object in the category of pairs and not the abelian structure; and not the assertion that the inclusion of cartesian O-modules into all O-modules fails to be exact, which the source states as the absence of a reason for exactness and not as a counterexample”.

> **Stacks 0D7K**, the cokernel half of the positive assertion, in degree one. The pullback of
> sheaves of modules is right exact unconditionally, so with no flatness hypothesis at all the
> cokernel of the degree-zero morphism of a morphism of pairs carries a comparison isomorphism
> corestricting the comparison isomorphism of the target pair along the cokernel projection.

```lean
theorem map_comp_cokernelIso_hom :
    (S.componentModulePullback O (SimplexCategory.δ (1 : Fin 2))).map (cokernel.π f.map) ≫
        (cokernelIso S O f).hom =
      B.iso.hom ≫
        (S.componentModulePullback O (SimplexCategory.δ (0 : Fin 2))).map (cokernel.π f.map)
```

## Tag 0D7L, a lemma

[Tag 0D7L](https://stacks.math.columbia.edu/tag/0D7L) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerivedModule_iff_forall_isCartesianModule_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleCohomology.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleCohomology.lean#L151). The attribute's comment: “part (2), cartesian objects of D(O) for flat face transitions”.

> Let `O` be a sheaf of rings on the total site of a simplicial site such
> that the morphisms of ringed topoi `f_{δ^n_j} : (Sh(C_n), O_n) ⟶ (Sh(C_{n-1}), O_{n-1})` of the
> face maps are flat. Then an object `K` of `D(O)` is cartesian if and only if `H^q(K)` is a
> cartesian `O`-module for all `q`.

```lean
theorem isCartesianDerivedModule_iff_forall_isCartesianModule_homology
    (flat : ∀ (k : ℕ) (i : Fin (k + 2)),
      (S.transitionRingedToposHom O (SimplexCategory.δ i)).IsFlat)
    (K : DerivedCategory (S.totalRingedTopos O).Modules) :
    S.IsCartesianDerivedModule O K ↔
      ∀ q : ℤ, IsCartesianModule S O
        ((DerivedCategory.homologyFunctor (S.totalRingedTopos O).Modules q).obj K)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerived_iff_forall_isCartesianAbSheaf_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedCohomology.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedCohomology.lean#L92). The attribute's comment: “cartesian derived sheaves are those with cartesian cohomology”.

> **Stacks 0D7L (1).** An object of the derived category of abelian sheaves on the total site of
> a simplicial site is cartesian if and only if all of its cohomology sheaves are cartesian abelian
> sheaves.

```lean
theorem isCartesianDerived_iff_forall_isCartesianAbSheaf_homology
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    IsCartesianDerived' S K ↔
      ∀ q : ℤ, IsCartesianAbSheaf S
        ((DerivedCategory.homologyFunctor (Sheaf S.totalTopology Ab.{u}) q).obj K)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerived_iff_forall_isCartesianAbSheaf_homology'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedSheaves.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedSheaves.lean#L454). The attribute's comment: “cartesian derived sheaves are those with cartesian cohomology”.

> **Stacks 0D7L (1).** An object of the derived category of abelian sheaves on the total site of
> a simplicial site is cartesian if and only if all of its cohomology sheaves are cartesian abelian
> sheaves.

```lean
theorem isCartesianDerived_iff_forall_isCartesianAbSheaf_homology'
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    IsCartesianDerived S K ↔
      ∀ q : ℤ, IsCartesianAbSheaf S
        ((DerivedCategory.homologyFunctor (Sheaf S.totalTopology Ab.{u}) q).obj K)
```

## Tag 0D9E, a lemma

[Tag 0D9E](https://stacks.math.columbia.edu/tag/0D9E) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerivedModule_iff_forall_isIso_moduleProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleProjectionSituation.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleProjectionSituation.lean#L82). The attribute's comment: “part (2)”.

> **Stacks 0D9E (2).** In a simplicial-site situation (Stacks 09WE, either case) let `O` be a
> sheaf of rings on the total site such that the structure-sheaf transitions `f_φ^{-1}O_n ⟶ O_m`
> are flat for every simplex map `φ : [n] ⟶ [m]`. Then an object `K` of `D(O)` is cartesian if and
> only if the canonical map `g_{n!}K_n ⟶ g_{n!}O_n ⊗^L_O K` is an isomorphism for every `n`.

```lean
theorem isCartesianDerivedModule_iff_forall_isIso_moduleProjection
    (hflat : ∀ (n m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom O φ).IsFlat)
    (K : DerivedCategory (S.totalRingedTopos O).Modules) :
    S.IsCartesianDerivedModule O K ↔
      ∀ n : SimplexCategory, IsIso (S.moduleProjection O n (hflat n) K)
```

**`CategoryTheory.SimplicialSiteSituation.isCartesianDerived_iff_isIso_integerProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedLowerShriek.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/CartesianDerivedLowerShriek.lean#L246). The attribute's comment: “part (1)”.

> **Stacks 0D9E (1).** An object `K` of `D(𝒞_total)` is cartesian if and only if the canonical
> map `g_{n!}K_n ⟶ g_{n!}ℤ ⊗^L_ℤ K` is an isomorphism for every simplicial degree `n`.
>
> Since `K` is cartesian exactly when all of its cohomology sheaves are (Stacks 0D7L), this is the
> sheaf-level statement `isCartesianAbSheaf_iff_isIso_componentLowerShriekMap` read through
> `isIso_integerProjection_iff`.

```lean
theorem isCartesianDerived_iff_isIso_integerProjection
    (K : DerivedCategory (Sheaf S.totalTopology Ab.{u})) :
    S.IsCartesianDerived K ↔ ∀ n : SimplexCategory, IsIso (S.integerProjection K n)
```

## Tag 0D7M, a lemma

[Tag 0D7M](https://stacks.math.columbia.edu/tag/0D7M) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.IsCartesianWithQuasicoherentComponents`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/QuasicoherentCartesian.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/QuasicoherentCartesian.lean#L208). The attribute's comment: “the right-hand side of the equivalence only: `F` is cartesian in the sense of 07TF (2) and every component module `F_n` is a quasi-coherent `O_n`-module in the sense of 03DL (6). Neither direction of the equivalence with quasi-coherence of `F` on the total site is proved: both need a localization of the total site at an object, which the development does not have”.

> **The right-hand side of Stacks 0D7M.** A sheaf of `O`-modules on the total site of a
> simplicial-site situation is cartesian in the sense of Stacks 07TF (2) and each of its
> component modules `F_n` is a quasi-coherent `O_n`-module in the sense of Stacks 03DL (6).
>
> The source asserts that this condition is equivalent to quasi-coherence of `F` itself on the
> total site; that equivalence is not proved in this development.

```lean
noncomputable abbrev IsCartesianWithQuasicoherentComponents
    (F : SheafOfModules.{u} (S.totalRingSheaf O)) : Prop
```

**`CategoryTheory.SimplicialSiteSituation.isQuasicoherentOnSite_iff_isCartesianModule_and_isQuasicoherentOnSite_componentModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasicoherentCartesian/Equivalence.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasicoherentCartesian/Equivalence.lean#L59).

> **Stacks 0D7M.** In Situation 09WE, let `O` be a sheaf of rings on the total site and `F` a
> sheaf of `O`-modules. Then `F` is quasi-coherent in the sense of Stacks 03DL if and only if `F` is
> cartesian in the sense of Stacks 07TF (2) and every component `Fₙ` is a quasi-coherent
> `Oₙ`-module.
>
> The right-hand side is
> `CategoryTheory.SimplicialSiteSituation.IsCartesianWithQuasicoherentComponents`, spelled out.

```lean
theorem isQuasicoherentOnSite_iff_isCartesianModule_and_isQuasicoherentOnSite_componentModule
    (S : SimplicialSiteSituation.{u}) (O : Sheaf S.totalTopology CommRingCat.{u})
    (F : SheafOfModules.{u} (S.totalRingSheaf O)) :
    F.IsQuasicoherentOnSite ↔
      S.IsCartesianModule O F ∧
        ∀ n : SimplexCategory, (S.componentModule O F n).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_iff_isCartesianModule_and_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiQuasicoherentCartesian.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiQuasicoherentCartesian.lean#L198). The attribute's comment: “for the total Zariski site of a simplicial scheme, which is the site of 09VL; the cartesian condition is `AlgebraicGeometry.SimplicialScheme.IsCartesianModule`, 07TF (2) at the transition of 09WF, and quasi-coherence of the components is 03DL (6) over the structure sheaf of the degree, with the component functors of `ZariskiModulePushforward`”.

> **Stacks 0D7M for the total Zariski site of a simplicial scheme.** A sheaf of `𝒪_X`-modules
> on the total Zariski site is quasi-coherent in the sense of Stacks 03DL (6) if and only if it is
> cartesian in the sense of Stacks 07TF (2) and every one of its component modules `F_n` is a
> quasi-coherent `𝒪_{X_n}`-module.

```lean
public theorem isQuasicoherentOnSite_iff_isCartesianModule_and_components (F : Modules X) :
    F.IsQuasicoherentOnSite ↔
      IsCartesianModule X F ∧
        ∀ k : SimplexCategoryᵒᵖ,
          ((componentModule X k).obj F).IsQuasicoherentOnSite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.12, Tag 0D7G](https://stacks.math.columbia.edu/tag/0D7G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
