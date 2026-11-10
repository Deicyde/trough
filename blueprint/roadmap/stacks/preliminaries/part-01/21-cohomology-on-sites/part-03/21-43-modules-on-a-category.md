---
declaration: section
origin: cited
lean: Stacks.ModulesOnACategory.CartesianObjects.IsCartesian, Stacks.ModulesOnACategory.CartesianObjects.cartesianDerivedModules, Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isClosedUnderIsomorphisms, Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isSaturated, Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isTriangulated, Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isClosedUnderColimitsOfShape, Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isClosedUnderIsomorphisms, Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isSaturated
statement: formalized
proof: formalized
---

# 21.43 Modules on a category

Section 21.43 of the Stacks Project, [Tag 0GYU](https://stacks.math.columbia.edu/tag/0GYU). 13 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GYV, a definition

[Tag 0GYV](https://stacks.math.columbia.edu/tag/0GYV) in the Stacks Project.

**`Stacks.ModulesOnACategory.CartesianObjects.IsCartesian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjects.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjects.lean#L160). The attribute's comment: “cartesian-object condition”.

> An object of `D(O)` has cartesian derived sections if for every morphism `U → V` of `C` the
> canonical derived base-change comparison `RΓ(V, K) ⊗^L_{O(V)} O(U) ⟶ RΓ(U, K)` is an
> isomorphism.

```lean
abbrev IsCartesian (K : Stacks.ModulesOnACategory.QuasiCoherentEquivalence.DMod.{0} O) : Prop
```

**`Stacks.ModulesOnACategory.CartesianObjects.cartesianDerivedModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjects.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjects.lean#L166). The attribute's comment: “the full subcategory QC(O)”.

> The full subcategory `QC(O) ⊆ D(O)` consisting of the objects with cartesian derived
> sections.

```lean
abbrev cartesianDerivedModules : Type _
```

## Tag 0GYW, a lemma

[Tag 0GYW](https://stacks.math.columbia.edu/tag/0GYW) in the Stacks Project.

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean#L330). The attribute's comment: “strictly full”.

> **Stacks 0GYW**, strict fullness: the cartesian objects form a subcategory of `D(O)` closed
> under isomorphisms.

```lean
instance isQC_isClosedUnderIsomorphisms :
    ObjectProperty.IsClosedUnderIsomorphisms (IsQC.{w} bc)
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean#L353). The attribute's comment: “saturated”.

> **Stacks 0GYW**, saturation: a direct summand of a cartesian object is cartesian.

```lean
instance isQC_isSaturated : ObjectProperty.IsSaturated (IsQC.{w} bc)
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean#L375). The attribute's comment: “triangulated”.

> **Stacks 0GYW**, triangulatedness: the cartesian objects form a triangulated subcategory of
> `D(O)`.

```lean
instance isQC_isTriangulated : ObjectProperty.IsTriangulated (IsQC.{w} bc)
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.isQC_isClosedUnderColimitsOfShape`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsLocalizing.lean#L397). The attribute's comment: “arbitrary direct sums”.

> **Stacks 0GYW**, direct sums: a direct sum of cartesian objects, indexed by an arbitrary
> type, is cartesian.

```lean
instance isQC_isClosedUnderColimitsOfShape (J : Type j) :
    ObjectProperty.IsClosedUnderColimitsOfShape (IsQC.{w} bc) (Discrete J)
```

**`Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L100). The attribute's comment: “strictly full”.

> **Tag 0GYW, strict fullness.** The cartesian objects of `D(O)` are closed under isomorphism,
> so `QC(O)` is a strictly full subcategory of `D(O)`.

```lean
instance isCartesian_isClosedUnderIsomorphisms :
    ObjectProperty.IsClosedUnderIsomorphisms (Stacks.ModulesOnACategory.CartesianObjects.IsCartesian
      O hO)
```

**`Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L109). The attribute's comment: “saturated”.

> **Tag 0GYW, saturation.** The cartesian objects of `D(O)` are closed under direct summands, so
> `QC(O)` is a saturated (thick) subcategory of `D(O)`.

```lean
instance isCartesian_isSaturated :
    ObjectProperty.IsSaturated (Stacks.ModulesOnACategory.CartesianObjects.IsCartesian O hO)
```

**`Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L119). The attribute's comment: “triangulated”.

> **Tag 0GYW, triangulatedness.** `QC(O)` is a triangulated subcategory of `D(O)`: for each
> `a : V ⟶ U` the comparison maps are the components of a shift-compatible natural transformation
> between triangulated functors, `- ⊗^L_{O(V)} O(U)` being triangulated as a left adjoint of a
> triangulated functor, and the locus where such a transformation is invertible is triangulated.

```lean
instance isCartesian_isTriangulated :
    ObjectProperty.IsTriangulated (Stacks.ModulesOnACategory.CartesianObjects.IsCartesian O hO)
```

**`Stacks.ModulesOnACategory.CartesianSubcategory.isCartesian_isClosedUnderCoproducts_of_smallSite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L228). The attribute's comment: “arbitrary direct sums”.

> **Tag 0GYW, arbitrary direct sums.** `QC(O)` is closed under direct sums indexed by an
> arbitrary type. Discarding the zero summands leaves an index type small in the module universe,
> because `D(O)` is locally small there by tag 079Q, and both `RΓ(V, -) ⋙ (- ⊗^L_{O(V)} O(U))` and
> `RΓ(U, -)` preserve direct sums of that size — the first as a left adjoint, the second as the
> derived functor of the exact evaluation. Stated for a small site, the standing smallness
> convention of the source.

```lean
instance isCartesian_isClosedUnderCoproducts_of_smallSite {C : Type} [SmallCategory C]
    (O : Cᵒᵖ ⥤ RingCat.{0}) (hO : ∀ (U : Cᵒᵖ) (x y : O.obj U), x * y = y * x) (J : Type j) :
    ObjectProperty.IsClosedUnderColimitsOfShape
      (Stacks.ModulesOnACategory.CartesianObjects.IsCartesian O hO) (Discrete J)
```

## Tag 0GZQ, a lemma

[Tag 0GZQ](https://stacks.math.columbia.edu/tag/0GZQ) in the Stacks Project.

**`Stacks.ModulesOnACategory.TopCohomology.isQuasicoherentOnSite_topHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/QuasiCoherenceOfTopCohomology.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/QuasiCoherenceOfTopCohomology.lean#L446).

> **Quasi-coherence of the top cohomology module.**  Let `C` be a category viewed as a site
> with the chaotic topology and let `O` be its sheaf of rings.  If `M` is an object of `QC(O)`
> and `b` is an integer such that `H^i(M) = 0` for all `i > b`, then `H^b(M)` is a quasi-coherent
> module on `(C, O)`.

```lean
theorem isQuasicoherentOnSite_topHomology (hJ : J = ⊥) (bc : BaseChangeData.{w} R.obj)
    (M : DMod.{w} R.obj) (hM : IsQC.{w} bc M) (b : ℤ)
    (hvan : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor
      (PresheafOfModules.{max u v r w} R.obj) i).obj M)) :
    ∃ hsh : Presheaf.IsSheaf J ((DerivedCategory.homologyFunctor
        (PresheafOfModules.{max u v r w} R.obj) b).obj M).presheaf,
      (⟨_, hsh⟩ : SheafOfModules.{max u v r w} R).IsQuasicoherentOnSite
