---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.restrictSheafModulesPullbackComparison, AlgebraicGeometry.Stack.HasFlatBaseChangePropertySheafUnivLE, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit, AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_cokernel, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_initial, AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_colimit
statement: formalized
proof: formalized
---

# 103.7 Flat comparison maps

Section 103.7 of the Stacks Project, [Tag 0760](https://stacks.math.columbia.edu/tag/0760). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0761, an equation

[Tag 0761](https://stacks.math.columbia.edu/tag/0761) in the Stacks Project.

**`AlgebraicGeometry.Stack.restrictSheafModulesPullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L287). The attribute's comment: “with `f_{small}^*` the pullback of sheaves of modules along the morphism of ringed topoi of the small étale sites”.

> **Stacks 0761.** The comparison map
> `c_φ : f_{small}^*(F|_{U'_ét}) ⟶ F|_{U_ét}` of Equation (103.7.0.1) for an étale sheaf `F` of
> `𝒪_𝒳`-modules, below an arrow `φ : x ⟶ y` of `𝒳` lying over a morphism of schemes
> `f : U ⟶ U'`. Here `f_{small}^*` is the pullback of modules along the morphism of ringed topoi
> `(Sh(U_ét), 𝒪_U) ⟶ (Sh(U'_ét), 𝒪_{U'})`, that is `SheafOfModules.pullback` along the morphism
> of ringed sites `ε_f` of **Stacks 070R (2)**, whose ring map is the map `f_{small}^♯` of
> **Stacks 06WC**; it includes sheafification.
>
> It is `AlgebraicGeometry.Stack.restrictSheafPullbackComparison` (the adjunct, across
> sheafification on `U_ét`, of the presheaf map
> `AlgebraicGeometry.Stack.restrictModulePullbackComparison` of Sheaves on Stacks, Equation
> (96.9.4.1)) read through the identification
> `AlgebraicGeometry.Stack.sheafifiedPullbackComparisonIso` of the sheafified presheaf pullback
> with `SheafOfModules.pullback`.
>
> This is also **Stacks 06WC**, the comparison map
> `c_φ : a_{small}^*(F|_{V_ét}) ⟶ F|_{U_ét}` of `𝒪_{U_ét}`-modules of Sheaves on Stacks,
> Equation (96.9.4.1), for an étale sheaf `F` of modules on `𝒳`: there too `a_{small}^*` is the
> pullback of sheaves of modules along `ε_a`, the map `a_{small}^♯` being the one of Stacks 070R,
> and `F|_{V_ét}`, `F|_{U_ét}` are the restrictions of Stacks 06WJ.

```lean
noncomputable def restrictSheafModulesPullbackComparison
    (F : SheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))) :
    (SheafOfModules.pullback.{u} (SmallEtale.smallEtaleStructureMapRing E
        (smallEtaleBaseMorphism B E h S hS p φ))).obj
        ((restrictSheafToSmallEtale.{u, v, w, u} B E h S hS p hp y).obj F) ⟶
      (restrictSheafToSmallEtale.{u, v, w, u} B E h S hS p hp x).obj F
```

## Tag 0762, a definition

[Tag 0762](https://stacks.math.columbia.edu/tag/0762) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasFlatBaseChangePropertySheafUnivLE`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L329). The attribute's comment: “for an étale sheaf of modules on a category fibred in groupoids, with `f_{small}^*` the pullback of sheaves of modules”.

> **Stacks 0762.** An étale sheaf of `𝒪_𝒳`-modules *has the flat base change property* when the
> comparison map `c_φ` of **Stacks 0761**, taken with `a_{small}^*` the inverse image of sheaves of
> modules as the source takes it, is an isomorphism for every arrow `φ` of `𝒳` lying over a flat
> morphism of schemes. The source calls the name nonstandard.
>
> This is the property read in the source's ambient category `Mod(𝒳_étale, 𝒪_𝒳)`. The source
> takes `𝒳` an algebraic stack; here `𝒳` is any category fibred in groupoids over
> `(Sch/S)_{fppf}`. The module sections live in any universe `m` with `UnivLE.{u, m}`; the source's
> case is `m = u`, where `UnivLE.{u, u}` always holds, so this is no extra hypothesis. At `m = u`
> the comparison map is `AlgebraicGeometry.Stack.restrictSheafModulesPullbackComparison`, whose
> domain is `SheafOfModules.pullback`, up to the isomorphism of
> `hasFlatBaseChangePropertySheafUnivLE_iff_isIso_restrictSheafModulesPullbackComparison`.
> `AlgebraicGeometry.Stack.HasFlatBaseChangeProperty` is the same definition with the inverse image
> of presheaves of modules, which on an étale sheaf is strictly the stronger demand; the
> implementation notes of this file say why.

```lean
noncomputable abbrev HasFlatBaseChangePropertySheafUnivLE
    (F : SheafOfModules.{m} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))) : Prop
```

## Tag 0764, a lemma

[Tag 0764](https://stacks.math.columbia.edu/tag/0764) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L220). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: a colimit of presheaves of modules with the flat base change property has the flat base change property”.

> **Stacks 0764, part (4), for presheaves of modules.** The colimit of a diagram of presheaves
> of `𝒪_𝒳`-modules each having the flat base change property of **Stacks 0762** again has the flat
> base change property, and the colimit is the colimit of presheaves of modules.
>
> For an arrow `φ` of `𝒳` lying over a flat morphism of schemes, the comparison map `c_φ` is the
> component of a natural transformation from `F ↦ a_{small}^*(F|_{V_ét})` to `F ↦ F|_{U_ét}`. Both
> functors preserve colimits — the first because `a_{small}^*` is a left adjoint, the second
> because restriction to the small étale site is restriction along a functor followed by a change
> of scalars — and the component at a colimit of a natural transformation of colimit-preserving
> functors is an isomorphism as soon as every component on the diagram is.

```lean
theorem hasFlatBaseChangeProperty_colimit
    (K : J ⥤ PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp τ hτ).obj)
    (hK : ∀ i, HasFlatBaseChangeProperty B E h S hS p hp τ hτ (K.obj i)) :
    HasFlatBaseChangeProperty B E h S hS p hp τ hτ (colimit K)
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L237). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the vertex of a colimit cocone on a diagram of presheaves of modules with the flat base change property has the flat base change property”.

> **Stacks 0764, part (4), for presheaves of modules**, in the form for an arbitrary colimit
> cocone: the vertex of a colimit cocone on a diagram of presheaves of `𝒪_𝒳`-modules with the flat
> base change property has the flat base change property.
>
> This is `AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit` transported along the
> canonical isomorphism of the vertex with the chosen colimit.

```lean
theorem hasFlatBaseChangeProperty_of_isColimit
    {K : J ⥤ PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp τ hτ).obj}
    {c : Cocone K} (hc : IsColimit c)
    (hK : ∀ i, HasFlatBaseChangeProperty B E h S hS p hp τ hτ (K.obj i)) :
    HasFlatBaseChangeProperty B E h S hS p hp τ hτ c.pt
```

**`AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L279). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the modules with the flat base change property have colimits”.

> The presheaves of modules with the flat base change property are closed under colimits of
> shape `J`, by `AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit`.
>
> This is **Stacks 0764, part (4), for presheaves of modules**: through Mathlib's instances
> `CategoryTheory.Limits.hasColimitsOfShape_of_closedUnderColimits` and
> `CategoryTheory.preservesColimitOfShape_of_createsColimitsOfShape_and_hasColimitsOfShape`, the
> subcategory has colimits of shape `J` and its inclusion preserves them.

```lean
instance isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves :
    ObjectProperty.IsClosedUnderColimitsOfShape
      (flatBaseChangeModulePresheaves.{u, v, w} B E h S hS p hp τ hτ) J
```

**`AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L279). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: those colimits agree with the colimits of all modules”.

> The presheaves of modules with the flat base change property are closed under colimits of
> shape `J`, by `AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit`.
>
> This is **Stacks 0764, part (4), for presheaves of modules**: through Mathlib's instances
> `CategoryTheory.Limits.hasColimitsOfShape_of_closedUnderColimits` and
> `CategoryTheory.preservesColimitOfShape_of_createsColimitsOfShape_and_hasColimitsOfShape`, the
> subcategory has colimits of shape `J` and its inclusion preserves them.

```lean
instance isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves :
    ObjectProperty.IsClosedUnderColimitsOfShape
      (flatBaseChangeModulePresheaves.{u, v, w} B E h S hS p hp τ hτ) J
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L298). The attribute's comment: “part (2), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the closure under cokernels asked for by Stacks 0754”.

> **Stacks 0764, part (2), for presheaves of modules.** The cokernel of a morphism of
> presheaves of `𝒪_𝒳`-modules with the flat base change property of **Stacks 0762** has the flat
> base change property. This is the closure under cokernels asked for by **Stacks 0754**.
>
> A cokernel is a colimit indexed by the walking parallel pair, whose two values are the source
> and the target of the morphism, so this is a case of
> `AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit`.

```lean
theorem hasFlatBaseChangeProperty_cokernel
    {F G : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp τ hτ).obj} (α : F ⟶ G)
    (hF : HasFlatBaseChangeProperty B E h S hS p hp τ hτ F)
    (hG : HasFlatBaseChangeProperty B E h S hS p hp τ hτ G) :
    HasFlatBaseChangeProperty B E h S hS p hp τ hτ (cokernel α)
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_initial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L317). The attribute's comment: “part (2), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the zero object asked for by Stacks 0754”.

> **Stacks 0764, part (2), for presheaves of modules.** An initial presheaf of
> `𝒪_𝒳`-modules — equivalently, a zero object — has the flat base change property of
> **Stacks 0762**. This is the containment of a zero object asked for by **Stacks 0754**.
>
> An initial object is the colimit of the empty diagram, so this is the case of
> `AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit` in which the hypothesis on the
> diagram is vacuous.

```lean
theorem hasFlatBaseChangeProperty_initial
    {F : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp τ hτ).obj}
    (hF : IsInitial F) :
    HasFlatBaseChangeProperty B E h S hS p hp τ hτ F
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L404). The attribute's comment: “part (4), with the ambient category the étale sheaves of modules, as the source states it -- and so with a\_small^* the inverse image of sheaves of modules, not the inverse image of presheaves of modules used by the part (4) registrations of FlatBaseChangeColimits: a colimit of étale sheaves of modules with the flat base change property has the flat base change property”.

> **Stacks 0764, part (4), as the source states it.** The colimit of a diagram of étale sheaves
> of `𝒪_𝒳`-modules each having the flat base change property of **Stacks 0762** again has the flat
> base change property, the colimit being the colimit of `Mod(𝒳_étale, 𝒪_𝒳)`.
>
> For an arrow `φ` of `𝒳` lying over a flat morphism of schemes, `c_φ^{sh}` is the component of a
> natural transformation from `F ↦ a_{small}^*(F|_{V_ét})` to `F ↦ F|_{U_ét}`. Both functors
> preserve colimits — the first because the inverse image of sheaves of modules is a left adjoint,
> by `AlgebraicGeometry.Stack.sheafifiedPullbackComparisonAdjunction`, the second by
> `AlgebraicGeometry.Stack.preservesColimitsOfShape_restrictSheafToSmallEtale` — and the component
> at a colimit of a natural transformation of colimit-preserving functors is an isomorphism as
> soon as every component on the diagram is.

```lean
theorem hasFlatBaseChangePropertySheaf_colimit
    (K : J ⥤ SheafOfModules.{m} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))) [HasColimit K]
    (hK : ∀ i, HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp (K.obj i)) :
    HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp (colimit K)
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L450). The attribute's comment: “part (4), with the ambient category the étale sheaves of modules, as the source states it -- and so with a\_small^* the inverse image of sheaves of modules, not the inverse image of presheaves of modules used by the part (4) registrations of FlatBaseChangeColimits: the vertex of a colimit cocone on a diagram of étale sheaves of modules with the flat base change property has the flat base change property”.

> **Stacks 0764, part (4), as the source states it**, in the form for an arbitrary colimit
> cocone: the vertex of a colimit cocone on a diagram of étale sheaves of `𝒪_𝒳`-modules with the
> flat base change property has the flat base change property.
>
> This is `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_colimit` transported along the
> canonical isomorphism of the vertex with the chosen colimit.

```lean
theorem hasFlatBaseChangePropertySheaf_of_isColimit
    {K : J ⥤ SheafOfModules.{m} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))} {c : Cocone K} (hc : IsColimit c)
    (hK : ∀ i, HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp (K.obj i)) :
    HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp c.pt
