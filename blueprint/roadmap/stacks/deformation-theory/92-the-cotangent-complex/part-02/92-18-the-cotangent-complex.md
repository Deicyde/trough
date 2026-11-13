---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.standardResolution, CategoryTheory.Sheaf.cotangentSimplicialModule, CategoryTheory.Sheaf.cotangentComplex, CategoryTheory.Sheaf.cotangentComplexDerived, CategoryTheory.Sheaf.cotangentComplex_isZero_pos, CategoryTheory.Sheaf.cotangentComplex_d, CategoryTheory.Sheaf.inverseImageCotangentComplexIso, CategoryTheory.Sheaf.sectionwiseCotangentCohomology
statement: formalized
proof: formalized
---

# 92.18 The cotangent complex

Section 92.18 of the Stacks Project, [Tag 08UQ](https://stacks.math.columbia.edu/tag/08UQ). 10 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08SR, a definition

[Tag 08SR](https://stacks.math.columbia.edu/tag/08SR) in the Stacks Project.

**`CategoryTheory.Sheaf.standardResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/StandardResolution.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/StandardResolution.lean#L193).

> **Stacks 08SR.** The standard resolution of a morphism `A ⟶ B` of sheaves of commutative
> rings is the augmentation obtained by evaluating the free-forgetful standard resolution at the
> `A`-algebra `B`.

```lean
noncomputable def standardResolution {A B : Sheaf J CommRingCat.{max u v w}} (f : A ⟶ B) :
    SimplicialObject.Augmented (Under A)
```

## Tag 08SS, a definition

[Tag 08SS](https://stacks.math.columbia.edu/tag/08SS) in the Stacks Project.

**`CategoryTheory.Sheaf.cotangentSimplicialModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean#L329). The attribute's comment: “the simplicial module”.

> **Stacks 08SS.** The canonical simplicial sheaf of `B`-modules `Ω_{P_•/A} ⊗_{P_•} B` of the
> standard resolution.

```lean
noncomputable def cotangentSimplicialModule : CotangentSimplicialModuleData J f
```

**`CategoryTheory.Sheaf.cotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean#L334). The attribute's comment: “the associated complex”.

> **Stacks 08SS.** The cotangent complex of a morphism of sheaves of commutative rings.

```lean
noncomputable def cotangentComplex : CochainComplex (targetModules J B) ℤ
```

**`CategoryTheory.Sheaf.cotangentComplexDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean#L340). The attribute's comment: “the derived object”.

> **Stacks 08SS.** The cotangent complex regarded as an object of the derived category.

```lean
noncomputable abbrev cotangentComplexDerived [HasDerivedCategory.{t} (targetModules J B)] :
    DerivedCategory (targetModules J B)
```

**`CategoryTheory.Sheaf.cotangentComplex_isZero_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean#L356). The attribute's comment: “the positive-degree terms”.

> **Stacks 08SS.** The cotangent complex is zero in positive cohomological degrees.

```lean
theorem cotangentComplex_isZero_pos (m : ℤ) (hm : 0 < m) :
    IsZero ((cotangentComplex J f).X m)
```

**`CategoryTheory.Sheaf.cotangentComplex_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/CotangentComplex.lean#L366). The attribute's comment: “the differential”.

> **Stacks 08SS.** The differential is the alternating sum of the face maps, transported
> through the canonical degree isomorphisms.

```lean
theorem cotangentComplex_d (n : ℕ) :
    (cotangentComplex J f).d (-((n + 1 : ℕ) : ℤ)) (-(n : ℤ)) =
      (cotangentComplex_degreeIso J f (n + 1)).hom ≫
        AlgebraicTopology.AlternatingFaceMapComplex.objD
          (cotangentSimplicialModule J f).object n ≫
      (cotangentComplex_degreeIso J f n).inv
```

## Tag 08SV, a lemma

[Tag 08SV](https://stacks.math.columbia.edu/tag/08SV) in the Stacks Project.

**`CategoryTheory.Sheaf.inverseImageCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/InverseImageCotangentComplex.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/InverseImageCotangentComplex.lean#L746). The attribute's comment: “for an arbitrary morphism of topoi, with the object, arrow and section universes of the two sites independent”.

> **Stacks 08SV.** The inverse image of the cotangent complex of a homomorphism of sheaves of
> commutative rings along a morphism of topoi is the cotangent complex of its inverse image:
> `f⁻¹L_{B/A} = L_{f⁻¹B/f⁻¹A}`.

```lean
noncomputable def inverseImageCotangentComplexIso :
    ((inverseImageTargetModules.{u, v, w, u', v', w'} J K f).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj (cotangentComplex.{u', v', w'} K a) ≅
      cotangentComplex.{u, v, w} J (f.inverseImageRing.map a)
```

## Tag 08SW, a lemma

[Tag 08SW](https://stacks.math.columbia.edu/tag/08SW) in the Stacks Project.

**`CategoryTheory.Sheaf.sectionwiseCotangentCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionwiseCotangentComplex.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionwiseCotangentComplex.lean#L274). The attribute's comment: “the presheaf U ↦ H^i(L\_\{B(U)/A(U)}); not its sheafification”.

> **The sectionwise cotangent cohomology presheaf** `U ↦ H^i(L_{B(U)/A(U)})`: the cotangent
> cohomology groups of the ring maps on sections, with the maps induced by the restriction
> squares as restriction maps.

```lean
noncomputable def sectionwiseCotangentCohomology (i : ℤ) : Cᵒᵖ ⥤ AddCommGrpCat.{max u v w}
```

**`CategoryTheory.Sheaf.cohomologySheafification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionwiseCotangentComplexIso.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionwiseCotangentComplexIso.lean#L380). The attribute's comment: “the whole lemma: the sheaf associated to the presheaf U ↦ H^i(L\_\{B(U)/A(U)}) is H^i(L\_\{B/A}), by the canonical identification — `sectionwiseComplexIso`, which `sectionwiseComplexIso_hom_unit` shows is induced by the comparison maps L\_\{B(U)/A(U)} ⟶ L\_\{B/A}(U) of Remark 08SX. CARRIES NOTHING beyond the ambient variables: arbitrary site, arbitrary Grothendieck topology, arbitrary homomorphism of sheaves of commutative rings, every i, with the section universe a free parameter. The module-level form, before the structure over B is forgotten, is `cohomologySheafIso`”.

> For a homomorphism `A ⟶ B` of sheaves of commutative rings on a site, the cohomology sheaf
> `H^i(L_{B/A})` of the cotangent complex is the sheaf associated to the presheaf
> `U ↦ H^i(L_{B(U)/A(U)})` formed from the cotangent complexes of the ring maps on sections.
>
> The presheaf is `CategoryTheory.Sheaf.sectionwiseCotangentCohomology`, whose sections over `U`
> are `H^i(L_{B(U)/A(U)})` by `CategoryTheory.Sheaf.sectionwiseCotangentCohomology_obj` and whose
> restriction maps are those of the restriction squares; the sheafification is taken in abelian
> sheaves, and `CategoryTheory.Sheaf.cohomologySheafIso` is the same identification before the
> module structure over `B` is forgotten. The identification is the canonical one: it comes from
> `CategoryTheory.Sheaf.sectionwiseComplexIso`, which by
> `CategoryTheory.Sheaf.sectionwiseComplexIso_hom_unit` is induced by the canonical comparison maps
> `L_{B(U)/A(U)} ⟶ L_{B/A}(U)` of Remark 08SX.

```lean
noncomputable def cohomologySheafification (i : ℤ) :
    (presheafToSheaf J AddCommGrpCat.{max u v w}).obj (sectionwiseCotangentCohomology J f i) ≅
      (SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, max u v w} B)).obj
        ((cotangentComplex J f).homology i)
```

## Tag 08SX, a remark

[Tag 08SX](https://stacks.math.columbia.edu/tag/08SX) in the Stacks Project.

**`CategoryTheory.Sheaf.sectionsCotangentComplexComparison_restriction_degree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionsComparisonNaturality.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionsComparisonNaturality.lean#L405). The attribute's comment: “CLAUSE (2), the compatibility with the restriction maps of the site, in every cohomological degree. Remark 08SX makes three assertions: that for every U there is a canonical map L\_\{B(U)/A(U)} ⟶ L\_\{B/A}(U), that these maps are compatible with the restriction maps, and that L\_\{B/A} is the sheafification of U ↦ L\_\{B(U)/A(U)}. The first is `sectionsCotangentComplexComparison`, whose attribute records that only that clause is claimed and that this one needs naturality in U of `sectionsComonadLax`, hence of `resolutionSectionsComparison` — which is what is proved here, as `resolutionSectionsComparison_restriction_square`, and propagated to the complex. CARRIES NOTHING beyond the ambient variables of the comparison itself: arbitrary site, arbitrary Grothendieck topology, arbitrary morphism of sheaves of commutative rings, arbitrary g. No sheaf-condition, smallness or site hypothesis is added, because the proof is a variables-to-variables induction over the standard resolution tower. The SHEAFIFICATION clause (3) is not claimed here; it is `sectionwiseComplexIso` of `StacksFrontier/Cotangent/SheavesOfRings/SectionwiseCotangentComplexIso.lean`”.

> In each cohomological degree `j`, the canonical maps `L_{B(U)/A(U)} ⟶ L_{B/A}(U)` commute
> with the restriction maps along `g : U ⟶ V`.

```lean
theorem sectionsCotangentComplexComparison_restriction_degree {U V : Cᵒᵖ} (g : U ⟶ V) (j : ℤ) :
    (sectionsCotangentComplexComparison J f U).f j ≫
        ((cotangentComplex J f).X j).val.map g =
      (CommAlgCat.squareCotangentComplexMap.{max u v w, max u v w, max u v w}
          (sectionsRestrictionSquare J f g)).f j ≫
        (ModuleCat.restrictScalars (sectionsRestrictionSquare J f g).map).map
          ((sectionsCotangentComplexComparison J f V).f j)
```

**`CategoryTheory.Sheaf.sectionsCotangentComplexComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionsCotangentComparison.lean, line 899](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionsCotangentComparison.lean#L899). The attribute's comment: “the canonical map L\_\{B(U)/A(U)} ⟶ L\_\{B/A}(U); not the sheafification clause”.

> The canonical map `L_{B(U)/A(U)} ⟶ L_{B/A}(U)` of complexes of `B(U)`-modules: the comparison
> of standard resolutions, base-changed on differentials, pushed through the alternating-face-map
> complex and through the reindexing which places simplicial degree `n` in cohomological degree
> `-n`.

```lean
noncomputable def sectionsCotangentComplexComparison (U : Cᵒᵖ) :
    CommAlgCat.cotangentComplex.{max u v w, max u v w} (A.obj.obj U)
        (sectionsAlgebra J f U) ⟶
      ((moduleSections J f U).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (cotangentComplex J f)
```

**`CategoryTheory.Sheaf.isIso_sheafify_sectionwiseCotangentTermComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionwiseSheafification.lean, line 859](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionwiseSheafification.lean#L859). The attribute's comment: “the third assertion, in each degree and in sheaves of B-modules: the degree-j term of L\_\{B/A} is the sheafification of the presheaf of B-modules U ↦ L^j\_\{B(U)/A(U)} along the canonical maps of the first assertion”.

> In every degree `j`, the term of the cotangent complex `L_{B/A}` of a homomorphism of sheaves
> of rings is the sheafification of the presheaf of `B`-modules `U ↦ L^j_{B(U)/A(U)}` of the terms of
> the cotangent complexes of the ring maps on sections, along the canonical maps
> `L_{B(U)/A(U)} ⟶ L_{B/A}(U)`: the adjunct of the canonical map out of the sheafification is an
> isomorphism.

```lean
theorem isIso_sheafify_sectionwiseCotangentTermComparison (j : ℤ) :
    IsIso ((PresheafOfModules.sheafificationHomEquiv.{max u v w}
      (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, max u v w} B).obj)).symm
        (sectionwiseCotangentTermComparison J f j))
```

**`CategoryTheory.Sheaf.sheafifiedSectionwiseCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/SectionwiseSheafification.lean, line 1006](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/SectionwiseSheafification.lean#L1006). The attribute's comment: “the third assertion: L\_\{B/A} is the sheafification of U ↦ L\_\{B(U)/A(U)}, the sheafification of the presheaf of complexes of abelian groups U ↦ L\_\{B(U)/A(U)} being isomorphic to L\_\{B/A} along the canonical maps of the first assertion; degreewise, in sheaves of B-modules, this is isIso\_sheafify\_sectionwiseCotangentTermComparison”.

> The cotangent complex `L_{B/A}` of a homomorphism of sheaves of rings is the sheafification of
> the rule `U ↦ L_{B(U)/A(U)}`: the sheafification of the presheaf of complexes of abelian groups
> `U ↦ L_{B(U)/A(U)}` is isomorphic to `L_{B/A}`, by the canonical maps followed by the counit of
> sheafification.

```lean
noncomputable def sheafifiedSectionwiseCotangentComplexIso :
    ((presheafToSheaf J AddCommGrpCat.{max u v w}).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (sectionwiseCotangentPresheafComplex J f) ≅ cotangentComplexAb J f
```

## Tag 08UR, a lemma

[Tag 08UR](https://stacks.math.columbia.edu/tag/08UR) in the Stacks Project.

**`CategoryTheory.Sheaf.cotangentComplex_homologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/HomologyZero.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/HomologyZero.lean#L579).

> The zeroth homology of the cotangent complex of a morphism of sheaves of
> commutative rings on a site is its sheaf of relative differentials, the sheaf of modules
> corepresenting the relative derivations.

```lean
noncomputable def cotangentComplex_homologyZeroIso :
    (cotangentComplex J f).homology 0 ≅
      (AlgebraicGeometry.SheafOfModules.derivationsFunctor.{max u v w} A B f).coreprX
```

## Tag 08SY, a lemma

[Tag 08SY](https://stacks.math.columbia.edu/tag/08SY) in the Stacks Project.

**`CategoryTheory.Sheaf.prodCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/ProductRings.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/ProductRings.lean#L192). The attribute's comment: “the comparison map”.

> The canonical comparison map `L_{B ⨯ B'/A} ⟶ L_{B/A} ⊕ L_{B'/A}` of complexes of sheaves of
> `B ⨯ B'`-modules: the pairing of the two maps of cotangent complexes induced by the two projection
> squares, each summand read over `B ⨯ B'` by restriction of scalars along the corresponding
> projection.

```lean
noncomputable def prodCotangentComparison :
    cotangentComplex.{u, v, w} J (prodRingHom J f f') ⟶ prodCotangentSum J f f'
```

**`CategoryTheory.Sheaf.prodCotangentComparisonDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/ProductRings.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/ProductRings.lean#L257). The attribute's comment: “the comparison map in the derived category”.

> The comparison map `L_{B ⨯ B'/A} ⟶ L_{B/A} ⊕ L_{B'/A}` read in the derived category
> `D(B ⨯ B')`.

```lean
noncomputable abbrev prodCotangentComparisonDerived
    [HasDerivedCategory.{t} (targetModules.{u, v, w} J (B ⨯ B'))] :
    cotangentComplexDerived.{u, v, w, t} J (prodRingHom J f f') ⟶
      DerivedCategory.Q.obj (prodCotangentSum J f f')
```

**`CategoryTheory.Sheaf.isIso_prodCotangentComparisonDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/ProductRingsSectionwise.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/ProductRingsSectionwise.lean#L555). The attribute's comment: “the lemma: the canonical map L\_\{B×B'/A} → L\_\{B/A} ⊕ L\_\{B'/A}, the pairing of the maps induced by the two projections, is an isomorphism in D(B×B'), for an arbitrary site and arbitrary homomorphisms A → B, A → B' of sheaves of rings”.

> Let `C` be a site and let `A ⟶ B`, `A ⟶ B'` be homomorphisms of sheaves of commutative rings
> on `C`. Then the canonical map `L_{B ⨯ B'/A} ⟶ L_{B/A} ⊕ L_{B'/A}`
> (`CategoryTheory.Sheaf.prodCotangentComparisonDerived`, the pairing of the maps of cotangent
> complexes induced by the two projections) is an isomorphism in `D(B ⨯ B')`.

```lean
theorem isIso_prodCotangentComparisonDerived
    [HasDerivedCategory.{t} (targetModules.{u, v, w} J (B ⨯ B'))] :
    IsIso (prodCotangentComparisonDerived.{u, v, w, t} J f f')
```

## Tag 08SZ, a lemma

[Tag 08SZ](https://stacks.math.columbia.edu/tag/08SZ) in the Stacks Project.

**`CategoryTheory.Sheaf.baseChangedCotangentComplexDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/BaseChangedCotangentDerived.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/BaseChangedCotangentDerived.lean#L184). The attribute's comment: “the first vertex: `L_{B/A} ⊗^L_B D`, the derived pullback along `h : B ⟶ D` of the cotangent complex, is the class of its degreewise base change, the first vertex of the triangle of `CategoryTheory.Sheaf.exists_distTriang_towerCotangent`; on any site”.

> **The first vertex of the triangle of Tag 08SZ is `L_{B/A} ⊗^L_B D`.** The complex
> `L_{B/A} ⊗_B D`, the degreewise base change of the cotangent complex of `A ⟶ B`, represents the
> derived base change of `L_{B/A}` along `h : B ⟶ D`: the cotangent complex is K-flat with flat
> terms, so its derived pullback is computed degreewise (Tag 06YY), and degreewise pullback along
> the change of coefficient rings is extension of scalars.

```lean
def baseChangedCotangentComplexDerivedIso :
    (towerDerivedBaseChange.{u, v, w} J h).obj
        (DerivedCategory.Q.obj (cotangentComplex.{u, v, w} J g)) ≅
      DerivedCategory.Q.obj (baseChangedCotangentComplex.{u, v, w} J g h)
```

**`CategoryTheory.Sheaf.towerCotangentBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean#L284). The attribute's comment: “the first displayed arrow L\_\{B/A} ⊗\_B C ⟶ L\_\{C/A}, with the DEGREEWISE tensor product in place of the derived one — the two agree only once the terms of L\_\{B/A} are known to be locally free, which is not proved here and for which no derived extension of scalars for sheaves of modules on a site exists in this library. Distinguishedness of the triangle is not claimed by this declaration”.

> **Stacks Project, Tag 08SZ, the first displayed arrow.** The canonical map
> `L_{B/A} ⊗_B D ⟶ L_{D/A}` of complexes of sheaves of `D`-modules: the transpose, along the
> extension–restriction adjunction for sheaves of modules, of the `B`-linear map of cotangent
> complexes attached to the square `(𝟙 A, h)` of the tower.
>
> The tensor product in the source is the degreewise one, not the derived one; see the module
> documentation.

```lean
noncomputable def towerCotangentBaseChange :
    baseChangedCotangentComplex.{u, v, w} J g h ⟶ cotangentComplex.{u, v, w} J (g ≫ h)
```

**`CategoryTheory.Sheaf.towerCotangentChangeOfBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean#L310). The attribute's comment: “the second displayed arrow L\_\{C/A} ⟶ L\_\{C/B}, unconditionally and with no identification intervening. Distinguishedness of the triangle is not claimed by this declaration”.

> **Stacks Project, Tag 08SZ, the second displayed arrow.** The canonical
> change-of-base-ring map `L_{D/A} ⟶ L_{D/B}` of complexes of sheaves of `D`-modules: the map of
> cotangent complexes attached to the square `(g, 𝟙 D)` of the tower. Restriction of scalars along
> the identity of `D` is the identity functor, so no identification intervenes between the stated
> target and `L_{D/B}`.

```lean
noncomputable def towerCotangentChangeOfBase :
    cotangentComplex.{u, v, w} J (g ≫ h) ⟶ cotangentComplex.{u, v, w} J h
```

**`CategoryTheory.Sheaf.exists_distTriang_cotangentComplexDerived_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangle.lean#L368). The attribute's comment: “the distinguished triangle, under ONE carried hypothesis the source lacks: the short exact sequence `S`, `hS` realizing the two canonical arrows (`hf`, `hg`) on the three vertices (`e₁`, `e₂`, `e₃`) — the sheaf-level analogue of Tag 08SD, absent from this library, as are Tag 08SE and the ISOMORPHISM of Tag 08SY. The first vertex carries the DEGREEWISE tensor product in place of the derived one”.

> **Stacks Project, Tag 08SZ, under one carried hypothesis.** Let `A ⟶ B ⟶ D` be homomorphisms
> of sheaves of commutative rings on a site. Then there is a distinguished triangle
>
> `L_{B/A} ⊗_B D ⟶ L_{D/A} ⟶ L_{D/B} ⟶ (L_{B/A} ⊗_B D)[1]`
>
> in `D(D)` whose first two arrows are the two canonical maps
> `CategoryTheory.Sheaf.towerCotangentBaseChange` and
> `CategoryTheory.Sheaf.towerCotangentChangeOfBase` constructed above.
>
> The hypothesis carried is the sheaf-level differential short exact sequence of the source's
> proof (Tag 08SD): a short complex `S` of cochain complexes of sheaves of `D`-modules that is
> short exact (`hS`), whose three terms are the three vertices (`e₁`, `e₂`, `e₃`) and whose two
> maps are the two canonical arrows (`hf`, `hg`). The source identifies the third term using
> Tag 08SE and reduces to the case of an injective `B ⟶ D` using the isomorphism of Tag 08SY.
>
> The first vertex carries the degreewise, not the derived, tensor product; see the module
> documentation.

```lean
theorem exists_distTriang_cotangentComplexDerived_of_shortExact
    [HasDerivedCategory.{t} (targetModules.{u, v, w} J D)]
    (S : ShortComplex (CochainComplex (targetModules.{u, v, w} J D) ℤ)) (hS : S.ShortExact)
    (e₁ : S.X₁ ≅ baseChangedCotangentComplex.{u, v, w} J g h)
    (e₂ : S.X₂ ≅ cotangentComplex.{u, v, w} J (g ≫ h))
    (e₃ : S.X₃ ≅ cotangentComplex.{u, v, w} J h)
    (hf : S.f = e₁.hom ≫ towerCotangentBaseChange.{u, v, w} J g h ≫ e₂.inv)
    (hg : S.g = e₂.hom ≫ towerCotangentChangeOfBase.{u, v, w} J g h ≫ e₃.inv) :
    ∃ δ : cotangentComplexDerived.{u, v, w, t} J h ⟶
        (DerivedCategory.Q.obj (baseChangedCotangentComplex.{u, v, w} J g h))⟦(1 : ℤ)⟧,
      Triangle.mk (DerivedCategory.Q.map (towerCotangentBaseChange.{u, v, w} J g h))
          (DerivedCategory.Q.map (towerCotangentChangeOfBase.{u, v, w} J g h)) δ ∈
        distTriang (DerivedCategory (targetModules.{u, v, w} J D))
```

**`CategoryTheory.Sheaf.exists_distTriang_towerCotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangleGeneral.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/FundamentalTriangleGeneral.lean#L565). The attribute's comment: “the distinguished triangle `L_{B/A} ⊗^L_B D → L_{D/A} → L_{D/B} → (L_{B/A} ⊗^L_B D)[1]` with the canonical first two arrows, in `D(D)`, on any site; the first vertex is identified with `L_{B/A} ⊗^L_B D` by `CategoryTheory.Sheaf.baseChangedCotangentComplexDerivedIso`”.

> **Stacks 08SZ, the fundamental triangle.** Let `A ⟶ B ⟶ D` be homomorphisms of sheaves of
> commutative rings on a site. The triangle
>
> `L_{B/A} ⊗_B D ⟶ L_{D/A} ⟶ L_{D/B} ⟶ (L_{B/A} ⊗_B D)[1]`
>
> with first two arrows `CategoryTheory.Sheaf.towerCotangentBaseChange` and
> `CategoryTheory.Sheaf.towerCotangentChangeOfBase` is distinguished in `D(D)`; its first vertex
> is `L_{B/A} ⊗^L_B D` by `CategoryTheory.Sheaf.baseChangedCotangentComplexDerivedIso`.
>
> This is the argument of the source: the homomorphism `B ⟶ B × D`, `b ↦ (b, h b)`, is injective
> on sections, so the triangle of `A ⟶ B ⟶ B × D` is distinguished
> (`CategoryTheory.Sheaf.exists_distTriang_towerCotangent_of_injective`), and the exact second
> summand functor `Mod(B × D) ⥤ Mod(D)` carries it to the triangle of `A ⟶ B ⟶ D`.

```lean
theorem exists_distTriang_towerCotangent
    [HasDerivedCategory.{t} (targetModules.{u, v, w} J D)] :
    ∃ δ : cotangentComplexDerived.{u, v, w, t} J h ⟶
        (DerivedCategory.Q.obj (baseChangedCotangentComplex.{u, v, w} J g h))⟦(1 : ℤ)⟧,
      Triangle.mk (DerivedCategory.Q.map (towerCotangentBaseChange.{u, v, w} J g h))
          (DerivedCategory.Q.map (towerCotangentChangeOfBase.{u, v, w} J g h)) δ ∈
        distTriang (DerivedCategory (targetModules.{u, v, w} J D))
```

## Tag 08T0, a lemma

[Tag 08T0](https://stacks.math.columbia.edu/tag/08T0) in the Stacks Project.

**`CategoryTheory.Sheaf.pointStalkCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/PointStalkCotangentComplex.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/PointStalkCotangentComplex.lean#L397). The attribute's comment: “The point is a point of the site in the sense of Stacks 00Y5 (Mathlib's GrothendieckTopology.Point), with fibre functor valued in the universe of the sections of A and B, the single universe of sets of the source. The left-hand side is the stalk at the point of L\_\{B/A} as a complex of B\_p-modules (Stacks.sheafModuleFiberOfCommRing), the right-hand side is the cotangent complex of Tag 08PN of the ring map of stalks A\_p -> B\_p (pointStalkAlgebra). The instance LocallySmall.\{max u v w} C holds for every category C in these universes (Mathlib's instance locallySmall\_of\_univLE), so it restricts nothing. On germs the isomorphism is described by pointStalkCotangentComplexIso\_hom\_germ.”.

> **The stalk of the cotangent complex at a point of a site** (Tag 08T0): the stalk at `Φ` of
> `L_{B/A}` is `L_{B_Φ/A_Φ}`, as complexes of `B_Φ`-modules. On germs it is described by
> `CategoryTheory.Sheaf.pointStalkCotangentComplexIso_hom_germ`.

```lean
def pointStalkCotangentComplexIso :
    ((Stacks.sheafModuleFiberOfCommRing Φ B).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (cotangentComplex J f) ≅
      CommAlgCat.cotangentComplex.{max u v w, max u v w} _ (pointStalkAlgebra J Φ f)
```

## Tag 08US, a lemma

[Tag 08US](https://stacks.math.columbia.edu/tag/08US) in the Stacks Project.

**`CategoryTheory.Sheaf.naiveComparisonNegOne_conormalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean#L529). The attribute's comment: “the degree `-1` component of the canonical map `L_{B/A} → NL_{B/A}`, with its value `[d₀ x - d₁ x]` on a pure differential. Hypotheses beyond the source: the naive cotangent complex is realized as the conormal sequence of the presentation `P₀ ⟶ B` by the degree-zero term of the standard resolution, and the identification of that presentation with `Stacks.Sites.FreeAlgebra.canonicalPresentation` is not carried. The identification of the naive complex with the truncation `τ_{≥ -1} L_{B/A}` is NOT proved: the source proves it by comparison with the chaotic topology, and that comparison is not carried. Tag 08TZ, which it uses, IS formalized, as `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`”.

> **Stacks 08US, the degree `-1` component of the canonical map.** On the pure differential
> `d x` of a local section `x` of `P₁`, the comparison is the class of `d₀ x - d₁ x` in `I/I²`;
> the general local section `d x ⊗ b` goes to `b` times that class.

```lean
theorem naiveComparisonNegOne_conormalClass (U : Cᵒᵖ)
    (x : (resolutionTerm J f (op ⦋1⦌)).obj.obj U) :
    (naiveComparisonNegOne J f).val.app U
        (((cotangentSimplicialModule J f).universalDerivation (op ⦋1⦌)).d x) =
      conormalClassSection J f U (faceDifference J f U x)
```

**`CategoryTheory.Sheaf.naiveComparisonNegOne_comp_conormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean#L579). The attribute's comment: “the lower commuting square: the degree `-1` component composed with the differential of the naive cotangent complex is the difference of the two faces composed with the degree-zero component. Hypotheses beyond the source: the naive cotangent complex is realized as the conormal sequence of the presentation `P₀ ⟶ B` by the degree-zero term of the standard resolution, and the differential of `L_{B/A}` appears as the difference of the two face maps of the base-changed simplicial module rather than transported through `CategoryTheory.Sheaf.cotangentComplex_degreeIso`”.

> **Stacks 08US, the lower commuting square.** Following the degree `-1` component by the
> differential `I/I² ⟶ B ⊗_{P₀} Ω_{P₀/A}` of the naive cotangent complex is the difference of the
> two faces `Ω_{P₁/A} ⊗ B ⇉ Ω_{P₀/A} ⊗ B` followed by the degree-zero component.  The difference
> of the two faces is the differential of the cotangent complex out of degree `-1`, so this is the
> lower square of the comparison diagram: the differential of the naive complex sends
> `[d₀ x - d₁ x]` to `1 ⊗ d(d₀ x - d₁ x)`.

```lean
theorem naiveComparisonNegOne_comp_conormal :
    naiveComparisonNegOne J f ≫ (naiveSequence J f).f =
      (cotangentSimplicialModule J f).object.δ 0 ≫ naiveComparisonZero J f -
        (cotangentSimplicialModule J f).object.δ 1 ≫ naiveComparisonZero J f
```

**`CategoryTheory.Sheaf.naiveComparisonNegOne_faceSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonArrow.lean#L639). The attribute's comment: “the upper commuting square: the degree `-1` component annihilates the alternating sum of the three faces, which is the differential of `L_{B/A}` into degree `-1`, the naive cotangent complex being zero in degree `-2`. Hypotheses beyond the source: the naive cotangent complex is realized as the conormal sequence of the presentation `P₀ ⟶ B` by the degree-zero term of the standard resolution, and the differential of `L_{B/A}` appears as the alternating sum of the face maps of the base-changed simplicial module rather than transported through `CategoryTheory.Sheaf.cotangentComplex_degreeIso`”.

> **Stacks 08US, the upper commuting square.** The degree `-1` component annihilates the
> alternating sum of the three faces `Ω_{P₂/A} ⊗ B ⟶ Ω_{P₁/A} ⊗ B`, which is the differential of
> the cotangent complex into degree `-1`.  The naive cotangent complex is zero in degree `-2`, so
> this is exactly the commutation of the comparison with that differential.

```lean
theorem naiveComparisonNegOne_faceSum :
    ((cotangentSimplicialModule J f).object.δ (0 : Fin 3) -
        (cotangentSimplicialModule J f).object.δ (1 : Fin 3) +
        (cotangentSimplicialModule J f).object.δ (2 : Fin 3)) ≫
      naiveComparisonNegOne J f = 0
```

**`CategoryTheory.Sheaf.naiveCotangentComplexIsoCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean#L283). The attribute's comment: “the naive cotangent complex of the presentation P₀ = A[B] is the naive cotangent complex NL\_\{B/A} of Tag 08TW”.

> The naive cotangent complex of the presentation `P₀ ⟶ B` is the naive cotangent complex
> `NL_{B/A}` of Tag 08TW, through the isomorphism `P₀ ≅ A[B]` of `A`-algebras over `B`.

```lean
noncomputable def naiveCotangentComplexIsoCanonical :
    naiveCotangentComplex.{u, v, w} J f ≅
      Stacks.SheafOfModules.naiveCotangentComplex.{v, u, max u v w, u} J A B f
```

**`CategoryTheory.Sheaf.canonicalNaiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean#L397). The attribute's comment: “the canonical map `L_{B/A} → NL_{B/A}`, into the naive cotangent complex `Stacks.SheafOfModules.naiveCotangentComplex` of Tag 08TW”.

> **Stacks 08US, the canonical map.** The canonical map `L_{B/A} ⟶ NL_{B/A}` from the cotangent
> complex to the naive cotangent complex of Tag 08TW: `d x ⊗ b ↦ b · [d₀ x - d₁ x]` in degree `-1`
> and `d p ⊗ b ↦ b ⊗ d p` in degree `0` (`CategoryTheory.Sheaf.naiveComparison`), read in
> `NL_{B/A}` through the isomorphism `P₀ ≅ A[B]` of `A`-algebras over `B`.

```lean
noncomputable def canonicalNaiveComparison :
    cotangentComplex.{u, v, w} J f ⟶
      Stacks.SheafOfModules.naiveCotangentComplex.{v, u, max u v w, u} J A B f
```

**`CategoryTheory.Sheaf.canonicalNaiveComparison_isIso_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/NaiveComparisonCanonical.lean#L410). The attribute's comment: “the canonical map identifies the naive cotangent complex `NL_{B/A}` of Tag 08TW with the truncation `τ_{≥ -1} L_{B/A}`: it is an isomorphism on the cohomology sheaf of every degree `≥ -1`, the naive complex having no terms outside degrees `-1` and `0`”.

> **Stacks 08US.** The canonical map `L_{B/A} ⟶ NL_{B/A}` into the naive cotangent complex of
> Tag 08TW is an isomorphism on the cohomology sheaf of every degree `≥ -1`.  Since `NL_{B/A}` has
> no terms outside degrees `-1` and `0` (`Stacks.SheafOfModules.naiveCotangentComplex_isZero_X`),
> this says that the canonical map identifies the naive cotangent complex with the truncation
> `τ_{≥ -1} L_{B/A}`.

```lean
theorem canonicalNaiveComparison_isIso_homologyMap (i : ℤ) (hi : -1 ≤ i) :
    IsIso (HomologicalComplex.homologyMap (canonicalNaiveComparison J f) i)
```

**`CategoryTheory.Sheaf.naiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean#L226). The attribute's comment: “the canonical map `L_{B/A} → NL_{B/A}` as a map of complexes, assembled from the degreewise comparison and its two squares. Hypotheses beyond the source: the naive cotangent complex is realized as the conormal sequence of the presentation `P₀ ⟶ B` by the degree-zero term of the standard resolution, and the identification of that presentation with `Stacks.Sites.FreeAlgebra.canonicalPresentation` is not carried”.

> The canonical map of complexes `L_{B/A} ⟶ NL_{B/A}`: it is `d x ⊗ b ↦ b · [d₀ x - d₁ x]` in
> degree `-1`, it is `d p ⊗ b ↦ b ⊗ d p` in degree `0`, and it is zero in every other degree, the
> naive cotangent complex having no other terms.

```lean
noncomputable def naiveComparison :
    cotangentComplex.{u, v, w} J f ⟶ naiveCotangentComplex.{u, v, w} J f
```

**`CategoryTheory.Sheaf.naiveComparison_isIso_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean#L281). The attribute's comment: “the identification of the naive cotangent complex with the truncation `τ_{≥ -1} L_{B/A}`, stated as: the canonical map is an isomorphism on the cohomology sheaf of every degree `≥ -1`, the naive complex having no cohomology below degree `-1` by `CategoryTheory.Sheaf.naiveCotangentComplex_isZero_homology`. Hypotheses carried: `homologyZeroIsIso` and `homologyNegOneIsIso`, the isomorphisms on `H⁰` and on `H^{-1}`, which are the final step of the source's proof — the comparison with the chaotic topology, reducing them to the ring-level map of Tag 08UP and transporting along the inverse-image isomorphism of Tag 08TZ. That tag IS carried as an isomorphism of complexes, `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`; what is not carried is the comparison with the chaotic topology”.

> If the canonical map `L_{B/A} ⟶ NL_{B/A}` is an isomorphism on the cohomology sheaves of
> degrees `0` and `-1` (the hypotheses `homologyZeroIsIso` and `homologyNegOneIsIso`), then it is an
> isomorphism on the cohomology sheaf of every degree `≥ -1`. Since the naive cotangent complex has
> no cohomology below degree `-1`, this says that the canonical map identifies `NL_{B/A}` with the
> truncation `τ_{≥ -1} L_{B/A}`.

```lean
theorem naiveComparison_isIso_homologyMap
    (homologyZeroIsIso :
      IsIso (HomologicalComplex.homologyMap (naiveComparison.{u, v, w} J f) 0))
    (homologyNegOneIsIso :
      IsIso (HomologicalComplex.homologyMap (naiveComparison.{u, v, w} J f) (-1)))
    (i : ℤ) (hi : -1 ≤ i) :
    IsIso (HomologicalComplex.homologyMap (naiveComparison.{u, v, w} J f) i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.18, Tag 08UQ](https://stacks.math.columbia.edu/tag/08UQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
