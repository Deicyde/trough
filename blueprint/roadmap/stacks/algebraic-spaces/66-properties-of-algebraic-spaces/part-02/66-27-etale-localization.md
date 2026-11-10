---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.spacesEtaleLocalization, AlgebraicGeometry.Space.spacesEtaleLocalization_forget, AlgebraicGeometry.Space.spacesEtaleLocalization_slice, AlgebraicGeometry.Space.spacesEtaleLocalization_isContinuous, AlgebraicGeometry.Space.spacesEtaleLocalization_inverse_isContinuous, AlgebraicGeometry.Space.spacesEtaleLocalization_structureSheaf, AlgebraicGeometry.Space.spacesEtaleLocalizationRingedHom, AlgebraicGeometry.Space.smallEtaleEquivalenceOverChart
statement: formalized
proof: formalized
---

# 66.27 Étale localization

Section 66.27 of the Stacks Project, [Tag 04LX](https://stacks.math.columbia.edu/tag/04LX). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04LY, an equation

[Tag 04LY](https://stacks.math.columbia.edu/tag/04LY) in the Stacks Project.

**`AlgebraicGeometry.Space.spacesEtaleLocalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean#L449). The attribute's comment: “equivalence of categories”.

> **Stacks 04LY.** For an étale morphism `f : X ⟶ Y` of algebraic spaces, the spaces-étale
> site of `X` is equivalent to the localization of the spaces-étale site of `Y` at the object
> `f`.

```lean
noncomputable def spacesEtaleLocalization :
    SpacesEtale B S hS X ≌ Over (etaleObject B S hS f hf)
```

**`AlgebraicGeometry.Space.spacesEtaleLocalization_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean#L479). The attribute's comment: “canonical identification”.

> **Stacks 04LY.** Under the localization equivalence an algebraic space étale over `X` is
> unchanged, and its structure morphism to `Y` is the composite with `f`.

```lean
theorem spacesEtaleLocalization_forget :
    (spacesEtaleLocalization B S hS f hf).functor ⋙
        Over.forget (etaleObject B S hS f hf) ⋙ SpacesEtale.inclusion B S hS Y =
      SpacesEtale.inclusion B S hS X ⋙ Over.map f
```

**`AlgebraicGeometry.Space.spacesEtaleLocalization_slice`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean#L498). The attribute's comment: “slice arrows”.

> **Stacks 04LY.** The localization equivalence preserves the whole arrow to `X`, not only
> its composite with `f`; this is what makes it canonical.

```lean
theorem spacesEtaleLocalization_slice :
    (spacesEtaleLocalization B S hS f hf).functor ⋙
        Over.post (SpacesEtale.toSpaces B S hS Y) =
      SpacesEtale.inclusion B S hS X
```

**`AlgebraicGeometry.Space.spacesEtaleLocalization_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean#L523). The attribute's comment: “forward topology”.

> **Stacks 04LY.** The localization equivalence carries covering sieves of the spaces-étale
> site of `X` to covering sieves of the slice topology.

```lean
theorem spacesEtaleLocalization_isContinuous :
    (spacesEtaleLocalization B S hS f hf).functor.IsContinuous
      (SpacesEtale.topology B S hS X)
      ((SpacesEtale.topology B S hS Y).over (etaleObject B S hS f hf))
```

**`AlgebraicGeometry.Space.spacesEtaleLocalization_inverse_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleLocalization.lean#L549). The attribute's comment: “inverse topology”.

> **Stacks 04LY.** The inverse of the localization equivalence carries covering sieves of
> the slice topology to covering sieves of the spaces-étale site of `X`.

```lean
theorem spacesEtaleLocalization_inverse_isContinuous :
    (spacesEtaleLocalization B S hS f hf).inverse.IsContinuous
      ((SpacesEtale.topology B S hS Y).over (etaleObject B S hS f hf))
      (SpacesEtale.topology B S hS X)
```

## Tag 04LZ, an equation

[Tag 04LZ](https://stacks.math.columbia.edu/tag/04LZ) in the Stacks Project.

**`AlgebraicGeometry.Space.spacesEtaleLocalization_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean#L390). The attribute's comment: “the structure sheaves”.

> **Stacks 04LZ.** For an étale morphism `f : X ⟶ Y` of algebraic spaces, the structure sheaf
> of the spaces-étale site of `X` is the restriction of the structure sheaf of `Y` along the
> localization equivalence of Stacks 04LY: `𝒪_X = 𝒪_Y|_{Y_{spaces,étale}/X}`.

```lean
theorem spacesEtaleLocalization_structureSheaf :
    ((spacesEtaleLocalization B S hS f hf).functor.sheafPushforwardContinuous
          CommRingCat.{u + 1} (SpacesEtale.topology B S hS X)
          ((SpacesEtale.topology B S hS Y).over (etaleObject B S hS f hf))).obj
        ((SpacesEtale.structureSheaf B S hS Y).over (etaleObject B S hS f hf)) =
      SpacesEtale.structureSheaf B S hS X
```

**`AlgebraicGeometry.Space.spacesEtaleLocalizationRingedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleStructureSheaf.lean#L406). The attribute's comment: “the identification of ringed sites”.

> **Stacks 04LZ.** For an étale morphism `f : X ⟶ Y` of algebraic spaces, the ringed site
> `(X_{spaces,étale}, 𝒪_X)` is the localized ringed site
> `(Y_{spaces,étale}/X, 𝒪_Y|_{Y_{spaces,étale}/X})`: the identification of sites of Stacks 04LY
> matches the two structure sheaves.

```lean
noncomputable def spacesEtaleLocalizationRingedHom :
    RingedToposSiteHom (spacesEtaleRingedToposOver B S hS f hf)
      (spacesEtaleRingedTopos B S hS X)
```

## Tag 04M0, an equation

[Tag 04M0](https://stacks.math.columbia.edu/tag/04M0) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleEquivalenceOverChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartEquivalence.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartEquivalence.lean#L371).

> **Stacks 04M0.** The small étale site of an étale scheme chart `X → F` is canonically the
> localization of the small étale site of `F` at that chart. The equivalence preserves the entire
> arrow to `X`, not just the underlying scheme over `S`.

```lean
theorem smallEtaleEquivalenceOverChart
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hF : IsAlgebraicSpace B S hS F)
    (X : SmallEtale B S hS F) :
    ∃ e : SmallEtale B S hS
        (yoneda.obj ((SmallEtale.toOver B S hS F).obj X)) ≌ Over X,
      e.functor.inducedTopology ((SmallEtale.topology B S hS F).over X) =
        SmallEtale.topology B S hS
          (yoneda.obj ((SmallEtale.toOver B S hS F).obj X)) ∧
      e.functor ⋙ Over.forget X ⋙ SmallEtale.toOver B S hS F =
        SmallEtale.toOver B S hS
          (yoneda.obj ((SmallEtale.toOver B S hS F).obj X)) ∧
      e.functor ⋙ Over.post (SmallEtale.toOver B S hS F ⋙ yoneda) =
        SmallEtale.inclusion B S hS
            (yoneda.obj ((SmallEtale.toOver B S hS F).obj X)) ⋙
          CostructuredArrow.toOver yoneda
            (yoneda.obj ((SmallEtale.toOver B S hS F).obj X))
```

## Tag 04M1, an equation

[Tag 04M1](https://stacks.math.columbia.edu/tag/04M1) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedEquivalenceOverChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean#L56).

> The small étale ringed site of an étale scheme chart `X → Y` of an
> algebraic space is the localization of the ringed small étale site of `Y` at that chart: the
> localization equivalence of Tag 04M0 matches the two structure presheaves, naturally in the
> chart.

```lean
theorem smallEtaleRingedEquivalenceOverChart
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hY : IsAlgebraicSpace B S hS Y)
    (X : SmallEtale B S hS Y) :
    ∃ e : SmallEtale B S hS (yoneda.obj ((SmallEtale.toOver B S hS Y).obj X)) ≌ Over X,
      e.functor.inducedTopology ((SmallEtale.topology B S hS Y).over X) =
        SmallEtale.topology B S hS (yoneda.obj ((SmallEtale.toOver B S hS Y).obj X)) ∧
      (e.functor ⋙ Over.forget X ⋙ SmallEtale.toOver B S hS Y =
        SmallEtale.toOver B S hS (yoneda.obj ((SmallEtale.toOver B S hS Y).obj X))) ∧
      (e.functor.op ⋙ (Over.forget X).op ⋙ structurePresheaf B S hS Y =
        structurePresheaf B S hS (yoneda.obj ((SmallEtale.toOver B S hS Y).obj X)))
```

## Tag 04M2, an equation

[Tag 04M2](https://stacks.math.columbia.edu/tag/04M2) in the Stacks Project.

**`AlgebraicGeometry.Space.affineEtaleEquivalenceOverChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean#L103).

> The affine étale site of an affine étale chart `X → Y` of an algebraic
> space is the localization of the affine étale site of `Y` at that chart, by an equivalence
> preserving both the topology and the underlying objects of the big fppf site.

```lean
theorem affineEtaleEquivalenceOverChart
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hY : IsAlgebraicSpace B S hS Y)
    (X : AffineEtale B S hS Y) :
    ∃ e : AffineEtale B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X)) ≌ Over X,
      e.functor.inducedTopology ((AffineEtale.topology B S hS Y).over X) =
        AffineEtale.topology B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X)) ∧
      e.functor ⋙ Over.forget X ⋙ AffineEtale.toOver B S hS Y =
        AffineEtale.toOver B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X))
