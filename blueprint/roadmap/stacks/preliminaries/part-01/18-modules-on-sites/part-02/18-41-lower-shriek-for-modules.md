---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.lowerShriek, Stacks.SheafOfModules.lowerShriekAdjunction, AlgebraicGeometry.smallEtaleModuleProjectionAdjunction, Stacks.SheafOfModules.lowerShriekForgetComparison, Stacks.SheafOfModules.lowerShriekForgetComparison_homEquiv, Stacks.SheafOfModules.lowerShriekForget_not_isomorphic, Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_iff, Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_iff_of_isos
statement: formalized
proof: formalized
---

# 18.41 Lower shriek for modules

Section 18.41 of the Stacks Project, [Tag 0796](https://stacks.math.columbia.edu/tag/0796). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0797, a lemma

[Tag 0797](https://stacks.math.columbia.edu/tag/0797) in the Stacks Project.

**`Stacks.SheafOfModules.lowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriek.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriek.lean#L85). References: SGA 4 IV (14.2), “j_!”.

> **Stacks 0797.** Lower shriek `g_! : Mod(O_C) ⥤ Mod(O_D)` for the morphism of topoi
> associated with a continuous and cocontinuous functor of sites, where `O_C = g^{-1} O_D`: a
> sheaf of `O_C`-modules is pushed forward as a presheaf of modules and the result is sheafified.

```lean
def lowerShriek [u.IsCocontinuous J K] :
    _root_.SheafOfModules.{v} (inverseImageRing J K u O) ⥤ _root_.SheafOfModules.{v} O
```

**`Stacks.SheafOfModules.lowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriek.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriek.lean#L95). References: SGA 4 IV (14.2), “j_! ⊣ j^*”.

> **Stacks 0797.** Lower shriek is left adjoint to the inverse image `g^* = g^{-1}` of sheaves
> of modules, for the morphism of topoi associated with a continuous and cocontinuous functor of
> sites.

```lean
def lowerShriekAdjunction [u.IsCocontinuous J K] :
    lowerShriek.{v} J K u O ⊣ inverseImage.{v} J K u O
```

**`AlgebraicGeometry.smallEtaleModuleProjectionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleProjectionPullback.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ModuleProjectionPullback.lean#L194). The attribute's comment: “the adjunction at the inclusion of the small étale site of a scheme into its big étale site, at the module universe of Stacks 0DDH part (6)”.

> **Stacks 0797 at the small étale inclusion.** `π_S^*` is left adjoint to `π_{S,*}`, which is
> `AlgebraicGeometry.smallEtaleModuleRestriction B S S (𝟙 S)`.

```lean
public def smallEtaleModuleProjectionAdjunction :
    smallEtaleModuleProjectionPullback B S ⊣ smallEtaleModuleRestriction B S S (𝟙 S)
```

## Tag 0798, a remark

[Tag 0798](https://stacks.math.columbia.edu/tag/0798) in the Stacks Project.

**`Stacks.SheafOfModules.lowerShriekForgetComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L81). The attribute's comment: “comparison_transformation”.

> The canonical natural transformation from lower shriek applied to the underlying abelian
> sheaf to the underlying abelian sheaf of lower shriek on modules.

```lean
noncomputable def lowerShriekForgetComparison :
    _root_.SheafOfModules.toSheaf.{w} S ⋙
        F.sheafPullback AddCommGrpCat.{w} J K ⟶
      _root_.SheafOfModules.pullback.{w} phi ⋙ _root_.SheafOfModules.toSheaf.{w} R
```

**`Stacks.SheafOfModules.lowerShriekForgetComparison_homEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L133). The attribute's comment: “comparison_transformation”.

> The comparison map is adjoint to the forgotten unit of the module lower-shriek
> adjunction.

```lean
theorem lowerShriekForgetComparison_homEquiv (M : _root_.SheafOfModules.{w} S) :
    (F.sheafAdjunctionContinuous AddCommGrpCat.{w} J K).homEquiv
        ((_root_.SheafOfModules.toSheaf.{w} S).obj M)
        ((_root_.SheafOfModules.toSheaf.{w} R).obj
          ((_root_.SheafOfModules.pullback.{w} phi).obj M))
        ((lowerShriekForgetComparison F phi).app M) =
      (_root_.SheafOfModules.toSheaf.{w} S).map
        ((_root_.SheafOfModules.pullbackPushforwardAdjunction.{w} phi).unit.app M)
```

**`Stacks.SheafOfModules.lowerShriekForget_not_isomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L448). The attribute's comment: “noncommutativity”.

