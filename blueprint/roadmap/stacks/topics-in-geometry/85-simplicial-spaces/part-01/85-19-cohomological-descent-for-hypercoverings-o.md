---
declaration: section
origin: cited
lean: Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianSheaf_qcAugmentation, Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianAbSheaf_qcAugmentation, CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage_over, CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage_over, CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage_over, CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_over, CategoryTheory.SimplicialSemiRepresentable.isIso_unit_over, CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_over
statement: formalized
proof: formalized
---

# 85.19 Cohomological descent for hypercoverings of an object

Section 85.19 of the Stacks Project, [Tag 0D8J](https://stacks.math.columbia.edu/tag/0D8J). 4 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D8K, a lemma

[Tag 0D8K](https://stacks.math.columbia.edu/tag/0D8K) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianSheaf_qcAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L338). The attribute's comment: “part (1) for a hypercovering augmentation of the quasi-compact site LC\_qc”.

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

**`Stacks.Topology.LocallyQuasiCompactQcSite.mem_essImage_iff_isCartesianAbSheaf_qcAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LocallyQuasiCompact/QcSmallModel.lean#L357). The attribute's comment: “part (2) for a hypercovering augmentation of the quasi-compact site LC\_qc”.

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

**`CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L222). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is faithful”.

> **Stacks 0D8K (1), the faithfulness half.** For a hypercovering `K` of `X` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/K)_total)` of the augmentation is faithful.
>
> The inverse image is restriction along `j_total`, which is continuous and cover dense, and
> restriction along such a functor is faithful by Stacks 04D9.

```lean
theorem faithful_inverseImage_over (hK : IsHypercovering P K) :
    (totalLocalizationMorphism (P.toGrothendieck.over X) K).inverseImage.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_totalInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L230). The attribute's comment: “part (1): a^\{-1} of Stacks 0D70 on sheaves of sets is faithful”.

> **Stacks 0D8K (1), the faithfulness half**, for the inverse image of the morphism of topoi
> which Stacks 0D70 attaches to the augmentation. By Stacks 0D8B that functor is isomorphic to
> restriction along `j_total`, and faithfulness is invariant under isomorphism of functors.

```lean
theorem faithful_totalInverseImage_over (hK : IsHypercovering P K) :
    Functor.Faithful
      (augmentation (P.toGrothendieck.over X) K).totalMorphismOfTopoi.inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L243). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is faithful”.

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

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L259). The attribute's comment: “part (1): a^\{-1} on sheaves of sets is full”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L277). The attribute's comment: “part (1): the unit E = a\_*a⁻¹E on sheaves of sets is an isomorphism”.

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

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L288). The attribute's comment: “part (2): a^\{-1} on abelian sheaves is full”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L300). The attribute's comment: “part (2): the unit M = a\_*a⁻¹M on abelian sheaves is an isomorphism”.

> **Stacks 0D8K (2), the degree-zero identification `M = a_* a^{-1} M`** on sheaves of abelian
> groups: for a hypercovering `K` of `X` and every sheaf of abelian groups `M` on `C/X` the
> canonical map `M ⟶ a_* a^{-1} M` is an isomorphism, `a^{-1}` being restriction along
> `j_total`.

```lean
theorem isIso_abelianUnit_over (hK : IsHypercovering P K) :
    IsIso (abelianTotalAdjunction (P.toGrothendieck.over X) K).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianSheaf_of_mem_essImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L314). The attribute's comment: “part (1): the essential image of a^\{-1} consists of cartesian sheaves of sets”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianAbSheaf_of_mem_essImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDescent.lean#L328). The attribute's comment: “part (2): the essential image of a^\{-1} consists of cartesian abelian sheaves”.

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