```

**`AlgebraicGeometry.Stack.hasColimitsOfShape_flatBaseChangeEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 664](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L664). The attribute's comment: “part (4), in the source's ambient category Mod(X\_etale, O\_X): the full subcategory of etale sheaves of modules with the flat base change property has colimits”.

> **Stacks 0764, part (4), as the source states it**: the category of étale sheaves of
> `𝒪_𝒳`-modules with the flat base change property has the colimits that `Mod(𝒳_étale, 𝒪_𝒳)`
> has; those colimits exist, the étale sheafification of abelian presheaves on `𝒳` being
> available unconditionally.

```lean
theorem hasColimitsOfShape_flatBaseChangeEtaleModules :
    HasColimitsOfShape J (flatBaseChangeEtaleModules.{u, v, w} B E h S hS p hp).FullSubcategory
```

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_flatBaseChangeEtaleModules_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 680](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L680). The attribute's comment: “part (4), in the source's ambient category Mod(X\_etale, O\_X): the colimits of the subcategory agree with the colimits in Mod(X\_etale, O\_X)”.

> **Stacks 0764, part (4), as the source states it**: the colimits of étale sheaves of
> `𝒪_𝒳`-modules with the flat base change property agree with the colimits of
> `Mod(𝒳_étale, 𝒪_𝒳)`, the inclusion preserving them.