```

## Tag 04M3, an equation

[Tag 04M3](https://stacks.math.columbia.edu/tag/04M3) in the Stacks Project.

**`AlgebraicGeometry.Space.affineEtaleRingedEquivalenceOverChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartLocalization.lean#L220).

> The affine étale ringed site of an affine étale chart `X → Y` of an
> algebraic space is the localization of the ringed affine étale site of `Y` at that chart: the
> equivalence of Tag 04M2 matches the two structure presheaves, naturally under restriction.

```lean
theorem affineEtaleRingedEquivalenceOverChart
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hY : IsAlgebraicSpace B S hS Y)
    (X : AffineEtale B S hS Y) :
    ∃ e : AffineEtale B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X)) ≌ Over X,
      e.functor.inducedTopology ((AffineEtale.topology B S hS Y).over X) =
        AffineEtale.topology B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X)) ∧
      (e.functor ⋙ Over.forget X ⋙ AffineEtale.toOver B S hS Y =
        AffineEtale.toOver B S hS (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X))) ∧
      (e.functor.op ⋙ (Over.forget X).op ⋙ (AffineEtale.inclusion B S hS Y).op ⋙
          structurePresheaf B S hS Y =
        (AffineEtale.inclusion B S hS
          (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X))).op ⋙
          structurePresheaf B S hS
            (yoneda.obj ((AffineEtale.toOver B S hS Y).obj X)))
```

