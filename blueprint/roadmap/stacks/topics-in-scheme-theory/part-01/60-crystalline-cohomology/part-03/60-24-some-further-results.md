---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.computes07MK, Crystalline.GlobalCrystallineSituation.pullbackToClosedFiber, Crystalline.GlobalCrystallineSituation.pullbackSituation, Crystalline.GlobalCrystallineSituation.isOpenImmersion_pullbackSituationToX, Crystalline.GlobalCrystallineSituation.range_pullbackSituationToX, Crystalline.GlobalCrystallineSituation.pullbackCrisMorphism, Crystalline.GlobalCrystallineSituation.pullbackStructureToposMorphism, Crystalline.GlobalCrystallineSituation.pullbackSheaf
statement: formalized
proof: formalized
---

# 60.24 Some further results

Section 60.24 of the Stacks Project, [Tag 07MI](https://stacks.math.columbia.edu/tag/07MI). 5 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07MJ, a remark

[Tag 07MJ](https://stacks.math.columbia.edu/tag/07MJ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.computes07MK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Formula07MKProof.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/Formula07MKProof.lean#L521). The attribute's comment: “the displayed equation (07MK): (Rf\_\{cris,*}F)\_\{T'} ≅ R(T ⟶ T')\_*(Rτ\_\{U/T,*}F\_U) in D⁺(Ab(T'\_Zar)) for every object (U', T', δ') of Cris(X'/S'), naturally in F; stated for every abelian sheaf F on Cris(X/S), so in particular for the abelian sheaf underlying an O\_\{X/S}-module”.

> **Stacks Project, Tag 07MJ, the displayed equation (07MK).**  For every object
> `(U', T', δ')` of `Cris(X'/S')`, with `U = X ×_{X'} U'` and `T = S ×_{S'} T'`,
>
> `(Rf_{cris, *}F)_{T'} ≅ R(T ⟶ T')_*(Rτ_{U/T, *}F_U)`
>
> in `D⁺(Ab(T'_Zar))`, naturally in the abelian sheaf `F` on `Cris(X/S)`.

```lean
theorem computes07MK
    [HasDerivedCategory.{u + 2} (Sheaf (smallTopology S) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{u + 2} (Sheaf (smallTopology S') AddCommGrpCat.{u + 1})] :
    Computes07MK S S' fS fX hf
```

**`Crystalline.GlobalCrystallineSituation.pullbackToClosedFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L187). The attribute's comment: “the induced morphism U ⟶ T₀, for T = S ×\_\{S'} T' and U = X ×\_\{X'} U'”.

> **Stacks Project, Tag 07MJ.**  The induced morphism `U ⟶ T₀` of the remark: the closed fibre
> of `T = S ×_{S'} T'` is `S₀ ×_{S'₀} T'₀` by [Stacks, Tag 07ME], and `U = X ×_{X'} U'` maps to `S₀`
> through `X` and to `T'₀ = U'` through `U'`.

```lean
def pullbackToClosedFiber : pullbackSource S S' fX A' ⟶ closedFiber (pullbackBase S S' fS A')
```

**`Crystalline.GlobalCrystallineSituation.pullbackSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L219). The attribute's comment: “the crystalline situation U/T attached to an object (U', T', δ') of Cris(X'/S')”.

> **Stacks Project, Tag 07MJ.**  The crystalline situation `U/T` of the remark attached to an
> object `(U', T', δ')` of `Cris(X'/S')`: the divided power base is the fibre product
> `T = S ×_{S'} T'` of [Stacks, Tag 07ME], the scheme is `U = X ×_{X'} U'`, and the structure
> morphism to `T₀` is `pullbackToClosedFiber`.  The prime `p` is locally nilpotent on `U` because it
> is on `X` and `U ⟶ X` induces maps on local rings.

```lean
def pullbackSituation : GlobalCrystallineSituation.{u}
```

**`Crystalline.GlobalCrystallineSituation.isOpenImmersion_pullbackSituationToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L262). The attribute's comment: “U = X ×\_\{X'} U' is an open subscheme of X”.

> **Stacks Project, Tag 07MJ.**  `U = X ×_{X'} U'` is an open subscheme of `X`, the morphism
> `U' ⟶ X'` of an object of the small crystalline site being an open immersion.

```lean
theorem isOpenImmersion_pullbackSituationToX :
    IsOpenImmersion (pullback.fst fX A'.obj.toX)
```

**`Crystalline.GlobalCrystallineSituation.range_pullbackSituationToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L270). The attribute's comment: “U = X ×\_\{X'} U' is f⁻¹(U')”.

> **Stacks Project, Tag 07MJ.**  The open subscheme `U = X ×_{X'} U'` of `X` is `f⁻¹(U')`: its
> image in `X` is the preimage under `f` of the image of `U'` in `X'`.

```lean
theorem range_pullbackSituationToX :
    Set.range (pullback.fst fX A'.obj.toX) = fX ⁻¹' Set.range A'.obj.toX
```

**`Crystalline.GlobalCrystallineSituation.pullbackCrisMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L287). The attribute's comment: “the morphism (U/T)\_cris ⟶ (X/S)\_cris”.

> The morphism of small crystalline topoi `(U/T)_cris ⟶ (X/S)_cris` induced by `U ⟶ X` over
> `T ⟶ S`, [Stacks, Tag 07IK]. It is unconditional, left exactness of `i_!` for `X/S` being
> `Crystalline.GlobalCrystallineSituation.CrystallineThickening.preservesFiniteLimits_lowerShriek`.

```lean
def pullbackCrisMorphism :
    MorphismOfTopoi (smallTopos (pullbackSituation S S' fS fX hf A')) (smallTopos S)
```

**`Crystalline.GlobalCrystallineSituation.pullbackStructureToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L308). The attribute's comment: “the structure morphism τ\_\{U/T} : (U/T)\_cris ⟶ Sh(T\_Zar)”.

> **Stacks Project, Tag 07MJ.**  The structure morphism `τ_{U/T} : (U/T)_cris ⟶ Sh(T_Zar)` of
> the remark.

```lean
def pullbackStructureToposMorphism :
    MorphismOfTopoi (smallTopos (pullbackSituation S S' fS fX hf A'))
      (Sheaf (Opens.grothendieckTopology (pullbackBase S S' fS A').scheme.carrier)
        (Type (u + 1)))
```

**`Crystalline.GlobalCrystallineSituation.pullbackSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L318). The attribute's comment: “the pullback F\_U of a sheaf on Cris(X/S) to Cris(U/T); the displayed equation (07MK) is Crystalline.GlobalCrystallineSituation.SmallSite.computes07MK”.

> **Stacks Project, Tag 07MJ.**  The pullback `F_U` to `Cris(U/T)` of a sheaf `F` on
> `Cris(X/S)`.

```lean
def pullbackSheaf (F : smallTopos S) : smallTopos (pullbackSituation S S' fS fX hf A')
```

## Tag 07ML, a remark

[Tag 07ML](https://stacks.math.columbia.edu/tag/07ML) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.exists_distinguished_triangle_derivedCrisModuleDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisDirectImage.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisDirectImage.lean#L298). The attribute's comment: “the distinguished triangle Rf\_\{cris,*}F → Rf'\_\{cris,*}F' ⊕ Rf''\_\{cris,*}F'' → Rf'''\_\{cris,*}F''' → Rf\_\{cris,*}F[1] in D(O\_\{X'/S'}), for an open covering X = X' ∪ X'' in the situation of 07MJ, with Rf\_\{cris,*} the right derived functor of the module-valued direct image and F', F'', F''' the restrictions of the O\_\{X/S}-module F to Cris(X'/S), Cris(X''/S), Cris(X'''/S)”.

> **Stacks Project, Tag 07ML (Mayer--Vietoris for `Rf_{cris, *}`).**  In the situation of
> [Stacks, Tag 07MJ] — a morphism `f : X ⟶ X'` over a morphism of divided power schemes
> `(S, I, γ) ⟶ (S', I', γ')` over `ℤ_(p)`, `p` locally nilpotent on `X` and `X'` — let
> `X = X₁ ∪ X₂` be an open covering (`V₁ ⊔ V₂ = ⊤`) with `X₁₂ = X₁ ∩ X₂`, and let `F` be an
> `𝒪_{X/S}`-module on `Cris(X/S)`.  Writing `f₁`, `f₂`, `f₁₂` for the restrictions of `f` to `X₁`,
> `X₂`, `X₁₂` (morphisms of situations `X₁/S ⟶ X'/S'` etc. over the same `S ⟶ S'`) and `F₁`,
> `F₂`, `F₁₂` for the restrictions of `F` to the crystalline sites `Cris(X₁/S)`, `Cris(X₂/S)`,
> `Cris(X₁₂/S)`, there is a distinguished triangle
>
> `Rf_{cris, *}F ⟶ Rf₁_{cris, *}F₁ ⊕ Rf₂_{cris, *}F₂ ⟶ Rf₁₂_{cris, *}F₁₂ ⟶ Rf_{cris, *}F[1]`
>
> in `D(𝒪_{X'/S'})`, the derived category of sheaves of `𝒪_{X'/S'}`-modules on `Cris(X'/S')`.
> (The source names the opens `X'`, `X''`, `X'''`, the target of `f` also being `X'`.)
>
> Here `Rf_{cris, *}` is `derivedCrisModuleDirectImage`, the right derived functor of the
> module-valued direct image `...SmallSite.crisModuleDirectImage` on `D⁺`, applied to `F` in degree
> zero and read in `D(𝒪_{X'/S'})` through `DerivedCategory.Plus.ι`; `X₁/S` is
> `Crystalline.GlobalCrystallineSituation.openSubspace S V₁`, `f₁` is `V₁.ι ≫ fX` over `fS`, and
> `F₁` is `...SmallSite.openSubspaceModuleRestriction S V₁` of `F`.  The statement holds for every
> choice of the derived category models.

```lean
theorem exists_distinguished_triangle_derivedCrisModuleDirectImage (hV : V₁ ⊔ V₂ = ⊤)
    (F : ModuleSheaf S) :
    ∃ (a : DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage hf).obj
          ((DerivedCategory.Plus.singleFunctor _ 0).obj F)) ⟶
        DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf V₁)).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj
            ((openSubspaceModuleRestriction S V₁).obj F))) ⊞
        DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf V₂)).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj
            ((openSubspaceModuleRestriction S V₂).obj F))))
      (b : DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf V₁)).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj
            ((openSubspaceModuleRestriction S V₁).obj F))) ⊞
        DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf V₂)).obj ((DerivedCategory.Plus.singleFunctor _ 0).obj
            ((openSubspaceModuleRestriction S V₂).obj F))) ⟶
        DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf (V₁ ⊓ V₂))).obj
            ((DerivedCategory.Plus.singleFunctor _ 0).obj
              ((openSubspaceModuleRestriction S (V₁ ⊓ V₂)).obj F))))
      (c : DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage
          (openSubspaceRestrictCondition hf (V₁ ⊓ V₂))).obj
            ((DerivedCategory.Plus.singleFunctor _ 0).obj
              ((openSubspaceModuleRestriction S (V₁ ⊓ V₂)).obj F))) ⟶
        (DerivedCategory.Plus.ι.obj ((derivedCrisModuleDirectImage hf).obj
          ((DerivedCategory.Plus.singleFunctor _ 0).obj F)))⟦(1 : ℤ)⟧),
      Triangle.mk a b c ∈ distTriang (DerivedCategory (ModuleSheaf S'))
```

## Tag 07MS, a remark

[Tag 07MS](https://stacks.math.columbia.edu/tag/07MS) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisGlobalBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapGlobal07MS.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapGlobal07MS.lean#L72). The attribute's comment: “the base change map RΓ(Cris(X'/S'), F') ⊗^L\_\{A'} A ⟶ RΓ(Cris(X/S), F) of (07MT) in D(A), the sheaf-level base change map read on global sections, for an arbitrary g : X ⟶ X'”.

> **The base change map (07MT) on global sections**
>
> `RΓ(Cris(X'/S'), F') ⊗^L_{A'} A ⟶ RΓ(Cris(X/S), F)`   in `D(A)`,
>
> `A = Γ(S, 𝒪_S)`, `A' = Γ(S', 𝒪_{S'})`, for an `𝒪_{X'/S'}`-module `F'`, its pullback
> `F = f_cris^*F'` (`crisModuleInverseImage`) and an arbitrary morphism `g : X ⟶ X'` over a
> morphism of divided power bases `f`. It is `RΓ(S, -)` of the sheaf-level base change map
> `crisSheafBaseChangeMap`, preceded by the canonical map
> `RΓ(S', K) ⊗^L_{A'} A ⟶ RΓ(S, L(S ⟶ S')^*K)` at `K = Rτ_{X'/S', *}F'` and read through
> `RΓ(S, Rτ_*-) = RΓ(Cris, -)` at both ends.

```lean
def crisGlobalBaseChangeMap (F' : ModuleSheaf S') :
    (derivedBaseChangeTensor f).obj
        (DerivedCategory.Plus.ι.obj ((derivedModuleGlobalSections S').obj F')) ⟶
      DerivedCategory.Plus.ι.obj
        ((derivedModuleGlobalSections S).obj ((crisModuleInverseImage f g h).obj F'))
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisSheafBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapSheaf07MS.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapSheaf07MS.lean#L109). The attribute's comment: “the canonical base change map L(S ⟶ S')^* Rτ\_\{X'/S',*} F' ⟶ Rτ\_\{X/S,*} F in D(O\_S), F = f\_cris^* F', for an arbitrary morphism g : X ⟶ X', built as the hint prescribes”.

> **Stacks Project, Tag 07MS: the canonical base change map**
>
> `L(S ⟶ S')^* Rτ_{X'/S', *}F' ⟶ Rτ_{X/S, *}F`   in `D(𝒪_S)`,
>
> for an `𝒪_{X'/S'}`-module `F'`, its pullback `F = f_cris^*F'` (`crisModuleInverseImage`), and an
> arbitrary morphism `g : X ⟶ X'` over a morphism of divided power bases `f` — the situation of
> [Stacks, Tag 07MJ].  As the source's hint prescribes, it is the base change map of
> [Stacks, Tag 07A7] for the square `structureSquareTwoIso`, followed by `Rτ_{X/S, *}` of the
> canonical map `Lf_cris^*F' ⟶ f_cris^*F' = F`.

```lean
def crisSheafBaseChangeMap (F' : ModuleSheaf S') :
    (derivedPullback (X := zariskiRingedTopos S.S.scheme) (Y := zariskiRingedTopos S'.S.scheme)
        (zariskiRingedHom f.hom)).obj (tauDerivedDirectImage S' F') ⟶
      tauDerivedDirectImage S ((crisModuleInverseImage f g h).obj F')
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisModuleInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LowerShriekModules.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LowerShriekModules.lean#L357). The attribute's comment: “the pullback F = f\_cris^* F' of an O\_\{X'/S'}-module F', for an arbitrary morphism g : X ⟶ X'”.

> **`f_cris^{-1}` on sheaves of modules, in the generality of [Stacks, Tag 07MJ]**: no
> hypothesis whatever on `g : X ⟶ X'`, in particular not that it is an open immersion, so this
> covers the hypothesis `X = X' ×_{S'₀} S₀` of [Stacks, Tag 07MU\](4).
>
> It is the composite of the two legs of [Stacks, Tag 07IK]'s
> `f_cris = π_{X'} ∘ f_CRIS ∘ i_X`: the module-level `i_{X', !}` of [Stacks, Tag 07IJ] carries a
> sheaf of `𝒪_{X'/S'}`-modules on `Cris(X'/S')` to the big site `CRIS(X'/S')`, and
> `...SmallSite.crisModulePullback` restricts it along `Cris(X/S) ⥤ CRIS(X/S) ⥤ CRIS(X'/S')`, a
> functor of sites that exists for every `g`.
>
> Where `...SmallSite.smallChangeBaseModulePullback` applies — that is, for `g` an open immersion,
> the generality of [Stacks, Tag 07KL] — the two agree, by
> `crisModuleInverseImageIsoSmallChangeBase`.
>
> This is the pullback `F = f_cris^*F'` of [Stacks, Tag 07MS]; the base change map of that tag,
> `L(S ⟶ S')^*Rτ_{X'/S', *}F' ⟶ Rτ_{X/S, *}F`, is `...SmallSite.crisSheafBaseChangeMap`, and on
> global sections `...SmallSite.crisGlobalBaseChangeMap`.

```lean
def crisModuleInverseImage (f : S.S ⟶ S'.S) (g : S.X ⟶ S'.X)
    (h : S.toClosedFiber ≫ DividedPowerScheme.closedFiberMap f = g ≫ S'.toClosedFiber) :
    ModuleSheaf S' ⥤ ModuleSheaf S
```

## Tag 07MV, a remark

[Tag 07MV](https://stacks.math.columbia.edu/tag/07MV) in the Stacks Project.

**`Crystalline.exists_forall_isPAdicLevel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean#L72). The attribute's comment: “for e ≫ 0 the ideal (p^e) ⊆ I is preserved by γ”.

> **Stacks Project, Tag 07MV.**  For a divided power ring `(A, I, γ)` with `A` an algebra over
> `ℤ_(p)` and `p` nilpotent in `A/I`, every sufficiently large exponent `e` has `(p^e) ⊆ I`
> preserved by `γ`.

```lean
theorem exists_forall_isPAdicLevel [Fact p.Prime]
    [Algebra (DividedPowers.IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    ∃ N, ∀ e, N ≤ e → IsPAdicLevel I γ p e
```

**`Crystalline.pAdicLevelRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean#L138). The attribute's comment: “the divided power ring A/p^eA whose spectrum is the base S\_e = Spec(A/p^eA)”.

> **Stacks Project, Tag 07MV.**  The divided power ring `(A/p^eA, I/p^eA, γ̄)` at a finite
> divided power level `e`, of which the base `S_e = Spec(A/p^eA)` of the remark is the spectrum.

```lean
noncomputable def pAdicLevelRing {e : ℕ} (he : IsPAdicLevel I γ p e) : DividedPowerRing.{u}
```

**`Crystalline.preservesInjectiveObjects_pAdicLevelSheafRestriction`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L159). The attribute's comment: “restriction of abelian sheaves to a finite level carries injectives to injectives, the first half of the remark's hint”.

> **Stacks Project, Tag 07MV.**  Restriction of abelian sheaves from `Cris(X/S)` to a finite
> divided power level `Cris(X/S_e)` carries injective abelian sheaves to injective abelian sheaves.
>
> This is the first half of the hint of the remark.  The functor of levels is change of divided
> power base at the pair `(S_e ⟶ S, 𝟙 X)`, so this is
> `...SmallSite.preservesInjectiveObjects_smallChangeBaseAbelianRestriction`:
> the left adjoint of restriction is the abelian lower shriek, which is exact by
> [Stacks, Tag 00X4] because `Cris(X/S_e)` has fibre products and equalizers and change of base
> preserves them, hence preserves monomorphisms, and a right adjoint of a
> monomorphism-preserving functor preserves injective objects, [Stacks, Tag 015Z].

```lean
instance preservesInjectiveObjects_pAdicLevelSheafRestriction {e : ℕ}
    (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelSheafRestriction I γ p he X toCF hX).PreservesInjectiveObjects
```

**`Crystalline.preservesInjectiveObjects_pAdicLevelStepSheafRestriction`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L176). The attribute's comment: “restriction of abelian sheaves between two finite levels carries injectives to injectives”.

> **Stacks Project, Tag 07MV.**  Restriction of abelian sheaves between two finite divided
> power levels `Cris(X/S_e) ⟶ Cris(X/S_m)`, for `m ≤ e`, carries injective abelian sheaves to
> injective abelian sheaves.  This is the same argument as
> `Crystalline.preservesInjectiveObjects_pAdicLevelSheafRestriction` at the pair
> `(S_m ⟶ S_e, 𝟙 X)`.

```lean
instance preservesInjectiveObjects_pAdicLevelStepSheafRestriction {m e : ℕ}
    (hm : IsPAdicLevel I γ p m) (he : IsPAdicLevel I γ p e) (hme : m ≤ e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelStepSheafRestriction I γ p hm he hme X toCF hX).PreservesInjectiveObjects
```

**`Crystalline.rightAcyclic_globalSections_pAdicLevelSheafRestriction_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L234). The attribute's comment: “restriction to a finite level carries an injective abelian sheaf to one with acyclic global sections, the acyclicity hypothesis of (015M); NOT the tower and NOT the remark's conclusion”.

> **Stacks Project, Tag 07MV.**  Restriction to a finite divided power level carries an
> injective abelian sheaf to one with **acyclic global sections**: this is
> `Crystalline.preservesInjectiveObjects_pAdicLevelSheafRestriction` followed by
> `CategoryTheory.Functor.rightAcyclic_of_injective`, an injective object being right acyclic for
> every additive functor whose bounded below right derived functor exists.
>
> This is verbatim the hypothesis `hg` of
> `Crystalline.GlobalCrystallineSituation.SmallSite.derivedGlobalSectionsCompIso`, and so the
> first half of the hint of the remark.

```lean
theorem rightAcyclic_globalSections_pAdicLevelSheafRestriction_of_injective {e : ℕ}
    (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w'} (Sheaf (smallTopology (pAdicLevelSituation I γ p he X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w''} AddCommGrpCat.{u + 1}] :
    ∀ F : Sheaf (smallTopology (specSituation I γ p X toCF hX)) AddCommGrpCat.{u + 1},
      Injective F → (globalSections (pAdicLevelSituation I γ p he X toCF hX)).rightAcyclic
        ((pAdicLevelSheafRestriction I γ p he X toCF hX).obj F)
```

**`Crystalline.rightAcyclic_globalSections_pAdicLevelStepSheafRestriction_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L253). The attribute's comment: “restriction between two finite levels carries an injective abelian sheaf to one with acyclic global sections, the acyclicity hypothesis of (015M) for the tower's arrows”.

> **Stacks Project, Tag 07MV.**  The transition-functor form of
> `Crystalline.rightAcyclic_globalSections_pAdicLevelSheafRestriction_of_injective`: restriction
> from `Cris(X/S_e)` to `Cris(X/S_m)`, `m ≤ e`, carries an injective abelian sheaf to one with
> acyclic global sections.

```lean
theorem rightAcyclic_globalSections_pAdicLevelStepSheafRestriction_of_injective {m e : ℕ}
    (hm : IsPAdicLevel I γ p m) (he : IsPAdicLevel I γ p e) (hme : m ≤ e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w'} (Sheaf (smallTopology (pAdicLevelSituation I γ p hm X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w''} AddCommGrpCat.{u + 1}] :
    ∀ F : Sheaf (smallTopology (pAdicLevelSituation I γ p he X toCF hX)) AddCommGrpCat.{u + 1},
      Injective F → (globalSections (pAdicLevelSituation I γ p hm X toCF hX)).rightAcyclic
        ((pAdicLevelStepSheafRestriction I γ p hm he hme X toCF hX).obj F)
```

**`Crystalline.pAdicLevelScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L174). The attribute's comment: “S\_e = Spec(A/p^eA) is a divided power base, for e a finite divided power level”.

> The divided power base `S_e = Spec(A/p^eA)` at a finite divided power level `e`: the spectrum
> of the divided power ring `Crystalline.pAdicLevelRing`.

```lean
def pAdicLevelScheme {e : ℕ} (he : IsPAdicLevel I γ p e) : DividedPowerScheme.{u}
```

**`Crystalline.pAdicLevelClosedFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L243). The attribute's comment: “S\_e has the same closed fibre S₀ = Spec(A/I) as S, since (p^e) ⊆ I”.

> The closed fibre of `S_e = Spec(A/p^eA)` is the closed fibre `S_0 = Spec(A/I)` of `S`. Both
> are the spectrum of a double quotient of `A`, and the two double quotients agree because
> `(p^e) ⊆ I`.

```lean
def pAdicLevelClosedFiberIso {e : ℕ} (he : IsPAdicLevel I γ p e) :
    closedFiber (pAdicLevelScheme I γ p he) ≅ closedFiber (specBase I γ)
```

**`Crystalline.pAdicLevelSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L323). The attribute's comment: “X/S\_e is a global crystalline situation on the same X, so Cris(X/S\_e) is defined”.

> The global crystalline situation `X/S_e` at a finite divided power level `e`, on the *same*
> scheme `X`: the structure morphism `X ⟶ S_0` of the situation `X/S` is read in the closed fibre
> of `S_e` through the identification `Crystalline.pAdicLevelClosedFiberIso` of the two closed
> fibres.

```lean
def pAdicLevelSituation {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    GlobalCrystallineSituation.{u}
```

**`Crystalline.pAdicLevelExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L390). The attribute's comment: “the functor Cris(X/S\_e) ⥤ Cris(X/S)”.

> The functor `Cris(X/S_e) ⥤ Cris(X/S)`: change of divided power base along the projection
> `S_e ⟶ S` and the identity of `X`. An object of `Cris(X/S_e)` is a divided power thickening of `X`
> relative to `S_e`, which composed with `S_e ⟶ S` is one relative to `S`.

```lean
def pAdicLevelExtend {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    GlobalCrystallineSituation.CrystallineThickening
        (pAdicLevelSituation I γ p he X toCF hX) ⥤
      GlobalCrystallineSituation.CrystallineThickening (specSituation I γ p X toCF hX)
```

**`Crystalline.pAdicLevelExtendFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L403). The attribute's comment: “Cris(X/S\_e) is a full subcategory of Cris(X/S)”.

> `Cris(X/S_e)` is a full subcategory of `Cris(X/S)`: change of divided power base along
> `S_e ⟶ S` and `𝟙 X` is fully faithful, the projection `S_e ⟶ S` being a closed immersion and
> hence a monomorphism.

```lean
def pAdicLevelExtendFullyFaithful {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelExtend I γ p he X toCF hX).FullyFaithful
```

**`Crystalline.pAdicLevelModuleRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L446). The attribute's comment: “F\_e, the restriction of an 𝒪\_\{X/S}-module F to Cris(X/S\_e), as a presheaf of modules”.

> The restriction `F_e` of a presheaf of `𝒪_{X/S}`-modules on `Cris(X/S)` to a presheaf of
> `𝒪_{X/S_e}`-modules on `Cris(X/S_e)`. No comparison of structure presheaves is needed: the
> restriction of `𝒪_{X/S}` along the functor is `𝒪_{X/S_e}` itself, by
> `Crystalline.pAdicLevelExtend_op_comp_crisRing`.

```lean
def pAdicLevelModuleRestriction {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    (F : PresheafOfModules.{u}
      (GlobalCrystallineSituation.SmallSite.crisRing (specSituation I γ p X toCF hX))) :
    PresheafOfModules.{u}
      (GlobalCrystallineSituation.SmallSite.crisRing
        (pAdicLevelSituation I γ p he X toCF hX))
```

**`Crystalline.pAdicLevelStepExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L419). The attribute's comment: “the transition functor Cris(X/S\_m) ⥤ Cris(X/S\_e) of the tower of finite levels”.

> **Stacks Project, Tag 07MV.**  The transition functor `Cris(X/S_m) ⥤ Cris(X/S_e)` of the tower
> of finite divided power levels, for `m ≤ e`: change of divided power base along the closed
> immersion `S_m ⟶ S_e` and the identity of `X`.  This is the arrow of the tower whose inverse
> limit the remark takes; `Crystalline.pAdicLevelExtend` is its colimit end, the functor
> to `Cris(X/S)` itself.

```lean
def pAdicLevelStepExtend {m e : ℕ} (hm : IsPAdicLevel I γ p m) (he : IsPAdicLevel I γ p e)
    (hme : m ≤ e) (X : Scheme.{u}) (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    GlobalCrystallineSituation.CrystallineThickening
        (pAdicLevelSituation I γ p hm X toCF hX) ⥤
      GlobalCrystallineSituation.CrystallineThickening
        (pAdicLevelSituation I γ p he X toCF hX)
```

**`Crystalline.pAdicLevelStepExtendFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L433). The attribute's comment: “Cris(X/S\_m) is a full subcategory of Cris(X/S\_e) for m ≤ e”.

> **Stacks Project, Tag 07MV.**  `Cris(X/S_m)` is a full subcategory of `Cris(X/S_e)` for
> `m ≤ e`: the transition `S_m ⟶ S_e` is a closed immersion, hence a monomorphism.

```lean
def pAdicLevelStepExtendFullyFaithful {m e : ℕ} (hm : IsPAdicLevel I γ p m)
    (he : IsPAdicLevel I γ p e) (hme : m ≤ e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelStepExtend I γ p hm he hme X toCF hX).FullyFaithful
```

**`Crystalline.pAdicLevelSmallModuleRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L504). The attribute's comment: “F\_e as a sheaf of 𝒪\_\{X/S\_e}-modules on the small site Cris(X/S\_e), by restriction”.

> **Stacks Project, Tag 07MV.**  `F_e`, the restriction of a sheaf of `𝒪_{X/S}`-modules on the
> small crystalline site `Cris(X/S)` to a sheaf of `𝒪_{X/S_e}`-modules on `Cris(X/S_e)`.
>
> This is the `F_e` of the remark.  It is the restriction itself, not a sheafification of it: that
> rests on the continuity of `Crystalline.pAdicLevelExtend`, and no comparison of structure sheaves
> is needed because the restriction of `𝒪_{X/S}` along the functor *is* `𝒪_{X/S_e}`.

```lean
def pAdicLevelSmallModuleRestriction {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    SheafOfModules.{u} (GlobalCrystallineSituation.SmallSite.structureSheaf
        (specSituation I γ p X toCF hX)) ⥤
      SheafOfModules.{u} (GlobalCrystallineSituation.SmallSite.structureSheaf
        (pAdicLevelSituation I γ p he X toCF hX))
```

**`Crystalline.pAdicLevelDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L539). The attribute's comment: “the individual terms RΓ(Cris(X/S\_e), F\_e) of the remark's R lim, for F an abelian sheaf; NOT the tower (its arrows are missing) and NOT the conclusion”.

> **Stacks Project, Tag 07MV.**  `RΓ(Cris(X/S_e), F_e)`, the term at level `e` of the tower
> whose derived inverse limit the remark takes: derived global sections on the small crystalline
> site of `X/S_e` applied to the restriction `F_e` of an abelian sheaf `F` on `Cris(X/S)`.
>
> This is an object of `D⁺(Ab)`, and it is the restriction `F_e` itself — not a sheafification of
> it — that is being evaluated, by the continuity of `Crystalline.pAdicLevelExtend`.

```lean
def pAdicLevelDerivedGlobalSections {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w} (Sheaf (GlobalCrystallineSituation.smallTopology
      (pAdicLevelSituation I γ p he X toCF hX)) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} AddCommGrpCat.{u + 1}]
    (F : Sheaf (GlobalCrystallineSituation.smallTopology (specSituation I γ p X toCF hX))
      AddCommGrpCat.{u + 1}) :
    DerivedCategory.Plus AddCommGrpCat.{u + 1}
```

**`Crystalline.pAdicLevelStepDerivedGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean#L296). The attribute's comment: “the arrow RΓ(Cris(X/S\_e), F\_e) ⟶ RΓ(Cris(X/S\_m), F\_m) of the remark's tower, for m ≤ e”.

> **Stacks Project, Tag 07MV.**  **The arrow
> `RΓ(Cris(X/S_e), F_e) ⟶ RΓ(Cris(X/S_m), F_m)` of the tower of finite divided power levels**, for
> `m ≤ e`.
>
> Four inputs from the library and no hypothesis.  The underived comparison
> `Crystalline.pAdicLevelStepGlobalSectionsTrans` is derived by
> `Stacks.DerivedIndexing.rightDerivedFunctorPlusNatTrans`; its target, the derived functor of the
> composite `ρ ⋙ Γ(Cris(X/S_m), -)`, is split by
> `Crystalline.pAdicLevelStepDerivedGlobalSectionsCompIso`, which is [Stacks, Tag 015M] and is
> unconditional because restriction to a level preserves injectives;
> `CategoryTheory.Functor.rightDerivedFunctorPlusObjSingleIso` replaces `Rρ(F_e[0])` by
> `ρ(F_e)[0]`, restriction to a level being exact; and
> `Crystalline.pAdicLevelStepSheafRestrictionCompIso` identifies `ρ(F_e)` with `F_m`.

```lean
def pAdicLevelStepDerivedGlobalSectionsMap {m e : ℕ} (hm : IsPAdicLevel I γ p m)
    (he : IsPAdicLevel I γ p e) (hme : m ≤ e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w} (Sheaf (smallTopology (pAdicLevelSituation I γ p he X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} (Sheaf (smallTopology (pAdicLevelSituation I γ p hm X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w''} AddCommGrpCat.{u + 1}]
    (F : Sheaf (smallTopology (specSituation I γ p X toCF hX)) AddCommGrpCat.{u + 1}) :
    pAdicLevelDerivedGlobalSections I γ p he X toCF hX F ⟶
      pAdicLevelDerivedGlobalSections I γ p hm X toCF hX F
```

**`Crystalline.pAdicLevelDerivedGlobalSectionsTower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean#L337). The attribute's comment: “the tower e ↦ RΓ(Cris(X/S\_e), F\_e) of the remark, as a functor ℕᵒᵖ ⥤ D⁺(Ab); NOT the remark's conclusion, that RΓ(Cris(X/S), F) is its derived limit”.

> **Stacks Project, Tag 07MV.**  **The tower `n ↦ RΓ(Cris(X/S_{N+n}), F_{N+n})` of the remark,
> as a functor `ℕᵒᵖ ⥤ D⁺(Ab)`.**
>
> The terms are `Crystalline.pAdicLevelDerivedGlobalSections` and the arrows are
> `Crystalline.pAdicLevelStepDerivedGlobalSectionsMap` at the successive pairs `N + n ≤ N + n + 1`.
> `CategoryTheory.Functor.ofOpSequence` asks for no more than those successive steps, which is why
> no coherence between three levels is needed.  The threshold `N` is the one of
> `Crystalline.exists_forall_isPAdicLevel`: the remark's exponents are the levels, and `e ≫ 0` is
> the hypothesis `hN`.
>
> This is the tower whose derived limit the remark asserts is `RΓ(Cris(X/S), F)`.  **That
> assertion is not proved**: nothing below compares the tower with `RΓ(Cris(X/S), F)`.

```lean
def pAdicLevelDerivedGlobalSectionsTower {N : ℕ}
    (hN : ∀ e, N ≤ e → IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w''} AddCommGrpCat.{u + 1}]
    (F : Sheaf (smallTopology (specSituation I γ p X toCF hX)) AddCommGrpCat.{u + 1}) :
    ℕᵒᵖ ⥤ DerivedCategory.Plus AddCommGrpCat.{u + 1}
```

**`Crystalline.pAdicLevelDerivedGlobalSectionsConeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerCone.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerCone.lean#L197). The attribute's comment: “the arrow RΓ(Cris(X/S), F) ⟶ RΓ(Cris(X/S\_e), F\_e) comparing derived global sections with the remark's tower; NOT the remark's conclusion, that RΓ(Cris(X/S), F) is the derived limit”.

> **Stacks Project, Tag 07MV.**  **The arrow `RΓ(Cris(X/S), F) ⟶ RΓ(Cris(X/S_e), F_e)`** from
> derived global sections on `Cris(X/S)` to the term of the remark's tower at the finite divided
> power level `e`.
>
> It is assembled exactly as `Crystalline.pAdicLevelStepDerivedGlobalSectionsMap` is, from four
> proved inputs and no hypothesis.  The underived restriction
> `Crystalline.pAdicLevelGlobalSectionsTrans` is derived by
> `Stacks.DerivedIndexing.rightDerivedFunctorPlusNatTrans`; its target, the derived functor of the
> composite `ρ_e ⋙ Γ(Cris(X/S_e), -)`, is split by
> `Crystalline.pAdicLevelDerivedGlobalSectionsCompIso`, which is [Stacks, Tag 015M] and is
> unconditional because restriction to a level preserves injectives; and
> `CategoryTheory.Functor.rightDerivedFunctorPlusObjSingleIso` replaces `Rρ_e(F[0])` by `F_e[0]`,
> restriction to a level being exact.  Unlike the step map no further identification is needed:
> the sheaf being restricted is `F` itself.
>
> **This is the comparison whose being a derived limit presentation is the conclusion of the
> remark; that it is one is not proved.**

```lean
def pAdicLevelDerivedGlobalSectionsConeMap {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ DividedPowerScheme.closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x))
    [HasDerivedCategory.{w} (Sheaf (smallTopology (specSituation I γ p X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w'} (Sheaf (smallTopology (pAdicLevelSituation I γ p he X toCF hX))
      AddCommGrpCat.{u + 1})]
    [HasDerivedCategory.{w''} AddCommGrpCat.{u + 1}]
    (F : Sheaf (smallTopology (specSituation I γ p X toCF hX)) AddCommGrpCat.{u + 1}) :
    (derivedGlobalSections (specSituation I γ p X toCF hX)).obj F ⟶
      pAdicLevelDerivedGlobalSections I γ p he X toCF hX F
```

## Tag 07MW, a remark

[Tag 07MW](https://stacks.math.columbia.edu/tag/07MW) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.Situation07MW.moduleWithConnection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothLiftingConnection.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothLiftingConnection.lean#L128). The attribute's comment: “(2): the restriction F\_Y of a crystal F in quasi-coherent O\_\{X/S}-modules comes endowed with a canonical integrable connection F\_Y ⟶ F\_Y ⊗ Ω\_\{Y/S}, the restriction of the 07J6 connection, with its twisted de Rham complex”.

> **[Stacks, Tag 07MW] part (2): the restriction `F_Y` of a crystal in quasi-coherent
> `𝒪_{X/S}`-modules to the smooth lifting `(X, Y, γ)` carries a canonical integrable connection.**
> The module is `F_Y`, the connection is `moduleConnection`, the twisted de Rham differential is
> `twistedDeRhamDifferential` (the restriction to `Y` of the de Rham complex of
> [Stacks, Tag 07LM]), and integrability is `twistedDeRhamDifferential_isComplex` in degree zero.
> That the connection is the canonical one of [Stacks, Tag 07J6] is
> `moduleWithConnection_connection_d_eq_canonical`.

```lean
def moduleWithConnection : ModuleWithConnection T.toBase
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.Situation07MW.deRhamComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothLiftingDeRhamCohomology07MW.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SmoothLiftingDeRhamCohomology07MW.lean#L76). The attribute's comment: “(3): RΓ(Cris(X/S), F) = RΓ(Y, F\_Y ⊗ Ω^•\_\{Y/S}) in D(A), for every crystal F in quasi-coherent O\_\{X/S}-modules, F\_Y with the canonical integrable connection of (2)”.

> **Stacks Project, Tag 07MW, part (3).**  Let `p` be a prime, `(A, I, γ)` a divided power
> ring with `p` nilpotent in `A`, `S = Spec(A)`, `Y` a smooth `S`-scheme and `X = Y ×_S S₀`, and let
> `F` be a crystal in quasi-coherent `𝒪_{X/S}`-modules.  Then
>
> `RΓ(Cris(X/S), F) = RΓ(Y, F_Y ⊗_{𝒪_Y} Ω^•_{Y/S})` in `D(A)`,
>
> where `F_Y` carries the canonical integrable connection of part (2),
> `Situation07MW.moduleWithConnection`, and the right hand side is the cohomology of its twisted de
> Rham complex.

```lean
theorem deRhamComparison {F : SheafOfModules.{u} (structureSheaf S)}
    (hF : F.IsQuasicoherentOnSite) :
    Nonempty (moduleULiftDerivedGlobalSections S F ≅
      derivedBaseGlobalSections T.toBase (T.moduleWithConnection hF).complex)
```

**`Crystalline.GlobalCrystallineSituation.smoothLiftingCrystallineThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmoothLifting.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmoothLifting.lean#L337). The attribute's comment: “(1): γ extends to a divided power structure on the ideal of X in Y, and (X, Y, γ) is an object of Cris(X/S)”.

> The object `(X, Y, γ)` of the small crystalline site `Cris(X/S)` given by a smooth lifting
> `Y` of the closed fibre: the object `smoothLiftingThickening` of `CRIS(X/S)`, whose map to `X` is
> the identity.

```lean
noncomputable def smoothLiftingCrystallineThickening : CrystallineThickening base
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.24, Tag 07MI](https://stacks.math.columbia.edu/tag/07MI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
