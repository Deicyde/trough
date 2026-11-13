---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_derived, AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriek_derived, AlgebraicGeometry.Stack.FlatFppf.lowerShriekModules_derived, AlgebraicGeometry.Stack.LisseEtale.lowerShriekModules_derived, AlgebraicGeometry.Stack.FlatFppf.derivedRestrictionBaseChangeIso, AlgebraicGeometry.Stack.FlatFppf.derivedLowerShriekBaseChangeIso, AlgebraicGeometry.Stack.FlatFppf.moduleDerivedRestrictionBaseChangeIso, AlgebraicGeometry.Stack.FlatFppf.moduleDerivedLowerShriekBaseChangeIso
statement: formalized
proof: formalized
---

# 104.3 The lisse-étale and the flat-fppf sites

Section 104.3 of the Stacks Project, [Tag 08MZ](https://stacks.math.columbia.edu/tag/08MZ). 3 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07AS, a lemma

[Tag 07AS](https://stacks.math.columbia.edu/tag/07AS) in the Stacks Project.

**`AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriek_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean#L67). The attribute's comment: “part (1), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on abelian sheaves for the lisse-étale site, its adjunction `Lg_! ⊣ g⁻¹` (with invertible unit), and `g⁻¹ ∘ Lg_! = id`, for every algebraic stack, with no hypothesis. The acyclicity statement of Tag 07AC is proved, as `AlgebraicGeometry.Stack.LisseEtale.abelianLowerShriekAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (1)**, all three assertions, for every algebraic stack and with NO hypothesis.
> For `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_{étale})` the comparison morphism of topoi of
> **Stacks 0788** (1):
>
> * the functor `g_! : Ab(𝒳_{lisse,étale}) ⥤ Ab(𝒳_{étale})` has a left derived functor
>   `Lg_! : D(𝒳_{lisse,étale}) ⟶ D(𝒳_{étale})` — degreewise `g_!` followed by the localization of
>   the homotopy category of `Ab(𝒳_{étale})` has a pointwise left derived functor along the
>   localization of the homotopy category of `Ab(𝒳_{lisse,étale})`, and `Lg_!` is that total left
>   derived functor;
> * `Lg_!` is left adjoint to `g⁻¹`, by an adjunction whose unit is an isomorphism;
> * `g⁻¹ ∘ Lg_! = id`.

```lean
theorem abelianLowerShriek_derived :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isCocontinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := abelianLowerShriek_additive.{u, w} B S hS 𝒳
    ((abelianLowerShriek.{u, w} B S hS 𝒳
        (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ)) ∧
    (∃ adj : derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⊣
        derivedAbelianRestriction.{u, w} B S hS 𝒳, IsIso adj.unit) ∧
    Nonempty (derivedAbelianLowerShriek.{u, w} B S hS 𝒳 ⋙
        derivedAbelianRestriction.{u, w} B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AbCat.{u, u + 1})))
```

**`AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriek_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteAbelianDerivedLowerShriek.lean#L109). The attribute's comment: “part (3), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on abelian sheaves for the flat-fppf site, its adjunction `Lg_! ⊣ g⁻¹` (with invertible unit), and `g⁻¹ ∘ Lg_! = id`, for every algebraic stack, with no hypothesis. The acyclicity statement of Tag 07AC is proved, as `AlgebraicGeometry.Stack.FlatFppf.abelianLowerShriekAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (3)**, all three assertions, for every algebraic stack and with NO hypothesis.
> For `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_{fppf})` the comparison morphism of topoi of
> **Stacks 0788** (2):
>
> * the functor `g_! : Ab(𝒳_{flat,fppf}) ⥤ Ab(𝒳_{fppf})` has a left derived functor
>   `Lg_! : D(𝒳_{flat,fppf}) ⟶ D(𝒳_{fppf})` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Ab(𝒳_{fppf})` has a pointwise left derived functor along the localization
>   of the homotopy category of `Ab(𝒳_{flat,fppf})`, and `Lg_!` is that total left derived functor;
> * `Lg_!` is left adjoint to `g⁻¹`, by an adjunction whose unit is an isomorphism;
> * `g⁻¹ ∘ Lg_! = id`.

```lean
theorem abelianLowerShriek_derived :
    haveI := isContinuous_inclusion B S hS 𝒳 flatClosure
    haveI := isCocontinuous_inclusion B S hS 𝒳 flatClosure
    haveI := abelianLowerShriek_additive B S hS 𝒳
    ((abelianLowerShriek B S hS 𝒳 flatClosure).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      (HomotopyCategory.quasiIso
        (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1}) (ComplexShape.up ℤ)) ∧
    (∃ adj : derivedAbelianLowerShriekFunctor B S hS 𝒳 ⊣ derivedAbelianRestriction B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedAbelianLowerShriekFunctor B S hS 𝒳 ⋙ derivedAbelianRestriction B S hS 𝒳 ≅
      𝟭 (DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AbCat.{u, u + 1})))
```

**`AlgebraicGeometry.Stack.FlatFppf.lowerShriekModules_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean#L448). The attribute's comment: “part (4), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on sheaves of modules for the flat-fppf site, its adjunction `Lg_! ⊣ g^*` (with invertible unit), and `g^* ∘ Lg_! = id`, for every algebraic stack, with no hypothesis. The structure sheaf is the one of Tag 06TV; the acyclicity statement of Tag 07AC is proved, as `AlgebraicGeometry.Stack.subsiteLowerShriekModulesAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (4)**, all three assertions, for every algebraic stack and with NO
> hypothesis.  For `g : Sh(𝒳_{flat,fppf}) ⟶ Sh(𝒳_τ)` the morphism of ringed topoi of
> **Stacks 0788**:
>
> * the functor `g_! : Mod(𝒪_{𝒳_{flat,fppf}}) ⥤ Mod(𝒪_𝒳)` has a left derived functor
>   `Lg_! : D(𝒪_{𝒳_{flat,fppf}}) ⟶ D(𝒪_𝒳)` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Mod(𝒪_𝒳)` has a pointwise left derived functor along the localization of
>   the homotopy category of `Mod(𝒪_{𝒳_{flat,fppf}})`, and `Lg_!` is that total left derived functor;
> * `Lg_!` is left adjoint to `g^*`, by an adjunction whose unit is an isomorphism;
> * `g^* ∘ Lg_! = id`.
>
> The structure sheaf is the one of **Stacks 06TV**, with sections in `Type u`, and the modules
> have their sections in `Type (u+1)`.

```lean
theorem lowerShriekModules_derived :
    (FreeRingUniverse.lowerShriekOnHomotopy.{u + 1} (inclusionTopology B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p B.topology) (objectProperty B S hS 𝒳).ι
        (moduleRing B S hS 𝒳) ⋙
      DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
        (FreeRingUniverse.sourceQuasiIso.{u + 1} (inclusionTopology B S hS 𝒳)
        (associatedTopology B S hS 𝒳.val.val.p B.topology) (objectProperty B S hS 𝒳).ι
        (moduleRing B S hS 𝒳)) ∧
    (∃ adj : derivedLowerShriekModules B S hS 𝒳 ⊣ derivedRestrictionModules B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedLowerShriekModules B S hS 𝒳 ⋙ derivedRestrictionModules B S hS 𝒳 ≅
      𝟭 (DerivedCategory (SheafOfModules.{u + 1} (subsiteModuleRingFlat B S hS 𝒳))))
```

**`AlgebraicGeometry.Stack.LisseEtale.lowerShriekModules_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SubsiteModuleDerivedLowerShriek.lean#L577). The attribute's comment: “part (2), the whole of it: existence of the unbounded left derived functor `Lg_!` of `g_!` on sheaves of modules for the lisse-étale site, its adjunction `Lg_! ⊣ g^*` (with invertible unit), and `g^* ∘ Lg_! = id`, for every algebraic stack, with no hypothesis. The structure sheaf is the one of Tag 06TV; the acyclicity statement of Tag 07AC is proved, as `AlgebraicGeometry.Stack.subsiteLowerShriekModulesAcyclic`, and the invertibility of the ordinary unit is Tag 077I”.

> **Stacks 07AS (2)**, all three assertions, for every algebraic stack and with NO
> hypothesis.  For `g : Sh(𝒳_{lisse,étale}) ⟶ Sh(𝒳_τ)` the morphism of ringed topoi of
> **Stacks 0788**:
>
> * the functor `g_! : Mod(𝒪_{𝒳_{lisse,étale}}) ⥤ Mod(𝒪_𝒳)` has a left derived functor
>   `Lg_! : D(𝒪_{𝒳_{lisse,étale}}) ⟶ D(𝒪_𝒳)` — degreewise `g_!` followed by the localization of the
>   homotopy category of `Mod(𝒪_𝒳)` has a pointwise left derived functor along the localization of
>   the homotopy category of `Mod(𝒪_{𝒳_{lisse,étale}})`, and `Lg_!` is that total left derived
>   functor;
> * `Lg_!` is left adjoint to `g^*`, by an adjunction whose unit is an isomorphism;
> * `g^* ∘ Lg_! = id`.
>
> The structure sheaf is the one of **Stacks 06TV**, with sections in `Type u`, and the modules
> have their sections in `Type (u+1)`.

```lean
theorem lowerShriekModules_derived :
    (FreeRingUniverse.lowerShriekOnHomotopy.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (ambientTopology B S hS 𝒳) (smoothObject.{u, w} B S hS 𝒳).ι
        (moduleRing.{u, w} B S hS 𝒳) ⋙
      DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
        (FreeRingUniverse.sourceQuasiIso.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (ambientTopology B S hS 𝒳) (smoothObject.{u, w} B S hS 𝒳).ι
        (moduleRing.{u, w} B S hS 𝒳)) ∧
    (∃ adj : derivedLowerShriekModules B S hS 𝒳 ⊣ derivedRestrictionModules B S hS 𝒳,
      IsIso adj.unit) ∧
    Nonempty (derivedLowerShriekModules B S hS 𝒳 ⋙ derivedRestrictionModules B S hS 𝒳 ≅
      𝟭 (DerivedCategory (SheafOfModules.{u + 1} (subsiteModuleRingSmooth B S hS 𝒳))))
```

## Tag 07AV, a lemma

[Tag 07AV](https://stacks.math.columbia.edu/tag/07AV) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.derivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean#L113). The attribute's comment: “the flat-fppf case for abelian sheaves, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories, as an isomorphism (g')⁻¹ ⋙ Rf'\_* ≅ Rf\_* ⋙ g⁻¹ for every pair of total right derived functors Rf\_*, Rf'\_* of the two direct images, the canonical ones included, with nothing assumed. The degree-zero square of Stacks 07AT (2) and the fact that restricted K-injective complexes compute Rf'\_* (Stacks 07AK at the 2-fibre products V ×\_y 𝒳, the content of Stacks 0GR3) are proved, not assumed”.

> **Stacks 07AV, first identity, for abelian sheaves on the flat-fppf sites:
> `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, `Rf_*`
> and `Rf'_*` total right derived functors of the direct images along `f` and along its restriction
> `f'` to the flat-fppf sites, and `g⁻¹`, `(g')⁻¹` restriction of abelian sheaves to the
> flat-fppf sites of `𝒴` and `𝒳`. Then, on the unbounded derived categories,
>
> `(g')⁻¹ ⋙ Rf'_* ≅ Rf_* ⋙ g⁻¹`.
>
> No hypothesis is made beyond the right derived functor properties of `Rf_*` and `Rf'_*` (a right
> derived functor being determined only up to unique isomorphism). The isomorphism is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero
> identification `AlgebraicGeometry.Stack.FlatFppf.isIso_abelianSheafBaseChange` and at
> `AlgebraicGeometry.Stack.FlatFppf.isIso_derivedPushforwardUnit_restriction`.

```lean
def derivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology)
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p B.topology)
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (αf : haveI := (isContinuous_and_isCocontinuous_homFunctor B S hS f).2
      haveI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p B.topology)
          (associatedTopology B S hS 𝒴.val.val.p B.topology)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p B.topology)
          (associatedTopology B S hS 𝒴.val.val.p B.topology)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : haveI := isCocontinuous_subsiteFunctor B S hS f hf
      haveI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (flatObject B S hS 𝒳.val)
          (flatObject_map B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology B S hS 𝒳)
        (inclusionTopology B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (Sheaf (associatedTopology B S hS 𝒳.val.val.p B.topology) AddCommGrpCat.{u + 1})
      (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (Sheaf (inclusionTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))] :
    haveI := isContinuous_inclusion B S hS 𝒳 (closedUnderFlatMorphisms B S hS 𝒳)
    haveI := isContinuous_inclusion B S hS 𝒴 (closedUnderFlatMorphisms B S hS 𝒴)
    haveI := additive_subsiteRestriction B S hS 𝒳
    haveI := additive_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒴
    (subsiteRestriction B S hS 𝒳.val.val.p B.topology
        (flatObject B S hS 𝒳.val)).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p B.topology
        (flatObject B S hS 𝒴.val)).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfDerivedBaseChange.lean#L345). The attribute's comment: “the flat-fppf case for abelian sheaves, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! of the canonical functors, with nothing assumed: the derived lower shrieks are those of Stacks 07AS (3), and the four derived adjunctions are constructed”.

> **Stacks 07AV, second identity, for abelian sheaves on the flat-fppf sites:
> `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.** For a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, with
> `Lg_!` and `L(g')_!` the derived lower shrieks of **Stacks 07AS** (1) for `𝒴` and `𝒳`, and `f⁻¹`,
> `(f')⁻¹` the inverse images along `f` and along its restriction `f'` to the flat-fppf sites,
>
> `Lg_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')_!`
>
> on the unbounded derived categories of abelian sheaves. All four functors are the canonical ones
> and no hypothesis is made. The isomorphism is the conjugate, under the composites of the derived
> adjunctions `Lg_! ⊣ g⁻¹`, `L(g')_! ⊣ (g')⁻¹` of Stacks 07AS (3) and `f⁻¹ ⊣ Rf_*`,
> `(f')⁻¹ ⊣ Rf'_*` (exact left adjoints), of the first identity
> `AlgebraicGeometry.Stack.FlatFppf.derivedRestrictionBaseChangeIso`.

```lean
def derivedLowerShriekBaseChangeIso :
    derivedAbelianLowerShriekFunctor B S hS 𝒴 ⋙ derivedAbelianInverseImage B S hS f ≅
      derivedAbelianSubsiteInverseImage B S hS f hf ⋙ derivedAbelianLowerShriekFunctor B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.moduleDerivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean#L179). The attribute's comment: “the module case for the flat-fppf sites, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories of sheaves of modules, as an isomorphism (g')^* ⋙ Rf'\_* ≅ Rf\_* ⋙ g^* for every pair of total right derived functors Rf\_*, Rf'\_* of the two direct images, the canonical ones included, with nothing assumed: the degree-zero square of Stacks 07AT (2) on modules and the fact that restricted K-injective complexes of modules compute Rf'\_* (Stacks 0D6J with Stacks 07AK at the 2-fibre products V ×\_y 𝒳) are proved, not assumed”.

> **Stacks 07AV, first identity, for sheaves of modules on the flat-fppf sites:
> `g^* ∘ Rf_* = Rf'_* ∘ (g')^*`.** For a flat 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, total
> right derived functors `Rf_*`, `Rf'_*` of the direct images of sheaves of modules along `f` and
> along its restriction `f'` to the flat-fppf sites, and `g^*`, `(g')^*` the restrictions of
> sheaves of modules to the flat-fppf sites (which are `g⁻¹`, `(g')⁻¹`),
>
> `(g')^* ⋙ Rf'_* ≅ Rf_* ⋙ g^*`
>
> on the unbounded derived categories, with no further hypothesis. It is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero square
> `AlgebraicGeometry.Stack.FlatFppf.isIso_moduleSquareComparison` and at
> `Stacks.SheafOfModules.isIso_derivedPushforwardUnit_inverseImage`, fed with
> `AlgebraicGeometry.Stack.FlatFppf.qh_map_bijective_directImageCorep_restriction`.

```lean
def moduleDerivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒴)))
    (Rf' : DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒴)))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (moduleSubsitePushforward B S hS f hf).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))] :
    (moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.FlatFppf.moduleDerivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfModuleDerivedBaseChange.lean#L354). The attribute's comment: “the module case for the flat-fppf sites, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories of sheaves of modules, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! for the actual derived lower shrieks and the exact inverse images, with nothing assumed: the adjunctions Lg\_! ⊣ g⁻¹, f⁻¹ ⊣ Rf\_* and their primed versions are constructed, and the first identity is proved”.

> **Stacks 07AV, the module case for the flat-fppf sites, second identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a flat 1-morphism of algebraic stacks, `f'` its restriction to the flat-fppf
> sites, and `Lg_!`, `L(g')_!` the derived lower shrieks of sheaves of modules along the inclusions
> of the flat-fppf sites (`AlgebraicGeometry.Stack.FlatFppf.derivedModuleLowerShriekSucc`). Then
>
> `Lg_! ⋙ f^{-1} ≅ (f')^{-1} ⋙ L(g')_!`
>
> on the unbounded derived categories of sheaves of modules, that is,
> `L(g')_! ∘ (f')^{-1} = f^{-1} ∘ Lg_!`. Here `f^{-1}`, `(f')^{-1}` are the exact inverse images
> (Stacks 06WE, and restriction along `f'`), left adjoint to the canonical total right derived
> direct images `Rf_*`, `Rf'_*` (`derivedAdjunctionOfExactLeftAdjoint` on
> `AlgebraicGeometry.Stack.FlatFppf.modulePullbackPushforwardAdjunction` and
> `AlgebraicGeometry.Stack.FlatFppf.moduleSubsiteInverseImageAdjunction`), and the isomorphism
> is the conjugate, across the composed adjunctions, of the first identity
> `AlgebraicGeometry.Stack.FlatFppf.moduleDerivedRestrictionBaseChangeIso`.

```lean
def moduleDerivedLowerShriekBaseChangeIso :
    derivedModuleLowerShriekSucc B S hS 𝒴 ⋙ derivedModulePullback B S hS f ≅
      derivedModuleSubsiteInverseImage B S hS f hf ⋙ derivedModuleLowerShriekSucc B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean#L165). The attribute's comment: “the lisse-étale case for abelian sheaves, first identity, for every smooth 1-morphism f : 𝒳 ⟶ 𝒴 of algebraic stacks (the setup of Stacks 07AT (1)): g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories, as an isomorphism (g')⁻¹ ⋙ Rf'\_* ≅ Rf\_* ⋙ g⁻¹ for every pair of total right derived functors Rf\_*, Rf'\_* of the two direct images, the canonical ones included, with nothing assumed. The degree-zero square of Stacks 07AT (1) and the fact that restricted K-injective complexes compute Rf'\_* (Stacks 07AK at the 2-fibre products V ×\_y 𝒳, the content of Stacks 0GR3) are proved, not assumed”.

> **Stacks 07AV, first identity, for abelian sheaves on the lisse-étale sites:
> `g⁻¹ ∘ Rf_* = Rf'_* ∘ (g')⁻¹`.** Let `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, `Rf_*`
> and `Rf'_*` total right derived functors of the direct images along `f` and along its restriction
> `f'` to the lisse-étale sites, and `g⁻¹`, `(g')⁻¹` restriction of abelian sheaves to the
> lisse-étale sites of `𝒴` and `𝒳`. Then, on the unbounded derived categories,
>
> `(g')⁻¹ ⋙ Rf'_* ≅ Rf_* ⋙ g⁻¹`.
>
> No hypothesis is made beyond the right derived functor properties of `Rf_*` and `Rf'_*` (a right
> derived functor being determined only up to unique isomorphism). The isomorphism is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero
> identification `AlgebraicGeometry.Stack.LisseEtale.isIso_abelianSheafBaseChange` and at
> `AlgebraicGeometry.Stack.LisseEtale.isIso_derivedPushforwardUnit_restriction`.

```lean
def derivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))
        AddCommGrpCat.{u + 1}))
    (Rf' : DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory (Sheaf (inclusionTopology.{u, w} B S hS 𝒴) AddCommGrpCat.{u + 1}))
    (αf : haveI := (isContinuous_and_isCocontinuous_homFunctor_associatedTopology B S hS f
        (etaleTopology B)).2
      haveI : (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      (f.hom.hom.toFunctor.sheafPushforwardCocontinuous AddCommGrpCat.{u + 1}
          (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
          (associatedTopology B S hS 𝒴.val.val.p (etaleTopology B))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : haveI := isCocontinuous_subsiteFunctor.{u, w} B S hS f hf
      haveI : ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor
          (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).Additive :=
        Functor.sheafPushforwardCocontinuous_additive.{u + 1, u + 1, u, u, u + 1} _ _ _
      ((SubsitePushforward.subsiteFunctor f.hom.hom.toFunctor (smoothObject.{u, w} B S hS 𝒳)
          (smoothObject_map.{u, w} B S hS f hf)).sheafPushforwardCocontinuous
        AddCommGrpCat.{u + 1} (inclusionTopology.{u, w} B S hS 𝒳)
        (inclusionTopology.{u, w} B S hS 𝒴)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (Sheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) AddCommGrpCat.{u + 1})
      (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (Sheaf (inclusionTopology.{u, w} B S hS 𝒳) AddCommGrpCat.{u + 1}) (ComplexShape.up ℤ))] :
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒳 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒳)
    haveI := isContinuous_inclusion.{u, w} B S hS 𝒴 (closedUnderSmoothMorphisms.{u, w} B S hS 𝒴)
    haveI := additive_subsiteRestriction B S hS 𝒳
    haveI := additive_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteLimits_subsiteRestriction B S hS 𝒴
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒳
    haveI := preservesFiniteColimits_subsiteRestriction B S hS 𝒴
    (subsiteRestriction B S hS 𝒳.val.val.p (etaleTopology B)
        (smoothObject.{u, w} B S hS 𝒳)).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (subsiteRestriction B S hS 𝒴.val.val.p (etaleTopology B)
        (smoothObject.{u, w} B S hS 𝒴)).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleDerivedBaseChange.lean#L404). The attribute's comment: “the lisse-étale case for abelian sheaves, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! of the canonical functors, with nothing assumed: the derived lower shrieks are those of Stacks 07AS (1), and the four derived adjunctions are constructed”.

> **Stacks 07AV, second identity, for abelian sheaves on the lisse-étale sites:
> `L(g')_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg_!`.** For a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, with
> `Lg_!` and `L(g')_!` the derived lower shrieks of **Stacks 07AS** (1) for `𝒴` and `𝒳`, and `f⁻¹`,
> `(f')⁻¹` the inverse images along `f` and along its restriction `f'` to the lisse-étale sites,
>
> `Lg_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')_!`
>
> on the unbounded derived categories of abelian sheaves. All four functors are the canonical ones
> and no hypothesis is made. The isomorphism is the conjugate, under the composites of the derived
> adjunctions `Lg_! ⊣ g⁻¹`, `L(g')_! ⊣ (g')⁻¹` of Stacks 07AS (1) and `f⁻¹ ⊣ Rf_*`,
> `(f')⁻¹ ⊣ Rf'_*` (exact left adjoints), of the first identity
> `AlgebraicGeometry.Stack.LisseEtale.derivedRestrictionBaseChangeIso`.

```lean
def derivedLowerShriekBaseChangeIso :
    derivedAbelianLowerShriek.{u, w} B S hS 𝒴 ⋙ derivedAbelianInverseImage B S hS f ≅
      derivedAbelianSubsiteInverseImage B S hS f hf ⋙ derivedAbelianLowerShriek.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.moduleDerivedRestrictionBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean#L332). The attribute's comment: “the module case for the lisse-étale sites, first identity: g⁻¹ ∘ Rf\_* = Rf'\_* ∘ (g')⁻¹ on the unbounded derived categories of sheaves of modules, as an isomorphism (g')^* ⋙ Rf'\_* ≅ Rf\_* ⋙ g^* for every pair of total right derived functors Rf\_*, Rf'\_* of the two direct images, the canonical ones included, with nothing assumed: the degree-zero square of Stacks 07AT (1) on modules and the fact that restricted K-injective complexes of modules compute Rf'\_* (Stacks 0D6J with Stacks 07AK at the 2-fibre products V ×\_y 𝒳) are proved, not assumed”.

> **Stacks 07AV, first identity, for sheaves of modules on the lisse-étale sites:
> `g^* ∘ Rf_* = Rf'_* ∘ (g')^*`.** For a smooth 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, total
> right derived functors `Rf_*`, `Rf'_*` of the direct images of sheaves of modules along `f` and
> along its restriction `f'` to the lisse-étale sites, and `g^*`, `(g')^*` the restrictions of
> sheaves of modules to the lisse-étale sites (which are `g⁻¹`, `(g')⁻¹`),
>
> `(g')^* ⋙ Rf'_* ≅ Rf_* ⋙ g^*`
>
> on the unbounded derived categories, with no further hypothesis. It is
> `Stacks.Cohomology.UnboundedComplexes.derivedBaseChangeIsoOfUnit` at the degree-zero square
> `AlgebraicGeometry.Stack.LisseEtale.isIso_moduleSquareComparison` and at
> `Stacks.SheafOfModules.isIso_derivedPushforwardUnit_inverseImage`, fed with
> `AlgebraicGeometry.Stack.LisseEtale.qh_map_bijective_directImageCorep_restriction`.

```lean
def moduleDerivedRestrictionBaseChangeIso
    (Rf : DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒴)))
    (Rf' : DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒴)))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (moduleSubsitePushforward B S hS f hf).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    [hRf : Rf.IsRightDerivedFunctor αf (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))]
    [hRf' : Rf'.IsRightDerivedFunctor αf' (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)) (ComplexShape.up ℤ))] :
    (moduleInverseImage B S hS 𝒳).mapDerivedCategory ⋙ Rf' ≅
      Rf ⋙ (moduleInverseImage B S hS 𝒴).mapDerivedCategory
```

**`AlgebraicGeometry.Stack.LisseEtale.moduleDerivedLowerShriekBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/LisseEtaleModuleDerivedBaseChange.lean#L514). The attribute's comment: “the module case for the lisse-étale sites, second identity: L(g')\_! ∘ (f')⁻¹ = f⁻¹ ∘ Lg\_! on the unbounded derived categories of sheaves of modules, as an isomorphism Lg\_! ⋙ f⁻¹ ≅ (f')⁻¹ ⋙ L(g')\_! for the actual derived lower shrieks and the exact inverse images, with nothing assumed: the adjunctions Lg\_! ⊣ g⁻¹, f⁻¹ ⊣ Rf\_* and their primed versions are constructed, and the first identity is proved”.

> **Stacks 07AV, the module case for the lisse-étale sites, second identity.** Let
> `f : 𝒳 ⟶ 𝒴` be a smooth 1-morphism of algebraic stacks, `f'` its restriction to the lisse-étale
> sites, and `Lg_!`, `L(g')_!` the derived lower shrieks of sheaves of modules along the inclusions
> of the lisse-étale sites (`AlgebraicGeometry.Stack.LisseEtale.derivedModuleLowerShriekSucc`). Then
>
> `Lg_! ⋙ f^{-1} ≅ (f')^{-1} ⋙ L(g')_!`
>
> on the unbounded derived categories of sheaves of modules, that is,
> `L(g')_! ∘ (f')^{-1} = f^{-1} ∘ Lg_!`. Here `f^{-1}`, `(f')^{-1}` are the exact inverse images
> (Stacks 06WE, and restriction along `f'`), left adjoint to the canonical total right derived
> direct images `Rf_*`, `Rf'_*` (`derivedAdjunctionOfExactLeftAdjoint` on
> `AlgebraicGeometry.Stack.LisseEtale.modulePullbackPushforwardAdjunction` and
> `AlgebraicGeometry.Stack.LisseEtale.moduleSubsiteInverseImageAdjunction`), and the isomorphism
> is the conjugate, across the composed adjunctions, of the first identity
> `AlgebraicGeometry.Stack.LisseEtale.moduleDerivedRestrictionBaseChangeIso`.

```lean
def moduleDerivedLowerShriekBaseChangeIso :
    derivedModuleLowerShriekSucc B S hS 𝒴 ⋙ derivedModulePullback B S hS f ≅
      derivedModuleSubsiteInverseImage B S hS f hf ⋙ derivedModuleLowerShriekSucc B S hS 𝒳
```

## Tag 07B3, a lemma

[Tag 07B3](https://stacks.math.columbia.edu/tag/07B3) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.locallyQuasicoherentSheafFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedModuleLowerShriekSheafFlatBaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedModuleLowerShriekSheafFlatBaseChange.lean#L90). The attribute's comment: “part (2): for a quasi-coherent module `H` (Stacks 03DL) on the flat-fppf site of an arbitrary algebraic stack and every `p`, `H^p(Lg_! H)` is a locally quasi-coherent module with the flat base change property, the class `LQCoh^fbc` of Stacks 0762 read with the pullback of sheaves, for the actual derived lower shriek `Lg_!` of Stacks 07AS (4) at the universe of the rings, with no hypothesis”.

> **Stacks 07B3, part (2).** Let `H` be a quasi-coherent module on the flat-fppf site of an
> algebraic stack `𝒳`. For every `p`, the cohomology sheaf `H^p(Lg_! H)` of the derived lower shriek of
> Stacks 07AS (4) is a locally quasi-coherent module with the flat base change property on `𝒳`, the
> flat base change property of Stacks 0762 being read with the pullback of sheaves.

```lean
theorem locallyQuasicoherentSheafFlatBaseChange_homology_derivedModuleLowerShriek
    (H : flatFppfModules B S hS 𝒳) (hH : H.IsQuasicoherentOnSite) (p : ℤ) :
    letI := (SheafOfModules.instAbelian _ : Abelian (fppfModules B S hS 𝒳))
    letI := abelianFlatFppfModulesSpelling B S hS 𝒳
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳
      ((DerivedCategory.homologyFunctor _ p).obj
        ((derivedModuleLowerShriek B S hS 𝒳).obj ((DerivedCategory.singleFunctor _ 0).obj H)))
```

**`AlgebraicGeometry.Stack.LisseEtale.isLocallyQuasicoherentWithSheafFlatBaseChange_homology_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedModuleLowerShriekSheafFlatBaseChange.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedModuleLowerShriekSheafFlatBaseChange.lean#L56). The attribute's comment: “part (1): for a quasi-coherent module `H` (Stacks 03DL) on the lisse-étale site of an arbitrary algebraic stack and every `p`, `H^p(Lg_! H)` is a locally quasi-coherent module with the flat base change property, the class `LQCoh^fbc` of Stacks 0762 read with the pullback of sheaves, for the actual derived lower shriek `Lg_!` of Stacks 07AS (2) at the universe of the rings, with no hypothesis”.

> **Stacks 07B3, part (1).** Let `H` be a quasi-coherent module on the lisse-étale site of an
> algebraic stack `𝒳`. For every `p`, the cohomology sheaf `H^p(Lg_! H)` of the derived lower shriek `Lg_!` is a locally
> quasi-coherent module with the flat base change property on `𝒳`, the flat base change property
> being read with the pullback of sheaves.

```lean
theorem isLocallyQuasicoherentWithSheafFlatBaseChange_homology_derivedModuleLowerShriek
    (H : SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳)) (hH : H.IsQuasicoherentOnSite)
    (p : ℤ) :
    letI := abelianEtaleModules B S hS 𝒳
    letI := abelianLisseEtaleModules B S hS 𝒳
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳))
    letI := HasDerivedCategory.standard (SheafOfModules.{u}
      (SmallModel.targetRing (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B))
        (associatedRingedTopos B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (etaleTopology B)
          (etaleTopology_le_topology B)).O))
    IsLocallyQuasicoherentWithSheafFlatBaseChange.{u, u + 1, u, u} B E h S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      ((DerivedCategory.homologyFunctor _ p).obj
        ((derivedModuleLowerShriek B S hS 𝒳).obj
          ((DerivedCategory.singleFunctor _ 0).obj H))).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.3, Tag 08MZ](https://stacks.math.columbia.edu/tag/08MZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
