---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.pullbackToClosedFiber, Crystalline.GlobalCrystallineSituation.pullbackSituation, Crystalline.GlobalCrystallineSituation.isOpenImmersion_pullbackSituationToX, Crystalline.GlobalCrystallineSituation.range_pullbackSituationToX, Crystalline.GlobalCrystallineSituation.pullbackCrisMorphism, Crystalline.GlobalCrystallineSituation.pullbackStructureToposMorphism, Crystalline.GlobalCrystallineSituation.pullbackSheaf, Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.isPullback_sections_openCoverSquare
statement: formalized
proof: formalized
---

# 60.24 Some further results

Section 60.24 of the Stacks Project, [Tag 07MI](https://stacks.math.columbia.edu/tag/07MI). 5 tags here are carried by 34 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07MJ, a remark

[Tag 07MJ](https://stacks.math.columbia.edu/tag/07MJ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.pullbackToClosedFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L187). The attribute's comment: “the induced morphism U ⟶ T₀, for T = S ×_{S'} T' and U = X ×_{X'} U'”.

> **Stacks Project, Tag 07MJ.**  The induced morphism `U ⟶ T₀` of the remark: the closed fibre
> of `T = S ×_{S'} T'` is `S₀ ×_{S'₀} T'₀` by [Stacks, Tag 07ME], and `U = X ×_{X'} U'` maps to `S₀`
> through `X` and to `T'₀ = U'` through `U'`.

```lean
def pullbackToClosedFiber : pullbackSource S S' fX A' ⟶ closedFiber (pullbackBase S S' fS A')
```

**`Crystalline.GlobalCrystallineSituation.pullbackSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L219). The attribute's comment: “the crystalline situation U/T attached to an object (U', T', δ') of Cris(X'/S')”.

> **Stacks Project, Tag 07MJ.**  The crystalline situation `U/T` of the remark attached to an
> object `(U', T', δ')` of `Cris(X'/S')`: the divided power base is the fibre product
> `T = S ×_{S'} T'` of [Stacks, Tag 07ME], the scheme is `U = X ×_{X'} U'`, and the structure
> morphism to `T₀` is `pullbackToClosedFiber`.  The prime `p` is locally nilpotent on `U` because it
> is on `X` and `U ⟶ X` induces maps on local rings.

```lean
def pullbackSituation : GlobalCrystallineSituation.{u}
```

**`Crystalline.GlobalCrystallineSituation.isOpenImmersion_pullbackSituationToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L262). The attribute's comment: “U = X ×_{X'} U' is an open subscheme of X”.

> **Stacks Project, Tag 07MJ.**  `U = X ×_{X'} U'` is an open subscheme of `X`, the morphism
> `U' ⟶ X'` of an object of the small crystalline site being an open immersion.

```lean
theorem isOpenImmersion_pullbackSituationToX :
    IsOpenImmersion (pullback.fst fX A'.obj.toX)
```

**`Crystalline.GlobalCrystallineSituation.range_pullbackSituationToX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L270). The attribute's comment: “U = X ×_{X'} U' is f⁻¹(U')”.

> **Stacks Project, Tag 07MJ.**  The open subscheme `U = X ×_{X'} U'` of `X` is `f⁻¹(U')`: its
> image in `X` is the preimage under `f` of the image of `U'` in `X'`.

```lean
theorem range_pullbackSituationToX :
    Set.range (pullback.fst fX A'.obj.toX) = fX ⁻¹' Set.range A'.obj.toX
```

**`Crystalline.GlobalCrystallineSituation.pullbackCrisMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L287). The attribute's comment: “the morphism (U/T)_cris ⟶ (X/S)_cris”.

> The morphism of small crystalline topoi `(U/T)_cris ⟶ (X/S)_cris` induced by `U ⟶ X` over
> `T ⟶ S`, [Stacks, Tag 07IK]. It is unconditional, left exactness of `i_!` for `X/S` being
> `Crystalline.GlobalCrystallineSituation.CrystallineThickening.preservesFiniteLimits_lowerShriek`.

```lean
def pullbackCrisMorphism :
    MorphismOfTopoi (smallTopos (pullbackSituation S S' fS fX hf A')) (smallTopos S)
```

**`Crystalline.GlobalCrystallineSituation.pullbackStructureToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L308). The attribute's comment: “the structure morphism τ_{U/T} : (U/T)_cris ⟶ Sh(T_Zar)”.

> **Stacks Project, Tag 07MJ.**  The structure morphism `τ_{U/T} : (U/T)_cris ⟶ Sh(T_Zar)` of
> the remark.

```lean
def pullbackStructureToposMorphism :
    MorphismOfTopoi (smallTopos (pullbackSituation S S' fS fX hf A'))
      (Sheaf (Opens.grothendieckTopology (pullbackBase S S' fS A').scheme.carrier)
        (Type (u + 1)))
```

**`Crystalline.GlobalCrystallineSituation.pullbackSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/HigherDirectImage.lean#L320). The attribute's comment: “the pullback F_U of a sheaf on Cris(X/S) to Cris(U/T), completing the data of the remark's recipe. NOT covered, here or elsewhere: the displayed equation 07MK (Rf_{cris,*}F)_{T'} = R(T → T')_*(R τ_{U/T,*} F_U), which the source states without proof, and the hint that Cris(U/T) is the localization of Cris(X/S) at f_cris^{-1} h_{(U',T',δ')}”.

> **Stacks Project, Tag 07MJ.**  The pullback `F_U` to `Cris(U/T)` of a sheaf `F` on
> `Cris(X/S)`.

```lean
def pullbackSheaf (F : smallTopos S) : smallTopos (pullbackSituation S S' fS fX hf A')
```

## Tag 07ML, a remark

[Tag 07ML](https://stacks.math.columbia.edu/tag/07ML) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.isPullback_sections_openCoverSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisCover.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisCover.lean#L324). The attribute's comment: “the Mayer-Vietoris square of the covering on Cris(X/S), the fact the remark's triangle is a formal consequence of. The triangle at a fixed object of the site is openCoverTriangle_distinguished of SmallSite/MayerVietorisTriangle.lean; the remark's own statement, about the derived global sections of the four crystalline sites, is not stated”.

> **Stacks Project, Tag 07ML.**  Mayer--Vietoris for an open covering `X = X' ∪ X''` on the small
> crystalline site: for every sheaf `F` on `Cris(X/S)` and every object `(U, T, δ)`, the sections of
> `F` over `(U, T, δ)` and over its restrictions to `X'`, `X''` and `X''' = X' ∩ X''` form a
> cartesian square.  For a sheaf of abelian groups this is exactness of
> `0 ⟶ F(U, T, δ) ⟶ F' ⊕ F'' ⟶ F'''`.
>
> This is the geometric input the remark reduces its distinguished triangle to.  The short exact
> form of this square at an injective abelian sheaf is
> `CrystallineThickening.openCoverShortComplex_shortExact` of
> `StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisShortExact.lean`, and the
> triangle it yields, at a fixed object of the site, is
> `CrystallineThickening.openCoverTriangle_distinguished` of
> `StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisTriangle.lean`.  What the
> remark's own statement still wants is the same sequence for the derived *global* sections of the
> four crystalline sites; see the module documentation.

```lean
theorem isPullback_sections_openCoverSquare {𝒜 : Type v} [Category.{w} 𝒜]
    (A : CrystallineThickening S) {V₁ V₂ : S.X.Opens} (hV : V₁ ⊔ V₂ = ⊤)
    (F : Sheaf (smallTopology S) 𝒜) :
    ((openCoverSquare A V₁ V₂).op.map F.obj).IsPullback
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.openCoverShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisShortExact.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisShortExact.lean#L87). The attribute's comment: “the Mayer-Vietoris sequence of the covering on Cris(X/S), short exact at an injective sheaf, which is the form a derived functor consumes. NOT the remark's triangle: that is openCoverTriangle_distinguished of SmallSite/MayerVietorisTriangle.lean, at a fixed object of the site, and identifying its terms with RGamma of the four sites is still open”.

> **The Mayer--Vietoris sequence of an injective abelian sheaf on `Cris(X/S)` for an open
> covering `X = X' ∪ X''` is short exact**:
>
> `0 ⟶ I(U, T, δ) ⟶ I' ⊕ I'' ⟶ I''' ⟶ 0`.

```lean
theorem openCoverShortComplex_shortExact (A : CrystallineThickening S) {V₁ V₂ : S.X.Opens}
    (hV : V₁ ⊔ V₂ = ⊤) (I : Sheaf (smallTopology S) AddCommGrpCat.{u + 1}) [Injective I] :
    (openCoverShortComplex A V₁ V₂ I).ShortExact
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.longExact_openCoverFunctorComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisTriangle.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisTriangle.lean#L265). The attribute's comment: “the long exact sequence of the same Mayer-Vietoris short complex of section functors, at a fixed object of Cris(X/S). NOT the identification of its terms with RGamma of the four crystalline sites: that needs the same sequence for GLOBAL sections, see the module docstring”.

> **Stacks Project, Tag 07ML.**  The long exact sequence of the Mayer--Vietoris short complex
> of section functors of an open covering `X = X' ∪ X''`, at a fixed object `(U, T, δ)` of
> `Cris(X/S)`: the right derived functors of sections over `(U, T, δ)`, of the sum of sections over
> the `X'`- and `X''`-parts, and of sections over the `X'''`-part fit into a long exact sequence,
> natural in the abelian sheaf.
>
> The same scope caveat as for `openCoverTriangle_distinguished` applies: this is the sequence at a
> fixed object of the site, and identifying its terms with the derived global sections of the four
> crystalline sites of the remark needs clause (d) of [Stacks, Tag 07KL].

```lean
theorem longExact_openCoverFunctorComplex (A : CrystallineThickening S) {V₁ V₂ : S.X.Opens}
    (hV : V₁ ⊔ V₂ = ⊤) :
    ∃ delta : ∀ n : ℕ, (openCoverFunctorComplex A V₁ V₂).X₃.rightDerived n ⟶
        (openCoverFunctorComplex A V₁ V₂).X₁.rightDerived (n + 1),
      (∀ F : Sheaf (smallTopology S) AddCommGrpCat.{u + 1},
          Mono ((NatTrans.rightDerived (openCoverFunctorComplex A V₁ V₂).f 0).app F)) ∧
        ∀ (n : ℕ) (F : Sheaf (smallTopology S) AddCommGrpCat.{u + 1}),
          (ComposableArrows.mk₅
            ((NatTrans.rightDerived (openCoverFunctorComplex A V₁ V₂).f n).app F)
            ((NatTrans.rightDerived (openCoverFunctorComplex A V₁ V₂).g n).app F)
            ((delta n).app F)
            ((NatTrans.rightDerived (openCoverFunctorComplex A V₁ V₂).f (n + 1)).app F)
            ((NatTrans.rightDerived (openCoverFunctorComplex A V₁ V₂).g (n + 1)).app F)).Exact
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.CrystallineThickening.openCoverTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisTriangle.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/MayerVietorisTriangle.lean#L347). The attribute's comment: “the remark's distinguished triangle, at a fixed object (U, T, delta) of Cris(X/S) and a fixed pair of opens of X, for a cochain complex of injective abelian sheaves. NOT the identification of the three terms with RGamma(Cris(X'/S), F) etc., which needs the same short exact sequence for GLOBAL sections of the four sites; see the module docstring”.

> **Stacks Project, Tag 07ML.**  The Mayer--Vietoris triangle of an open covering
> `X = X' ∪ X''` on the small crystalline site is distinguished: for every object `(U, T, δ)` of
> `Cris(X/S)` and every cochain complex `K` of injective abelian sheaves on `Cris(X/S)`,
>
> `Γ((U, T, δ), K) ⟶ Γ(X'-part, K) ⊕ Γ(X''-part, K) ⟶ Γ(X'''-part, K) ⟶ [1]`
>
> is a distinguished triangle of `D(Ab)`.
>
> This is the remark's triangle at a *fixed* object of the site and a fixed pair of opens of `X`.
> Identifying its three terms with `RΓ(Cris(X/S), F)`, `RΓ(Cris(X'/S), F)`, `RΓ(Cris(X''/S), F)`
> and `RΓ(Cris(X'''/S), F)` is a further step, which the module docstring describes; it is not
> claimed here.

```lean
theorem openCoverTriangle_distinguished (A : CrystallineThickening S) {V₁ V₂ : S.X.Opens}
    (hV : V₁ ⊔ V₂ = ⊤) (K : CochainComplex (Sheaf (smallTopology S) AddCommGrpCat.{u + 1}) ℤ)
    (hK : ∀ n, Injective (K.X n)) :
    openCoverTriangle A hV K hK ∈ distTriang (DerivedCategory AddCommGrpCat.{u + 1})
```

## Tag 07MS, a remark

[Tag 07MS](https://stacks.math.columbia.edu/tag/07MS) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisGlobalBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapGlobal07MS.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapGlobal07MS.lean#L72). The attribute's comment: “the base change map RΓ(Cris(X'/S'), F') ⊗^L_{A'} A ⟶ RΓ(Cris(X/S), F) of (07MT) in D(A), the sheaf-level base change map read on global sections, for an arbitrary g : X ⟶ X'”.

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

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisSheafBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapSheaf07MS.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/BaseChangeMapSheaf07MS.lean#L109). The attribute's comment: “the canonical base change map L(S ⟶ S')^* Rτ_{X'/S',*} F' ⟶ Rτ_{X/S,*} F in D(O_S), F = f_cris^* F', for an arbitrary morphism g : X ⟶ X', built as the hint prescribes”.

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

**`Crystalline.GlobalCrystallineSituation.SmallSite.crisModuleInverseImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LowerShriekModules.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/LowerShriekModules.lean#L357). The attribute's comment: “the pullback F = f_cris^* F' of an O_{X'/S'}-module F', for an arbitrary morphism g : X ⟶ X'”.

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

**`Crystalline.exists_forall_isPAdicLevel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean#L72). The attribute's comment: “for e ≫ 0 the ideal (p^e) ⊆ I is preserved by γ”.

> **Stacks Project, Tag 07MV.**  For a divided power ring `(A, I, γ)` with `A` an algebra over
> `ℤ_(p)` and `p` nilpotent in `A/I`, every sufficiently large exponent `e` has `(p^e) ⊆ I`
> preserved by `γ`.

```lean
theorem exists_forall_isPAdicLevel [Fact p.Prime]
    [Algebra (DividedPowers.IntegersAtPrime p) A]
    (hp : IsNilpotent (Ideal.Quotient.mk I (p : A))) :
    ∃ N, ∀ e, N ≤ e → IsPAdicLevel I γ p e
```

**`Crystalline.pAdicLevelRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelBase.lean#L138). The attribute's comment: “the divided power ring A/p^eA whose spectrum is the base S_e = Spec(A/p^eA)”.

> **Stacks Project, Tag 07MV.**  The divided power ring `(A/p^eA, I/p^eA, γ̄)` at a finite
> divided power level `e`, of which the base `S_e = Spec(A/p^eA)` of the remark is the spectrum.

```lean
noncomputable def pAdicLevelRing {e : ℕ} (he : IsPAdicLevel I γ p e) : DividedPowerRing.{u}
```

**`Crystalline.preservesInjectiveObjects_pAdicLevelSheafRestriction`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L159). The attribute's comment: “restriction of abelian sheaves to a finite level carries injectives to injectives, the first half of the remark's hint”.

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

**`Crystalline.preservesInjectiveObjects_pAdicLevelStepSheafRestriction`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L176). The attribute's comment: “restriction of abelian sheaves between two finite levels carries injectives to injectives”.

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

**`Crystalline.rightAcyclic_globalSections_pAdicLevelSheafRestriction_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L234). The attribute's comment: “restriction to a finite level carries an injective abelian sheaf to one with acyclic global sections, the acyclicity hypothesis of (015M); NOT the tower and NOT the remark's conclusion”.

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

**`Crystalline.rightAcyclic_globalSections_pAdicLevelStepSheafRestriction_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelRestrictionInjectives.lean#L253). The attribute's comment: “restriction between two finite levels carries an injective abelian sheaf to one with acyclic global sections, the acyclicity hypothesis of (015M) for the tower's arrows”.

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

**`Crystalline.pAdicLevelScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L174). The attribute's comment: “S_e = Spec(A/p^eA) is a divided power base, for e a finite divided power level”.