**`CategoryTheory.SimplicialSemiRepresentable.essImage_of_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L159). The attribute's comment: “part (1): every cartesian sheaf of sets on the total site is an a^\{-1}E”.

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

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_inverseImage_iff_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L176). The attribute's comment: “part (1): the essential image of a^\{-1} on sheaves of sets is exactly the cartesian sheaves of sets”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L190). The attribute's comment: “part (1): a^\{-1} a\_* F = F for cartesian F on sheaves of sets”.

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

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImage_of_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L223). The attribute's comment: “part (1): every cartesian sheaf of sets is an a^\{-1}E for the a of Stacks 0D70 at the simplicial-site situation of C/X”.

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

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImage_iff_isCartesianSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescent.lean#L241). The attribute's comment: “part (1): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation of C/X is exactly the cartesian sheaves of sets”.

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

**`CategoryTheory.SimplicialSemiRepresentable.essImage_of_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L179). The attribute's comment: “part (2): every cartesian abelian sheaf on the total site is an a^\{-1}G”.

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

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_abelianInverseImage_iff_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L196). The attribute's comment: “part (2): the essential image of a^\{-1} on abelian sheaves is exactly the cartesian abelian sheaves”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L208). The attribute's comment: “part (2): a^\{-1} a\_* F = F for cartesian F on abelian sheaves”.

> For a cartesian sheaf of abelian groups `ℱ` on the total site of a hypercovering of an
> object `X`, the counit `a⁻¹ a_* ℱ ⟶ ℱ` is an isomorphism.

