---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_affine_isSurjective_isEtale_of_isQuasiCompactSpace, AlgebraicGeometry.Space.ResolutionPropertyDescentSituation, AlgebraicGeometry.Space.exists_epi_biproduct_idealSheafPowPushforward, AlgebraicGeometry.Space.exists_isFiniteLocallyFreeOnSite_epi_modulePushforwardIdeal, AlgebraicGeometry.Space.hasResolutionProperty_iff_exists_epi_modulePushforwardIdeal, AlgebraicGeometry.Space.ResolutionPropertyDescentSituation.exists_isFiniteLocallyFreeOnSite_epi_idealDirectImage_of_hasResolutionProperty, AlgebraicGeometry.Space.hasResolutionProperty_iff_exists_epi_idealDirectImage, AlgebraicGeometry.Space.hasResolutionProperty_limitAlgebraicSpace_iff
statement: formalized
proof: formalized
---

# 76.56 The resolution property

Section 76.56 of the Stacks Project, [Tag 0GUX](https://stacks.math.columbia.edu/tag/0GUX). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GUY, a situation

[Tag 0GUY](https://stacks.math.columbia.edu/tag/0GUY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_isSurjective_isEtale_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentSituation.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentSituation.lean#L111). The attribute's comment: “the existence of the affine surjective étale chart of the situation”.

> **Stacks 0GUY, the existence of the chart `V → X`.** A quasi-compact algebraic space over
> `S` admits a surjective étale morphism from an affine scheme of the site, surjectivity being
> the point-set notion of Stacks 03ME.
>
> This is the parenthetical claim of the source that such a chart exists: Stacks 03H6 gives a
> chart whose every represented base change is a surjective morphism of schemes, and Stacks
> 03H5 identifies that with surjectivity on points.

```lean
theorem exists_affine_isSurjective_isEtale_of_isQuasiCompactSpace
    (X : AlgebraicSpaces B S hS) (hX : IsQuasiCompactSpace B S hS X.1) :
    ∃ (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ X.1),
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        IsSurjective B S hS φ ∧ IsEtale B S hS φ
```

**`AlgebraicGeometry.Space.ResolutionPropertyDescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentSituation.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentSituation.lean#L130). The attribute's comment: “the data chosen in the situation, and the conditions imposed on it”.

> **Stacks 0GUY.** The choices fixed in the situation of the source for a quasi-compact and
> quasi-separated algebraic space `X` over `S`: an affine scheme `V` of the site with a
> surjective étale morphism `φ : V → X`, a factorization of `φ` into an open immersion
> `j : V → Y` into an algebraic space `Y` followed by a finite morphism `π : Y → X`, and a
> finite type quasi-coherent sheaf of ideals `ℐ ⊆ 𝒪_Y` with `|V(ℐ)| = |Y| ∖ |j(V)|`.
>
> A chart `V` as in the first clause exists by
> `AlgebraicGeometry.Space.exists_affine_isSurjective_isEtale_of_isQuasiCompactSpace`.

```lean
structure ResolutionPropertyDescentSituation (X : AlgebraicSpaces B S hS)
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
```

## Tag 0GUZ, a lemma

[Tag 0GUZ](https://stacks.math.columbia.edu/tag/0GUZ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_epi_biproduct_idealSheafPowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ResolutionPropertySurjection.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ResolutionPropertySurjection.lean#L218).

> **Stacks 0GUZ.**  In the situation of Stacks 0GUY — a quasi-compact and quasi-separated
> algebraic space `X`, a surjective étale `φ : V ⟶ X` from an affine scheme factored as an open
> immersion `j : V ⟶ Y` followed by a finite `π : Y ⟶ X`, and a finite type quasi-coherent sheaf of
> ideals `ℐ ⊆ 𝒪_Y` with `V(ℐ) = Y ∖ j(V)` — assume `X` Noetherian.  Then every coherent
> `𝒪_X`-module `ℱ` admits, for some `r ≥ 0` and integers `n_1, …, n_r ≥ 0`, a surjection
>
> `⨁_{i = 1}^{r} π_*(ℐ^{n_i}) ⟶ ℱ`
>
> of `𝒪_X`-modules.  This is
> `AlgebraicGeometry.Space.exists_epi_biproduct_idealSheafPowPushforward_of_le` at `N = 0`.

```lean
theorem exists_epi_biproduct_idealSheafPowPushforward (hX : IsNoetherian B S hS hZ X.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F) :
    ∃ (r : ℕ) (n : Fin r → ℕ)
      (_ : HasBiproduct fun i =>
        idealSheafPowPushforward B S hS (D.piHom B S hS hZ X hqc hqs) D.I (n i))
      (σ : (⨁ fun i => idealSheafPowPushforward B S hS (D.piHom B S hS hZ X hqc hqs) D.I (n i)) ⟶
        F), Epi σ
```

## Tag 0GV0, a lemma

[Tag 0GV0](https://stacks.math.columbia.edu/tag/0GV0) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFiniteLocallyFreeOnSite_epi_modulePushforwardIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentIdealQuotient.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyDescentIdealQuotient.lean#L134). The attribute's comment: “the direction from the resolution property: `π_*ℐ` is coherent by Stacks 07UH, so the resolution property of the Noetherian `X` exhibits it as the quotient of a finite locally free module. The converse direction is not claimed; its input Stacks 0GUZ, the powers `ℐ^n` of a quasi-coherent sheaf of ideals on an algebraic space, and the closure of finite local freeness under tensor powers and finite direct sums are all absent from the library, as the module documentation records”.

> **Stacks 0GV0, the direction from the resolution property.**  In the situation of
> Stacks 0GUY with `X` Noetherian, if `X` has the resolution property then `π_*ℐ` is the quotient
> of a finite locally free `𝒪_X`-module: there are a finite locally free `𝒪_X`-module `E` and an
> epimorphism `E ⟶ π_*ℐ`.

```lean
theorem exists_isFiniteLocallyFreeOnSite_epi_modulePushforwardIdeal
    (hX : IsNoetherian B S hS hZ X.1)
    (hRP : HasResolutionProperty.{u, u} B S hS X.1 X.2) :
    ∃ (E : Modules.{u, u} B S hS X.1 X.2)
      (_ : SheafOfModules.IsFiniteLocallyFreeOnSite E)
      (p : E ⟶ modulePushforwardIdeal B S hS hZ X hqc hqs D), Epi p
```

**`AlgebraicGeometry.Space.hasResolutionProperty_iff_exists_epi_modulePushforwardIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyNoetherianIdealCriterion.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyNoetherianIdealCriterion.lean#L90). The attribute's comment: “the whole statement, both directions”.

> Let `X` be a quasi-compact and quasi-separated algebraic space, `φ : V ⟶ X` a surjective
> étale morphism from an affine scheme factored as an open immersion `j : V ⟶ Y` followed by a
> finite `π : Y ⟶ X`, and `ℐ ⊆ 𝒪_Y` a finite type quasi-coherent sheaf of ideals with
> `V(ℐ) = Y ∖ j(V)`, and assume `X` is Noetherian. Then `X` has the resolution property if and only
> if `π_*ℐ` is the quotient of a finite locally free `𝒪_X`-module.

```lean
theorem hasResolutionProperty_iff_exists_epi_modulePushforwardIdeal
    (hX : IsNoetherian B S hS hZ X.1) :
    HasResolutionProperty.{u, u} B S hS X.1 X.2 ↔
      ∃ (E : Modules.{u, u} B S hS X.1 X.2) (_ : SheafOfModules.IsFiniteLocallyFreeOnSite E)
        (p : E ⟶ modulePushforwardIdeal B S hS hZ X hqc hqs D), Epi p
```

## Tag 0GV1, a lemma

[Tag 0GV1](https://stacks.math.columbia.edu/tag/0GV1) in the Stacks Project.

**`AlgebraicGeometry.Space.ResolutionPropertyDescentSituation.exists_isFiniteLocallyFreeOnSite_epi_idealDirectImage_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyIdealDirectImage.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyIdealDirectImage.lean#L141). The attribute's comment: “the implication from the resolution property of `X` to `π_*ℐ` being the quotient of a finite locally free `𝒪_X`-module; the reverse implication, whose proof in the source reduces to the Noetherian case Stacks 0GV0, is not proved — see the module documentation for the inputs it needs”.

> **Stacks 0GV1, the implication from the resolution property.**  In the situation of Stacks
> 0GUY, if the algebraic space `X` has the resolution property then `π_*ℐ` is the quotient of a
> finite locally free `𝒪_X`-module.

```lean
theorem exists_isFiniteLocallyFreeOnSite_epi_idealDirectImage_of_hasResolutionProperty
    (hX : HasResolutionProperty.{u, u} B S hS X.1 X.2) :
    ∃ (E : Modules.{u, u} B S hS X.1 X.2)
      (_ : SheafOfModules.IsFiniteLocallyFreeOnSite E)
      (f : E ⟶ idealDirectImage B S hS hZ sit), Epi f
```

**`AlgebraicGeometry.Space.hasResolutionProperty_iff_exists_epi_idealDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyIdealDirectImageConverse.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyIdealDirectImageConverse.lean#L269).

> In the situation of Stacks 0GUY — `X` a quasi-compact and quasi-separated algebraic space
> over `S`, `V` an affine scheme with a surjective étale `φ : V ⟶ X` factored as an open immersion
> `j : V ⟶ Y` followed by a finite `π : Y ⟶ X`, and `ℐ ⊆ 𝒪_Y` a finite type quasi-coherent sheaf
> of ideals with `|V(ℐ)| = |Y| ∖ |j(V)|` — the algebraic space `X` has the resolution property if
> and only if `π_*ℐ` is the quotient of a finite locally free `𝒪_X`-module.

```lean
theorem hasResolutionProperty_iff_exists_epi_idealDirectImage
    (sit : ResolutionPropertyDescentSituation B S hS hZ X hqc hqs) :
    HasResolutionProperty.{u, u} B S hS X.1 X.2 ↔
      ∃ (E : Modules.{u, u} B S hS X.1 X.2) (_ : SheafOfModules.IsFiniteLocallyFreeOnSite E)
        (p : E ⟶ sit.idealDirectImage B S hS hZ), Epi p
```

## Tag 0GV2, a lemma

[Tag 0GV2](https://stacks.math.columbia.edu/tag/0GV2) in the Stacks Project.

**`AlgebraicGeometry.Space.hasResolutionProperty_limitAlgebraicSpace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyLimitIff.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyLimitIff.lean#L77).

> **Stacks 0GV2.**  Let `X = lim X_i` be the limit of a cofiltered system of quasi-compact and
> quasi-separated algebraic spaces over `S` with affine transition morphisms.  Then `X` has the
> resolution property if and only if some `X_i` has it.
>
> The system is indexed by a cofiltered category, which contains the directed systems of the
> source; the bounds `hSize` and `hHomSize` on the index are those under which the limit of the
> presheaves `D` is an algebraic space of the big fppf site (`limitAlgebraicSpace`, Stacks 07SF).
>
> If `X_i` has the resolution property, so does `X`, by the affine case of Stacks 0GUU along the
> affine projection `X ⟶ X_i`.  Conversely, the proof is the source's; see the module
> documentation.

```lean
theorem hasResolutionProperty_limitAlgebraicSpace_iff
    (hqc : ∀ i, IsQuasiCompactSpace B S hS (D.obj i))
    (hqs : ∀ i, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i)) :
    HasResolutionProperty.{u, u} B S hS
        (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).1
        (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).2 ↔
      ∃ i, HasResolutionProperty.{u, u} B S hS (D.obj i) (hD i)
```

## Tag 0GV3, a lemma

[Tag 0GV3](https://stacks.math.columbia.edu/tag/0GV3) in the Stacks Project.

**`AlgebraicGeometry.Space.isAffineHom_viewOverIntegers_diag_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyAffineDiagonal.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyAffineDiagonal.lean#L139).

> **Stacks 0GV3.**  Let `X` be a quasi-compact and quasi-separated algebraic space over a
> scheme `S` with the resolution property.  Then `X` has affine diagonal over `ℤ`: the diagonal of
> `X` viewed as an algebraic space over `Spec ℤ` is an affine morphism.

```lean
theorem isAffineHom_viewOverIntegers_diag_of_hasResolutionProperty
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hXres : HasResolutionProperty.{u, u} B S hS X hX) :
    IsAffineHom B (⊤_ Scheme.{u}) hZ (diag (viewOverIntegers B S hS hZ X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.56, Tag 0GUX](https://stacks.math.columbia.edu/tag/0GUX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
