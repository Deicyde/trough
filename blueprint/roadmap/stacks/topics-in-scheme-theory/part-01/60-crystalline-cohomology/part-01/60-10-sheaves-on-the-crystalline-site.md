---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.Thickening.restrictionFMap, Crystalline.GlobalCrystallineSituation.Thickening.comparison, Crystalline.GlobalCrystallineSituation.Thickening.isIso_comparison, Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction.restrictionFMap, Crystalline.GlobalCrystallineSituation.Thickening.moduleComparisonSheaf, Crystalline.GlobalCrystallineSituation.Thickening.isIso_moduleComparisonSheaf_of_isCartesian, Crystalline.GlobalCrystallineSituation.Thickening.moduleComparison, Crystalline.GlobalCrystallineSituation.Thickening.isIso_moduleComparison
statement: formalized
proof: formalized
---

# 60.10 Sheaves on the crystalline site

Section 60.10 of the Stacks Project, [Tag 07IN](https://stacks.math.columbia.edu/tag/07IN). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07IP, an equation

[Tag 07IP](https://stacks.math.columbia.edu/tag/07IP) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.Thickening.restrictionFMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean, line 752](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean#L752). The attribute's comment: “the f-map assembled from the restriction mappings”.

> **Stacks Project, Tag 07IP.**  The `f`-map from the restriction of a presheaf to the ambient
> scheme of the target of a morphism `f` of `CRIS(X/S)` to its restriction to the ambient scheme of
> the source: over an open `W` of the target it is the presheaf applied to the restriction of `f`
> over `W`.

```lean
def restrictionFMap {A B : Thickening S} (g : A ⟶ B) :
    restriction F B ⟶ g.targetHom.hom.base _* restriction F A
```

**`Crystalline.GlobalCrystallineSituation.Thickening.comparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean, line 766](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean#L766). The attribute's comment: “the comparison map on the big crystalline site, for presheaves”.

> **Stacks Project, Tag 07IP.**  The comparison morphism `c_f : f⁻¹F_{T'} ⟶ F_T` of a morphism
> `f : (U, T, δ) ⟶ (U', T', δ')` of `CRIS(X/S)`, obtained from the `f`-map `F_{T'} ⟶ f_* F_T` by the
> adjunction between inverse and direct image.

```lean
def comparison [HasColimits 𝒜] {A B : Thickening S} (g : A ⟶ B) :
    (TopCat.Presheaf.pullback 𝒜 g.targetHom.hom.base).obj (restriction F B) ⟶ restriction F A
```

**`Crystalline.GlobalCrystallineSituation.Thickening.isIso_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean, line 812](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean#L812). The attribute's comment: “the comparison map is an isomorphism for an open immersion”.

> **The comparison morphism of an open immersion of `CRIS(X/S)` is an isomorphism.**  For a
> Cartesian morphism `f : (U, T, δ) ⟶ (U', T', δ')` which is an open immersion on ambient schemes,
> the restriction `F_T` is the restriction of `F_{T'}` to the open `T` of `T'`, so the comparison
> morphism `c_f : f⁻¹F_{T'} ⟶ F_T` is invertible.

```lean
theorem isIso_comparison [HasColimits 𝒜] {A B : Thickening S} (g : A ⟶ B)
    [IsOpenImmersion g.targetHom.hom] (hg : IsCartesian g) : IsIso (comparison F g)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction.restrictionFMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CohomologyRestriction.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CohomologyRestriction.lean#L144). The attribute's comment: “the f-map on the small crystalline site, for presheaves”.

> **Stacks Project, Tag 07IP.**  The `f`-map from the restriction of a presheaf on `Cris(X/S)` to
> the ambient scheme of the target of a morphism `f` of `Cris(X/S)` to its restriction to the ambient
> scheme of the source: over an open `W` of the target it is the presheaf applied to the restriction
> of `f` over `W`.

```lean
def restrictionFMap {A B : CrystallineThickening S} (g : A ⟶ B) :
    restriction F B ⟶ g.hom.targetHom.hom.base _* restriction F A
```

## Tag 07IQ, an equation

[Tag 07IQ](https://stacks.math.columbia.edu/tag/07IQ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.Thickening.moduleComparisonSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean#L194). The attribute's comment: “the comparison map for modules on the big crystalline site, for sheaves”.

> **Stacks Project, Tag 07IQ.**  The comparison map `c_f : f^* F_{T'} ⟶ F_T` of a morphism
> `f : (U, T, δ) ⟶ (U', T', δ')` of `CRIS(X/S)` and a sheaf of `𝒪_{X/S}`-modules `F`, a map of
> sheaves of `𝒪_T`-modules obtained from the `f`-map `F_{T'} ⟶ f_* F_T` by the adjunction between
> pullback and pushforward of *sheaves* of modules.  The pullback is the sheafification of the
> pullback of presheaves of modules, so this map is in general not the comparison map
> `Crystalline.GlobalCrystallineSituation.Thickening.moduleComparison` of the underlying presheaves
> of modules.

```lean
noncomputable def moduleComparisonSheaf (g : A ⟶ B) :
    (SheafOfModules.pullback.{u} (ringRestrictionSheafFMap g)).obj
        (moduleRestrictionSheaf M B) ⟶ moduleRestrictionSheaf M A
```

**`Crystalline.GlobalCrystallineSituation.Thickening.isIso_moduleComparisonSheaf_of_isCartesian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean#L275). The attribute's comment: “the comparison map for sheaves of modules is an isomorphism for an open immersion”.

> **Stacks Project, Tag 07IQ.**  The comparison map of sheaves of modules of a Cartesian open
> immersion of `CRIS(X/S)` is an isomorphism: the restriction `F_T` is then the restriction of
> `F_{T'}` to the open `T` of `T'` already at the level of presheaves of modules.

```lean
theorem isIso_moduleComparisonSheaf_of_isCartesian (g : A ⟶ B)
    [IsOpenImmersion g.targetHom.hom] (hg : IsCartesian g) :
    IsIso (moduleComparisonSheaf M g)
```

**`Crystalline.GlobalCrystallineSituation.Thickening.moduleComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean, line 921](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean#L921). The attribute's comment: “the comparison map for modules on the big crystalline site, for presheaves”.

> **Stacks Project, Tag 07IQ.**  The comparison morphism `c_f : f^* M_{T'} ⟶ M_T` of a morphism
> `f : (U, T, δ) ⟶ (U', T', δ')` of `CRIS(X/S)` and a presheaf of `𝒪_{X/S}`-modules `M`, a map of
> `𝒪_T`-modules obtained from the `f`-map `M_{T'} ⟶ f_* M_T` by the adjunction between pullback and
> pushforward of presheaves of modules along the `f`-map of the structure sheaf.

```lean
def moduleComparison (M : PresheafOfModules.{u} (crisRing S)) {A B : Thickening S} (g : A ⟶ B) :
    (PresheafOfModules.pullback (F := Opens.map g.targetHom.hom.base)
        (restrictionFMap (crisRing S) g)).obj (moduleRestriction M B) ⟶ moduleRestriction M A
```

**`Crystalline.GlobalCrystallineSituation.Thickening.isIso_moduleComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean, line 1070](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SheafComparison.lean#L1070). The attribute's comment: “the comparison map for modules is an isomorphism for an open immersion”.

> **The comparison morphism of an open immersion of `CRIS(X/S)` for presheaves of modules is an
> isomorphism.**  For a Cartesian morphism `f : (U, T, δ) ⟶ (U', T', δ')` which is an open immersion
> on ambient schemes, the restriction `M_T` is the restriction of `M_{T'}` to the open `T` of `T'`,
> so the comparison morphism `c_f : f^* M_{T'} ⟶ M_T` is invertible.

```lean
theorem isIso_moduleComparison (M : PresheafOfModules.{u} (crisRing S)) (g : A ⟶ B)
    [IsOpenImmersion g.targetHom.hom] (hg : IsCartesian g) : IsIso (moduleComparison M g)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction.moduleComparisonSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SheafCrystal.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SheafCrystal.lean#L189). The attribute's comment: “the comparison map for modules on the small crystalline site, for sheaves”.

> **Stacks Project, Tag 07IQ.**  The comparison map `c_f : f^* F_{T'} ⟶ F_T` of a morphism
> `f : (U, T, δ) ⟶ (U', T', δ')` of `Cris(X/S)` and a sheaf of `𝒪_{X/S}`-modules `F` on
> `Cris(X/S)`, a map of sheaves of `𝒪_T`-modules obtained from the `f`-map `F_{T'} ⟶ f_* F_T` by the
> adjunction between pullback and pushforward of *sheaves* of modules.  The pullback is the
> sheafification of the pullback of presheaves of modules, so this map is in general not the
> comparison map
> `Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction.moduleComparison` of the
> underlying presheaves of modules.

```lean
def moduleComparisonSheaf (g : A ⟶ B) :
    (SheafOfModules.pullback.{u} (Thickening.ringRestrictionSheafFMap g.hom)).obj
        (moduleRestrictionSheaf M B) ⟶ moduleRestrictionSheaf M A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.10, Tag 07IN](https://stacks.math.columbia.edu/tag/07IN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
