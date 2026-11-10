---
declaration: section
origin: cited
lean: AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePullback, AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePullback_of_presentation, AlgebraicGeometry.SimplicialScheme.isQuasicoherent_componentModule_modulePushforward, AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePushforward, AlgebraicGeometry.SimplicialScheme.quasicoherentModulePullbackAdjPushforward', AlgebraicGeometry.pullbackToSimplicialSchemeComponentIso, AlgebraicGeometry.isEquivalence_pullbackToSimplicialScheme_of_section, AlgebraicGeometry.isEquivalence_pullbackToSimplicialScheme_of_fpqcLocalSection
statement: formalized
proof: formalized
---

# 85.28 Quasi-coherent modules on simplicial schemes

Section 85.28 of the Stacks Project, [Tag 07TE](https://stacks.math.columbia.edu/tag/07TE). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07TI, a lemma

[Tag 07TI](https://stacks.math.columbia.edu/tag/07TI) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPullbackQuasicoherent.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPullbackQuasicoherent.lean#L51). The attribute's comment: “for a quasi-coherent module, which is the hypothesis the source states; proved through the localization 04J0 of a morphism of ringed sites at an object, in the form asking only that every object of the source site admit an arrow into the image of the functor, applied on the equi-universe model of the total Zariski site, and not through 0D7M”.

> Let `f : V ⟶ U` be a morphism of simplicial schemes and let `F` be a quasi-coherent module on
> `U_Zar`. Then the pullback `f^*F` is a quasi-coherent module on `V_Zar`.

```lean
public theorem isQuasicoherentOnSite_modulePullback (f : V ⟶ U) {F : Modules U}
    (hF : F.IsQuasicoherentOnSite) :
    ((modulePullback f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePullback_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiRingedTopos.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiRingedTopos.lean#L316). The attribute's comment: “for a module admitting a GLOBAL presentation on the total Zariski site, a strengthening of the source's hypothesis that it be quasi-coherent, i.e. presented only locally. The source's statement is proved in full at `AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePullback`, through the localization 04J0 of a morphism of ringed sites at an object on the equi-universe model of the total Zariski site; this is the direct specialization of 03DO, which needs no localization”.

> **Stacks 07TI for a globally presented module.** For a morphism of simplicial schemes
> `f : V ⟶ U` and a sheaf of `𝒪_U`-modules on `U_Zar` admitting a global presentation, the
> pullback `f^*F` is a quasi-coherent sheaf of `𝒪_V`-modules on `V_Zar`.

```lean
public theorem isQuasicoherentOnSite_modulePullback_of_presentation (f : V ⟶ U)
    {F : Modules U} (P : F.Presentation) :
    ((modulePullback f).obj F).IsQuasicoherentOnSite
```

## Tag 07TJ, a lemma

[Tag 07TJ](https://stacks.math.columbia.edu/tag/07TJ) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.isQuasicoherent_componentModule_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherent.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherent.lean#L185). The attribute's comment: “the quasi-coherence of the COMPONENTS of the pushforward only: `(f_*G)_n` is a quasi-coherent module on `U_n` as soon as `f_n` is quasi-compact and quasi-separated and `G_n` is quasi-coherent. This is the source's identification `F_n = f_{n,*}G_n` (09VP, here `componentModulePushforwardIso`) together with 01LC, and it needs neither the cartesian hypothesis on `f` nor the flatness of the face maps of `U`. What is NOT proved is that `f_*G` is quasi-coherent on the total Zariski site: the source gets that from 0D7M, of which this development has only the right-hand side (`CategoryTheory.SimplicialSiteSituation.IsCartesianWithQuasicoherentComponents`, neither direction of the equivalence), and the other half of that right-hand side -- that `f_*G` is cartesian, which is where 02KH and the flatness of the face maps enter -- cannot even be stated here, the development carrying no cartesian-module predicate for the total Zariski site of a simplicial scheme”.

> **Stacks 07TJ for the components of the pushforward.** Let `f : V ⟶ U` be a morphism of
> simplicial schemes and `G` a sheaf of `𝒪_V`-modules on the total Zariski site. If `f_n` is
> quasi-compact and quasi-separated and the degree-`n` component `G_n` is a quasi-coherent
> `𝒪_{V_n}`-module, then the degree-`n` component `(f_*G)_n` of the pushforward is a
> quasi-coherent `𝒪_{U_n}`-module.

```lean
public theorem isQuasicoherent_componentModule_modulePushforward (f : V ⟶ U)
    (n : SimplexCategoryᵒᵖ) [QuasiCompact (f.app n)] [QuasiSeparated (f.app n)]
    (G : Modules V) [((componentModule V n).obj G).IsQuasicoherent] :
    ((componentModule U n).obj ((modulePushforward f).obj G)).IsQuasicoherent
```

**`AlgebraicGeometry.SimplicialScheme.isQuasicoherentOnSite_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherentTotal.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiPushforwardQuasicoherentTotal.lean#L61).

> **Stacks 07TJ.** Let `f : V ⟶ U` be a cartesian morphism of simplicial schemes, assume that
> the face maps `d^n_j` of `U` are flat and that the components `f_n : V_n ⟶ U_n` are quasi-compact
> and quasi-separated. Then for a quasi-coherent module `G` on the total Zariski site of `V` the
> direct image `f_*G` is a quasi-coherent module on the total Zariski site of `U`.

```lean
public theorem isQuasicoherentOnSite_modulePushforward (f : V ⟶ U)
    (hcart : NatTrans.Equifibered f)
    (hflat : ∀ (k : ℕ) (j : Fin (k + 2)), Flat (U.δ j))
    (hqc : ∀ k : SimplexCategoryᵒᵖ, QuasiCompact (f.app k))
    (hqs : ∀ k : SimplexCategoryᵒᵖ, QuasiSeparated (f.app k))
    (G : Modules V) (hG : G.IsQuasicoherentOnSite) :
    ((modulePushforward f).obj G).IsQuasicoherentOnSite
```

## Tag 07TK, a lemma

[Tag 07TK](https://stacks.math.columbia.edu/tag/07TK) in the Stacks Project.

**`AlgebraicGeometry.SimplicialScheme.quasicoherentModulePullbackAdjPushforward'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiQuasicoherentAdjunctionUnconditional.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ZariskiQuasicoherentAdjunctionUnconditional.lean#L116).

> **Stacks 07TK.** Let `f : V ⟶ U` be a cartesian morphism of simplicial schemes such that
> every face map of `U` is flat and every component `f_n : V_n ⟶ U_n` is quasi-compact and
> quasi-separated. Then the pullback `f^*` and the pushforward `f_*` are an adjoint pair between
> the category of quasi-coherent modules on `U_Zar` and the category of quasi-coherent modules on
> `V_Zar`.
>
> Quasi-coherence of the pullback is Stacks 07TI and of the pushforward is Stacks 07TJ;
> adjointness itself is the adjunction of Stacks 03D7 on all sheaves of modules, restricted along
> the two full subcategory inclusions.

```lean
public noncomputable def quasicoherentModulePullbackAdjPushforward' (f : V ⟶ U)
    (hcart : NatTrans.Equifibered f)
    (hflat : ∀ (k : ℕ) (j : Fin (k + 2)), Flat (U.δ j))
    (hqc : ∀ k : SimplexCategoryᵒᵖ, QuasiCompact (f.app k))
    (hqs : ∀ k : SimplexCategoryᵒᵖ, QuasiSeparated (f.app k)) :
    quasicoherentModulePullback f ⊣ quasicoherentModulePushforward' f hcart hflat hqc hqs
```

## Tag 07TL, a lemma

[Tag 07TL](https://stacks.math.columbia.edu/tag/07TL) in the Stacks Project.

**`AlgebraicGeometry.pullbackToSimplicialSchemeComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean#L147). The attribute's comment: “the functor is pullback: its component in degree n is the pullback along the structure morphism (X/S)\_n ⟶ S”.

> **The pullback is computed degreewise**: the component in degree `n` of the pullback of a
> quasi-coherent `O_S`-module `M` to the total Zariski site of `(X/S)_•` is the pullback of `M`
> along the structure morphism `(X/S)_n ⟶ S`, naturally in `M`.

```lean
def pullbackToSimplicialSchemeComponentIso (n : ℕ) :
    pullbackToSimplicialScheme f ⋙ ObjectProperty.ι _ ⋙ componentModule _ (op ⦋n⦌) ≅
      ObjectProperty.ι _ ⋙ Scheme.Modules.pullback (baseMap f n)
```

**`AlgebraicGeometry.isEquivalence_pullbackToSimplicialScheme_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean#L166).

> Let `f : X ⟶ S` be a morphism of schemes with a section `σ`, and let `(X/S)_•` be the
> simplicial scheme of Stacks 024A. Then pullback is an equivalence between the quasi-coherent
> `O_S`-modules and the quasi-coherent modules on the total Zariski site `((X/S)_•)_Zar`. The
> pullback functor is `AlgebraicGeometry.pullbackToSimplicialScheme`; its component in degree `n`
> is the pullback along `(X/S)_n ⟶ S`
> (`AlgebraicGeometry.pullbackToSimplicialSchemeComponentIso`).

```lean
theorem isEquivalence_pullbackToSimplicialScheme_of_section (σ : S ⟶ X) (hσ : σ ≫ f = 𝟙 S) :
    (pullbackToSimplicialScheme f).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_pullbackToSimplicialScheme_of_fpqcLocalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesSimplicialSection.lean#L176). The attribute's comment: “the footnote: it is enough that f have a section fpqc locally on S”.

> Pullback is an equivalence between the quasi-coherent `O_S`-modules and the quasi-coherent
> modules on `((X/S)_•)_Zar` already when `f` has a section only fpqc locally on `S`: there is an
> fpqc covering `{p_i : T_i ⟶ S}` and morphisms `s_i : T_i ⟶ X` with `s_i ≫ f = p_i`.

```lean
theorem isEquivalence_pullbackToSimplicialScheme_of_fpqcLocalSection {I : Type*}
    {T : I → Scheme.{u}} (p : ∀ i, T i ⟶ S)
    (hp : Presieve.ofArrows T p ∈ Scheme.fpqcPrecoverage.{u} S)
    (s : ∀ i, T i ⟶ X) (hs : ∀ i, s i ≫ f = p i) :
    (pullbackToSimplicialScheme f).IsEquivalence
```

**`AlgebraicGeometry.quasicoherentDescentEquivalenceOfSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesWithSection.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesWithSection.lean#L185). The attribute's comment: “the equivalence, with its target in descent-data form: the quasi-coherent descent data for \{f}, not yet identified with QCoh(((X/S)\_bullet)\_Zar); that identification is the cited 07TJ together with 07TH, and 07TJ is absent here”.

> **Stacks 07TL, in its descent-data form.** For a morphism of schemes `f : X ⟶ S` with a
> section, pullback is an equivalence between the category of quasi-coherent `O_S`-modules and the
> category of quasi-coherent descent data for `{f}`, i.e. the quasi-coherent modules on the
> simplicial scheme `(X/S)_•` of Stacks 024A.

```lean
def quasicoherentDescentEquivalenceOfSection
    (f : X ⟶ S) (σ : S ⟶ X) (hσ : σ ≫ f = 𝟙 S) :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      QuasicoherentDescentData (PreZeroHypercover.singleton.{0} f).f
```

**`AlgebraicGeometry.quasicoherentDescentEquivalenceOfFpqcLocalSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesWithSection.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/QuasiCoherentModulesWithSection.lean#L222). The attribute's comment: “the footnote's stronger form, f having a section only fpqc locally on S; target in descent-data form as above, its identification with QCoh(((X/S)\_bullet)\_Zar) being the cited 07TJ together with 07TH, and 07TJ is absent here”.

> **Stacks 07TL in the stronger form of its footnote, in the descent-data form.** If `f` admits
> a section after an fpqc covering of `S`, pullback is an equivalence between the quasi-coherent
> `O_S`-modules and the quasi-coherent descent data for `{f}`, i.e. the quasi-coherent modules on
> the simplicial scheme `(X/S)_•` of Stacks 024A.

```lean
def quasicoherentDescentEquivalenceOfFpqcLocalSection
    (f : X ⟶ S) {I : Type v} {T : I → Scheme.{u}} (p : ∀ i, T i ⟶ S)
    (hp : Presieve.ofArrows T p ∈ Scheme.fpqcPrecoverage.{u} S)
    (s : ∀ i, T i ⟶ X) (hs : ∀ i, s i ≫ f = p i) :
    (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory ≌
      QuasicoherentDescentData (PreZeroHypercover.singleton.{0} f).f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.28, Tag 07TE](https://stacks.math.columbia.edu/tag/07TE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
