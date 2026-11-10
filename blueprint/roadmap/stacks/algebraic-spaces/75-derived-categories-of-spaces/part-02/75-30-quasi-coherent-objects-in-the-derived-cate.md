---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isQC_iff_hasQuasicoherentCohomology_affineEtaleChaotic, AlgebraicGeometry.Space.isQC_eq_hasQuasicoherentCohomology_affineEtaleChaotic, AlgebraicGeometry.Space.derivedCategoryB_isQuasicoherentOnSite_affineEtaleRestriction_iff, AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleEquivalence, AlgebraicGeometry.Space.isQC_iff_hasQuasicoherentCohomology_affineEtaleChartChaotic, AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence, AlgebraicGeometry.Space.affineEtaleChartQuasicoherentDerivedChaoticEquivalence, AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChartEquivalence
statement: formalized
proof: formalized
---

# 75.30 Quasi-coherent objects in the derived category

Section 75.30 of the Stacks Project, [Tag 0H05](https://stacks.math.columbia.edu/tag/0H05). 2 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H06, a lemma

[Tag 0H06](https://stacks.math.columbia.edu/tag/0H06) in the Stacks Project.

**`AlgebraicGeometry.Space.isQC_iff_hasQuasicoherentCohomology_affineEtaleChaotic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean#L179). The attribute's comment: “the equivalence of (3) D_QCoh(X_affine, O_X) and (4) QC(X_affine, O_X), as an equality of the two conditions on an object of D(O_X) of the chaotic affine etale site”.

> **Categories (3) and (4) of Stacks 0H06 agree.**  On the affine étale charts of an algebraic
> space with the chaotic topology, an object of the derived category of `𝒪_F`-modules is a
> cartesian object in the sense of Stacks 0GYU exactly when all of its cohomology sheaves are
> quasi-coherent; that is, `QC(F_{affine}, 𝒪_F) = D_QCoh(F_{affine}, 𝒪_F)`.
>
> This is Stacks 0GZR,
> `Stacks.ModulesOnACategory.QuasiCoherentCohomology.isQC_iff_hasQuasicoherentCohomology`, whose
> two hypotheses are supplied by `AlgebraicGeometry.Space.affineEtaleChaoticRingedSite_J` and
> `AlgebraicGeometry.Space.flat_affineEtaleChaoticRingedSite_O_map`.

```lean
theorem isQC_iff_hasQuasicoherentCohomology_affineEtaleChaotic
    (bc : BaseChangeData.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (affineEtaleChaoticRingedSite B S hS F hF).O).obj)
    (K : DMod.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (affineEtaleChaoticRingedSite B S hS F hF).O).obj) :
    IsQC.{w} bc K ↔
      hasQuasicoherentCohomology.{w} (affineEtaleChaoticRingedSite B S hS F hF) K
```

**`AlgebraicGeometry.Space.isQC_eq_hasQuasicoherentCohomology_affineEtaleChaotic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean#L194). The attribute's comment: “the equivalence of (3) D_QCoh(X_affine, O_X) and (4) QC(X_affine, O_X), as an equality of object properties on D(O_X) of the chaotic affine etale site”.

> **Categories (3) and (4) of Stacks 0H06 are cut out of `D(𝒪_F)` by the same object
> property.**  This is the previous result as an equality of object properties, which is the form
> that exhibits the two full subcategories as the same subcategory of `D(𝒪_F)` rather than merely
> as equivalent ones.

```lean
theorem isQC_eq_hasQuasicoherentCohomology_affineEtaleChaotic
    (bc : BaseChangeData.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (affineEtaleChaoticRingedSite B S hS F hF).O).obj) :
    (fun K ↦ IsQC.{w} bc K :
        ObjectProperty (DMod.{w}
          (Stacks.SheafOfModules.Tensor.ringSheaf (affineEtaleChaoticRingedSite B S hS F hF).O).obj)) =
      hasQuasicoherentCohomology.{w} (affineEtaleChaoticRingedSite B S hS F hF)
```