```lean
theorem preservesColimitsOfShape_flatBaseChangeEtaleModules_ι :
    PreservesColimitsOfShape J (flatBaseChangeEtaleModules.{u, v, w} B E h S hS p hp).ι
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_etaleInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInternalHom.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInternalHom.lean#L153). The attribute's comment: “part (6): for F, G in Mod(𝒳\_étale, 𝒪\_𝒳) with F of finite presentation and G with the flat base change property, the internal Hom 𝓗om\_\{𝒪\_𝒳}(F, G) of Mod(𝒳\_étale, 𝒪\_𝒳) has the flat base change property”.

> **Stacks 0764, part (6).** Let `p : 𝒳 ⥤ (Sch/S)_{fppf}` be a category fibred in groupoids and
> let `F`, `G` be étale sheaves of `𝒪_𝒳`-modules, with `F` of finite presentation on `𝒳_étale`
> (Stacks 03DL) and `G` with the flat base change property of Stacks 0762. Then the internal Hom
> `𝓗om_{𝒪_𝒳}(F, G)` of `Mod(𝒳_étale, 𝒪_𝒳)` has the flat base change property.
>
> Let `φ : x ⟶ y` lie over a flat morphism, and let `{e_j : y_j ⟶ y}` be an étale covering on
> whose members `F` has a finite presentation. At every arrow into some `y_j` lying over a flat
> morphism the comparison map of `𝓗om(F, G)` is invertible by the presented case proved above, and
> that suffices for `c_φ` by the étale-local criterion
> `AlgebraicGeometry.Stack.isIso_restrictSheafPullbackComparison_of_etaleCover`.

```lean
theorem hasFlatBaseChangePropertySheaf_etaleInternalHom
    (F G : SheafOfModules.{u}
      (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)))
    (hfp : F.IsFinitePresentationOnSite)
    (hG : HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp G) :
    HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp (etaleInternalHom B S hS p hp F G)
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInverseImage.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInverseImage.lean#L267). The attribute's comment: “part (1), the whole part, in the source's ambient category of étale sheaves of modules (a\_small^* the inverse image of sheaves of modules), for any 1-morphism f : 𝒳 ⥤ 𝒴 of categories fibred in groupoids over (Sch/S)\_fppf, in particular any morphism of algebraic stacks: the inverse image f^*F of a module F with the flat base change property has the flat base change property”.

