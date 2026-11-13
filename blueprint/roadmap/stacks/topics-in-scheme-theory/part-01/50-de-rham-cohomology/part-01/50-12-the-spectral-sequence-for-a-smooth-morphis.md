---
declaration: section
origin: cited
lean: Stacks.DeRhamSmooth.deRhamSmoothFiltration_spec, Stacks.DeRhamSmooth.relativeDifferentialsShortComplex_shortExact_and_locally_split, Stacks.DeRhamSmooth.relativeDifferentialsExteriorFiltration_smooth_spec, Stacks.DeRhamSmooth.gradedPieceIsoGradedTargetComplexOfSmooth, Stacks.DeRhamSmooth.nonempty_gradedPiece_X_iso_pulledBackTargetFormsTensor, Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_smooth, Stacks.DeRhamRigidity.isLocallyFree_deRhamCohomologySheaf_of_proper_smooth_rat, Stacks.DeRhamSmooth.deRhamSmoothSpectralSequence_gaussManin
statement: formalized
proof: formalized
---

# 50.12 The spectral sequence for a smooth morphism

Section 50.12 of the Stacks Project, [Tag 0FMK](https://stacks.math.columbia.edu/tag/0FMK). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FMK, the section

[Tag 0FMK](https://stacks.math.columbia.edu/tag/0FMK) in the Stacks Project.

**`Stacks.DeRhamSmooth.deRhamSmoothFiltration_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltration.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltration.lean#L111). The attribute's comment: “the filtered complex: F^kΩ^•\_\{X/S} is the image of the wedge map out of Tot(f^\{-1}σ\_\{≥k}Ω^•\_\{Y/S} ⊗\_\{p^\{-1}O\_S} Ω^•\_\{X/S}), a decreasing filtration of Ω^•\_\{X/S} by subcomplexes with F^0Ω^•\_\{X/S} = Ω^•\_\{X/S}; it holds for every f, smooth or not”.

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

**`Stacks.DeRhamSmooth.relativeDifferentialsShortComplex_shortExact_and_locally_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean#L61). The attribute's comment: “the locally split short exact sequence 0 → f^*Ω\_\{Y/S} → Ω\_\{X/S} → Ω\_\{X/Y} → 0 of a smooth f (Tag 02K4)”.

> **Stacks Project, Section 0FMK: the locally split short exact sequence.** For `f : X ⟶ Y`
> smooth over a base `S`, the sequence `0 ⟶ f^*Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0` is short exact,
> and every point of `X` has an open neighbourhood over which it splits.

```lean
theorem relativeDifferentialsShortComplex_shortExact_and_locally_split [Smooth f] :
    (Scheme.Hom.relativeDifferentialsShortComplex f g).ShortExact ∧
      ∀ x : X, ∃ U : X.Opens, x ∈ U ∧
        Nonempty (Scheme.Hom.relativeDifferentialsShortComplexRestrict f g U).Splitting
```

**`Stacks.DeRhamSmooth.relativeDifferentialsExteriorFiltration_smooth_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean#L82). The attribute's comment: “the filtration Ω^p\_\{X/S} = F^0 ⊃ F^1 ⊃ … ⊃ F^\{p+1} = 0 induced by f^*Ω\_\{Y/S} ⊆ Ω\_\{X/S}, with gr^kΩ^p\_\{X/S} ≅ f^*Ω^k\_\{Y/S} ⊗\_\{O\_X} Ω^\{p-k}\_\{X/Y} for k = 0, …, p (for k < p the canonical comparison is an isomorphism; for k = p, gr^p = F^p since F^\{p+1} = 0)”.

> **Stacks Project, Section 0FMK: the filtration of `Ω^p_{X/S}` and its successive
> quotients.** For `f : X ⟶ Y` smooth over a base `S` and every `p`, the filtration of
> `Ω^p_{X/S} = ⋀^pΩ_{X/S}` induced by `f^*Ω_{Y/S} ⊆ Ω_{X/S}`, whose `k`-th step is the image of
> `⋀^k(f^*Ω_{Y/S}) ⊗_{𝒪_X} ⋀^{p-k}Ω_{X/S} ⟶ Ω^p_{X/S}`, satisfies:
>
> * `F^0Ω^p_{X/S} = Ω^p_{X/S}`, and the steps decrease;
> * `F^{p+1}Ω^p_{X/S} = 0`;
> * for `k < p`, writing `p = k + 1 + m`, the canonical morphism
>   `f^*Ω^k_{Y/S} ⊗_{𝒪_X} Ω^{m+1}_{X/Y} ⟶ gr^kΩ^p_{X/S}` is an isomorphism;
> * for `k = p`, `gr^pΩ^p_{X/S} = F^pΩ^p_{X/S} ≅ f^*Ω^p_{Y/S} ⊗_{𝒪_X} Ω^0_{X/Y}`.

```lean
theorem relativeDifferentialsExteriorFiltration_smooth_spec [Smooth f] (p : ℕ) :
    Scheme.Hom.relativeDifferentialsExteriorFiltration f g p 0 = ⊤ ∧
      Antitone (Scheme.Hom.relativeDifferentialsExteriorFiltration f g p) ∧
      IsZero (Subobject.underlying.obj
        (Scheme.Hom.relativeDifferentialsExteriorFiltration f g p (p + 1))) ∧
      (∀ k m : ℕ, k + 1 + m = p →
        IsIso (Scheme.Hom.relativeDifferentialsPullbackGradedComparison f g k m)) ∧
      Nonempty (Subobject.underlying.obj
          (Scheme.Hom.relativeDifferentialsExteriorFiltration f g p p) ≅
        (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor X.toRingedSpace.sheaf)).obj
          ((Scheme.Modules.pullback f).obj
              (AlgebraicGeometry.Scheme.Hom.relativeDifferentialForms g (p : ℤ)),
            AlgebraicGeometry.Scheme.Hom.relativeDifferentialForms f ((0 : ℕ) : ℤ)))
```

**`Stacks.DeRhamSmooth.gradedPieceIsoGradedTargetComplexOfSmooth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean#L127). The attribute's comment: “the graded pieces of the filtered complex: gr^kΩ^•\_\{X/S} ≅ f^\{-1}Ω^k\_\{Y/S}[-k] ⊗\_\{f^\{-1}O\_Y} Ω^•\_\{X/Y} as complexes, for f smooth”.

> **Stacks Project, Section 0FMK: the graded pieces of the filtered complex.** For
> `f : X ⟶ Y` smooth over a base `S` and every `k`, the `k`-th graded piece of the filtration of
> `Ω^•_{X/S}` by the forms pulled back from `Y` is
>
> `gr^kΩ^•_{X/S}  ≅  f^{-1}Ω^k_{Y/S}[-k] ⊗_{f^{-1}𝒪_Y} Ω^•_{X/Y}`,
>
> an isomorphism of complexes of `(f ∘ g)^{-1}𝒪_S`-modules on `X`. The target is
> `Stacks.DeRhamSmooth.gradedTargetComplex`: its degree-`n` term is
> `f^{-1}Ω^k_{Y/S} ⊗_{f^{-1}𝒪_Y} Ω^{n-k}_{X/Y}` (`Stacks.DeRhamSmooth.gradedTargetComplex_X`) and
> its differential is `(-1)^k(1 ⊗ d_{X/Y})`, the one the shift `[-k]` carries
> (`Stacks.DeRhamSmooth.gradedTargetComplex_d`).

```lean
def gradedPieceIsoGradedTargetComplexOfSmooth [Smooth f] (k : ℕ) :
    gradedPiece (inverseImageBase (f ≫ g)) (k : ℤ) (deRhamSmoothFiltration f g) ≅
      gradedTargetComplex f g k
```

**`Stacks.DeRhamSmooth.nonempty_gradedPiece_X_iso_pulledBackTargetFormsTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothFiltrationGradedPieces.lean#L139). The attribute's comment: “gr^kΩ^p\_\{X/S} ≅ f^\{-1}Ω^k\_\{Y/S} ⊗\_\{f^\{-1}O\_Y} Ω^\{p-k}\_\{X/Y} in each degree p = k + j, for f smooth”.

> **Stacks Project, Section 0FMK: the graded pieces in each degree, over `f^{-1}𝒪_Y`.** For
> `f : X ⟶ Y` smooth over a base `S` and `p = k + j`, the degree-`p` term of the `k`-th graded piece
> of the filtration of `Ω^•_{X/S}` is `f^{-1}Ω^k_{Y/S} ⊗_{f^{-1}𝒪_Y} Ω^j_{X/Y}`, read over
> `(f ∘ g)^{-1}𝒪_S`.

```lean
theorem nonempty_gradedPiece_X_iso_pulledBackTargetFormsTensor [Smooth f] (k j p : ℕ)
    (h : k + j = p) :
    Nonempty ((gradedPiece (inverseImageBase (f ≫ g)) (k : ℤ) (deRhamSmoothFiltration f g)).X
        (p : ℤ) ≅
      (coefficientRestriction f g).obj ((pulledBackTargetFormsTensor f g k).obj
        ((pushforward (toInverseImageBase f)).obj
          (AlgebraicGeometry.Scheme.Hom.relativeDifferentialForms f ((j : ℕ) : ℤ)))))
```

## Tag 0FMM, a lemma

[Tag 0FMM](https://stacks.math.columbia.edu/tag/0FMM) in the Stacks Project.

**`Stacks.DeRhamSmooth.exists_boundedDeRhamSpectralSequence_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceTheorem.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothSpectralSequenceTheorem.lean#L59). The attribute's comment: “the bounded spectral sequence of a quasi-compact, quasi-separated, smooth morphism, with first page H^q(Ω^p\_\{Y/S} ⊗ᴸ Rf\_*Ω^•\_\{X/Y}) and abutment R^\{p+q}f\_*Ω^•\_\{X/S}”.

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

**`Stacks.DeRhamRigidity.isLocallyFree_deRhamCohomologySheaf_of_proper_smooth_rat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/ArtinianRigidity/LocallyFreeRat.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/ArtinianRigidity/LocallyFreeRat.lean#L46). The attribute's comment: “if f is proper in addition to being smooth and S is a scheme over Q, then H^q\_dR(X/Y) is finite locally free (the sentence the source defers to a future reference)”.

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

**`Stacks.DeRhamSmooth.deRhamSmoothSpectralSequence_gaussManin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/GaussManinConnection.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/GaussManinConnection.lean#L103). The attribute's comment: “the first page Ω^p\_\{Y/S} ⊗ ℋ^q\_dR(X/Y) for flat ℋ^q\_dR, d\_1^\{0,q} the integrable Gauss–Manin connection and d\_1^\{•,q} its de Rham complex; the finite local freeness for proper f over ℚ is deferred by the source and omitted”.

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

**`Stacks.DeRhamSmooth.deRhamCohomologySheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean#L180). The attribute's comment: “the cohomology sheaves ℋ^q\_dR(X/Y) = H^q(Rf\_*Ω^•\_\{X/Y})”. References: SGA 7 XXII (3.3), “more general”.

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

**`Stacks.DeRhamSmooth.deRhamFirstPageFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/SmoothCohomologySheaves.lean#L193). The attribute's comment: “the module Ω^p\_\{Y/S} ⊗\_\{𝒪\_Y} ℋ^q\_dR(X/Y) of the flat case”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