**`AlgebraicGeometry.Space.derivedCategoryB_isQuasicoherentOnSite_affineEtaleRestriction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean#L391). The attribute's comment: “the equivalence of (1) D_QCoh(O_X) and (2) D_QCoh(X_affine_etale, O_X), at the level of the object properties cutting them out, carrying as the hypothesis hrefl the converse of isQuasicoherentOnSite_affineEtaleModuleRestriction: a module on the small etale site whose restriction to the affine charts is quasi-coherent is quasi-coherent”.

> **Categories (1) and (2) of Stacks 0H06 agree**, over the single named input `hrefl`.
>
> Restriction to the affine étale charts is an equivalence of the unbounded derived categories of
> `𝒪_F`-modules (`AlgebraicGeometry.Space.affineEtaleDerivedRestrictionEquivalence`), and under it
> a complex has quasi-coherent cohomology exactly when its restriction does; so it identifies
> `D_QCoh(𝒪_F)` with `D_QCoh(F_{affine,étale}, 𝒪_F)`.
>
> One direction of the identification of quasi-coherence is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_affineEtaleModuleRestriction`, proved above; the
> other is the hypothesis `hrefl`, a statement about single modules and therefore the degree-zero
> part of the conclusion rather than the conclusion itself.  The passage from modules to complexes
> is `CategoryTheory.Functor.mapDerivedCategoryHomologyIso`, which identifies the cohomology
> sheaves of the restricted complex with the restrictions of the cohomology sheaves.

```lean
theorem derivedCategoryB_isQuasicoherentOnSite_affineEtaleRestriction_iff
    (hrefl : ∀ M : SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)),
      ((affineEtaleModuleRestriction B S hS F hF).obj M).IsQuasicoherentOnSite →
        M.IsQuasicoherentOnSite)
    (K : DerivedCategory
      (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)))) :
    DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite (affineEtaleRingRestriction B S hS F hF))
        ((affineEtaleDerivedRestrictionEquivalence B S hS F hF).functor.obj K) ↔
      DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherentOnSite
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))) K
```

**`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerived.lean#L449). The attribute's comment: “the equivalence of (1) D_QCoh(O_X) and (2) D_QCoh(X_affine_etale, O_X), as an equivalence of categories induced by derived restriction, carrying as the hypothesis hrefl the converse of isQuasicoherentOnSite_affineEtaleModuleRestriction: a module on the small etale site whose restriction to the affine charts is quasi-coherent is quasi-coherent”.

> **Categories (1) and (2) of Stacks 0H06 are equivalent**, over the single named input
> `hrefl`: restriction to the affine étale charts is an exact equivalence
>
> `D_QCoh(𝒪_F) ⟶ D_QCoh(F_{affine,étale}, 𝒪_F)`.
>
> It is the equivalence of unbounded derived categories
> `AlgebraicGeometry.Space.affineEtaleDerivedRestrictionEquivalence`, which is triangulated, cut
> down to the two full subcategories by
> `AlgebraicGeometry.Space.derivedCategoryB_isQuasicoherentOnSite_affineEtaleRestriction_iff`; so
> the comparison is the canonical one, being the restriction of the derived restriction functor,
> and not merely some equivalence.  See the module docstring for the status of `hrefl`.

```lean
noncomputable def quasicoherentDerivedAffineEtaleEquivalence
    (hrefl : ∀ M : SheafOfModules.{u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O)),
      ((affineEtaleModuleRestriction B S hS F hF).obj M).IsQuasicoherentOnSite →
        M.IsQuasicoherentOnSite) :
    QuasicoherentDerivedCategory.{u, u} B S hS F hF ≌
      affineEtaleQuasicoherentDerivedCategory B S hS F hF
```

**`AlgebraicGeometry.Space.isQC_iff_hasQuasicoherentCohomology_affineEtaleChartChaotic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L405). The attribute's comment: “the equivalence of (3) D_QCoh(X_affine, O_X) and (4) QC(X_affine, O_X), as an equality of the two conditions on an object of D(X_affine, O_X), with O_X the structure sheaf of D_QCoh(O_X) restricted to the affine charts”.