> **Stacks 0764, part (1), in the source's ambient category.** Let `f : 𝒳 ⥤ 𝒴` be a
> 1-morphism of categories fibred in groupoids over the big fppf category of `S`, and let `F` be an
> étale sheaf of `𝒪_𝒴`-modules with the flat base change property of **Stacks 0762** (comparison
> maps taken with the inverse image of sheaves of modules on the small étale sites). Then the
> inverse image `f^*F` of sheaves of modules has the flat base change property.
>
> An arrow `φ` of `𝒳` lies over the same morphism of schemes as `f φ`, so this is
> `AlgebraicGeometry.Stack.isIso_restrictSheafPullbackComparison_modulePullback_iff` at each arrow
> lying over a flat morphism.

```lean
theorem hasFlatBaseChangePropertySheaf_modulePullback
    (F : SheafOfModules.{m} (ringStructureSheafCore B S hS q hq (etaleTopology B)
      (etaleTopology_le_topology B)))
    (hF : HasFlatBaseChangePropertySheafUnivLE B E h S hS q hq F) :
    HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp
      ((modulePullback B S hS p q hp hq f hf (etaleTopology B)
        (etaleTopology_le_topology B)).obj F)
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafSmoothLocal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafSmoothLocal.lean#L120). The attribute's comment: “part (3), the whole part, in the source's ambient category of étale sheaves of modules (a\_small^* the inverse image of sheaves of modules): for a family of smooth 1-morphisms f j : 𝒵 j ⟶ 𝒳 of algebraic stacks with |𝒳| = ⋃ j, |f j|(|𝒵 j|), if each inverse image f j^* F has the flat base change property then so does F”.

> **Stacks 0764, part (3), in the source's ambient category.** Let `f j : 𝒵 j ⟶ 𝒳` be a family
> of smooth 1-morphisms of algebraic stacks over `S` with `|𝒳| = ⋃ j, |f j|(|𝒵 j|)`, and let `F` be
> an étale sheaf of `𝒪_𝒳`-modules. If every inverse image `f j^* F` of sheaves of modules has the
> flat base change property of **Stacks 0762**, then so does `F`.
>
> `AlgebraicGeometry.Stack.exists_etaleCovering_family_fibre_lift` covers the scheme below any
> object of `𝒳` by étale morphisms over which the object lifts through some `f j`, and
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_etaleLocal` concludes.

