---
declaration: section
origin: cited
lean: Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianSheaf_qcAugmentation, Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianAbSheaf_qcAugmentation, CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage_over, CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage_over, CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage_over, CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_over, CategoryTheory.SimplicialSemiRepresentable.isIso_unit_over, CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_over
statement: formalized
proof: formalized
---

# 85.19 Cohomological descent for hypercoverings of an object

Section 85.19 of the Stacks Project, [Tag 0D8J](https://stacks.math.columbia.edu/tag/0D8J). 4 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D8K, a lemma

[Tag 0D8K](https://stacks.math.columbia.edu/tag/0D8K) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianSheaf_qcAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L338). The attribute's comment: “part (1) for a hypercovering augmentation of the quasi-compact site LC\_qc”.

> **Stacks 0D8K (1) for a hypercovering augmentation of `LC_qc`.** Let `a : U ⟶ Y` be a
> hypercovering augmentation of an object `Y` of the quasi-compact site, in the sense of
> Stacks 09X8. Then on the total site of the associated simplicial semi-representable object,
> carried to the small model, the sheaves of sets which are inverse images along the augmentation
> are exactly the cartesian ones.
>
> This is the statement the smallness reconciliation buys. Its hypothesis is a datum on `LC_qc`,
> which is where Stacks 0DAF's diagram lives; its conclusion is about the total site of the small
> model, which is where the apparatus of Stacks 09WE exists at all; and
> `smallSheafEquiv` identifies the base topos of the two.

```lean
theorem mem_essImage_iff_isCartesianSheaf_qcAugmentation {Y : S.category}
    (U : SimplicialObject S.category)
    (a : U ⟶ (SimplicialObject.const S.category).obj Y)
    (h : IsHypercoveringAugmentation S.pretopology U a)
    (E : Sheaf (situation (S.smallOverTopology Y)
      (S.smallAssociatedSimplicialObject U a)).totalTopology (Type u)) :
    (totalLocalizationMorphism (S.smallOverTopology Y)
        (S.smallAssociatedSimplicialObject U a)).inverseImage.essImage E ↔
      (situation (S.smallOverTopology Y)
        (S.smallAssociatedSimplicialObject U a)).IsCartesianSheaf E
```

**`Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianAbSheaf_qcAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L357). The attribute's comment: “part (2) for a hypercovering augmentation of the quasi-compact site LC\_qc”.

> **Stacks 0D8K (2) for a hypercovering augmentation of `LC_qc`.** The same for sheaves of
> abelian groups: on the total site of the associated simplicial semi-representable object carried
> to the small model, the abelian sheaves which are inverse images along the augmentation are
> exactly the cartesian ones.

```lean
theorem mem_essImage_iff_isCartesianAbSheaf_qcAugmentation {Y : S.category}
    (U : SimplicialObject S.category)
    (a : U ⟶ (SimplicialObject.const S.category).obj Y)
    (h : IsHypercoveringAugmentation S.pretopology U a)
    (G : Sheaf (situation (S.smallOverTopology Y)
      (S.smallAssociatedSimplicialObject U a)).totalTopology Ab.{u}) :
    ((totalForget (S.smallAssociatedSimplicialObject U a)).sheafPushforwardContinuous Ab.{u}
        ((situation (S.smallOverTopology Y)
          (S.smallAssociatedSimplicialObject U a)).totalTopology)
        (S.smallOverTopology Y)).essImage G ↔
      (situation (S.smallOverTopology Y)
        (S.smallAssociatedSimplicialObject U a)).IsCartesianAbSheaf G
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L222). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is faithful”.

> **Stacks 0D8K (1), the faithfulness half.** For a hypercovering `K` of `X` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/K)_total)` of the augmentation is faithful.
>
> The inverse image is restriction along `j_total`, which is continuous and cover dense, and
> restriction along such a functor is faithful by Stacks 04D9.

```lean
theorem faithful_inverseImage_over (hK : IsHypercovering P K) :
    (totalLocalizationMorphism (P.toGrothendieck.over X) K).inverseImage.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L230). The attribute's comment: “part (1): a^\{-1} of Stacks 0D70 on sheaves of sets is faithful”.

> **Stacks 0D8K (1), the faithfulness half**, for the inverse image of the morphism of topoi
> which Stacks 0D70 attaches to the augmentation. By Stacks 0D8B that functor is isomorphic to
> restriction along `j_total`, and faithfulness is invariant under isomorphism of functors.