> The divided power base `S_e = Spec(A/p^eA)` at a finite divided power level `e`: the spectrum
> of the divided power ring `Crystalline.pAdicLevelRing`.

```lean
def pAdicLevelScheme {e : ℕ} (he : IsPAdicLevel I γ p e) : DividedPowerScheme.{u}
```

**`Crystalline.pAdicLevelClosedFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L243). The attribute's comment: “S_e has the same closed fibre S₀ = Spec(A/I) as S, since (p^e) ⊆ I”.

> The closed fibre of `S_e = Spec(A/p^eA)` is the closed fibre `S_0 = Spec(A/I)` of `S`. Both
> are the spectrum of a double quotient of `A`, and the two double quotients agree because
> `(p^e) ⊆ I`.

```lean
def pAdicLevelClosedFiberIso {e : ℕ} (he : IsPAdicLevel I γ p e) :
    closedFiber (pAdicLevelScheme I γ p he) ≅ closedFiber (specBase I γ)
```

**`Crystalline.pAdicLevelSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L323). The attribute's comment: “X/S_e is a global crystalline situation on the same X, so Cris(X/S_e) is defined”.

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

**`Crystalline.pAdicLevelExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L390). The attribute's comment: “the functor Cris(X/S_e) ⥤ Cris(X/S)”.

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

**`Crystalline.pAdicLevelExtendFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L403). The attribute's comment: “Cris(X/S_e) is a full subcategory of Cris(X/S)”.

