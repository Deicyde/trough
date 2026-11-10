---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallAffineChaoticDerivedQuasiCoherentEquivQC, AlgebraicGeometry.smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι, AlgebraicGeometry.smallAffineChaotic_qcohCohomologyProperty_isTriangulated, AlgebraicGeometry.smallAffineChaotic_qcohCohomologyProperty_isTriangulated_univ, AlgebraicGeometry.Scheme.nonempty_quasicoherentDerived_linearTriangulatedEquivalences, AlgebraicGeometry.Stack.affineBigSiteQuasiCoherentDerivedEquivalence
statement: formalized
proof: formalized
---

# 36.41 Quasi-coherent objects in the derived category

Section 36.41 of the Stacks Project, [Tag 0GZY](https://stacks.math.columbia.edu/tag/0GZY). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GZZ, a lemma

[Tag 0GZZ](https://stacks.math.columbia.edu/tag/0GZZ) in the Stacks Project.

**`AlgebraicGeometry.smallAffineChaoticDerivedQuasiCoherentEquivQC`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean#L238). The attribute's comment: “the equivalence (4) ≃ (5)”.

> **Stacks 0GZZ, the equivalence of (4) and (5).** For a scheme `S`, the derived category of
> modules on the small affine site `S_affine` with quasi-coherent cohomology sheaves is
> canonically equivalent to the category `QC(S_affine, 𝒪)` of quasi-coherent objects of the
> derived category.
>
> The equivalence is realized inside `D(S_affine, 𝒪)`, by
> `smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι`; the two subcategories are in
> fact equal, by `smallAffineChaotic_isQC_eq_hasQuasicoherentCohomology`.
>
> For a scheme in `Scheme.{0}` both sides are triangulated subcategories of `D(S_affine, 𝒪)`, by
> `smallAffineChaotic_qcohCohomologyProperty_isTriangulated`, so the comparison is then an exact
> equivalence of triangulated categories. None of the other four comparisons of Stacks 0GZZ is
> proved; see the coverage note of this file.

```lean
def smallAffineChaoticDerivedQuasiCoherentEquivQC
    (bc : BaseChangeData.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineChaoticRingedSite B S hS).O).obj) :
    (qcohCohomologyProperty.{w} (smallAffineChaoticRingedSite B S hS)).FullSubcategory ≌
      QC.{w} bc
```

**`AlgebraicGeometry.smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean#L262). The attribute's comment: “the equivalence (4) ≃ (5) is the canonical one”.

> **Stacks 0GZZ, the equivalence of (4) and (5), as a commuting triangle.** The comparison
> `D_QCoh(S_affine, 𝒪) ≌ QC(S_affine, 𝒪)` is the canonical one: it commutes with the inclusions
> of both sides into `D(S_affine, 𝒪)`.

```lean
def smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι
    (bc : BaseChangeData.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallAffineChaoticRingedSite B S hS).O).obj) :
    (smallAffineChaoticDerivedQuasiCoherentEquivQC.{w} B S hS bc).functor ⋙ QCι.{w} bc ≅
      (qcohCohomologyProperty.{w} (smallAffineChaoticRingedSite B S hS)).ι
```

**`AlgebraicGeometry.smallAffineChaotic_qcohCohomologyProperty_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjects.lean#L319). The attribute's comment: “(4) and (5) are triangulated, for a scheme in `Scheme.{0}`”.

> **Stacks 0GZZ, triangulatedness of (4) and (5).** For a scheme in `Scheme.{0}`,
> `D_QCoh(S_affine, 𝒪)` is a triangulated subcategory of `D(S_affine, 𝒪)`: it is the same
> subcategory as `QC(S_affine, 𝒪)`, which is triangulated by Stacks 0GYW.
>
> Together with `smallAffineChaoticDerivedQuasiCoherentEquivQC` and
> `smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι` this makes the comparison of (4)
> and (5) an exact equivalence of triangulated categories, both sides being triangulated
> subcategories of `D(S_affine, 𝒪)` and the comparison commuting with the two inclusions.
>
> The restriction to `Scheme.{0}` comes from the input: the library constructs derived base
> change only over a structure sheaf with values in `RingCat.{0}`; see
> `smallAffineChaoticBaseChangeData`.

```lean
theorem smallAffineChaotic_qcohCohomologyProperty_isTriangulated :
    ObjectProperty.IsTriangulated
      (qcohCohomologyProperty.{0} (smallAffineChaoticRingedSite B₀ S₀ hS₀))
```

