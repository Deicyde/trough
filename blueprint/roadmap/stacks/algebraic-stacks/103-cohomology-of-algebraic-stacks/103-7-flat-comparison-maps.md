---
declaration: section
origin: cited
lean: restrictModulePullbackComparison, AlgebraicGeometry.Stack.HasFlatBaseChangeProperty, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit, AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_cokernel, AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_initial, AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_colimit
statement: formalized
proof: formalized
---

# 103.7 Flat comparison maps

Section 103.7 of the Stacks Project, [Tag 0760](https://stacks.math.columbia.edu/tag/0760). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0761, an equation

[Tag 0761](https://stacks.math.columbia.edu/tag/0761) in the Stacks Project.

Declarations registered for the tag:

- [`restrictModulePullbackComparison`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=restrictModulePullbackComparison#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeProperty.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeProperty.lean#L60) (StacksFrontier): “the comparison map `c_φ`”.

## Tag 0762, a definition

[Tag 0762](https://stacks.math.columbia.edu/tag/0762) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasFlatBaseChangeProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeProperty.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeProperty.lean#L71).

> **Stacks 0762.** A presheaf of modules over the structure sheaf of a category fibred in
> groupoids *has the flat base change property* when the comparison map `c_φ` of Stacks 0761 is an
> isomorphism for every arrow `φ` of `𝒳` lying over a flat morphism of schemes.
>
> The source calls the name nonstandard.

```lean
noncomputable abbrev HasFlatBaseChangeProperty {𝒳 : Type v} [Category.{w} 𝒳]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology)
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp τ hτ).obj) : Prop
```

## Tag 0764, a lemma

[Tag 0764](https://stacks.math.columbia.edu/tag/0764) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L220). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: a colimit of presheaves of modules with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L237). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the vertex of a colimit cocone on a diagram of presheaves of modules with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L279). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the modules with the flat base change property have colimits”.

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

**`AlgebraicGeometry.Stack.isClosedUnderColimitsOfShape_flatBaseChangeModulePresheaves`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L279). The attribute's comment: “part (4), with the ambient category the presheaves of modules rather than the étale sheaves of modules: those colimits agree with the colimits of all modules”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L298). The attribute's comment: “part (2), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the closure under cokernels asked for by Stacks 0754”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangeProperty_initial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeColimits.lean#L317). The attribute's comment: “part (2), with the ambient category the presheaves of modules rather than the étale sheaves of modules: the zero object asked for by Stacks 0754”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L332). The attribute's comment: “part (4), with the ambient category the étale sheaves of modules, as the source states it -- and so with a_small^* the inverse image of sheaves of modules, not the inverse image of presheaves of modules used by the part (4) registrations of FlatBaseChangeColimits: a colimit of étale sheaves of modules with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L378). The attribute's comment: “part (4), with the ambient category the étale sheaves of modules, as the source states it -- and so with a_small^* the inverse image of sheaves of modules, not the inverse image of presheaves of modules used by the part (4) registrations of FlatBaseChangeColimits: the vertex of a colimit cocone on a diagram of étale sheaves of modules with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.hasColimitsOfShape_flatBaseChangeEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L592). The attribute's comment: “part (4), in the source's ambient category Mod(X_etale, O_X): the full subcategory of etale sheaves of modules with the flat base change property has colimits”.

> **Stacks 0764, part (4), as the source states it**: the category of étale sheaves of
> `𝒪_𝒳`-modules with the flat base change property has the colimits that `Mod(𝒳_étale, 𝒪_𝒳)`
> has; those colimits exist, the étale sheafification of abelian presheaves on `𝒳` being
> available unconditionally.

```lean
theorem hasColimitsOfShape_flatBaseChangeEtaleModules :
    HasColimitsOfShape J (flatBaseChangeEtaleModules.{u, v, w} B E h S hS p hp).FullSubcategory
```

**`AlgebraicGeometry.Stack.preservesColimitsOfShape_flatBaseChangeEtaleModules_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafColimits.lean#L608). The attribute's comment: “part (4), in the source's ambient category Mod(X_etale, O_X): the colimits of the subcategory agree with the colimits in Mod(X_etale, O_X)”.

> **Stacks 0764, part (4), as the source states it**: the colimits of étale sheaves of
> `𝒪_𝒳`-modules with the flat base change property agree with the colimits of
> `Mod(𝒳_étale, 𝒪_𝒳)`, the inclusion preserving them.

```lean
theorem preservesColimitsOfShape_flatBaseChangeEtaleModules_ι :
    PreservesColimitsOfShape J (flatBaseChangeEtaleModules.{u, v, w} B E h S hS p hp).ι
```

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_etaleInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInternalHom.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInternalHom.lean#L153). The attribute's comment: “part (6): for F, G in Mod(𝒳_étale, 𝒪_𝒳) with F of finite presentation and G with the flat base change property, the internal Hom 𝓗om_{𝒪_𝒳}(F, G) of Mod(𝒳_étale, 𝒪_𝒳) has the flat base change property”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInverseImage.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafInverseImage.lean#L267). The attribute's comment: “part (1), the whole part, in the source's ambient category of étale sheaves of modules (a_small^* the inverse image of sheaves of modules), for any 1-morphism f : 𝒳 ⥤ 𝒴 of categories fibred in groupoids over (Sch/S)_fppf, in particular any morphism of algebraic stacks: the inverse image f^*F of a module F with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafSmoothLocal.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafSmoothLocal.lean#L120). The attribute's comment: “part (3), the whole part, in the source's ambient category of étale sheaves of modules (a_small^* the inverse image of sheaves of modules): for a family of smooth 1-morphisms f j : 𝒵 j ⟶ 𝒳 of algebraic stacks with |𝒳| = ⋃ j, |f j|(|𝒵 j|), if each inverse image f j^* F has the flat base change property then so does F”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafTensor.lean, line 816](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafTensor.lean#L816). The attribute's comment: “part (5), with the ambient category the étale sheaves of modules, as the source states it -- and so with a_small^* the inverse image of sheaves of modules: the tensor product in Mod(𝒳_étale, 𝒪_𝒳) of two modules with the flat base change property has the flat base change property”.

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

**`AlgebraicGeometry.Stack.isWeakSerreClass_flatBaseChangeEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafWeakSerre.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSheafWeakSerre.lean#L215). The attribute's comment: “part (2): the étale sheaves of O_X-modules with the flat base change property form a weak Serre subcategory of Mod(X_etale, O_X), in the form of Stacks 0754 -- strictly full, with a zero object, and closed under kernels, cokernels and extensions. The whole of part (2), in the source's ambient category, with a_small^* the inverse image of sheaves of modules, and with no hypothesis beyond the source's”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertySheaf_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFlatBaseChangeSheaf.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageFlatBaseChangeSheaf.lean#L168). The attribute's comment: “R^i f_* of a locally quasi-coherent étale module with the flat base change property has the flat base change property, for f quasi-compact and quasi-separated”.

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

**`AlgebraicGeometry.Stack.hasFlatBaseChangePropertyUnivLE_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalCriterion.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalCriterion.lean#L582). The attribute's comment: “the whole statement, in every degree and with the source's hypotheses unweakened, granted six named hypotheses: Stacks 076Z quantified over every rule; the weak Serre condition for LQCoh^fbc (Stacks 06WM (1)-(3), Stacks 0764 (2)); Stacks 0764 (1) and (3); Stacks 075Y at section universe u+1; and the affine case (Stacks 075P, Stacks 073K)”.

> **Stacks 0765.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact (**Stacks 050U**) and quasi-separated
> (**Stacks 04YW**) 1-morphism of algebraic stacks over `S` and let `ℱ` be a sheaf of `𝒪_𝒳`-modules
> on `𝒳_étale` which is locally quasi-coherent (**Stacks 06WJ**) and has the flat base change
> property (**Stacks 0762**). Then every higher direct image `Rⁱf_*ℱ`, computed in the étale
> topology, has the flat base change property.
>
> The conclusion is `AlgebraicGeometry.Stack.HasFlatBaseChangePropertyHigherDirectImage`: both
> hypotheses on `ℱ` are the source's, the conclusion is about the flat base change property alone as
> in the source, and it holds in every degree.
>
> The route is the source's: the criterion of **Stacks 076Z** at the rule `LQCoh^fbc`, whose
> conclusion gives local quasi-coherence of `Rⁱf_*ℱ` — which is **Stacks 075Z** — and the flat base
> change property, of which only the latter is asserted. Five hypotheses are carried, each a clause
> of that criterion at `LQCoh^fbc` or at the flat base change property alone, and each a result of
> the source this library does not have:
>
> * `hcrit` is **Stacks 076Z**, quantified over every rule.
> * `hserre` is hypothesis (1) for `LQCoh^fbc`, which is parts (1) to (3) of **Stacks 06WM**
>   together with part (2) of **Stacks 0764**.
> * `hfbcPull` is the flat base change half of hypothesis (2), which is part (1) of **Stacks 0764**;
>   its local quasi-coherence half is **Stacks 06WL** and is proved.
> * `hconvLqc` and `hconvFbc` are the two halves of the converse of hypothesis (3), namely
>   **Stacks 075Y** at section universe `u + 1` and part (3) of **Stacks 0764**.
> * `haffine` is hypothesis (4) for `LQCoh^fbc`, which the source proves from **Stacks 075P** and
>   **Stacks 073K**; **Stacks 073K** is proved but the cohomological content of **Stacks 075P** is
>   not.

```lean
theorem hasFlatBaseChangePropertyUnivLE_moduleSheafHigherDirectImage
    (hcrit : SmoothLocalHigherDirectImageCriterion.{u, t, s} B S hS)
    (hserre : StackEtaleModuleRule.IsWeakSerre.{u, t} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    (hfbcPull : StackEtaleModuleRule.IsStableUnderSmoothPullback.{u, t} B S hS
      (flatBaseChangePropertyRule B E h S hS))
    (hconvLqc : StackEtaleModuleRule.IsSmoothLocalConverse.{u, t, s} B S hS
      (locallyQuasicoherentRule B E h S hS))
    (hconvFbc : StackEtaleModuleRule.IsSmoothLocalConverse.{u, t, s} B S hS
      (flatBaseChangePropertyRule B E h S hS))
    (haffine : StackEtaleModuleRule.PreservesHigherDirectImagesOfAffine.{u, t} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f) (i : ℕ) :
    HasFlatBaseChangePropertyHigherDirectImage B E h S hS f i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.7, Tag 0760](https://stacks.math.columbia.edu/tag/0760)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