```lean
theorem faithful_totalInverseImage_over (hK : IsHypercovering P K) :
    Functor.Faithful
      (augmentation (P.toGrothendieck.over X) K).totalMorphismOfTopoi.inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L243). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is faithful”.

> **Stacks 0D8K (2), the faithfulness half.** For a hypercovering `K` of `X` the inverse image
> `a^{-1} : Ab(C/X) ⥤ Ab((C/K)_total)` of the augmentation — restriction along `j_total` on abelian
> sheaves, as in Stacks 09WM (2) — is faithful.
>
> Cover density of `j_total` is a statement about the site, so the argument of
> `faithful_inverseImage_over` applies at any coefficient category.

```lean
theorem faithful_abelianInverseImage_over (hK : IsHypercovering P K) :
    ((totalForget K).sheafPushforwardContinuous Ab.{u}
      ((situation (P.toGrothendieck.over X) K).totalTopology)
      (P.toGrothendieck.over X)).Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L259). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is full”.

> **Stacks 0D8K (1), the fullness half.** For a hypercovering `K` of `X` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/K)_total)` of the augmentation is full.
>
> The inverse image is restriction along `j_total`, which is continuous, cover dense by the
> degree-zero clause of Stacks 01G5 and locally full by
> `CategoryTheory.SimplicialSemiRepresentable.isLocallyFull_totalForget_over`; restriction along
> such a functor is full.

```lean
theorem full_inverseImage_over (hK : IsHypercovering P K) :
    (totalLocalizationMorphism (P.toGrothendieck.over X) K).inverseImage.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L277). The attribute's comment: “part (1): the unit E = a\_*a⁻¹E on sheaves of sets is an isomorphism”.

> **Stacks 0D8K (1), the degree-zero identification `E = a_* a^{-1} E`.** For a hypercovering
> `K` of `X` and every sheaf of sets `E` on `C/X` the canonical map `E ⟶ a_* a^{-1} E` is an
> isomorphism, `a^{-1}` being restriction along `j_total`.
>
> The unit of an adjunction with fully faithful left adjoint is invertible, and `a^{-1}` is fully
> faithful by `fullyFaithfulInverseImageOver`.

```lean
theorem isIso_unit_over (hK : IsHypercovering P K) :
    IsIso (totalLocalizationMorphism (P.toGrothendieck.over X) K).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L288). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is full”.

> **Stacks 0D8K (2), the fullness half.** The inverse image
> `a^{-1} : Ab(C/X) ⥤ Ab((C/K)_total)` of the augmentation is full.
>
> Cover density and local fullness of `j_total` are statements about the site, so the argument of
> `full_inverseImage_over` applies at any coefficient category.

```lean
theorem full_abelianInverseImage_over (hK : IsHypercovering P K) :
    ((totalForget K).sheafPushforwardContinuous Ab.{u}
      ((situation (P.toGrothendieck.over X) K).totalTopology)
      (P.toGrothendieck.over X)).Full
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L300). The attribute's comment: “part (2): the unit M = a\_*a⁻¹M on abelian sheaves is an isomorphism”.

> **Stacks 0D8K (2), the degree-zero identification `M = a_* a^{-1} M`** on sheaves of abelian
> groups: for a hypercovering `K` of `X` and every sheaf of abelian groups `M` on `C/X` the
> canonical map `M ⟶ a_* a^{-1} M` is an isomorphism, `a^{-1}` being restriction along
> `j_total`.

```lean
theorem isIso_abelianUnit_over (hK : IsHypercovering P K) :
    IsIso (abelianTotalAdjunction (P.toGrothendieck.over X) K).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianSheaf_of_mem_essImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L314). The attribute's comment: “part (1): the essential image of a^\{-1} consists of cartesian sheaves of sets”.

> **Stacks 0D8K (1), the inclusion of the essential image in the cartesian sheaves.** Every
> sheaf of sets on the total site `(C/K)_total` isomorphic to an inverse image along the
> augmentation towards `C/X` is cartesian.
>
> This is Stacks 0D7H (1) together with invariance of cartesianness under isomorphism, and uses no
> condition on the simplicial semi-representable object `K`.

```lean
theorem isCartesianSheaf_of_mem_essImage_over (J : GrothendieckTopology C)
    {F : Sheaf (situation (J.over X) K).totalTopology (Type u)}
    (hF : (totalLocalizationMorphism (J.over X) K).inverseImage.essImage F) :
    (situation (J.over X) K).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianAbSheaf_of_mem_essImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L328). The attribute's comment: “part (2): the essential image of a^\{-1} consists of cartesian abelian sheaves”.