> **Categories (3) and (4) of Stacks 0H06 agree.** On the chaotic affine étale site of `F`, an
> object of the derived category of modules is cartesian in the sense of Stacks 0GYU exactly when
> all of its cohomology sheaves are quasi-coherent, for every base-change datum.
>
> This is Stacks 0GZR, `isQC_iff_hasQuasicoherentCohomology`: a morphism of affine étale charts is
> flat on the underlying affine schemes, so the restriction maps of `𝒪_F` are flat
> (`AlgebraicGeometry.Space.flat_affineEtaleChartRings_map`).

```lean
theorem isQC_iff_hasQuasicoherentCohomology_affineEtaleChartChaotic
    (bc : BaseChangeData.{w} (affineEtaleRingRestriction B S hS F hF).obj)
    (K : DMod.{w} (affineEtaleRingRestriction B S hS F hF).obj) :
    IsQC.{w} bc K ↔
      hasQuasicoherentCohomology.{w} (affineEtaleChartChaoticRingedSite B S hS F hF) K
```

**`AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L420). The attribute's comment: “the equivalence of (3) D_QCoh(X_affine, O_X) and (4) QC(X_affine, O_X)”.

> **The equivalence of categories (3) and (4) of Stacks 0H06**,
> `D_QCoh(F_{affine}, 𝒪_F) ≌ QC(F_{affine}, 𝒪_F)`: the two are the same full subcategory of
> `D(F_{affine}, 𝒪_F)`, by
> `AlgebraicGeometry.Space.isQC_iff_hasQuasicoherentCohomology_affineEtaleChartChaotic`, and the
> equivalence is the identity on objects.

```lean
noncomputable def affineEtaleChartChaoticQuasicoherentQCEquivalence :
    affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
      QC.{w} (affineEtaleBaseChangeData.{u, w} B S hS F hF)
```

**`AlgebraicGeometry.Space.affineEtaleChartQuasicoherentDerivedChaoticEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L474). The attribute's comment: “the equivalence of (2) D_QCoh(X_affine_etale, O_X) and (3) D_QCoh(X_affine, O_X), given by Rε_* for the change of topology ε from the etale to the chaotic topology”.

> **Categories (2) and (3) of Stacks 0H06 are equivalent**: for the change of topology
> `ε : (F_{affine,étale}, 𝒪_F) ⟶ (F_{affine}, 𝒪_F)` from the étale to the chaotic topology on the
> affine étale charts, `Rε_*` is an equivalence
>
> `D_QCoh(F_{affine,étale}, 𝒪_F) ≌ D_QCoh(F_{affine}, 𝒪_F)`
>
> with quasi-inverse `ε^*`.
>
> It is Stacks 0GZS for `ε` (`AlgebraicGeometry.Space.affineEtaleCartesianPushforwardEquivalence`),
> whose hypothesis is `AlgebraicGeometry.Space.isLocallyKFlatAcyclic_affineEtale`, with its source
> identified with `D_QCoh(F_{affine,étale}, 𝒪_F)`
> (`AlgebraicGeometry.Space.affineEtaleChartQuasicoherentDerivedCartesianEquivalence`) and its
> target with `D_QCoh(F_{affine}, 𝒪_F)`
> (`AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence`). That its functor
> is `Rε_*` is `affineEtaleChartQuasicoherentDerivedChaoticEquivalence_functor_comp_ι`.

```lean
noncomputable def affineEtaleChartQuasicoherentDerivedChaoticEquivalence :
    affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
      affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF
```