**`AlgebraicGeometry.smallAffineChaotic_qcohCohomologyProperty_isTriangulated_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjectsSupplement.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteQuasiCoherentObjectsSupplement.lean#L82). The attribute's comment: “(4) and (5) are triangulated”.

> **Stacks 0GZZ, triangulatedness of (4) and (5).** For an arbitrary scheme `S`,
> `D_QCoh(S_affine, 𝒪)` is a triangulated subcategory of `D(S_affine, 𝒪)`: it is the same
> subcategory as `QC(S_affine, 𝒪)`, which is triangulated by Stacks 0GYW.
>
> Together with `smallAffineChaoticDerivedQuasiCoherentEquivQC` and
> `smallAffineChaoticDerivedQuasiCoherentEquivQC_functor_comp_ι` this makes the comparison of (4)
> and (5) an exact equivalence of triangulated categories, both sides being triangulated
> subcategories of `D(S_affine, 𝒪)` and the comparison commuting with the two inclusions.

```lean
theorem smallAffineChaotic_qcohCohomologyProperty_isTriangulated_univ :
    ObjectProperty.IsTriangulated
      (qcohCohomologyProperty.{w} (smallAffineChaoticRingedSite B S hS))
```

**`AlgebraicGeometry.Scheme.nonempty_quasicoherentDerived_linearTriangulatedEquivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/QuasiCoherentObjectsExactEquivalences.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/QuasiCoherentObjectsExactEquivalences.lean#L597).

> **Stacks 0GZZ.** Let `X` be a scheme, and let `Sch_Zar` be a big Zariski site containing it.
> There are canonical exact equivalences between the following triangulated categories:
>
> 1. `D_QCoh(𝒪_X)`, the complexes of `𝒪_X`-modules on the ringed space `(X, 𝒪_X)` with
>    quasi-coherent cohomology sheaves;
> 2. `D_QCoh(X_Zar, 𝒪)`, the same on the small Zariski site `X_Zar` of Topologies, Definition 020T
>    (the open immersions `U → X` of `Sch_Zar`), with its structure sheaf `U ↦ Γ(U, 𝒪_U)` and
>    quasi-coherence in the sense of Modules on Sites, Definition 03DL;
> 3. `D_QCoh(X_{affine, Zar}, 𝒪)`, the same on the category of affine opens of `X` with the
>    Zariski topology;
> 4. `D_QCoh(X_affine, 𝒪)`, the same on the category of affine opens of `X` with the chaotic
>    topology, where modules are presheaves of modules;
> 5. `QC(X_affine, 𝒪)`, the full subcategory of `D(X_affine, 𝒪)` of Cohomology on Sites,
>    Definition 0GYV: the objects `K` for which `RΓ(V, K) ⊗^L_{𝒪(V)} 𝒪(U) ⟶ RΓ(U, K)` is an
>    isomorphism for all `U ⟶ V`, formed with the derived base change of
>    `AlgebraicGeometry.affineChaoticBaseChangeData`.
>
> Formally: the five subcategories are triangulated subcategories of their ambient derived
> categories, and there are equivalences of triangulated categories (an equivalence whose functor
> commutes with the shifts and preserves distinguished triangles)
> `(2) ≌ (1)`, `(1) ≌ (3)`, `(4) ≌ (3)` and `(4) ≌ (5)`, which are the canonical ones: each lies,
> through the inclusions of the subcategories, over the canonical functor of the source, namely
> derived restriction along the identification of modules of Descent, Remark 03FG; derived
> restriction to the affine opens; the identification of presheaves with sheaves for the chaotic
> topology followed by `Lε^*` for the morphism of ringed sites
> `ε : (X_{affine, Zar}, 𝒪) ⟶ (X_affine, 𝒪)` of Cohomology on Sites, Lemma 07A8; and the identity
> of `D(X_affine, 𝒪)`.
>
> The derived categories of sheaves of modules are taken at the standard model
> `HasDerivedCategory.standard`, the one the change of topology of Stacks 07A8 is constructed at;
> those of presheaves of modules at the model of
> `Stacks.ModulesOnACategory.QuasiCoherentEquivalence.DMod`.