```

## Tag 0H0R, a lemma

[Tag 0H0R](https://stacks.math.columbia.edu/tag/0H0R) in the Stacks Project.

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.main_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/TerminalMorphismOfSitesEquivalence.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/TerminalMorphismOfSitesEquivalence.lean#L67).

> **Lemma 21.43.4 (tag 0H0R).** The adjunction `Lf^* ⊣ Rf_*` along the morphism of sites
> `f : (C, O) → (pt, O(X))` of a terminal object `X` exhibits `Lf^*` and `Rf_*` as mutually
> quasi-inverse equivalences between `D(O(X))` and `QC(O)`: the derived pullback lands in `QC(O)`,
> the unit is invertible on all of `D(O(X))`, and the counit is invertible on every object of
> `QC(O)`.
>
> Both the base change and the derived pullback are the library's own constructions here — the
> canonical base-change datum, and the morphism of sites of `X` — so the only hypothesis is the
> commutativity `hO` of the section rings of `O`.

```lean
theorem main_equivalence (hO : ∀ (U : Cᵒᵖ) (x y : O.obj U), x * y = y * x) :
    (∀ P, IsQC.{w} (baseChangeDataOfComm.{r, v, u, w} O hO)
        ((morphismOfSites O hO hX).Lpullback.obj P)) ∧
    (∀ P : DerivedCategory (ModuleCat.{max u v r w} (O.obj (Opposite.op X))),
      IsIso ((morphismOfSites O hO hX).adj.unit.app P)) ∧
    (∀ K, IsQC.{w} (baseChangeDataOfComm.{r, v, u, w} O hO) K →
      IsIso ((morphismOfSites O hO hX).adj.counit.app K))
```

## Tag 0H0S, a lemma

[Tag 0H0S](https://stacks.math.columbia.edu/tag/0H0S) in the Stacks Project.

**`Stacks.ModulesOnACategory.MorphismsOverAnObject.homDerivedRestriction_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/MorphismsOverAnObject.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/MorphismsOverAnObject.lean#L356).

> Let `K` be a derived module with cartesian derived sections and let `M` be an arbitrary derived
> module. Applying derived sections over the terminal object `id_U` of `C/U` and conjugating by
> `derivedSectionsIso` identifies the morphisms `K|_U ⟶ M|_U` in `D(O_U)` with the morphisms
> `RΓ(U, K) ⟶ RΓ(U, M)` in `D(O(U))`.