**`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChartEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L507). The attribute's comment: “the equivalence of (1) D_QCoh(O_X) and (2) D_QCoh(X_affine_etale, O_X), induced by restriction to the affine charts”.

> **Categories (1) and (2) of Stacks 0H06 are equivalent**: restriction to the affine étale
> charts induces an equivalence
>
> `D_QCoh(𝒪_F) ≌ D_QCoh(F_{affine,étale}, 𝒪_F)`.
>
> Restriction of sheaves of `𝒪_F`-modules to the affine charts is an equivalence of abelian
> categories (`AlgebraicGeometry.Space.affineEtaleRestrictionEquivalence`, the Comparison Lemma
> along the dense subsite inclusion of Stacks 04JS, i.e. the equivalence of ringed topoi of
> Stacks 0H03 on modules); it is exact, so it derives to an equivalence of the unbounded derived
> categories, and it preserves and reflects quasi-coherence
> (`AlgebraicGeometry.Space.isQuasicoherentOnSite_affineEtaleModulePushforward_iff`), so that
> equivalence matches the two subcategories. Its functor is the derived functor of restriction,
> `quasicoherentDerivedAffineEtaleChartEquivalence_functor_obj_obj`.

```lean
noncomputable def quasicoherentDerivedAffineEtaleChartEquivalence :
    QuasicoherentDerivedCategory.{u, max (u + 1) w} B S hS F hF ≌
      affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF
```

**`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L574). The attribute's comment: “the chain of equivalences (1) ≃ (2) ≃ (3) ≃ (4)”.

> **Stacks 0H06.** For an algebraic space `F` over `S`, the four categories
>
> 1. `D_QCoh(𝒪_F)`,
> 2. `D_QCoh(F_{affine,étale}, 𝒪_F)`,
> 3. `D_QCoh(F_{affine}, 𝒪_F)`, and
> 4. `QC(F_{affine}, 𝒪_F)`
>
> are equivalent, by the canonical equivalences `(1) ≌ (2)` induced by restriction to the affine
> charts (`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChartEquivalence`),
> `(2) ≌ (3)` given by `Rε_*` for the change of topology from the étale to the chaotic topology
> (`AlgebraicGeometry.Space.affineEtaleChartQuasicoherentDerivedChaoticEquivalence`), and
> `(3) ≌ (4)` the identity of the common full subcategory of `D(F_{affine}, 𝒪_F)`
> (`AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence`).

```lean
noncomputable def quasicoherentDerivedAffineEtaleChain :
    (QuasicoherentDerivedCategory.{u, max (u + 1) w} B S hS F hF ≌
        affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF) ×
      (affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
        affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF) ×
      (affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
        QC.{w} (affineEtaleBaseChangeData.{u, w} B S hS F hF))
```

**`AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L383). The attribute's comment: “the four categories (1) D_QCoh(O_X), (2) D_QCoh(X_affine_etale, O_X), (3) D_QCoh(X_affine, O_X) and (4) QC(X_affine, O_X) are full triangulated subcategories of the derived categories they sit in, which is the triangulated structure the tag speaks of”.

> **The four categories of Stacks 0H06 are full triangulated subcategories** of the derived
> categories they sit in: in order, `D_QCoh(𝒪_F) ⊆ D(𝒪_F)`,
> `D_QCoh(F_{affine,étale}, 𝒪_F) ⊆ D(F_{affine,étale}, 𝒪_F)`, and
> `D_QCoh(F_{affine}, 𝒪_F), QC(F_{affine}, 𝒪_F) ⊆ D(F_{affine}, 𝒪_F)`.
>
> A full triangulated subcategory is exactly what
> `CategoryTheory.ObjectProperty.IsTriangulated` says: the subcategory contains a zero object, is
> stable under the translation in both directions, and is closed under extensions in distinguished
> triangles.  From it Mathlib derives the shift and the pretriangulated structure of the
> subcategory itself, whose distinguished triangles are the triangles distinguished in the ambient
> derived category, and the triangulatedness of the inclusion.  This is the triangulated structure
> the tag's phrase *the following triangulated categories* refers to.

```lean
theorem isTriangulated_quasicoherentDerivedAffineEtaleChain :
    letI : HasDerivedCategory (Modules.{u, max (u + 1) w} B S hS F hF) :=
      HasDerivedCategory.standard _
    ObjectProperty.IsTriangulated
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, max (u + 1) w}
            (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))) ∧
      ObjectProperty.IsTriangulated
        (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u,
          max (u + 1) w} (affineEtaleRingRestriction B S hS F hF))) ∧
      ObjectProperty.IsTriangulated
        (hasQuasicoherentCohomologyAffineEtaleChart.{u, w} B S hS F hF) ∧
      ObjectProperty.IsTriangulated
        (IsQC.{w} (affineEtaleBaseChangeData.{u, w} B S hS F hF))