> **Stacks 0D8K (2), the inclusion of the essential image in the cartesian sheaves.** Every
> sheaf of abelian groups on the total site `(C/K)_total` isomorphic to an inverse image along the
> augmentation towards `C/X` is cartesian.
>
> Cartesianness of an abelian sheaf is cartesianness of its underlying sheaf of sets, and the
> underlying sheaf of the restriction of `𝒢` along `j_total` is the restriction of the underlying
> sheaf of `𝒢`, both being a composition of functors.

```lean
theorem isCartesianAbSheaf_of_mem_essImage_over (J : GrothendieckTopology C)
    {F : Sheaf (situation (J.over X) K).totalTopology Ab.{u}}
    (hF : ((totalForget K).sheafPushforwardContinuous Ab.{u}
      ((situation (J.over X) K).totalTopology) (J.over X)).essImage F) :
    (situation (J.over X) K).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_of_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L159). The attribute's comment: “part (1): every cartesian sheaf of sets on the total site is an a^\{-1}E”.

> **Stacks 0D8K (1), essential surjectivity onto the cartesian sheaves of sets**, for
> restriction along the localization functor `j_total` of a hypercovering `K` of an object `X`:
> every cartesian sheaf of sets on the total site is isomorphic to a restriction of a sheaf on
> `C/X`.
>
> A hypercovering of `X` in `C` is a hypercovering of the final presheaf of the localized site
> `C/X` with the same simplicial object, by
> `Stacks.CategoryTheory.Hypercovering.exists_hypercoveringOfTerminal_over_of_isHypercovering`, and
> hence has the same total site, total topology and localization morphism; so this is Stacks
> 0D8E (1) read over `C/X`. The hypercovering that identification produces is one for the
> pretopology of covering families of `C/X`, which generates the localized topology
> `P.toGrothendieck.over X` itself by the Galois insertion between pretopologies and topologies;
> the sheaf is quantified inside the statement because its category depends on that topology.

```lean
theorem essImage_of_isCartesianSheaf_over (hK : IsHypercovering P K) :
    ∀ E : Sheaf (situation (P.toGrothendieck.over X) K).totalTopology (Type u),
      (situation (P.toGrothendieck.over X) K).IsCartesianSheaf E →
        (totalLocalizationMorphism (P.toGrothendieck.over X) K).inverseImage.essImage E
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_inverseImage_iff_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L176). The attribute's comment: “part (1): the essential image of a^\{-1} on sheaves of sets is exactly the cartesian sheaves of sets”.

> **Stacks 0D8K (1), the essential image is exactly the cartesian sheaves of sets**, for
> restriction along `j_total` for a hypercovering of an object `X`. One inclusion is
> `isCartesianSheaf_of_mem_essImage_over`, which is Stacks 0D7H (1) and uses no condition on `K`;
> the other is `essImage_of_isCartesianSheaf_over`.

```lean
theorem mem_essImage_inverseImage_iff_isCartesianSheaf_over (hK : IsHypercovering P K)
    (E : Sheaf (situation (P.toGrothendieck.over X) K).totalTopology (Type u)) :
    (totalLocalizationMorphism (P.toGrothendieck.over X) K).inverseImage.essImage E ↔
      (situation (P.toGrothendieck.over X) K).IsCartesianSheaf E
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L190). The attribute's comment: “part (1): a^\{-1} a\_* F = F for cartesian F on sheaves of sets”.

> **Stacks 0D8K (1), `a_*` is a quasi-inverse on the cartesian sheaves of sets.** For a
> cartesian sheaf of sets `F` on the total site of a hypercovering of an object `X` the counit
> `a⁻¹ a_* F ⟶ F` is an isomorphism.
>
> `a⁻¹` is fully faithful, so its counit is invertible at exactly the objects of its essential
> image, and `essImage_of_isCartesianSheaf_over` puts `F` there.

```lean
theorem isIso_counit_app_over (hK : IsHypercovering P K)
    (E : Sheaf (situation (P.toGrothendieck.over X) K).totalTopology (Type u))
    (hE : (situation (P.toGrothendieck.over X) K).IsCartesianSheaf E) :
    IsIso ((totalLocalizationMorphism (P.toGrothendieck.over X) K).adj.counit.app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImage_of_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L223). The attribute's comment: “part (1): every cartesian sheaf of sets is an a^\{-1}E for the a of Stacks 0D70 at the simplicial-site situation of C/X”.