```lean
theorem Scheme.nonempty_quasicoherentDerived_linearTriangulatedEquivalences :
    letI := SmallZariski.abelianModules B X hX
    letI := SmallZariski.derivedCategoryModel B X hX
    haveI := Scheme.isWeakSerreClass_isQuasicoherent_ringCatSheaf X
    haveI := SmallZariski.isWeakSerreClass_isQuasicoherentOnSite B X hX
    haveI := SmallZariski.additive_restrictModuleEquivalence B X hX
    -- the five subcategories are triangulated
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).IsTriangulated ∧
    (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (SmallZariski.structureSheaf B X hX))).IsTriangulated ∧
    (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u, u, u, u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.affineZariskiRingedSite.O))).IsTriangulated ∧
    (qcohCohomologyProperty.{u} X.affineChaoticRingedSite).IsTriangulated ∧
    (isQCProperty.{u} (affineChaoticBaseChangeData.{u} X)).IsTriangulated ∧
    -- `(2) ≃ (1)`, over derived restriction along Descent, Remark 03FG
    (∃ e : LinearTriangulatedEquivalence ℤ
        (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (SmallZariski.structureSheaf B X hX))).FullSubcategory
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory,
      Nonempty (e.equivalence.functor ⋙
          (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ≅
        (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (SmallZariski.structureSheaf B X hX))).ι ⋙
          (SmallZariski.restrictModuleEquivalence B X hX).functor.mapDerivedCategory)) ∧
    -- `(1) ≃ (3)`, over derived restriction to the affine opens
    (∃ e : LinearTriangulatedEquivalence ℤ
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory
        X.affineOpensQuasicoherentDerivedCategory,
      Nonempty (e.equivalence.functor ⋙
          (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.affineZariskiRingedSite.O))).ι ≅
        (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙
          X.affineOpensModuleRestrictionEquivalence.functor.mapDerivedCategory)) ∧
    -- `(4) ≃ (3)`, over sheafification for the chaotic topology followed by `Lε^*`
    (∃ e : LinearTriangulatedEquivalence ℤ
        (qcohCohomologyProperty.{u} X.affineChaoticRingedSite).FullSubcategory
        X.affineOpensQuasicoherentDerivedCategory,
      Nonempty (e.equivalence.functor ⋙
          (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite.{u, u, u, u}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.affineZariskiRingedSite.O))).ι ≅
        (qcohCohomologyProperty.{u} X.affineChaoticRingedSite).ι ⋙
          X.affineChaoticSheafPresheafEquivalence.inverse.mapDerivedCategory ⋙
            X.affineCoarseningDerivedPullback)) ∧
    -- `(4) ≃ (5)`, over the identity of `D(X_affine, 𝒪)`
    (∃ e : LinearTriangulatedEquivalence ℤ
        (qcohCohomologyProperty.{u} X.affineChaoticRingedSite).FullSubcategory
        (QC.{u} (affineChaoticBaseChangeData.{u} X)),
      Nonempty (e.equivalence.functor ⋙ QCι.{u} (affineChaoticBaseChangeData.{u} X) ≅
        (qcohCohomologyProperty.{u} X.affineChaoticRingedSite).ι))
```

## Tag 0H00, a remark

[Tag 0H00](https://stacks.math.columbia.edu/tag/0H00) in the Stacks Project.

**`AlgebraicGeometry.Stack.affineBigSiteQuasiCoherentDerivedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SchemeQC/AffineBigSiteEquivalence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/SchemeQC/AffineBigSiteEquivalence.lean#L92).

> **Stacks 0H00.** Let `S` be a scheme in a big fppf site `B`. Then `QC((Aff/S), O)` — the
> triangulated category of quasi-coherent objects (Stacks 0GYV) of the derived category of
> `O`-modules on the category `(Aff/S)` of affine schemes over `S` with the chaotic topology and
> its sheaf of rings of global functions, that is `QC((Sch/S)_{fppf})` of Stacks 0H0H for the
> identity of `(Sch/S)_{fppf}` — is canonically equivalent to `D_QCoh(O_S)`, the full subcategory
> of the derived category of `O_S`-modules (in any model) of the objects with quasi-coherent
> cohomology sheaves; the modules have their sections in `max (u + 1) t`.
>
> The equivalence is the composite of the three equivalences of the proof of Stacks 0H0K, for the
> Zariski topology: `ε^*` from `QC((Aff/S), O)` onto the objects `K` of `D((Aff/S)_{Zar}↑)` with
> `Rε_*K` cartesian (Stacks 0H0J, 0GZS); the direct image along the morphism of ringed sites given
> by the affine opens of `S`, inverse to the derived pullback on the 0GZS subcategories (the
> argument of Stacks 09J1); and the identification of the 0GZS subcategory of the lifted small
> affine Zariski site of `S` with `D_QCoh(O_S)` (Descent 03FG, Stacks 0F1B, 0H04).

```lean
def affineBigSiteQuasiCoherentDerivedEquivalence
    [HasDerivedCategory (SheafOfModules.{max (u + 1) t} S.ringCatSheaf)] :
    quasiCoherentDerived.{u, u + 1, u, t} B S hS (𝟭 (BigFppfOver B S hS)) ≌
      (DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherentOnSite S.ringCatSheaf :
        ObjectProperty (SheafOfModules.{max (u + 1) t} S.ringCatSheaf))).FullSubcategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.41, Tag 0GZY](https://stacks.math.columbia.edu/tag/0GZY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