```

**`AlgebraicGeometry.Space.commShiftAffineEtaleChartChaoticQuasicoherentQCEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L417). The attribute's comment: “the equivalence (3) D_QCoh(X_affine, O_X) ≃ (4) QC(X_affine, O_X) commutes with the translation [1]: half of the tag's assertion that it is exact”.

> **The equivalence of categories (3) and (4) of Stacks 0H06 commutes with the translation.**
> Its functor, followed by the inclusion of `QC(F_{affine}, 𝒪_F)`, is the inclusion of
> `D_QCoh(F_{affine}, 𝒪_F)`
> (`AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence_functor_comp_ι`),
> and the inclusion of a full triangulated subcategory commutes with the translation.
>
> This is the canonical shift-compatibility of the equivalence `(3) ≌ (4)`, and it is an instance:
> the compatibility of the equivalence with the translation `[1]` is half of the tag's assertion
> that the equivalence is *exact*, so it is a registered fact about the equivalence and not a
> structure chosen inside the statement of the other half.

```lean
noncomputable instance commShiftAffineEtaleChartChaoticQuasicoherentQCEquivalence :
    (affineEtaleChartChaoticQuasicoherentQCEquivalence.{u, w} B S hS F hF).functor.CommShift ℤ
```

**`AlgebraicGeometry.Space.commShiftAffineEtaleChartQuasicoherentDerivedChaoticEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L452). The attribute's comment: “the equivalence (2) D_QCoh(X_affine_etale, O_X) ≃ (3) D_QCoh(X_affine, O_X) commutes with the translation [1]: half of the tag's assertion that it is exact”.

> **The equivalence of categories (2) and (3) of Stacks 0H06 commutes with the translation.**
> Its functor, followed by the inclusion of `D_QCoh(F_{affine}, 𝒪_F)`, is the inclusion of
> `D_QCoh(F_{affine,étale}, 𝒪_F)` followed by `Rε_*`
> (`AlgebraicGeometry.Space.affineEtaleChartQuasicoherentDerivedChaoticEquivalence_functor_comp_ι`),
> and `Rε_*` commutes with the translation
> (`Stacks.ModulesOnACategory.ChaoticComparison.derivedEpsilonPushforwardCommShift`).
>
> This is the canonical shift-compatibility of the equivalence `(2) ≌ (3)`, and it is an instance,
> for the reason given at
> `AlgebraicGeometry.Space.commShiftAffineEtaleChartChaoticQuasicoherentQCEquivalence`.

```lean
noncomputable instance commShiftAffineEtaleChartQuasicoherentDerivedChaoticEquivalence :
    (affineEtaleChartQuasicoherentDerivedChaoticEquivalence.{u, w} B S hS F
      hF).functor.CommShift ℤ
```

**`AlgebraicGeometry.Space.commShiftQuasicoherentDerivedAffineEtaleChartEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L501). The attribute's comment: “the equivalence (1) D_QCoh(O_X) ≃ (2) D_QCoh(X_affine_etale, O_X) commutes with the translation [1]: half of the tag's assertion that it is exact”.

> **The equivalence of categories (1) and (2) of Stacks 0H06 commutes with the translation.**
> Its functor, followed by the inclusion of `D_QCoh(F_{affine,étale}, 𝒪_F)`, is the inclusion of
> `D_QCoh(𝒪_F)` followed by the derived functor of restriction to the affine charts
> (`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChartEquivalence_functor_comp_ι`), and
> the derived functor of an exact functor commutes with the translation.
>
> This is the canonical shift-compatibility of the equivalence `(1) ≌ (2)`, and it is an instance,
> for the reason given at
> `AlgebraicGeometry.Space.commShiftAffineEtaleChartChaoticQuasicoherentQCEquivalence`.  The
> derived category of `𝒪_F`-modules it is read over is the standard model, introduced by the `letI`
> of the first line as everywhere in the chain; that `letI` names the *category*, not the
> shift-compatibility, and the goal it is found at carries the same one.

