---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChain, AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChain, AlgebraicGeometry.Space.isTriangulatedEquivalence_quasicoherentDerivedAffineEtaleChain, AlgebraicGeometry.Stack.representableQuasiCoherentDerivedEquivalence
statement: formalized
proof: formalized
---

# 75.30 Quasi-coherent objects in the derived category

Section 75.30 of the Stacks Project, [Tag 0H05](https://stacks.math.columbia.edu/tag/0H05). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H06, a lemma

[Tag 0H06](https://stacks.math.columbia.edu/tag/0H06) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentDerivedAffineEtaleChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChain.lean#L570). The attribute's comment: “the chain of equivalences (1) ≃ (2) ≃ (3) ≃ (4)”.

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
> (`AlgebraicGeometry.Space.affineEtaleChartChaoticQuasicoherentQCEquivalence`).  The tag is
> registered here, for the equivalences, and in
> `StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean`, for
> the triangulated structure of the four categories and the exactness of the three equivalences;
> the three component equivalences above are not registered separately.

```lean
noncomputable def quasicoherentDerivedAffineEtaleChain :
    (QuasicoherentDerivedCategory.{u, max (u + 1) w} B S hS F hF ≌
        affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF) ×
      (affineEtaleChartQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
        affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF) ×
      (affineEtaleChartChaoticQuasicoherentDerivedCategory.{u, w} B S hS F hF ≌
        QC.{w} (affineEtaleBaseChangeData.{u, w} B S hS F hF))
```

**`AlgebraicGeometry.Space.isTriangulated_quasicoherentDerivedAffineEtaleChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L384). The attribute's comment: “the four categories (1) D\_QCoh(O\_X), (2) D\_QCoh(X\_affine\_etale, O\_X), (3) D\_QCoh(X\_affine, O\_X) and (4) QC(X\_affine, O\_X) are full triangulated subcategories of the derived categories they sit in, which is the triangulated structure the tag speaks of”.

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

**`AlgebraicGeometry.Space.isTriangulatedEquivalence_quasicoherentDerivedAffineEtaleChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentDerivedChainTriangulated.lean#L703). The attribute's comment: “each of the three equivalences (1) D\_QCoh(O\_X) ≃ (2) D\_QCoh(X\_affine\_etale, O\_X), (2) ≃ (3) D\_QCoh(X\_affine, O\_X) and (3) ≃ (4) QC(X\_affine, O\_X) is an exact equivalence of triangulated categories: functor and inverse both commute with the translation [1], compatibly on unit and counit, and both preserve distinguished triangles”.

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

## Tag 0H07, a remark

[Tag 0H07](https://stacks.math.columbia.edu/tag/0H07) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.representableQuasiCoherentDerivedEquivalence`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/Equivalence.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/BigAffineSiteTag.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RepresentableQC/BigAffineSiteTag.lean#L21) (StacksFrontier): “the equivalence QC((Aff/X), 𝒪) ≌ D\_QCoh(𝒪\_X), on the proof of Stacks 0H0K”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.30, Tag 0H05](https://stacks.math.columbia.edu/tag/0H05)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
