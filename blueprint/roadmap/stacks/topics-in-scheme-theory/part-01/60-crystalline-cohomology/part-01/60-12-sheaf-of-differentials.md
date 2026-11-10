---
declaration: section
origin: cited
lean: Crystalline.dpDifferentialsSheaf, Crystalline.universalDPSchemeDerivation_isUniversal, Crystalline.GlobalCrystallineSituation.crisRing_isSheaf, Crystalline.GlobalCrystallineSituation.structureSheaf_isSheaf, Crystalline.GlobalCrystallineSituation.crystallineStructureSheaf, Crystalline.GlobalCrystallineSituation.SDerivation, Crystalline.affineSectionsEquiv, Crystalline.dpDifferentialsSheaf_isQuasicoherent
statement: formalized
proof: formalized
---

# 60.12 Sheaf of differentials

Section 60.12 of the Stacks Project, [Tag 07IW](https://stacks.math.columbia.edu/tag/07IW). 7 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07IW, the section

[Tag 07IW](https://stacks.math.columbia.edu/tag/07IW) in the Stacks Project.

**`Crystalline.dpDifferentialsSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean#L493). The attribute's comment: “the sheaf Ω\_\{T/Y,δ} of divided power differentials of a divided power scheme over a scheme”.

> **The sheaf of divided power differentials** `Ω_{T/Y,δ}` of a divided power scheme `T` over a
> scheme `Y`: the sheaf of `𝒪_T`-modules associated with the presheaf of divided power
> differentials.

```lean
def dpDifferentialsSheaf : T.scheme.Modules
```

**`Crystalline.universalDPSchemeDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SchemeDifferentials.lean#L692). The attribute's comment: “the universal divided power derivation d\_\{T/Y,δ} and its universal property”.

> **The universal property of the sheaf of divided power differentials.**  Every divided power
> derivation of `𝒪_T` over `Y` into a sheaf of `𝒪_T`-modules factors uniquely through the universal
> one.

```lean
theorem universalDPSchemeDerivation_isUniversal :
    (universalDPSchemeDerivation T Y f).IsUniversal
```

## Tag 07IX, a definition

[Tag 07IX](https://stacks.math.columbia.edu/tag/07IX) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.crisRing_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean#L315). The attribute's comment: “the structure presheaf is a sheaf of rings”.

> **Stacks Project, Tag 07IX.**  The structure presheaf of rings of the big crystalline site is
> a sheaf for the crystalline Zariski topology.  It suffices to check the Zariski covering families,
> and for such a family the condition is Zariski descent for the structure sheaf of the ambient
> scheme of the base.

```lean
theorem crisRing_isSheaf (S : GlobalCrystallineSituation.{u}) :
    Presheaf.IsSheaf (topology S) (crisRing S)
```

**`Crystalline.GlobalCrystallineSituation.structureSheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean#L325). The attribute's comment: “the structure presheaf is a sheaf of commutative rings”.

> **Stacks Project, Tag 07IX.**  The structure presheaf of commutative rings of the big
> crystalline site is a sheaf for the crystalline Zariski topology.

```lean
theorem structureSheaf_isSheaf (S : GlobalCrystallineSituation.{u}) :
    Presheaf.IsSheaf (topology S) (structureSheaf S)
```

**`Crystalline.GlobalCrystallineSituation.crystallineStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/BigSite/StructureSheaf.lean#L334). The attribute's comment: “the structure sheaf”.

> **Stacks Project, Tag 07IX.**  The structure sheaf `𝒪_{X/S}` of the big crystalline site: the
> sheaf of rings on `CRIS(X/S)` sending an object `(U, T, δ)` to the ring `Γ(T, 𝒪_T)` of global
> sections of its ambient scheme.

```lean
def crystallineStructureSheaf (S : GlobalCrystallineSituation.{u}) :
    Sheaf (topology S) RingCat.{u}
```

**`Crystalline.GlobalCrystallineSituation.SDerivation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SDerivation.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SDerivation.lean#L279). The attribute's comment: “S-derivation”.

> **An `S`-derivation on the big crystalline category.**  For a presheaf `F` of modules over
> the structure presheaf of `CRIS(X/S)`, this is a map of presheaves of abelian groups
> `𝒪_{X/S} → F` such that for every object `(U, T, δ)` and *every* open `V ⊆ S` through which the
> structure morphism `T → S` factors, the induced map `Γ(T, 𝒪_T) → Γ(T, F)` is a divided power
> `Γ(V, 𝒪_V)`-derivation.

```lean
structure SDerivation (F : PresheafOfModules.{u} (structureRingCatPresheaf S))
```

## Tag 07IY, a lemma

[Tag 07IY](https://stacks.math.columbia.edu/tag/07IY) in the Stacks Project.

**`Crystalline.affineSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsAffineSections.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsAffineSections.lean#L554). The attribute's comment: “clause (2): the sections over an affine open”.

> For an affine open `W` of a divided power scheme `T` lying over an affine open `V` of the base
> `Y`, the sections of the sheaf `Ω_{T/Y,δ}` of divided power differentials over `W` are the module
> `Ω¹_{Γ(W,𝒪_T)/Γ(V,𝒪_Y),δ}` of divided power differentials of the corresponding rings.

```lean
def affineSectionsEquiv :
    Γ(dpDifferentialsSheaf T Y f, W) ≃ₗ[Γ(T.scheme, W)]
      ↑(dpDifferentials (f.appLE V W h) (T.dividedPowers.dividedPowers (op W)))
```

**`Crystalline.dpDifferentialsSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsQuasicoherent.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsQuasicoherent.lean#L764). The attribute's comment: “quasi-coherence of the sheaf of divided power differentials”.

> **The sheaf of divided power differentials is quasi-coherent**, being the quotient of the
> quasi-coherent sheaf of relative differentials by a subsheaf which, over an affine open, is the
> image of a free module.

```lean
instance dpDifferentialsSheaf_isQuasicoherent :
    (dpDifferentialsSheaf T Y f).IsQuasicoherent
```

## Tag 07IZ, a lemma

[Tag 07IZ](https://stacks.math.columbia.edu/tag/07IZ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.comparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystallineDifferentials.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystallineDifferentials.lean#L783). The attribute's comment: “the module identification, at the level of presheaves”.

> **Stacks Project, Tag 07IZ.**  The restriction of `Ω_{X/S}` to the ambient scheme of an object
> `(U, T, δ)` of `CRIS(X/S)` is the presheaf of divided power differentials of `T` over `S`, and the
> isomorphism carries `d_{T/S,δ}` to the restriction of `d_{X/S}`.

```lean
def comparisonIso (A : Thickening S) :
    dpDifferentialsPresheaf A.thickening.target S.S.scheme A.toBase.hom ≅
      restrictedCrysDifferentials S A
```

**`Crystalline.GlobalCrystallineSituation.restrictedToSheaf_app_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystallineDifferentials.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystallineDifferentials.lean#L807). The attribute's comment: “the derivations correspond”.

> **Stacks Project, Tag 07IZ, on derivations.**  The comparison carries the restriction of
> `d_{X/S}` to `d_{T/S,δ}`: the section of the restriction of `Ω_{X/S}` over `W` given by the
> restricted universal `S`-derivation of a section `b` is sent to `d_{T/S,δ} b`.

```lean
theorem restrictedToSheaf_app_d (A : Thickening S) (W : A.thickening.target.scheme.Opens)
    (b : Γ(A.thickening.target.scheme, W)) :
    ((restrictedToSheaf A).app (op W)).hom
        ((crysSDerivation S).app (A.restrictOpen W) (openTopRes W b)) =
      (universalDPSchemeDerivation A.thickening.target S.S.scheme A.toBase.hom).app W b
```

**`Crystalline.GlobalCrystallineSituation.restrictedCrysDifferentialsSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean#L100). The attribute's comment: “the module identification, at the level of sheaves”.

> The `𝒪_T`-module `(Ω_{X/S})_T` obtained by restricting `Ω_{X/S}` to the ambient scheme of
> an object `(U, T, δ)` of `CRIS(X/S)` is the sheaf `Ω_{T/S,δ}` of divided power differentials of
> `T` over `S`.

```lean
def restrictedCrysDifferentialsSheafIso (A : Thickening S) :
    (dpDifferentialsSheaf A.thickening.target S.S.scheme A.toBase.hom :
        SheafOfModules.{u} A.thickening.target.scheme.ringCatSheaf) ≅
      restrictedCrysDifferentialsSheaf S A
```

## Tag 07J0, a lemma

[Tag 07J0](https://stacks.math.columbia.edu/tag/07J0) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.affineCrysDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineObjectDifferentials.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineObjectDifferentials.lean#L458). The attribute's comment: “Γ((U, T, δ), Ω\_\{X/S}) = Ω¹\_\{Γ(T, 𝒪\_T)/Γ(V, 𝒪\_V), δ} for an affine object of the crystalline category mapping into an affine open V ⊆ S”.

> For an affine object `(U, T, δ)` of `CRIS(X/S)` whose structure morphism factors through an
> affine open `V ⊆ S`, the sections of `Ω_{X/S}` over `(U, T, δ)` are the divided power
> differentials `Ω¹_{Γ(T, 𝒪_T)/Γ(V, 𝒪_S), δ}`.

```lean
def affineCrysDifferentialsIso [IsAffine A.thickening.target.scheme] (hV : IsAffineOpen V) :
    crysDifferentialsObj S A ≅ affineCrysDifferentialsObj S A hVA
```

**`Crystalline.GlobalCrystallineSituation.existsUnique_affineCrysDifferentialsIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineObjectDifferentials.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineObjectDifferentials.lean#L497). The attribute's comment: “the equality sign of the tag: exactly one isomorphism Γ((U, T, δ), Ω\_\{X/S}) ≅ Ω¹\_\{Γ(T, 𝒪\_T)/Γ(V, 𝒪\_V), δ} carries d\_\{X/S} to the universal divided power differential”.

> **The identification of [Stacks, Tag 07J0] is the only one compatible with the universal
> derivations.**  This is what the equality sign of the source asserts: not that the two modules
> happen to be isomorphic, but that there is exactly one isomorphism carrying `d_{X/S}` to
> `d_{Γ(T, 𝒪_T)/Γ(V, 𝒪_S), δ}`, namely `affineCrysDifferentialsIso`.  Uniqueness holds because
> the universal differentials generate the sections of `Ω_{X/S}` over the object, which is
> `Crystalline.dpConstDifferentials_ext`.

```lean
theorem existsUnique_affineCrysDifferentialsIso [IsAffine A.thickening.target.scheme]
    (hV : IsAffineOpen V) :
    ∃! e : crysDifferentialsObj S A ≅ affineCrysDifferentialsObj S A hVA,
      ∀ b : Γ(A.thickening.target.scheme, ⊤),
        e.hom ((crysSDerivation S).app A b) =
          dpd (f := affineBaseAppLE S A hVA) (crysDividedPowers S A) b
```

## Tag 07J1, a lemma

[Tag 07J1](https://stacks.math.columbia.edu/tag/07J1) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.smallSelfProductDividedSquare_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L316). The attribute's comment: “second assertion: K^\{[2]} is a sub-ideal of K; sections over each open of T(1)”.

> **Stacks Project, Tag 07J1.**  The divided square of the diagonal ideal is a sub-ideal of the
> diagonal ideal: the square of an ideal is contained in it, and the diagonal ideal is preserved by
> the divided powers of `J_{T(1)}`.

```lean
theorem smallSelfProductDividedSquare_le (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (W : D.obj.thickening.target.scheme.Opens) :
    smallSelfProductDividedSquare h W ≤ smallSelfProductDiagonalIdeal h W
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductConormalComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 826](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L826). The attribute's comment: “second assertion: the comparison map (Ω\_\{X/S})\_T → K/K^\{[2]} on each open of T; an isomorphism on an affine open of T lying over an affine open of S”.

> **Stacks Project, Tag 07J1, the comparison map of the second assertion.**  The universal
> property of the divided power differentials of `T` over `S` on an open `V` applied to the
> difference of the two coprojections: a `Γ(V, 𝒪_T)`-linear map from `Ω_{T/S,δ}(V)`, which is
> `(Ω_{X/S})_T(V)` by [Stacks, Tag 07IZ], to the conormal module `K/K^{[2]}` of the diagonal,
> carrying `d f` to the class of `p₁^♯ f - p₀^♯ f`.
>
> This is the map the equality `(Ω_{X/S})_T = K/K^{[2]}` of the source is an equality of.  It is an
> isomorphism over an affine open of `T` lying over an affine open of `S` — the hypotheses under
> which the source's proof works — by
> `Crystalline.GlobalCrystallineSituation.isIso_smallSelfProductConormalComparison` in
> `StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean`.

```lean
def smallSelfProductConormalComparison (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (V : B.obj.thickening.target.scheme.Opens) :
    (dpDifferentialsPresheaf B.obj.thickening.target S.S.scheme B.obj.toBase.hom).obj (op V) ⟶
      smallSelfProductConormal h V
```

**`Crystalline.GlobalCrystallineSituation.isClosedImmersion_smallSelfProductAmbientDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 1048](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L1048). The attribute's comment: “the diagonal Δ : T ⟶ T(1) is a closed immersion”.

> **Stacks Project, Tag 07J1.**  The ambient diagonal `Δ : T ⟶ T(1)` of a self-product taken in
> `Cris(X/S)` is a closed immersion.  It is surjective on stalks because it is a section of either
> coprojection, and a closed embedding because it is a homeomorphism on spaces: that is `U(1) = U`
> read through the immersions of the two thickenings.

```lean
theorem isClosedImmersion_smallSelfProductAmbientDiagonal
    (h : IsLimit (BinaryFan.mk pr₀ pr₁)) :
    IsClosedImmersion (smallSelfProductAmbientDiagonal h).hom
```

**`Crystalline.GlobalCrystallineSituation.ker_ideal_smallSelfProductAmbientDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean, line 1065](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormal.lean#L1065). The attribute's comment: “K is the quasi-coherent ideal sheaf of the closed immersion Δ, on affine opens”.

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

**`Crystalline.GlobalCrystallineSituation.isAffineOpen_smallSelfProductOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalAffine.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalAffine.lean#L64). The attribute's comment: “the open of T(1) corresponding to an affine open of T is affine, by Limits, Lemma 01ZT applied to the restriction of the diagonal”.

> **The open of `T(1)` lying over an affine open of `T` is affine.**  The ambient diagonal
> `Δ : T ⟶ T(1)` is a closed immersion, hence finite, and a homeomorphism on spaces, hence
> surjective; it pulls `p₀⁻¹V ⊓ p₁⁻¹V` back to `V`, so its restriction over that open is a finite
> surjective morphism with affine source, and [Stacks, Tag 01ZT] applies.

```lean
theorem isAffineOpen_smallSelfProductOpen (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    {V : B.obj.thickening.target.scheme.Opens} (hV : IsAffineOpen V) :
    IsAffineOpen (smallSelfProductOpen pr₀ pr₁ V)
```

**`Crystalline.GlobalCrystallineSituation.exists_isIso_smallSelfProductConormalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean#L590). The attribute's comment: “second assertion: the comparison Ω\_\{T/S,δ} → K/K^\{[2]} is an isomorphism on a neighbourhood of every point of every open of T, with no hypothesis on the open”.

> **Stacks Project, Tag 07J1, the second assertion, with no hypothesis on the open.**  Every
> point of every open `W` of `T` has an open neighbourhood `V ≤ W` on which the comparison map
> `Ω_{T/S,δ}(V) → K/K^{[2]}` is an isomorphism.  The affine opens of `T` lying over an affine open
> of `S` are such neighbourhoods, by `isIso_smallSelfProductConormalComparison`, and they form a
> basis of the topology of `T`, by `Crystalline.exists_isAffineOpen_over_isAffineOpen`.

```lean
theorem exists_isIso_smallSelfProductConormalComparison
    (h : IsLimit (BinaryFan.mk pr₀ pr₁)) {W : B.obj.thickening.target.scheme.Opens}
    {x : B.obj.thickening.target.scheme} (hx : x ∈ W) :
    ∃ V : B.obj.thickening.target.scheme.Opens, x ∈ V ∧ V ≤ W ∧
      IsIso (smallSelfProductConormalComparison h V)
```

**`Crystalline.GlobalCrystallineSituation.exists_isIso_restrictedCrysDifferentialsConormalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean#L608). The attribute's comment: “second assertion: (Ω\_\{X/S})\_T = K/K^\{[2]} on a neighbourhood of every point of every open of T, with no hypothesis on the open”.

> **Stacks Project, Tag 07J1, the second assertion, with no hypothesis on the open.**  Every
> point of every open `W` of `T` has an open neighbourhood `V ≤ W` on which the comparison map
> `(Ω_{X/S})_T(V) → K/K^{[2]}` is an isomorphism.  This is the second assertion read out of
> `(Ω_{X/S})_T` itself, through [Stacks, Tag 07IZ], and it carries no hypothesis the source does
> not: the affineness of the open of `T` and of an open of `S` below it, under which the source's
> own proof works, is discharged against
> `Crystalline.exists_isAffineOpen_over_isAffineOpen`.

```lean
theorem exists_isIso_restrictedCrysDifferentialsConormalComparison
    (h : IsLimit (BinaryFan.mk pr₀ pr₁)) {W : B.obj.thickening.target.scheme.Opens}
    {x : B.obj.thickening.target.scheme} (hx : x ∈ W) :
    ∃ V : B.obj.thickening.target.scheme.Opens, x ∈ V ∧ V ≤ W ∧
      IsIso (restrictedCrysDifferentialsConormalComparison h V)
```

**`Crystalline.GlobalCrystallineSituation.isBasis_isIso_restrictedCrysDifferentialsConormalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalIso.lean#L625). The attribute's comment: “second assertion: the opens of T on which (Ω\_\{X/S})\_T = K/K^\{[2]} form a basis of the topology of T”.

> **Stacks Project, Tag 07J1, the second assertion, as a basis of the topology of `T`.**  The
> opens of `T` on which the comparison `(Ω_{X/S})_T → K/K^{[2]}` is an isomorphism form a basis of
> the topology of `T`.  The conormal module is built open by open, so there is no morphism of
> sheaves of `𝒪_T`-modules to call an isomorphism; a basis of opens on which the comparison is one
> is what the source's equality of sheaves amounts to for that presentation.

```lean
theorem isBasis_isIso_restrictedCrysDifferentialsConormalComparison
    (h : IsLimit (BinaryFan.mk pr₀ pr₁)) :
    TopologicalSpace.Opens.IsBasis
      {W : B.obj.thickening.target.scheme.Opens |
        IsIso (restrictedCrysDifferentialsConormalComparison h W)}
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductConormalInverse_comp_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalThickening.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductConormalThickening.lean#L495). The attribute's comment: “second assertion: the inverse comparison K/K^\{[2]} → (Ω\_\{X/S})\_T out of the first-order thickening T', and that it undoes the comparison map”.

> **Stacks Project, Tag 07J1, the inverse comparison.**  The comparison map
> `(Ω_{X/S})_T(V) → K/K^{[2]}` followed by the map back out of the first-order thickening is the
> comparison of the presheaf of divided power differentials with the sheaf it generates.  In
> particular the comparison map is injective whenever that comparison is.

```lean
theorem smallSelfProductConormalInverse_comp_comparison (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (V : B.obj.thickening.target.scheme.Opens)
    (x : ↥((dpDifferentialsPresheaf B.obj.thickening.target S.S.scheme
      B.obj.toBase.hom).obj (op V))) :
    smallSelfProductConormalInverse h V ((smallSelfProductConormalComparison h V).hom x) =
      (dpDifferentialsToSheaf B.obj.thickening.target S.S.scheme B.obj.toBase.hom).app (op V)
        x
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductDiagonalIdeal_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean#L306). The attribute's comment: “K ⊆ J\_\{T(1)}; sections over each open, K the kernel of Δ on sections”.

> For a self-product `(U(1), T(1), δ(1))` of an object `(U, T, δ)` of `Cris(X/S)` with itself,
> the diagonal ideal `K` of `Δ : T ⟶ T(1)` is contained in the divided power ideal `J_{T(1)}` on
> every open of `T(1)`.

```lean
theorem smallSelfProductDiagonalIdeal_le (h : IsLimit (BinaryFan.mk pr₀ pr₁))
    (W : D.obj.thickening.target.scheme.Opens) :
    smallSelfProductDiagonalIdeal h W ≤ D.obj.thickening.target.ideal.obj (op W)
```

**`Crystalline.GlobalCrystallineSituation.smallSelfProductDiagonalIdeal_isSubDPIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SelfProductDiagonal.lean#L316). The attribute's comment: “K is preserved by the divided structure on J\_\{T(1)}; sections over each open”.

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

**`Crystalline.GlobalCrystallineSituation.isLocallySurjective_moduleComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsComparison.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsComparison.lean#L198). The attribute's comment: “(2), the comparison map along a closed immersion is surjective”.

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

**`Crystalline.GlobalCrystallineSituation.crysDifferentials_isLocallyQuasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DifferentialsLocallyQuasicoherent.lean#L134). The attribute's comment: “clause (1): Ω\_\{X/S} is locally quasi-coherent”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