> `Cris(X/S_e)` is a full subcategory of `Cris(X/S)`: change of divided power base along
> `S_e ⟶ S` and `𝟙 X` is fully faithful, the projection `S_e ⟶ S` being a closed immersion and
> hence a monomorphism.

```lean
def pAdicLevelExtendFullyFaithful {e : ℕ} (he : IsPAdicLevel I γ p e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelExtend I γ p he X toCF hX).FullyFaithful
```

**`Crystalline.pAdicLevelModuleRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelSite.lean#L446). The attribute's comment: “F_e, the restriction of an 𝒪_{X/S}-module F to Cris(X/S_e), as a presheaf of modules”.

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

**`Crystalline.pAdicLevelStepExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L419). The attribute's comment: “the transition functor Cris(X/S_m) ⥤ Cris(X/S_e) of the tower of finite levels”.

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

**`Crystalline.pAdicLevelStepExtendFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L433). The attribute's comment: “Cris(X/S_m) is a full subcategory of Cris(X/S_e) for m ≤ e”.

> **Stacks Project, Tag 07MV.**  `Cris(X/S_m)` is a full subcategory of `Cris(X/S_e)` for
> `m ≤ e`: the transition `S_m ⟶ S_e` is a closed immersion, hence a monomorphism.

```lean
def pAdicLevelStepExtendFullyFaithful {m e : ℕ} (hm : IsPAdicLevel I γ p m)
    (he : IsPAdicLevel I γ p e) (hme : m ≤ e) (X : Scheme.{u})
    (toCF : X ⟶ closedFiber (specBase I γ))
    (hX : ∀ x : X, IsNilpotent (p : X.presheaf.stalk x)) :
    (pAdicLevelStepExtend I γ p hm he hme X toCF hX).FullyFaithful