```lean
noncomputable instance commShiftQuasicoherentDerivedAffineEtaleChartEquivalence :
    letI : HasDerivedCategory (Modules.{u, max (u + 1) w} B S hS F hF) :=
      HasDerivedCategory.standard _
    haveI := isTriangulated_quasicoherentDerivedChart.{u, w} B S hS F hF
    (quasicoherentDerivedAffineEtaleChartEquivalence.{u, w} B S hS F hF).functor.CommShift ℤ
```

**`AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChainEquivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L616). The attribute's comment: “the three equivalences of the chain are exact: (1) D_QCoh(O_X) ≃ (2) D_QCoh(X_affine_etale, O_X), (2) ≃ (3) D_QCoh(X_affine, O_X) and (3) ≃ (4) QC(X_affine, O_X) each carry distinguished triangles to distinguished triangles, over the compatibilities with the translation [1] registered for them under this tag”.

> **The three equivalences of Stacks 0H06 are exact.**  For an algebraic space `F` over `S`, the
> canonical equivalences
>
> 1. `D_QCoh(𝒪_F) ≌ D_QCoh(F_{affine,étale}, 𝒪_F)`, induced by restriction to the affine charts,
> 2. `D_QCoh(F_{affine,étale}, 𝒪_F) ≌ D_QCoh(F_{affine}, 𝒪_F)`, given by `Rε_*` for the change
>    from the étale to the chaotic topology, and
> 3. `D_QCoh(F_{affine}, 𝒪_F) ≌ QC(F_{affine}, 𝒪_F)`, the identity of the common full subcategory
>    of `D(F_{affine}, 𝒪_F)`,
>
> are exact functors of triangulated categories: each carries distinguished triangles to
> distinguished triangles, over the shift-compatibility of the equivalence it belongs to.  That
> shift-compatibility is not chosen here: `CategoryTheory.Functor.IsTriangulated` takes the
> `CategoryTheory.Functor.CommShift` structure it is read over as an instance, and the instance
> found at each of the three functors is the one registered for it under this tag, namely
> `AlgebraicGeometry.Space.commShiftQuasicoherentDerivedAffineEtaleChartEquivalence`,
> `AlgebraicGeometry.Space.commShiftAffineEtaleChartQuasicoherentDerivedChaoticEquivalence` and
> `AlgebraicGeometry.Space.commShiftAffineEtaleChartChaoticQuasicoherentQCEquivalence`.  So both
> halves of *exact* — compatibility with the translation `[1]` and preservation of distinguished
> triangles — are registered facts about the three equivalences.
>
> Together with
> `AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChain`, which says that
> the four categories are full triangulated subcategories of the derived categories they sit in,
> and `AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChain`, which is the chain of
> equivalences itself, this is the assertion of the tag;
> `AlgebraicGeometry.Space.isTriangulatedEquivalence_quasicoherentDerivedAffineEtaleChain` states
> the same exactness in Mathlib's bundled form.

```lean
theorem isTriangulated_quasicoherentDerivedAffineEtaleChainEquivalences :
    letI : HasDerivedCategory (Modules.{u, max (u + 1) w} B S hS F hF) :=
      HasDerivedCategory.standard _
    haveI := isTriangulated_quasicoherentDerivedChart.{u, w} B S hS F hF
    (quasicoherentDerivedAffineEtaleChartEquivalence.{u, w} B S hS F hF).functor.IsTriangulated ∧
      (affineEtaleChartQuasicoherentDerivedChaoticEquivalence.{u, w} B S hS F
        hF).functor.IsTriangulated ∧
      (affineEtaleChartChaoticQuasicoherentQCEquivalence.{u, w} B S hS F
        hF).functor.IsTriangulated