```lean
theorem homDerivedRestriction_bijective
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x)
    (K M : DMod.{w} O)
    (hK : IsQC.{w} (baseChangeDataOfComm.{r, v, u, w} O hO) K) :
    Function.Bijective (fun f : (derivedRestriction.{w} O U).obj K ⟶
        (derivedRestriction.{w} O U).obj M =>
      ((derivedSectionsIso.{w} O U).app K).inv ≫
        (RGamma.{w} (overRingPresheaf O U)
          (Opposite.op (Over.mk (𝟙 U)))).map f ≫
        ((derivedSectionsIso.{w} O U).app M).hom)
```

## Tag 0GYX, a lemma

[Tag 0GYX](https://stacks.math.columbia.edu/tag/0GYX) in the Stacks Project.

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_subcomplex_containing_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallSubcomplexEnlargements.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallSubcomplexEnlargements.lean#L123). The attribute's comment: “presheaf model”.

> **Stacks 0GYX in the presheaf model.** There is a cardinal, depending only on the category
> and its presheaf of rings, such that every family of prescribed sections of a complex of
> `O`-modules is contained in a subcomplex whose number of sections is bounded by the maximum of
> that cardinal and the size of the family.
>
> This is the transport of
> `Stacks.ModulesOnACategory.exists_subcomplex_containing_sections_of_size_le` across the
> equivalence between sheaves of modules on the chaotic site and presheaves of modules, which
> preserves monomorphisms and identifies the two counts of sections.

```lean
theorem exists_subcomplex_containing_sections (O : Cᵒᵖ ⥤ RingCat.{r}) :
    ∃ kappa : Cardinal.{max u v r w},
      ∀ (F : CochainComplex (PresheafOfModules.{max u v r w} O) ℤ)
        (Omega : ∀ (i : ℤ) (U : C), Set ((F.X i).obj (op U))),
        ∃ (H : CochainComplex (PresheafOfModules.{max u v r w} O) ℤ) (inclusion : H ⟶ F),
          Mono inclusion ∧
            (∀ (i : ℤ) (U : C) (x : (F.X i).obj (op U)), x ∈ Omega i U →
              ∃ y : (H.X i).obj (op U), (inclusion.f i).app (op U) y = x) ∧
            complexSectionSize.{w} O H ≤ max kappa (presheafSectionFamilySize.{w} Omega)
```

**`Stacks.ModulesOnACategory.exists_subcomplex_containing_sections_of_size_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallSubcomplexesOfSections.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallSubcomplexesOfSections.lean#L476).

> **Stacks 0GYX.** There is a cardinal, depending only on the category and its sheaf of
> rings, such that every family of prescribed sections of a complex is contained in a
> subcomplex whose size is bounded by the maximum of that cardinal and the size of the
> family.

```lean
theorem exists_subcomplex_containing_sections_of_size_le
    (R : Sheaf (⊥ : GrothendieckTopology C) RingCat.{r}) :
    ∃ kappa : Cardinal.{max u v m r},
      ∀ (F : CochainComplex (SheafOfModules.{m} R) ℤ)
        (Omega : ∀ (i : ℤ) (U : C), Set ((F.X i).val.obj (op U))),
        ∃ (H : CochainComplex (SheafOfModules.{m} R) ℤ) (inclusion : H ⟶ F),
          Mono inclusion ∧
            (∀ (i : ℤ) (U : C) (x : (F.X i).val.obj (op U)), x ∈ Omega i U →
              ∃ y : (H.X i).val.obj (op U), (inclusion.f i).val.app (op U) y = x) ∧
            complexSectionSize H ≤ max kappa (sectionFamilySize Omega)
```

## Tag 0GYY, a lemma

[Tag 0GYY](https://stacks.math.columbia.edu/tag/0GYY) in the Stacks Project.

**`Stacks.ModulesOnACategory.exists_small_quasiIso_subcomplex_presheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticModelTransport.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticModelTransport.lean#L289). The attribute's comment: “presheaf model”.

> There is a cardinal, depending only on the category and its sheaf of rings, such that every
> complex of presheaves of modules representing a derived object contains a quasi-isomorphic
> subcomplex bounded by that cardinal and the size of the derived object.

```lean
theorem exists_small_quasiIso_subcomplex_presheaf :
    ∃ κ : Cardinal.{max u v r w},
      ∀ (F : CochainComplex (PresheafOfModules.{max u v r w} R.obj) ℤ)
        (K : DerivedCategory (PresheafOfModules.{max u v r w} R.obj)),
        Nonempty (DerivedCategory.Q.obj F ≅ K) →
          ∃ (H : CochainComplex (PresheafOfModules.{max u v r w} R.obj) ℤ) (f : H ⟶ F),
            Mono f ∧ QuasiIso f ∧
              QuasiCoherentEquivalence.complexSectionSize.{w} R.obj H ≤
                max κ (QuasiCoherentEquivalence.derivedObjectSize.{w} R.obj K)
```

**`Stacks.ModulesOnACategory.exists_small_quasiIso_subcomplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallRepresentatives.lean, line 1232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallRepresentatives.lean#L1232).

> There is a cardinal, depending only on the category and its sheaf of rings, such that every
> representative of a derived object contains a quasi-isomorphic subcomplex bounded by that cardinal
> and the size of the derived object.

```lean
theorem exists_small_quasiIso_subcomplex :
    ∃ κ : Cardinal.{max u v m r},
      ∀ (F : CochainComplex (SheafOfModules.{m} R) ℤ)
        (K : DerivedCategory (SheafOfModules.{m} R)),
        Nonempty (DerivedCategory.Q.obj F ≅ K) →
          ∃ (H : CochainComplex (SheafOfModules.{m} R) ℤ) (f : H ⟶ F),
            Mono f ∧ QuasiIso f ∧
              complexSectionSize H ≤
                max κ (derivedObjectSize R K)
```

## Tag 0GYZ, a lemma

[Tag 0GYZ](https://stacks.math.columbia.edu/tag/0GYZ) in the Stacks Project.

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_cardinal_small_nonzero_map_and_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianEnlargementExists.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianEnlargementExists.lean#L269). The attribute's comment: “both conclusions, at one cardinal, for a presheaf of commutative rings”.

> **Stacks 0GYZ.** Let `C` be a category, regarded as a site with the chaotic topology, and let
> `O` be a presheaf of commutative rings on `C`. There is a cardinal `κ` such that
>
> 1. every nonzero object `K` of `QC(O)` receives a nonzero morphism from an object of `QC(O)` of
>    size at most `κ`, and
> 2. every morphism `α : E ⟶ ⨁_n K_n` of `QC(O)` with `|E| ≤ κ` factors through a morphism
>    `⨁_n E_n ⟶ ⨁_n K_n` induced by morphisms `E_n ⟶ K_n` of `QC(O)` with `|E_n| ≤ κ`.
>
> Conclusion (1) is `exists_nonzero_map_of_size_le_of_cartesianEnlargement` fed with
> `exists_hasCartesianEnlargement`. Conclusion (2) comes from its analogue for `D(O)`,
> `exists_factorization_of_sum_of_derivedObjectSize_le`, by replacing each of the summands it
> produces with a cartesian object of the same size bound, which is
> `exists_small_cartesian_factorization`.

```lean
theorem exists_cardinal_small_nonzero_map_and_factorization (bc : BaseChangeData.{w} O)
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x) :
    ∃ κ : Cardinal.{max u v r w},
      (∀ K : QC.{w} bc, ¬ IsZero K.obj →
          ∃ (E : QC.{w} bc) (f : E ⟶ K), f ≠ 0 ∧ derivedObjectSize.{w} O E.obj ≤ κ) ∧
        (∀ (E : QC.{w} bc) (K : ℕ → QC.{w} bc) (α : E.obj ⟶ ∐ fun n => (K n).obj),
          derivedObjectSize.{w} O E.obj ≤ κ →
          ∃ (E' : ℕ → QC.{w} bc) (f : ∀ n, E' n ⟶ K n)
            (β : E.obj ⟶ ∐ fun n => (E' n).obj),
            (∀ n, derivedObjectSize.{w} O (E' n).obj ≤ κ) ∧
              α = β ≫ Limits.Sigma.map fun n => (QCι.{w} bc).map (f n))
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_factorization_of_sum_of_derivedObjectSize_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallFactorizationThroughSums.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallFactorizationThroughSums.lean#L429). The attribute's comment: “part (2) for D(O) in place of QC(O): cartesianness dropped from the source and from the summands”.

> **Conclusion (2) of Stacks 0GYZ with the cartesianness demand dropped.** There is a cardinal
> `κ₀`, depending only on the category and its presheaf of rings, such that for every cardinal `κ`
> above it, every morphism from an object of `D(O)` of size at most `κ` into a countable direct sum
> factors through a direct sum of objects of size at most `κ` mapping to the summands.
>
> The conclusion is stated at every `κ ≥ κ₀` rather than at `κ₀` alone — which is the source's
> form, recovered by taking `κ = κ₀` — because the hypothesis and the conclusion both read `≤ κ`,
> so the property is monotone in neither direction and the form at a single cardinal cannot be
> combined with conclusion (1) at one cardinal, as Stacks 0GYZ asserts it is.

```lean
theorem exists_factorization_of_sum_of_derivedObjectSize_le :
    ∃ κ₀ : Cardinal.{max u v r w}, ∀ κ : Cardinal.{max u v r w}, κ₀ ≤ κ →
      ∀ (E : DMod.{w} O) (K : ℕ → DMod.{w} O) (α : E ⟶ ∐ K),
        derivedObjectSize.{w} O E ≤ κ →
        ∃ (E' : ℕ → DMod.{w} O) (f : ∀ n, E' n ⟶ K n) (β : E ⟶ ∐ E'),
          (∀ n, derivedObjectSize.{w} O (E' n) ≤ κ) ∧ α = β ≫ Limits.Sigma.map f
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_nonzero_map_of_derivedObjectSize_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallNonzeroMaps.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/SmallNonzeroMaps.lean#L330). The attribute's comment: “part (1) for D(O) in place of QC(O): cartesianness dropped from both objects”.

> **Every nonzero object of `D(O)` receives a nonzero morphism from an object of size at most
> `singleGeneratorBound O`.** This is the detection step of conclusion (1) of Stacks 0GYZ with the
> cartesianness demand dropped from both objects: the subcomplex produced by
> `exists_small_subcomplex_detecting_nonzero` is used as the source as it stands, with no
> enlargement.

```lean
theorem exists_nonzero_map_of_derivedObjectSize_le (K : DMod.{w} O) (hK : ¬ IsZero K) :
    ∃ (E : DMod.{w} O) (f : E ⟶ K),
      f ≠ 0 ∧ derivedObjectSize.{w} O E ≤ singleGeneratorBound.{w} O
```

## Tag 0GZ0, a proposition

[Tag 0GZ0](https://stacks.math.columbia.edu/tag/0GZ0) in the Stacks Project.

**`AlgebraicGeometry.exists_isTriangulated_rightAdjoint_smallAffineChaoticDerivedQuasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteBrownRepresentability.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineSiteBrownRepresentability.lean#L132). The attribute's comment: “part (3) on D\_QCoh(S\_affine, 𝒪) of an arbitrary scheme, through the equality of that subcategory with QC(S\_affine, 𝒪) which is the comparison (4) ≃ (5) of Stacks 0GZZ”.

> **[Stacks, Tag 0GZ0] part (3) on `D_QCoh(S_affine, 𝒪)`.** Let `S` be a scheme and let
> `(S_affine, 𝒪)` be its small affine Zariski site read with the chaotic topology. An exact functor
> `F : D_QCoh(S_affine, 𝒪) ⥤ D'` of triangulated categories which transforms direct sums into
> direct sums has a right adjoint `G`, which is again exact: the adjunction `F ⊣ G` is a
> triangulated adjunction for a `Functor.CommShift ℤ` structure on `G`.
>
> No hypothesis is carried: no compact generation, and no quasi-compactness or
> quasi-separatedness. The two inputs are [Stacks, Tag 0GZ0] part (3) for the cartesian objects,
> which is Brown representability without compact generation, and the identification of
> `D_QCoh(S_affine, 𝒪)` with `QC(S_affine, 𝒪)`, which is the comparison (4) ≃ (5) of
> [Stacks, Tag 0GZZ] in the sharp form
> `AlgebraicGeometry.smallAffineChaotic_isQC_eq_hasQuasicoherentCohomology`: on the chaotic site
> the two subcategories of `D(S_affine, 𝒪)` are equal, not merely equivalent.
>
> This is the abstract input of the Stacks proof of [Stacks, Tag 0A9E], but on the affine site;
> nothing here is a statement about `D_QCoh(𝒪_S)`, and Tag 0A9E does not follow. See the coverage
> note of this file.

```lean
theorem exists_isTriangulated_rightAdjoint_smallAffineChaoticDerivedQuasiCoherent
    {D' : Type u'} [Category.{max (u + 1) w} D'] [HasZeroObject D'] [Preadditive D']
    [HasShift D' ℤ] [∀ n : ℤ, (shiftFunctor D' n).Additive] [Pretriangulated D']
    (F : (qcohCohomologyProperty.{w} (smallAffineChaoticRingedSite B S hS)).FullSubcategory ⥤ D')
    [F.CommShift ℤ] [F.IsTriangulated]
    [∀ α : Type (max (u + 1) w), PreservesColimitsOfShape (Discrete α) F] :
    ∃ (G : D' ⥤
        (qcohCohomologyProperty.{w} (smallAffineChaoticRingedSite B S hS)).FullSubcategory)
      (adj : F ⊣ G) (_ : G.CommShift ℤ), adj.IsTriangulated
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_iso_preadditiveYoneda_of_isHomological_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean#L129). The attribute's comment: “part (2), for a presheaf of commutative rings”.

> **[Stacks, Tag 0GZ0] part (2).** Let `C` be a category with the chaotic topology, let `O` be a
> presheaf of commutative rings on `C` and let `bc` be derived base-change data for `O`. Every
> contravariant cohomological functor on `QC(O)` which transforms direct sums into products is
> representable.
>
> This is weak Brown representability [Stacks, Tag 0GYG] applied to the generating family
> `Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_small_generating_family`, which is
> [Stacks, Tag 0GYZ].

```lean
theorem exists_iso_preadditiveYoneda_of_isHomological_unconditional
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x)
    (H : (QC.{w} bc)ᵒᵖ ⥤ AddCommGrpCat.{max u v r w}) [H.IsHomological]
    [∀ J : Type (max u v r w), PreservesLimitsOfShape (Discrete J) H] :
    ∃ K : QC.{w} bc, Nonempty (preadditiveYoneda.obj K ≅ H)
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_isTriangulated_rightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean#L148). The attribute's comment: “part (3), for a presheaf of commutative rings”.

> **[Stacks, Tag 0GZ0] part (3).** Let `C` be a category with the chaotic topology, let `O` be a
> presheaf of commutative rings on `C` and let `bc` be derived base-change data for `O`. An exact
> functor `F : QC(O) ⥤ D'` of triangulated categories which transforms direct sums into direct sums
> has a right adjoint `G`, which is again exact: the adjunction `F ⊣ G` is a triangulated adjunction
> for a `Functor.CommShift ℤ` structure on `G`.
>
> This is Brown representability in the form [Stacks, Tag 0GYH] applied to the generating family
> `Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_small_generating_family`, which is
> [Stacks, Tag 0GYZ].

```lean
theorem exists_isTriangulated_rightAdjoint
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x)
    {D' : Type u'} [Category.{max u v r w} D'] [HasZeroObject D'] [Preadditive D']
    [HasShift D' ℤ] [∀ n : ℤ, (shiftFunctor D' n).Additive] [Pretriangulated D']
    (F : QC.{w} bc ⥤ D') [F.CommShift ℤ] [F.IsTriangulated]
    [∀ α : Type (max u v r w), PreservesColimitsOfShape (Discrete α) F] :
    ∃ (G : D' ⥤ QC.{w} bc) (adj : F ⊣ G) (_ : G.CommShift ℤ), adj.IsTriangulated
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_isTriangulated_rightAdjoint_QCι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/BrownRepresentabilityUnconditional.lean#L166). The attribute's comment: “part (4), for a presheaf of commutative rings”.

> **[Stacks, Tag 0GZ0] part (4).** The inclusion `QC(O) ⥤ D(O)` of the cartesian objects has an
> exact right adjoint. The inclusion is exact and transforms direct sums into direct sums, because
> `QC(O)` is a triangulated subcategory closed under direct sums ([Stacks, Tag 0GYW]), so this is the
> special case `F = QCι` of
> `Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_isTriangulated_rightAdjoint`.

```lean
theorem exists_isTriangulated_rightAdjoint_QCι
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x) :
    ∃ (G : DMod.{w} O ⥤ QC.{w} bc) (adj : QCι.{w} bc ⊣ G) (_ : G.CommShift ℤ),
      adj.IsTriangulated
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_iso_preadditiveYoneda_of_isHomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean#L201). The attribute's comment: “part (2); part (1) is on the covering set of 0GYW, parts (3) and (4) below”.

> **Stacks 0GZ0, assertion (2).** Let `C` be a category, regarded as a site with the chaotic
> topology, and let `O` be a presheaf of commutative rings on `C`. Every contravariant
> cohomological functor on `QC(O)` which transforms direct sums into products is representable.
>
> This is weak Brown representability (Stacks 0GYG) applied to the generating family of
> `exists_qc_generating_family`, which is Stacks 0GYZ.

```lean
theorem exists_iso_preadditiveYoneda_of_isHomological (bc : BaseChangeData.{w} O)
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x)
    (H : (QC.{w} bc)ᵒᵖ ⥤ AddCommGrpCat.{max u v r w}) [H.IsHomological]
    [∀ J : Type (max u v r w), PreservesLimitsOfShape (Discrete J) H] :
    ∃ K : QC.{w} bc, Nonempty (preadditiveYoneda.obj K ≅ H)
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_isTriangulated_rightAdjoint_of_preservesCoproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean#L227). The attribute's comment: “part (3); part (1) is on the covering set of 0GYW, part (2) above, part (4) below”.

> **Stacks 0GZ0, assertion (3).** Let `C` be a category, regarded as a site with the chaotic
> topology, and let `O` be a presheaf of commutative rings on `C`. Every exact functor
> `F : QC(O) ⥤ D` of triangulated categories which transforms direct sums into direct sums has a
> right adjoint `G`, and `G` is again exact: the adjunction `F ⊣ G` is triangulated for a (unique)
> `Functor.CommShift ℤ` structure on `G`.
>
> This is Stacks 0GYH applied to the generating family of `exists_qc_generating_family`, which is
> Stacks 0GYZ.

```lean
theorem exists_isTriangulated_rightAdjoint_of_preservesCoproducts (bc : BaseChangeData.{w} O)
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x)
    (F : QC.{w} bc ⥤ D) [F.CommShift ℤ] [F.IsTriangulated]
    [∀ α : Type (max u v r w), PreservesColimitsOfShape (Discrete α) F] :
    ∃ (G : D ⥤ QC.{w} bc) (adj : F ⊣ G) (_ : G.CommShift ℤ), adj.IsTriangulated
```

**`Stacks.ModulesOnACategory.QuasiCoherentEquivalence.exists_isTriangulated_rightAdjoint_qcι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianBrownRepresentability.lean#L246). The attribute's comment: “part (4); part (1) is on the covering set of 0GYW, parts (2) and (3) above”.

> **Stacks 0GZ0, assertion (4).** Let `C` be a category, regarded as a site with the chaotic
> topology, and let `O` be a presheaf of commutative rings on `C`. The inclusion
> `QC(O) ⥤ D(O)` has an exact right adjoint.
>
> This is assertion (3) at the inclusion functor: the inclusion is exact and transforms direct sums
> into direct sums, `QC(O)` being a triangulated subcategory of `D(O)` closed under arbitrary direct
> sums (Stacks 0GYW), so that the inclusion creates them.

```lean
theorem exists_isTriangulated_rightAdjoint_qcι (bc : BaseChangeData.{w} O)
    (hO : ∀ (V : Cᵒᵖ) (x y : O.obj V), x * y = y * x) :
    ∃ (G : DMod.{w} O ⥤ QC.{w} bc) (adj : QCι.{w} bc ⊣ G) (_ : G.CommShift ℤ),
      adj.IsTriangulated
```

Declarations registered for the tag:

- [`isCartesian_isClosedUnderIsomorphisms`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCartesian_isClosedUnderIsomorphisms#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L244) (StacksFrontier): “subcategory”.
- [`isCartesian_isSaturated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCartesian_isSaturated#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L245) (StacksFrontier): “subcategory”.
- [`isCartesian_isTriangulated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCartesian_isTriangulated#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L246) (StacksFrontier): “subcategory”.
- [`isCartesian_isClosedUnderCoproducts_of_smallSite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isCartesian_isClosedUnderCoproducts_of_smallSite#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/CartesianObjectsTriangulatedSubcategory.lean#L247) (StacksFrontier): “subcategory”.

## Tag 0GZ1, a lemma

[Tag 0GZ1](https://stacks.math.columbia.edu/tag/0GZ1) in the Stacks Project.

**`Stacks.ModulesOnACategory.PullbackPreservesQuasiCoherent.isQC_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/DerivedPullbackOfModules/RestrictionMaps.lean, line 705](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/DerivedPullbackOfModules/RestrictionMaps.lean#L705). The attribute's comment: “Lg^* carries QC(O) into QC(O'), for the derived pullback constructed here”.

> **Derived pullback along a morphism of ringed topoi on chaotic sites carries cartesian
> objects to cartesian objects.** If the derived sections of `K` are cartesian then so are the
> derived sections of `Lg^*K`, the cartesian condition on either side being taken with respect to
> the derived base changes along the restriction homomorphisms of the structure sheaf there.

```lean
theorem isQC_derivedPullback (K : DMod.{max u' v'} O)
    (hK : IsQC.{max u' v'}
      (PullbackQuasiCoherentBaseChange.baseChangeDataOfComm.{r, v, u, max u' v'} O hO) K) :
    IsQC.{max u v}
      (PullbackQuasiCoherentBaseChange.baseChangeDataOfComm.{r, v', u', max u v} O' hO')
      ((derivedPullback F O O' φ).obj K)
```

**`Stacks.ModulesOnACategory.PullbackQuasiCoherentBaseChange.isQC_Lpullback_of_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/PullbackQuasiCoherentBaseChange.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/PullbackQuasiCoherentBaseChange.lean#L213). The attribute's comment: “pullback of cartesian objects, for a derived pullback with its sections”.

> **Stacks 0GZ1.** **Derived pullback along a morphism of ringed topoi carries cartesian
> objects to cartesian objects.** If the derived sections of `K` are cartesian then so are the
> derived sections of `Lg^*K`, the cartesian condition on either side being taken with respect to
> the derived base changes along the restriction homomorphisms of the structure sheaf there.
>
> The derived pullback is supplied as data, together with the computation of its derived sections
> of Stacks 0D6D, in the same way that
> `Stacks.ModulesOnACategory.QuasiCoherentEquivalence.MorphismOfSites` supplies it for the
> statements of Stacks 0H0R and 0H0S.

```lean
theorem isQC_Lpullback_of_comm
    (d : DerivedPullbackData (structureBaseChange F O O' φ hO hO')
      (baseChangeDataOfComm.{r, v, u, max u' v'} O hO)
      (baseChangeDataOfComm.{r, v', u', max u v} O' hO'))
    (K : DMod.{max u' v'} O)
    (hK : IsQC.{max u' v'} (baseChangeDataOfComm.{r, v, u, max u' v'} O hO) K) :
    IsQC.{max u v} (baseChangeDataOfComm.{r, v', u', max u v} O' hO') (d.Lpullback.obj K)
```

## Tag 0GZR, a lemma

[Tag 0GZR](https://stacks.math.columbia.edu/tag/0GZR) in the Stacks Project.

**`Stacks.ModulesOnACategory.QuasiCoherentCohomology.isQC_iff_hasQuasicoherentCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/QuasiCoherentCohomologyUnderFlatRestrictions.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/QuasiCoherentCohomologyUnderFlatRestrictions.lean#L301).

> **Quasi-coherent cohomology under flat restrictions.** Let `C` be a category viewed as a
> site with the chaotic topology, let `O` be its sheaf of rings, and assume that for every
> morphism `U → V` of `C` the restriction homomorphism `O(V) → O(U)` is flat.  Then an object of
> `D(O)` lies in `QC(O)` exactly when all of its cohomology sheaves are quasi-coherent, that is,
> `QC(O) = D_QCoh(O)`.

```lean
theorem isQC_iff_hasQuasicoherentCohomology (X : RingedSite.{u, v, r}) (hX : X.J = ⊥)
    (hflat : ∀ {U V : X.Cᵒᵖ} (a : V ⟶ U), RingHom.Flat (X.O.obj.map a).hom)
    (bc : BaseChangeData.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)
    (K : DMod.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj) :
    IsQC.{w} bc K ↔ hasQuasicoherentCohomology.{w} X K
```

## Tag 0GZS, a lemma

[Tag 0GZS](https://stacks.math.columbia.edu/tag/0GZS) in the Stacks Project.

**`Stacks.ModulesOnACategory.ChaoticComparison.cartesianEquivalenceOfLocallyKFlatAcyclic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticComparisonUnitSquare.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticComparisonUnitSquare.lean#L425).

> Let `C` carry a Grothendieck topology `τ`, let `τ'` be the chaotic topology on `C` and let `O`
> be a `τ`-sheaf of rings with commuting sections. Assume hypothesis (2) of the source: for every
> object `U` of `C` and every K-flat complex `M^•` of `O(U)`-modules the canonical map
> `M^• ⟶ RΓ((C/U)_τ, (M^• ⊗_{O(U)} O_U)^#)` is a quasi-isomorphism. Then `ε^*` and `Rε_*` are
> mutually quasi-inverse equivalences between `QC(O)` and the full subcategory of `D(C_τ, O_τ)`
> consisting of the objects `K` with `Rε_*K` in `QC(O)`.
>
> Hypothesis (1) of the source, that `τ'` is the chaotic topology, is structural here: a module on
> `(C_τ', O_τ')` *is* a presheaf of `O`-modules, `ε_*` is the forgetful functor and `ε^*` is
> `τ`-sheafification. Hypothesis (2) is `IsLocallyKFlatAcyclic`, read on the localized site
> `(C/U, τ)`. The commutativity `hO` gives the canonical base-change datum
> `Stacks.ModulesOnACategory.PullbackQuasiCoherentBaseChange.baseChangeDataOfComm`; the cartesian
> condition does not depend on the choice of datum.
>
> The objects and the morphisms of `C` and the section rings lie in independent universes `u`, `v`
> and `r`, and the modules in `max u v r w`; the site therefore need not be small, as is the case
> for the associated affine site of a category fibred in groupoids (Stacks 0H0J).

```lean
def cartesianEquivalenceOfLocallyKFlatAcyclic (h2 : IsLocallyKFlatAcyclic.{w} R hO) :
    (IsCartesianPushforward.{w} R
          (baseChangeDataOfComm.{r, v, u, w} R.obj hO)).FullSubcategory ≌
      QC.{w} (baseChangeDataOfComm.{r, v, u, w} R.obj hO)
```

## Tag 0H0T, a lemma

[Tag 0H0T](https://stacks.math.columbia.edu/tag/0H0T) in the Stacks Project.

**`Stacks.ModulesOnACategory.ChaoticComparison.homEpsilonPullback_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticComparisonOnCartesianObjects.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ModulesOnACategory/ChaoticComparisonOnCartesianObjects.lean#L197). The attribute's comment: “morphisms out of a sheafified cartesian object are maps of derived sections over U”.

> Let `K` be an object of `QC(O)` and let `M` be an arbitrary object of `D((O_U)_τ)`.
> Transposing under the adjunction `ε^* ⊣ Rε_*` over `C/U` and then taking derived sections over the
> terminal object `id_U` of `C/U` identifies the morphisms `ε^*(K|_U) ⟶ M` of `D((O_U)_τ)` with the
> morphisms `RΓ(U, K) ⟶ RΓ(U, Rε_*M)` of `D(O(U))`.

```lean
theorem homEpsilonPullback_bijective
    (hO : ∀ (V : Cᵒᵖ) (x y : R.obj.obj V), x * y = y * x)
    (K : DMod.{w} R.obj)
    (hK : IsQC.{w} (baseChangeDataOfComm.{r, v, u, w} R.obj hO) K)
    (M : DerivedCategory (SheafOfModules.{max u v r w} (overRingSheaf R U))) :
    Function.Bijective (fun f : (epsilonPullback.{w} (overRingSheaf R U)).mapDerivedCategory.obj
        ((derivedRestriction.{w} R.obj U).obj K) ⟶ M =>
      ((derivedSectionsIso.{w} R.obj U).app K).inv ≫
        (RGamma.{w} (overRingPresheaf R.obj U) (Opposite.op (Over.mk (𝟙 U)))).map
          ((derivedEpsilonAdjunction.{w} (overRingSheaf R U)).unit.app
              ((derivedRestriction.{w} R.obj U).obj K) ≫
            (derivedEpsilonPushforward.{w} (overRingSheaf R U)).map f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.43, Tag 0GYU](https://stacks.math.columbia.edu/tag/0GYU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