> **Stacks 0D8K (1), essential surjectivity onto the cartesian sheaves of sets**, for the
> inverse image of the total augmentation as Stacks 0D70 constructs it from the simplicial-site
> situation of `C/X`.
>
> By Stacks 0D8B that inverse image is restriction along `j_total`, for which every cartesian
> sheaf of sets is an inverse image by `essImage_of_isCartesianSheaf_over`; the essential image is
> invariant under isomorphism of functors.

```lean
theorem essImage_situationTotalInverseImage_of_isCartesianSheaf_over (hK : IsHypercovering P K)
    (E : Sheaf (situation (P.toGrothendieck.over X) K).totalTopology (Type u))
    (hE : (situation (P.toGrothendieck.over X) K).IsCartesianSheaf E) :
    (Augmentation.totalMorphismOfTopoi
      (situation (P.toGrothendieck.over X) K) (Cat.of (Over X)) (P.toGrothendieck.over X)
      (situationAugmentation (P.toGrothendieck.over X) K)).inverseImage.essImage E
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImage_iff_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L241). The attribute's comment: “part (1): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation of C/X is exactly the cartesian sheaves of sets”.

> **Stacks 0D8K (1), the essential image is exactly the cartesian sheaves of sets**, for the
> inverse image of the morphism of topoi of Stacks 0D70 at the simplicial-site situation of `C/X`.
> One inclusion is `mem_essImage_inverseImage_iff_isCartesianSheaf_over` carried across
> Stacks 0D8B, the other is `essImage_situationTotalInverseImage_of_isCartesianSheaf_over`.

```lean
theorem mem_essImage_situationTotalInverseImage_iff_isCartesianSheaf_over
    (hK : IsHypercovering P K)
    (E : Sheaf (situation (P.toGrothendieck.over X) K).totalTopology (Type u)) :
    (Augmentation.totalMorphismOfTopoi
        (situation (P.toGrothendieck.over X) K) (Cat.of (Over X)) (P.toGrothendieck.over X)
        (situationAugmentation (P.toGrothendieck.over X) K)).inverseImage.essImage E ↔
      (situation (P.toGrothendieck.over X) K).IsCartesianSheaf E
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_of_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L179). The attribute's comment: “part (2): every cartesian abelian sheaf on the total site is an a^\{-1}G”.

> For a hypercovering `L` of an object `X`, every cartesian sheaf of abelian groups on the
> total site is isomorphic to the restriction along the localization functor `j_total` of a sheaf of
> abelian groups on `C/X`.

```lean
theorem essImage_of_isCartesianAbSheaf_over (hL : IsHypercovering P L) :
    ∀ G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u},
      (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G →
        ((totalForget L).sheafPushforwardContinuous Ab.{u}
          ((situation (P.toGrothendieck.over X) L).totalTopology)
          (P.toGrothendieck.over X)).essImage G
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_abelianInverseImage_iff_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L196). The attribute's comment: “part (2): the essential image of a^\{-1} on abelian sheaves is exactly the cartesian abelian sheaves”.

> For a hypercovering `L` of an object `X`, the essential image of restriction of abelian
> sheaves along `j_total` is exactly the cartesian abelian sheaves.

```lean
theorem mem_essImage_abelianInverseImage_iff_isCartesianAbSheaf_over (hL : IsHypercovering P L)
    (G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u}) :
    ((totalForget L).sheafPushforwardContinuous Ab.{u}
        ((situation (P.toGrothendieck.over X) L).totalTopology)
        (P.toGrothendieck.over X)).essImage G ↔
      (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L208). The attribute's comment: “part (2): a^\{-1} a\_* F = F for cartesian F on abelian sheaves”.

> For a cartesian sheaf of abelian groups `ℱ` on the total site of a hypercovering of an
> object `X`, the counit `a⁻¹ a_* ℱ ⟶ ℱ` is an isomorphism.

