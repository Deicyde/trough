---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingPair, AlgebraicGeometry.Scheme.Hom.isRelativeDualizingComplex_derivedSections, AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.isRelativeDualizingComplex_derivedSections, AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.isIso_derivedSheafHomothety, AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.existsUnique_iso, AlgebraicGeometry.Scheme.Hom.exists_isRelativeDualizingComplex, AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.baseChange, Stacks.Duality.isRelativeDualizingComplex_relativeDualizingComplex
statement: formalized
proof: formalized
---

# 48.28 Relative dualizing complexes

Section 48.28 of the Stacks Project, [Tag 0E2S](https://stacks.math.columbia.edu/tag/0E2S). 10 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E2T, a definition

[Tag 0E2T](https://stacks.math.columbia.edu/tag/0E2T) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingPair`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingPair.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingPair.lean#L101).

> **Stacks 0E2T.** A relative dualizing complex for a flat, locally finitely presented
> morphism `f : X ⟶ S`, relative to an open `W ⊆ X ×_S X` through which the relative diagonal
> factors as a closed immersion `Δ : X ⟶ W`: a pair `(K, ξ)` consisting of an object `K` of
> `D(𝒪_X)` and a map `ξ : Δ_*𝒪_X ⟶ L pr₁^*K|_W` in `D(𝒪_W)` such that `K` is `S`-perfect
> (Stacks 0DI0) and `ξ` defines an isomorphism of `Δ_*𝒪_X` with
> `R SheafHom_{𝒪_W}(Δ_*𝒪_X, L pr₁^*K|_W)`.

```lean
structure IsRelativeDualizingPair [Flat f] [LocallyOfFinitePresentation f]
    (D : DiagonalOpen f) (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (ξ : D.diagonalObject ⟶ D.derivedPullbackProj K) : Prop
```

## Tag 0E2U, a lemma

[Tag 0E2U](https://stacks.math.columbia.edu/tag/0E2U) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isRelativeDualizingComplex_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexAffineRestriction.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexAffineRestriction.lean#L172). The attribute's comment: “variant: for an arbitrary family of certified tensorings, given the Tor-dimension clause of Tag 0DI2 at every object and an affine diagonal comparison datum; the tag is AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.isRelativeDualizingComplex\_derivedSections”.

> **Stacks 0E2U.** Let `f : X ⟶ S` be flat and locally of finite presentation and let
> `(K, ξ)` be a relative dualizing complex for `f` relative to an open `W ⊆ X ×_S X` through which
> the relative diagonal factors as a closed immersion. Let `U ⊆ X` be an affine open lying over an
> affine open `V ⊆ S`, and put `R = Γ(S, V)` and `A = Γ(X, U)`, an `R`-algebra through `f`. Then
> `RΓ(U, K)`, the object of `D(A)` corresponding to `K|_U` under Stacks 06Z0, is a relative
> dualizing complex for `R → A` in the sense of Stacks 0E2C.
>
> Two cited inputs are carried. `hTor` is the Tor-dimension clause of Stacks 0DI2, at every object
> of `D(𝒪_X)`: the affine comparison of Stacks 0DHY part (2) together with the affine-locality
> assembly that the Tor-dimension half of Stacks 0DI2 still lacks. `cmp` is the affine comparison
> of `Δ_*𝒪_X`, `L pr₁^*` and `R SheafHom_{𝒪_W}` at a chart of `W` over `A ⊗_R A`, that is
> Stacks 08DW part (2) and Stacks 0A6H (3)(a). The pseudo-coherence clause and the condition on
> `ξ` are proved. The statement at the source's hypotheses, at the derived tensor product of
> Stacks 06YU, is `isRelativeDualizingComplex_derivedSections` in the namespace
> `AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex`.

```lean
theorem isRelativeDualizingComplex_derivedSections [Flat f] [LocallyOfFinitePresentation f]
    (Dten : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring.{d', u}
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding))
    (D : DiagonalOpen f) (K : DerivedCategory X.Modules)
    (ξ : D.diagonalObject ⟶ D.derivedPullbackProj K)
    (hK : IsRelativeDualizingComplex f Dten D K ξ)
    {U : X.Opens} (hU : IsAffineOpen U) {V : S.Opens} (hV : IsAffineOpen V)
    (hUV : U ≤ f ⁻¹ᵁ V)
    [Algebra ↑Γ(S, V) ↑Γ(X, U)] [Module.Flat ↑Γ(S, V) ↑Γ(X, U)]
    [Algebra.FinitePresentation ↑Γ(S, V) ↑Γ(X, U)]
    (_halg : algebraMap ↑Γ(S, V) ↑Γ(X, U) = (f.appLE V U hUV).hom)
    (hTor : ∀ E : DerivedCategory X.Modules,
      RingedSpace.LocallyHasFiniteTorDimension
          (RingedSpace.inverseImage S.toRingedSpace f.base) Dten
          ((derivedScalarRestriction f).obj E) →
        StacksDraft.TorAmplitude.HasFiniteTorDimension
          (CochainComplex.DerivedTensor.canonicalDerivedTensorProduct ↑Γ(S, V)).tensor
          (StacksDraft.TorAmplitude.canonicalTensorComparison ↑Γ(S, V))
          (StacksDraft.TorAmplitude.canonicalTensorIsLeftDerived ↑Γ(S, V))
          ((ModuleCat.restrictScalars (algebraMap ↑Γ(S, V) ↑Γ(X, U))).mapDerivedCategory.obj
            ((derivedSectionsUnbounded X U).obj E)))
    (cmp : D.AffineDiagonalComparison U ↑Γ(S, V)) :
    Dualizing.IsRelativeDualizingComplex ↑Γ(S, V) ↑Γ(X, U)
      ((derivedSectionsUnbounded X U).obj K)
```

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.isRelativeDualizingComplex_derivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexAffineSections.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexAffineSections.lean#L267).

> **Stacks 0E2U.** Let `f : X ⟶ S` be flat and locally of finite presentation and let `(K, ξ)`
> be a relative dualizing complex for `f` (Stacks 0E2T), relative to an open `W ⊆ X ×_S X` through
> which the relative diagonal factors as a closed immersion. Let `U ⊆ X` be an affine open lying
> over an affine open `V ⊆ S`, and put `R = Γ(S, V)` and `A = Γ(X, U)`, an `R`-algebra through `f`.
> Then `RΓ(U, K)`, the object of `D(A)` corresponding to `K|_U` under Stacks 06Z0, is a relative
> dualizing complex for `R → A` in the sense of Stacks 0E2C.
>
> `S`-perfectness is read at the derived tensor product of Stacks 06YU on the open subspaces of
> `(X, f⁻¹𝒪_S)`, as in Stacks 0DI2.

```lean
theorem isRelativeDualizingComplex_derivedSections {D : DiagonalOpen f}
    {K : DerivedCategory X.Modules} {ξ : D.diagonalObject ⟶ D.derivedPullbackProj K}
    (hK : IsRelativeDualizingComplex f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ)
    {U : X.Opens} (hU : IsAffineOpen U) {V : S.Opens} (hV : IsAffineOpen V)
    (hUV : U ≤ f ⁻¹ᵁ V) :
    letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
    letI : Module.Flat Γ(S, V) Γ(X, U) := moduleFlat_appLE f hV hU hUV rfl
    letI : Algebra.FinitePresentation Γ(S, V) Γ(X, U) :=
      algebraFinitePresentation_appLE f hV hU hUV rfl
    Dualizing.IsRelativeDualizingComplex Γ(S, V) Γ(X, U)
      ((derivedSectionsUnbounded X U).obj K)
```

## Tag 0E2V, a lemma

[Tag 0E2V](https://stacks.math.columbia.edu/tag/0E2V) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.isIso_derivedSheafHomothety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexEndomorphisms.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexEndomorphisms.lean#L208).

> **Stacks 0E2V.** Let `f : X ⟶ S` be flat and locally of finite presentation and let `(K, ξ)`
> be a relative dualizing complex for `f` (Stacks 0E2T), relative to an open `W ⊆ X ×_S X` through
> which the relative diagonal factors as a closed immersion. Then the homothety
> `𝒪_X ⟶ R𝓗om_{𝒪_X}(K, K)` is an isomorphism.
>
> `S`-perfectness is read at the derived tensor product of Stacks 06YU on the open subspaces of
> `(X, f⁻¹𝒪_S)`, as in Stacks 0DI2 and Stacks 0E2U. The proof is the source's: on every compatible
> pair of affine opens `RΓ(U, K)` is a relative dualizing complex for `Γ(S, V) → Γ(X, U)` by
> Stacks 0E2U, and the algebraic case is Stacks 0E2G.

```lean
theorem isIso_derivedSheafHomothety {D : DiagonalOpen f}
    {K : DerivedCategory X.Modules} {ξ : D.diagonalObject ⟶ D.derivedPullbackProj K}
    (hK : IsRelativeDualizingComplex f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ) :
    IsIso (Stacks.SheafOfModules.derivedSheafHomothety X.sheaf K)
```

## Tag 0E2W, a lemma

[Tag 0E2W](https://stacks.math.columbia.edu/tag/0E2W) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexUniqueIso.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexUniqueIso.lean#L48).

> **Stacks 0E2W.** Let `f : X ⟶ S` be flat and locally of finite presentation, and let `W` be an
> open of `X ×_S X` through which the relative diagonal factors as a closed immersion
> `Δ : X ⟶ W`. If `(K, ξ)` and `(L, η)` are relative dualizing complexes on `X/S` relative to `W`
> (Stacks 0E2T), then there is a unique isomorphism `α : K ≅ L` sending `ξ` to `η`, that is with
> `ξ ≫ L pr₁^*α|_W = η`.

```lean
theorem existsUnique_iso {D : DiagonalOpen f}
    {K L : DerivedCategory (OXMod.{u, u} X.toRingedSpace)}
    {ξ : D.diagonalObject ⟶ D.derivedPullbackProj K}
    {η : D.diagonalObject ⟶ D.derivedPullbackProj L}
    (hK : IsRelativeDualizingComplex f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ)
    (hL : IsRelativeDualizingComplex f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D L η) :
    ∃! α : K ≅ L, ξ ≫ D.derivedPullbackProjMap α.hom = η
```

## Tag 0E2X, a lemma

[Tag 0E2X](https://stacks.math.columbia.edu/tag/0E2X) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.exists_isRelativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexExistence.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexExistence.lean#L1025).

> **Stacks 0E2X.** Let `f : X ⟶ S` be flat and locally of finite presentation. There exists a
> relative dualizing complex `(K, ξ)` (Stacks 0E2T), relative to any open `W ⊆ X ×_S X` through
> which the relative diagonal factors as a closed immersion: `K ∈ D(𝒪_X)` is `S`-perfect and
> `ξ : Δ_*𝒪_X ⟶ L pr₁^*K|_W` defines an isomorphism
> `Δ_*𝒪_X ≅ R SheafHom_{𝒪_W}(Δ_*𝒪_X, L pr₁^*K|_W)`.
>
> `S`-perfectness is read at a family `Dten` of derived tensor products on the open subspaces of
> `(X, f⁻¹𝒪_S)` whose underived tensor products are those of sheaves of modules, so that it is
> Stacks 0DI0 (`AlgebraicGeometry.Scheme.Hom.isPerfectRelativeTo_iff_isRelativelyPerfect`).
>
> The derived categories of the inverse-image ringed spaces `(X, f⁻¹𝒪_S)|_U` are those of
> `CategoryTheory.HasDerivedCategory.standard`, the model at which the chart step (Stacks 0E2F read
> through Stacks 0E2U, `exists_isRelativeDualizingComplex_chart`), the restriction of relative
> dualizing complexes and Stacks 0E2W are stated. They cannot be left arbitrary: the Tor clause of
> `S`-perfectness is read on `(derivedScalarRestriction f).obj K` in the chosen model of
> `D(f⁻¹𝒪_S)`, and carrying it from one model to another needs the comparison of the two models of
> the derived category, which the library does not provide.

```lean
theorem exists_isRelativeDualizingComplex [Flat f] [LocallyOfFinitePresentation f]
    (Dten : ∀ U : TopologicalSpace.Opens
        (RingedSpace.inverseImage S.toRingedSpace f.base).carrier,
      RingedSpace.CertifiedDerivedSheafTensoring
        ((RingedSpace.inverseImage S.toRingedSpace f.base).restrict U.isOpenEmbedding))
    (hD : IsGenuineRelativeTensorFamily f Dten) (D : DiagonalOpen f) :
    ∃ (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
      (ξ : D.diagonalObject ⟶ D.derivedPullbackProj K),
      IsRelativeDualizingComplex f Dten D K ξ
```

## Tag 0E2Y, a lemma

[Tag 0E2Y](https://stacks.math.columbia.edu/tag/0E2Y) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexBaseChangeTheorem.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexBaseChangeTheorem.lean#L154). The attribute's comment: “As in the source's proof, `W'` is any diagonal open of `f'` with `(g' × g')(W') ⊆ W`, and `w : W' ⟶ W` is the induced morphism.”.

> **Stacks 0E2Y: base change of a relative dualizing complex.** Let `X' = X ×_S S'` with
> projections `g' : X' ⟶ X` and `f' : X' ⟶ S'`, `f` flat and locally of finite presentation, and
> let `(K, ξ)` be a relative dualizing complex for `f` relative to a diagonal open `W`. For a
> diagonal open `W'` of `f'` with `(g' × g')(W') ⊆ W` and `w : W' ⟶ W` the induced morphism, set
> `K' = L(g')^*K` and let `ξ'` be the derived base change of `ξ`: `Lw^*ξ` read through
> `Lw^*Δ_*𝒪_X = Δ'_*𝒪_{X'}` (the base change of `Δ_*` across the Tor independent diagonal square)
> and transitivity of derived pullback. Then `(K', ξ')` is a relative dualizing complex for `f'`
> relative to `W'`.

```lean
theorem baseChange (hpb : IsPullback g' f' f g) {D : DiagonalOpen f}
    {K : DerivedCategory X.Modules} {ξ : D.diagonalObject ⟶ D.derivedPullbackProj K}
    (hK : IsRelativeDualizingComplex f
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ)
    (D' : DiagonalOpen f') (w : D'.W ⟶ D.W)
    (hw : w ≫ D.ι = D'.ι ≫ pullbackMapOfIsPullback hpb) :
    haveI : Flat f' := MorphismProperty.of_isPullback (P := @Flat) hpb (inferInstance : Flat f)
    haveI : LocallyOfFinitePresentation f' :=
      MorphismProperty.of_isPullback (P := @LocallyOfFinitePresentation) hpb
        (inferInstance : LocallyOfFinitePresentation f)
    IsRelativeDualizingComplex f'
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S'.toRingedSpace f'.base)) D'
      (DiagonalOpen.baseChangeComplex g' K)
      (D.baseChangeDiagonalMap D' g' w (DiagonalOpen.proj_baseChange hpb D D' w hw)
        (DiagonalOpen.baseChangeDiagonalIso hpb D D' w hw) K ξ)
```

## Tag 0E2Z, a lemma

[Tag 0E2Z](https://stacks.math.columbia.edu/tag/0E2Z) in the Stacks Project.

**`Stacks.Duality.isRelativeDualizingComplex_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexOfProperFlat.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexOfProperFlat.lean#L61).

> **Stacks Project, Tag 0E2Z.** Let `S` be a quasi-compact and quasi-separated scheme and let
> `f : X ⟶ S` be a proper, flat morphism of finite presentation. The relative dualizing complex
> `ω_{X/S}^• = a(𝒪_S)` of [Stacks, Remark 0B6S]
> (`Stacks.Duality.StandardModel.relativeDualizingComplex`) together with the map
> `ξ : Δ_*𝒪_X ⟶ L pr₁^*ω_{X/S}^•` coming from the isomorphism `𝒪_X ≅ c(L pr₁^*ω_{X/S}^•)` of
> [Stacks, Tag 0E2Q] (`Stacks.Duality.relativeDualizingComplexDiagonalMap`) is a relative
> dualizing complex in the sense of [Stacks, Definition 0E2T], for the open `W = X ×_S X` (the
> morphism being separated) and the derived tensor product of sheaves of modules.
>
> Of finite presentation is `LocallyOfFinitePresentation f` together with the quasi-compactness and
> quasi-separatedness that properness includes.

```lean
theorem isRelativeDualizingComplex_relativeDualizingComplex {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace (pullback f f : Scheme.{u}) :=
      QuasiCompact.compactSpace_of_compactSpace (pullback.fst f f)
    haveI : QuasiSeparatedSpace (pullback f f : Scheme.{u}) :=
      quasiSeparatedSpace_of_quasiSeparated (pullback.fst f f)
    @Scheme.Hom.IsRelativeDualizingComplex X S f (HasDerivedCategory.standard _)
      (fun _ => HasDerivedCategory.standard _) _ _
      (@RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base) (fun _ => HasDerivedCategory.standard _))
      (Scheme.Hom.DiagonalOpen.ofIsSeparated f) (StandardModel.relativeDualizingComplex f).obj
      (relativeDualizingComplexDiagonalMap f)
```

## Tag 0E4P, a remark

[Tag 0E4P](https://stacks.math.columbia.edu/tag/0E4P) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.relativeDualizingComplex_baseChange_twistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexProperFlatBaseChange.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexProperFlatBaseChange.lean#L193).

> **Relative dualizing complexes and base change.** Let `f : X ⟶ S` be flat, proper and of
> finite presentation, and let `W` be a diagonal open of `f`. There is a relative dualizing complex
> `(ω_{X/S}^•, ξ)` for `f` relative to `W` (Stacks 0E2X), and for every such pair, every morphism
> `g : S' ⟶ S` with `S'` quasi-compact and quasi-separated, with base change `f' : X' ⟶ S'` and
> projection `g' : X' ⟶ X`, and every diagonal open `W'` of `f'` mapped into `W` by `g' × g'`,
> there is a unique isomorphism `ω_{X'/S'}^• = a'(𝒪_{S'}) ≅ L(g')^*ω_{X/S}^•` compatible with the
> map of Equation 0E2Q (restricted to `W'`) and the derived base change `L(g')^*ξ` of
> Stacks 0E2Y.

```lean
theorem relativeDualizingComplex_baseChange_twistedInverseImage {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f] (D : DiagonalOpen f) :
    (∃ (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
      (ξ : D.diagonalObject ⟶ D.derivedPullbackProj K),
      IsRelativeDualizingComplex f (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ) ∧
    ∀ (K : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
      (ξ : D.diagonalObject ⟶ D.derivedPullbackProj K),
      IsRelativeDualizingComplex f (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily
        (RingedSpace.inverseImage S.toRingedSpace f.base)) D K ξ →
      ∀ {X' S' : Scheme.{u}} [CompactSpace S'] [QuasiSeparatedSpace S'] {g : S' ⟶ S}
        {g' : X' ⟶ X} {f' : X' ⟶ S'} (hpb : IsPullback g' f' f g)
        (D' : DiagonalOpen f') (w : D'.W ⟶ D.W)
        (hw : w ≫ D.ι = D'.ι ≫ pullbackMapOfIsPullback hpb),
        haveI : IsProper f' := MorphismProperty.of_isPullback (P := @IsProper) hpb inferInstance
        haveI : Flat f' := MorphismProperty.of_isPullback (P := @Flat) hpb inferInstance
        haveI : LocallyOfFinitePresentation f' :=
          MorphismProperty.of_isPullback (P := @LocallyOfFinitePresentation) hpb inferInstance
        haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
        haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
        haveI : CompactSpace (pullback f' f' : Scheme.{u}) :=
          QuasiCompact.compactSpace_of_compactSpace (pullback.fst f' f')
        haveI : QuasiSeparatedSpace (pullback f' f' : Scheme.{u}) :=
          quasiSeparatedSpace_of_quasiSeparated (pullback.fst f' f')
        ∃! φ : (Stacks.Duality.StandardModel.relativeDualizingComplex f').obj ≅
            DiagonalOpen.baseChangeComplex g' K,
          (DiagonalOpen.ofIsSeparated f').restrictDiagonalMap D' D'.ι
              (DiagonalOpen.comp_ι_ofIsSeparated f' D')
              (Stacks.Duality.StandardModel.relativeDualizingComplex f').obj
              (Stacks.Duality.relativeDualizingComplexDiagonalMap f') ≫
              D'.derivedPullbackProjMap φ.hom =
            D.baseChangeDiagonalMap D' g' w (DiagonalOpen.proj_baseChange hpb D D' w hw)
              (DiagonalOpen.baseChangeDiagonalIso hpb D D' w hw) K ξ
```

## Tag 0E9W, a lemma

[Tag 0E9W](https://stacks.math.columbia.edu/tag/0E9W) in the Stacks Project.

**`Stacks.Duality.exists_isRelativeDualizingComplex_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizing.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativeDualizing.lean#L269).

> **Stacks Project, Tag 0E9W.** In Situation 48.16.1 (`S` Noetherian), let
> `f : X ⟶ Y` be a flat morphism of `FTS S`, with `f^!` computed at any compactification `j`. Then
> `f^!𝒪_Y` is the first component of a relative dualizing complex for `X` over `Y`
> (Definition 0E2T): for every open `W ⊆ X ×_Y X` through which the diagonal factors as a closed
> immersion `Δ : X ⟶ W` there is `ξ : Δ_*𝒪_X ⟶ L pr₁^* f^!𝒪_Y|_W` making `(f^!𝒪_Y, ξ)` a relative
> dualizing complex.

```lean
theorem exists_isRelativeDualizingComplex_upperShriek (D : f.left.DiagonalOpen) :
    letI := locallyOfFinitePresentation_left f
    ∃ ξ : D.diagonalObject ⟶ D.derivedPullbackProj (relativeDualizingComplexObj f j),
      Scheme.Hom.IsRelativeDualizingComplex.{u + 1, u} f.left
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _) D
        (relativeDualizingComplexObj f j) ξ
```

## Tag 0E30, a lemma

[Tag 0E30](https://stacks.math.columbia.edu/tag/0E30) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsRelativeDualizingComplex.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexComposite.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexComposite.lean#L97).

> **Stacks 0E30.** Let `f : Y ⟶ X` and `g : X ⟶ S` be flat and locally of finite
> presentation, and let `(K, ξ)` and `(M, η)` be relative dualizing complexes for `g` and `f`.
> Then `(M ⊗ᴸ Lf^*K, ζ)` is a relative dualizing complex for `f ≫ g`, for a suitable `ζ`, on the
> diagonal open `W' = Dg.comp Df` of the source's proof.
>
> The source's proof applies Stacks 0E2N with tensor factor `Lq^*M` over `𝒪_{Y ×_S Y}`, which
> needs Tor amplitude of `Lq^*M` over `𝒪_{Y ×_S Y}`; this fails for `X = S = Spec k`,
> `Y = Spec B`, `B` Artinian non-Gorenstein, `M = ω_B`. The proof here uses instead the Tor
> amplitude of `Lq^*M` relative to `f × f`, as the algebraic version 0E2H does over `A ⊗_R A`.

```lean
theorem IsRelativeDualizingComplex.comp {X Y S : Scheme.{u}} (g : X ⟶ S) (f : Y ⟶ X)
    [Flat g] [LocallyOfFinitePresentation g] [Flat f] [LocallyOfFinitePresentation f]
    {Dg : DiagonalOpen g} {K : DerivedCategory X.Modules}
    {ξ : Dg.diagonalObject ⟶ Dg.derivedPullbackProj K}
    (hK : IsRelativeDualizingComplex g (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _)
      Dg K ξ)
    {Df : DiagonalOpen f} {M : DerivedCategory Y.Modules}
    {η : Df.diagonalObject ⟶ Df.derivedPullbackProj M}
    (hM : IsRelativeDualizingComplex f (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _)
      Df M η) :
    ∃ ζ, IsRelativeDualizingComplex (f ≫ g)
      (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _) (Dg.comp Df)
      (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
        Y.toRingedSpace.sheaf).obj M).obj
        ((derivedPullback f.toLRSHom.toShHom).obj K)) ζ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.28, Tag 0E2S](https://stacks.math.columbia.edu/tag/0E2S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