```lean
theorem hasFlatBaseChangePropertySheaf_of_isSmooth_jointlySurjective [UnivLE.{u, m}]
    {J : Type v} {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳)
    (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)))
    (hF : ∀ j, HasFlatBaseChangePropertySheafUnivLE B E h S hS
      (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
      ((modulePullback B S hS (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
        𝒳.val.val.p (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
        𝒳.val.isFiberedInGroupoids (CatFiberedInGroupoids.homFunctor (f j).hom) rfl
        (etaleTopology B) (etaleTopology_le_topology B)).obj F)) :
    HasFlatBaseChangePropertySheafUnivLE B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids F
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafTensor.lean, line 816](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafTensor.lean#L816). The attribute's comment: “part (5), with the ambient category the étale sheaves of modules, as the source states it -- and so with a\_small^* the inverse image of sheaves of modules: the tensor product in Mod(𝒳\_étale, 𝒪\_𝒳) of two modules with the flat base change property has the flat base change property”.

> **Stacks 0764, part (5).** The tensor product, in `Mod(𝒳_étale, 𝒪_𝒳)`, of two étale sheaves of
> `𝒪_𝒳`-modules with the flat base change property of **Stacks 0762** has the flat base change
> property.
>
> The tensor product is the canonical one, `Stacks.SheafOfModules.Tensor.sheafTensor` at the
> structure sheaf of the associated étale site; it is
> `AlgebraicGeometry.Stack.etaleTensorSheaf` by `AlgebraicGeometry.Stack.etaleTensorSheaf_eq`. The
> sheafification instances it is formed with hold for every `𝒳`, by
> `AlgebraicGeometry.Stack.hasSheafify_etaleAssociatedTopology` and
> `AlgebraicGeometry.Stack.wEqualsLocallyBijective_etaleAssociatedTopology`, and are supplied here.
>
> At an arrow over a flat morphism of schemes this is
> `AlgebraicGeometry.Stack.isIso_restrictSheafPullbackComparison_etaleTensorSheaf`: the
> restrictions commute with tensor products, the pullback commutes with tensor products by
> **Stacks 03EL**, and under these identifications the comparison map of the tensor product is the
> tensor product of the comparison maps.

```lean
theorem hasFlatBaseChangePropertySheaf_tensor
    (F G : SheafOfModules.{u}
      (ringStructureSheafCore B S hS p hp (etaleTopology B) (etaleTopology_le_topology B)))
    (hF : HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp F)
    (hG : HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp G) :
    letI := hasSheafify_etaleAssociatedTopology B S hS p hp
    letI := wEqualsLocallyBijective_etaleAssociatedTopology B S hS p hp
    HasFlatBaseChangePropertySheafUnivLE B E h S hS p hp
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, _, u, u}
        (structureSheaf B S hS p hp (etaleTopology B)
          (etaleTopology_le_topology B))).obj F).obj G)
