---
declaration: section
origin: cited
lean: Stacks.Sheaves.RingedSpaceCotangent.cotangentComplex, Stacks.Sheaves.RingedSpaceCotangent.cotangentComplexDerived, Stacks.Sheaves.RingedSpaceCotangent.cotangentComplex_homologyZeroIso, Stacks.Sheaves.RingedSpaceCotangent.baseStructureMap_comp, Stacks.Sheaves.RingedSpaceCotangent.cotangentChangeOfBase, Stacks.Sheaves.RingedSpaceCotangent.exists_distTriang_of_shortExact, Stacks.Sheaves.RingedSpaceCotangent.exists_distTriang_degreewisePullback_of_shortExact, Stacks.Sheaves.RingedSpaceCotangent.sheafPullbackCompIso_hom_app_comp_inverseImageStructureMap
statement: formalized
proof: formalized
---

# 92.20 The cotangent complex of a morphism of ringed spaces

Section 92.20 of the Stacks Project, [Tag 08UT](https://stacks.math.columbia.edu/tag/08UT). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08UU, a definition

[Tag 08UU](https://stacks.math.columbia.edu/tag/08UU) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceCotangent.cotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean#L90). The attribute's comment: “the complex L\_f”.

> The cotangent complex `L_{X/S}` of a morphism of ringed spaces `f : X ⟶ S`: the cotangent
> complex of the morphism of sheaves of commutative rings `f⁻¹𝒪_S ⟶ 𝒪_X` on the site of open
> subsets of `X`.

```lean
noncomputable def cotangentComplex (f : X ⟶ S) :
    CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ
```

**`Stacks.Sheaves.RingedSpaceCotangent.cotangentComplexDerived`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean#L103). The attribute's comment: “the object L\_f of the derived category of O\_X-modules”.

> `L_{X/S}` regarded as an object of the derived category of sheaves of `𝒪_X`-modules.

```lean
noncomputable abbrev cotangentComplexDerived (f : X ⟶ S)
    [HasDerivedCategory.{t} (SheafOfModules.{u} (structureSheafRing X))] :
    DerivedCategory (SheafOfModules.{u} (structureSheafRing X))
```

## Tag 08UV, a lemma

[Tag 08UV](https://stacks.math.columbia.edu/tag/08UV) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceCotangent.cotangentComplex_homologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpace.lean#L127).

> **Stacks 08UV.** The zeroth cohomology of the cotangent complex of a morphism of ringed
> spaces `f : (X, 𝒪_X) ⟶ (S, 𝒪_S)` is its sheaf of relative differentials:
> `H⁰(L_{X/S}) ≅ Ω_{X/S}`. Both sheaves of `𝒪_X`-modules corepresent the relative derivations of
> `𝒪_X` over `f⁻¹𝒪_S`, so they are canonically isomorphic.

```lean
noncomputable def cotangentComplex_homologyZeroIso (f : X ⟶ S) :
    (cotangentComplex f).homology 0 ≅ moduleOfDifferentials f
```

## Tag 08T4, a lemma

[Tag 08T4](https://stacks.math.columbia.edu/tag/08T4) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceCotangent.baseStructureMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean#L165). The attribute's comment: “the canonical tower of inverse images, whose fundamental triangle is the triangle of this tag”.

> **Stacks Project, Tag 08T4**, the tower. The structure map of `g ∘ f` factors through the
> structure map of `f` by `baseStructureMap`, so that `(g ∘ f)⁻¹𝒪_Z ⟶ f⁻¹𝒪_Y ⟶ 𝒪_X` is a tower
> of sheaves of commutative rings on `X` whose composite is the structure map of `g ∘ f`.

```lean
theorem baseStructureMap_comp (f : X ⟶ Y) (g : Y ⟶ Z) :
    baseStructureMap f g ≫ inverseImageStructureMap f = inverseImageStructureMap (f ≫ g)
```

**`Stacks.Sheaves.RingedSpaceCotangent.cotangentChangeOfBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean#L221). The attribute's comment: “the second displayed arrow L\_\{X/Z} ⟶ L\_\{X/Y}, unconditionally. Distinguishedness of the triangle is not claimed by this declaration”.

> **Stacks Project, Tag 08T4**, the second displayed arrow `L_{X/Z} ⟶ L_{X/Y}`: the
> change-of-base-ring map of Tag 08SZ for the tower `(g ∘ f)⁻¹𝒪_Z ⟶ f⁻¹𝒪_Y ⟶ 𝒪_X`.

```lean
def cotangentChangeOfBase (f : X ⟶ Y) (g : Y ⟶ Z) :
    (cotangentComplex (f ≫ g) : CochainComplex (structureModules X) ℤ) ⟶
      cotangentComplex f
```

**`Stacks.Sheaves.RingedSpaceCotangent.exists_distTriang_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean#L285). The attribute's comment: “the triangle with FIRST VERTEX THE DEGREEWISE base change L\_\{f⁻¹O\_Y/(g∘f)⁻¹O\_Z} ⊗\_\{f⁻¹O\_Y} O\_X, not Lf^* L\_\{Y/Z}, and under the ONE carried hypothesis of Tag 08SZ: the short exact sequence `S`/`hS`, the sheaf-level analogue of Tag 08SD, absent from this library. See the docstring above”.

> **Stacks Project, Tag 08T4, under one carried hypothesis.** For morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the triangle
>
> `L_{f⁻¹𝒪_Y/(g ∘ f)⁻¹𝒪_Z} ⊗_{f⁻¹𝒪_Y} 𝒪_X ⟶ L_{X/Z} ⟶ L_{X/Y} ⟶ ⋯`
>
> on the two canonical arrows `cotangentBaseChange` and `cotangentChangeOfBase` is distinguished
> in `D(𝒪_X)`.
>
> The hypothesis carried is the one carried by Tag 08SZ, in the same shape: a short complex `S`
> of complexes of sheaves of `𝒪_X`-modules that is short exact (`hS`), whose three terms are the
> three vertices (`e₁`, `e₂`, `e₃`) and whose two maps are the two canonical arrows (`hf`, `hg`).
> See the "What is proved and what is not" section of the module documentation.

```lean
theorem exists_distTriang_of_shortExact (f : X ⟶ Y) (g : Y ⟶ Z)
    (S : ShortComplex (CochainComplex (structureModules X) ℤ))
    (hS : S.ShortExact) (e₁ : S.X₁ ≅ baseChangedCotangentComplex f g)
    (e₂ : S.X₂ ≅ cotangentComplex (f ≫ g)) (e₃ : S.X₃ ≅ cotangentComplex f)
    (hf : S.f = e₁.hom ≫ cotangentBaseChange f g ≫ e₂.inv)
    (hg : S.g = e₂.hom ≫ cotangentChangeOfBase f g ≫ e₃.inv) :
    ∃ δ : (DerivedCategory.Q (C := structureModules X)).obj (cotangentComplex f) ⟶
        ((DerivedCategory.Q (C := structureModules X)).obj
          (baseChangedCotangentComplex f g))⟦(1 : ℤ)⟧,
      Triangle.mk ((DerivedCategory.Q (C := structureModules X)).map (cotangentBaseChange f g))
          ((DerivedCategory.Q (C := structureModules X)).map (cotangentChangeOfBase f g)) δ ∈
        distTriang (DerivedCategory (structureModules X))
```

**`Stacks.Sheaves.RingedSpaceCotangent.exists_distTriang_degreewisePullback_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceFundamentalTriangle.lean#L325). The attribute's comment: “the triangle with first vertex the DEGREEWISE pullback f^* L\_\{Y/Z}, not Lf^* L\_\{Y/Z}; the two agree in D(O\_X) exactly when L\_\{Y/Z} is K-flat, which is NOT proved here. TWO carried hypotheses: `e` is Tag 08SV for this tower, `S`/`hS` is what Tag 08SZ carries. See the docstring above and the module documentation”.

> **Stacks Project, Tag 08T4, under two carried hypotheses.** For morphisms of ringed spaces
> `f : X ⟶ Y` and `g : Y ⟶ Z` the triangle
>
> `f^*L_{Y/Z} ⟶ L_{X/Z} ⟶ L_{X/Y} ⟶ f^*L_{Y/Z}[1]`
>
> is distinguished in `D(𝒪_X)`, its first arrow being the base-change arrow of Tag 08SZ for the
> tower read on `f^*L_{Y/Z}` and its second the canonical map `cotangentChangeOfBase`.
>
> Two hypotheses are carried. `e` is Tag 08SV for the tower: the degreewise pullback of `L_{Y/Z}`
> is the first vertex `L_{f⁻¹𝒪_Y/(g ∘ f)⁻¹𝒪_Z} ⊗_{f⁻¹𝒪_Y} 𝒪_X` of the triangle of Tag 08SZ. The
> short exact sequence `S`, `hS` is the hypothesis Tag 08SZ itself carries. The first vertex is
> the degreewise pullback `f^*L_{Y/Z}`; it is `Lf^*L_{Y/Z}` as soon as `L_{Y/Z}` is K-flat, by
> `isIso_derivedPullbackComparison_cotangentComplex`. See the "What is proved and what is not"
> section of the module documentation.

```lean
theorem exists_distTriang_degreewisePullback_of_shortExact (f : X ⟶ Y) (g : Y ⟶ Z)
    (e : degreewisePullbackCotangentComplex f g ≅ baseChangedCotangentComplex f g)
    (S : ShortComplex (CochainComplex (structureModules X) ℤ))
    (hS : S.ShortExact) (e₁ : S.X₁ ≅ baseChangedCotangentComplex f g)
    (e₂ : S.X₂ ≅ cotangentComplex (f ≫ g)) (e₃ : S.X₃ ≅ cotangentComplex f)
    (hf : S.f = e₁.hom ≫ cotangentBaseChange f g ≫ e₂.inv)
    (hg : S.g = e₂.hom ≫ cotangentChangeOfBase f g ≫ e₃.inv) :
    ∃ δ : (DerivedCategory.Q (C := structureModules X)).obj (cotangentComplex f) ⟶
        ((DerivedCategory.Q (C := structureModules X)).obj
          (degreewisePullbackCotangentComplex f g))⟦(1 : ℤ)⟧,
      Triangle.mk ((DerivedCategory.Q (C := structureModules X)).map
            (e.hom ≫ cotangentBaseChange f g))
          ((DerivedCategory.Q (C := structureModules X)).map (cotangentChangeOfBase f g)) δ ∈
        distTriang (DerivedCategory (structureModules X))
```

**`Stacks.Sheaves.RingedSpaceCotangent.sheafPullbackCompIso_hom_app_comp_inverseImageStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean#L133). The attribute's comment: “the tower (g ∘ f)⁻¹O\_Z = f⁻¹g⁻¹O\_Z ⟶ f⁻¹O\_Y ⟶ O\_X of the proof: the structure map of g ∘ f is the composite of the tower”.

> The structure map of `g ∘ f` is the structure map of `g` pulled back along `f` followed by
> the structure map of `f`, across `(g ∘ f)⁻¹𝒪_Z ≅ f⁻¹g⁻¹𝒪_Z` (Tag 008I).

```lean
theorem sheafPullbackCompIso_hom_app_comp_inverseImageStructureMap (f : X ⟶ Y) (g : Y ⟶ Z) :
    (sheafPullbackCompIso f.hom.base g.hom.base CommRingCat.{u}).hom.app Z.sheaf ≫
        (TopCat.Sheaf.pullback CommRingCat.{u} f.hom.base).map (inverseImageStructureMap g) ≫
          inverseImageStructureMap f =
      inverseImageStructureMap (f ≫ g)
```

**`Stacks.Sheaves.RingedSpaceCotangent.transitivityUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean#L330). The attribute's comment: “the canonical first arrow Lf^* L\_\{Y/Z} ⟶ L\_\{X/Z} of the triangle”.

> The first arrow `Lf^* L_{Y/Z} ⟶ L_{X/Z}` of the transitivity triangle: the first arrow of
> the triangle of Tag 08V1 for the presented morphisms of ringed topoi, read through
> `derivedPullbackCotangentComplexIso` and `compCotangentComplexIsoRingedTopos`.

```lean
def transitivityUnit (f : X ⟶ Y) (g : Y ⟶ Z) :
    (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj
        (cotangentComplexDerived g) ⟶ cotangentComplexDerived (f ≫ g)
```

**`Stacks.Sheaves.RingedSpaceCotangent.transitivityCounit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean#L342). The attribute's comment: “the canonical second arrow L\_\{X/Z} ⟶ L\_\{X/Y} of the triangle”.

> The second arrow `L_{X/Z} ⟶ L_{X/Y}` of the transitivity triangle: the second arrow of the
> triangle of Tag 08V1 for the presented morphisms of ringed topoi, read through
> `compCotangentComplexIsoRingedTopos` and `cotangentComplexIsoRingedTopos`.

```lean
def transitivityCounit (f : X ⟶ Y) (g : Y ⟶ Z) :
    cotangentComplexDerived (f ≫ g) ⟶ cotangentComplexDerived f
```

**`Stacks.Sheaves.RingedSpaceCotangent.exists_distTriang_transitivity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceTransitivityTriangle.lean#L359).

> **The transitivity triangle.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of ringed
> spaces. The canonical triangle
>
> `Lf^* L_{Y/Z} ⟶ L_{X/Z} ⟶ L_{X/Y} ⟶ Lf^* L_{Y/Z}[1]`
>
> is distinguished in `D(𝒪_X)`. Here `L_{X/S}` is the cotangent complex of Definition 08UU,
> `Lf^*` is the derived pullback of Tag 06YJ, and the two arrows are `transitivityUnit` and
> `transitivityCounit`, those of the fundamental triangle of the tower
> `(g ∘ f)⁻¹𝒪_Z = f⁻¹g⁻¹𝒪_Z ⟶ f⁻¹𝒪_Y ⟶ 𝒪_X` (Tags 08SZ and 08V1).

```lean
theorem exists_distTriang_transitivity (f : X ⟶ Y) (g : Y ⟶ Z) :
    ∃ δ : cotangentComplexDerived f ⟶
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj
          (cotangentComplexDerived g))⟦(1 : ℤ)⟧,
      Triangle.mk (transitivityUnit f g) (transitivityCounit f g) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
```

## Tag 08UW, a lemma

[Tag 08UW](https://stacks.math.columbia.edu/tag/08UW) in the Stacks Project.

**`Stacks.Sheaves.RingedSpaceCotangent.canonicalNaiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceCanonicalNaiveComparison.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceCanonicalNaiveComparison.lean#L62). The attribute's comment: “the canonical map `L_{X/Y} → NL_{X/Y}`, into the naive cotangent complex `AlgebraicGeometry.RingedSpace.naiveCotangentComplex` of Tag 08TN; the special case of the map of Tag 08US”.

> The canonical map `L_{X/S} ⟶ NL_{X/S}` from the cotangent complex of a morphism of ringed
> spaces to its naive cotangent complex `AlgebraicGeometry.RingedSpace.naiveCotangentComplex`: the
> canonical map `CategoryTheory.Sheaf.canonicalNaiveComparison` for the morphism of sheaves of
> rings `f⁻¹𝒪_S ⟶ 𝒪_X`.

```lean
noncomputable def canonicalNaiveComparison (f : X ⟶ S) :
    cotangentComplex f ⟶ RingedSpace.naiveCotangentComplex f
```

**`Stacks.Sheaves.RingedSpaceCotangent.canonicalNaiveComparison_isIso_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceCanonicalNaiveComparison.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceCanonicalNaiveComparison.lean#L75). The attribute's comment: “the canonical map identifies the naive cotangent complex `NL_{X/Y}` with the truncation `τ_{≥ -1} L_{X/Y}`: it is an isomorphism on the cohomology sheaf of every degree `≥ -1`, the naive complex having no terms outside degrees `-1` and `0`; the special case of Tag 08US”.

> The canonical map `L_{X/S} ⟶ NL_{X/S}` is an isomorphism on the cohomology sheaf of every
> degree `≥ -1`. Since `NL_{X/S}` has no terms outside degrees `-1` and `0`
> (`AlgebraicGeometry.RingedSpace.naiveCotangentComplex_isZero_X`), the canonical map identifies
> the naive cotangent complex with the truncation `τ_{≥ -1} L_{X/S}`.

```lean
theorem canonicalNaiveComparison_isIso_homologyMap (f : X ⟶ S) (i : ℤ) (hi : -1 ≤ i) :
    IsIso (HomologicalComplex.homologyMap (canonicalNaiveComparison f) i)
```

**`Stacks.Sheaves.RingedSpaceCotangent.naiveComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean#L116). The attribute's comment: “the canonical map `L_{X/Y} → NL_{X/Y}` as a morphism of cochain complexes of sheaves of `O_X`-modules, with both of its components pinned by the lemmas below. Hypotheses beyond the source: `NL_{X/Y}` is realized as the two-term complex of the conormal sequence of the presentation `P₀ ⟶ O_X` by the degree-zero term of the standard resolution, whose free algebra is spelled by `CategoryTheory.Sheaf.freeAlgebraSheaf`; the identification of that model with the one of `AlgebraicGeometry.RingedSpace.naiveCotangentComplex` is not carried. The second half of the tag, that this map identifies the naive cotangent complex with the truncation `tau_{>=-1} L_{X/Y}`, is NOT proved and is nowhere assumed”.

> The canonical chain map `L_{X/S} ⟶ NL_{X/S}` of a morphism of ringed spaces:
> `CategoryTheory.Sheaf.naiveComparison` at the morphism of sheaves of rings `f⁻¹𝒪_S ⟶ 𝒪_X`.

```lean
noncomputable def naiveComparison (f : X ⟶ S) :
    cotangentComplex f ⟶ naivePresentationComplex f
```

**`Stacks.Sheaves.RingedSpaceCotangent.naiveComparison_f_negOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean#L127). The attribute's comment: “the degree `-1` component of the canonical map is the comparison arrow `Omega_{P_1} ⊗ O_X → I/I²`, so the map is the canonical one. Same hypotheses as `Stacks.Sheaves.RingedSpaceCotangent.naiveComparison`”.

> The degree `-1` component of the canonical map is the comparison arrow
> `CategoryTheory.Sheaf.naiveComparisonNegOne` for the morphism of sheaves of rings
> `f⁻¹𝒪_S ⟶ 𝒪_X`.

```lean
theorem naiveComparison_f_negOne (f : X ⟶ S) :
    (naiveComparison f).f (-1) ≫ (naivePresentationComplexXNegOneIso f).hom =
      (CategoryTheory.Sheaf.cotangentComplex_degreeIso (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f) 1).hom ≫
        CategoryTheory.Sheaf.naiveComparisonNegOne (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f)
```

**`Stacks.Sheaves.RingedSpaceCotangent.naiveComparison_f_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean#L142). The attribute's comment: “the degree `0` component of the canonical map is the comparison arrow `Omega_{P_0} ⊗ O_X → O_X ⊗ Omega_{P_0}`, so the map is the canonical one. Same hypotheses as `Stacks.Sheaves.RingedSpaceCotangent.naiveComparison`”.

> The degree `0` component of the canonical map is the comparison arrow
> `CategoryTheory.Sheaf.naiveComparisonZero` for the morphism of sheaves of rings `f⁻¹𝒪_S ⟶ 𝒪_X`.

```lean
theorem naiveComparison_f_zero (f : X ⟶ S) :
    (naiveComparison f).f 0 ≫ (naivePresentationComplexXZeroIso f).hom =
      (CategoryTheory.Sheaf.cotangentComplex_degreeIso (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f) 0).hom ≫
        CategoryTheory.Sheaf.naiveComparisonZero (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f)
```

**`Stacks.Sheaves.RingedSpaceCotangent.naiveComparison_f_negOne_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparison.lean#L162). The attribute's comment: “the value of the canonical map on local sections in degree `-1`: the pure differential `d x` goes to the class of `d_0 x - d_1 x` in `I/I²`. Same hypotheses as `Stacks.Sheaves.RingedSpaceCotangent.naiveComparison`”.

> On local sections over an open `U` the degree `-1` component of the canonical map sends the
> pure differential `d x` of a section `x` of `P₁` to the class of `d₀ x - d₁ x` in `I/I²`.

```lean
theorem naiveComparison_f_negOne_apply (f : X ⟶ S) (U : (Opens X.carrier)ᵒᵖ)
    (x : (CategoryTheory.Sheaf.resolutionTerm (Opens.grothendieckTopology X.carrier)
      (inverseImageStructureMap f) (op ⦋1⦌)).obj.obj U) :
    ((CategoryTheory.Sheaf.cotangentComplex_degreeIso (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f) 1).inv ≫ (naiveComparison f).f (-1) ≫
        (naivePresentationComplexXNegOneIso f).hom).val.app U
        (((CategoryTheory.Sheaf.cotangentSimplicialModule
          (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f)).universalDerivation (op ⦋1⦌)).d x) =
      CategoryTheory.Sheaf.conormalClassSection (Opens.grothendieckTopology X.carrier)
        (inverseImageStructureMap f) U
        (CategoryTheory.Sheaf.faceDifference (Opens.grothendieckTopology X.carrier)
          (inverseImageStructureMap f) U x)
```

**`Stacks.Sheaves.RingedSpaceCotangent.isIso_homologyMap_naiveComparison_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparisonHomologyZero.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/RingedSpaceNaiveComparisonHomologyZero.lean#L44). The attribute's comment: “the degree-zero clause of the second assertion: the canonical map `L_{X/Y} → NL_{X/Y}` is an isomorphism on the degree-zero cohomology sheaf, both sides being `Omega_{X/Y}`. `NL_{X/Y}` is realized as the two-term complex of the conormal sequence of the presentation `P₀ ⟶ O_X` by the degree-zero term of the standard resolution, as for `Stacks.Sheaves.RingedSpaceCotangent.naiveComparison`”.

> The canonical map `L_{X/S} ⟶ NL_{X/S}` is an isomorphism on the degree-zero cohomology
> sheaf, both sides being the sheaf of relative differentials `Ω_{X/S}`.

```lean
theorem isIso_homologyMap_naiveComparison_zero (f : X ⟶ S) :
    IsIso (HomologicalComplex.homologyMap (naiveComparison f) 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.20, Tag 08UT](https://stacks.math.columbia.edu/tag/08UT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