```lean
theorem isIso_abelianCounit_app_over (hL : IsHypercovering P L)
    (G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u})
    (hG : (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G) :
    IsIso ((abelianTotalAdjunction (P.toGrothendieck.over X) L).counit.app G)
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L221). The attribute's comment: “part (2): every cartesian abelian sheaf is an a^\{-1}G for the a of Stacks 0D70 at the simplicial-site situation of C/X”.

> For a hypercovering `L` of an object `X`, every cartesian abelian sheaf on the total site
> lies in the essential image of the abelian inverse image of the total augmentation which
> Stacks 0D70 constructs from the simplicial-site situation of `C/X`.

```lean
theorem essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf_over
    (hL : IsHypercovering P L)
    (G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u})
    (hG : (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G) :
    (Augmentation.totalInverseImageAb (situation (P.toGrothendieck.over X) L)
      (Cat.of (Over X)) (P.toGrothendieck.over X)
      (situationAugmentation (P.toGrothendieck.over X) L)).essImage G
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImageAb_iff_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L237). The attribute's comment: “part (2): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation of C/X is exactly the cartesian abelian sheaves”.

> For a hypercovering `L` of an object `X`, the essential image of the abelian inverse image of
> the morphism of topoi of Stacks 0D70 at the simplicial-site situation of `C/X` is exactly the
> cartesian abelian sheaves.

```lean
theorem mem_essImage_situationTotalInverseImageAb_iff_isCartesianAbSheaf_over
    (hL : IsHypercovering P L)
    (G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u}) :
    (Augmentation.totalInverseImageAb (situation (P.toGrothendieck.over X) L)
        (Cat.of (Over X)) (P.toGrothendieck.over X)
        (situationAugmentation (P.toGrothendieck.over X) L)).essImage G ↔
      (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_situationTotalAdjunctionUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L383). The attribute's comment: “part (1): the unit E = a\_*a⁻¹E of the morphism of topoi of Stacks 0D70 on sheaves of sets is an isomorphism”.

> **Stacks 0D8K (1), the degree-zero identification `E = a_* a^{-1} E`**, for the morphism of
> topoi which Stacks 0D70 attaches to the *simplicial-site situation* of a hypercovering `K` of an
> object `X`: for every sheaf of sets `E` on `C/X` the canonical map `E ⟶ a_* a^{-1} E` is an
> isomorphism, with no condition carried beyond `K` being a hypercovering of `X`.
>
> This is the comparison `isIso_situationTotalAdjunctionUnit_of_isIso_unit` at the site `C/X`,
> applied to `isIso_unit_over`.

```lean
theorem isIso_situationTotalAdjunctionUnit_over (hK : IsHypercovering P K) :
    IsIso (SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi
      (situation (P.toGrothendieck.over X) K) (Cat.of (Over X)) (P.toGrothendieck.over X)
      (situationAugmentation (P.toGrothendieck.over X) K)).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_situationAbelianTotalAdjunctionUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L400). The attribute's comment: “part (2): the unit M = a\_*a⁻¹M of the morphism of topoi of Stacks 0D70 on abelian sheaves is an isomorphism”.

> **Stacks 0D8K (2), the degree-zero identification `M = a_* a^{-1} M`** on sheaves of abelian
> groups, for the morphism of topoi which Stacks 0D70 attaches to the *simplicial-site situation*
> of a hypercovering `K` of an object `X`: for every sheaf of abelian groups `M` on `C/X` the
> canonical map `M ⟶ a_* a^{-1} M` is an isomorphism, with no condition carried beyond `K` being a
> hypercovering of `X`.
>
> This is the spelling of the unit which the derived statements of Stacks 0D8L consume, and it
> discharges the clause those statements would otherwise carry as a hypothesis.

```lean
theorem isIso_situationAbelianTotalAdjunctionUnit_over (hK : IsHypercovering P K) :
    IsIso (SimplicialSiteSituation.Augmentation.abelianTotalAdjunction
      (situation (P.toGrothendieck.over X) K) (Cat.of (Over X)) (P.toGrothendieck.over X)
      (situationAugmentation (P.toGrothendieck.over X) K)).unit
```

## Tag 0D8L, a lemma