```

**`AlgebraicGeometry.Stack.isWeakSerreClass_flatBaseChangeEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafWeakSerre.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafWeakSerre.lean#L215). The attribute's comment: “part (2): the étale sheaves of O\_X-modules with the flat base change property form a weak Serre subcategory of Mod(X\_etale, O\_X), in the form of Stacks 0754 -- strictly full, with a zero object, and closed under kernels, cokernels and extensions. The whole of part (2), in the source's ambient category, with a\_small^* the inverse image of sheaves of modules, and with no hypothesis beyond the source's”.

> **Stacks 0764, part (2), as the source states it.** The étale sheaves of `𝒪_𝒳`-modules with
> the flat base change property of **Stacks 0762** form a weak Serre subcategory of
> `Mod(𝒳_étale, 𝒪_𝒳)`, in the form **Stacks 0754** gives: a strictly full subcategory containing a
> zero object and closed under kernels, cokernels and extensions.
>
> Strict fullness is
> `AlgebraicGeometry.Stack.isClosedUnderIsomorphisms_flatBaseChangeEtaleModules`, the zero object
> is `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_initial`, the cokernels are
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_cokernel`, the extensions are
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_shortExact`, and the kernels are
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_kernel`, the last with the left exactness
> `AlgebraicGeometry.Stack.preservesFiniteLimits_sheafifiedPullbackComparison`: this is
> `AlgebraicGeometry.Stack.isWeakSerreClass_flatBaseChangeEtaleModules_of_preservesFiniteLimits`
> at section universe `u`.
>
> The abelian structure on `Mod(𝒳_étale, 𝒪_𝒳)` is the one coming from étale sheafification of
> abelian presheaves on `𝒳`, whose two instances are supplied in the statement by
> `AlgebraicGeometry.Stack.hasSheafify_etaleAssociatedTopology` and
> `AlgebraicGeometry.Stack.wEqualsLocallyBijective_etaleAssociatedTopology`; they are not
> hypotheses.

```lean
theorem isWeakSerreClass_flatBaseChangeEtaleModules :
    letI := hasSheafify_etaleAssociatedTopology B S hS p hp
    letI := wEqualsLocallyBijective_etaleAssociatedTopology B S hS p hp
    letI : Abelian (SheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B))) :=
      SheafOfModules.instAbelian (ringStructureSheafCore B S hS p hp (etaleTopology B)
        (etaleTopology_le_topology B))
    (flatBaseChangeEtaleModules.{u, v, w} B E h S hS p hp).IsWeakSerreClass