## Tag 04M4, a lemma

[Tag 04M4](https://stacks.math.columbia.edu/tag/04M4) in the Stacks Project.

**`AlgebraicGeometry.Space.spacesEtaleComparisonMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleRelocalization.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleRelocalization.lean#L211). The attribute's comment: “the map `c : U ⟶ V ×_Y X` corresponding to `g`, and nothing else”.

> The map `c : U ⟶ V ×_Y X` corresponding to `g`, as an arrow of the spaces-étale site of
> `X` from `U` to the cartesian base change of `V` along `f`.

```lean
noncomputable def spacesEtaleComparisonMap (hsq : g ≫ q = p ≫ f) :
    etaleObject B S hS p hp ⟶
      (spacesBaseChange B S hS f).functor.obj (etaleObject B S hS q hq)
```

**`AlgebraicGeometry.Space.spacesEtaleRelocalizedTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleRelocalization.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SpacesEtaleRelocalization.lean#L512). The attribute's comment: “the two morphisms of ringed topoi are 2-isomorphic, via the identifications of 04LZ read as the two vertical arrows of a commuting square”.

> Via the identifications of Stacks 04LZ for `U ⟶ X` and for `V ⟶ Y`, the morphism of ringed
> topoi `(g_{spaces,étale}, g^♯)` is 2-isomorphic to the morphism `(f_{spaces,étale,c}, f_c^♯)` of
> Stacks 04J1 built from `(f_{spaces,étale}, f^♯)` and the map `c : U ⟶ V ×_Y X` corresponding to
> `g`: the square of ringed topoi whose vertical arrows are the two identifications commutes, up
> to an invertible 2-morphism.

```lean
noncomputable def spacesEtaleRelocalizedTwoIso :
    AlgebraicGeometry.RingedToposHom.TwoIso
      (A := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
        ((spacesEtaleRingedSite B S hS X).over (etaleObject B S hS p hp)))
      (B := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
        (spacesEtaleRingedSite B S hS V))
      (AlgebraicGeometry.RingedToposHom.comp
        (X := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          ((spacesEtaleRingedSite B S hS X).over (etaleObject B S hS p hp)))
        (Y := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          ((spacesEtaleRingedSite B S hS Y).over (etaleObject B S hS q hq)))
        (Z := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          (spacesEtaleRingedSite B S hS V))
        (spacesEtaleLocalizationRingedSiteHom B S hS q hq).ringedToposHom
        ((spacesEtaleRingedSiteHom B S hS f).relocalized c))
      (AlgebraicGeometry.RingedToposHom.comp
        (X := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          ((spacesEtaleRingedSite B S hS X).over (etaleObject B S hS p hp)))
        (Y := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          (spacesEtaleRingedSite B S hS U))
        (Z := AlgebraicGeometry.RingedSite.ringedTopos.{u + 1, u + 1, u + 1}
          (spacesEtaleRingedSite B S hS V))
        (spacesEtaleRingedSiteHom B S hS g).ringedToposHom
        (spacesEtaleLocalizationRingedSiteHom B S hS p hp).ringedToposHom)
```

## Tag 04M5, a lemma

[Tag 04M5](https://stacks.math.columbia.edu/tag/04M5) in the Stacks Project.

**`AlgebraicGeometry.Space.chartRelocalizedTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartRelocalization.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleChartRelocalization.lean#L294). The attribute's comment: “via the identifications of 04M1 at U and V, the morphism (g\_small, g^sharp) is 2-isomorphic to the morphism (f\_\{small,s}, f\_s^sharp) of 04J8 for the map s : h\_U -> f^\{-1}h\_V corresponding to g”.

> **Stacks 04M5.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let `U ⟶ X` and
> `V ⟶ Y` be étale morphisms from schemes (objects of the small étale sites of `X` and `Y`) and let
> `g : U ⟶ V` be a morphism of schemes with `q ∘ g = f ∘ p`. Via the identifications of Stacks 04M1
> of the small étale ringed topoi of `U` and `V` with the localizations of those of `X` at `h_U` and
> of `Y` at `h_V` (`AlgebraicGeometry.Space.chartLocalizationHom`, an equivalence of topoi), the
> morphism of small étale ringed topoi `(g_small, g♯)` is 2-isomorphic to the morphism
> `(f_{small,s}, f_s♯)` of Stacks 04J8 built from `(f_small, f♯)` and the map
> `s : h_U ⟶ f_small⁻¹h_V` corresponding to `g`
> (`AlgebraicGeometry.Space.chartRelocalizationSheafMap`).

```lean
noncomputable def chartRelocalizedTwoIso :
    RingedToposHom.TwoIso (A := 𝒰) (B := 𝒴ᵥ) (chartRelocalizedHom B S hS f U V g hg)
      (chartMorphismHom B S hS U V g)
```

## Tag 0GF6, a lemma

[Tag 0GF6](https://stacks.math.columbia.edu/tag/0GF6) in the Stacks Project.

**`AlgebraicGeometry.Space.sheafGivesSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafGivesSpace.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafGivesSpace.lean#L205).

> Let `Y` be an algebraic space over `S` and `𝓕` a sheaf of sets on its small étale site,
> satisfying the set-theoretic condition of the source's proof. Write `G` for the corresponding
> sheaf on the spaces-étale site (Stacks 03G1) and `X` for the functor
> `T ↦ {(y, s) | y : T → Y, s ∈ Γ(T, y⁻¹ 𝓕)}` on `(Sch/S)_fppf`. Then
>
> 1. `X` is an algebraic space;
> 2. the map `X → Y`, `(y, s) ↦ y`, is étale;
> 3. via `Sh(Y_étale) = Sh(Y_{spaces,étale})`, `𝓕 ≅ h_X`, where `h_X(U)` is the set of
>    morphisms `U → X` over `Y` of functors on `(Sch/S)_fppf`;
> 4. `X` is the (universe-lifted) functor of points of an algebraic space `X'`, under which the
>    map `X → Y` is an étale morphism `f : X' → Y`; the inverse image `f_small⁻¹` has a left
>    adjoint `f_{small,!}` (Stacks 03LP), and for every such left adjoint `𝓕 ≅ f_{small,!} *`,
>    where `*` is the terminal sheaf on `X'_étale`.

```lean
theorem sheafGivesSpace (F : Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)))
    (hF : SheafGivesSpace.SatisfiesSetTheoreticCondition B S hS Y F) :
    IsAlgebraicSpaceULift.{u + 1} B S hS
        (sheafPairsFunctor B S hS ((smallEtaleToposEquiv B S hS Y).inverse.obj F)) ∧
      IsEtaleULift.{u + 1} B S hS
        (sheafPairsFunctorToBase B S hS ((smallEtaleToposEquiv B S hS Y).inverse.obj F)) ∧
      Nonempty (((smallEtaleToposEquiv B S hS Y).inverse.obj F).obj ≅
        sheafPairsHom B S hS ((smallEtaleToposEquiv B S hS Y).inverse.obj F)) ∧
      ∃ (X' : AlgebraicSpaces B S hS) (f : X' ⟶ Y) (_ : IsEtale B S hS f.hom)
        (ι : sheafPairsFunctor B S hS ((smallEtaleToposEquiv B S hS Y).inverse.obj F) ≅
          X'.obj ⋙ uliftFunctor.{u + 1}),
        sheafPairsFunctorToBase B S hS ((smallEtaleToposEquiv B S hS Y).inverse.obj F) =
            ι.hom ≫ Functor.whiskerRight f.hom uliftFunctor.{u + 1} ∧
          (∃ L : Sheaf (SmallEtale.topology B S hS X'.1) (Type (u + 1)) ⥤
              Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)),
            Nonempty (L ⊣ (smallToposMorphism B S hS f).inverseImage)) ∧
          ∀ (L : Sheaf (SmallEtale.topology B S hS X'.1) (Type (u + 1)) ⥤
              Sheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)))
            (_ : L ⊣ (smallToposMorphism B S hS f).inverseImage),
            Nonempty (F ≅ L.obj (⊤_ (Sheaf (SmallEtale.topology B S hS X'.1) (Type (u + 1)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.27, Tag 04LX](https://stacks.math.columbia.edu/tag/04LX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