```

**`AlgebraicGeometry.Space.isTriangulatedEquivalence_quasicoherentDerivedAffineEtaleChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L709). The attribute's comment: “each of the three equivalences (1) D_QCoh(O_X) ≃ (2) D_QCoh(X_affine_etale, O_X), (2) ≃ (3) D_QCoh(X_affine, O_X) and (3) ≃ (4) QC(X_affine, O_X) is an exact equivalence of triangulated categories: functor and inverse both commute with the translation [1], compatibly on unit and counit, and both preserve distinguished triangles”.

> **The three equivalences of Stacks 0H06 are exact equivalences of triangulated categories**,
> in Mathlib's bundled form: for an algebraic space `F` over `S`, each of
>
> 1. `D_QCoh(𝒪_F) ≌ D_QCoh(F_{affine,étale}, 𝒪_F)`,
> 2. `D_QCoh(F_{affine,étale}, 𝒪_F) ≌ D_QCoh(F_{affine}, 𝒪_F)`, and
> 3. `D_QCoh(F_{affine}, 𝒪_F) ≌ QC(F_{affine}, 𝒪_F)`
>
> is a `CategoryTheory.Equivalence.IsTriangulated`: its functor and its inverse both commute with
> the translation `[1]`, those two compatibilities agree on the unit and the counit, and both
> carry distinguished triangles to distinguished triangles.  This is the tag's phrase *canonical
> exact equivalences between the following triangulated categories* with nothing left implicit:
> the triangulated structure of the four categories is
> `AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChain`, the equivalences
> are `AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChain`, and exactness is this.

```lean
theorem isTriangulatedEquivalence_quasicoherentDerivedAffineEtaleChain :
    letI : HasDerivedCategory (Modules.{u, max (u + 1) w} B S hS F hF) :=
      HasDerivedCategory.standard _
    haveI := isTriangulated_quasicoherentDerivedChart.{u, w} B S hS F hF
    (quasicoherentDerivedAffineEtaleChartEquivalence.{u, w} B S hS F hF).IsTriangulated ∧
      (affineEtaleChartQuasicoherentDerivedChaoticEquivalence.{u, w} B S hS F hF).IsTriangulated ∧
      (affineEtaleChartChaoticQuasicoherentQCEquivalence.{u, w} B S hS F hF).IsTriangulated
```

**`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleRestrictionEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentReflection.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentReflection.lean#L175). The attribute's comment: “the equivalence of (1) D_QCoh(O_X) and (2) D_QCoh(X_affine_etale, O_X), induced by derived restriction, for module sections in the universe of the schemes”.

> **Categories (1) and (2) of Stacks 0H06 are equivalent, at the universe of the schemes**:
> restriction to the affine étale charts is an exact equivalence
>
> `D_QCoh(𝒪_F) ⟶ D_QCoh(F_{affine,étale}, 𝒪_F)`
>
> for module sections in the universe of the schemes. It is
> `AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleEquivalence` with its hypothesis
> discharged by the reflection of quasi-coherence under restriction to the affine charts,
> `isQuasicoherentOnSite_of_isQuasicoherentOnSite_affineEtaleModuleRestriction`, so it is the
> restriction of the derived restriction functor
> `AlgebraicGeometry.Space.affineEtaleDerivedRestrictionEquivalence`.

```lean
noncomputable def quasicoherentDerivedAffineEtaleRestrictionEquivalence :
    QuasicoherentDerivedCategory.{u, u} B S hS F hF ≌
      affineEtaleQuasicoherentDerivedCategory B S hS F hF
```

## Tag 0H07, a remark

[Tag 0H07](https://stacks.math.columbia.edu/tag/0H07) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.representableQuasiCoherentDerivedEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/Equivalence.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/BigAffineSiteTag.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/BigAffineSiteTag.lean#L21) (StacksFrontier): “the equivalence QC((Aff/X), 𝒪) ≌ D_QCoh(𝒪_X), on the proof of Stacks 0H0K”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.30, Tag 0H05](https://stacks.math.columbia.edu/tag/0H05)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
