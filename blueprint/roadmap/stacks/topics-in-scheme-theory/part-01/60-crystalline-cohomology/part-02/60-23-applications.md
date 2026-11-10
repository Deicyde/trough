---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.stacks07LM, Crystalline.GlobalCrystallineSituation.SmallSite.crysFormsSheaf_vanishing, Crystalline.GlobalCrystallineSituation.SmallSite.underlineModules_vanishing, Crystalline.GlobalCrystallineSituation.SmallSite.underlineStructure_vanishing, Crystalline.GlobalCrystallineSituation.SmallSite.isZero_derivedZariskiDirectImage_of_vanishingHypotheses, Crystalline.GlobalCrystallineSituation.SmallSite.crystallineToAmbientDeRham, Crystalline.GlobalCrystallineSituation.SmallSite.truncation_comp_crystallineToAmbientDeRham
statement: formalized
proof: formalized
---

# 60.23 Applications

Section 60.23 of the Stacks Project, [Tag 07LL](https://stacks.math.columbia.edu/tag/07LL). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07LM, a proposition

[Tag 07LM](https://stacks.math.columbia.edu/tag/07LM) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.stacks07LM`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Proposition07LM.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Proposition07LM.lean#L99). The attribute's comment: “the whole proposition: for F a crystal in quasi-coherent O\_\{X/S}-modules on Cris(X/S), Ru\_\{X/S,*} carries the truncation map (F → F ⊗ Ω¹ → F ⊗ Ω² → ⋯) ⟶ F[0] to an isomorphism of D⁺(Ab(X\_Zar)), the differentials of the complex being the extensions of the canonical connection of F of 07J6; and Ru\_\{X/S,*}(F ⊗\_\{O\_\{X/S}} Ω^i\_\{X/S}) = 0 for every i > 0”.

> Let `F` be a crystal in quasi-coherent `𝒪_{X/S}`-modules on `Cris(X/S)`.  The truncation map
> of complexes
>
> `(F → F ⊗_{𝒪_{X/S}} Ω¹_{X/S} → F ⊗_{𝒪_{X/S}} Ω²_{X/S} → ⋯) ⟶ F[0]`
>
> becomes a quasi-isomorphism after applying `Ru_{X/S, *}` — it is carried to an isomorphism of
> `D⁺(Ab(X_{Zar}))` — and in fact `Ru_{X/S, *}(F ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0` for every `i > 0`.
>
> The complex is `(crystalDeRhamSheafData hF).complex`: its terms are the sheaves
> `F ⊗_{𝒪_{X/S}} Ω^i_{X/S}` and its differentials `crystalDeRhamDifferential hF i` are the
> extensions `m ⊗ ω ↦ ∇(m) ∧ ω + m ⊗ d ω` of the canonical connection `∇(m) = p₁^* m - p₀^* m` of
> [Stacks, Tag 07J6].

```lean
theorem stacks07LM (F : SheafOfModules.{u} (structureSheaf S)) (hF : F.IsQuasicoherentOnSite) :
    IsIso ((derivedZariskiDirectImageFunctor S).map
        (DerivedCategory.Plus.Qh.map
          ((HomotopyCategory.Plus.quotient _).map
            (sheafPlusTruncation S (crystalDeRhamSheafData hF).complex
              (CrystalDeRhamSheafData.singleComplex (F := F))
              (crystalDeRhamSheafData hF).truncation)))) ∧
      ∀ i : ℕ, 0 < i →
        IsZero ((derivedZariskiDirectImage S).obj (tensorDifferentialFormsSheaf F i))
```

## Tag 07LN, a remark

[Tag 07LN](https://stacks.math.columbia.edu/tag/07LN) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crysFormsSheaf_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean#L99). The attribute's comment: “the sheaves Ω^j\_\{X/S}, every j: Ω^j\_\{X/S} satisfies conditions (1) and (2) of 07JN, hence Ru\_\{X/S,*}(Ω^j\_\{X/S} ⊗ Ω^i\_\{X/S}) = 0 for every i > 0”.

> **Stacks Project, Remark 60.23.2, Tag 07LN, for the sheaves `Ω^j_{X/S}`.**  For every `j`,
> the sheaf of `𝒪_{X/S}`-modules `Ω^j_{X/S}` on `Cris(X/S)` — `crysFormsSheaf S j`, the sheaf
> associated with the presheaf `Ω^j_{X/S} = ⋀^j Ω_{X/S}` (`toCrysFormsSheaf` is locally bijective,
> `isLocallyInjective_toCrysFormsSheaf` and `isLocallySurjective_toCrysFormsSheaf`) — satisfies
> conditions (1) and (2) of [Stacks, Tag 07JN], and therefore, for every `i > 0`,
>
> `Ru_{X/S, *}(Ω^j_{X/S} ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0`.
>
> Condition (1) is `isLocallyQuasiCoherent_crysFormsSheaf`: the restriction of `Ω^j_{X/S}` to the
> ambient scheme `T` of an object is the sheaf associated with the restriction of the presheaf,
> that is `Ω^j_{T/S, δ}` ([Stacks, Tag 07IZ]), which is quasi-coherent ([Stacks, Tag 07IY]).
> Condition (2) is `isSurjectiveComparison_crysFormsSheaf`: the comparison maps of the presheaf
> `Ω^j_{X/S}` are locally surjective ([Stacks, Tag 07KM]), and so are those of its sheaf.  The
> vanishing is then `isZero_derivedZariskiDirectImage_of_vanishingHypotheses`.

```lean
theorem crysFormsSheaf_vanishing (j : ℕ) :
    IsLocallyQuasiCoherent (crysFormsSheaf S j) ∧
      CohomologyRestriction.IsSurjectiveComparison (crysFormsSheaf S j).val ∧
      ∀ i : ℕ, 0 < i →
        IsZero ((derivedZariskiDirectImage S).obj
          (tensorDifferentialFormsSheaf (crysFormsSheaf S j) i))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.underlineModules_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean#L126). The attribute's comment: “the sheaves F-underline: for F a quasi-coherent O\_X-module, F-underline satisfies conditions (1) and (2) of 07JN, hence Ru\_\{X/S,*}(F-underline ⊗ Ω^i\_\{X/S}) = 0 for every i > 0”.

> **Stacks Project, Remark 60.23.2, Tag 07LN, for the sheaves `F̲`.**  Let `F` be a
> quasi-coherent `𝒪_X`-module and `F̲` the sheaf of `𝒪_{X/S}`-modules on `Cris(X/S)` with
> `F̲(U, T, δ) = F(U)`.  Then `F̲` satisfies conditions (1) and (2) of [Stacks, Tag 07JN] — it is
> locally quasi-coherent, and its comparison morphisms `c_f` along the morphisms of `Cris(X/S)`
> whose map on ambient schemes is a closed immersion are surjective — and therefore, for every
> `i > 0`,
>
> `Ru_{X/S, *}(F̲ ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0`.
>
> Condition (1) is `isLocallyQuasiCoherent_underlineModules`: the restriction of `F̲` to the ambient
> scheme `T` of `(U, T, δ)` is the direct image of `F|_U` along the closed immersion `U ↪ T`.
> Condition (2) is `isSurjectiveComparison_underlineModules`.  The vanishing is then
> `isZero_derivedZariskiDirectImage_of_vanishingHypotheses`.

```lean
theorem underlineModules_vanishing (F : S.X.Modules) [F.IsQuasicoherent] :
    IsLocallyQuasiCoherent (underlineModules S F) ∧
      CohomologyRestriction.IsSurjectiveComparison (underlineModules S F).val ∧
      ∀ i : ℕ, 0 < i →
        IsZero ((derivedZariskiDirectImage S).obj
          (tensorDifferentialFormsSheaf (underlineModules S F) i))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.underlineStructure_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Remark07LN.lean#L158). The attribute's comment: “the sheaf O\_X-underline = G\_a-underline: it satisfies conditions (1) and (2) of 07JN, hence Ru\_\{X/S,*}(O\_X-underline ⊗ Ω^i\_\{X/S}) = 0 for every i > 0”.

> **Stacks Project, Remark 60.23.2, Tag 07LN, for `𝒪_X̲ = G_a̲`.**  The sheaf `𝒪_X̲` of
> `𝒪_{X/S}`-modules on `Cris(X/S)`, whose sections over `(U, T, δ)` are `Γ(U, 𝒪_U)` — the sheaf
> `G_a̲`, `underlineModules_unit_presheaf` — satisfies conditions (1) and (2) of
> [Stacks, Tag 07JN], and for every `i > 0`
>
> `Ru_{X/S, *}(𝒪_X̲ ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0`.
>
> This is `underlineModules_vanishing` at the quasi-coherent module `𝒪_X`.

```lean
theorem underlineStructure_vanishing :
    IsLocallyQuasiCoherent (underlineModules S (SheafOfModules.unit S.X.ringCatSheaf)) ∧
      CohomologyRestriction.IsSurjectiveComparison
        (underlineModules S (SheafOfModules.unit S.X.ringCatSheaf)).val ∧
      ∀ i : ℕ, 0 < i →
        IsZero ((derivedZariskiDirectImage S).obj
          (tensorDifferentialFormsSheaf (underlineModules S (SheafOfModules.unit S.X.ringCatSheaf))
            i))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isZero_derivedZariskiDirectImage_of_vanishingHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Vanishing07LMProof.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Vanishing07LMProof.lean#L152). The attribute's comment: “the remark's conclusion itself: Ru\_\{X/S,*}(F ⊗ Ω^i\_\{X/S}) = 0 for every i > 0 and EVERY sheaf of O\_\{X/S}-modules F satisfying conditions (1) local quasi-coherence and (2) local surjectivity of the comparison map c\_f along a closed immersion, of 07JN -- which is the generality the remark gives the vanishing clause of 07LM, weaker than being a crystal. The proof is the source's: 072W for u\_\{X/S} reduces to an affine open of X over an affine open of S, 07KL identifies the sections functors there with the cohomology of Cris(V/S|\_W), the coefficients transport along that restriction together with the two conditions, and 07LF kills the cohomology”.

> **Stacks Project, Remark 60.23.2, Tag 07LN.**  For any sheaf of `𝒪_{X/S}`-modules `F` on the
> small crystalline site satisfying conditions (1) and (2) of [Stacks, Proposition 60.19.1,
> Tag 07JN] — `F` is locally quasi-coherent, and for every morphism of `Cris(X/S)` whose map on
> ambient schemes is a closed immersion the comparison morphism `c_f : f^*F_{T'} ⟶ F_T` is
> surjective — and for every `i > 0`,
>
> `Ru_{X/S, *}(F ⊗_{𝒪_{X/S}} Ω^i_{X/S}) = 0`.
>
> This is the conclusion the remark observes holds at that generality rather than only for a
> crystal, the proof of [Stacks, Proposition 60.23.1, Tag 07LM] using nothing else about `F`.  It is
> the source's own argument: the local-to-global criterion [Stacks, Tag 072W] for `u_{X/S}` reduces
> it to an affine open `V` of `X` mapping into an affine open `W` of `S`, over such an open the
> right derived functors of `ℋ ↦ Γ(V, u_{X/S, *}ℋ)` are the cohomology of `Cris(V/S|_W)` by
> [Stacks, Tag 07KL], the coefficient sheaf transports to the restricted situation together with
> conditions (1) and (2), and [Stacks, Tag 07LF] kills that cohomology in every degree.

```lean
theorem isZero_derivedZariskiDirectImage_of_vanishingHypotheses
    (F : SheafOfModules.{u} (structureSheaf S)) (hqc : IsLocallyQuasiCoherent F)
    (hsurj : CohomologyRestriction.IsSurjectiveComparison F.val) (i : ℕ) (hi : 0 < i) :
    IsZero ((derivedZariskiDirectImage S).obj (tensorDifferentialFormsSheaf F i))
```

## Tag 07LP, an equation

[Tag 07LP](https://stacks.math.columbia.edu/tag/07LP) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystallineToAmbientDeRham`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Equation07LP.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Equation07LP.lean#L429). The attribute's comment: “the canonical map RΓ(Cris(X/S), F) ⟶ RΓ(T, F\_T ⊗ Ω*\_\{T/S,δ}) for a crystal in quasi-coherent modules F and an object (U, T, δ), built from 07LM, restriction to T and 07IZ”.

> **Stacks Project, Equation 07LP.**  In Situation 07MF, let `F` be a crystal in quasi-coherent
> modules on `Cris(X/S)` and let `(U, T, δ)` be an object of `Cris(X/S)`.  The canonical map
>
> `RΓ(Cris(X/S), F) ⟶ RΓ(T, F_T ⊗_{𝒪_T} Ω^*_{T/S,δ})`
>
> in `D⁺(Ab)`, constructed as in the source: `RΓ(Cris(X/S), F) = RΓ(Cris(X/S), F ⊗ Ω^*_{X/S})` by
> [Stacks, Tag 07LM] (`CrystalDeRhamSheafData.derivedGlobalSectionsIsoDeRham`, the inverse of the
> image of the truncation map, invertible after `Ru_{X/S, *}` and hence after `RΓ(Cris(X/S), -)`);
> then the restriction of global cohomology classes to `T`
> (`...CrystallineThickening.derivedGlobalSectionsToAmbient`); then the identification of the
> restriction of `F ⊗ Ω^*_{X/S}` to `T` with `F_T ⊗_{𝒪_T} Ω^*_{T/S,δ}` by [Stacks, Tag 07IZ]
> (`restrictCrystalDeRhamComplexIso`).  `truncation_comp_crystallineToAmbientDeRham` records that
> it is this composite.  The target is `RΓ(T, -)` of `ambientDeRhamComplex hF A`, read as a bounded
> below complex (`CrystalDeRhamSheafData.ambientComplexPlus`).

```lean
def crystallineToAmbientDeRham :
    (derivedGlobalSections S).obj (abelianSheaf F) ⟶
      (CrystallineThickening.derivedAmbientGlobalSectionsFunctor A).obj
        (DerivedCategory.Plus.Qh.obj ((HomotopyCategory.Plus.quotient _).obj
          ((crystalDeRhamSheafData hF).ambientComplexPlus A)))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.truncation_comp_crystallineToAmbientDeRham`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Equation07LP.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Equation07LP.lean#L445). The attribute's comment: “the canonical map is the composite of the source: 07LM, restriction of global cohomology classes to T, and 07IZ”.

> **The map of [Stacks, Equation 07LP] is the composite of the source.**  Precomposed with the
> image under `RΓ(Cris(X/S), -)` of the truncation map `F ⊗ Ω^*_{X/S} ⟶ F[0]` of
> [Stacks, Tag 07LM] — an isomorphism — it is the restriction to `T` of the global cohomology
> classes of `F ⊗ Ω^*_{X/S}`, followed by `RΓ(T, -)` of the identification
> `(F ⊗ Ω^*_{X/S})_T ≅ F_T ⊗_{𝒪_T} Ω^*_{T/S,δ}` of [Stacks, Tag 07IZ].

```lean
theorem truncation_comp_crystallineToAmbientDeRham :
    (derivedGlobalSectionsFunctor S).map
        (DerivedCategory.Plus.Qh.map
          ((HomotopyCategory.Plus.quotient _).map
            (sheafPlusTruncation S (crystalDeRhamSheafData hF).complex
              (CrystalDeRhamSheafData.singleComplex (F := F))
              (crystalDeRhamSheafData hF).truncation))) ≫
      (derivedGlobalSectionsFunctor S).map
          (CrystalDeRhamSheafData.singleFunctorIsoSingleComplex (F := F)).inv ≫
        crystallineToAmbientDeRham hF A =
      (CrystallineThickening.derivedGlobalSectionsToAmbient A).app _ ≫
        (CrystallineThickening.derivedAmbientGlobalSectionsFunctor A).map
          ((crystalDeRhamSheafData hF).derivedRestrictComplexIso A).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.23, Tag 07LL](https://stacks.math.columbia.edu/tag/07LL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