> The lower shriek of modules may differ, even as an abelian sheaf, from lower
> shriek of the underlying abelian sheaf.

```lean
theorem lowerShriekForget_not_isomorphic :
    ∃ (J : GrothendieckTopology PUnit) (K : GrothendieckTopology Bool)
      (F : PUnit ⥤ Bool) (R : Sheaf K RingCat.{0})
      (hF : F.IsContinuous J K) (_hFc : F.IsCocontinuous J K),
      letI : F.IsContinuous J K := hF
      let S : Sheaf J RingCat.{0} :=
        (F.sheafPushforwardContinuous RingCat.{0} J K).obj R
      let φ : S ⟶ (F.sheafPushforwardContinuous RingCat.{0} J K).obj R := 𝟙 S
      ∃ (hAb : (F.sheafPushforwardContinuous AddCommGrpCat.{0} J K).IsRightAdjoint)
        (hMod : (SheafOfModules.pushforward.{0} φ).IsRightAdjoint),
      letI : (F.sheafPushforwardContinuous AddCommGrpCat.{0} J K).IsRightAdjoint := hAb
      letI : (SheafOfModules.pushforward.{0} φ).IsRightAdjoint := hMod
      ∃ M : SheafOfModules.{0} S,
        ¬ Nonempty
          (((SheafOfModules.toSheaf.{0} S ⋙
              F.sheafPullback AddCommGrpCat.{0} J K).obj M) ≅
            ((SheafOfModules.pullback.{0} φ ⋙
              SheafOfModules.toSheaf.{0} R).obj M))
```

**`Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L653). The attribute's comment: “the criterion: agreement iff the comparison is invertible at every j_{U!} O_U”.

> The canonical comparison between lower shriek on sheaves of modules and lower shriek on the
> underlying abelian sheaves is an isomorphism if and only if it is an isomorphism at the extension
> by zero `j_{U!} O_U` of the structure sheaf for every object `U` of the source site.

```lean
theorem isIso_lowerShriekForgetComparison_iff :
    IsIso (lowerShriekForgetComparison F phi) ↔
      ∀ U : C, IsIso ((lowerShriekForgetComparison F phi).app
        (extensionByZeroUnit.{u₁, v₁, u, max u₂ v₂ t} S U))
```

**`Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_iff_of_isos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L697). The attribute's comment: “the criterion, at any family isomorphic to the extensions by zero of the structure sheaf”.

> If a family `G` of sheaves of modules is isomorphic, object by object, to the extensions by
> zero of the structure sheaf, then the comparison is an isomorphism exactly when it is an
> isomorphism at every `G U`.

```lean
theorem isIso_lowerShriekForgetComparison_iff_of_isos
    (G : C → _root_.SheafOfModules.{max u₁ v₁ u₂ v₂ u t} S)
    (e : ∀ U : C, extensionByZeroUnit.{u₁, v₁, u, max u₂ v₂ t} S U ≅ G U) :
    IsIso (lowerShriekForgetComparison F phi) ↔
      ∀ U : C, IsIso ((lowerShriekForgetComparison F phi).app (G U))
```

**`Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_iff_extensionByZeroUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForget.lean#L778). The attribute's comment: “the criterion in the source's form: the comparison is an isomorphism iff `g_!^{Ab} j_{U!} O_U ⟶ j_{u(U)!} O_{u(U)}` is one for every `U`, the target being identified by Stacks 07AC”.

> The canonical comparison between lower shriek on sheaves of modules and lower shriek on the
> underlying abelian sheaves is an isomorphism if and only if, for every object `U` of the source
> site, the canonical map
>
> `g_!^{Ab} j_{U!} O_U ⟶ j_{u(U)!} O_{u(U)}`
>
> is an isomorphism.

```lean
theorem isIso_lowerShriekForgetComparison_iff_extensionByZeroUnit :
    IsIso (lowerShriekForgetComparison u (structureMap J K u O)) ↔
      ∀ V : C, IsIso ((lowerShriekForgetComparison u (structureMap J K u O)).app
            (extensionByZeroUnit (inverseImageRing J K u O) V) ≫
          (_root_.SheafOfModules.toSheaf O).map
            (pullbackExtensionByZeroUnitIso.{t, u₁, u₂, v₁, v₂} J K u O V).hom)
