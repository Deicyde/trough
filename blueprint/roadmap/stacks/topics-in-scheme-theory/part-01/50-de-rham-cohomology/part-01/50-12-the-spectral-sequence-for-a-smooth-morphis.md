---
declaration: section
origin: cited
lean: Stacks.DeRhamSmooth.deRhamSmoothFiltration_spec, Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence, Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_pullback, Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_smooth, Stacks.DeRhamRigidity.isLocallyFree_deRhamCohomologySheaf_of_proper_smooth_rat, Stacks.DeRhamSmooth.deRhamSmoothSpectralSequence_gaussManin, Stacks.DeRhamSmooth.deRhamCohomologySheaf, Stacks.DeRhamSmooth.deRhamFirstPageFlat
statement: formalized
proof: formalized
---

# 50.12 The spectral sequence for a smooth morphism

Section 50.12 of the Stacks Project, [Tag 0FMK](https://stacks.math.columbia.edu/tag/0FMK). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FMK, the section

[Tag 0FMK](https://stacks.math.columbia.edu/tag/0FMK) in the Stacks Project.

**`Stacks.DeRhamSmooth.deRhamSmoothFiltration_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltration.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltration.lean#L116). The attribute's comment: “the filtration of Ω^•_{X/S} by the forms pulled back from Y, constructed from the pullback map of Tag 0FKP, with its subcomplex, decreasing and exhaustion clauses; NOT the identification of the graded pieces: the local Künneth decomposition of the forms along a local splitting of the smooth differentials sequence is available, but its independence of the chosen splitting, which is what glues the local comparisons onto gr^k, is not”.

> **Stacks Project, Section 0FMK.** For `f : X ⟶ Y` over a base `S`, the canonical pullback map
> `ρ : f^{-1}Ω^•_{Y/S} ⟶ Ω^•_{X/S}` of `(f∘g)^{-1}𝒪_S`-modules filters the relative de Rham complex
> `Ω^•_{X/S}` by the forms pulled back from `Y`:
>
> * the underlying complex of the filtration is `Ω^•_{X/S}`;
> * its `(k+1)`-st step is the image of the wedge map out of
>   `Tot(f^{-1}σ^{≥(k+1)}Ω^•_{Y/S} ⊗_{(f∘g)^{-1}𝒪_S} Ω^•_{X/S})`, so each step is a subcomplex;
> * the steps decrease;
> * and the filtration is exhaustive, its steps in degrees `≤ 0` being all of `Ω^•_{X/S}`.

```lean
theorem deRhamSmoothFiltration_spec :
    (deRhamSmoothFiltration f g).X = deRhamCochainComplex (f ≫ g) ∧
      (∀ k : ℤ, (deRhamSmoothFiltration f g).filtration.subobject (op k) =
        AlgebraicGeometry.SheafOfModules.wedgeFiltrationStep
          (Scheme.Hom.deRhamAlgebras (f ≫ g))
          (AlgebraicGeometry.SheafOfModules.deRhamDifferential
            (Scheme.Hom.deRhamAlgebras (f ≫ g)))
          (pulledBackDeRhamComplex f g)
          (Stacks.DeRhamPullback.deRhamPullbackChain f g) k) ∧
      Antitone (AlgebraicGeometry.SheafOfModules.wedgeFiltrationStep
        (Scheme.Hom.deRhamAlgebras (f ≫ g))
        (AlgebraicGeometry.SheafOfModules.deRhamDifferential
          (Scheme.Hom.deRhamAlgebras (f ≫ g)))
        (pulledBackDeRhamComplex f g)
        (Stacks.DeRhamPullback.deRhamPullbackChain f g)) ∧
      ∀ k : ℤ, k ≤ 0 → IsIso ((deRhamSmoothFiltration f g).filtration.ι.app (op k))
```

## Tag 0FMM, a lemma

[Tag 0FMM](https://stacks.math.columbia.edu/tag/0FMM) in the Stacks Project.

**`Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequence.lean#L195). The attribute's comment: “granted the filtration of Section 0FMK as the hypotheses K, hKX, hexh and hvanish, and its graded pieces together with Tag 0FML as the hypothesis hgr”.

> **Stacks Project, Tag 0FMM.** Let `f : X ⟶ Y` be a quasi-compact, quasi-separated and smooth
> morphism of schemes over a base `S`, with `g : Y ⟶ S` the structure morphism of the target.
> There is a bounded cohomological spectral sequence of sheaves of `g^{-1}𝒪_S`-modules on `Y`,
> starting at its first page, with
>
> `E_1^{p, q} = H^q(Ω^p_{Y/S} ⊗^{\mathbf L}_{𝒪_Y} Rf_*Ω^•_{X/Y})`,
>
> which abuts to `R^{p + q}f_*Ω^•_{X/S}`.
>
> The filtration of `Ω^•_{X/S}` by the forms pulled back from `Y` is supplied as the filtered
> complex `K` with `K.X = Ω^•_{X/S}`, together with its exhaustion `hexh`, the eventual vanishing
> `hvanish` of the higher direct images of its far steps, and the identification `hgr` of
> `R^{p + q}f_*gr^pK` with the first page; `hgr` is the computation of the graded pieces
> `gr^kΩ^•_{X/S} = f^{-1}Ω^k_{Y/S}[-k] ⊗_{f^{-1}𝒪_Y} Ω^•_{X/Y}` of Section 0FMK followed by the
> projection formula of Tag 0FML. The spectral sequence, its boundedness in the sense of Tag
> 0BDU, and its abutment are then those of the filtered complex `K`.

```lean
theorem exists_boundedDeRhamSpectralSequence
    [QuasiCompact f] [QuasiSeparated f] [Smooth f]
    (K : CochainComplex.Filtered (SheafOfModules.{u} (structureSheafRing (inverseImageBase (f ≫ g)))))
    (hKX : K.X = deRhamCochainComplex (f ≫ g))
    (hexh : ∀ p : ℤ, p ≤ 0 → IsIso (K.filtration.ι.app (op p)))
    (hvanish : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      IsZero (higherDirectImage (derivedRelativePushforward f g)
        (K.filtration.obj (op p)) n))
    (hgr : ∀ p q : ℤ, Nonempty (higherDirectImage (derivedRelativePushforward f g)
      ((FilteredObject.gr p).obj K) (p + q) ≅ deRhamFirstPage f g p q)) :
    ∃ E : CohomologicalSpectralSequence
        (SheafOfModules.{u} (structureSheafRing (inverseImageBase g))) 1,
      _root_.IsBounded E ∧
      (∀ p q : ℤ, Nonempty ((E.page 1).X (p, q) ≅ deRhamFirstPage f g p q)) ∧
      SpectralSequence.AbutsTo E (fun n => deRhamHigherDirectImage f g n)
```

**`Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceFiltered.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceFiltered.lean#L102). The attribute's comment: “at the filtration of Section 0FMK, which is constructed rather than assumed; granted only hvanish, the eventual vanishing of R^nf_* on the far steps, and hgr, the graded pieces of Section 0FMK followed by the projection formula of Tag 0FML conclusions (4) and (5)”.

> **Stacks Project, Tag 0FMM**, at the filtration of Section 50.12. Let `f : X ⟶ Y` be a
> quasi-compact, quasi-separated and smooth morphism of schemes over a base `S`, with `g : Y ⟶ S`
> the structure morphism of the target. There is a bounded cohomological spectral sequence of
> sheaves of `g^{-1}𝒪_S`-modules on `Y`, starting at its first page, with
>
> `E_1^{p, q} = H^q(Ω^p_{Y/S} ⊗^{\mathbf L}_{𝒪_Y} Rf_*Ω^•_{X/Y})`,
>
> which abuts to `R^{p + q}f_*Ω^•_{X/S}`.
>
> The filtration is not assumed: it is `Stacks.DeRhamSmooth.deRhamSmoothFiltration`, the filtration
> of `Ω^•_{X/S}` by the forms pulled back from `Y`, and its identification with `Ω^•_{X/S}` and its
> exhaustion come from `Stacks.DeRhamSmooth.deRhamSmoothFiltration_spec`. What is assumed is the
> eventual vanishing `hvanish` of `R^nf_*` on the far steps of that filtration, and the
> identification `hgr` of `R^{p+q}f_*gr^p` with the first page, which is the computation of the
> graded pieces `gr^kΩ^•_{X/S} = f^{-1}Ω^k_{Y/S}[-k] ⊗_{f^{-1}𝒪_Y} Ω^•_{X/Y}` of Section 0FMK
> followed by the projection formula of Tag 0FML.

```lean
theorem exists_boundedDeRhamSpectralSequence_of_pullback
    [QuasiCompact f] [QuasiSeparated f] [Smooth f]
    (hvanish : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      IsZero (higherDirectImage (derivedRelativePushforward f g)
        ((deRhamSmoothFiltration f g).filtration.obj (op p)) n))
    (hgr : ∀ p q : ℤ, Nonempty (higherDirectImage (derivedRelativePushforward f g)
      (gradedPiece (inverseImageBase (f ≫ g)) p (deRhamSmoothFiltration f g)) (p + q) ≅
        deRhamFirstPage f g p q)) :
    ∃ E : CohomologicalSpectralSequence
        (SheafOfModules.{u} (structureSheafRing (inverseImageBase g))) 1,
      _root_.IsBounded E ∧
      (∀ p q : ℤ, Nonempty ((E.page 1).X (p, q) ≅ deRhamFirstPage f g p q)) ∧
      SpectralSequence.AbutsTo E (fun n => deRhamHigherDirectImage f g n)
```

**`Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceTheorem.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceTheorem.lean#L47). The attribute's comment: “the bounded spectral sequence of a quasi-compact, quasi-separated, smooth morphism, with first page H^q(Ω^p_{Y/S} ⊗ᴸ Rf_*Ω^•_{X/Y}) and abutment R^{p+q}f_*Ω^•_{X/S}”.

> Let `f : X ⟶ Y` be a quasi-compact, quasi-separated and smooth morphism of schemes over a base
> scheme `S`, with `g : Y ⟶ S` the structure morphism of the target. There is a bounded cohomological
> spectral sequence of sheaves of `g^{-1}𝒪_S`-modules on `Y`, starting at its first page, with
>
> `E_1^{p,q} = H^q(Ω^p_{Y/S} ⊗^𝐋_{𝒪_Y} Rf_*Ω^•_{X/Y})`,
>
> which abuts to `R^{p+q}f_*Ω^•_{X/S}`.

```lean
theorem exists_boundedDeRhamSpectralSequence_of_smooth
    [QuasiCompact f] [QuasiSeparated f] [Smooth f] :
    ∃ E : CohomologicalSpectralSequence
        (SheafOfModules.{u} (structureSheafRing (Stacks.DeRhamDirectImage.inverseImageBase g))) 1,
      _root_.IsBounded E ∧
      (∀ p q : ℤ, Nonempty ((E.page 1).X (p, q) ≅ deRhamFirstPage f g p q)) ∧
      SpectralSequence.AbutsTo E (fun n => deRhamHigherDirectImage f g n)
```

## Tag 0FMN, a remark

[Tag 0FMN](https://stacks.math.columbia.edu/tag/0FMN) in the Stacks Project.

**`Stacks.DeRhamRigidity.isLocallyFree_deRhamCohomologySheaf_of_proper_smooth_rat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ArtinianRigidity/LocallyFreeRat.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/ArtinianRigidity/LocallyFreeRat.lean#L46). The attribute's comment: “if f is proper in addition to being smooth and S is a scheme over Q, then H^q_dR(X/Y) is finite locally free (the sentence the source defers to a future reference)”.

> **The de Rham cohomology sheaves of a proper smooth morphism over `ℚ` are finite locally
> free** ([Stacks, Tag 0FMN], the sentence the source defers to a future reference). Let
> `f : X ⟶ Y` be proper and smooth, with `Y` over a scheme `S` over `Spec R` for a `ℚ`-algebra `R`.
> Then every `ℋ^q_dR(X/Y)` is a finite locally free `𝒪_Y`-module. The proof reduces to an Artinian
> local base (`Stacks.DeRhamSmooth.isLocallyFree_deRhamCohomologySheaf_of_artinian`), where the
> de Rham complex is rigid (`nonempty_derivedDeRhamDirectImage_iso_trivialMap`) and the trivial
> deformation has free cohomology (`free_moduleSpecΓ_deRhamCohomologySheaf_trivialMap`).

```lean
theorem isLocallyFree_deRhamCohomologySheaf_of_proper_smooth_rat {X Y S : Scheme.{u}}
    {R : CommRingCat.{u}} [Algebra ℚ R] (f : X ⟶ Y) (g : Y ⟶ S) (σ : S ⟶ Spec R) [IsProper f]
    [Smooth f] (q : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} (deRhamCohomologySheaf f q)
```

**`Stacks.DeRhamSmooth.deRhamSmoothSpectralSequence_gaussManin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/GaussManinConnection.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/GaussManinConnection.lean#L103). The attribute's comment: “the first page Ω^p_{Y/S} ⊗ ℋ^q_dR(X/Y) for flat ℋ^q_dR, d_1^{0,q} the integrable Gauss–Manin connection and d_1^{•,q} its de Rham complex; the finite local freeness for proper f over ℚ is deferred by the source and omitted”.

> **Stacks Project, Tag 0FMN.** Let `f : X ⟶ Y` be a quasi-compact, quasi-separated, smooth
> morphism of schemes over `S`, with `g : Y ⟶ S` the structure morphism of the target, and suppose
> the de Rham cohomology sheaves `ℋ^q_dR(X/Y)` are flat `𝒪_Y`-modules. Then the spectral sequence
> `E` of [Stacks, Tag 0FMM] (bounded, abutting to `R^{p + q}f_*Ω^•_{X/S}`) has
> `E_1^{p, q} = Ω^p_{Y/S} ⊗_{𝒪_Y} ℋ^q_dR(X/Y)` (`deRhamSmoothFirstPageFlatIso`), and for every `q`:
>
> 1. its differentials are maps `d_1^{p, q} : Ω^p_{Y/S} ⊗ ℋ^q ⟶ Ω^{p + 1}_{Y/S} ⊗ ℋ^q`, namely
>    `deRhamFirstPageFlatDifferential`, and they satisfy the Katz–Oda Leibniz rule
>    `d_1(ω ⊗ s) = dω ⊗ s + (-1)^p ω ∧ d_1(1 ⊗ s)`;
> 2. `d_1^{0, q} : ℋ^q ⟶ Ω^1_{Y/S} ⊗ ℋ^q` is the integrable connection `∇` of
>    `gaussManinConnection` (the **Gauss–Manin connection**), read through
>    `Ω^1_{Y/S} ⊗ ℋ^q ≅ ℋ^q ⊗ Ω_{Y/S}`;
> 3. the complex `ℋ^q ⟶ Ω^1_{Y/S} ⊗ ℋ^q ⟶ Ω^2_{Y/S} ⊗ ℋ^q ⟶ ⋯` with differentials `d_1^{•, q}` is
>    the de Rham complex of `∇` (`gaussManinTwistedDifferential`, a complex), its differential in
>    degree `p` being `d_1^{p, q}` read through `Ω^p_{Y/S} ⊗ ℋ^q ≅ ℋ^q ⊗ Ω^p_{Y/S}`.
>
> The sentence of the remark on finite local freeness for proper `f` over `ℚ` is deferred by the
> source to a future reference and is not included.

```lean
theorem deRhamSmoothSpectralSequence_gaussManin (q : ℤ) :
    _root_.IsBounded (deRhamSmoothSpectralSequence f g) ∧
      SpectralSequence.AbutsTo (deRhamSmoothSpectralSequence f g)
        (fun n => deRhamHigherDirectImage f g n) ∧
      (∀ p : ℤ, Nonempty (((deRhamSmoothSpectralSequence f g).page 1).X (p, q) ≅
        deRhamFirstPageFlat f g p q)) ∧
      (∀ p : ℤ, ((deRhamSmoothSpectralSequence f g).page 1).d (p, q) (p + 1, q) =
        (deRhamSmoothFirstPageFlatIso f g hflat p q).hom ≫
          deRhamFirstPageFlatDifferential f g hflat p q ≫
            (deRhamSmoothFirstPageFlatIso f g hflat (p + 1) q).inv) ∧
      IsKatzOdaLeibniz g (deRhamCohomologySheaf f q)
        (fun p => deRhamFirstPageFlatDifferential f g hflat p q) ∧
      (∀ (U : (Y.Opens)ᵒᵖ) (s : (deRhamCohomologySheaf f q).val.obj U),
        (gaussManinConnection f g hflat q).d U s =
          (formsTensorConnectionIso g (deRhamCohomologySheaf f q)).hom.val.app U
            ((deRhamFirstPageFlatDifferential f g hflat 0 q).val.app U
              (formsTensorUnitTmul g (deRhamCohomologySheaf f q) U s))) ∧
      (gaussManinConnection f g hflat q).IsIntegrable (gaussManinTwistedDifferential f g hflat q) ∧
      (gaussManinTwistedDifferential f g hflat q).IsComplex ∧
      ∀ p : ℕ, (gaussManinTwistedDifferential f g hflat q).d p =
        (_root_.pushforward (toInverseImageBase g)).map
            (β_ (modulesOnRing (deRhamCohomologySheaf f q)) (formsOnRing g p)).hom ≫
          deRhamFirstPageFlatDifferential f g hflat p q ≫
          (_root_.pushforward (toInverseImageBase g)).map
            ((formsTensorSuccIso g (deRhamCohomologySheaf f q) p).hom ≫
              (β_ (formsOnRing g ((p + 1 : ℕ) : ℤ))
                (modulesOnRing (deRhamCohomologySheaf f q))).hom)
```

**`Stacks.DeRhamSmooth.deRhamCohomologySheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean#L179). The attribute's comment: “the cohomology sheaves ℋ^q_dR(X/Y) = H^q(Rf_*Ω^•_{X/Y})”. References: SGA 7 XXII (3.3), “more general”.

> **`ℋ^q_dR(X/Y) = H^q(Rf_*Ω^•_{X/Y})`**, the `q`-th de Rham cohomology sheaf of `X` over `Y`:
> the `q`-th cohomology sheaf of the derived direct image along `f` of the relative de Rham complex
> of `X` over `Y`, a sheaf of `𝒪_Y`-modules.
>
> The derived direct image is `Stacks.DeRhamDirectImage.derivedDeRhamDirectImage`, an object of
> `D⁺(𝒪_Y)`, so the cohomology is read with the cohomology functors of `D⁺`; along the inclusion
> of `D⁺(𝒪_Y)` into `D(𝒪_Y)` these agree with the cohomology functors of `D(𝒪_Y)`. By
> [Stacks, Tag 0FLX] — `Stacks.DeRhamDirectImage.isQuasicoherent_homology_derivedDeRhamDirectImage`
> — these sheaves are quasi-coherent whenever `f` is quasi-compact and quasi-separated.

```lean
def deRhamCohomologySheaf (q : ℤ) : Y.Modules
```

**`Stacks.DeRhamSmooth.deRhamFirstPageFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean#L192). The attribute's comment: “the module Ω^p_{Y/S} ⊗_{𝒪_Y} ℋ^q_dR(X/Y) of the flat case”.

> **`Ω^p_{Y/S} ⊗_{𝒪_Y} ℋ^q_dR(X/Y)`**, the module the remark [Stacks, Tag 0FMN] writes the
> first page of the spectral sequence of [Stacks, Tag 0FMM] as when the `ℋ^q_dR(X/Y)` are flat:
> the ordinary — not derived — tensor product over `𝒪_Y` of the sheaf `Ω^p_{Y/S}` of relative
> `p`-forms of `Y` over `S` with the `q`-th de Rham cohomology sheaf of `X` over `Y`, read as a
> sheaf of `g^{-1}𝒪_S`-modules by restriction of scalars along `g^{-1}𝒪_S ⟶ 𝒪_Y`.
>
> The restriction of scalars is the one `Stacks.DeRhamSmooth.deRhamFirstPage` uses, so this module
> and `deRhamFirstPage f g p q` are objects of the same category; `deRhamFirstPageIsoFlat` is the
> isomorphism between them, granted the hypotheses the source does not discharge.

```lean
def deRhamFirstPageFlat (p q : ℤ) : Modules (inverseImageBase g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.12, Tag 0FMK](https://stacks.math.columbia.edu/tag/0FMK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
