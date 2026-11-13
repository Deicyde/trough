---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeProjMapTriple, Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.relativeMapDomain_mapHom_twistMap_comp, Stacks.AlgebraicGeometry.Tag07ZGTwistCounterexample.exists_epi_not_isIso_relativeTwistMap, Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_closedImmersion_twistEpi_of_eventually_epi, Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_isIso_twistIsIso_of_eventually_isIso, Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_closedImmersion_twistIsIso_of_generatedInDegreeOne
statement: formalized
proof: formalized
---

# 27.18 Functoriality of relative Proj

Section 27.18 of the Stacks Project, [Tag 07ZF](https://stacks.math.columbia.edu/tag/07ZF). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07ZG, a lemma

[Tag 07ZG](https://stacks.math.columbia.edu/tag/07ZG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeProjMapTriple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistAlgebra.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistAlgebra.lean#L239). The attribute's comment: “the tag in one statement: the open U(ψ) of Proj\_S(B), the morphism r\_ψ : U(ψ) ⟶ Proj\_S(A) over S, and θ as a map of ℤ-graded 𝒪\_\{U(ψ)}-algebras, together with the characterisation of all three over every affine open of the base by the triple Lemma 01MY attaches to the induced homomorphism of graded rings of sections, and the uniqueness of each”. References: EGA II (3.5.1), “partial”; EGA II (8.12.4), “special case”.

> Let `S` be a scheme, let `A` and `B` be quasi-coherent graded `𝒪_S`-algebras, set
> `p : X = Proj_S(A) ⟶ S` and `q : Y = Proj_S(B) ⟶ S`, and let `ψ : A ⟶ B` be a homomorphism of
> graded `𝒪_S`-algebras. There is a canonical open `U(ψ) ⊆ Y`, a canonical morphism of schemes
> `r_ψ : U(ψ) ⟶ X` over `S`, and a map of `ℤ`-graded `𝒪_{U(ψ)}`-algebras
>
> `θ = θ_ψ : r_ψ^*(⨁_{d ∈ ℤ} 𝒪_X(d)) ⟶ ⨁_{d ∈ ℤ} 𝒪_{U(ψ)}(d)`,
>
> and the triple `(U(ψ), r_ψ, θ)` is characterised by the property that for every affine open
> `W ⊆ S` the triple `(U(ψ) ∩ q⁻¹W, r_ψ|_{U(ψ) ∩ q⁻¹W}, θ|_{U(ψ) ∩ q⁻¹W})` is the triple attached
> to `ψ : A(W) ⟶ B(W)`, via the identifications `p⁻¹W = Proj(A(W))` and `q⁻¹W = Proj(B(W))`.
>
> The triple is `ψ.relativeMapDomain`, `relativeMapHom ψ` and `relativeTwistAlgebraHom ψ`, and the
> seven conjuncts are, in order:
>
> 1. `r_ψ` is a morphism over `S`.
> 2. The inverse image of `U(ψ)` under the chart over an affine open `W` of the base is the open
>    `mapDomain` of `ψ_W` in `Proj(B(W))`.
> 3. Under the canonical identification of `U(ψ) ∩ q⁻¹W` with `U(ψ_W)`, the restriction of `r_ψ` is
>    the morphism `mapHom` of `ψ_W` followed by the chart of `X` over `W`.
> 4. In every degree `n`, the restriction of the `n`-th component of `θ` to the piece over `W` is
>    `relativeTwistChart ψ n W`, the comparison map for `ψ_W` conjugated by the chart
>    identifications.
> 5., 6., 7. Each of the three is determined by its affine-local description.

```lean
public theorem relativeProjMapTriple :
    (relativeMapHom ψ ≫ (relativeProj A).toBase =
        ψ.relativeMapDomain.ι ≫ (relativeProj B).toBase) ∧
      (∀ (V : S.Opens) (hV : IsAffineOpen V),
        (relativeProj B).chart V hV ⁻¹ᵁ ψ.relativeMapDomain =
          mapDomain (A.grading V) (B.grading V) (ψ.sectionHom V)) ∧
      (∀ U : AffineOpen S,
        (chartPieceIso ψ U).hom ≫
            (relativeProj B).scheme.homOfLE
                (inf_le_left : ψ.relativeMapDomain ⊓ ((relativeProj B).toBase ⁻¹ᵁ U.1) ≤ _) ≫
              relativeMapHom ψ =
          mapHom (A.grading U.1) (B.grading U.1) (ψ.sectionHom U.1) ≫
            (relativeProj A).chart U.1 U.2) ∧
      (∀ (n : ℤ) (U : S.affineOpens),
        (Scheme.Modules.pullback (pieceIncl ψ U)).map ((relativeTwistAlgebraHom ψ).app n) =
          relativeTwistChart ψ n U) ∧
      (∀ W : (relativeProj B).scheme.Opens,
        (∀ (V : S.Opens) (hV : IsAffineOpen V),
            (relativeProj B).chart V hV ⁻¹ᵁ W =
              mapDomain (A.grading V) (B.grading V) (ψ.sectionHom V)) →
          W = ψ.relativeMapDomain) ∧
      (∀ r : ψ.relativeMapDomain.toScheme ⟶ (relativeProj A).scheme,
        (∀ U : AffineOpen S,
            (((relativeProj B).chart U.1 U.2).isoImage
                  (mapDomain (A.grading U.1) (B.grading U.1) (ψ.sectionHom U.1))).hom ≫
                (relativeProj B).scheme.homOfLE (chartImage_le ψ U) ≫ r =
              mapHom (A.grading U.1) (B.grading U.1) (ψ.sectionHom U.1) ≫
                (relativeProj A).chart U.1 U.2) →
          r = relativeMapHom ψ) ∧
      (∀ (n : ℤ)
          (θ : (Scheme.Modules.pullback (relativeMapHom ψ)).obj (relativeTwist A n) ⟶
            (Scheme.Modules.pullback ψ.relativeMapDomain.ι).obj (relativeTwist B n)),
        (∀ U : S.affineOpens,
            (Scheme.Modules.pullback (pieceIncl ψ U)).map θ = relativeTwistChart ψ n U) →
          θ = (relativeTwistAlgebraHom ψ).app n)
```

## Tag 07ZH, a lemma

[Tag 07ZH](https://stacks.math.columbia.edu/tag/07ZH) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.relativeMapDomain_mapHom_twistMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistCompStatement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistCompStatement.lean#L107). The attribute's comment: “the tag's three assertions in one statement: the domain of the composite is the inverse image of the inner factor's domain along `r_ψ`, the morphism of the composite is the restriction of `r_ψ` followed by `r_φ`, and the maps on twists compose. The first conjunct is the intended reading `U(psi.comp phi) = r_psi^{-1}(U(phi))` of a source statement printed as `U(psi.comp phi) = r_phi^{-1}(U(psi))`, which is TYPE-INCORRECT -- `r_phi` is defined on `U(phi)` in `Proj_S(B)` and so accepts opens of `Proj_S(A)`, whereas `U(psi)` is an open of `Proj_S(C)`, the two names having been interchanged; the deviation is documented in the module docstring”.

> **[Stacks, Tag 07ZH].** Let `S` be a scheme, let `A`, `B` and `C` be quasi-coherent graded
> `𝒪_S`-algebras and let `φ : A ⟶ B` and `ψ : B ⟶ C` be homomorphisms between them. Then the open,
> the morphism and the maps on twists that Tag 07ZG attaches to the composite `ψ ∘ φ` are
> determined by those of `φ` and of `ψ`.
>
> The three conjuncts are, in order:
>
> 1. `U(ψ ∘ φ) = r_ψ^{-1}(U(φ))`: the open attached to the composite is the inverse image under
>   `r_ψ` of the open attached to the inner factor, read inside `Proj_S(C)` as the image of that
>   inverse image under the inclusion of `U(ψ)`. (This is the intended reading of a source
>   statement that is type-incorrect as printed; see the implementation notes above.)
> 2. `r_{ψ ∘ φ} = r_φ ∘ r_ψ|_{U(ψ ∘ φ)}`: the morphism attached to the composite is the
>   restriction `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeMapHomRestrict` of `r_ψ` to
>   `U(ψ ∘ φ)`, followed by the morphism attached to the inner factor.
> 3. `θ_ψ ∘ r_ψ^*θ_φ = θ_{ψ ∘ φ}`: for every `n` the `n`-th map on twists of the composite is the
>   inverse image along that same restriction of the `n`-th map on twists of `φ`, followed by the
>   inverse image along the inclusion of `U(ψ ∘ φ)` into `U(ψ)` of the `n`-th map on twists of
>   `ψ`. The isomorphisms of inverse-image functors that identify the source and the target of the
>   two sides are the ones named by conjuncts 1 and 2 and by
>   `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeMapHomRestrict_comp_ι`.
>
> Each conjunct is the corresponding component declaration:
> `Stacks.AlgebraicGeometry.RelativeProjMapComp.relativeMapDomain_comp`,
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeMapHomRestrict_comp_relativeMapHom` and
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.relativeTwistMap_comp`. The source states the tag for
> arbitrary `A`, `B`, `C`, `φ` and `ψ`, and those are the only binders here.

```lean
theorem relativeMapDomain_mapHom_twistMap_comp :
    (ψ.comp φ).relativeMapDomain =
        ψ.relativeMapDomain.ι ''ᵁ (relativeMapHom ψ ⁻¹ᵁ φ.relativeMapDomain) ∧
      relativeMapHomRestrict φ ψ ≫ relativeMapHom φ = relativeMapHom (ψ.comp φ) ∧
      ∀ n : ℤ,
        (Scheme.Modules.pullbackCongr
              (relativeMapHomRestrict_comp_relativeMapHom φ ψ)).inv.app
            (relativeTwist A n) ≫
            (Scheme.Modules.pullbackComp (relativeMapHomRestrict φ ψ)
              (relativeMapHom φ)).inv.app (relativeTwist A n) ≫
            (Scheme.Modules.pullback (relativeMapHomRestrict φ ψ)).map
              (relativeTwistMap φ n) ≫
            (Scheme.Modules.pullbackComp (relativeMapHomRestrict φ ψ)
              φ.relativeMapDomain.ι).hom.app (relativeTwist B n) ≫
            (Scheme.Modules.pullbackCongr
              (relativeMapHomRestrict_comp_ι φ ψ)).hom.app (relativeTwist B n) ≫
            (Scheme.Modules.pullbackComp
              ((relativeProj C).scheme.homOfLE (relativeMapDomain_comp_le φ ψ))
              (relativeMapHom ψ)).inv.app (relativeTwist B n) ≫
            (Scheme.Modules.pullback ((relativeProj C).scheme.homOfLE
              (relativeMapDomain_comp_le φ ψ))).map (relativeTwistMap ψ n) ≫
            (Scheme.Modules.pullbackComp
              ((relativeProj C).scheme.homOfLE (relativeMapDomain_comp_le φ ψ))
              ψ.relativeMapDomain.ι).hom.app (relativeTwist C n) ≫
            (Scheme.Modules.pullbackCongr (Scheme.homOfLE_ι (relativeProj C).scheme
              (relativeMapDomain_comp_le φ ψ))).hom.app (relativeTwist C n) =
          relativeTwistMap (ψ.comp φ) n
```

## Tag 07ZI, a lemma

[Tag 07ZI](https://stacks.math.columbia.edu/tag/07ZI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag07ZGTwistCounterexample.exists_epi_not_isIso_relativeTwistMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualCounterexample.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualCounterexample.lean#L58). The attribute's comment: “(3), second half: the maps θ are surjective but not isomorphisms in general, even if A → B is surjective — a map ψ of quasi-coherent graded algebras surjective in every degree with θ₁ not an isomorphism (A = R[x,y]/(x²), deg x = 1, deg y = 2, B = A/(x), on Spec R)”.

> **[Stacks, Tag 07ZI] (3), second half.** The maps `θ_n : r_ψ^* 𝒪_X(n) ⟶ 𝒪_Y(n)` of Tag 07ZG
> are not isomorphisms in general, even if `A → B` is surjective: there are a scheme `S`,
> quasi-coherent graded `𝒪_S`-algebras `A` and `B` and a homomorphism `ψ : A ⟶ B` such that every
> `ψ_n : A_n ⟶ B_n` is an epimorphism (so the hypothesis of Tag 07ZI holds in every degree), every
> `θ_n` is an epimorphism, as the first half of assertion (3) says, and `θ_1` is not an
> isomorphism.
>
> The witness is `S = Spec R` for `R = ULift ℤ`, `A = R[x, y]/(x²)` with `deg x = 1`, `deg y = 2`,
> `B = A/(x)` and `ψ` the quotient map:
> `Stacks.AlgebraicGeometry.ProjTwistCompare.NotIsoExample.epi_sheafHom_app`,
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.epi_relativeTwistMap_of_eventually_epi` and
> `Stacks.AlgebraicGeometry.ProjTwistCompare.NotIsoExample.not_isIso_relativeTwistMap`.

```lean
theorem exists_epi_not_isIso_relativeTwistMap :
    ∃ (S : Scheme.{u}) (A B : SheafGradedAlgebra S) (ψ : SheafGradedAlgebraHom A B),
      (∀ n : ℤ, Epi (ψ.app n)) ∧ (∀ n : ℤ, Epi (relativeTwistMap ψ n)) ∧
        ¬ IsIso (relativeTwistMap ψ ((1 : ℕ) : ℤ))
```

**`Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_closedImmersion_twistEpi_of_eventually_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean#L97). The attribute's comment: “the tag's three assertions in one statement: under degreewise surjectivity in all large degrees the domain of definition is all of `Proj_S(B)`, the induced morphism `r_ψ` is a closed immersion, and every comparison map `θ_n` on twists is an epimorphism”. References: EGA II (2.9.2), “more general”.

> **[Stacks, Tag 07ZI].** Let `S` be a scheme, let `A` and `B` be quasi-coherent graded
> `𝒪_S`-algebras and let `ψ : A ⟶ B` be a homomorphism between them. If `A_d → B_d` is surjective
> for all sufficiently large `d`, then `U(ψ) = Y`, the morphism `r_ψ : U(ψ) ⟶ X` of Tag 07ZG is a
> closed immersion, and every map `θ_n : r_ψ^* 𝒪_X(n) ⟶ 𝒪_Y(n)|_{U(ψ)}` is an epimorphism.
>
> The three conjuncts are, in order:
>
> 1. The open of `Y = Proj_S(B)` on which `ψ` induces a morphism is all of `Y`.
> 2. That morphism is a closed immersion.
> 3. For every `n : ℤ` the comparison map on the `n`-th twist is an epimorphism.
>
> Each is the corresponding component declaration:
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.relativeMapDomain_eq_top_of_eventually_epi`,
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.isClosedImmersion_relativeMapHom_of_eventually_epi`
> and `Stacks.AlgebraicGeometry.Tag07ZGTwist.epi_relativeTwistMap_of_eventually_epi`. The only
> hypothesis is the source's, degreewise surjectivity in all large degrees.
>
> The source's assertion (3) adds that the maps `θ_n` are not isomorphisms in general, even if
> `A → B` is surjective. That is an existence statement, not a consequence of the hypothesis, and is
> `Stacks.AlgebraicGeometry.Tag07ZGTwistCounterexample.exists_epi_not_isIso_relativeTwistMap`.

```lean
theorem domain_closedImmersion_twistEpi_of_eventually_epi
    (hsurj : ∀ᶠ d : ℕ in atTop, Epi (ψ.app (d : ℤ))) :
    ψ.relativeMapDomain = ⊤ ∧
      IsClosedImmersion (relativeMapHom ψ) ∧
      ∀ n : ℤ, Epi (relativeTwistMap ψ n)
```

## Tag 07ZJ, a lemma

[Tag 07ZJ](https://stacks.math.columbia.edu/tag/07ZJ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_isIso_twistIsIso_of_eventually_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean#L127). The attribute's comment: “the tag's three assertions in one statement: under degreewise invertibility in all large degrees the domain of definition is all of `Proj_S(B)`, the induced morphism `r_ψ` is an isomorphism, and every comparison map `θ_n` on twists is an isomorphism”. References: EGA II (3.6.1), “TN-bijective clause”.

> **[Stacks, Tag 07ZJ].** Let `S` be a scheme, let `A` and `B` be quasi-coherent graded
> `𝒪_S`-algebras and let `ψ : A ⟶ B` be a homomorphism between them. If `A_d → B_d` is an
> isomorphism for all sufficiently large `d`, then `U(ψ) = Y`, the morphism `r_ψ : U(ψ) ⟶ X` of
> Tag 07ZG is an isomorphism, and every map `θ_n : r_ψ^* 𝒪_X(n) ⟶ 𝒪_Y(n)|_{U(ψ)}` is an
> isomorphism.
>
> The three conjuncts are, in order:
>
> 1. The open of `Y = Proj_S(B)` on which `ψ` induces a morphism is all of `Y`.
> 2. That morphism is an isomorphism.
> 3. For every `n : ℤ` the comparison map on the `n`-th twist is an isomorphism.
>
> Each is the corresponding component declaration:
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.relativeMapDomain_eq_top_of_eventually_isIso`,
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.isIso_relativeMapHom_of_eventually_isIso` and
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.isIso_relativeTwistMap_of_eventually_isIso`. The only
> hypothesis is the source's, degreewise invertibility in all large degrees.

```lean
theorem domain_isIso_twistIsIso_of_eventually_isIso
    (hbij : ∀ᶠ d : ℕ in atTop, IsIso (ψ.app (d : ℤ))) :
    ψ.relativeMapDomain = ⊤ ∧
      IsIso (relativeMapHom ψ) ∧
      ∀ n : ℤ, IsIso (relativeTwistMap ψ n)
```

## Tag 07ZK, a lemma

[Tag 07ZK](https://stacks.math.columbia.edu/tag/07ZK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag07ZGTwistStatement.domain_closedImmersion_twistIsIso_of_generatedInDegreeOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphism/TwistEventualStatement.lean#L159). The attribute's comment: “the tag's three assertions in one statement: under degreewise surjectivity in all large degrees and generation in degree one the domain of definition is all of `Proj_S(B)`, the induced morphism `r_ψ` is a closed immersion, and every comparison map `θ_n` on twists is an isomorphism”. References: EGA II (3.5.1), “special case”.

> **[Stacks, Tag 07ZK].** Let `S` be a scheme, let `A` and `B` be quasi-coherent graded
> `𝒪_S`-algebras and let `ψ : A ⟶ B` be a homomorphism between them. If `A_d → B_d` is surjective
> for all sufficiently large `d` and `A` is generated by `A_1` over `A_0`, then `U(ψ) = Y`, the
> morphism `r_ψ : U(ψ) ⟶ X` of Tag 07ZG is a closed immersion, and every map
> `θ_n : r_ψ^* 𝒪_X(n) ⟶ 𝒪_Y(n)|_{U(ψ)}` is an isomorphism.
>
> The three conjuncts are, in order:
>
> 1. The open of `Y = Proj_S(B)` on which `ψ` induces a morphism is all of `Y`.
> 2. That morphism is a closed immersion.
> 3. For every `n : ℤ` the comparison map on the `n`-th twist is an isomorphism.
>
> The first two are the two component declarations of Tag 07ZI,
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.relativeMapDomain_eq_top_of_eventually_epi` and
> `Stacks.AlgebraicGeometry.RelativeProjMapDomain.isClosedImmersion_relativeMapHom_of_eventually_epi`,
> which need only the surjectivity hypothesis; the third is
> `Stacks.AlgebraicGeometry.Tag07ZGTwist.isIso_relativeTwistMap_of_generatedInDegreeOne`, which
> uses both. Generation in degree one is read over the affine opens of the base, which is where the
> graded algebras have graded rings of sections.

```lean
theorem domain_closedImmersion_twistIsIso_of_generatedInDegreeOne
    (hsurj : ∀ᶠ d : ℕ in atTop, Epi (ψ.app (d : ℤ)))
    (hgen : ∀ U : S.Opens, IsAffineOpen U → A.IsGeneratedInDegreeOneAt U) :
    ψ.relativeMapDomain = ⊤ ∧
      IsClosedImmersion (relativeMapHom ψ) ∧
      ∀ n : ℤ, IsIso (relativeTwistMap ψ n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.18, Tag 07ZF](https://stacks.math.columbia.edu/tag/07ZF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