```lean
theorem isIso_abelianCounit_app_over (hL : IsHypercovering P L)
    (G : Sheaf (situation (P.toGrothendieck.over X) L).totalTopology Ab.{u})
    (hG : (situation (P.toGrothendieck.over X) L).IsCartesianAbSheaf G) :
    IsIso ((abelianTotalAdjunction (P.toGrothendieck.over X) L).counit.app G)
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_situationTotalInverseImageAb_of_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L221). The attribute's comment: “part (2): every cartesian abelian sheaf is an a^\{-1}G for the a of Stacks 0D70 at the simplicial-site situation of C/X”.

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

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_situationTotalInverseImageAb_iff_isCartesianAbSheaf_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringSituationDescentAb.lean#L237). The attribute's comment: “part (2): the essential image of the a^\{-1} of Stacks 0D70 at the simplicial-site situation of C/X is exactly the cartesian abelian sheaves”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_situationTotalAdjunctionUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L383). The attribute's comment: “part (1): the unit E = a\_*a⁻¹E of the morphism of topoi of Stacks 0D70 on sheaves of sets is an isomorphism”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_situationAbelianTotalAdjunctionUnit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringUnit.lean#L400). The attribute's comment: “part (2): the unit M = a\_*a⁻¹M of the morphism of topoi of Stacks 0D70 on abelian sheaves is an isomorphism”.

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

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitOver_app_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforwardUnconditional.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforwardUnconditional.lean#L205). The attribute's comment: “for a hypercovering K of X by semi-representable objects, with the Ra\_*-acyclicity of a⁻¹ of a K-injective complex taken as an explicit input; the degree-zero identification M = a\_*a⁻¹M is discharged here from the hypercovering conditions, being Tag 0D8K part (2). The acyclicity is discharged, and this tag carried unconditionally, by ...SimplicialSemiRepresentable .isIso\_derivedAugmentationUnitOver\_app\_of\_isHypercovering\_unconditional”.

> **Stacks Project, Tag 0D8L**, granted the one input this library does not have. For a site
> `C` with fibre products, an object `X` of `C` and a hypercovering `K` of `X` by semi-representable
> objects, the canonical map `E ⟶ Ra_* a^{-1} E` is an isomorphism for every object `E` of the
> unbounded derived category of abelian sheaves on `C/X`.
>
> `E` is arbitrary: no boundedness is assumed and the coefficients are all abelian sheaves.
>
> Of the two inputs carried by `isIso_derivedAugmentationUnitOver_app`, the first is discharged
> here from the hypercovering conditions on `K` alone, by
> `isIso_homotopyAugmentationUnitOver_of_isHypercovering`; that theorem states the same
> invertibility for an arbitrary `K` and so has to carry it. What remains is `hacyclic`, that the
> direct image of `a^{-1}` of a K-injective complex needs no derivation, that is, that
> `R^p a_* a^{-1}` vanishes in positive degrees; the source reads that off the spectral sequence of
> Stacks 0D7A, which this library builds but without the convergence to `R^{p+q} a_*` that the
> reading needs. It is asked only at the K-injective complexes, which is where the source's
> argument supplies it. No unconditional invertibility is claimed.

```lean
theorem isIso_derivedAugmentationUnitOver_app_of_isHypercovering (hK : IsHypercovering P K)
    (hacyclic : ∀ I : CochainComplex (AbelianSheavesOver P.toGrothendieck X) ℤ,
      I.IsKInjective →
        IsIso ((derivedAbelianTotalPushforwardOverUnit P.toGrothendieck X K).app
          (((abelianTotalInverseImageOver P.toGrothendieck X K).mapHomotopyCategory
            (ComplexShape.up ℤ)).obj
              ((HomotopyCategory.quotient (AbelianSheavesOver P.toGrothendieck X)
                (ComplexShape.up ℤ)).obj I))))
    (E : DerivedCategory (AbelianSheavesOver P.toGrothendieck X)) :
    IsIso ((derivedAugmentationUnitOver P.toGrothendieck X K).app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitOver_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforward.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforward.lean#L370). The attribute's comment: “granted two inputs this library does not have: the degree-zero identification M = a\_*a⁻¹M, which is the unproved clause of Tag 0D8K, and the vanishing of R^p a\_* a⁻¹ in positive degrees; the isomorphism is not proved unconditionally”.

> **Stacks Project, Tag 0D8L**, granted its two inputs. For a simplicial semi-representable
> object `K` over an object `X` of a site with fibre products, the canonical map
> `E ⟶ Ra_* a^{-1} E` is an isomorphism for every `E` of `D(C/X)` — as soon as, at every complex
> of abelian sheaves on `C/X`, the ordinary augmentation unit is invertible and the direct image
> of its inverse image needs no derivation.
>
> These are the two steps of the source's argument for cohomological descent, and this reduces
> that argument to them. Neither is discharged in this library, so both are carried as
> hypotheses and the invertibility is not proved unconditionally.

```lean
theorem isIso_derivedAugmentationUnitOver_app
    (hunit : ∀ M, IsIso ((homotopyAugmentationUnitOver J X K).app M))
    (hacyclic : ∀ M, IsIso ((derivedAbelianTotalPushforwardOverUnit J X K).app
      (((abelianTotalInverseImageOver J X K).mapHomotopyCategory
        (ComplexShape.up ℤ)).obj M)))
    (E : DerivedCategory (AbelianSheavesOver J X)) :
    IsIso ((derivedAugmentationUnitOver J X K).app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitOver_app_of_isHypercovering_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean#L140).

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

**`CategoryTheory.SimplicialSemiRepresentable.derivedGlobalSectionsInverseImageIsoOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean#L159). The attribute's comment: “RESTRICTED: granted the two inputs of Tag 0D8L — the underived unit F = a\_*a⁻¹F and the Ra\_*-acyclicity of a⁻¹ of a K-injective complex — and the underived identity Γ(C/X, a\_*F) = Γ(total, F); stated for every simplicial semi-representable object over X, hence for a hypercovering of X”.

> **Stacks 09X7**, granted the inputs the library does not have. For a site `C` with fibre
> products, an object `X` of `C`, a simplicial semi-representable object `K` over `X` — in
> particular a hypercovering of `X` — and the augmentation `a : Sh((C/K)_total) ⟶ Sh(C/X)` of
> Stacks 0D8B read over the slice site, derived global sections over `X` are derived global
> sections on the total site of the inverse image:
>
> `RΓ(X, E) = RΓ((C/K)_total, a⁻¹E)`.
>
> The statement is an isomorphism of functors on the *unbounded* derived category of abelian
> sheaves on `C/X`, so it holds at every object `E` of `D(C/X)` with no boundedness assumption,
> which is the form the source states.
>
> Three hypotheses are carried. `hunit` and `hacyclic` are the two inputs of Stacks 0D8L, the
> statement over `C/X` of what Stacks 0D8G states over `C`: the first is the degree-zero
> identification of Stacks 0D8K, that the underived unit `F ⟶ a_*a⁻¹F` is an isomorphism, and the
> second is that `a⁻¹` of a K-injective complex computes `Ra_*`. `hΓ` is the underived identity
> `Γ(C/X, a_*F) = Γ((C/K)_total, F)` on which the factorisation of Stacks 08J6 rests. The derived
> content of Stacks 08J6 is *not* assumed: see the module docstring.

```lean
def derivedGlobalSectionsInverseImageIsoOver
    (hunit : IsIso (Augmentation.abelianTotalAdjunction (situationOver P K) (Cat.of (Over X))
      (P.toGrothendieck.over X) (augmentationOver P K)).unit)
    (hacyclic : Augmentation.InverseImageComputesDerivedPushforward (situationOver P K)
      (Cat.of (Over X)) (P.toGrothendieck.over X) (augmentationOver P K))
    (hΓ : Augmentation.abelianTotalPushforward (situationOver P K) (Cat.of (Over X))
          (P.toGrothendieck.over X) (augmentationOver P K) ⋙
        Sheaf.Γ (P.toGrothendieck.over X) AddCommGrpCat.{u} ≅
      Sheaf.Γ (situationOver P K).totalTopology AddCommGrpCat.{u}) :
    Augmentation.derivedGlobalSectionsBase (Cat.of (Over X)) (P.toGrothendieck.over X) ≅
      Augmentation.derivedTotalInverseImage (situationOver P K) (Cat.of (Over X))
          (P.toGrothendieck.over X) (augmentationOver P K) ⋙
        Augmentation.derivedGlobalSectionsTotal (situationOver P K)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedGlobalSectionsInverseImageIsoOverOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L88).

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

**`CategoryTheory.SimplicialSemiRepresentable.derivedCategoryBPlus_derivedTotalInverseImageOver_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectDerivedBoundedBelowFunctors.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectDerivedBoundedBelowFunctors.lean#L188). The attribute's comment: “the first half of the well-definedness clause only: a⁻¹ sends D⁺(C/X) into D⁺\_𝒜((C/K)\_total); the equivalence itself is not proved”.

> **Stacks Project, Tag 0D8M, the first half of the well-definedness clause.** For a site `C`
> with fibre products, an object `X` of `C`, a simplicial semi-representable object `K` over `X` —
> in particular a hypercovering of `X` — and the augmentation `a : Sh((C/K)_total) ⟶ Sh(C/X)` of
> Stacks 0D8B read over the slice site, the derived inverse image sends `D⁺(C/X)` into
> `D⁺_𝒜((C/K)_total)`: it preserves boundedness below, and its cohomology sheaves are cartesian by
> `isCartesianAbSheaf_homology_derivedTotalInverseImageOver_obj`.
>
> This is the clause of Stacks 0D8M which says that the functor whose invertibility the source
> asserts is defined at all. The invertibility is not proved here.

```lean
theorem derivedCategoryBPlus_derivedTotalInverseImageOver_obj
    (E : DerivedCategory (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u}))
    (hE : DerivedCategoryB.IsBoundedBelow E) :
    derivedPlusCartesianOver P K
      ((Augmentation.derivedTotalInverseImage (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)).obj E)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedCategoryBPlus_derivedTotalPushforwardOver_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectDerivedBoundedBelowFunctors.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectDerivedBoundedBelowFunctors.lean#L205). The attribute's comment: “the second half of the well-definedness clause only: Ra\_* sends D⁺\_𝒜((C/K)\_total) into D⁺(C/X); the equivalence itself is not proved”.

> **Stacks Project, Tag 0D8M, the second half of the well-definedness clause.** In the same
> situation the derived direct image sends `D⁺_𝒜((C/K)_total)` into `D⁺(C/X)`. Only boundedness
> below is at stake, the weak Serre subcategory on `C/X` being all of `Ab(C/X)`.
>
> This is the clause of Stacks 0D8M which says that the quasi-inverse the source names is defined
> at all. That it *is* a quasi-inverse is not proved here.

```lean
theorem derivedCategoryBPlus_derivedTotalPushforwardOver_obj
    (E : DerivedCategory (Sheaf (situationOver P K).totalTopology AddCommGrpCat.{u}))
    (hE : DerivedCategoryB.IsBoundedBelow E) :
    derivedPlusBaseOver P X
      ((Augmentation.derivedTotalPushforward (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)).obj E)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean#L223). The attribute's comment: “RESTRICTED: granted the two inputs of Tag 0D8L — the underived unit F = a\_*a⁻¹F and the Ra\_*-acyclicity of a⁻¹ of a K-injective complex — and the essential surjectivity clause of Tag 0D8K (2); stated for every simplicial semi-representable object over X, hence for a hypercovering of X”.

> **Stacks 0D8M**, granted the inputs the library does not have. For a site `C` with fibre
> products, an object `X` of `C`, a simplicial semi-representable object `K` over `X` — in
> particular a hypercovering of `X` — the augmentation `a` of Stacks 0D8B read over the slice site
> `C/X`, and the weak Serre subcategory `𝒜 ⊂ Ab((C/K)_total)` of cartesian abelian sheaves of
> Stacks 0D7J, the derived inverse image is an equivalence
>
> `a⁻¹ : D⁺(C/X) ⟶ D⁺_𝒜((C/K)_total)`
>
> with quasi-inverse `Ra_*`. Both functors of the equivalence are the restrictions of `a⁻¹` and of
> `Ra_*` on the nose, since the equivalence is the restricted adjunction; for the forward functor
> this is `derivedTotalInverseImageEquivalenceOver_functor`.
>
> Three hypotheses are carried. `hunit` and `hacyclic` are the two inputs of Stacks 0D8L, the
> statement over `C/X` of what Stacks 0D8G states over `C`. `hsurj` is the remaining clause of
> Stacks 0D8K (2), that every cartesian abelian sheaf on the total site lies in the essential image
> of `a⁻¹`. The derived content — that both functors restrict to the bounded below subcategories,
> that the cohomology sheaves of `a⁻¹E` are cartesian, and the propagation of the counit from `𝒜`
> to all of `D⁺_𝒜` — is *not* assumed.

```lean
def derivedTotalInverseImageEquivalenceOver :
    (DerivedCategoryB.derivedCategoryBPlus
        (⊤ : ObjectProperty
          (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u}))).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus
        ((situationOver P K).IsCartesianAbSheaf)).FullSubcategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOver_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescent.lean#L240). The attribute's comment: “RESTRICTED: the forward functor of the equivalence is a⁻¹, for the equivalence built granted the two inputs of Tag 0D8L and the essential surjectivity clause of Tag 0D8K (2)”.

> **Stacks 0D8M, the forward functor of the equivalence is `a⁻¹`:** it is the restriction of the
> derived inverse image to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOver_functor :
    (derivedTotalInverseImageEquivalenceOver P K hunit hacyclic hsurj).functor =
      Augmentation.derivedTotalInverseImagePlus (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L107).

> Let `C` be a site with fibre products, `X` an object of `C`, `K` a hypercovering of `X`, `a`
> the augmentation of the simplicial family of sites `n ↦ (C/X)/K_n`, and `𝒜 ⊂ Ab((C/K)_total)` the
> weak Serre subcategory of cartesian abelian sheaves. The derived inverse image is an equivalence
>
> `a⁻¹ : D⁺(C/X) ⟶ D⁺_𝒜((C/K)_total)`
>
> with quasi-inverse `Ra_*`.

```lean
def derivedTotalInverseImageEquivalenceOverOfHypercovering :
    (DerivedCategoryB.derivedCategoryBPlus
        (⊤ : ObjectProperty
          (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u}))).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus
        ((situationOver P K).IsCartesianAbSheaf)).FullSubcategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L122). The attribute's comment: “the forward functor of the equivalence is a⁻¹”.

> The forward functor of `derivedTotalInverseImageEquivalenceOverOfHypercovering` is the
> restriction of the derived inverse image `a⁻¹` to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceOverOfHypercovering_functor :
    (derivedTotalInverseImageEquivalenceOverOfHypercovering P K hK).functor =
      Augmentation.derivedTotalInverseImagePlus (situationOver P K) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationOver P K)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceOverOfHypercovering_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedDescentUnconditional.lean#L132). The attribute's comment: “the quasi-inverse of the equivalence is Ra\_*”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