```

**`Crystalline.pAdicLevelSmallModuleRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L504). The attribute's comment: “F_e as a sheaf of 𝒪_{X/S_e}-modules on the small site Cris(X/S_e), by restriction”.

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

**`Crystalline.pAdicLevelDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean, line 539](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTower.lean#L539). The attribute's comment: “the individual terms RΓ(Cris(X/S_e), F_e) of the remark's R lim, for F an abelian sheaf; NOT the tower (its arrows are missing) and NOT the conclusion”.

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

**`Crystalline.pAdicLevelStepDerivedGlobalSectionsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean#L296). The attribute's comment: “the arrow RΓ(Cris(X/S_e), F_e) ⟶ RΓ(Cris(X/S_m), F_m) of the remark's tower, for m ≤ e”.

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

**`Crystalline.pAdicLevelDerivedGlobalSectionsTower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerArrows.lean#L337). The attribute's comment: “the tower e ↦ RΓ(Cris(X/S_e), F_e) of the remark, as a functor ℕᵒᵖ ⥤ D⁺(Ab); NOT the remark's conclusion, that RΓ(Cris(X/S), F) is its derived limit”.

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

**`Crystalline.pAdicLevelDerivedGlobalSectionsConeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerCone.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FiniteLevelTowerCone.lean#L197). The attribute's comment: “the arrow RΓ(Cris(X/S), F) ⟶ RΓ(Cris(X/S_e), F_e) comparing derived global sections with the remark's tower; NOT the remark's conclusion, that RΓ(Cris(X/S), F) is the derived limit”.

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

**`Crystalline.GlobalCrystallineSituation.smoothLiftingCrystallineThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmoothLifting.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmoothLifting.lean#L343). The attribute's comment: “part (1): γ extends to the ideal of X in Y, and (X, Y, γ) is an object of Cris(X/S)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