[Tag 0D8L](https://stacks.math.columbia.edu/tag/0D8L) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitOver_app_of_isHypercovering_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean#L142). The attribute's comment: “for a hypercovering K of X, the map E → Ra\_*a⁻¹E is an isomorphism for every E in D(C/X)”.

> For a hypercovering `K` of an object `X` of a site `C` with fibre products, the canonical map
> `E ⟶ Ra_* a⁻¹ E` is invertible at every object `E` of the unbounded derived category of abelian
> sheaves on `C/X`.

```lean
theorem isIso_derivedAugmentationUnitOver_app_of_isHypercovering_unconditional
    (P : Pretopology C) {X : C} (K : SimplicialObject (FormalCoproduct.{u} (Over X)))
    (hK : IsHypercovering P K)
    (E : DerivedCategory (AbelianSheavesOver P.toGrothendieck X)) :
    IsIso ((derivedAugmentationUnitOver P.toGrothendieck X K).app E)
```

## Tag 09X7, a lemma

[Tag 09X7](https://stacks.math.columbia.edu/tag/09X7) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedGlobalSectionsInverseImageIsoOverOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L88). The attribute's comment: “RΓ(X, E) ≅ RΓ((C/K)\_total, a⁻¹E) for E ∈ D(C/X), K a hypercovering of X”.

> Let `C` be a site with fibre products, `X` an object of `C`, `K` a hypercovering of `X` and
> `a : Sh((C/K)_total) ⟶ Sh(C/X)` the augmentation of the simplicial family of sites
> `n ↦ (C/X)/K_n`. Derived global sections over `X` are derived global sections on the total site of
> the inverse image:
>
> `RΓ(X, E) = RΓ((C/K)_total, a⁻¹E)`,
>
> as an isomorphism of functors on the unbounded derived category of abelian sheaves on `C/X`.

```lean
def derivedGlobalSectionsInverseImageIsoOverOfHypercovering :
    Augmentation.derivedGlobalSectionsBase (Cat.of (Over X)) (P.toGrothendieck.over X) ≅
      Augmentation.derivedTotalInverseImage (situationOver P K) (Cat.of (Over X))
          (P.toGrothendieck.over X) (augmentationOver P K) ⋙
        Augmentation.derivedGlobalSectionsTotal (situationOver P K)
```

## Tag 0D8M, a lemma

[Tag 0D8M](https://stacks.math.columbia.edu/tag/0D8M) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L111).

> Let `C` be a site with fibre products, `X` an object of `C`, `K` a hypercovering of `X`, `a`
> the augmentation of the simplicial family of sites `n ↦ (C/X)/K_n`, and `𝒜 ⊂ Ab((C/K)_total)` the
> weak Serre subcategory of cartesian abelian sheaves. The derived inverse image is an equivalence
>
> `a⁻¹ : D⁺(C/X) ⟶ D⁺_𝒜((C/K)_total)`
>
> with quasi-inverse `Ra_*`. The hypercovering condition enters through the two inputs of
> Stacks 0D8L (`isIso_situationAbelianTotalAdjunctionUnit_over`,
> `inverseImageComputesDerivedPushforward_over_of_isHypercovering`) and the essential surjectivity
> clause of Stacks 0D8K (2) (`essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf_over`),
> all proved from `hK`.

```lean
def derivedTotalInverseImageEquivalenceOverOfHypercovering :
    (DerivedCategoryB.derivedCategoryBPlus
        (⊤ : ObjectProperty
          (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u}))).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus
        ((situationOver P K).IsCartesianAbSheaf)).FullSubcategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L126). The attribute's comment: “the forward functor of the equivalence is a⁻¹”.

> The forward functor of `derivedTotalInverseImageEquivalenceOverOfHypercovering` is the
> restriction of the derived inverse image `a⁻¹` to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOverOfHypercovering_functor :
    (derivedTotalInverseImageEquivalenceOverOfHypercovering P K hK).functor =
      Augmentation.derivedTotalInverseImagePlus (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L136). The attribute's comment: “the quasi-inverse of the equivalence is Ra\_*”.

> The quasi-inverse of `derivedTotalInverseImageEquivalenceOverOfHypercovering` is the
> restriction of the derived direct image `Ra_*` to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOverOfHypercovering_inverse :
    (derivedTotalInverseImageEquivalenceOverOfHypercovering P K hK).inverse =
      Augmentation.derivedTotalPushforwardPlus (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.19, Tag 0D8J](https://stacks.math.columbia.edu/tag/0D8J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
