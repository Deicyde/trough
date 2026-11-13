---
declaration: section
origin: cited
lean: Crystalline.dpDifferentialsSheaf, Crystalline.universalDPSchemeDerivation_isUniversal, Crystalline.existsUnique_siteDPDesc, Crystalline.universalDerivation_postcomp_siteDPQuotient, Crystalline.siteDPQuotient_relation, Crystalline.existsUnique_siteDPQuotient_desc, Crystalline.GlobalCrystallineSituation.SmallSite.existsUnique_crisDesc, Crystalline.GlobalCrystallineSituation.SmallSite.SDerivation
statement: formalized
proof: formalized
---

# 60.12 Sheaf of differentials

Section 60.12 of the Stacks Project, [Tag 07IW](https://stacks.math.columbia.edu/tag/07IW). 7 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07IW, the section

[Tag 07IW](https://stacks.math.columbia.edu/tag/07IW) in the Stacks Project.

**`Crystalline.dpDifferentialsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean#L493). The attribute's comment: “the sheaf Ω\_\{T/Y,δ} of divided power differentials of a divided power scheme over a scheme”.

> **The sheaf of divided power differentials** `Ω_{T/Y,δ}` of a divided power scheme `T` over a
> scheme `Y`: the sheaf of `𝒪_T`-modules associated with the presheaf of divided power
> differentials.

```lean
def dpDifferentialsSheaf : T.scheme.Modules
```

**`Crystalline.universalDPSchemeDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean, line 692](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean#L692). The attribute's comment: “the universal divided power derivation d\_\{T/Y,δ} and its universal property”.

> **The universal property of the sheaf of divided power differentials.**  Every divided power
> derivation of `𝒪_T` over `Y` into a sheaf of `𝒪_T`-modules factors uniquely through the universal
> one.

```lean
theorem universalDPSchemeDerivation_isUniversal :
    (universalDPSchemeDerivation T Y f).IsUniversal
```

**`Crystalline.existsUnique_siteDPDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean#L372). The attribute's comment: “the universal divided power 𝒜-derivation d\_\{ℬ/𝒜,δ} : ℬ → Ω\_\{ℬ/𝒜,δ} on a site”.

> **The universal property of `d_{ℬ/𝒜,δ}`** ([Stacks, Tag 07IW]).  Every divided power
> `𝒜`-derivation of `ℬ` into a sheaf of `ℬ`-modules factors through the universal divided power
> derivation by a unique map of sheaves of modules.  The site and the base `𝒜` are arbitrary: `𝒜`
> is a presheaf of commutative rings, so that `𝒜 = f⁻¹𝒪'` for a morphism of ringed topoi may be
> used in its presheaf form, and the modules live in any universe `max u w` in which the site
> admits sheafification.

```lean
theorem existsUnique_siteDPDesc (F : SheafOfModules.{max u w} (ringSheaf B))
    (D : PresheafOfModulesOfCommRing.Derivation' F.val φ) (hD : IsSiteDPDerivation φ δ D) :
    ∃! f : siteDPDifferentials.{w} φ δ ⟶ F,
      (siteDPUniversalDerivation.{w} φ δ).postcomp f.val = D
```

**`Crystalline.universalDerivation_postcomp_siteDPQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean#L408). The attribute's comment: “d\_\{ℬ/𝒜,δ} is the composite of d\_\{ℬ/𝒜} : ℬ → Ω\_\{ℬ/𝒜} with Ω\_\{ℬ/𝒜} → Ω\_\{ℬ/𝒜,δ}”.

> **`d_{ℬ/𝒜,δ}` is the composite `ℬ ⟶ Ω_{ℬ/𝒜} ⟶ Ω_{ℬ/𝒜,δ}`** of the universal derivation
> of [Stacks, Tag 04BL] with `Crystalline.siteDPQuotient`.

```lean
theorem universalDerivation_postcomp_siteDPQuotient :
    (universalDerivation A B φ).postcomp (siteDPQuotient φ δ).val =
      siteDPUniversalDerivation.{u} φ.hom δ.toPresheafDividedPowers
```

**`Crystalline.siteDPQuotient_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean#L452). The attribute's comment: “Ω\_\{ℬ/𝒜} → Ω\_\{ℬ/𝒜,δ} kills the sections d(δ\_n x) - δ\_\{n-1}(x) d(x)”.

> **The map `Ω_{ℬ/𝒜} ⟶ Ω_{ℬ/𝒜,δ}` kills the local sections
> `d_{ℬ/𝒜}(δ_n x) - δ_{n-1}(x) d_{ℬ/𝒜}(x)`.**

```lean
theorem siteDPQuotient_relation (U : Cᵒᵖ) (n : ℕ) (x : B.obj.obj U)
    (hx : x ∈ sectionIdeal B I U) :
    ((siteDPQuotient φ δ).val.app U).hom (siteDPRelation φ δ U n x) = 0
```

**`Crystalline.existsUnique_siteDPQuotient_desc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SiteDividedPowerDifferentials.lean#L464). The attribute's comment: “Ω\_\{ℬ/𝒜} → Ω\_\{ℬ/𝒜,δ} is the quotient by the submodule generated by the sections d(δ\_n x) - δ\_\{n-1}(x) d(x)”.

> **`Ω_{ℬ/𝒜,δ}` is the quotient of `Ω_{ℬ/𝒜}` by the submodule generated by the local sections
> `d_{ℬ/𝒜}(δ_n x) - δ_{n-1}(x) d_{ℬ/𝒜}(x)`.**  Every map of sheaves of `ℬ`-modules out of
> `Ω_{ℬ/𝒜}` killing those sections factors uniquely through `Ω_{ℬ/𝒜} ⟶ Ω_{ℬ/𝒜,δ}`.

```lean
theorem existsUnique_siteDPQuotient_desc (F : SheafOfModules.{u} (ringSheaf B))
    (g : moduleOfDifferentials A B φ ⟶ F)
    (hg : ∀ (U : Cᵒᵖ) (n : ℕ) (x : B.obj.obj U), x ∈ sectionIdeal B I U →
      (g.val.app U).hom (siteDPRelation φ δ U n x) = 0) :
    ∃! h : siteDPDifferentials.{u} φ.hom δ.toPresheafDividedPowers ⟶ F,
      siteDPQuotient φ δ ≫ h = g
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.existsUnique_crisDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDividedPowerDifferentials.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDividedPowerDifferentials.lean#L218). The attribute's comment: “Ω\_\{X/S} and the universal divided power derivation d\_\{X/S} : 𝒪\_\{X/S} → Ω\_\{X/S} on Cris(X/S), from the construction on a site applied to (X/S)\_cris → Sh(S\_Zar)”.

> **The universal property of `d_{X/S}`** ([Stacks, Tag 07IW]).  Every `S`-derivation of
> `𝒪_{X/S}` into a sheaf of `𝒪_{X/S}`-modules on `Cris(X/S)`, that is every derivation killing the
> sections pulled back from the opens of `S` and obeying the divided power chain rule on `𝒥_{X/S}`
> ([Stacks, Tag 07IX]), factors through `d_{X/S}` by a unique map of sheaves of modules.

```lean
theorem existsUnique_crisDesc (F : SheafOfModules.{u + 1} (crisStructureRingSheaf S))
    (D : PresheafOfModulesOfCommRing.Derivation' (M := F.val) (crisBaseMap S))
    (hD : IsSiteDPDerivation.{u + 1, u + 1, u, u} (M := F.val) (crisBaseMap S)
      (crisDividedPowers S) D) :
    ∃! f : crisDifferentials S ⟶ F, (crisUniversalDerivation S).postcomp f.val = D
```

## Tag 07IX, a definition

[Tag 07IX](https://stacks.math.columbia.edu/tag/07IX) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.SDerivation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean, line 533](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean#L533). The attribute's comment: “S-derivation O\_\{X/S} → F into a sheaf F of O\_\{X/S}-modules on Cris(X/S), as SDerivation S F.val”.

> **An `S`-derivation on the small crystalline site** ([Stacks, Tag 07IX]).  For a presheaf `F`
> of `𝒪_{X/S}`-modules on `Cris(X/S)`, a map of presheaves of abelian groups `𝒪_{X/S} → F` such
> that for every object `(U, T, δ)` and *every* open `V ⊆ S` through which `T → S` factors, the map
> `Γ(T, 𝒪_T) → F(U, T, δ)` is a divided power `Γ(V, 𝒪_V)`-derivation.  For `F` the underlying
> presheaf `ℱ.val` of a sheaf `ℱ` of `𝒪_{X/S}`-modules this is the definition of the source.

```lean
structure SDerivation (F : PresheafOfModules.{u} (structureSheaf S).obj)
```

## Tag 07IY, a lemma

[Tag 07IY](https://stacks.math.columbia.edu/tag/07IY) in the Stacks Project.

**`Crystalline.affineSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsAffineSections.lean, line 554](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsAffineSections.lean#L554). The attribute's comment: “clause (2): the sections over an affine open”.

> For an affine open `W` of a divided power scheme `T` lying over an affine open `V` of the base
> `Y`, the sections of the sheaf `Ω_{T/Y,δ}` of divided power differentials over `W` are the module
> `Ω¹_{Γ(W,𝒪_T)/Γ(V,𝒪_Y),δ}` of divided power differentials of the corresponding rings.

```lean
def affineSectionsEquiv :
    Γ(dpDifferentialsSheaf T Y f, W) ≃ₗ[Γ(T.scheme, W)]
      ↑(dpDifferentials (f.appLE V W h) (T.dividedPowers.dividedPowers (op W)))
```

**`Crystalline.dpDifferentialsSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsQuasicoherent.lean, line 764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsQuasicoherent.lean#L764). The attribute's comment: “quasi-coherence of the sheaf of divided power differentials”.

> **The sheaf of divided power differentials is quasi-coherent**, being the quotient of the
> quasi-coherent sheaf of relative differentials by a subsheaf which, over an affine open, is the
> image of a free module.

```lean
instance dpDifferentialsSheaf_isQuasicoherent :
    (dpDifferentialsSheaf T Y f).IsQuasicoherent
```

## Tag 07IZ, a lemma

[Tag 07IZ](https://stacks.math.columbia.edu/tag/07IZ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysDifferentialsSheafRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean#L458). The attribute's comment: “(Ω\_\{X/S})\_T = Ω\_\{T/S,δ}, as sheaves of 𝒪\_T-modules on T\_Zar”.

> **Stacks Project, Tag 07IZ, the module identification.**  For an object `(U, T, δ)` of
> `Cris(X/S)` the restriction `(Ω_{X/S})_T` of the sheaf of crystalline differentials to `T_Zar` is
> the sheaf `Ω_{T/S,δ}` of divided power differentials of `T` over `S`, as sheaves of
> `𝒪_T`-modules.

```lean
def crysDifferentialsSheafRestrictionIso (A : CrystallineThickening S) :
    dpDifferentialsSheaf A.obj.thickening.target S.S.scheme A.obj.toBase.hom ≅
      crysDifferentialsSheafRestriction A
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysDifferentialsSheafRestrictionIso_hom_app_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystallineDifferentialsSheaf.lean#L489). The attribute's comment: “d\_\{X/S}|\_T = d\_\{T/S,δ}”.

> **Stacks Project, Tag 07IZ, the derivations.**  Under the identification
> `Ω_{T/S,δ} ≅ (Ω_{X/S})_T` of `crysDifferentialsSheafRestrictionIso`, the universal divided power
> derivation `d_{T/S,δ}` is the restriction `d_{X/S}|_T` of the universal derivation of `Ω_{X/S}`:
> for an open `W` of `T` and a section `b` of `𝒪_T` over `W`, the section `d_{T/S,δ} b` of
> `Ω_{T/S,δ}` over `W` corresponds to `d_{X/S} b` over the restricted object `(U ∩ W, W, δ|_W)`.

```lean
theorem crysDifferentialsSheafRestrictionIso_hom_app_d (A : CrystallineThickening S)
    (W : A.obj.thickening.target.scheme.Opens) (b : Γ(A.obj.thickening.target.scheme, W)) :
    (crysDifferentialsSheafRestrictionIso A).hom.val.app (op W)
        ((universalDPSchemeDerivation A.obj.thickening.target S.S.scheme
          A.obj.toBase.hom).app W b) =
      crysSheafD S (A.restrictOpen W) (openTopRes W b)
```

## Tag 07J0, a lemma

[Tag 07J0](https://stacks.math.columbia.edu/tag/07J0) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.affineCrysFormsSheafOneEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AffineDifferentialsSheafSections.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/AffineDifferentialsSheafSections.lean#L175). The attribute's comment: “Γ((U, T, δ), Ω\_\{X/S}) = Ω\_\{Γ(T, 𝒪\_T)/Γ(V, 𝒪\_V), δ} for the sheaf Ω\_\{X/S} (crysFormsSheaf S 1, the sheaf associated with ⋀¹ of the crystalline differentials) on an affine object of Cris(X/S) mapping into an affine open V ⊆ S”.

> **[Stacks, Tag 07J0]: the sections of the sheaf `Ω_{X/S}` over an affine object.**  For an
> object `(U, T, δ)` of `Cris(X/S)` with `T` affine whose structure morphism factors through an
> affine open `V ⊆ S`, the sections over `(U, T, δ)` of the sheaf `Ω_{X/S}` — the sheaf
> `crysFormsSheaf S 1` associated with `⋀¹ Ω_{X/S} = Ω_{X/S}` — are the divided power differentials
> `Ω_{Γ(T, 𝒪_T)/Γ(V, 𝒪_V), δ}`, as modules over `Γ(T, 𝒪_T)` (the sections of `𝒪_{X/S}` there).
>
> It is the inverse of the sheafification map on those sections
> (`bijective_toCrysFormsSheaf_app_of_isAffine`), followed by `⋀¹ M = M` and the presheaf-level
> identification `Crystalline.GlobalCrystallineSituation.affineCrysDifferentialsIso`.

```lean
def affineCrysFormsSheafOneEquiv [IsAffine A.obj.thickening.target.scheme]
    {V : S.S.scheme.Opens}
    (h : (⊤ : A.obj.thickening.target.scheme.Opens) ≤ A.obj.toBase.hom ⁻¹ᵁ V)
    (hV : IsAffineOpen V) :
    (crysFormsSheaf S 1).val.obj (op A) ≃ₗ[crysFormRing S A] affineCrysDifferentialsObj S A.obj h
```

## Tag 07J1, a lemma

[Tag 07J1](https://stacks.math.columbia.edu/tag/07J1) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.isClosedImmersion_smallSelfProductAmbientDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L1049). The attribute's comment: “the diagonal Δ : T ⟶ T(1) is a closed immersion”.

> **Stacks Project, Tag 07J1.**  The ambient diagonal `Δ : T ⟶ T(1)` of a self-product taken in
> `Cris(X/S)` is a closed immersion.  It is surjective on stalks because it is a section of either
> coprojection, and a closed embedding because it is a homeomorphism on spaces: that is `U(1) = U`
> read through the immersions of the two thickenings.

```lean
theorem isClosedImmersion_smallSelfProductAmbientDiagonal
    (h : IsLimit (BinaryFan.mk pr₀ pr₁)) :
    IsClosedImmersion (smallSelfProductAmbientDiagonal h).hom
```

**`Crystalline.GlobalCrystallineSituation.ker_ideal_smallSelfProductAmbientDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 1066](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L1066). The attribute's comment: “K is the quasi-coherent ideal sheaf of the closed immersion Δ, on affine opens”.

> **Stacks Project, Tag 07J1.**  On an affine open of `T(1)` the quasi-coherent sheaf of ideals
> of the closed immersion `Δ` is the diagonal ideal.  This is what reconciles the presentation of
> `K` used here and in `SelfProductDiagonal.lean` — the kernel of `Δ` on sections over each open —
> with the source's, the quasi-coherent sheaf of ideals of the closed immersion `Δ`.

```lean
theorem ker_ideal_smallSelfProductAmbientDiagonal (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (W : D.obj.thickening.target.scheme.affineOpens) :
    (smallSelfProductAmbientDiagonal h).hom.ker.ideal W =
      smallSelfProductDiagonalIdeal h (W : D.obj.thickening.target.scheme.Opens)
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductConormalSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalSheaf.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalSheaf.lean#L295). The attribute's comment: “the sheaf of 𝒪\_T-modules K/K^\{[2]} of the second assertion, the sheaf associated with the conormal modules over the opens p₀⁻¹V ⊓ p₁⁻¹V of T(1)”.

> **The sheaf of `𝒪_T`-modules `K/K^{[2]}`**: the sheaf associated with the conormal presheaf
> `V ↦ K/K^{[2]}` over `p₀⁻¹V ⊓ p₁⁻¹V`.  The diagonal is a homeomorphism `T ≅ T(1)` on spaces, so
> this is the quotient of the ideal sheaf `K` of `Δ` by its divided square, read on `T`, with
> `𝒪_T`-module structure through `Δ`.

```lean
def smallSelfProductConormalSheaf (h : IsLimit (BinaryFan.mk pr₀ pr₁)) :
    SheafOfModules.{u} B.obj.thickening.target.scheme.ringCatSheaf
```

**`Crystalline.GlobalCrystallineSituation.restrictedCrysDifferentialsSheafIsoConormalSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalSheaf.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalSheaf.lean#L346). The attribute's comment: “second assertion: (Ω\_\{X/S})\_T ≅ K/K^\{[2]} as sheaves of 𝒪\_T-modules, d f ↦ [p₁^♯ f - p₀^♯ f]; the first assertion is smallSelfProductDiagonalIdeal\_le and smallSelfProductDiagonalIdeal\_isSubDPIdeal”.

> **Stacks Project, Tag 07J1, second assertion.**  For a self-product
> `(U(1), T(1), δ(1))` of an object `(U, T, δ)` of `Cris(X/S)`, with `K` the ideal of the diagonal
> `Δ : T ⟶ T(1)`, the sheaf of `𝒪_T`-modules `(Ω_{X/S})_T` is isomorphic to `K/K^{[2]}`.  The
> isomorphism is the sheafification of the comparison morphism, which sends `d f` to the class of
> `p₁^♯ f - p₀^♯ f` (`smallSelfProductConormalComparison_d`).

```lean
def restrictedCrysDifferentialsSheafIsoConormalSheaf (h : IsLimit (BinaryFan.mk pr₀ pr₁)) :
    restrictedCrysDifferentialsSheaf S B.obj ≅ smallSelfProductConormalSheaf h
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductDiagonalIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean#L306). The attribute's comment: “K ⊆ J\_\{T(1)}; sections over each open, K the kernel of Δ on sections”.

> For a self-product `(U(1), T(1), δ(1))` of an object `(U, T, δ)` of `Cris(X/S)` with itself,
> the diagonal ideal `K` of `Δ : T ⟶ T(1)` is contained in the divided power ideal `J_{T(1)}` on
> every open of `T(1)`.

```lean
theorem smallSelfProductDiagonalIdeal_le (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (W : D.obj.thickening.target.scheme.Opens) :
    smallSelfProductDiagonalIdeal h W ≤ D.obj.thickening.target.ideal.obj (op W)
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductDiagonalIdeal_isSubDPIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean#L316). The attribute's comment: “K is preserved by the divided structure on J\_\{T(1)}; sections over each open”.

> For a self-product `(U(1), T(1), δ(1))` of an object `(U, T, δ)` of `Cris(X/S)` with itself,
> the diagonal ideal `K` of `Δ : T ⟶ T(1)` is preserved by the divided structure on `J_{T(1)}` on
> every open of `T(1)`.

```lean
theorem smallSelfProductDiagonalIdeal_isSubDPIdeal (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (W : D.obj.thickening.target.scheme.Opens) :
    (D.obj.thickening.target.dividedPowers.dividedPowers (op W)).IsSubDPIdeal
      (smallSelfProductDiagonalIdeal h W)
```

## Tag 07KM, a lemma

[Tag 07KM](https://stacks.math.columbia.edu/tag/07KM) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.isLocallySurjective_moduleComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsComparison.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsComparison.lean#L198). The attribute's comment: “(2), the comparison map along a closed immersion is surjective”.

> **Stacks Project, Tag 07KM (2).**  For a morphism `f : (U, T, δ) ⟶ (U', T', δ')` of
> `CRIS(X/S)` whose map `T ⟶ T'` on ambient schemes is a closed immersion, the comparison morphism
> `c_f : f^*(Ω_{X/S})_{T'} ⟶ (Ω_{X/S})_T` is surjective: every section of `(Ω_{X/S})_T` is, on the
> members of an open covering, in the image of `c_f`.  A closed immersion is a topological
> embedding, so every open of `T` is the preimage of an open of `T'`, and the preimages of the
> affine opens contained in that one cover it; over each of those the comparison morphism is
> already surjective on sections.

```lean
theorem isLocallySurjective_moduleComparison [IsClosedImmersion g.targetHom.hom] :
    Presheaf.IsLocallySurjective (Opens.grothendieckTopology A.thickening.target.scheme)
      ((PresheafOfModules.toPresheaf (ringRestriction A)).map
        (moduleComparison (crysDifferentials S) g))
```

**`Crystalline.GlobalCrystallineSituation.crysDifferentials_isLocallyQuasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean#L141). The attribute's comment: “clause (1): Ω\_\{X/S} is locally quasi-coherent”.

> `Ω_{X/S}` is locally quasi-coherent: for every object `(U, T, δ)` of `CRIS(X/S)` the
> restriction `(Ω_{X/S})_T`, taken as the sheaf associated with the restriction of the presheaf
> `Ω_{X/S}`, is a quasi-coherent module over the restriction of `𝒪_{X/S}` to the opens of `T`.

```lean
theorem crysDifferentials_isLocallyQuasiCoherent (A : Thickening S) :
    (crysDifferentialsRestrictionSheaf S A).IsQuasicoherentOnSite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.12, Tag 07IW](https://stacks.math.columbia.edu/tag/07IW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