```

**`Stacks.SheafOfModules.lowerShriekForgetComparison_app_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetCounit.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetCounit.lean#L52). The attribute's comment: “the comparison on counits”.

> The lower-shriek forget comparison carries the forgotten counit of the module lower-shriek
> adjunction to the counit of the abelian one: both sides are maps from the abelian lower shriek of
> the direct image of `N` to the abelian sheaf underlying `N`, the left one going through the module
> lower shriek of the direct image.

```lean
theorem lowerShriekForgetComparison_app_comp_counit (N : _root_.SheafOfModules.{w} R) :
    (lowerShriekForgetComparison F phi).app
          ((_root_.SheafOfModules.pushforward.{w} phi).obj N) ≫
        (_root_.SheafOfModules.toSheaf.{w} R).map
          ((_root_.SheafOfModules.pullbackPushforwardAdjunction.{w} phi).counit.app N) =
      (F.sheafAdjunctionContinuous AddCommGrpCat.{w} J K).counit.app
        ((_root_.SheafOfModules.toSheaf.{w} R).obj N)
```

**`Stacks.SheafOfModules.abelianShriekOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean#L103). The attribute's comment: “`g_!^{Ab} j_{U!} = j_{u(U)!} (g')^{Ab}_!`, the consequence of the localized square of Stacks 03EG that the remark uses”.

> Lower shriek of abelian sheaves commutes with localization: with `V = u(U)` and
> `g' : Sh(C/U) ⟶ Sh(D/V)` the morphism of topoi induced by the localized functor `u' = Over.post u`
> of Stacks 03EG,
>
> `g_!^{Ab} ∘ j_{U!} ≅ j_{V!} ∘ (g')^{Ab}_!`.

```lean
def abelianShriekOverIso :
    (Over.forget U).sheafPullback AddCommGrpCat.{w} (J.over U) J ⋙
        u.sheafPullback AddCommGrpCat.{w} J K ≅
      (Over.post u : Over U ⥤ Over (u.obj U)).sheafPullback AddCommGrpCat.{w}
          (J.over U) (K.over (u.obj U)) ⋙
        (Over.forget (u.obj U)).sheafPullback AddCommGrpCat.{w} (K.over (u.obj U)) K
```

**`Stacks.SheafOfModules.homEquiv_comp_lowerShriekForgetComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean#L567). The attribute's comment: “the composition law for the comparison transformation `g_!^{Ab} ∘ forget ⟶ forget ∘ g_!`”.

> The composition law for the comparison transformation of Stacks 0798. For a composite
> `a ⋙ b` of continuous functors of sites, with the structure sheaves the successive restrictions
> of a sheaf of rings on the target, the composite
>
> `b_!^{Ab} (c^a) ≫ c^b`
>
> of the two comparison transformations is the adjoint transpose, under the composite of the two
> lower-shriek adjunctions for abelian sheaves, of the forgotten unit of the composite of the two
> lower-shriek adjunctions for modules, written with the two units separated.

```lean
theorem homEquiv_comp_lowerShriekForgetComparison
    (M : _root_.SheafOfModules.{w} (inverseImageRing JA JB a (inverseImageRing JB JE b O))) :
    ((a.sheafAdjunctionContinuous AddCommGrpCat.{w} JA JB).comp
        (b.sheafAdjunctionContinuous AddCommGrpCat.{w} JB JE)).homEquiv _ _
      ((b.sheafPullback AddCommGrpCat.{w} JB JE).map
          ((lowerShriekForgetComparison a
            (structureMap JA JB a (inverseImageRing JB JE b O))).app M) ≫
        (lowerShriekForgetComparison b (structureMap JB JE b O)).app
          ((_root_.SheafOfModules.pullback.{w}
            (structureMap JA JB a (inverseImageRing JB JE b O))).obj M)) =
      (_root_.SheafOfModules.toSheaf.{w}
            (inverseImageRing JA JB a (inverseImageRing JB JE b O))).map
          ((_root_.SheafOfModules.pullbackPushforwardAdjunction.{w}
            (structureMap JA JB a (inverseImageRing JB JE b O))).unit.app M) ≫
        (a.sheafPushforwardContinuous AddCommGrpCat.{w} JA JB).map
          ((_root_.SheafOfModules.toSheaf.{w} (inverseImageRing JB JE b O)).map
            ((_root_.SheafOfModules.pullbackPushforwardAdjunction.{w}
              (structureMap JB JE b O)).unit.app
              ((_root_.SheafOfModules.pullback.{w}
                (structureMap JA JB a (inverseImageRing JB JE b O))).obj M)))
```

**`Stacks.SheafOfModules.localizedStructureSheafComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean, line 1064](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean#L1064). The attribute's comment: “the canonical map of equation 0799, `κ_U : (g')_!^{Ab} O_U ⟶ O_{u(U)}`”.

> The canonical map `(g')_!^{Ab} O_U ⟶ O_{u(U)}` of Stacks 0798: lower shriek of abelian
> sheaves applied to the underlying abelian sheaf of the structure sheaf of the localized source
> site, mapping to the underlying abelian sheaf of the structure sheaf of the localized target
> site. It is the comparison transformation of Stacks 0798 for the localized functor, evaluated at
> the structure sheaf, followed by the canonical map `g'_! O_U ⟶ O_{u(U)}` of sheaves of
> modules.

```lean
def localizedStructureSheafComparison :
    ((Over.post (X := V) u).sheafPullback AddCommGrpCat.{w} (J.over V) (K.over (u.obj V))).obj
        ((_root_.SheafOfModules.toSheaf.{w} (inverseImageRing (J.over V) (K.over (u.obj V))
            (Over.post (X := V) u) (O.over (u.obj V)))).obj
          (_root_.SheafOfModules.unit _)) ⟶
      (_root_.SheafOfModules.toSheaf.{w} (O.over (u.obj V))).obj
        (_root_.SheafOfModules.unit (O.over (u.obj V)))
```

**`Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_of_localizedStructureSheafComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean, line 1154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekForgetLocalized.lean#L1154). The attribute's comment: “the criterion: `g_! = g_!^{Ab}` if the canonical map of equation 0799 is an isomorphism for every object `U`”.

> Lower shriek on sheaves of modules agrees with lower shriek on the underlying abelian
> sheaves, that is, the comparison transformation `Stacks.SheafOfModules.lowerShriekForgetComparison`
> is an isomorphism, as soon as, for every object `U` of the source site, the canonical map
>
> `(g')_!^{Ab} O_U ⟶ O_{u(U)}`
>
> of `Stacks.SheafOfModules.localizedStructureSheafComparison` is an isomorphism, `g'` being the
> morphism of topoi induced by the localized functor `u' = Over.post u : C/U ⥤ D/u(U)` of Stacks
> 03EG.

```lean
theorem isIso_lowerShriekForgetComparison_of_localizedStructureSheafComparison
    (h : ∀ V : C, IsIso (localizedStructureSheafComparison J K u O V)) :
    IsIso (lowerShriekForgetComparison u (structureMap J K u O))
```

**`AlgebraicGeometry.Space.isIso_etaleLowerShriekForgetComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleExtensionByZeroForget.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleExtensionByZeroForget.lean#L68). The attribute's comment: “postcomposition along an étale morphism of algebraic spaces”.

> **Stacks 0798** for postcomposition along an étale morphism of algebraic spaces: the
> comparison from extension by zero of the underlying abelian sheaf to the underlying abelian
> sheaf of extension by zero of modules is an isomorphism, because every slice functor of
> postcomposition is an equivalence and the structure morphism of rings is the identity.

```lean
instance isIso_etaleLowerShriekForgetComparison (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) :
    IsIso (Stacks.SheafOfModules.lowerShriekForgetComparison.{u, u}
      (smallEtalePostcomp B S hS f hf)
      (Stacks.SheafOfModules.structureMap (SmallEtale.topology B S hS X.1)
        (SmallEtale.topology B S hS Y.1) (smallEtalePostcomp B S hS f hf)
        (etaleRingSheaf B S hS Y)))
```

**`AlgebraicGeometry.Space.etaleModuleShriekForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekForgetStalk.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekForgetStalk.lean#L91). The attribute's comment: “extension by zero of modules and of abelian sheaves, for an étale morphism”.

> **Tag 0798 for an étale morphism of algebraic spaces.**  The abelian sheaf underlying the
> extension by zero of a sheaf of `𝒪_X`-modules is the extension by zero of the abelian sheaf
> underlying it.
>
> This is `AlgebraicGeometry.Space.etaleModuleShriekForgetIsoRaw` repackaged: the two isomorphisms
> have the same components, and only the spelling of the functors differs.  The repackaging is
> what makes the structure sheaf of rings of `X` appear as
> `AlgebraicGeometry.Space.etaleRingSheaf` rather than as the restriction along postcomposition of
> that of `Y`, and the module categories appear as `AlgebraicGeometry.Space.Modules`; without it
> every rewrite below is rejected for being type-incorrect at the transparency rewriting uses.

```lean
def etaleModuleShriekForgetIso :
    SheafOfModules.toSheaf (etaleRingSheaf B S hS X) ⋙
        abelianEtaleExtensionByZero B S hS f hf ≅
      etaleModuleLowerShriek B S hS f hf ⋙
        SheafOfModules.toSheaf (etaleRingSheaf B S hS Y)
```

**`AlgebraicGeometry.Space.etaleModuleShriekForgetIso_hom_app_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekForgetStalk.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModuleShriekForgetStalk.lean#L114). The attribute's comment: “the comparison on counits, for an étale morphism”.

> **The comparison of Tag 0798 carries the forgotten counit of the module extension-by-zero
> adjunction to the counit of the abelian one.**

```lean
theorem etaleModuleShriekForgetIso_hom_app_comp_counit
    (N : Modules.{u, u} B S hS Y.1 Y.2) :
    (etaleModuleShriekForgetIso B S hS f hf).hom.app
          ((etaleModulePullback.{u, u} B S hS f hf).obj N) ≫
        (SheafOfModules.toSheaf (etaleRingSheaf B S hS Y)).map
          ((etaleModuleLowerShriekAdjunction B S hS f hf).counit.app N) =
      (abelianEtaleExtensionByZeroAdjunction B S hS f hf).counit.app
        ((SheafOfModules.toSheaf (etaleRingSheaf B S hS Y)).obj N)
```

## Tag 0FN3, a lemma

[Tag 0FN3](https://stacks.math.columbia.edu/tag/0FN3) in the Stacks Project.

**`Stacks.SheafOfModules.inverseImageCompCocontinuousPushforwardOfIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekCocontinuousSquare.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekCocontinuousSquare.lean#L444). The attribute's comment: “first conclusion: `f'_* ∘ (g')^* ≅ g^* ∘ f_*` on sheaves of modules, for a commutative square of ringed topoi whose four functors `u`, `u'`, `v`, `v'` are cocontinuous, with `v`, `v'` continuous as well, with the comparison functors of the index categories of Section 00XF cofinal, and with `g^{-1} O_D = O_{D'}`, `(g')^{-1} O_C = O_{C'}`. An isomorphism rather than an equality, the sheaf-level comparison of Stacks 0FN1 being a base change of right Kan extensions. The direct images of sheaves of modules along the cocontinuous `u` and `u'` are the canonical ones attached to the structure map `f^♯ : O_D → {}_su O_C` of the morphism of ringed topoi, whose underlying sheaves of abelian groups are `{}_su`, `{}_su'`.”.

> **Stacks 0FN3**, first conclusion, for the canonical direct images. For a commutative square
> of ringed topoi as in the module docstring — all four functors cocontinuous giving `f`, `f'`,
> `g`, `g'`, the functors `v`, `v'` continuous as well as cocontinuous, `u' ⋙ v = v' ⋙ u`, the
> comparison functors `{}^{u'}_{V'} I ⥤ {}^u_{v(V')} I` all cofinal, and `g^{-1} O_D = O_{D'}`,
> `(g')^{-1} O_C = O_{C'}` — we have `f'_* ∘ (g')^* ≅ g^* ∘ f_*` on sheaves of modules.
>
> The direct images of sheaves of modules are the canonical ones: `f_*` is
> `Stacks.SheafOfModules.pushforwardCocontinuous` for the given structure map
> `f^♯ : O_D ⟶ {}_su O_C`, and `f'_*` is the same construction for the structure map
> `(f')^♯ : O_{D'} ⟶ {}_su' O_{C'}` that `f^♯` induces by restriction along `v` and base change.
> For these the linearity hypothesis of
> `Stacks.SheafOfModules.nonempty_inverseImage_comp_cocontinuousPushforward_iso` is a theorem,
> `Stacks.SheafOfModules.ranSMul_squareComparison`, so no hypothesis beyond the square, the
> cofinality and the structure map remains, and the isomorphism itself is available: it is the
> inverse of `Stacks.SheafOfModules.squareComparison`.

```lean
def inverseImageCompCocontinuousPushforwardOfIso
    (fSharp : OD ⟶ (u.sheafPushforwardCocontinuous RingCat.{r} J K).obj OC)
    (hsq : u' ⋙ v = v' ⋙ u)
    (hfinal : ∀ V' : D',
      (CostructuredArrow.map₂ (S := u') (T := V') (U := u) (V := v.obj V') (F := v') (G := v)
        (eqToHom hsq.symm) (𝟙 (v.obj V'))).Final) :
    inverseImage.{v} J' J v' OC ⋙
        (CocontinuousPushforward.of.{v} J' K' u'
          (structureMapSquare (J' := J') (K' := K') fSharp hsq)).functor ≅
      (CocontinuousPushforward.of.{v} J K u fSharp).functor ⋙ inverseImage.{v} K' K v OD
```

**`Stacks.SheafOfModules.lowerShriekCompLeftAdjointOfIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekCocontinuousSquare.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekCocontinuousSquare.lean#L501). The attribute's comment: “second conclusion: `g'_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ g_!` on sheaves of modules, for a commutative square of ringed topoi whose four functors `u`, `u'`, `v`, `v'` are cocontinuous, with `v`, `v'` continuous as well, with the comparison functors of the index categories of Section 00XF cofinal, and with `g^{-1} O_D = O_{D'}`, `(g')^{-1} O_C = O_{C'}`. Deduced from the first conclusion by uniqueness of left adjoints, so an isomorphism and not an equality. `g_!` and `g'_!` are the lower shriek of Stacks 0797, and `f^{-1}`, `(f')^{-1}` the inverse image `f^* G = O_C ⊗_{f^{-1}O_D} f^{-1}G` of `Stacks.SheafOfModules.inverseImageCocontinuous`: all four are constructed, none assumed, so the source's condition (1) — a cocontinuous functor giving rise to a morphism of ringed topoi — is a theorem here. The direct images along `u` and `u'` are the canonical ones attached to the structure map `f^♯ : O_D → {}_su O_C`.”.

> **Stacks 0FN3**, second conclusion, for the canonical direct images. In the situation of
> `Stacks.SheafOfModules.inverseImageCompCocontinuousPushforwardOfIso` we have
> `g'_! ∘ (f')^{-1} ≅ f^{-1} ∘ g_!`. The composite
> `g'_! ∘ (f')^{-1}` is left adjoint to `f'_* ∘ (g')^*` and `f^{-1} ∘ g_!` is left adjoint to
> `g^* ∘ f_*`; by the first conclusion those two right adjoints are isomorphic, so uniqueness of
> left adjoints identifies the two composites. The left adjoints `g_!` and `g'_!` of `g^*` and
> `(g')^*` are the concrete lower shriek of Stacks 0797, and the inverse images `f^{-1}` and
> `(f')^{-1}` of the two canonical direct images along the cocontinuous `u` and `u'` — which is
> condition (1) — are `Stacks.SheafOfModules.inverseImageCocontinuous`, constructed by
> `Stacks.SheafOfModules.inverseImageCocontinuousAdjunction`. All four exist by the `UnivLE`,
> `HasWeakSheafify` and `WEqualsLocallyBijective` hypotheses of this section.

```lean
def lowerShriekCompLeftAdjointOfIso
    (fSharp : OD ⟶ (u.sheafPushforwardCocontinuous RingCat.{r} J K).obj OC)
    (hsq : u' ⋙ v = v' ⋙ u)
    (hfinal : ∀ V' : D',
      (CostructuredArrow.map₂ (S := u') (T := V') (U := u) (V := v.obj V') (F := v') (G := v)
        (eqToHom hsq.symm) (𝟙 (v.obj V'))).Final) :
    (CocontinuousPushforward.of.{v} J' K' u'
          (structureMapSquare (J' := J') (K' := K') fSharp hsq)).functor.leftAdjoint ⋙
        lowerShriek.{v} J' J v' OC ≅
      lowerShriek.{v} K' K v OD ⋙
        (CocontinuousPushforward.of.{v} J K u fSharp).functor.leftAdjoint
```

## Tag 0FN4, a lemma

[Tag 0FN4](https://stacks.math.columbia.edu/tag/0FN4) in the Stacks Project.

**`Stacks.SheafOfModules.inverseImage_comp_pushforward_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekContinuousSquare.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekContinuousSquare.lean#L139). The attribute's comment: “first conclusion: `f'_* ∘ (g')^* = g^* ∘ f_*` on sheaves of modules, for a commutative square of ringed topoi whose horizontal functors `u`, `u'` are continuous and whose vertical functors `v`, `v'` are continuous as well as cocontinuous, with `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`”.

> **Stacks 0FN4**, first conclusion. For a commutative square of ringed topoi as in the module
> docstring — `u`, `u'` continuous giving `f`, `f'`, the functors `v`, `v'` continuous as well as
> cocontinuous giving `g`, `g'`, `v ⋙ u = u' ⋙ v'`, and `g^{-1} O_D = O_{D'}`,
> `(g')^{-1} O_C = O_{C'}` — we have `f'_* ∘ (g')^* = g^* ∘ f_*` on sheaves of modules. Both sides
> are restriction along one of the two sides of the square together with restriction of scalars
> along the corresponding composite structure map, and the square says those agree.

```lean
theorem inverseImage_comp_pushforward_eq (hsq : v ⋙ u = u' ⋙ v')
    (hcomm : f'Sharp = restrictStructureMap J' J K' K u u' v v' OC OD fSharp hsq) :
    inverseImage.{v} J' J v' OC ⋙ _root_.SheafOfModules.pushforward.{v} f'Sharp =
      _root_.SheafOfModules.pushforward.{v} fSharp ⋙ inverseImage.{v} K' K v OD
```

**`Stacks.SheafOfModules.pullbackCompLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekContinuousSquare.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LowerShriekContinuousSquare.lean#L176). The attribute's comment: “second conclusion: `g'_! ∘ (f')⁻¹ ≅ f⁻¹ ∘ g_!` on sheaves of modules, for a commutative square of ringed topoi whose horizontal functors `u`, `u'` are continuous and whose vertical functors `v`, `v'` are continuous as well as cocontinuous, with `g^{-1} O_D = O_{D'}` and `(g')^{-1} O_C = O_{C'}`; a canonical isomorphism rather than an equality, uniqueness of left adjoints giving no more. `g_!` and `g'_!` are the lower shriek of Stacks 0797 and `f⁻¹`, `(f')⁻¹` the pullback of Stacks 03D7; the existence of all four is proved, not assumed.”.

> **Stacks 0FN4**, second conclusion. In the situation of
> `Stacks.SheafOfModules.inverseImage_comp_pushforward_eq` we have
> `g'_! ∘ (f')^{-1} ≅ f^{-1} ∘ g_!`, where `g_!` and `g'_!` are the lower shriek
> `Stacks.SheafOfModules.lowerShriek` of Stacks 0797 and `f^{-1}`, `(f')^{-1}` are the pullbacks
> `SheafOfModules.pullback` of Stacks 03D7. The composite `g'_! ∘ (f')^{-1}` is left adjoint to
> `f'_* ∘ (g')^*` and `f^{-1} ∘ g_!` is left adjoint to `g^* ∘ f_*`; by the first conclusion those
> two right adjoints are the same functor, so uniqueness of left adjoints identifies the two
> composites.
>
> Nothing beyond the square is assumed: the four adjunctions are
> `Stacks.SheafOfModules.lowerShriekAdjunction` of Stacks 0797 and
> `SheafOfModules.pullbackPushforwardAdjunction` of Stacks 03D7, which the `UnivLE`,
> `HasWeakSheafify` and `WEqualsLocallyBijective` hypotheses of this section make available.

```lean
def pullbackCompLowerShriekIso (hsq : v ⋙ u = u' ⋙ v')
    (hcomm : f'Sharp = restrictStructureMap J' J K' K u u' v v' OC OD fSharp hsq) :
    _root_.SheafOfModules.pullback.{v} f'Sharp ⋙ lowerShriek.{v} J' J v' OC ≅
      lowerShriek.{v} K' K v OD ⋙ _root_.SheafOfModules.pullback.{v} fSharp
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.41, Tag 0796](https://stacks.math.columbia.edu/tag/0796)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
