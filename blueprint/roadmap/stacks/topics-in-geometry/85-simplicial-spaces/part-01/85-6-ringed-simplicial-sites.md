---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.componentRingedTopos_restrictionIso, CategoryTheory.SimplicialSiteSituation.componentRingedTopos_restrictionIso_forget, CategoryTheory.SimplicialSiteSituation.componentRingedToposHom, CategoryTheory.SimplicialSiteSituation.componentRingedToposHom_toToposHom, CategoryTheory.SimplicialSiteSituation.moduleSumFormulaLegEq, CategoryTheory.SimplicialSiteSituation.componentRingedToposHom_fSharpInverseImageRing_ringSheafMap, CategoryTheory.SimplicialSiteSituation.componentPullbackModulesRestrictionIso, CategoryTheory.SimplicialSiteSituation.componentPullbackModulesRestrictionIso_underlying
statement: formalized
proof: formalized
---

# 85.6 Ringed simplicial sites

Section 85.6 of the Stacks Project, [Tag 0D71](https://stacks.math.columbia.edu/tag/0D71). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D72, a lemma

[Tag 0D72](https://stacks.math.columbia.edu/tag/0D72) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentRingedTopos_restrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean#L134). The attribute's comment: “component_ringed_topos”.

> The inverse image of sheaves of commutative rings along the component morphism of topoi is
> canonically and naturally isomorphic to restriction along the component inclusion.

```lean
noncomputable def componentRingedTopos_restrictionIso (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) :
    inverseImageCommRingFunctor (J := S.componentTopology n) (K := S.totalTopology)
        (componentMorphism S n) ≅
      (componentFunctor S n).sheafPushforwardContinuous CommRingCat.{u}
        (S.componentTopology n) S.totalTopology
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedTopos_restrictionIso_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean#L148). The attribute's comment: “component_ringed_topos”.

> The restriction isomorphism is the canonical comparison of Stacks 09WG after forgetting the
> ring operations. In particular its scalar map is not an arbitrary natural automorphism of
> restriction.

```lean
theorem componentRingedTopos_restrictionIso_forget (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) (O : Sheaf S.totalTopology CommRingCat.{u}) :
    (sheafCompose (S.componentTopology n) (forget CommRingCat.{u})).map
        ((componentRingedTopos_restrictionIso S n).hom.app O) =
      (inverseImageCommRingForgetIso (S.componentTopology n)
          (componentMorphism S n)).hom.app O ≫
        ((componentFunctor S n).sheafPullbackCocontinuousIsoSheafPushforwardContinuous
          (Type u) (S.componentTopology n) S.totalTopology).hom.app
          ((sheafCompose S.totalTopology (forget CommRingCat.{u})).obj O)
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean#L166). The attribute's comment: “component_ringed_topos”.

> The canonical morphism of ringed topoi from a simplicial component to the total site. Its
> structure map is the adjoint of the comparison `gₙ⁻¹O ⟶ Oₙ` of structure sheaves.

```lean
noncomputable def componentRingedToposHom (S : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology CommRingCat.{u}) (n : SimplexCategory) :
    RingedToposHom (componentRingedTopos S O n) (totalRingedTopos S O)
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedToposHom_toToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Basic.lean#L176). The attribute's comment: “component_ringed_topos”.

> The underlying geometric morphism is the component morphism of Stacks 09WG.

```lean
theorem componentRingedToposHom_toToposHom (S : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology CommRingCat.{u}) (n : SimplexCategory) :
    (componentRingedToposHom S O n).toToposHom = componentMorphism S n
```

**`CategoryTheory.SimplicialSiteSituation.moduleSumFormulaLegEq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleOfModuleSystem.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/CartesianDerivedModuleOfModuleSystem.lean#L72). The attribute's comment: “the summand inclusions of the direct-sum formula on sheaves of modules are the canonical maps f_φ^*G ⟶ g_m^*g_{n!}G, in Situation 09WE (both cases)”.

> **The leg equation of Stacks 0D72 (6) in every simplicial-site situation.** For every simplex
> map `φ : [n] ⟶ [m]` the `φ`th summand inclusion of the componentwise direct-sum formula for
> sheaves of modules, followed by the inverse of that formula, is the canonical map attached to
> `φ`. In case (A) of Stacks 09WE this is
> `CategoryTheory.SimplicialSite.moduleSumFormulaLegEq_situation`, and in case (B) it is
> `CategoryTheory.CocontinuousSimplicialSite.moduleSumFormulaLegEqB`.

```lean
theorem moduleSumFormulaLegEq : S.ModuleSumFormulaLegEq O
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedToposHom_fSharpInverseImageRing_ringSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackRestriction.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackRestriction.lean#L107). The attribute's comment: “the structure map of the component morphism on underlying sheaves of sets”.

> **The inverse-image form of the structure map of `g_n` on underlying sheaves of sets is the
> comparison of Stacks 09WG.** The structure map is recorded through the adjunction for sheaves of
> commutative rings and used through the adjunction for sheaves of rings; the two agree on
> underlying sheaves of sets, where the first is Stacks 09WG by construction of the component
> ringed topos.

```lean
theorem componentRingedToposHom_fSharpInverseImageRing_ringSheafMap :
    (sheafCompose (S.componentTopology n) (forget RingCat.{u})).map
        (componentRingedToposHom S O n).fSharpInverseImageRing =
      (componentRingedTopos_setRestrictionIso S n).hom.app
        ((sheafCompose S.totalTopology (forget CommRingCat.{u})).obj O)
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackModulesRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackRestriction.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackRestriction.lean#L171). The attribute's comment: “the pullback of modules along g_n is restriction to the component”.

> **Stacks 0D72: the pullback of sheaves of modules to a simplicial component is the literal
> restriction.** The two presentations of restriction to the degree-`n` component that this
> development carries — pullback of modules along the component morphism of ringed topoi, and
> restriction of sections along the component inclusion — are canonically isomorphic.

```lean
def componentPullbackModulesRestrictionIso :
    (componentRingedToposHom S O n).toModulesHom.pullbackModules ≅
      S.componentModulesRestriction O n
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackModulesRestrictionIso_underlying`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackUnderlying.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentPullbackUnderlying.lean#L210). The attribute's comment: “the comparison of the two presentations of restriction, on underlying sheaves of sets”.

> **Stacks 0D72 on underlying sheaves of sets is Stacks 09WG.** Read through the identification
> of the underlying sheaf of a pullback of modules with an inverse image, the comparison of
> Stacks 0D72 between the pullback of sheaves of modules along the component morphism of ringed
> topoi and the literal restriction to the component is the comparison of Stacks 09WG between the
> inverse image of sheaves of sets and restriction along the component inclusion.

```lean
theorem componentPullbackModulesRestrictionIso_underlying
    (M : SheafOfModules.{u} (S.totalRingSheaf O)) :
    (AlgebraicGeometry.RingedToposHom.pullbackUnderlyingIsoOfIsIso
          (componentRingedToposHom S O n)).inv.app M ≫
        (Sheaf.moduleSheafFunctor
            (Stacks.SheafOfModules.Tensor.ringSheaf (S.componentRingedTopos O n).O)).map
          ((componentPullbackModulesRestrictionIso S O n).hom.app M) =
      (componentRingedTopos_setRestrictionIso S n).hom.app
        (Sheaf.moduleSheaf.{u, u, u} (S.totalRingSheaf O) M)
```

**`CategoryTheory.SimplicialSiteSituation.componentPullbackComplexRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean#L84). The attribute's comment: “degreewise pullback of complexes along g_n is degreewise restriction”.

> **Stacks 0D72 on cochain complexes.** Degreewise pullback of complexes of modules along the
> component morphism of ringed topoi is degreewise restriction to the component.

```lean
def componentPullbackComplexRestrictionIso :
    Stacks.Sheaves.DerivedPullback.pullbackComplexFunctor
        (X := S.componentRingedTopos O n) (Y := S.totalRingedTopos O)
        (componentRingedToposHom S O n).toModulesHom ≅
      S.componentModulesRestrictionComplex O n
```

**`CategoryTheory.SimplicialSiteSituation.componentModuleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriek.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriek.lean#L128). The attribute's comment: “existence of the left adjoint g_{n!} of g_n^* on modules”.

> **Stacks 0D72.** The defining adjunction `g_{n!} ⊣ g_n^*` of lower shriek of modules on a
> simplicial component, exhibiting the left adjoint `g_{n!}` of `g_n^*` whose existence the tag
> asserts.

```lean
noncomputable def componentModuleLowerShriekAdjunction :
    componentModuleLowerShriek S O n ⊣ componentModuleRestriction S O n
```

**`CategoryTheory.SimplicialSite.componentModuleSumFormulaA`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaCaseA.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaCaseA.lean#L137). The attribute's comment: “direct-sum formula in case (A), on sheaves of modules”.

> **Stacks 0D72, the componentwise direct-sum formula for sheaves of modules in case (A).**
> The restriction to simplicial degree `m` of lower shriek `g_{n!}` of sheaves of `O`-modules from
> degree `n` is the direct sum, over the simplex maps `φ : [n] ⟶ [m]`, of the pullbacks `f_φ^*` of
> sheaves of modules along the transitions, each taken along the ring map `O(φ)`.

```lean
def componentModuleSumFormulaA (n m : SimplexCategory) :
    (∐ fun φ : n ⟶ m => transitionModulePullbackA C O φ) ≅
      (situation C).componentModuleLowerShriek O n ⋙
        (situation C).componentModuleRestriction O m
```

**`CategoryTheory.CocontinuousSimplicialSite.componentModuleSumFormulaB`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaCaseB.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaCaseB.lean#L155). The attribute's comment: “direct-sum formula in case (B), on sheaves of modules”.

> **The componentwise direct-sum formula for sheaves of modules in case (B).** The restriction
> to simplicial degree `m` of lower shriek `g_{n!}` of sheaves of `O`-modules from degree `n` is the
> direct sum, over the simplex maps `φ : [n] ⟶ [m]`, of the pullbacks `f_φ^*` of sheaves of modules
> along the transitions.

```lean
def componentModuleSumFormulaB :
    (∐ fun φ : n ⟶ m => transitionModulePullbackB C P n m φ) ≅
      (situation C).componentModuleLowerShriek (totalRingSheafB C P) n ⋙
        (situation C).componentModuleRestriction (totalRingSheafB C P) m
```

**`CategoryTheory.SimplicialSiteSituation.moduleSumFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean#L101). The attribute's comment: “direct-sum formula on sheaves of modules, in Situation 09WE (both cases)”.

> **The componentwise direct-sum formula of Stacks 0D72 (6) for sheaves of modules**, for an
> arbitrary simplicial-site situation and in the summand spelling Stacks 0D74 consumes: the
> restriction to degree `m` of lower shriek from degree `n` is the direct sum, over the simplex maps
> `φ : [n] ⟶ [m]`, of the pullbacks of sheaves of modules along the transition morphisms of ringed
> topoi.
>
> A situation is one of the two cases of Stacks 09WE, and the formula is proved in each:
> `CategoryTheory.SimplicialSite.moduleSumFormulaA` in case (A), where the transitions are
> morphisms of sites, and `CategoryTheory.CocontinuousSimplicialSite.moduleSumFormulaB` in case
> (B), where they are cocontinuous functors.

```lean
def moduleSumFormula : ∀ (S : SimplicialSiteSituation.{u})
    (P : Sheaf S.totalTopology CommRingCat.{u}) (n : SimplexCategory), S.ModuleSumFormula' P n
```

**`Stacks.Sites.ComponentModuleSumFormula.colimitPullbackRestrictionIsoCoproduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentModuleSumFormulaPresheaf.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentModuleSumFormulaPresheaf.lean#L220). The attribute's comment: “direct-sum formula in case (B), on presheaves of modules”.

> The restriction to simplicial degree `m` of the presheaf-level module lower shriek from degree
> `n` is, as a functor, the direct sum over the simplex maps `φ : [n] ⟶ [m]` of the presheaf-level
> module pullbacks `f_φ^*` along the transitions, the summand labelled `φ` being the pullback along
> the transition of `φ`.

```lean
noncomputable def colimitPullbackRestrictionIsoCoproduct :
    Stacks.PullbackColimit.colimitPullback (Grothendieck.ι C.underlying (op n)) R ⋙
        PresheafOfModules.pushforward₀OfCommRingCat
          (Grothendieck.ι C.underlying (op m)) R ≅
      ∐ fun φ : n ⟶ m => transitionPullbackPresheafModules C R φ
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedToposHom_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean, line 711](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RingedToposMorphism.lean#L711). The attribute's comment: “the structure map of the component morphism, in inverse-image form”.

> The structure map of the canonical morphism from a simplicial component to the total ringed
> topos is, in inverse-image form, the comparison of structure sheaves of Stacks 0D72.

```lean
theorem componentRingedToposHom_fSharpInverseImage (S : SimplicialSiteSituation.{u})
    (O : Sheaf S.totalTopology CommRingCat.{u}) (n : SimplexCategory) :
    (componentRingedToposHom S O n).fSharpInverseImage =
      (componentRingedTopos_restrictionIso S n).hom.app O
```

## Tag 0D73, a lemma

[Tag 0D73](https://stacks.math.columbia.edu/tag/0D73) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isTotallyAcyclic_component_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentTotalAcyclicity.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentTotalAcyclicity.lean#L83).

> **Stacks Project, Tag 0D73.** Let `O` be a sheaf of rings on the total site of a
> simplicial-site situation and let `I` be an injective sheaf of `O`-modules. The abelian sheaf
> underlying the restriction `I_n` of `I` to the degree-`n` simplicial component is totally
> acyclic: its cohomology over every sheaf of sets on `C_n` vanishes in every positive degree.

```lean
theorem isTotallyAcyclic_component_of_injective
    [HasExt.{u} (Sheaf (S.componentTopology n) AddCommGrpCat.{u})]
    [HasExt.{u} (Sheaf S.totalTopology AddCommGrpCat.{u})]
    (O : Sheaf S.totalTopology RingCat.{u}) (I : SheafOfModules.{u} O) [Injective I] :
    IsTotallyAcyclic.{u} (S.componentTopology n)
      ((S.restrictAb n).obj ((SheafOfModules.toSheaf O).obj I))
```

**`CategoryTheory.SimplicialSiteSituation.isTotallyAcyclic_componentModule_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentTotalAcyclicity.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentTotalAcyclicity.lean#L118). The attribute's comment: “the conclusion read on the restricted sheaf of modules rather than on the restriction of the underlying abelian sheaf”.

> **Stacks Project, Tag 0D73**, with the conclusion read on the restricted sheaf of modules.
> The restriction of an injective sheaf of `O`-modules to the degree-`n` simplicial component —
> reindexing the sections and restricting the scalars along the identity of the restricted sheaf
> of rings — has totally acyclic underlying abelian sheaf.

```lean
theorem isTotallyAcyclic_componentModule_of_injective
    [HasExt.{u} (Sheaf (S.componentTopology n) AddCommGrpCat.{u})]
    [HasExt.{u} (Sheaf S.totalTopology AddCommGrpCat.{u})]
    (O : Sheaf S.totalTopology RingCat.{u}) (I : SheafOfModules.{u} O) [Injective I] :
    IsTotallyAcyclic.{u} (S.componentTopology n)
      ((SheafOfModules.toSheaf _).obj
        ((SheafOfModules.pushforward (F := componentFunctor S n)
          (𝟙 (((componentFunctor S n).sheafPushforwardContinuous RingCat.{u}
            (S.componentTopology n) S.totalTopology).obj O))).obj I))
```

## Tag 0D74, a lemma

[Tag 0D74](https://stacks.math.columbia.edu/tag/0D74) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.exactFunctor_componentModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriekExact.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriekExact.lean#L194). The attribute's comment: “with the componentwise direct-sum formula of Tag 0D72 proved in either case of 09WE”.

> **Stacks 0D74.** Lower shriek `g_{n!}` of sheaves of modules from the degree-`n` simplicial
> component is exact as soon as every structure-sheaf transition `f_φ⁻¹O_n ⟶ O_m` out of degree `n`
> is flat.
>
> Right exactness is formal. For left exactness: the restrictions to the components detect finite
> limits, the componentwise direct-sum formula of Stacks 0D72
> (`CategoryTheory.SimplicialSiteSituation.moduleSumFormula`) presents the restriction of `g_{n!}`
> to degree `m` as the direct sum over the finitely many simplex maps `[n] ⟶ [m]` of the transition
> pullbacks, hence as their product, and each of those is left exact by Stacks 04JC. This is
> `CategoryTheory.SimplicialSiteSituation.exactFunctor_componentModuleLowerShriek'`.

```lean
theorem exactFunctor_componentModuleLowerShriek
    (hflat : ∀ (m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom P φ).IsFlat) :
    exactFunctor
      (SheafOfModules.{u} (S.componentRingSheaf ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) P) n))
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) P))
      (S.componentModuleLowerShriek ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) P) n)
```

**`CategoryTheory.SimplicialSiteSituation.exactFunctor_componentModuleLowerShriek'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean#L118).

> **Stacks 0D74.** Lower shriek `g_{n!}` of sheaves of modules from the degree-`n` simplicial
> component is exact as soon as every structure-sheaf transition `f_φ⁻¹O_n ⟶ O_m` out of degree `n`
> is flat.
>
> Right exactness is formal. For left exactness: the restrictions to the components detect finite
> limits, the componentwise direct-sum formula of Stacks 0D72 presents the restriction of `g_{n!}`
> to degree `m` as the direct sum over the finitely many simplex maps `[n] ⟶ [m]` of the transition
> pullbacks, hence as their product, and each of those is left exact by Stacks 04JC.

```lean
theorem exactFunctor_componentModuleLowerShriek'
    (hflat : ∀ (m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom P φ).IsFlat) :
    exactFunctor
      (SheafOfModules.{u} (S.componentRingSheaf
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology) P)) n))
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology) P)))
      (S.componentModuleLowerShriek
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology) P)) n)
```

## Tag 0D75, a lemma

[Tag 0D75](https://stacks.math.columbia.edu/tag/0D75) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.injective_componentModuleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriekExact.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleLowerShriekExact.lean#L227). The attribute's comment: “with the componentwise direct-sum formula of Tag 0D72 proved in either case of 09WE”.

> **Stacks 0D75.** Let `O` be a sheaf of rings on the total site whose structure-sheaf
> transitions `f_φ⁻¹O_n ⟶ O_m` out of degree `n` are flat. An injective sheaf of `O`-modules
> restricts to an injective sheaf of `O_n`-modules on the degree-`n` simplicial component.
>
> Restriction is right adjoint to `g_{n!}`, which is exact by Stacks 0D74, so Homology 015Z
> applies; the componentwise direct-sum formula of Tag 0D72 that Stacks 0D74 starts from is
> `CategoryTheory.SimplicialSiteSituation.moduleSumFormula`.

```lean
theorem injective_componentModuleRestriction
    (hflat : ∀ (m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom P φ).IsFlat)
    (I : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) P)) [Injective I] :
    Injective ((S.componentModuleRestriction ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology)) P) n).obj I)
```

**`CategoryTheory.SimplicialSiteSituation.injective_componentModuleRestriction'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleSumFormulaSituation.lean#L177).

> **Stacks 0D75.** Let `O` be a sheaf of rings on the total site whose structure-sheaf
> transitions `f_φ⁻¹O_n ⟶ O_m` out of degree `n` are flat. An injective sheaf of `O`-modules
> restricts to an injective sheaf of `O_n`-modules on the degree-`n` simplicial component.
>
> Restriction is right adjoint to `g_{n!}`, which is exact by Stacks 0D74, so Homology 015Z
> applies.

```lean
theorem injective_componentModuleRestriction'
    (hflat : ∀ (m : SimplexCategory) (φ : n ⟶ m), (S.transitionRingedToposHom P φ).IsFlat)
    (I : SheafOfModules.{u}
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology) P))) [Injective I] :
    Injective ((S.componentModuleRestriction
      ((Stacks.SheafOfModules.Tensor.ringSheaf (J := S.totalTopology) P)) n).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.6, Tag 0D71](https://stacks.math.columbia.edu/tag/0D71)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