```

## Tag 0765, a lemma

[Tag 0765](https://stacks.math.columbia.edu/tag/0765) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFlatBaseChangeSheaf.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFlatBaseChangeSheaf.lean#L187). The attribute's comment: “the whole lemma, in every degree, with the source's hypotheses: f quasi-compact and quasi-separated, F an étale O\_X-module that is locally quasi-coherent with the flat base change property (read on sheaves, as in the source); then every R^i f\_* F, computed in the étale topology, has the flat base change property. Proved by the criterion of Stacks 076Z applied to LQCoh^fbc, all four of its conditions discharged”.

> Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact (Stacks 050U) and quasi-separated
> (Stacks 04YW) 1-morphism of algebraic stacks, and let `ℱ` be an étale sheaf of
> `𝒪_𝒳`-modules which is locally quasi-coherent (Stacks 06WJ) and has the flat base change property
> (Stacks 0762). Then every higher direct image `Rⁱf_*ℱ`, computed in the étale topology, has the
> flat base change property.
>
> The flat base change property is the source's, read on sheaves
> (`AlgebraicGeometry.Stack.HasFlatBaseChangePropertySheafUnivLE`); the sheaves of modules have their
> sections in `Type (u + 1)`, where the higher direct images of Stacks 06WE live, and the source
> `𝒳` is presented strictly, its structure functor written as the functor of `f` followed by that
> of `𝒴`.
>
> This is the registered form of **Stacks 0765**: the whole lemma, in every degree, with the
> source's hypotheses and nothing more. The proof is the source's: the criterion of
> **Stacks 076Z** (`AlgebraicGeometry.Stack.smoothLocalHigherDirectImageCriterion_unconditional`)
> at the rule `LQCoh^fbc`, whose four conditions are discharged in this file and its imports
> (**Stacks 06WM**, **Stacks 06WL**, **Stacks 075Y** with **Stacks 0764**, and the affine case).
> The presheaf-reading statement
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertyUnivLE_moduleSheafHigherDirectImage` is untagged.

```lean
theorem hasFlatBaseChangePropertySheaf_moduleSheafHigherDirectImage
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : SheafOfModules.{u + 1} (ringStructureSheafCore B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) (etaleTopology B)
      (etaleTopology_le_topology B)))
    (hlqc : IsLocallyQuasicoherent B E h S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) F.val)
    (hfbc : HasFlatBaseChangePropertySheafUnivLE.{u, u + 1, u, u + 1} B E h S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) F)
    (i : ℕ) :
    letI := hasSheafify_associatedTopology_of_category_succ B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
    letI := wEqualsLocallyBijective_associatedTopology_of_category_succ B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
    letI := hasSheafify_associatedTopology_of_category_succ B S hS 𝒴.val.val.p
    letI := wEqualsLocallyBijective_associatedTopology_of_category_succ B S hS 𝒴.val.val.p
    HasFlatBaseChangePropertySheafUnivLE.{u, u + 1, u, u + 1} B E h S hS 𝒴.val.val.p
      𝒴.val.isFiberedInGroupoids
      ((moduleSheafHigherDirectImage.{u, u + 1, u, u + 1, u} B S hS
        (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p) 𝒴.val.val.p
        (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) 𝒴.val.isFiberedInGroupoids
        (CatFiberedInGroupoids.homFunctor f.hom) rfl (etaleTopology B)
        (etaleTopology_le_topology B) i).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.7, Tag 0760](https://stacks.math.columbia.edu/tag/0760)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
