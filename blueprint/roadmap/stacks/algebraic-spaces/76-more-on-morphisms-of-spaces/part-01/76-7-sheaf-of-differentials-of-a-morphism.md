---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.differentialsComparison, AlgebraicGeometry.SmallEtale.differentialsComparison_adjunct, AlgebraicGeometry.SmallEtale.eq_differentialsComparison, AlgebraicGeometry.SmallEtale.differentialsComparison_postcomp, AlgebraicGeometry.SmallEtale.existsUnique_postcomp_associatedRelativeDifferentialsDerivation, AlgebraicGeometry.SmallEtale.associatedRelativeDifferentialsDerivation, AlgebraicGeometry.SmallEtale.differentialsIso, AlgebraicGeometry.SmallEtale.postcomp_differentialsIso_hom
statement: formalized
proof: formalized
---

# 76.7 Sheaf of differentials of a morphism

Section 76.7 of the Stacks Project, [Tag 04CR](https://stacks.math.columbia.edu/tag/04CR). 16 tags here are carried by 85 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04CS, a lemma

[Tag 04CS](https://stacks.math.columbia.edu/tag/04CS) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.differentialsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean#L197). The attribute's comment: “the comparison map `c'' : (Ω_{X/Y})^a ⟶ 𝓕` of the source's proof, for a derivation of `𝒪_{X_étale}` annihilating the functions pulled back from `Y`”.

> **Stacks 04CS**, the comparison map.  Let `D` be a derivation of `𝒪_{X_étale}` with values
> in a sheaf of `𝒪_{X_étale}`-modules `𝓕` which annihilates every function pulled back from an
> open of `Y`.  This is the morphism `c'' : (Ω_{X/Y})^a ⟶ 𝓕` of `𝒪_{X_étale}`-modules adjoint,
> under the adjunction between the associated-module functor of Stacks 03DU (4) and restriction to
> the small Zariski site, to the morphism `c' : Ω_{X/Y} ⟶ ε_* 𝓕` through which the small Zariski
> restriction of `D` factors.
>
> At `𝓕 = Ω_{X_étale/Y_étale}` and `D` its universal derivation this is the map the source's proof
> calls `c''`.

```lean
public noncomputable def differentialsComparison
    (hD : ∀ (W : Y.Opens) (b : Γ(Y, W)), D.d (pullbackSection B hX f W b) = 0) :
    associatedRelativeDifferentials B hX f ⟶ F
```

**`AlgebraicGeometry.SmallEtale.differentialsComparison_adjunct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean#L225). The attribute's comment: “compatibility of the comparison map with the universal derivation `d_{X/Y}` on the small Zariski site”.

> **Stacks 04CS**, compatibility with the universal derivations on the small Zariski site.
> The adjunct `c' : Ω_{X/Y} ⟶ ε_* 𝓕` of the comparison map carries the universal derivation
> `d_{X/Y}` of `Ω_{X/Y}` to the small Zariski restriction of `D`.

```lean
public theorem differentialsComparison_adjunct
    (hD : ∀ (W : Y.Opens) (b : Γ(Y, W)), D.d (pullbackSection B hX f W b) = 0) :
    (f.universalRelativeDerivation).postcomp
        ((((associatedModuleAdjunction B X hX).homEquiv
          (Scheme.Hom.relativeDifferentials f) F)
            (differentialsComparison B hX f D hD))).val =
      zariskiRestriction B hX f D hD
```

**`AlgebraicGeometry.SmallEtale.eq_differentialsComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean#L239). The attribute's comment: “canonicity: the comparison map is the unique morphism whose adjunct carries `d_{X/Y}` to the small Zariski restriction of the derivation”.

> **Stacks 04CS**, canonicity of the comparison map.  It is the only morphism
> `(Ω_{X/Y})^a ⟶ 𝓕` whose adjunct carries the universal derivation `d_{X/Y}` to the small Zariski
> restriction of `D`.

```lean
public theorem eq_differentialsComparison
    (hD : ∀ (W : Y.Opens) (b : Γ(Y, W)), D.d (pullbackSection B hX f W b) = 0)
    (g : associatedRelativeDifferentials B hX f ⟶ F)
    (hg : (f.universalRelativeDerivation).postcomp
        ((((associatedModuleAdjunction B X hX).homEquiv
          (Scheme.Hom.relativeDifferentials f) F) g)).val =
      zariskiRestriction B hX f D hD) :
    g = differentialsComparison B hX f D hD
```

**`AlgebraicGeometry.SmallEtale.differentialsComparison_postcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean#L277). The attribute's comment: “naturality of the comparison map in the coefficient sheaf of modules”.

> **Stacks 04CS**, naturality of the comparison map in the coefficient sheaf: the comparison
> map of a derivation postcomposed with `α : 𝓕 ⟶ 𝓖` is the comparison map of the derivation
> followed by `α`.  So the comparison maps form a natural transformation out of `(Ω_{X/Y})^a`, and
> in particular an isomorphism `(Ω_{X/Y})^a ≅ 𝓕` exhibited by one of them is canonical.

```lean
public theorem differentialsComparison_postcomp
    (hD : ∀ (W : Y.Opens) (b : Γ(Y, W)), D.d (pullbackSection B hX f W b) = 0) (α : F ⟶ G) :
    differentialsComparison B hX f (D.postcomp α.val)
        (postcomp_pullbackSection_eq_zero B hX f D hD α) =
      differentialsComparison B hX f D hD ≫ α
```

**`AlgebraicGeometry.SmallEtale.existsUnique_postcomp_associatedRelativeDifferentialsDerivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsCorepresentable.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsCorepresentable.lean#L699). The attribute's comment: “corepresentability: `(Ω_{X/Y})^a` with `d^a` is the module of differentials”.

> **Stacks 04CS.**  The associated module `(Ω_{X/Y})^a` of the relative differentials of
> `f : X ⟶ Y`, together with the derivation `d^a`, is the module of differentials of
> `𝒪_{X_étale}` over `Y` in the sense of Stacks 04BN: every derivation `D` of `𝒪_{X_étale}` with
> values in a sheaf of `𝒪_{X_étale}`-modules `𝓖` which annihilates the functions pulled back from
> `Y` factors as `D = d^a ∘ g` for exactly one morphism `g : (Ω_{X/Y})^a ⟶ 𝓖` of sheaves of
> modules.
>
> The factorization is the comparison map `c''` of
> `AlgebraicGeometry.SmallEtale.differentialsComparison`; that it *is* a factorization, and that it
> is the only one, both come from the injectivity of restriction to the small Zariski site
> together with the identity
> `AlgebraicGeometry.SmallEtale.differentialsComparison_associatedRelativeDifferentialsDerivation`.
>
> The derivation is taken relative to the constant presheaf of integers, which imposes nothing
> beyond the Leibniz rule, so that the `Y`-linearity is carried by the hypothesis `hD` alone; see
> the implementation notes of
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentials.lean`.

```lean
public theorem existsUnique_postcomp_associatedRelativeDifferentialsDerivation
    {G : SheafOfModules.{u} (structureSheaf B X hX)}
    (D : PresheafOfModulesOfCommRing.Derivation' (R := (commRingStructureSheaf B X hX).obj) G.val
      (constIntMap (commRingStructureSheaf B X hX).obj))
    (hD : ∀ (W : Y.Opens) (b : Γ(Y, W)), D.d (pullbackSection B hX f W b) = 0) :
    ∃! g : associatedRelativeDifferentials B hX f ⟶ G,
      (associatedRelativeDifferentialsDerivation B hX f).postcomp g.val = D
```

**`AlgebraicGeometry.SmallEtale.associatedRelativeDifferentialsDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsDerivation.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsDerivation.lean#L245). The attribute's comment: “the derivation `d^a` into the associated module of differentials”.

> **The derivation `d^a` of the source's proof of Stacks 04CS**, on `(Ω_{X/Y})^a` itself:
> `AlgebraicGeometry.SmallEtale.sectionsDerivation` transported along the identification of the
> associated module with its sections description.

```lean
public noncomputable def associatedRelativeDifferentialsDerivation :
    PresheafOfModulesOfCommRing.Derivation' (R := (commRingStructureSheaf B X hX).obj)
      (associatedRelativeDifferentials B hX f).val
      (constIntMap (commRingStructureSheaf B X hX).obj)
```

**`AlgebraicGeometry.SmallEtale.differentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean#L460). The attribute's comment: “the canonical isomorphism `(Ω_{X/Y})^a ≅ Ω_{X_étale/Y_étale}`”.

> **Stacks 04CS.**  The canonical isomorphism `(Ω_{X/Y})^a ≅ Ω_{X_étale/Y_étale}`: both sides
> corepresent the functor of `Y_étale`-derivations of `𝒪_{X_étale}`, the left one by
> `AlgebraicGeometry.SmallEtale.existsUnique_postcomp_etaleAssociatedDerivation` and the right one
> by `AlgebraicGeometry.SmallEtale.universalDerivation_isUniversal`.

```lean
public noncomputable def differentialsIso :
    associatedRelativeDifferentials B X.property (schemeHom B f) ≅ sheafOfDifferentials B f
```

**`AlgebraicGeometry.SmallEtale.postcomp_differentialsIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean#L468). The attribute's comment: “compatibility of the canonical isomorphism with the universal derivations”.

> **Stacks 04CS**, compatibility with the universal derivations: the canonical isomorphism
> carries `d^a` to the universal `Y_étale`-derivation `d_{X_étale/Y_étale}`.

```lean
public theorem postcomp_differentialsIso_hom :
    (etaleAssociatedDerivation B f).postcomp (differentialsIso B f).hom.val =
      universalDerivation B f
```

**`AlgebraicGeometry.SmallEtale.isIso_universalDifferentialsComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleDifferentialsIso.lean#L518). The attribute's comment: “the comparison map `c''` is an isomorphism at `𝓕 = Ω_{X_étale/Y_étale}`”.

> **Stacks 04CS, the invertibility clause.**  The comparison map
> `c'' : (Ω_{X/Y})^a ⟶ 𝓕` of `AlgebraicGeometry.SmallEtale.differentialsComparison` is an
> isomorphism at `𝓕 = Ω_{X_étale/Y_étale}` carrying its universal derivation.  This is the
> statement the tag's "canonical isomorphism" amounts to for the map the source's proof
> produces.

```lean
public theorem isIso_universalDifferentialsComparison :
    IsIso (universalDifferentialsComparison B f)
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsSchemeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean, line 848](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean#L848). The attribute's comment: “the invertibility clause, for a morphism of schemes of the site read on the small étale site of the represented algebraic space”.

> **Stacks 04CS, the invertibility clause, for every morphism of schemes of the big fppf site
> over `S`.**  For a morphism `α : U ⟶ V` of schemes of the site, the sheaf of differentials of
> `α` read as a morphism of represented algebraic spaces — the module of differentials on the
> small étale site of `yoneda.obj U` — is the small-étale module attached by Stacks 03DU (4) to
> the Zariski sheaf of relative differentials `Ω_{U/V}` of Stacks 01US.
>
> This is the hypothesis `AlgebraicGeometry.Space.SheafOfDifferentialsSchemeComparison`, which the
> consumers of the final sentence of Stacks 04CU need.  It is
> `AlgebraicGeometry.SmallEtale.differentialsIso`, the canonical isomorphism
> `(Ω_{U/V})^a ≅ Ω_{U_étale/V_étale}` of Stacks 04CS, transported along the identification of the
> small étale site of `yoneda.obj U` with the small étale site of the scheme underlying `U`
> (`AlgebraicGeometry.Space.schemeDifferentialsIso`).

```lean
theorem sheafOfDifferentialsSchemeComparison :
    SheafOfDifferentialsSchemeComparison B S hS
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsSchemeVanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean, line 865](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean#L865). The attribute's comment: “the vanishing comparison for a morphism of schemes of the site”.

> **Stacks 04CS at zero objects**, the vanishing comparison that Stacks 04G9 needs:
> for a morphism `ψ : U ⟶ V` of schemes of the site, the spaces-level sheaf of differentials of
> `ψ` vanishes exactly when `Ω_{U/V}` does.

```lean
theorem sheafOfDifferentialsSchemeVanishing :
    SheafOfDifferentialsSchemeVanishing B S hS
```

## Tag 04CT, a definition

[Tag 04CT](https://stacks.math.columbia.edu/tag/04CT) in the Stacks Project.

**`AlgebraicGeometry.Space.sheafOfDifferentials`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean#L142). The attribute's comment: “the sheaf of differentials of a morphism of algebraic spaces”.

> **Stacks 04CT.** The sheaf of differentials `Ω_{X/Y}` of a morphism `f : X ⟶ Y` of algebraic
> spaces: the module of differentials of `f♯ : f⁻¹𝒪_Y ⟶ 𝒪_X`, realized as the associated sheaf of
> modules of the presheaf of sectionwise Kähler differentials of `f♯`.

```lean
noncomputable def sheafOfDifferentials (f : X ⟶ Y) : Modules.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.universalDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean#L150). The attribute's comment: “the universal `Y`-derivation `d_{X/Y}`”.

> **Stacks 04CT.** The universal `Y`-derivation `d_{X/Y} : 𝒪_X ⟶ Ω_{X/Y}`: the sectionwise
> Kähler differential followed by the unit of sheafification.

```lean
noncomputable def universalDerivation (f : X ⟶ Y) :
    PresheafOfModulesOfCommRing.Derivation' (sheafOfDifferentials B S hS f).val
      (structureSharpInverseImage B S hS f).hom
```

## Tag 04CU, a lemma

[Tag 04CU](https://stacks.math.columbia.edu/tag/04CU) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_etaleSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleBaseChange.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleBaseChange.lean#L190). The attribute's comment: “the identification `Ω_{X/Y}|_{U_étale} ≅ Ω_{U/V}` is the canonical one on a full square of étale charts: every comparison map of 04CX for a commutative square whose two vertical arrows are étale is an isomorphism. The already registered clause is the case of a square whose bottom edge is an identity”.

> **Stacks 04CU, the invertibility clause on a full square of étale charts.**  Let
>
> ```
> U --ψ--> V
> |        |
> a        b
> v        v
> X --f--> Y
> ```
>
> be a commutative square of algebraic spaces over `S` whose vertical arrows `a` and `b` are
> étale.  Then every comparison map `c : a^*Ω_{X/Y} ⟶ Ω_{U/V}` of Stacks 04CX for that square is
> an isomorphism.
>
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_etale` is this statement for
> `b = 𝟙 Y`.  The step to an arbitrary étale `b` is the étale-base comparison
> `Ω_{U/V} ≅ Ω_{U/(ψ ≫ b)}` of
> `AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso`, built from Stacks 03G8 and the
> clause `b^{-1}𝒪_Y = 𝒪_V` of Stacks 03LV: composing `c` with it produces, by
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_comp_sharpIsoHom`, a comparison map of the
> square with left edge `ψ ≫ b = a ≫ f`, which is invertible by the case already proved.

```lean
theorem isIso_of_isSheafOfDifferentialsMap_etaleSquare (f : X ⟶ Y) (a : U ⟶ X) (ψ : U ⟶ V)
    (b : V ⟶ Y) (ha : IsEtale B S hS a.hom) (hb : IsEtale B S hS b.hom)
    (hcomm : a ≫ f = ψ ≫ b)
    {c : (modulePullback B S hS a).obj (sheafOfDifferentials B S hS f) ⟶
      sheafOfDifferentials B S hS ψ}
    (hc : IsSheafOfDifferentialsMap B S hS a f ψ c) : IsIso c
```

**`AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleComparison.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleComparison.lean#L126). The attribute's comment: “the identification `Ω_{X/Y}|_{U_étale} ≅ Ω_{U/V}` is the canonical one: every comparison map of 04CX along an étale `a : U ⟶ X`, for a square whose bottom edge is an identity, is an isomorphism”.

> **The comparison map of Stacks 04CX along an étale morphism is an isomorphism.**  By
> uniqueness of the comparison map it is the identification of Stacks 04CU,
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleSourceLocalizationIso`.
>
> The left edge of the square is taken as a morphism `p' : U ⟶ Y` together with an equality
> `a ≫ f = p'`, so that the statement applies at whatever spelling of the composite a caller
> has.

```lean
theorem isIso_of_isSheafOfDifferentialsMap_etale (a : U ⟶ X) (ha : IsEtale B S hS a.hom)
    (f : X ⟶ Y) (p' : U ⟶ Y) (hp' : a ≫ f = p')
    {c : (modulePullback B S hS a).obj (sheafOfDifferentials B S hS f) ⟶
      sheafOfDifferentials B S hS p'}
    (hc : IsSheafOfDifferentialsMap B S hS a f p' c) : IsIso c
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean#L239). The attribute's comment: “the étale-base step: Ω\_\{X/Y} = Ω\_\{X/Z} when the two structure maps differ by an isomorphism of their sources, which is what 03G8 and the clause `b⁻¹𝒪_Y = 𝒪_V` of 03LV supply for an étale `b : V ⟶ Y` at `p = ψ`, `q = ψ ≫ b`”.

> **Stacks 04CU, the étale-base step.**  If the structure maps of `p : X ⟶ Y` and `q : X ⟶ Z`
> differ by an isomorphism `e` of their sources, then the two sheaves of differentials agree:
> `Ω_{X/Y} ≅ Ω_{X/Z}`.
>
> Both sheaves corepresent the same functor of derivations — a `Y`-derivation and a `Z`-derivation
> are the same additive map, by `PresheafOfModulesOfCommRing.Derivation'.precompBase` applied to `e` and to
> its inverse — so the identification is the one matching the two universal derivations.
>
> Applied to `ψ : U ⟶ V` and `ψ ≫ b : U ⟶ Y` for an étale `b : V ⟶ Y` this is the equality
> `Ω_{U/V} = Ω_{U/Y}` which the final sentence of the source's proof uses.

```lean
def sheafOfDifferentialsIsoOfSharpIso
    (he : e.hom ≫ structureSharpInverseImage B S hS p =
      structureSharpInverseImage B S hS q) :
    sheafOfDifferentials B S hS p ≅ sheafOfDifferentials B S hS q
```

**`AlgebraicGeometry.Space.universalDerivation_sheafOfDifferentialsIsoOfSharpIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean#L283). The attribute's comment: “the étale-base step carries one universal derivation to the other”.

> **Stacks 04CU, the étale-base step is canonical.**  The identification of
> `AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso` carries the universal
> `Y`-derivation `d_{X/Y}` of a local section to the universal `Z`-derivation `d_{X/Z}` of the
> same section, so it is the comparison the source names and not merely some isomorphism.

```lean
lemma universalDerivation_sheafOfDifferentialsIsoOfSharpIso
    (he : e.hom ≫ structureSharpInverseImage B S hS p =
      structureSharpInverseImage B S hS q)
    {W : (SmallEtale B S hS X.1)ᵒᵖ} (x : (structureRingSheaf B S hS X).obj.obj W) :
    (((sharpIsoHom B S hS p q e he).val.app W).hom)
        ((universalDerivation B S hS p).d x) =
      (universalDerivation B S hS q).d x
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsEtaleLocalizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleLocalization.lean#L342). The attribute's comment: “the identification Ω\_\{X/Y}|\_\{U\_étale} ≅ Ω\_\{U/V} on a square of étale charts, from the étale-source localization of 03LP, 03LQ and 04BO and the étale-base comparison of 03G8 and 03LV”.

> **Stacks 04CU.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` and let
> `a ≫ f = ψ ≫ b` be a commutative square with `a : U ⟶ X` and `b : V ⟶ Y` étale.  Then the
> restriction of `Ω_{X/Y}` to the small étale site of `U` — the pullback of `𝒪_X`-modules along
> `a`, by the abuse of notation of Stacks' Equation 03LW — is `Ω_{U/V}`.
>
> The source's proof has two steps and both are carried out here.  Its first step is the
> étale-source localization `Ω_{X/Y}|_{U_étale} = Ω_{U/Y}` of Stacks 03LP, 03LQ and 04BO, which is
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleSourceLocalizationIso` at the étale `a`.  Its
> second step is the identification `ψ^{-1}𝒪_V = (ψ ≫ b)^{-1}𝒪_Y` under the structure maps, which
> is `AlgebraicGeometry.Space.etaleBaseInverseImageStructureSheafIso` and its compatibility, from
> the composition law of Stacks 03G8 and the clause `b^{-1}𝒪_Y = 𝒪_V` of Stacks 03LV for the
> étale `b`.  The square then identifies `Ω_{U/Y}` with `Ω_{U/(ψ ≫ b)}`, and
> `AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso` identifies that with `Ω_{U/V}`.

```lean
noncomputable def sheafOfDifferentialsEtaleLocalizationIso (f : X ⟶ Y) (a : U ⟶ X) (ψ : U ⟶ V)
    (b : V ⟶ Y) (ha : IsEtale B S hS a.hom) (hb : IsEtale B S hS b.hom)
    (hcomm : a ≫ f = ψ ≫ b) :
    (modulePullback B S hS a).obj (sheafOfDifferentials B S hS f) ≅
      sheafOfDifferentials B S hS ψ
```

**`AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparison.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparison.lean#L356). The attribute's comment: “the comparison map of an étale triangle over the base is an isomorphism”.

> **Stacks 04CU: the comparison map of a triangle over `Y` whose upper edge is étale is an
> isomorphism.**  Let `a : U ⟶ X` be étale, let `f : X ⟶ Y`, and let `q : U ⟶ Y` be the
> composite.  Any morphism `c : a^*Ω_{X/Y} ⟶ Ω_{U/Y}` with the characterizing property of
> Stacks 04CX is an isomorphism.
>
> By `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap` there is at most one such `c`, and
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_etaleSourceLocalizationHom` exhibits one
> which is the forward map of
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleSourceLocalizationIso`.

```lean
theorem isIso_of_isSheafOfDifferentialsMap_of_isEtale (a : U ⟶ X) (ha : IsEtale B S hS a.hom)
    (f : X ⟶ Y) (q : U ⟶ Y) (haq : a ≫ f = q)
    {c : (modulePullback B S hS a).obj (sheafOfDifferentials B S hS f) ⟶
      sheafOfDifferentials B S hS q}
    (hc : IsSheafOfDifferentialsMap B S hS a f q c) : IsIso c
```

**`AlgebraicGeometry.Space.pullbackDifferentialsMap_eq_etaleSourceLocalizationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparisonMap.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparisonMap.lean#L94). The attribute's comment: “the étale-source localization is the comparison map of Stacks 04CX”.

> **The comparison map of Stacks 04CX along an étale morphism is the étale-source
> localization of Stacks 04CU.**  The two morphisms `a^*Ω_{X/Y} ⟶ Ω_{U/Y}` both have the
> characterizing property of Stacks 04CX, and at most one morphism does, by
> `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap`.

```lean
theorem pullbackDifferentialsMap_eq_etaleSourceLocalizationHom (a : U ⟶ X)
    (ha : IsEtale B S hS a.hom) (f : X ⟶ Y) :
    pullbackDifferentialsMap B S hS a f = etaleSourceLocalizationHom B S hS a ha f
```

**`AlgebraicGeometry.Space.isIso_pullbackDifferentialsMap_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparisonMap.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparisonMap.lean#L111). The attribute's comment: “the comparison map `a^*Ω_{X/Y} ⟶ Ω_{U/Y}` along an étale `a` is invertible”.

> **Stacks 04CU, the étale-source localization as an invertibility.**  For an étale
> `a : U ⟶ X` and any `f : X ⟶ Y`, the comparison map
> `c_a : a^*Ω_{X/Y} ⟶ Ω_{U/Y}` of Stacks 04CX — the first map
> `AlgebraicGeometry.Space.pullbackDifferentialsMap` of the transitivity sequence of Stacks 05Z8
> at the square over the identity of `Y` — is an isomorphism.
>
> It is the forward map of
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleSourceLocalizationIso`.

```lean
theorem isIso_pullbackDifferentialsMap_of_isEtale (a : U ⟶ X) (ha : IsEtale B S hS a.hom)
    (f : X ⟶ Y) : IsIso (pullbackDifferentialsMap B S hS a f)
```

**`AlgebraicGeometry.Space.derivationEtalePullbackEquiv_etaleSourceLocalizationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean#L421). The attribute's comment: “the étale-source comparison is the one matching the universal derivations”.

> **The defining property of the forward comparison.**  Read as a `Y`-derivation of `𝒪_U`
> through the four bijections, it is the universal `Y`-derivation `d_{U/Y}`.

```lean
theorem derivationEtalePullbackEquiv_etaleSourceLocalizationHom (a : U ⟶ X)
    (ha : IsEtale B S hS a.hom) (f : X ⟶ Y) :
    derivationEtalePullbackEquiv B S hS a ha f (sheafOfDifferentials B S hS (a ≫ f))
        (etaleSourceLocalizationHom B S hS a ha f) =
      universalDerivation B S hS (a ≫ f)
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsEtaleSourceLocalizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean#L459). The attribute's comment: “the étale-source localization `a^*Ω_{X/Y} ≅ Ω_{U/Y}` along an étale `a : U ⟶ X`: the first step of the source's proof, Properties of Spaces 03LP and Equation 03LQ together with Modules on Sites 04BO”.

> **Stacks 04CU, the étale-source localization.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` and let `a : U ⟶ X` be étale.  The restriction of `Ω_{X/Y}` to the small étale
> site of `U` — the pullback of `𝒪_X`-modules along `a`, by the abuse of notation of Stacks'
> Equation 03LW — is the sheaf of differentials of the composite:
>
> `a^*Ω_{X/Y} ≅ Ω_{U/Y}`.
>
> Both sides corepresent the functor of `Y`-derivations of `𝒪_U`, the left-hand side by
> `AlgebraicGeometry.Space.derivationEtalePullbackEquiv` and the right-hand side by its own
> universal property, so they are canonically isomorphic; the two morphisms are the ones through
> which the two universal derivations factor.
>
> This is the clause of Stacks 04CU that
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleLocalizationIso` consumes directly.  Together
> with the étale-base step `AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso` it gives the
> identification `Ω_{X/Y}|_{U_étale} ≅ Ω_{U/V}` on a square of étale charts that the source
> states.

```lean
def sheafOfDifferentialsEtaleSourceLocalizationIso (a : U ⟶ X) (ha : IsEtale B S hS a.hom)
    (f : X ⟶ Y) :
    (modulePullback B S hS a).obj (sheafOfDifferentials B S hS f) ≅
      sheafOfDifferentials B S hS (a ≫ f)
```

**`AlgebraicGeometry.Space.universalDerivation_etaleSourceLocalizationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceLocalization.lean#L487). The attribute's comment: “the étale-source localization carries the universal derivation of the restriction to the universal derivation `d_{U/Y}`, on local sections”.

> **Stacks 04CU, the étale-source localization on local sections.**  Reading the forward map of
> the identification `a^*Ω_{X/Y} ≅ Ω_{U/Y}` as a `Y`-derivation of `𝒪_U`, by the four bijections of
> `AlgebraicGeometry.Space.derivationEtalePullbackEquiv`, returns the universal differential
> `d_{U/Y}(x)` of every local section `x` of `𝒪_U`.  So the identification is the canonical
> comparison and not merely some isomorphism.

```lean
theorem universalDerivation_etaleSourceLocalizationHom (a : U ⟶ X) (ha : IsEtale B S hS a.hom)
    (f : X ⟶ Y) {W : (SmallEtale B S hS U.1)ᵒᵖ}
    (x : (structureRingSheaf B S hS U).obj.obj W) :
    (derivationEtalePullbackEquiv B S hS a ha f (sheafOfDifferentials B S hS (a ≫ f))
        (sheafOfDifferentialsEtaleSourceLocalizationIso B S hS a ha f).hom).d x =
      (universalDerivation B S hS (a ≫ f)).d x
```

**`AlgebraicGeometry.Space.isSheafOfDifferentialsMap_etaleBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMapTransport.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMapTransport.lean#L249). The attribute's comment: “the étale-base step for the comparison map of 04CX: the comparison map over `W` read through the identifications `Ω_{V/W} ≅ Ω_{V/Z}` and `Ω_{U/W} ≅ Ω_{U/Z}` is the comparison map over `Z`”.

> **Stacks 04CU, the étale-base step for the comparison map of Stacks 04CX.**  Let
> `ψ : U ⟶ V` be a morphism of algebraic spaces, `q : V ⟶ W` a structure morphism and
> `cw : W ⟶ Z` étale.  The comparison map `c_ψ : ψ^*Ω_{V/W} ⟶ Ω_{U/W}` of the square over `W`,
> read through the étale-base identifications `Ω_{V/W} ≅ Ω_{V/Z}` of the right edge and
> `Ω_{U/W} ≅ Ω_{U/Z}` of the left edge, has the characterizing property of the comparison map of
> the same square over `Z`.
>
> `AlgebraicGeometry.Space.sheafOfDifferentialsIsoOfSharpIso` supplies those identifications as
> isomorphisms of objects; what makes them compatible with the comparison map is that each carries
> one universal derivation to the other, so that
> `AlgebraicGeometry.Space.IsSheafOfDifferentialsMap.map_comp` and
> `AlgebraicGeometry.Space.IsSheafOfDifferentialsMap.comp_right` apply.

```lean
theorem isSheafOfDifferentialsMap_etaleBase :
    IsSheafOfDifferentialsMap B S hS ψ (q ≫ cw) ((ψ ≫ q) ≫ cw)
      ((modulePullback B S hS ψ).map (etaleBaseDifferentialsIso B S hS q cw hcw).inv ≫
        pullbackDifferentialsMap B S hS ψ q ≫
          (etaleBaseDifferentialsIso B S hS (ψ ≫ q) cw hcw).hom)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isSheafOfDifferentialsMap_etaleSourceLocalizationHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMapEtale.lean#L157), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparison.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsEtaleSourceComparison.lean#L343) (StacksFrontier): “the étale-source identification is the comparison map of 04CX”.
- [`AlgebraicGeometry.Space.sheafOfDifferentialsSchemeComparison`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean#L848), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean, line 854](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeTransport.lean#L854) (StacksFrontier): “the 'in particular' clause: for `U` and `V` schemes of the site the sheaf of differentials of `U ⟶ V` read on the small étale site agrees with the usual sheaf of differentials of the morphism of schemes, through the associated module of 03DU (4). The identification `Ω_{X/Y}|_{U_étale} = Ω_{U/V}` itself is elsewhere, on `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleLocalizationIso` and its chart form”.

## Tag 04CV, a lemma

[Tag 04CV](https://stacks.math.columbia.edu/tag/04CV) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsQuasicoherent.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsQuasicoherent.lean#L222).

> **Stacks 04CV.**  The sheaf of differentials `Ω_{X/Y}` of a morphism `f : X ⟶ Y` of
> algebraic spaces over a scheme `S` is a quasi-coherent `𝒪_X`-module on the small étale site
> of `X`.
>
> The proof follows the source.  An atlas `q : V ⟶ Y` of the target lifts, by Stacks 02X1, to a
> surjective étale chart `p : U ⟶ X` of the source together with a morphism `α : U ⟶ V` of
> schemes making the square commute.  The identification of Stacks 04CU then reads the pullback
> of `Ω_{X/Y}` along `p` as the sheaf of differentials of `α`, which
> `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeComparison` identifies with the small-étale
> module associated to the Zariski sheaf of
> relative differentials of `α`; that module is quasi-coherent because `Ω_{U/V}` is
> (Stacks 08S2) and because the associated module of a quasi-coherent module is quasi-coherent
> (`AlgebraicGeometry.Space.isQuasicoherentOnSite_representedAssociatedModule`).  Finally
> Stacks 03M0, conditions (1) and (2), returns quasi-coherence on `X` from quasi-coherence of the
> pullback along one surjective étale chart, the pullback of modules and étale restriction being
> matched by Equation 03LW.
>
> Nothing is carried: the two clauses of Stacks 04CU proper are used through
> `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleLocalizationIso`, and the final sentence,
> read through Stacks 04CS, through
> `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeComparison`; see the implementation
> notes.

```lean
theorem isQuasicoherentOnSite_sheafOfDifferentials
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    (sheafOfDifferentials B S hS f).IsQuasicoherentOnSite
```

## Tag 04CW, a remark

[Tag 04CW](https://stacks.math.columbia.edu/tag/04CW) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.differentialsDescentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean#L149). The attribute's comment: “the descent isomorphism `α : s^*Ω_{U/Y} ⟶ Ω_{R/Y} ⟶ t^*Ω_{U/Y}`”.

> The descent isomorphism `α : s^*Ω_{U/Y} ⟶ Ω_{R/Y} ⟶ t^*Ω_{U/Y}` attached to two étale
> morphisms `s, t : R ⟶ U` of schemes over `Y` inducing the same morphism to `Y`. Both comparison
> maps are isomorphisms because `s` and `t` are étale.

```lean
noncomputable def differentialsDescentIso (p : U ⟶ Y) (s t : R ⟶ U) (q : R ⟶ Y)
    (hs : s ≫ p = q) (ht : t ≫ p = q) [Etale s] [Etale t] :
    (Scheme.Modules.pullback s).obj (relativeDifferentials p) ≅
      (Scheme.Modules.pullback t).obj (relativeDifferentials p)
```

**`AlgebraicGeometry.Scheme.Hom.differentialsDescentIso_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean#L240). The attribute's comment: “the cocycle condition satisfied by `α`”.

> **Stacks 04CW**, the cocycle condition.  Let `T` carry three étale legs `a₀, a₁, a₂ : T ⟶ U`
> over `Y` and three morphisms `g₀₁, g₁₂, g₀₂ : T ⟶ R` realizing the pairs `(a₀, a₁)`, `(a₁, a₂)`
> and `(a₀, a₂)` through `(s, t)`.  Then the pullback of `α` along `g₀₂` is the composite of its
> pullbacks along `g₀₁` and `g₁₂`, each normalized by the canonical factorization isomorphisms.
> So `α` is a descent datum.

```lean
theorem differentialsDescentIso_cocycle {T : Scheme.{u}} (p : U ⟶ Y) (s t : R ⟶ U) (q : R ⟶ Y)
    (hs : s ≫ p = q) (ht : t ≫ p = q) [Etale s] [Etale t]
    (g₀₁ g₁₂ g₀₂ : T ⟶ R) {a₀ a₁ a₂ : T ⟶ U} (r : T ⟶ Y) [Etale a₀] [Etale a₁] [Etale a₂]
    (h₀₁s : g₀₁ ≫ s = a₀) (h₀₁t : g₀₁ ≫ t = a₁) (h₁₂s : g₁₂ ≫ s = a₁)
    (h₁₂t : g₁₂ ≫ t = a₂) (h₀₂s : g₀₂ ≫ s = a₀) (h₀₂t : g₀₂ ≫ t = a₂)
    (h₀ : a₀ ≫ p = r) (h₁ : a₁ ≫ p = r) (h₂ : a₂ ≫ p = r) :
    (Scheme.Modules.pullbackFactorIso g₀₂ s h₀₂s (relativeDifferentials p)).inv ≫
        (Scheme.Modules.pullback g₀₂).map (differentialsDescentIso p s t q hs ht).hom ≫
          (Scheme.Modules.pullbackFactorIso g₀₂ t h₀₂t (relativeDifferentials p)).hom =
      ((Scheme.Modules.pullbackFactorIso g₀₁ s h₀₁s (relativeDifferentials p)).inv ≫
          (Scheme.Modules.pullback g₀₁).map (differentialsDescentIso p s t q hs ht).hom ≫
            (Scheme.Modules.pullbackFactorIso g₀₁ t h₀₁t (relativeDifferentials p)).hom) ≫
        ((Scheme.Modules.pullbackFactorIso g₁₂ s h₁₂s (relativeDifferentials p)).inv ≫
          (Scheme.Modules.pullback g₁₂).map (differentialsDescentIso p s t q hs ht).hom ≫
            (Scheme.Modules.pullbackFactorIso g₁₂ t h₁₂t (relativeDifferentials p)).hom)
```

**`AlgebraicGeometry.Scheme.Hom.differentialsDescentIso_pullbackDescentIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean#L271). The attribute's comment: “for a quotient which is a scheme, `α` agrees with the canonical descent datum of `π^*Ω_{X/Y}`”.

> **For a quotient which is a scheme, `α` is the canonical descent datum of `π^*Ω_{X/Y}`.**
> For `π : U ⟶ X` over `Y` with `s ≫ π = t ≫ π`, the canonical map `π^*Ω_{X/Y} ⟶ Ω_{U/Y}` of
> Stacks 01UV carries the canonical descent isomorphism of `π^*Ω_{X/Y}` to `α`; when `π` is étale
> that map is an isomorphism, so the module `α` descends to is `Ω_{X/Y}`.  The same identification
> for a quotient which is an algebraic space is
> `AlgebraicGeometry.Space.sheafOfDifferentialsDescentIso_canonicalComparison` in
> `StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescent.lean`; here the comparison map
> is constructed rather than hypothesized, so no input beyond the square is needed.

```lean
theorem differentialsDescentIso_pullbackDescentIso {X : Scheme.{u}} (pX : X ⟶ Y) (π : U ⟶ X)
    (p : U ⟶ Y) (hp : π ≫ pX = p) (s t : R ⟶ U) (q : R ⟶ Y) (hs : s ≫ p = q)
    (ht : t ≫ p = q) [Etale s] [Etale t] (hπ : s ≫ π = t ≫ π) :
    (Scheme.Modules.pullbackDescentIso π hπ (relativeDifferentials pX)).hom ≫
        (Scheme.Modules.pullback t).map (triangleDifferentialsMap π pX p hp) =
      (Scheme.Modules.pullback s).map (triangleDifferentialsMap π pX p hp) ≫
        (differentialsDescentIso p s t q hs ht).hom
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsDescentIso_canonicalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescent.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescent.lean#L162). The attribute's comment: “the module `α` descends to is `Ω_{X/Y}`: `α` is the transition isomorphism of the canonical descent datum of `Ω_{X/Y}` on a presentation `π : U ⟶ X` of an algebraic space”.

> **Stacks 04CW.** For a presentation `π : U ⟶ X` of an algebraic space over `Y` and
> `s, t : R ⟶ U` with `s ≫ π = t ≫ π`, the descent isomorphism `α` is the transition isomorphism
> of the canonical descent datum of `Ω_{X/Y}`: the comparison map `c_π : π^*Ω_{X/Y} ⟶ Ω_{U/Y}`
> carries the canonical comparison of the two inverse images of `Ω_{X/Y}` to `α`.  So the module
> `α` descends to is `Ω_{X/Y}`.
>
> Invertibility of `c_s` and `c_t` is the étale-localization clause of Stacks 04CU; the identity
> it is divided out of,
> `AlgebraicGeometry.Space.canonicalComparison_comp_sheafOfDifferentialsMap`, needs no
> invertibility.

```lean
theorem sheafOfDifferentialsDescentIso_canonicalComparison (pX : X ⟶ Y) (π : U ⟶ X) (p : U ⟶ Y)
    {s t : R ⟶ U} (q : R ⟶ Y) (hπ : s ≫ π = t ≫ π)
    {cπ : (modulePullback B S hS π).obj (sheafOfDifferentials B S hS pX) ⟶
      sheafOfDifferentials B S hS p}
    {cs : (modulePullback B S hS s).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS q}
    {ct : (modulePullback B S hS t).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS q}
    (hcπ : IsSheafOfDifferentialsMap B S hS π pX p cπ)
    (hcs : IsSheafOfDifferentialsMap B S hS s p q cs)
    (hct : IsSheafOfDifferentialsMap B S hS t p q ct) [IsIso cs] [IsIso ct] :
    (QuasiCoherentDescent.canonicalComparison s t π π hπ
          (sheafOfDifferentials B S hS pX)).hom ≫
        (modulePullback B S hS t).map cπ =
      (modulePullback B S hS s).map cπ ≫
        (sheafOfDifferentialsDescentIso B S hS cs ct).hom
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsDescentIsoOfEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean#L106). The attribute's comment: “the descent isomorphism itself: `alpha : s^*Omega_{U/Y} -> t^*Omega_{U/Y}`, built from the two etale projections of the groupoid”.

> **Stacks 04CW.** The descent isomorphism `α : s^*Ω_{U/Y} ⟶ Ω_{R/Y} ⟶ t^*Ω_{U/Y}` attached to
> two *étale* morphisms `s, t : R ⟶ U` of algebraic spaces inducing the same morphism `q : R ⟶ Y`.
>
> It is the comparison map `c_s` of Stacks 04CX for the triangle `s ≫ p = q`, namely
> `AlgebraicGeometry.Space.sheafOfDifferentialsMap`, followed by the inverse of the comparison map
> `c_t` of the triangle `t ≫ p = q`.  Both comparison maps are isomorphisms because `s` and `t`
> are étale: that is the étale-localization clause of Stacks 04CU, in the form
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_of_isEtale`.

```lean
def sheafOfDifferentialsDescentIsoOfEtale (p : U ⟶ Y) {s t : R ⟶ U} {q : R ⟶ Y}
    (hs : IsEtale B S hS s.hom) (ht : IsEtale B S hS t.hom) (hsq : s ≫ p = q)
    (htq : t ≫ p = q) :
    (modulePullback B S hS s).obj (sheafOfDifferentials B S hS p) ≅
      (modulePullback B S hS t).obj (sheafOfDifferentials B S hS p)
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsDescentIsoOfEtale_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean#L254). The attribute's comment: “the cocycle condition for that isomorphism, which is what the remark leaves to the reader to verify”.

> **Stacks 04CW**, the cocycle condition.  Let the test space `T` carry three étale legs
> `a₀, a₁, a₂ : T ⟶ U` over `Y` and three morphisms `g₀₁, g₁₂, g₀₂ : T ⟶ R` realizing the pairs
> `(a₀, a₁)`, `(a₁, a₂)` and `(a₀, a₂)` through `(s, t)` — the situation of the three projections
> of a triple fibre product.  Then the pullback of `α` along `g₀₂` is the composite of its
> pullbacks along `g₀₁` and `g₁₂`, each normalized by the comparisons of iterated inverse images.
> So `α` is a descent datum, which is the check the source leaves to the reader.

```lean
theorem sheafOfDifferentialsDescentIsoOfEtale_cocycle {T : AlgebraicSpaces B S hS} (p : U ⟶ Y)
    {s t : R ⟶ U} (q : R ⟶ Y)
    (hs : IsEtale B S hS s.hom) (ht : IsEtale B S hS t.hom) (hsq : s ≫ p = q)
    (htq : t ≫ p = q) (g₀₁ g₁₂ g₀₂ : T ⟶ R) {a₀ a₁ a₂ : T ⟶ U} (r : T ⟶ Y)
    (h₀ : IsEtale B S hS a₀.hom) (h₁ : IsEtale B S hS a₁.hom) (h₂ : IsEtale B S hS a₂.hom)
    (h₀₁s : g₀₁ ≫ s = a₀) (h₀₁t : g₀₁ ≫ t = a₁) (h₁₂s : g₁₂ ≫ s = a₁)
    (h₁₂t : g₁₂ ≫ t = a₂) (h₀₂s : g₀₂ ≫ s = a₀) (h₀₂t : g₀₂ ≫ t = a₂)
    (hr₀ : a₀ ≫ p = r) (hr₁ : a₁ ≫ p = r) (hr₂ : a₂ ≫ p = r) :
    (QuasiCoherentDescent.pullbackComparison B S hS g₀₂ s a₀ h₀₂s
          (sheafOfDifferentials B S hS p)).hom ≫
        (modulePullback B S hS g₀₂).map
          (sheafOfDifferentialsDescentIsoOfEtale B S hS p hs ht hsq htq).hom ≫
        (QuasiCoherentDescent.pullbackComparison B S hS g₀₂ t a₂ h₀₂t
          (sheafOfDifferentials B S hS p)).inv =
      ((QuasiCoherentDescent.pullbackComparison B S hS g₀₁ s a₀ h₀₁s
            (sheafOfDifferentials B S hS p)).hom ≫
          (modulePullback B S hS g₀₁).map
            (sheafOfDifferentialsDescentIsoOfEtale B S hS p hs ht hsq htq).hom ≫
          (QuasiCoherentDescent.pullbackComparison B S hS g₀₁ t a₁ h₀₁t
            (sheafOfDifferentials B S hS p)).inv) ≫
        ((QuasiCoherentDescent.pullbackComparison B S hS g₁₂ s a₁ h₁₂s
            (sheafOfDifferentials B S hS p)).hom ≫
          (modulePullback B S hS g₁₂).map
            (sheafOfDifferentialsDescentIsoOfEtale B S hS p hs ht hsq htq).hom ≫
          (QuasiCoherentDescent.pullbackComparison B S hS g₁₂ t a₂ h₁₂t
            (sheafOfDifferentials B S hS p)).inv)
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsDescentIsoOfEtale_canonicalComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsDescentOfEtale.lean#L314). The attribute's comment: “the module `α` descends to is `Ω_{X/Y}`: `α` is the transition isomorphism of the canonical descent datum of `Ω_{X/Y}` on a presentation `π : U ⟶ X` which the two étale projections equalize”.

> **Stacks 04CW.** For a presentation `π : U ⟶ X` of an algebraic space `X` over `Y`, with
> `p = π ≫ pX`, and étale `s, t : R ⟶ U` with `s ≫ π = t ≫ π` inducing the same morphism
> `q : R ⟶ Y`, the descent isomorphism `α` is the transition isomorphism of the canonical descent
> datum of `Ω_{X/Y}`: the comparison map `c_π : π^*Ω_{X/Y} ⟶ Ω_{U/Y}` of Stacks 04CX, namely
> `AlgebraicGeometry.Space.sheafOfDifferentialsMap`, carries the canonical comparison of the two
> inverse images of `Ω_{X/Y}` to `α`.  When `π` is étale `c_π` is an isomorphism, by
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_of_isEtale`, so for a presentation
> the module `α` descends to is `Ω_{X/Y}`; étaleness of `π` is not needed for the identity itself
> and is not assumed.
>
> The identity `α` is divided out of,
> `AlgebraicGeometry.Space.canonicalComparison_comp_sheafOfDifferentialsMap`, needs no
> invertibility; the invertibility of `c_s` and `c_t` that forms `α` is derived from étaleness of
> `s` and `t` by Stacks 04CU.
>
> The cocycle condition is the separate statement
> `AlgebraicGeometry.Space.sheafOfDifferentialsDescentIsoOfEtale_cocycle` above, and in the
> scheme-level vocabulary `AlgebraicGeometry.Scheme.Hom.differentialsDescentIso_cocycle` in
> `StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/EtaleDescentDatum.lean`.  Together with
> `AlgebraicGeometry.Space.sheafOfDifferentialsDescentIsoOfEtale` and that cocycle condition, this
> is the source's remark in the vocabulary of algebraic spaces: the module obtained by gluing
> `Ω_{U/Y}` along `α` is `Ω_{X/Y}`.

```lean
theorem sheafOfDifferentialsDescentIsoOfEtale_canonicalComparison (pX : X ⟶ Y) (π : U ⟶ X)
    (p : U ⟶ Y) {s t : R ⟶ U} (q : R ⟶ Y) (hπ : s ≫ π = t ≫ π) (hπp : π ≫ pX = p)
    (hs : IsEtale B S hS s.hom) (ht : IsEtale B S hS t.hom) (hsq : s ≫ p = q)
    (htq : t ≫ p = q) :
    (QuasiCoherentDescent.canonicalComparison s t π π hπ
          (sheafOfDifferentials B S hS pX)).hom ≫
        (modulePullback B S hS t).map
          (sheafOfDifferentialsMap B S hS π pX p (𝟙 Y) (by rw [hπp, Category.comp_id])) =
      (modulePullback B S hS s).map
          (sheafOfDifferentialsMap B S hS π pX p (𝟙 Y) (by rw [hπp, Category.comp_id])) ≫
        (sheafOfDifferentialsDescentIsoOfEtale B S hS p hs ht hsq htq).hom
```

## Tag 04CX, a lemma

[Tag 04CX](https://stacks.math.columbia.edu/tag/04CX) in the Stacks Project.

**`AlgebraicGeometry.Space.pushforwardUniversalDerivationHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean#L200). The attribute's comment: “the composite `f_*d_{X'/Y'} ∘ f♯`”.

> **Stacks 04CX.** For a commutative square with top edge `f : X' ⟶ X` and left edge
> `p' : X' ⟶ Y'`, the structure map `f♯ : 𝒪_X ⟶ f_*𝒪_{X'}` followed by the direct image of the
> universal `Y'`-derivation `d_{X'/Y'}`, on underlying sheaves of sets.

```lean
noncomputable def pushforwardUniversalDerivationHom (f : X' ⟶ X) (p' : X' ⟶ Y') :
    CategoryTheory.Sheaf.ringSheaf.{u, u, u + 1} (structureRingSheaf B S hS X) ⟶
      CategoryTheory.Sheaf.moduleSheaf.{u, u, u + 1} (structureRingSheaf B S hS X)
        ((modulePushforward B S hS f).obj (sheafOfDifferentials B S hS p'))
```

**`AlgebraicGeometry.Space.IsSheafOfDifferentialsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean#L212). The attribute's comment: “the characterizing property of `c_f` on universal local sections”.

> **Stacks 04CX**, the characterizing property of the comparison map
> `c_f : f^*Ω_{X/Y} ⟶ Ω_{X'/Y'}` of a commutative square: its adjoint transpose carries the
> universal differential `d_{X/Y}(t)` of a local section `t` of `𝒪_X` to `d_{X'/Y'}(f♯ t)`.

```lean
def IsSheafOfDifferentialsMap (f : X' ⟶ X) (p : X ⟶ Y) (p' : X' ⟶ Y')
    (c : (modulePullback B S hS f).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p') : Prop
```

**`AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentials.lean#L225). The attribute's comment: “uniqueness of the comparison map `c_f`”.

> **Stacks 04CX**, uniqueness: at most one morphism `f^*Ω_{X/Y} ⟶ Ω_{X'/Y'}` of
> `𝒪_{X'}`-modules carries the pulled-back universal differentials to the universal differentials
> of the pulled-back local sections.

```lean
theorem eq_of_isSheafOfDifferentialsMap (f : X' ⟶ X) (p : X ⟶ Y) (p' : X' ⟶ Y')
    {c₁ c₂ : (modulePullback B S hS f).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p'}
    (h₁ : IsSheafOfDifferentialsMap B S hS f p p' c₁)
    (h₂ : IsSheafOfDifferentialsMap B S hS f p p' c₂) : c₁ = c₂
```

**`AlgebraicGeometry.Space.pushforwardUniversalDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean#L501). The attribute's comment: “the composite `f_*d_{X'/Y'} ∘ f♯` is a `Y`-derivation”.

> **Stacks 04CX.**  For a commutative square with top edge `f : X' ⟶ X`, the composite
> `D = f_*d_{X'/Y'} ∘ f♯ : 𝒪_X ⟶ f_*Ω_{X'/Y'}` is a `Y`-derivation of `𝒪_X` with values in the
> direct image of the sheaf of differentials of `p'`.

```lean
noncomputable def pushforwardUniversalDerivation (f : X' ⟶ X) (p : X ⟶ Y) (p' : X' ⟶ Y')
    (q : Y' ⟶ Y) (hcomm : f ≫ p = p' ≫ q) :
    PresheafOfModulesOfCommRing.Derivation'
      ((modulePushforward B S hS f).obj (sheafOfDifferentials B S hS p')).val
      (structureSharpInverseImage B S hS p).hom
```

**`AlgebraicGeometry.Space.sheafOfDifferentialsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean#L530). The attribute's comment: “the existence of the canonical map”.

> **Stacks 04CX.**  The comparison map `c_f : f^*Ω_{X/Y} ⟶ Ω_{X'/Y'}` of a commutative square
> of algebraic spaces: the `Y`-derivation `f_*d_{X'/Y'} ∘ f♯` read through Equation 0619.

```lean
noncomputable def sheafOfDifferentialsMap (f : X' ⟶ X) (p : X ⟶ Y) (p' : X' ⟶ Y') (q : Y' ⟶ Y)
    (hcomm : f ≫ p = p' ≫ q) :
    (modulePullback B S hS f).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p'
```

**`AlgebraicGeometry.Space.isSheafOfDifferentialsMap_sheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsMap.lean#L544). The attribute's comment: “the canonical map has the characterizing property”.

> **Stacks 04CX.**  The comparison map has the characterizing property of Stacks 04CX: its
> adjoint transpose carries the universal differential `d_{X/Y}(t)` of a local section `t` of
> `𝒪_X` to `d_{X'/Y'}(f♯ t)`.
>
> With `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap` this identifies
> `AlgebraicGeometry.Space.sheafOfDifferentialsMap` with any morphism having that property.

```lean
theorem isSheafOfDifferentialsMap_sheafOfDifferentialsMap (f : X' ⟶ X) (p : X ⟶ Y)
    (p' : X' ⟶ Y') (q : Y' ⟶ Y) (hcomm : f ≫ p = p' ≫ q) :
    IsSheafOfDifferentialsMap B S hS f p p'
      (sheafOfDifferentialsMap B S hS f p p' q hcomm)
```

## Tag 05Z7, a lemma

[Tag 05Z7](https://stacks.math.columbia.edu/tag/05Z7) in the Stacks Project.

**`AlgebraicGeometry.Space.isSheafOfDifferentialsMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean#L699). The attribute's comment: “the composite satisfies the characterization of `c_{g ≫ f}`”.

> **Stacks 05Z7**, the characterization: for two stacked commutative squares, the composite
> `c_g ∘ g^*c_f` of the comparison maps of the inner squares, read through the comparison
> `(g ≫ f)^* ≅ g^*f^*` of inverse images of Stacks 03LU, has the characterizing property of
> Stacks 04CX for the outer square.

```lean
theorem isSheafOfDifferentialsMap_comp (f : X' ⟶ X) (g : X'' ⟶ X') (p : X ⟶ Y) (p' : X' ⟶ Y')
    (p'' : X'' ⟶ Y'')
    {cf : (modulePullback B S hS f).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p'}
    {cg : (modulePullback B S hS g).obj (sheafOfDifferentials B S hS p') ⟶
      sheafOfDifferentials B S hS p''}
    (hf : IsSheafOfDifferentialsMap B S hS f p p' cf)
    (hg : IsSheafOfDifferentialsMap B S hS g p' p'' cg) :
    IsSheafOfDifferentialsMap B S hS (g ≫ f) p p''
      ((modulePullbackCompIso B S hS g f).inv.app (sheafOfDifferentials B S hS p) ≫
        (modulePullback B S hS g).map cf ≫ cg)
```

**`AlgebraicGeometry.Space.eq_comp_of_isSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsComp.lean#L723).

> **Stacks 05Z7.**  The comparison maps of Stacks 04CX compose: for two stacked commutative
> squares with top edges `g : X'' ⟶ X'` and `f : X' ⟶ X`, the comparison map of the outer square
> is the comparison map of the inner right square pulled back along `g`, followed by the
> comparison map of the inner left square, the two being composable through the comparison
> `(g ≫ f)^* ≅ g^*f^*` of Stacks 03LU.  Each of the three comparison maps appears through its
> characterizing property of Stacks 04CX, which determines it uniquely.

```lean
theorem eq_comp_of_isSheafOfDifferentialsMap (f : X' ⟶ X) (g : X'' ⟶ X') (p : X ⟶ Y)
    (p' : X' ⟶ Y') (p'' : X'' ⟶ Y'')
    {c : (modulePullback B S hS (g ≫ f)).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p''}
    {cf : (modulePullback B S hS f).obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p'}
    {cg : (modulePullback B S hS g).obj (sheafOfDifferentials B S hS p') ⟶
      sheafOfDifferentials B S hS p''}
    (hc : IsSheafOfDifferentialsMap B S hS (g ≫ f) p p'' c)
    (hf : IsSheafOfDifferentialsMap B S hS f p p' cf)
    (hg : IsSheafOfDifferentialsMap B S hS g p' p'' cg) :
    c = (modulePullbackCompIso B S hS g f).inv.app (sheafOfDifferentials B S hS p) ≫
      (modulePullback B S hS g).map cf ≫ cg
```

## Tag 05Z8, a lemma

[Tag 05Z8](https://stacks.math.columbia.edu/tag/05Z8) in the Stacks Project.

**`AlgebraicGeometry.Space.triangleDifferentials_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsTriangle.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsTriangle.lean#L302). The attribute's comment: “exactness at the right term: the map to Ω\_\{X/Y} is an epimorphism”.

> **Stacks 05Z8**, exactness at the right term of the transitivity sequence
> `f^*Ω_{Y/B} ⟶ Ω_{X/B} ⟶ Ω_{X/Y} ⟶ 0`: the canonical map `Ω_{X/B} ⟶ Ω_{X/Y}` is an epimorphism.
>
> Two morphisms out of `Ω_{X/Y}` agreeing after it agree on every `d_{X/Y}(t)`, because
> `d_{X/B}(t)` is carried to `d_{X/Y}(t)`, so they are equal by the uniqueness half of
> Stacks 04CT.

```lean
theorem triangleDifferentials_epi (f : X ⟶ Y) (g : Y ⟶ Z) :
    Epi (toRelativeDifferentials B S hS f g)
```

**`AlgebraicGeometry.Space.triangleDifferentials_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsTriangle.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsTriangle.lean#L506). The attribute's comment: “the composite of the two maps is zero, and exactness at the middle term Ω\_\{X/B}”.

> **Stacks 05Z8**, the two clauses of the transitivity sequence
> `f^*Ω_{Y/B} ⟶ Ω_{X/B} ⟶ Ω_{X/Y} ⟶ 0` that concern its left half: the composite of the two maps
> is zero, and the resulting short complex is exact at `Ω_{X/B}`.  Together with
> `AlgebraicGeometry.Space.triangleDifferentials_epi`, which is exactness at `Ω_{X/Y}`, this is
> the exactness of the whole sequence.
>
> Both come from `AlgebraicGeometry.Space.isColimitCokernelCoforkToRelativeDifferentials`: the
> cokernel cofork carries the vanishing of the composite, and
> `CategoryTheory.ShortComplex.exact_of_g_is_cokernel` turns the colimit into exactness in the
> middle.  The homology of the short complex is formed in the abelian category of `𝒪_X`-modules;
> the instance that makes it abelian is `HasSheafify` for abelian sheaves on the small étale
> site, which instance search does not find at the projection
> `(AlgebraicGeometry.Space.smallEtaleRingedSite B S hS X.1 X.2).J` of the ringed site, exactly as
> for `AlgebraicGeometry.Space.smallEtaleRingedSite_hasWeakSheafify`.

```lean
theorem triangleDifferentials_exact (f : X ⟶ Y) (g : Y ⟶ Z) :
    ∃ h : pullbackDifferentialsMap B S hS f g ≫ toRelativeDifferentials B S hS f g = 0,
      (ShortComplex.mk _ _ h).Exact
```

## Tag 05Z9, a lemma

[Tag 05Z9](https://stacks.math.columbia.edu/tag/05Z9) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean#L331). The attribute's comment: “the vanishing Ω\_\{X/Y} = 0, from local surjectivity of `f♯`; the gap to the source's hypothesis is that an immersion of algebraic spaces has locally surjective structure map, which is the inverse-image form of the surjectivity clause of 03MB”.

> **Stacks 05Z9**, with local surjectivity of the structure map in place of the hypothesis
> that `f` is an immersion.  If `f♯ : f⁻¹𝒪_Y ⟶ 𝒪_X` is locally surjective then `Ω_{X/Y}` is zero.
>
> `Ω_{X/Y}` corepresents the functor of `Y`-derivations, and by
> `AlgebraicGeometry.Space.derivation_eq_of_isLocallySurjective` that functor takes at most one
> value at each sheaf of `𝒪_X`-modules; so the identity and the zero endomorphism of `Ω_{X/Y}`
> both factor the same derivation and are therefore equal.
>
> An immersion has locally surjective structure map, by
> `AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage_of_isImmersion`, which is
> how `AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isImmersion_unconditional` reaches
> the source's statement.

```lean
theorem isZero_sheafOfDifferentials_of_isLocallySurjective (f : X ⟶ Y)
    (hsharp : Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      (structureSharpInverseImage B S hS f).hom) :
    IsZero (sheafOfDifferentials B S hS f)
```

**`AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean#L360). The attribute's comment: “the source's statement, carrying local surjectivity of the structure map of an immersion (the inverse-image form of the surjectivity clause of 03MB) as `hsharp`, quantified over all immersions of algebraic spaces over `S`”.

> **Stacks 05Z9.**  If `f : X ⟶ Y` is an immersion of algebraic spaces over `S` then
> `Ω_{X/Y}` is zero.
>
> The hypothesis `hsharp` is the one input not proved in this development: the structure map
> `f♯ : f⁻¹𝒪_Y ⟶ 𝒪_X` of an immersion of algebraic spaces is locally surjective.  It is the
> inverse-image form of the surjectivity clause of Stacks 03MB, which
> `AlgebraicGeometry.Space.isLocallySurjective_structureSharp` supplies only in the direct-image
> form `𝒪_Y ⟶ f_*𝒪_X` and only for closed immersions, and it is carried here universally
> quantified over all immersions of algebraic spaces over `S`.
>
> That input is no longer unproved: it is
> `AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage_of_isImmersion` above, so
> the hypothesis-free form of this statement is
> `AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isImmersion_unconditional`.

```lean
theorem isZero_sheafOfDifferentials_of_isImmersion
    (hsharp : ∀ (X' Y' : AlgebraicSpaces B S hS) (g : X' ⟶ Y'), IsImmersion B S hS g.hom →
      Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X'.1)
        (structureSharpInverseImage B S hS g).hom)
    (f : X ⟶ Y) (hf : IsImmersion B S hS f.hom) :
    IsZero (sheafOfDifferentials B S hS f)
```

**`AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isImmersion_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsImmersion.lean#L379). The attribute's comment: “the source's statement: the sheaf of differentials of an immersion of algebraic spaces over `S` is a zero object, with no hypothesis beyond the immersion”.

> **Stacks 05Z9.**  If `f : X ⟶ Y` is an immersion of algebraic spaces over `S` then
> `Ω_{X/Y}` is zero, with no hypothesis beyond the immersion.
>
> The structure map `f♯ : f⁻¹𝒪_Y ⟶ 𝒪_X` of an immersion is locally surjective
> (`AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage_of_isImmersion`), and
> local surjectivity forces the vanishing
> (`AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isLocallySurjective`).  This is
> `AlgebraicGeometry.Space.isZero_sheafOfDifferentials_of_isImmersion` with its hypothesis
> `hsharp` discharged.

```lean
theorem isZero_sheafOfDifferentials_of_isImmersion_unconditional (f : X ⟶ Y)
    (hf : IsImmersion B S hS f.hom) :
    IsZero (sheafOfDifferentials B S hS f)
```

## Tag 05ZA, a lemma

[Tag 05ZA](https://stacks.math.columbia.edu/tag/05ZA) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalSequenceFirstMap_comp_pullbackDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceComplex.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceComplex.lean#L236). The attribute's comment: “the composite of the two arrows is zero, so the sequence `𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}` is a complex, for a closed subspace. Unconditional”.

> **Stacks 05ZA, the composite of the two arrows is zero.**  For a closed subspace `Z` of an
> algebraic space `X` over `Bb`, with inclusion `i : Z ⟶ X`, the sequence
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}
> ```
> is a complex.
>
> This is
> `AlgebraicGeometry.Space.conormalSequenceIdealPullbackMap_comp_pullbackDifferentialsMap` with the
> source of the first arrow read as the conormal module, which it is by
> `AlgebraicGeometry.Space.conormalModule_eq`.

```lean
theorem conormalSequenceFirstMap_comp_pullbackDifferentialsMap
    (Z : ClosedSubspaces B S hS X.1) (b : X ⟶ Bb) :
    conormalSequenceFirstMap B S hS Z b ≫
        pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X Z) b = 0
```

**`AlgebraicGeometry.Space.conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceCompositeZero.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceCompositeZero.lean#L316). The attribute's comment: “the composite of the two arrows is zero, at a subspace inclusion, with the first arrow read out of the conormal module `𝒞_{Z/X}` of 04CN. The same clause at the first arrow of an arbitrary immersion is `conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero`”.

> **Stacks 05ZA, the composite of the two arrows is zero**, read at
> `AlgebraicGeometry.Space.conormalSequenceFirstMap`, that is with the source of the first arrow
> written as the conormal module `𝒞_{Z/X}` of Stacks 04CN rather than as `i^*𝓘`.  The two readings
> are the same morphism, by `AlgebraicGeometry.Space.conormalModule_eq`.
>
> This is the shape in which the clause is consumed: it is the `hzero` hypothesis carried by
> `AlgebraicGeometry.Space.thickeningConormalSequence_exact` of Stacks 060F and by
> `AlgebraicGeometry.Space.epi_thickeningConormalFirstMap` of Stacks 060G.

```lean
theorem conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero
    (Z : ClosedSubspaces B S hS Y.1) (b : Y ⟶ Bb) :
    conormalSequenceFirstMap B S hS Z b ≫
      pullbackDifferentialsMap B S hS (subspaceInclusion B S hS Y Z) b = 0
```

**`AlgebraicGeometry.Space.conormalSequenceIdealDifferential_val_app_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentials.lean, line 690](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentials.lean#L690). The attribute's comment: “the first arrow is induced by `d_{X/B}`: the transpose of the first arrow across `i^* ⊣ i_*` carries a section of the defining ideal sheaf to the universal differential of that section, followed by the unit”.

> **Stacks 05ZA, "the first arrow is induced by `d_{X/B}`".**  The first arrow is by definition
> the transpose across `i^* ⊣ i_*` of
> `AlgebraicGeometry.Space.conormalSequenceIdealDifferential`, and that transpose carries a local
> section `a` of the defining ideal sheaf of `Z` to `D(a)`, where `D` is `d_{X/B}` followed by the
> unit of the adjunction — which is what
> `AlgebraicGeometry.Space.conormalSequenceUnitDerivation` is, by its definition.  This equation is
> the whole of the arrow's dependence on `d_{X/B}`; since the transposition is a bijection, it
> determines the arrow.

```lean
theorem conormalSequenceIdealDifferential_val_app_apply (Z : ClosedSubspaces B S hS X.1)
    (b : X ⟶ Bb) (U : (SmallEtale B S hS X.1)ᵒᵖ)
    (x : (definingIdealSheaf B S hS X Z).toSheafOfModules.val.obj U) :
    ((conormalSequenceIdealDifferential B S hS Z b).val.app U).hom x =
      (conormalSequenceUnitDerivation B S hS Z b).d x.1
```

**`AlgebraicGeometry.Space.conormalSequenceFirstMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentials.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentials.lean#L733). The attribute's comment: “the canonical first arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/B}` induced by `d_{X/B}`, at a subspace inclusion. The same arrow at an arbitrary immersion is `conormalSequenceFirstMapOfImmersion`”.

> **Stacks 05ZA, the canonical first arrow.**  For a subspace `Z` of an algebraic space
> `X` over `B`, with inclusion `i : Z ⟶ X`, the arrow
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/B}
> ```
> induced by `d_{X/B}`.  It is `AlgebraicGeometry.Space.conormalSequenceIdealPullbackMap` with its
> source read as the conormal module, which it is by
> `AlgebraicGeometry.Space.conormalModule_eq`.

```lean
noncomputable def conormalSequenceFirstMap (Z : ClosedSubspaces B S hS X.1) (b : X ⟶ Bb) :
    conormalModule B S hS X Z ⟶
      (modulePullback B S hS (subspaceInclusion B S hS X Z)).obj
        (sheafOfDifferentials B S hS b)
```

**`AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentialsEpi.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceDifferentialsEpi.lean#L113). The attribute's comment: “exactness at the right term: the second arrow `i^*Ω_{X/B} ⟶ Ω_{Z/B}` is an epimorphism, carrying local surjectivity of `i♯ : i⁻¹𝒪_X ⟶ 𝒪_Z` (the inverse-image form of the surjectivity clause of 03MB) as `hsharp`”.

> **Stacks 05ZA, exactness at the right term**, under local surjectivity of the structure map
> `i♯ : i⁻¹𝒪_X ⟶ 𝒪_Z`.  The comparison map `c_i : i^*Ω_{X/B} ⟶ Ω_{Z/B}` of Stacks 04CX is an
> epimorphism, so the conormal sequence of `i` ends in zero.
>
> Left-cancellation is checked directly: given `g, g'` with equal composites,
> `AlgebraicGeometry.Space.sheafOfDifferentialsMap_comp_eq_iff` makes them agree on the universal
> differentials of the sections in the image of `i♯`; local surjectivity makes every local section
> of `𝒪_Z` locally of that form, so the two values agree on a covering sieve and hence are equal,
> the target being a sheaf; and `AlgebraicGeometry.Space.sheafOfDifferentials_hom_ext` turns that
> into `g = g'`.

```lean
theorem epi_pullbackDifferentialsMap_of_isLocallySurjective (i : X ⟶ Y) (b : Y ⟶ Bb)
    (hsharp : Presheaf.IsLocallySurjective (SmallEtale.topology B S hS X.1)
      (structureSharpInverseImage B S hS i).hom) :
    Epi (pullbackDifferentialsMap B S hS i b)
```

**`AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceEpiImmersion.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceEpiImmersion.lean#L71). The attribute's comment: “exactness at the right term: the second arrow `i^*Ω_{X/B} ⟶ Ω_{Z/B}` is an epimorphism for an immersion, with no hypothesis beyond the immersion”.

> **Stacks 05ZA, exactness at the right term, for an immersion.**  For an immersion
> `i : X ⟶ Y` of algebraic spaces over `B` and a structure morphism `b : Y ⟶ B`, the second arrow
> `i^*Ω_{Y/B} ⟶ Ω_{X/B}` of the conormal sequence — the comparison map of Stacks 04CX for the
> square over the identity of `B` — is an epimorphism.
>
> This is `AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_of_isLocallySurjective` with its
> hypothesis `hsharp` discharged by
> `AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage_of_isImmersion`.

```lean
theorem epi_pullbackDifferentialsMap_of_isImmersion (i : X ⟶ Y) (b : Y ⟶ Bb)
    (hi : IsImmersion B S hS i.hom) :
    Epi (pullbackDifferentialsMap B S hS i b)
```

**`AlgebraicGeometry.Space.conormalSequenceFirstMapOfImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionFirstMap.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionFirstMap.lean#L165). The attribute's comment: “the canonical first arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/B}` induced by `d_{X/B}`, for an arbitrary immersion”.

> **Stacks 05ZA, the canonical first arrow, for an arbitrary immersion.**  For an immersion
> `i : Z ⟶ X` of algebraic spaces over `B` with structure morphism `b : X ⟶ B`, the arrow
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/B}
> ```
> induced by `d_{X/B}`.
>
> It is `AlgebraicGeometry.Space.kernelConormalFirstMap`, the arrow built from the kernel ideal
> sheaf of `i` by restricting `d_{X/B}` followed by the unit of `i^* ⊣ i_*` to it, read out of the
> conormal module: `AlgebraicGeometry.Space.conormalAlgebra_piece_one` says the source of that
> arrow *is* the degree-one piece of the conormal algebra of `i`, and
> `AlgebraicGeometry.Space.conormalAlgebraOfImmersionPieceIso` identifies that piece with the
> conormal module of the immersion.

```lean
noncomputable def conormalSequenceFirstMapOfImmersion (i : Z ⟶ X)
    (hi : IsImmersion B S hS i.hom) (b : X ⟶ Bb) :
    immersionConormalModule B S hS i hi ⟶
      (modulePullback B S hS i).obj (sheafOfDifferentials B S hS b)
```

**`AlgebraicGeometry.Space.conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionFirstMap.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionFirstMap.lean#L181). The attribute's comment: “the composite `𝒞_{Z/X} ⟶ i^*Ω_{X/B} ⟶ Ω_{Z/B}` of the two arrows is zero, for an arbitrary immersion”.

> **Stacks 05ZA, the composite of the two arrows is zero, for an arbitrary immersion.**  The
> first arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/B}` followed by the second arrow `i^*Ω_{X/B} ⟶ Ω_{Z/B}`, the
> comparison map of Stacks 04CX for the square over the identity of `B`, is the zero morphism.
>
> The first arrow factors through
> `AlgebraicGeometry.Space.kernelConormalFirstMap`, for which the clause is
> `AlgebraicGeometry.Space.kernelConormalFirstMap_comp_pullbackDifferentialsMap_eq_zero`.

```lean
theorem conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero (i : Z ⟶ X)
    (hi : IsImmersion B S hS i.hom) (b : X ⟶ Bb) :
    conormalSequenceFirstMapOfImmersion B S hS i hi b ≫
      pullbackDifferentialsMap B S hS i b = 0
```

**`AlgebraicGeometry.Space.conormalSequenceOfImmersion_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionKernelExactness.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionKernelExactness.lean#L307). The attribute's comment: “exactness at the middle term `i^*Ω_{X/B}`: the second arrow is a cokernel of the first, for an arbitrary immersion `i : Z ⟶ X`, at the tag's own first arrow `conormalSequenceFirstMapOfImmersion`. Unconditional: the open-subspace reduction of the tag's own proof is carried out, through the factorisation of 04CE and the comparison of the two first arrows across the étale inclusion of the ambient open”.

> **Stacks 05ZA, exactness at the middle term, for an arbitrary immersion.**  For an immersion
> `i : Z ⟶ X` of algebraic spaces over `B` with structure morphism `b : X ⟶ B`, the sequence
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/B} ⟶ Ω_{Z/B}
> ```
> built from the canonical first arrow
> `AlgebraicGeometry.Space.conormalSequenceFirstMapOfImmersion` and the second arrow
> `AlgebraicGeometry.Space.pullbackDifferentialsMap` is exact at `i^*Ω_{X/B}`.
>
> **No hypothesis beyond the immersion is carried.**  It is
> `AlgebraicGeometry.Space.conormalSequenceKernel_exact_of_isImmersion` fed to
> `AlgebraicGeometry.Space.conormalSequenceOfImmersion_exact_of_kernelConormalFirstMap`, which
> reads the first arrow out of the conormal module `𝒞_{Z/X}` of [Stacks Project, Tag 04CN] rather
> than out of the kernel ideal sheaf; the two differ by the isomorphism
> `AlgebraicGeometry.Space.conormalModuleOfImmersionKernelPullbackIso` of the left-hand terms.

```lean
theorem conormalSequenceOfImmersion_exact (i : Z ⟶ X) (hi : IsImmersion B S hS i.hom)
    (b : X ⟶ Bb) :
    (ShortComplex.mk _ _
      (conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero
        B S hS i hi b)).Exact
```

**`AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_subspaceInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceMiddleExactness.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceMiddleExactness.lean#L335). The attribute's comment: “exactness at the right term: the second arrow `i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}` is an epimorphism. UNCONDITIONAL for a closed subspace: the local surjectivity of `i♯ : i⁻¹𝒪_X ⟶ 𝒪_Z` that `epi_pullbackDifferentialsMap_of_isLocallySurjective` carries as `hsharp` is `isLocallySurjective_structureSharpInverseImage`, the inverse-image form of the surjectivity clause of 03MB, applied to the closed immersion `Z.2.2`”.

> **Stacks 05ZA, exactness at the right term, unconditionally for a closed subspace.**  The
> second arrow `i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}` of the sequence of Stacks 05ZA is an epimorphism.
>
> `AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_of_isLocallySurjective` proves this from
> local surjectivity of `i♯ : i⁻¹𝒪_X ⟶ 𝒪_Z`, which that module's implementation notes record as
> *carried*; it is not carried any more, and for a closed immersion it is proved —
> `AlgebraicGeometry.Space.isLocallySurjective_structureSharpInverseImage` of
> `StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionStructureSharpInverseImage.lean`, the
> inverse-image form of the surjectivity clause of Stacks 03MB — and the inclusion of a closed
> subspace is a closed immersion by `Z.2.2`.

```lean
theorem epi_pullbackDifferentialsMap_subspaceInclusion :
    Epi (pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X Z) b)
```

**`AlgebraicGeometry.Space.conormalSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceMiddleExactnessAt.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceMiddleExactnessAt.lean#L492). The attribute's comment: “exactness at the middle term `i^*Ω_{X/B}`: the second arrow is a cokernel of the first, at a subspace inclusion `Z ⊆ X` — the case the tag's own proof reduces the immersion case to. Unconditional: stated at the canonical inclusion and at the registered first arrow `conormalSequenceFirstMap`, with no hypothesis beyond the tag's own data. The general form with the inclusion an explicit parameter is `conormalSequenceAt_exact`, whose three hypotheses this discharges — the two halves of `mem_definingIdealAt_iff` and the closed-immersion clause of 02YU(4); the inclusion is left a parameter there for the reason recorded in `ConormalSequenceInclusionParameter.lean`. The same clause at the first arrow of an arbitrary immersion, over the ambient open of 04CE, is `conormalSequenceOfImmersion_exact`”.

> **Stacks 05ZA, exactness at the middle term, unconditionally.**  For a subspace
> `Z ⊆ X` of an algebraic space over `B` with structure morphism `b : X ⟶ Bb`, the short complex
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/B} ⟶ Ω_{Z/B}
> ```
> built from the canonical first arrow `AlgebraicGeometry.Space.conormalSequenceFirstMap` and the
> second arrow `AlgebraicGeometry.Space.pullbackDifferentialsMap` is exact at `i^*Ω_{X/B}`.
>
> **No hypothesis is carried.**  This is
> `AlgebraicGeometry.Space.conormalSequenceAt_exact_subspaceInclusion`, read with the source of the
> first arrow written as the conormal module `𝒞_{Z/X}` of Stacks 04CN rather than as `i^*𝓘`; the
> two readings are the same morphism, by `AlgebraicGeometry.Space.conormalModule_eq`.
>
> The transport is through `CategoryTheory.ShortComplex.exact_iff_of_iso`, with every component of
> the isomorphism written out, rather than by ascribing the statement directly; the implementation
> notes of this file record what each of the other routes costs.

```lean
theorem conormalSequence_exact (Z : ClosedSubspaces B S hS X.1) (b : X ⟶ Bb) :
    (ShortComplex.mk _ _
      (conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero B S hS Z b)).Exact
```

**`AlgebraicGeometry.Space.exact_conormalSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceThickeningDescent.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceThickeningDescent.lean#L409). The attribute's comment: “exactness at the middle term: the short complex `𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}` is exact at `i^*Ω_{X/Bb}`, for a closed subspace”.

> **Stacks 05ZA, exactness at the middle term, unconditionally for a closed subspace.**  The
> short complex `𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb}` of [Stacks Project, Tag 05ZA] is exact at
> `i^*Ω_{X/Bb}`.
>
> This is
> `AlgebraicGeometry.Space.exact_conormalSequence_of_exists_pushforwardDerivation`, whose
> hypothesis `hdesc` is `AlgebraicGeometry.Space.exists_conormalPushforwardDerivation_eq` above.
> Nothing beyond the inclusion `i` being a closed immersion is used: the one step that used to
> carry a thickening hypothesis, the vanishing of the transpose of a derivation on the sections
> killed by `i^♯` in inverse-image form, is proved for an arbitrary closed subspace in
> `StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceThickeningKernelVanishing.lean` from the
> fibre-square presentation of the defining ideal sheaf.
>
> Together with `AlgebraicGeometry.Space.epi_pullbackDifferentialsMap_subspaceInclusion`, which is
> the clause at the right, this is the whole of 05ZA for the closed immersions this development
> models — the source asserts exactness at `i^*Ω_{X/Bb}` and at `Ω_{Z/Bb}` and nothing on the
> left.

```lean
theorem exact_conormalSequence :
    (ShortComplex.mk _ _
      (conormalSequenceFirstMap_comp_pullbackDifferentialsMap B S hS Z b)).Exact
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.pullbackDifferentialsMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsTriangle.lean#L412), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSecondMap.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSecondMap.lean#L32) (StacksFrontier): “the canonical second arrow `i^*Ω_{X/B} ⟶ Ω_{Z/B}`, the comparison map of 04CX for the square over the identity of the base”.

## Tag 05ZB, a lemma

[Tag 05ZB](https://stacks.math.columbia.edu/tag/05ZB) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_conormalSequenceOfImmersion_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExact.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExact.lean#L216). The attribute's comment: “the global clause at an arbitrary immersion `i : Z ⟶ X` having a left inverse over `B`: the conormal sequence of 05ZA is split exact, that is, it admits a `CategoryTheory.ShortComplex.Splitting`, so its first arrow is a monomorphism, it is exact at the middle term `i^*Ω_{X/B}` and its second arrow is a split epimorphism. Stated at the tag's own first arrow `conormalSequenceFirstMapOfImmersion` out of the conormal module of 04CN, with no hypothesis beyond `IsImmersion` and the tag's own left inverse over `B`. The source's open-subspace reduction is carried out: the immersion is factored through the open subspace of 04CE, where it is closed and the restricted left inverse makes `nonempty_conormalSequenceKernel_splitting` apply, and the splitting is transported back along the comparison of the two sequences across the étale inclusion of that open”.

> **Stacks 05ZB, the global clause, at an arbitrary immersion.**  Let `i : Z ⟶ X` be an
> immersion of algebraic spaces over `Bb` with structure morphism `b : X ⟶ Bb`, and let `g : X ⟶ Z`
> be a left inverse of `i` over `Bb`.  Then the conormal sequence of [Stacks Project, Tag 05ZA]
> ```
>   0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb} ⟶ 0
> ```
> is **split exact**: it admits a `CategoryTheory.ShortComplex.Splitting`, that is a retraction of
> the first arrow and a section of the second summing to the identity — so in particular the first
> arrow is a monomorphism, the sequence is exact at its middle term and the second arrow is a split
> epimorphism.
>
> The sequence is the one the tag states: the first arrow is
> `AlgebraicGeometry.Space.conormalSequenceFirstMapOfImmersion`, whose source is the conormal
> module `𝒞_{Z/X}` of [Stacks Project, Tag 04CN].  Nothing is assumed beyond the immersion and the
> left inverse over `Bb`, which are the tag's own data: the splitting at the kernel-ideal reading is
> `AlgebraicGeometry.Space.nonempty_conormalSequenceKernel_splitting_of_isImmersion`, and the two
> short complexes differ by the isomorphism
> `AlgebraicGeometry.Space.conormalModuleOfImmersionKernelPullbackIso` of their left-hand terms and
> nothing else.

```lean
theorem nonempty_conormalSequenceOfImmersion_splitting (i : Z ⟶ X)
    (hi : IsImmersion B S hS i.hom) (b : X ⟶ Bb) (g : X ⟶ Z) (hg : i ≫ g = 𝟙 Z)
    (hgb : g ≫ i ≫ b = b) :
    Nonempty (ShortComplex.mk _ _
      (conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero
        B S hS i hi b)).Splitting
```

**`AlgebraicGeometry.Space.nonempty_conormalSequenceOfImmersion_splitting_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExact.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExact.lean#L263). The attribute's comment: “the étale-local clause at an arbitrary immersion: for an étale `φ : W' ⟶ W`, an immersion `i' : Zs' ⟶ W'` and an étale `a : Zs' ⟶ Zs` with `i' ≫ φ = a ≫ i`, the immersion `i'` having a left inverse over `B`, the restricted conormal sequence of 05ZA is split exact — it admits a `CategoryTheory.ShortComplex.Splitting`, so its first arrow is a monomorphism, it is exact at the middle term and its second arrow is a split epimorphism — and the inverse image along `a` of the second arrow of the unrestricted sequence is a split epimorphism too, which is where the étale-localization clause of 04CU is consumed. Stated at the tag's own first arrow `conormalSequenceFirstMapOfImmersion`, with `IsImmersion` of `i'` and the étale-local data of the tag the only hypotheses; the unrestricted `i` is an arbitrary morphism”.

> **Stacks 05ZB, the étale-local clause, at an arbitrary immersion.**  Let `i : Zs ⟶ W` be a
> morphism of algebraic spaces over `Bb` with structure morphism `b : W ⟶ Bb`, let `φ : W' ⟶ W` be
> étale, let `i' : Zs' ⟶ W'` be an arbitrary immersion and `a : Zs' ⟶ Zs` étale with
> `i' ≫ φ = a ≫ i`, and let `g' : W' ⟶ Zs'` be a left inverse of `i'` over `Bb`.  Then
>
> * the restricted conormal sequence, the sequence of [Stacks Project, Tag 05ZA] at `i'` over
>   `φ ≫ b`, is split exact;
> * the inverse image along `a` of the second arrow of the unrestricted sequence is a split
>   epimorphism.
>
> Étaleness is assumed of `φ` and of `a` separately rather than `Zs'` being assumed to be the
> preimage of `Zs`, which is weaker: in the situation of the source `a` is a base change of `φ`.
> **The unrestricted morphism `i` is free**: the split epimorphism clause is
> `AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etale`, which assumes nothing
> of `i` or `i'`, and the restricted sequence's splitting is
> `AlgebraicGeometry.Space.nonempty_conormalSequenceOfImmersion_splitting` at `i'`.

```lean
theorem nonempty_conormalSequenceOfImmersion_splitting_of_etale (i : Zs ⟶ W) (b : W ⟶ Bb)
    (φ : W' ⟶ W) (hφ : IsEtale B S hS φ.hom) (i' : Zs' ⟶ W')
    (hi' : IsImmersion B S hS i'.hom) (a : Zs' ⟶ Zs) (ha : IsEtale B S hS a.hom)
    (hsq : i' ≫ φ = a ≫ i) (g' : W' ⟶ Zs') (hg' : i' ≫ g' = 𝟙 Zs')
    (hg'b : g' ≫ i' ≫ φ ≫ b = φ ≫ b) :
    Nonempty (ShortComplex.mk _ _
          (conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero B S hS i'
            hi' (φ ≫ b))).Splitting ∧
      IsSplitEpi ((modulePullback B S hS a).map (pullbackDifferentialsMap B S hS i b))
```

**`AlgebraicGeometry.Space.nonempty_map_conormalSequenceOfImmersion_splitting_of_isEtaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExactEtaleLocal.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceImmersionSplitExactEtaleLocal.lean#L723). The attribute's comment: “the étale-local clause in full: if i étale locally has a left inverse (on an étale covering \{X\_k → X} with Z\_k = Z ×\_X X\_k), the restriction to each Z\_k of the whole conormal sequence of i is split exact”.

> **Stacks 05ZB, the étale-local clause in full.**  Let `i : Z ⟶ X` be an immersion of
> algebraic spaces over `Bb` with structure morphism `b : X ⟶ Bb`, and assume that `i` étale
> locally has a left inverse: there is an étale covering `{φ_k : X_k ⟶ X}` of `X`
> (Stacks 041E: every `φ_k` étale, the family jointly surjective) such that, for each `k`, in a
> cartesian square
> ```
> Z_k --i_k--→ X_k
>  |            |
> a_k          φ_k
>  ↓            ↓
>  Z  ---i---→  X
> ```
> presenting `Z_k` as `Z ×_X X_k`, the immersion `i_k` has a left inverse `g_k` over `Bb`.  Then
> for every `k` the restriction to `Z_k` of the conormal sequence of [Stacks Project, Tag 05ZA]
> of `i` — the image under `a_k^*` of the whole short complex
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb},
> ```
> conormal term and first arrow included — admits a `CategoryTheory.ShortComplex.Splitting`.  So
> the restricted first arrow `a_k^*𝒞_{Z/X} ⟶ a_k^*i^*Ω_{X/Bb}` is a monomorphism, the restricted
> sequence is exact at its middle term, and its second arrow is a split epimorphism.
>
> Each member is
> `AlgebraicGeometry.Space.nonempty_map_conormalSequenceOfImmersion_splitting_of_isPullback`.

```lean
theorem nonempty_map_conormalSequenceOfImmersion_splitting_of_isEtaleCovering (i : Z ⟶ X)
    (hi : IsImmersion B S hS i.hom) (b : X ⟶ Bb) {ι : Type*}
    {Xk Zk : ι → AlgebraicSpaces B S hS} (φ : ∀ k, Xk k ⟶ X)
    (hφ : IsEtaleCovering B S hS (fun k ↦ (Xk k).1) (fun k ↦ (φ k).hom))
    (ik : ∀ k, Zk k ⟶ Xk k) (a : ∀ k, Zk k ⟶ Z) (hpb : ∀ k, IsPullback (ik k) (a k) (φ k) i)
    (g : ∀ k, Xk k ⟶ Zk k) (hg : ∀ k, ik k ≫ g k = 𝟙 (Zk k))
    (hgb : ∀ k, g k ≫ ik k ≫ φ k ≫ b = φ k ≫ b) (k : ι) :
    Nonempty ((ShortComplex.mk _ _
      (conormalSequenceFirstMapOfImmersion_comp_pullbackDifferentialsMap_eq_zero
        B S hS i hi b)).map (modulePullback B S hS (a k))).Splitting
```

**`AlgebraicGeometry.Space.conormalSequence_splitExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitExact.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitExact.lean#L681). The attribute's comment: “the global clause at the inclusion of a bundled subspace `Z ⊆ X` having a left inverse over `B`: the conormal sequence of 05ZA is exact at its middle term `i^*Ω_{X/B}` and its second arrow is a split epimorphism, hence also an epimorphism, which is exactness at the right term; the vanishing of the composite is the short complex itself. Stated at the canonical inclusion and at the registered first arrow `conormalSequenceFirstMap`, with no hypothesis beyond the left inverse, which is the tag's own datum. The injectivity clause at the left end of the sequence is the subject of `nonempty_conormalSequence_splitting_iff_mono`, which shows it equivalent to the full `ShortComplex.Splitting`. The general form with the inclusion an explicit parameter is `conormalSequenceAt_splitExact`, and the same clause at an arbitrary closed immersion, with no bundled subspace anywhere, is `conormalSequenceKernel_splitExact_of_isClosedImmersion`; at the generality the tag is stated at, an arbitrary immersion with a left inverse over `B`, the sequence is split exact in full by `nonempty_conormalSequenceOfImmersion_splitting`”.

> **Stacks 05ZB, the global clause, unconditionally.**  Let `Z ⊆ X` be a closed subspace of an
> algebraic space over `Bb` with structure morphism `b : X ⟶ Bb`, and let `g : X ⟶ Z` be a left
> inverse over `Bb` of the inclusion of `Z`.  Then the conormal sequence of Stacks 05ZA
> ```
>   𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb} ⟶ 0
> ```
> is exact at its middle term and its second arrow is a split epimorphism.
>
> **No hypothesis beyond the left inverse is carried**, and the sequence is the one Stacks 05ZA
> states: the first arrow is `AlgebraicGeometry.Space.conormalSequenceFirstMap`, whose source is the
> conormal module `𝒞_{Z/X}` of Stacks 04CN.  The exactness clause is
> `AlgebraicGeometry.Space.conormalSequence_exact`, which is
> `AlgebraicGeometry.Space.conormalSequenceAt_splitExact`'s first component at the canonical
> inclusion with its three hypotheses discharged — the two halves of
> `AlgebraicGeometry.Space.mem_definingIdealAt_iff` and part (4) of Stacks 02YU — and read at
> `conormalSequenceFirstMap`; the splitness clause is unchanged by that reading, since
> `AlgebraicGeometry.Space.pullbackDifferentialsMap` does not mention the first arrow.
>
> The hypothesis is satisfiable: at the top closed subspace the inclusion is an isomorphism, and its
> inverse is a left inverse over `Bb`; the retraction is written out in the proof of
> `AlgebraicGeometry.Space.isZero_conormalModule_top` of
> `StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/LiftingSheaf.lean`.

```lean
theorem conormalSequence_splitExact (Z : ClosedSubspaces B S hS X.1) (b : X ⟶ Bb)
    (g : X ⟶ (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))
    (hg : subspaceInclusion B S hS X Z ≫ g = 𝟙 (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))
    (hgb : g ≫ subspaceInclusion B S hS X Z ≫ b = b) :
    (ShortComplex.mk _ _
          (conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero B S hS Z b)).Exact ∧
      IsSplitEpi (pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X Z) b)
```

**`AlgebraicGeometry.Space.conormalSequence_splitExact_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitExact.lean, line 756](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitExact.lean#L756). The attribute's comment: “the étale-local clause: for closed subspaces `Z ⊆ X` and `Z' ⊆ X'` joined by an étale `φ : X' ⟶ X` and an étale `a : Z' ⟶ Z` over it, with the inclusion of `Z'` admitting a left inverse over `B`, the restricted conormal sequence of 05ZA is exact at its middle term and its second arrow is a split epimorphism, and so is the inverse image along `a` of the second arrow of the unrestricted sequence — which is where the étale-localization clause of 04CU is consumed. Stated at the two canonical inclusions and at the registered first arrow `conormalSequenceFirstMap`, with no hypothesis beyond the étale-local data of the tag. As in the global clause, the injectivity clause at the left end of the sequence is the subject of `nonempty_conormalSequence_splitting_iff_mono`. The general form with both inclusions explicit parameters is `conormalSequenceAt_splitExact_of_etale`”.

> **Stacks 05ZB, the étale-local clause, unconditionally.**  Let `Z ⊆ X` and `Z' ⊆ X'` be closed
> subspaces, let `φ : X' ⟶ X` be étale, let `a : Z' ⟶ Z` be étale with `i' ≫ φ = a ≫ i` for the two
> inclusions, and let `g' : X' ⟶ Z'` be a left inverse of the inclusion of `Z'` over `Bb`.  Then
>
> * the restricted conormal sequence, the sequence of Stacks 05ZA at `Z' ⊆ X'` over `φ ≫ b`, is
>   exact at its middle term, and its second arrow is a split epimorphism;
> * the inverse image along `a` of the second arrow of the unrestricted sequence is a split
>   epimorphism too.
>
> **No hypothesis beyond the étale-local data of the tag is carried**: `φ`, `a` and the square they
> sit in, and the left inverse `g'`.  The first clause is
> `AlgebraicGeometry.Space.conormalSequence_exact` at `Z' ⊆ X'` over `φ ≫ b`, so it is stated at the
> registered first arrow `AlgebraicGeometry.Space.conormalSequenceFirstMap` with the source read as
> `𝒞_{Z'/X'}`; the other two are the corresponding clauses of
> `AlgebraicGeometry.Space.conormalSequenceAt_splitExact_of_etale`, which do not mention the first
> arrow.  As there, étaleness is assumed of `φ` and of `a` separately rather than `Z'` being assumed
> to be the preimage of `Z`, which is weaker: in the situation of the source `a` is a base change
> of `φ`.

```lean
theorem conormalSequence_splitExact_of_etale (Z : ClosedSubspaces B S hS X.1)
    (Z' : ClosedSubspaces B S hS X'.1) (b : X ⟶ Bb) (φ : X' ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (a : (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))
    (ha : IsEtale B S hS a.hom)
    (hsq : subspaceInclusion B S hS X' Z' ≫ φ = a ≫ subspaceInclusion B S hS X Z)
    (g' : X' ⟶ (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hg' : subspaceInclusion B S hS X' Z' ≫ g' =
      𝟙 (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hg'b : g' ≫ subspaceInclusion B S hS X' Z' ≫ φ ≫ b = φ ≫ b) :
    (ShortComplex.mk _ _
          (conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero B S hS Z'
            (φ ≫ b))).Exact ∧
        IsSplitEpi (pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X' Z')
          (φ ≫ b)) ∧
      IsSplitEpi ((modulePullback B S hS a).map
        (pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X Z) b))
```

**`AlgebraicGeometry.Space.nonempty_conormalSequence_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitMono.lean, line 830](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitMono.lean#L830). The attribute's comment: “the global clause in full at the inclusion of a bundled subspace `Z ⊆ X` of an algebraic space over `B`, that inclusion having a left inverse over `B`: the conormal sequence of 05ZA is split exact, that is, it admits a `CategoryTheory.ShortComplex.Splitting`: the first arrow `conormalSequenceFirstMap` is a monomorphism, the sequence is exact at the middle term `i^*Ω_{X/B}`, and the second arrow is a split epimorphism. Stated at the canonical inclusion and at the registered first arrow, with no hypothesis beyond the tag's own left inverse over `B`. The same clause at an arbitrary closed immersion, with no bundled subspace anywhere, is `nonempty_conormalSequenceKernel_splitting`, and at the generality the tag is stated at, an arbitrary immersion with a left inverse over `B`, it is `nonempty_conormalSequenceOfImmersion_splitting`”.

> **Stacks 05ZB, the global clause in full.**  Let `Z ⊆ X` be a closed subspace of an algebraic
> space over `Bb` with structure morphism `b : X ⟶ Bb`, and let `g : X ⟶ Z` be a left inverse over
> `Bb` of its inclusion.  Then the conormal sequence of Stacks 05ZA
> ```
>   0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Bb} ⟶ Ω_{Z/Bb} ⟶ 0
> ```
> is **split exact**: it admits a `CategoryTheory.ShortComplex.Splitting`, that is a retraction of
> the first arrow and a section of the second summing to the identity — so in particular the first
> arrow is a monomorphism, the sequence is exact at its middle term and the second arrow is a split
> epimorphism.
>
> The exactness and the splitness of the second arrow are
> `AlgebraicGeometry.Space.conormalSequence_splitExact`; what completes the tag is the injectivity
> of the first arrow, `AlgebraicGeometry.Space.mono_conormalSequenceFirstMap`, which
> `AlgebraicGeometry.Space.nonempty_conormalSequence_splitting_iff_mono` turns into the full
> splitting.

```lean
theorem nonempty_conormalSequence_splitting (b : X ⟶ Bb)
    (hgb : g ≫ subspaceInclusion B S hS X Z ≫ b = b) :
    Nonempty (ShortComplex.mk _ _
      (conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero B S hS Z b)).Splitting
```

**`AlgebraicGeometry.Space.nonempty_conormalSequence_splitting_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitMono.lean, line 857](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitMono.lean#L857). The attribute's comment: “the étale-local clause in full: for closed subspaces `Z ⊆ X` and `Z' ⊆ X'` joined by an étale `φ : X' ⟶ X` and an étale `a : Z' ⟶ Z` over it, with the inclusion of `Z'` admitting a left inverse over `B`, the restricted conormal sequence of 05ZA is split exact — it admits a `CategoryTheory.ShortComplex.Splitting`, so its first arrow is a monomorphism, it is exact at the middle term and its second arrow is a split epimorphism — and the inverse image along `a` of the second arrow of the unrestricted sequence is a split epimorphism too, which is where the étale-localization clause of 04CU is consumed. Stated at the two canonical inclusions and at the registered first arrow, with no hypothesis beyond the étale-local data of the tag”.

> **Stacks 05ZB, the étale-local clause in full.**  Let `Z ⊆ X` and `Z' ⊆ X'` be closed
> subspaces, let `φ : X' ⟶ X` be étale, let `a : Z' ⟶ Z` be étale with `i' ≫ φ = a ≫ i` for the two
> inclusions, and let `g' : X' ⟶ Z'` be a left inverse over `Bb` of the inclusion of `Z'`.  Then
>
> * the restricted conormal sequence, the sequence of Stacks 05ZA at `Z' ⊆ X'` over `φ ≫ b`, is
>   split exact;
> * the inverse image along `a` of the second arrow of the unrestricted sequence is a split
>   epimorphism.
>
> As in `AlgebraicGeometry.Space.conormalSequence_splitExact_of_etale`, étaleness is assumed of `φ`
> and of `a` separately rather than `Z'` being assumed to be the preimage of `Z`, which is weaker:
> in the situation of the source `a` is a base change of `φ`.

```lean
theorem nonempty_conormalSequence_splitting_of_etale
    (Z' : ClosedSubspaces B S hS X'.1) (b : X ⟶ Bb) (φ : X' ⟶ X) (hφ : IsEtale B S hS φ.hom)
    (a : (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS) ⟶
      (⟨Z.1.toFunctor, Z.2.1⟩ : AlgebraicSpaces B S hS))
    (ha : IsEtale B S hS a.hom)
    (hsq : subspaceInclusion B S hS X' Z' ≫ φ = a ≫ subspaceInclusion B S hS X Z)
    (g' : X' ⟶ (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hg' : subspaceInclusion B S hS X' Z' ≫ g' =
      𝟙 (⟨Z'.1.toFunctor, Z'.2.1⟩ : AlgebraicSpaces B S hS))
    (hg'b : g' ≫ subspaceInclusion B S hS X' Z' ≫ φ ≫ b = φ ≫ b) :
    Nonempty (ShortComplex.mk _ _
          (conormalSequenceFirstMap_comp_pullbackDifferentialsMap_eq_zero B S hS Z'
            (φ ≫ b))).Splitting ∧
      IsSplitEpi ((modulePullback B S hS a).map
        (pullbackDifferentialsMap B S hS (subspaceInclusion B S hS X Z) b))
```

**`AlgebraicGeometry.Space.isSplitEpi_pullbackDifferentialsMap_of_leftInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean#L325). The attribute's comment: “the global clause: a left inverse of `i` over `B` splits the second arrow of the conormal sequence of 05ZA, so that sequence is split exact”.

> **Stacks 05ZB**, the global clause: a left inverse of `i` over `Bb` makes the second arrow of
> the sequence of Stacks 05ZA a split epimorphism, so that sequence is split exact.
>
> The comparison map of Stacks 04CX at the identity square is carried as the parameters `cid`,
> `hcid` and `[IsIso cid]`; see the implementation notes.

```lean
theorem isSplitEpi_pullbackDifferentialsMap_of_leftInverse (i : Z ⟶ X) (b : X ⟶ Bb) (g : X ⟶ Z)
    (hg : i ≫ g = 𝟙 Z) (hgb : g ≫ i ≫ b = b)
    (cid : (modulePullback B S hS (𝟙 Z)).obj (sheafOfDifferentials B S hS (i ≫ b)) ⟶
      sheafOfDifferentials B S hS (i ≫ b)) [IsIso cid]
    (hcid : IsSheafOfDifferentialsMap B S hS (𝟙 Z) (i ≫ b) (i ≫ b) cid) :
    IsSplitEpi (pullbackDifferentialsMap B S hS i b)
```

**`AlgebraicGeometry.Space.isSplitEpi_pullbackDifferentialsMap_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean#L345). The attribute's comment: “the global clause, unconditionally: a left inverse of `i` over `B` splits the second arrow of the conormal sequence of 05ZA, so that sequence is split exact”.

> **Stacks 05ZB**, the global clause, unconditionally: a left inverse of `i` over `Bb` makes the
> second arrow of the sequence of Stacks 05ZA a split epimorphism, so that sequence is split exact.
>
> This is `AlgebraicGeometry.Space.isSplitEpi_pullbackDifferentialsMap_of_leftInverse` with the
> comparison map of Stacks 04CX at the identity square supplied rather than carried: it is the unit
> law of Stacks 03LU at `Ω_{Z/Bb}`, which is a comparison map by
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_modulePullbackIdIso`, and invertible by
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_id`.  Nothing is assumed beyond the
> left inverse.

```lean
theorem isSplitEpi_pullbackDifferentialsMap_of_retraction (i : Z ⟶ X) (b : X ⟶ Bb) (g : X ⟶ Z)
    (hg : i ≫ g = 𝟙 Z) (hgb : g ≫ i ≫ b = b) :
    IsSplitEpi (pullbackDifferentialsMap B S hS i b)
```

**`AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etaleLeftInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean#L400). The attribute's comment: “the étale-local clause: a left inverse of the restriction of `i` along an étale `φ : X' ⟶ X` splits the inverse image along the induced `a : Z' ⟶ Z` of the second arrow of the conormal sequence of 05ZA”.

> **Stacks 05ZB**, the étale-local clause: if the restriction of `i` along an étale
> `φ : X' ⟶ X` has a left inverse over `Bb`, the inverse image along the induced `a : Z' ⟶ Z` of the
> second arrow of the sequence of Stacks 05ZA is a split epimorphism, so the restricted sequence is
> split exact.
>
> The section is the chosen section of the global clause at `i'`, conjugated by the two invertible
> comparison maps of Stacks 04CU and the composition comparisons of Stacks 03LU.  The comparison
> map at the identity square and the étale-localization clause of Stacks 04CU are carried as
> parameters and instances; see the implementation notes.

```lean
theorem isSplitEpi_map_pullbackDifferentialsMap_of_etaleLeftInverse (i : Z ⟶ X) (b : X ⟶ Bb)
    (φ : X' ⟶ X) (i' : Z' ⟶ X') (a : Z' ⟶ Z) (hsq : i' ≫ φ = a ≫ i) (g' : X' ⟶ Z')
    (hg' : i' ≫ g' = 𝟙 Z') (hg'b : g' ≫ i' ≫ φ ≫ b = φ ≫ b)
    (cid' : (modulePullback B S hS (𝟙 Z')).obj
        (sheafOfDifferentials B S hS (i' ≫ φ ≫ b)) ⟶
      sheafOfDifferentials B S hS (i' ≫ φ ≫ b)) [IsIso cid']
    (hcid' : IsSheafOfDifferentialsMap B S hS (𝟙 Z') (i' ≫ φ ≫ b) (i' ≫ φ ≫ b) cid')
    (ca : (modulePullback B S hS a).obj (sheafOfDifferentials B S hS (i ≫ b)) ⟶
      sheafOfDifferentials B S hS (i' ≫ φ ≫ b)) [IsIso ca]
    (hca : IsSheafOfDifferentialsMap B S hS a (i ≫ b) (i' ≫ φ ≫ b) ca)
    [IsIso (pullbackDifferentialsMap B S hS φ b)] :
    IsSplitEpi ((modulePullback B S hS a).map (pullbackDifferentialsMap B S hS i b))
```

**`AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etaleRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean#L445). The attribute's comment: “the étale-local clause, unconditional in 04CX: a left inverse of the restriction of `i` along an étale `φ : X' ⟶ X` splits the inverse image along the induced `a : Z' ⟶ Z` of the second arrow of the conormal sequence of 05ZA”.

> **Stacks 05ZB**, the étale-local clause, with the comparison map at the identity square no
> longer carried: if the restriction of `i` along an étale `φ : X' ⟶ X` has a left inverse over
> `Bb`, the inverse image along the induced `a : Z' ⟶ Z` of the second arrow of the sequence of
> Stacks 05ZA is a split epimorphism, so the restricted sequence is split exact.
>
> This is `AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etaleLeftInverse` with
> the unit law of Stacks 04CX supplied rather than carried, by
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_modulePullbackIdIso` and
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_id`.  So this clause is unconditional
> in Stacks 04CX.
>
> It still takes the invertibility of the two comparison maps as the instances `[IsIso ca]` and
> `[IsIso (pullbackDifferentialsMap B S hS φ b)]`, which is the conclusion of the
> étale-localization clause of Stacks 04CU at `a` and at `φ`; étaleness of `φ` and of `a` is not
> assumed, so this applies to any square where those two maps are invertible.
> `AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etale` is the form that
> assumes étaleness and discharges the two instances.

```lean
theorem isSplitEpi_map_pullbackDifferentialsMap_of_etaleRetraction (i : Z ⟶ X) (b : X ⟶ Bb)
    (φ : X' ⟶ X) (i' : Z' ⟶ X') (a : Z' ⟶ Z) (hsq : i' ≫ φ = a ≫ i) (g' : X' ⟶ Z')
    (hg' : i' ≫ g' = 𝟙 Z') (hg'b : g' ≫ i' ≫ φ ≫ b = φ ≫ b)
    (ca : (modulePullback B S hS a).obj (sheafOfDifferentials B S hS (i ≫ b)) ⟶
      sheafOfDifferentials B S hS (i' ≫ φ ≫ b)) [IsIso ca]
    (hca : IsSheafOfDifferentialsMap B S hS a (i ≫ b) (i' ≫ φ ≫ b) ca)
    [IsIso (pullbackDifferentialsMap B S hS φ b)] :
    IsSplitEpi ((modulePullback B S hS a).map (pullbackDifferentialsMap B S hS i b))
```

**`AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceSplitting.lean#L473). The attribute's comment: “the étale-local clause, with nothing carried: for étale `φ : X' ⟶ X` and `a`, a left inverse of the restriction of `i` along `φ` splits the inverse image along `a` of the second arrow of the conormal sequence of 05ZA”.

> **Stacks 05ZB**, the étale-local clause, with nothing carried: if `φ : X' ⟶ X` and the
> induced `a : Z' ⟶ Z` are étale and the restriction `i' : Z' ⟶ X'` of `i` along `φ` has a left
> inverse over `Bb`, then the inverse image along `a` of the second arrow of the sequence of
> Stacks 05ZA is a split epimorphism, so the restricted sequence is split exact.
>
> This is `AlgebraicGeometry.Space.isSplitEpi_map_pullbackDifferentialsMap_of_etaleRetraction` with
> the two invertible comparison maps supplied rather than carried: the comparison map of
> Stacks 04CX along an étale morphism, over a fixed base, is invertible by
> `AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_etale`, which is the
> étale-localization clause of Stacks 04CU.  So nothing is assumed here beyond the hypotheses of
> the source: `φ` is étale, `a` — a base change of `φ` in the situation of the source — is étale,
> the square `i' ≫ φ = a ≫ i` commutes, and `i'` has the left inverse `g'` over `Bb`.

```lean
theorem isSplitEpi_map_pullbackDifferentialsMap_of_etale (i : Z ⟶ X) (b : X ⟶ Bb)
    (φ : X' ⟶ X) (hφ : IsEtale B S hS φ.hom) (i' : Z' ⟶ X') (a : Z' ⟶ Z)
    (ha : IsEtale B S hS a.hom) (hsq : i' ≫ φ = a ≫ i) (g' : X' ⟶ Z')
    (hg' : i' ≫ g' = 𝟙 Z') (hg'b : g' ≫ i' ≫ φ ≫ b = φ ≫ b) :
    IsSplitEpi ((modulePullback B S hS a).map (pullbackDifferentialsMap B S hS i b))
```

## Tag 05ZC, a lemma

[Tag 05ZC](https://stacks.math.columbia.edu/tag/05ZC) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_of_isSheafOfDifferentialsMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsBaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsBaseChange.lean#L227). The attribute's comment: “granted, as `hetale`, the étale localization of 04CU: over each étale chart the comparison map is the canonical map 01UV of a cartesian square of schemes. The scheme case 01V0 is applied, not granted”.

> **Stacks 05ZC.**  Let `p : X ⟶ Y` be a morphism of algebraic spaces over `S`, let
> `g : Y' ⟶ Y` be a morphism and let `X'`, with its projections `g' : X' ⟶ X` and `p' : X' ⟶ Y'`,
> be the base change of `p` by `g`.  Then the comparison map
> `c_{g'} : (g')^*Ω_{X/Y} ⟶ Ω_{X'/Y'}` of Stacks 04CX is an isomorphism.
>
> The map is named by the characterizing property of Stacks 04CX, which determines it uniquely by
> `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap`; that uniqueness carries the
> étale-local input from the realization `c₀` it is stated for to the realization `c` in hand.
> The proof is the source's: over an étale chart the comparison map is the canonical map of a
> cartesian square of schemes, which is an isomorphism by Morphisms, Lemma 01V0, and an
> isomorphism on the sections over every chart is an isomorphism.

```lean
theorem isIso_of_isSheafOfDifferentialsMap_of_isPullback (g' : X' ⟶ X) (p' : X' ⟶ Y')
    (p : X ⟶ Y) (g : Y' ⟶ Y) (h : IsPullback g' p' p g)
    (c c₀ : (modulePullback B S hS g').obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p')
    (hc : IsSheafOfDifferentialsMap B S hS g' p p' c)
    (hc₀ : IsSheafOfDifferentialsMap B S hS g' p p' c₀)
    (hetale : IsEtaleLocalBaseChangeMap B S hS g' p' p g h c₀) :
    IsIso c
```

**`AlgebraicGeometry.Space.isIso_sheafOfDifferentialsMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeSquareBijective.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeSquareBijective.lean#L459). The attribute's comment: “the map of 04CX for the base change of X along g is an isomorphism, with the base change presented as a cartesian square and the map by the property characterizing it. The étale localization of 04CU and the scheme case 01V0 are both applied as proved”.

> **Stacks 05ZC.**  Let `X ⟶ Y` be a morphism of algebraic spaces over `S` and let
> `g : Y' ⟶ Y` be a morphism of algebraic spaces over `S`.  Let `X' = X_{Y'}` be the base change
> of `X` and let `g' : X' ⟶ X` be the projection.  Then the map
> `(g')^*Ω_{X/Y} ⟶ Ω_{X'/Y'}` of Stacks 04CX is an isomorphism.
>
> The base change is presented as a cartesian square `IsPullback g' p' p g` of algebraic spaces,
> and the map of Stacks 04CX by the property `AlgebraicGeometry.Space.IsSheafOfDifferentialsMap`
> that characterizes it — existence is
> `AlgebraicGeometry.Space.isSheafOfDifferentialsMap_sheafOfDifferentialsMap` and uniqueness
> `AlgebraicGeometry.Space.eq_of_isSheafOfDifferentialsMap`, so naming the map this way asserts
> nothing beyond the square.
>
> The proof is the source's own: the case of a square of schemes, Morphisms, Lemma 01V0, together
> with the étale localization of Stacks 04CU.  The scheme case enters as
> `AlgebraicGeometry.Scheme.Hom.bijective_restrictRelativeDerivation_of_isPullback` through
> `AlgebraicGeometry.Space.schemeSquareDerivationRestriction`.

```lean
theorem isIso_sheafOfDifferentialsMap_of_isPullback (g' : X' ⟶ X) (p' : X' ⟶ Y') (p : X ⟶ Y)
    (g : Y' ⟶ Y) (h : IsPullback g' p' p g)
    {c : (modulePullback B S hS g').obj (sheafOfDifferentials B S hS p) ⟶
      sheafOfDifferentials B S hS p'}
    (hc : IsSheafOfDifferentialsMap B S hS g' p p' c) : IsIso c
```

## Tag 05ZD, a lemma

[Tag 05ZD](https://stacks.math.columbia.edu/tag/05ZD) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_biprodDesc_of_isSheafOfDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsBaseChange.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsBaseChange.lean#L257). The attribute's comment: “granted, as `hetale`, the étale localization of 04CU: over each étale chart the map `p^*Ω_{X/T} ⊕ q^*Ω_{Y/T} ⟶ Ω_{W/T}` is the map 01V1 of a cartesian square of schemes. The scheme case 01V1 is applied, not granted”.

> **Stacks 05ZD.**  Let `f : X ⟶ T` and `g : Y ⟶ T` be morphisms of algebraic spaces over `S`
> with the same target and let `p : W ⟶ X`, `q : W ⟶ Y` be the projections of a fibre product of
> `f` and `g`.  The two comparison maps of Stacks 04CX exhibit `Ω_{W/T}` as the direct sum
> `p^*Ω_{X/T} ⊕ q^*Ω_{Y/T}`.
>
> Both summands are named by the characterizing property of Stacks 04CX for the square they come
> from — the one with top edge `p` and right edge `f`, and the one with top edge `q` and right
> edge `g`, both with left edge the structure morphism `p ≫ f` of `W` — so the conclusion is
> about the two comparison maps and not about some decomposition of `Ω_{W/T}`.  As for
> Stacks 05ZC the étale localization of Stacks 04CU is granted and Morphisms, Lemma 01V1 is
> applied.

```lean
theorem isIso_biprodDesc_of_isSheafOfDifferentialsMap {W T : AlgebraicSpaces B S hS}
    (p : W ⟶ X) (q : W ⟶ Y) (f : X ⟶ T) (g : Y ⟶ T) (h : IsPullback p q f g)
    (a a₀ : (modulePullback B S hS p).obj (sheafOfDifferentials B S hS f) ⟶
      sheafOfDifferentials B S hS (p ≫ f))
    (b b₀ : (modulePullback B S hS q).obj (sheafOfDifferentials B S hS g) ⟶
      sheafOfDifferentials B S hS (p ≫ f))
    (ha : IsSheafOfDifferentialsMap B S hS p f (p ≫ f) a)
    (ha₀ : IsSheafOfDifferentialsMap B S hS p f (p ≫ f) a₀)
    (hb : IsSheafOfDifferentialsMap B S hS q g (p ≫ f) b)
    (hb₀ : IsSheafOfDifferentialsMap B S hS q g (p ≫ f) b₀)
    (hetale : IsEtaleLocalFibreProductMap B S hS p q f g h (biprod.desc a₀ b₀)) :
    IsIso (biprod.desc a b)
```

**`AlgebraicGeometry.Space.isIso_biprodDesc_sheafOfDifferentialsMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeSquareBijective.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeSquareBijective.lean#L484). The attribute's comment: “the two maps of 04CX out of p^*Omega\_\{X/T} and q^*Omega\_\{Y/T} give an isomorphism onto Omega\_\{X x\_T Y/T}, with the fibre product presented as a cartesian square and each summand by the property characterizing it. The étale localization of 04CU and the scheme case 01V1 are both applied as proved”.

> **Stacks 05ZD.**  Let `f : X ⟶ T` and `g : Y ⟶ T` be morphisms of algebraic spaces over `S`
> with the same target and let `p : W ⟶ X`, `q : W ⟶ Y` be the projections of the fibre product
> `W = X ×_T Y`.  Then the maps of Stacks 04CX give an isomorphism
> `p^*Ω_{X/T} ⊕ q^*Ω_{Y/T} ⟶ Ω_{W/T}`.
>
> The fibre product is presented as a cartesian square `IsPullback p q f g` and the two summands
> by the property `AlgebraicGeometry.Space.IsSheafOfDifferentialsMap` that characterizes the map
> of Stacks 04CX for the square they come from, so the conclusion is about those two maps and not
> about some decomposition of `Ω_{W/T}`.
>
> The proof is the source's own: the case of schemes, Morphisms, Lemma 01V1, together with the
> étale localization of Stacks 04CU, the scheme case entering through
> `AlgebraicGeometry.Space.schemeSquareDerivationRestriction`.

```lean
theorem isIso_biprodDesc_sheafOfDifferentialsMap_of_isPullback {W T : AlgebraicSpaces B S hS}
    (p : W ⟶ X) (q : W ⟶ Y) (f : X ⟶ T) (g : Y ⟶ T) (h : IsPullback p q f g)
    (a : (modulePullback B S hS p).obj (sheafOfDifferentials B S hS f) ⟶
      sheafOfDifferentials B S hS (p ≫ f))
    (b : (modulePullback B S hS q).obj (sheafOfDifferentials B S hS g) ⟶
      sheafOfDifferentials B S hS (p ≫ f))
    (ha : IsSheafOfDifferentialsMap B S hS p f (p ≫ f) a)
    (hb : IsSheafOfDifferentialsMap B S hS q g (p ≫ f) b) :
    IsIso (biprod.desc a b)
```

## Tag 05ZE, a lemma

[Tag 05ZE](https://stacks.math.columbia.edu/tag/05ZE) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean#L652). The attribute's comment: “finite type of Ω\_\{X/Y}, from étale-local finite generation of 𝒪\_X over f⁻¹𝒪\_Y and unramifiedness of the transition maps of the small étale site; the gap to the source's hypothesis is the bridge from 03XF(1) to the algebra statement, and 00UU for the sections of an arrow of the small étale site”.

> **Stacks 05ZE**, with the two carried hypotheses in place of "`f` is locally of finite
> type".  If `𝒪_X` is étale-locally generated as an `f⁻¹𝒪_Y`-algebra by finitely many sections and
> the transition maps of the small étale site of `X` are unramified, then `Ω_{X/Y}` is a finite
> type `𝒪_X`-module.
>
> The covering of each object is the one `hft` supplies, presented as the family of all its arrows
> indexed by their sources, and on each member the finitely many generators are
> `AlgebraicGeometry.Space.hasFiniteGlobalGenerators_sheafOfDifferentials_over`.

```lean
theorem isFiniteTypeOnSite_sheafOfDifferentials (f : X ⟶ Y)
    (hunram : HasUnramifiedChartTransitions B S hS X)
    (hft : HasFiniteTypeChartAlgebras B S hS f) :
    (sheafOfDifferentials B S hS f).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean#L676). The attribute's comment: “the source's statement, carrying the bridge from 03XF(1) to étale-local finite generation of 𝒪\_X over f⁻¹𝒪\_Y as `hft` and unramifiedness of the transition maps of a small étale site (00UU) as `hunram`, both quantified over all algebraic spaces over `S`”.

> **Stacks 05ZE.**  If `f : X ⟶ Y` is a morphism of algebraic spaces over `S` which is locally
> of finite type, then `Ω_{X/Y}` is a finite type `𝒪_X`-module.
>
> The two inputs not proved in this development are carried universally quantified: the bridge
> from `AlgebraicGeometry.Space.IsLocallyOfFiniteType` (Stacks 03XF(1), defined through étale
> scheme charts) to the statement that `𝒪_X` is étale-locally a finite type `f⁻¹𝒪_Y`-algebra, and
> the unramifiedness of the transition maps of a small étale site, which is Algebra, Lemma 00UU
> for the ring map of sections of an arrow of that site.

```lean
theorem isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType
    (hunram : ∀ X' : AlgebraicSpaces B S hS, HasUnramifiedChartTransitions B S hS X')
    (hft : ∀ (X' Y' : AlgebraicSpaces B S hS) (g : X' ⟶ Y'),
      IsLocallyOfFiniteType B S hS g.hom → HasFiniteTypeChartAlgebras B S hS g)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    (sheafOfDifferentials B S hS f).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_affineChartAlgebras`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean, line 796](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteType.lean#L796). The attribute's comment: “finite type of Ω\_\{X/Y} from étale-local finite generation of 𝒪\_X over f⁻¹𝒪\_Y on a covering by affine charts, which is what 03XF(1) delivers; unramifiedness of the transition maps of the small étale site (00UU) is proved, not assumed. The source's own hypothesis is taken in `isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_unconditional`”.

> **Finite type of `Ω_{X/Y}` from the étale-local finite generation of `𝒪_X` over `f⁻¹𝒪_Y`.**
> If every object of the small étale site of `X` has a covering by affine charts over which `𝒪_X`
> is generated as an `f⁻¹𝒪_Y`-algebra by finitely many sections, then `Ω_{X/Y}` is a finite type
> `𝒪_X`-module.
>
> The covering of each object is the one `hft` supplies, and on each of its members the finitely
> many generators are
> `AlgebraicGeometry.Space.hasFiniteGlobalGenerators_sheafOfDifferentials_over_of_isAffine`.
> Unramifiedness of the transition maps — Algebra, Lemma 00UU — is *proved*, not assumed:
> affineness of the members is what makes
> `AlgebraicGeometry.Space.subsingleton_kaehlerDifferential_chartRing_of_affineChart` apply.
>
> This is the engine of Stacks 05ZE with no unramifiedness hypothesis; at the source's own
> hypothesis `AlgebraicGeometry.Space.IsLocallyOfFiniteType`, and with nothing else assumed, the
> statement is
> `AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_unconditional`,
> in `StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteTypeChartBridge.lean`.

```lean
theorem isFiniteTypeOnSite_sheafOfDifferentials_of_affineChartAlgebras (f : X ⟶ Y)
    (hft : HasFiniteTypeAffineChartAlgebras B S hS f) :
    (sheafOfDifferentials B S hS f).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteTypeChartBridge.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteTypeChartBridge.lean#L268). The attribute's comment: “Ω\_\{X/Y} is a finite type 𝒪\_X-module for f locally of finite type, with no further hypothesis”.

> **Stacks 05ZE.**  If `f : X ⟶ Y` is a morphism of algebraic spaces over `S` which is locally
> of finite type, then `Ω_{X/Y}` is a finite type `𝒪_X`-module.
>
> The chart-algebra condition of
> `AlgebraicGeometry.Space.hasFiniteTypeAffineChartAlgebras_of_isLocallyOfFiniteType` feeds
> `AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_affineChartAlgebras`, which
> generates `Ω_{X/Y}` over each member of the covering by the universal differentials of the
> generators. Algebra, Lemma 00UU for the transition maps of the small étale site is proved there,
> not assumed.

```lean
theorem isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_unconditional
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    (sheafOfDifferentials B S hS f).IsFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteTypeEtaleChart.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFiniteTypeEtaleChart.lean#L107).

> **Stacks 05ZE.** If `f : X ⟶ Y` is a morphism of algebraic spaces over `S` which is locally
> of finite type, then the sheaf of differentials `Ω_{X/Y}` is an `𝒪_X`-module of finite type.
>
> The proof is the source's. An atlas `q : V ⟶ Y` lifts, by Stacks 02X1, to a surjective étale
> chart `p : U ⟶ X` and a morphism `α : U ⟶ V` of schemes over `q`; `α` is locally of finite type
> because `f` is. The pullback of `Ω_{X/Y}` to `U` is the sheaf of differentials of `α`
> (Stacks 04CU), which is the small-étale module associated to `Ω_{U/V}`; that is of finite type by
> Stacks 01V2 and Stacks 08HD, and finite type descends from the surjective chart.

```lean
theorem isFiniteTypeOnSite_sheafOfDifferentials_of_isLocallyOfFiniteType_hom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f.hom) :
    (sheafOfDifferentials B S hS f).IsFiniteTypeOnSite
```

## Tag 05ZF, a lemma

[Tag 05ZF](https://stacks.math.columbia.edu/tag/05ZF) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean#L519). The attribute's comment: “finite presentation of Ω\_\{X/Y}. ASSUMED, not proved: the relations half of Descent, Proposition 03DX(2), as the last clause of `hfp` — that the relations among the universal differentials of a finite generating family are étale-locally finitely generated. Also assumed: the bridge from 03XP(1) to étale-local finite generation of 𝒪\_X over f⁻¹𝒪\_Y (first clause of `hfp`), and unramifiedness of the transition maps of the small étale site (`hunram`, 00UU), which `hasUnramifiedChartTransitions_of_forall_isAffine` discharges when every étale chart is affine. PROVED here: the generators half and the assembly into 03DL(7)”.

> **Stacks 05ZF**, with the two carried hypotheses in place of "`f` is locally of finite
> presentation".  If `𝒪_X` is étale-locally generated as an `f⁻¹𝒪_Y`-algebra by finitely many
> sections whose universal differentials have étale-locally finitely generated relations, and the
> transition maps of the small étale site of `X` are unramified, then `Ω_{X/Y}` is an
> `𝒪_X`-module of finite presentation.
>
> The covering of each object is the one `hfp` supplies, presented as the family of all its
> arrows indexed by their sources, and on each member the finite presentation is
> `AlgebraicGeometry.Space.hasFiniteGlobalPresentation_sheafOfDifferentials_over`.

```lean
theorem isFinitePresentationOnSite_sheafOfDifferentials (f : X ⟶ Y)
    (hunram : HasUnramifiedChartTransitions B S hS X)
    (hfp : HasFinitePresentationChartData B S hS f) :
    (sheafOfDifferentials B S hS f).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean#L548). The attribute's comment: “the source's statement. ASSUMED, not proved: the relations half of Descent, Proposition 03DX(2), inside `hfp`; the bridge from 03XP(1) to étale-local finite presentation data for 𝒪\_X over f⁻¹𝒪\_Y, also inside `hfp`; and unramifiedness of the transition maps of a small étale site (`hunram`, 00UU), discharged by `hasUnramifiedChartTransitions_of_forall_isAffine` when every étale chart is affine. Both inputs are quantified over all algebraic spaces over `S`”.

> **Stacks 05ZF.**  If `f : X ⟶ Y` is a morphism of algebraic spaces over `S` which is
> locally of finite presentation, then `Ω_{X/Y}` is an `𝒪_X`-module of finite presentation.
>
> The two inputs not proved in this development are carried universally quantified: the bridge
> from `AlgebraicGeometry.Space.IsLocallyOfFinitePresentation` (Stacks 03XP(1), defined through
> étale scheme charts) to the étale-local finite presentation data of
> `AlgebraicGeometry.Space.HasFinitePresentationChartData`, and the unramifiedness of the
> transition maps of a small étale site, which is Algebra, Lemma 00UU for the ring map of
> sections of an arrow of that site.

```lean
theorem isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation
    (hunram : ∀ X' : AlgebraicSpaces B S hS, HasUnramifiedChartTransitions B S hS X')
    (hfp : ∀ (X' Y' : AlgebraicSpaces B S hS) (g : X' ⟶ Y'),
      IsLocallyOfFinitePresentation B S hS g.hom → HasFinitePresentationChartData B S hS g)
    (f : X ⟶ Y) (hf : IsLocallyOfFinitePresentation B S hS f.hom) :
    (sheafOfDifferentials B S hS f).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_sheafOfDifferentials_of_chartData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean, line 736](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean#L736). The attribute's comment: “finite presentation of Ω\_\{X/Y} from étale-local finite presentation data for 𝒪\_X over f⁻¹𝒪\_Y; unramifiedness of the transition maps of the small étale site (00UU) is proved, not assumed. The source's own hypothesis is taken in `isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation_unconditional`”.

> **Finite presentation of `Ω_{X/Y}` from étale-local presentation data for `𝒪_X` over
> `f⁻¹𝒪_Y`.**  If `𝒪_X` is étale-locally generated as an `f⁻¹𝒪_Y`-algebra by finitely many sections
> whose universal differentials have étale-locally finitely generated relations, then `Ω_{X/Y}` is
> an `𝒪_X`-module of finite presentation.
>
> The covering of each object is the one `hfp` supplies, refined to its members with affine
> underlying scheme
> (`AlgebraicGeometry.Space.SmallEtale.ofArrows_affineMember_mem_topology`), and on each such
> member the finite presentation is
> `AlgebraicGeometry.Space.hasFiniteGlobalPresentation_sheafOfDifferentials_over`.  Refining to
> affine members is what makes Algebra, Lemma 00UU applicable: the only transition maps the proof
> differentiates are arrows between affine charts.
>
> The tag itself is
> `AlgebraicGeometry.Space.isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation`
> below, which takes the source's hypothesis on `f`; this is the sectionwise route to the same
> conclusion, kept because it reads the presentation off the construction of `Ω_{X/Y}` as a
> sheafification rather than off the scheme case.

```lean
theorem isFinitePresentationOnSite_sheafOfDifferentials_of_chartData (f : X ⟶ Y)
    (hfp : HasFinitePresentationChartData B S hS f) :
    (sheafOfDifferentials B S hS f).IsFinitePresentationOnSite
```

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsFinitePresentation.lean#L768). The attribute's comment: “finite presentation of Ω\_\{X/Y} for a morphism of algebraic spaces locally of finite presentation”. References: SGA 3 III (0.14), “more general”; SGA 7 VI (5.1), “partial”.

> **Stacks 05ZF.**  If `f : X ⟶ Y` is a morphism of algebraic spaces over `S` which is locally
> of finite presentation, then `Ω_{X/Y}` is an `𝒪_X`-module of finite presentation.
>
> The proof is the source's, and it is the finite-presentation refinement of the proof of
> Stacks 04CV in `StacksFrontier.AlgebraicGeometry.Spaces.SheafOfDifferentialsQuasicoherent`.  An
> atlas `q : V ⟶ Y` of the target lifts, by Stacks 02X1, to a surjective étale chart `p : U ⟶ X`
> of the source together with a morphism `α : U ⟶ V` of schemes of the site making the square
> commute.  Being locally of finite presentation is a condition on exactly such squares, so `α` is
> a morphism of schemes locally of finite presentation and its Zariski sheaf of relative
> differentials is of finite presentation by Morphisms, Lemma 01V3.  The identification of
> Stacks 04CU reads the pullback of `Ω_{X/Y}` along `p` as the sheaf of differentials of `α`, which
> the final sentence of Stacks 04CU — Stacks 04CS, in the form
> `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeComparison` — identifies with the small-étale
> module associated to that Zariski sheaf; the associated module of a module of finite presentation
> is of finite presentation by
> `AlgebraicGeometry.Space.isFinitePresentationOnSite_representedAssociatedModule`.  Finally
> finite presentation descends from a surjective étale chart by
> `AlgebraicGeometry.Space.isFinitePresentationOnSite_iff_exists_etale_surjective`, the pullback of
> modules and étale restriction being matched by Equation 03LW.

```lean
theorem isFinitePresentationOnSite_sheafOfDifferentials_of_isLocallyOfFinitePresentation_unconditional
    (f : X ⟶ Y) (hf : IsLocallyOfFinitePresentation B S hS f.hom) :
    (sheafOfDifferentials B S hS f).IsFinitePresentationOnSite
```

## Tag 0CK5, a lemma

[Tag 0CK5](https://stacks.math.columbia.edu/tag/0CK5) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_sheafOfDifferentials_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSiteTransport.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSiteTransport.lean#L97). The attribute's comment: “the unconditional form, with the 04CS site transport of finite local freeness discharged by `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeSiteComparison`; smoothness of `f` is the only thing this asks”.

> **Stacks 0CK5, asking nothing beyond smoothness.** The sheaf of differentials `Ω_{X/Y}` of a
> smooth morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` is finite locally free on the
> small étale site of `X`.
>
> This is `AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_sheafOfDifferentials`, the reduction
> of Stacks 0CK5 to Stacks 02G1, applied to
> `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeSiteComparison`, which proves the comparison
> of Stacks 04CS that the reduction takes as its argument `hsite`.  The mathematics is that of the
> reduction; only the argument is supplied.

```lean
theorem isFiniteLocallyFreeOnSite_sheafOfDifferentials_of_isSmooth
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsSmooth B S hS f.hom) :
    SheafOfModules.IsFiniteLocallyFreeOnSite (sheafOfDifferentials B S hS f)
```

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOnSite_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSmoothFiniteLocallyFree.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSmoothFiniteLocallyFree.lean#L199). The attribute's comment: “granted as `hsite` the comparison of 04CS transporting finite local freeness of the differentials of a morphism of schemes of the site from its small Zariski site to its small étale site. The identification Ω\_\{X/Y}|\_\{U\_étale} ≅ Ω\_\{U/V} of 04CU over a commuting square of étale charts is not granted: it is proved here”.

> **Stacks 0CK5.** The sheaf of differentials `Ω_{X/Y}` of a smooth morphism `f : X ⟶ Y` of
> algebraic spaces over a scheme `S` is finite locally free on the small étale site of `X`,
> granted the comparison `AlgebraicGeometry.Space.SheafOfDifferentialsSchemeSiteComparison`.
>
> An atlas of the target lifts along `f`, by Stacks 02X1, to a commuting square of étale charts
> whose chart of the source is surjective on points.  Smoothness of `f` is the every-chart
> condition of Stacks 03ZC(1), so the square's scheme morphism `ψ` is smooth; Stacks 02G1 makes
> `Ω_{U/V}` finite locally free in the local-generators form of Stacks 01C6(2), and
> `Stacks.SheafOfModules.isFiniteLocallyFreeOnSite_of_isFiniteLocallyFree` rewrites that in the
> covering-family form of Stacks 03DL(2).  The hypothesis carries it to the small étale site,
> Stacks 04CU — `AlgebraicGeometry.Space.sheafOfDifferentialsEtaleChartComparison`, which is proved
> and no longer assumed — to the restriction of `Ω_{X/Y}` to the chart, and the clause of
> Stacks 03DN along an étale morphism of algebraic spaces descends it from that surjective chart
> to `X`.

```lean
theorem isFiniteLocallyFreeOnSite_sheafOfDifferentials {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsSmooth B S hS f.hom)
    (hsite : SheafOfDifferentialsSchemeSiteComparison B S hS) :
    SheafOfModules.IsFiniteLocallyFreeOnSite (sheafOfDifferentials B S hS f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.7, Tag 04CR](https://stacks.math.columbia.edu/tag/04CR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
