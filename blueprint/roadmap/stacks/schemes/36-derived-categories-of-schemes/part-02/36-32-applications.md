---
declaration: section
origin: cited
lean: AlgebraicGeometry.FibreBetti.fibreBetti_baseChange, AlgebraicGeometry.FibreBetti.upperSemicontinuous_fibreBetti, AlgebraicGeometry.FibreBetti.fibreBetti_baseChange_upperSemicontinuous_isLocallyConstructible, AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.isLocallyConstant_chiFibre, AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.chiFibre_baseChange, AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.isLocallyConstant_fibreEulerCharacteristic, AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.fibreEulerCharacteristic_baseChange, AlgebraicGeometry.ProperFlatRankOpen.factorsThrough_rankOpen_iff
statement: formalized
proof: formalized
---

# 36.32 Applications

Section 36.32 of the Stacks Project, [Tag 0BDM](https://stacks.math.columbia.edu/tag/0BDM). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BDN, a lemma

[Tag 0BDN](https://stacks.math.columbia.edu/tag/0BDN) in the Stacks Project.

**`AlgebraicGeometry.FibreBetti.fibreBetti_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbers.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbers.lean#L179). The attribute's comment: “part (1): formation of the Betti functions beta_i of the fibres commutes with arbitrary base change. The function beta_i is fibreBetti, dim over kappa(s) of H^i of the pullback of F to the scheme-theoretic fibre X_s, and all four hypotheses of the source are fields of IsFlatFamily, which CohomologyAndBaseChange extends. WHAT IS ASSUMED rather than proved: the source's cohomology-and-base-change step, carried as the fields isPseudoCoherent and fibreBetti_eq of CohomologyAndBaseChange (that Rf_*F is pseudo-coherent and that beta_i is its derived-fibre Betti function) and as BaseChangeCompatible (that the formation of Rf_*F commutes with the cartesian square). Both are consequences of Stacks 0B91, of which this library carries ONLY the base-change half of the conclusion and that half in the tensor form of the source's own reduction, namely AlgebraicGeometry.ProperFlatBaseChange.isIso_tensorFlatBaseChangeMap_module in StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChange.lean line 334, tagged at line 309: invertibility of tensorFlatBaseChangeMap at F in degree zero, hence for Rf_*(O_X tensor^L F) and not for Rf_*F, with the perfection half absent from the library altogether. WHAT IS PROVED here: the transport of the conclusion across those identifications, using derivedFiberBetti_eq_of_iso and part (1) of Stacks 0BDI, AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti_derivedPullback”.

> The formation of `β_i` commutes with arbitrary base change: for a cartesian square whose
> right-hand vertical morphism is `f : X ⟶ S` and whose base is changed along an arbitrary
> `g : S' ⟶ S`, the `i`-th Betti-number function of the family `(f', (g')^*ℱ)` is the pullback
> along `g` of the `i`-th Betti-number function of `(f, ℱ)`.

```lean
public theorem fibreBetti_baseChange {X S X' S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X) (F : X.Modules)
    (h : CohomologyAndBaseChange f F)
    (h' : CohomologyAndBaseChange f' ((Scheme.Modules.pullback g').obj F))
    (hbc : BaseChangeCompatible f g f' g' F) (i : ℤ) :
    fibreBetti f' ((Scheme.Modules.pullback g').obj F) i = fibreBetti f F i ∘ g.base
```

**`AlgebraicGeometry.FibreBetti.upperSemicontinuous_fibreBetti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbers.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbers.lean#L215). The attribute's comment: “part (2): the Betti functions beta_i of the fibres are upper semi-continuous, for beta_i the function fibreBetti and all four hypotheses of the source present as fields of IsFlatFamily. WHAT IS ASSUMED rather than proved: first the cohomology-and-base-change step, as the fields isPseudoCoherent and fibreBetti_eq of CohomologyAndBaseChange, which is the half of Stacks 0B91 this library does not carry (see the attribute on fibreBetti_baseChange and AlgebraicGeometry.ProperFlatBaseChange.isIso_tensorFlatBaseChangeMap_module in StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChange.lean line 334, tagged at line 309); and second part (2) of Stacks 0BDI for Rf_*F, which is NOT in the library -- the only @[stacks 0BDI] attributes in the library are on its base-change half -- and which is assumed here in its LOCAL form only, as upper semi-continuity of the derived-fibre Betti function of the derived pullback of Rf_*F to each affine open of S. The affine case of that input is available for an object of D(R) on PrimeSpectrum R as StacksDraft.Perfect.upperSemicontinuous_fibreBetti_of_isPseudoCoherent in StacksFrontier/Homology/Perfect/BettiSemicontinuity.lean line 395, but no bridge from it to AlgebraicGeometry.DerivedFibreBetti.derivedFiberBetti on Spec R exists in the library. WHAT IS PROVED here: the passage from that local form to upper semi-continuity on S, by the reduction AlgebraicGeometry.DerivedFibreBetti.upperSemicontinuous_derivedFiberBetti_of_openImmersions applied to the cover of S by its affine opens, and the transport of the conclusion to beta_i”.

> The Betti-number function `β_i` is upper semi-continuous, provided that for every affine
> open `U` of `S` the derived-fibre Betti function of the restriction of `Rf_*ℱ` to `U` is upper
> semi-continuous.

```lean
public theorem upperSemicontinuous_fibreBetti {X S : Scheme.{u}} (f : X ⟶ S) (F : X.Modules)
    (h : CohomologyAndBaseChange f F) (i : ℤ)
    (hloc : ∀ U : S.affineOpens, UpperSemicontinuous
      (DerivedFibreBetti.derivedFiberBetti U.1.toScheme
        ((derivedPullback U.1.ι.toLRSHom.toShHom).obj (totalDirectImage f F))
        (DerivedFibreBetti.isPseudoCoherent_derivedPullback U.1.ι (totalDirectImage f F)
          h.isPseudoCoherent) i)) :
    UpperSemicontinuous (fibreBetti f F i)
```

**`AlgebraicGeometry.FibreBetti.fibreBetti_baseChange_upperSemicontinuous_isLocallyConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbersCohomologyBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/FibreBettiNumbersCohomologyBaseChange.lean#L187). References: SGA 6 III (5.7), “(ii), special case”.

> **[Stacks, Tag 0BDN].** Let `f : X ⟶ S` be a proper morphism of finite presentation and let
> `ℱ` be an `𝒪_X`-module of finite presentation, flat over `S`. Fix `i ∈ ℤ` and let `β_i` be the
> function `s ↦ dim_{κ(s)} H^i(X_s, ℱ_s)` (`AlgebraicGeometry.FibreBetti.fibreBetti`). Then
>
> 1. the formation of `β_i` commutes with arbitrary base change: for every cartesian square with
>    `g : S' ⟶ S`, `f' : X' ⟶ S'` and `g' : X' ⟶ X`, the function `β_i` of `(f', (g')^*ℱ)` is
>    `β_i ∘ g`;
> 2. `β_i` is upper semi-continuous;
> 3. every level set `β_i⁻¹{n}` is locally constructible in `S`.
>
> The proof is the source's. By [Stacks, Tag 0B91], `β_i` is the derived-fibre Betti function of
> the perfect object `Rf_*ℱ` (`fibreBetti_eq_derivedFiberBetti`), so the three parts are parts (1),
> (2) and (3) of [Stacks, Tag 0BDI].

```lean
public theorem fibreBetti_baseChange_upperSemicontinuous_isLocallyConstructible
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f) [IsProper f] (F : X.Modules)
    [F.IsFinitePresentation] (hflat : IsFlatOver f.toLRSHom.toShHom F) (i : ℤ) :
    (∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X),
        IsPullback g' f' f g →
          fibreBetti f' ((Scheme.Modules.pullback g').obj F) i = fibreBetti f F i ∘ g.base) ∧
      UpperSemicontinuous (fibreBetti f F i) ∧
      ∀ n : ℕ, IsLocallyConstructible (fibreBetti f F i ⁻¹' {n})
```

## Tag 0B9T, a lemma

[Tag 0B9T](https://stacks.math.columbia.edu/tag/0B9T) in the Stacks Project.

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.isLocallyConstant_chiFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristic.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristic.lean#L187). The attribute's comment: “the local constancy conclusion, with the function in the derived-fibre form s |-> sum (-1)^i dim_k(s) H^i(Rf_*F tensor^L k(s)) that the source's proof passes to. Rf_*F is perfect by Tag 0B91 (2), proved as isPerfect_derivedPushforward_singleFunctor_of_isProper, and the conclusion is Tag 0BDJ at Rf_*F. The identification with s |-> chi(X_s, F_s) and the statement in that form are in ProperFlatFibreEulerCharacteristicUnconditional.lean (isLocallyConstant_fibreEulerCharacteristic). The base-change conclusion is chiFibre_baseChange”.

> **[Stacks, Tag 0B9T], the first conclusion.** For a proper morphism `f : X ⟶ S` of finite
> presentation and an `𝒪_X`-module `ℱ` of finite presentation, flat over `S`, the Euler
> characteristic of the derived fibres of `Rf_*ℱ` is a locally constant function on `S`.
>
> `Rf_*ℱ` is perfect by the perfection half of [Stacks, Tag 0B91] (2),
> `isPerfect_derivedPushforward_singleFunctor_of_isProper`, and this is [Stacks, Tag 0BDJ] at
> `Rf_*ℱ`.

```lean
public theorem isLocallyConstant_chiFibre
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f) (hproper : IsProper f)
    (F : X.Modules) (hfp : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    IsLocallyConstant (chiFibre f F
      (DerivedFibreBetti.isPseudoCoherent_of_isPerfect _
        (isPerfect_derivedPushforward_singleFunctor_of_isProper f hf hproper F hfp hflat)))
```

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.chiFibre_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristic.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristic.lean#L227). The attribute's comment: “the base-change conclusion ('formation of this function commutes with base change'), with the function in the derived-fibre form s |-> sum (-1)^i dim_k(s) H^i(Rf_*F tensor^L k(s)), for every cartesian square. The isomorphism Lg^*Rf_*F = Rf'_*(g')^*F is Tag 0B91 (2), proved as nonempty_derivedPullback_derivedPushforward_singleFunctor_iso; the conclusion is then Tag 0BDI summed over the degrees, chiDerivedFibre_derivedPullback, and invariance under isomorphism, chiDerivedFibre_congr. hpc and hpc' are the pseudo-coherence proofs the function is built from, and the equality holds for all of them. The statement for s |-> chi(X_s, F_s) itself is fibreEulerCharacteristic_baseChange in ProperFlatFibreEulerCharacteristicUnconditional.lean. The local constancy conclusion is isLocallyConstant_chiFibre”.

> **[Stacks, Tag 0B9T], the second conclusion.** Formation of the Euler characteristic of the
> derived fibres of `Rf_*ℱ` commutes with base change: for a cartesian square
>
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
>
> the function on `S'` attached to `f'` and `(g')^*ℱ` is the function on `S` attached to `f` and
> `ℱ`, composed with `g`.
>
> The base-change isomorphism `Lg^*Rf_*ℱ ≅ Rf'_*(g')^*ℱ` is the base-change half of
> [Stacks, Tag 0B91] (2), `nonempty_derivedPullback_derivedPushforward_singleFunctor_iso`; with it,
> this is the base-change clause of [Stacks, Tag 0BDI] summed over the degrees,
> `AlgebraicGeometry.DerivedFibreBetti.chiDerivedFibre_derivedPullback`, together with the
> invariance of the derived-fibre Euler characteristic under isomorphism. The function is defined
> from a proof of pseudo-coherence of each object, `hpc` and `hpc'`; the equality holds for every
> such proof.

```lean
public theorem chiFibre_baseChange
    {X S X' S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
    (hsq : IsPullback g' f' f g) (hf : FinitePresentation f) (hproper : IsProper f)
    (F : X.Modules) (hfp : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F)
    (hpc : RingedSpace.IsPseudoCoherent (X := S.toRingedSpace) (derivedPushforwardModule f F))
    (hpc' : RingedSpace.IsPseudoCoherent (X := S'.toRingedSpace)
      (derivedPushforwardModule f' ((Scheme.Modules.pullback g').obj F))) :
    chiFibre f' ((Scheme.Modules.pullback g').obj F) hpc' =
      chiFibre f F hpc ∘ g.base
```

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.isLocallyConstant_fibreEulerCharacteristic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristicUnconditional.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristicUnconditional.lean#L141). The attribute's comment: “local constancy of s |-> chi(X_s, F_s)”. References: EGA III (7.9.4), “special case”; EGA III (7.9.5), “special case”.

> For `f : X ⟶ S` proper and of finite presentation and `ℱ` an `𝒪_X`-module of finite
> presentation, flat over `S`, the function `s ↦ χ(X_s, ℱ_s)` is locally constant on `S`.

```lean
theorem isLocallyConstant_fibreEulerCharacteristic {X S : Scheme.{u}} (f : X ⟶ S)
    (hf : FinitePresentation f) [IsProper f] (F : X.Modules) (hF : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    IsLocallyConstant (fibreEulerCharacteristic f F)
```

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.fibreEulerCharacteristic_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristicUnconditional.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristicUnconditional.lean#L155). The attribute's comment: “formation of s |-> chi(X_s, F_s) commutes with base change”. References: EGA III (7.9.7), “special case”.

> Formation of `s ↦ χ(X_s, ℱ_s)` commutes with base change: for a cartesian square with
> `g : S' ⟶ S`, the function attached to the base change `f' : X' ⟶ S'` and `(g')^*ℱ` is the
> function attached to `f` and `ℱ`, composed with `g`.

```lean
theorem fibreEulerCharacteristic_baseChange {X S X' S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S)
    (f' : X' ⟶ S') (g' : X' ⟶ X) (hsq : IsPullback g' f' f g) (hf : FinitePresentation f)
    [IsProper f] (F : X.Modules) (hF : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    fibreEulerCharacteristic f' ((Scheme.Modules.pullback g').obj F) =
      fibreEulerCharacteristic f F ∘ g.base
```

## Tag 0B9S, a lemma

[Tag 0B9S](https://stacks.math.columbia.edu/tag/0B9S) in the Stacks Project.

**`AlgebraicGeometry.ProperFlatRankOpen.factorsThrough_rankOpen_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpen.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpen.lean#L240). The attribute's comment: “for an open immersion T --> S only, and with rank r : N; nothing is assumed -- the base-change input is proved here as openImmersionBaseChangeDerivedPushforward from Tag 08FE. See the declaration docstring”.

> **[Stacks, Tag 0B9S], the characterising property of the open subscheme, for an open immersion
> of the base.** Let `f : X ⟶ S` be proper of finite presentation, let `ℱ` be an `𝒪_X`-module of
> finite presentation, flat over `S`, and fix `i` and `r`. An open immersion `g : T ⟶ S` factors
> through `rankOpen f ℱ i r` exactly when `Rf_{T,*}ℱ_T` is isomorphic to a finite locally free module
> of rank `r` placed in degree `i`.
>
> This is [Stacks, Tag 0BDK] at `Rf_*ℱ`, together with the base change of
> `openImmersionBaseChangeDerivedPushforward`.
>
> **Nothing is assumed.** The base-change input — the half of [Stacks, Tag 0B91] clause (2) which
> identifies the restriction of `Rf_*ℱ` along `g` with `Rf_{T,*}(g')^*ℱ` — is proved here, as
> `openImmersionBaseChangeDerivedPushforward`, from [Stacks, Tag 08FE]: derived direct image
> commutes with restriction to an open of the base, which is available precisely because `g` is an
> open immersion. So neither the tensor form of Tag 0B91 nor the unit coherence of
> [Stacks, Tag 079U] is involved. The *perfectness* half of Tag 0B91 is likewise not needed:
> neither `singleDegreeRankOpen` nor its universal property for open immersions uses it.
>
> **Two scope restrictions**, neither a carried hypothesis. First, the characterising property is
> delivered only for an open immersion `T ⟶ S`, not for an arbitrary morphism as the source states
> it: the universal property of the open subscheme of [Stacks, Tag 0BDK] is available in this
> library only for open immersions, as
> `AlgebraicGeometry.Scheme.Modules.factorsThrough_singleDegreeRankOpen_iff`, the description along
> an arbitrary morphism needing the pointwise description of that open through the Betti numbers of
> the derived fibres, which uses perfectness. Second, the rank `r` is a natural number where the
> source says `i, r ∈ ℤ`; this follows `singleDegreeRankOpen`, and for a negative `r` the open the
> source asserts is empty and the statement vacuous.

```lean
public theorem factorsThrough_rankOpen_iff
    (f : X ⟶ S) (hf : FinitePresentation f) (hproper : IsProper f)
    (F : X.Modules) (hfp : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (i : ℤ) (r : ℕ)
    {T XT : Scheme.{u}} (g : T ⟶ S) [IsOpenImmersion g] (fT : XT ⟶ T) (g' : XT ⟶ X)
    (hsq : IsPullback g' fT f g) :
    (∃ h : T ⟶ (rankOpen f F i r).toScheme, h ≫ (rankOpen f F i r).ι = g) ↔
      ∃ M : T.Modules,
        AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} M r ∧
          Nonempty (derivedPushforwardModule fT ((Scheme.Modules.pullback g').obj F) ≅
            (DerivedCategory.singleFunctor T.Modules i).obj M)
```

**`AlgebraicGeometry.ProperFlatRankOpen.exists_opens_factorsThrough_iff_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpenBaseChange.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpenBaseChange.lean#L207).

> **[Stacks, Tag 0B9S].** Let `f : X ⟶ S` be a proper morphism of finite presentation, let `ℱ`
> be an `𝒪_X`-module of finite presentation, flat over `S`, and fix `i, r ∈ ℤ`. Then there exists an
> open subscheme `U ⊆ S` with the following property: a morphism `g : T ⟶ S` factors through `U`
> if and only if `Rf_{T,*}ℱ_T` is isomorphic to a finite locally free module of rank `r` placed in
> degree `i`. Here, for any cartesian square
>
> ```
> X_T --g'--> X
>  |          |
> f_T         f
>  v          v
>  T  --g---> S
> ```
>
> `ℱ_T = (g')^*ℱ` and `Rf_{T,*}ℱ_T` is the derived direct image of `ℱ_T` placed in degree `0`; the
> property holds for every such square.
>
> For `r ≥ 0` the open subscheme is `rankOpen f ℱ i r` and the property is
> `factorsThrough_rankOpen_iff_baseChange`. For `r < 0` it is `∅`: both sides say that `T` is
> empty, by `factorsThrough_bot_iff` and `isEmpty_of_isFiniteLocallyFreeOfIntRank`, and on an empty
> `T` the case of rank `0` supplies the module.

```lean
public theorem exists_opens_factorsThrough_iff_derivedPushforward
    (f : X ⟶ S) (hf : FinitePresentation f) (hproper : IsProper f)
    (F : X.Modules) (hfp : F.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (i r : ℤ) :
    ∃ U : S.Opens, ∀ {T XT : Scheme.{u}} (g : T ⟶ S) (fT : XT ⟶ T) (g' : XT ⟶ X),
      IsPullback g' fT f g →
        ((∃ h : T ⟶ U.toScheme, h ≫ U.ι = g) ↔
          ∃ M : T.Modules, IsFiniteLocallyFreeOfIntRank M r ∧
            Nonempty (derivedPushforwardModule fT ((Scheme.Modules.pullback g').obj F) ≅
              (DerivedCategory.singleFunctor T.Modules i).obj M))
```

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.exists_opens_factorsThrough_iff_hasDerivedPushforwardRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpenUnconditional.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatRankOpenUnconditional.lean#L50). The attribute's comment: “the rank r is a natural number: no module is locally free of negative rank, so for r < 0 the source's open is empty”.

> **[Stacks, Tag 0B9S].** Let `π : Y ⟶ T` be proper and of finite presentation, `ℱ` an
> `𝒪_Y`-module of finite presentation flat over `T`, `i` an integer and `r` a natural number. There
> is an open `U ⊆ T` such that a morphism `h : T' ⟶ T` factors through `U` exactly when
> `Rπ'_*(h'^*ℱ)` is a finite locally free `𝒪_{T'}`-module of rank `r` placed in degree `i`, for the
> base change `π' : Y' ⟶ T'` of `π` along `h` (any cartesian square).

```lean
theorem exists_opens_factorsThrough_iff_hasDerivedPushforwardRank {Y T : Scheme.{u}}
    (π : Y ⟶ T) (hfp : FinitePresentation π) [IsProper π] (F : Y.Modules)
    (hF : F.IsFinitePresentation) (hflat : IsFlatOver π.toLRSHom.toShHom F) (i : ℤ) (r : ℕ) :
    ∃ U : T.Opens, ∀ {Y' T' : Scheme.{u}} (h : T' ⟶ T) (π' : Y' ⟶ T') (h' : Y' ⟶ Y),
      IsPullback h' π' π h →
      ((∃ g : T' ⟶ U.toScheme, g ≫ U.ι = h) ↔
        HasDerivedPushforwardRank π' ((Scheme.Modules.pullback h').obj F) i r)
```

## Tag 0D4E, a lemma

[Tag 0D4E](https://stacks.math.columbia.edu/tag/0D4E) in the Stacks Project.

**`Stacks.AlgebraicGeometry.VanishingHigherDirectImages.isFiniteLocallyFree_pushforward_and_isIso_baseChange_of_isZero_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/VanishingHigherDirectImagesLocallyFree.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/VanishingHigherDirectImagesLocallyFree.lean#L85). The attribute's comment: “both conclusions: f_*F is finite locally free, and for every cartesian square the canonical comparison g^*f_*F --> f'_*(g')^*F (baseChangeNatTrans, the mate of the two pullback-pushforward adjunctions) is an isomorphism, which is the meaning the source's proof gives to `commutes with arbitrary base change`”. References: EGA III (7.9.10), “partial”; SGA 6 III (5.7), “(iii), special case”.

> **[Stacks, Tag 0D4E].** Let `f : X ⟶ S` be a morphism of schemes of finite presentation and
> let `ℱ` be an `𝒪_X`-module of finite presentation, flat over `S`, whose support is proper over
> `S`. If `R ⁱ f_* ℱ = 0` for all `i > 0`, then
>
> 1. `f_* ℱ` is a finite locally free `𝒪_S`-module, and
> 2. the formation of `f_* ℱ` commutes with arbitrary base change: for every cartesian square
>    with `g' : X' ⟶ X`, `f' : X' ⟶ S'` and `g : S' ⟶ S`, the canonical comparison map
>    `g^* f_* ℱ ⟶ f'_* (g')^* ℱ` (`Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans`)
>    is an isomorphism.
>
> The first conclusion is `isFiniteLocallyFree_pushforward_of_isZero_higherDirectImage`, the second
> `isIso_baseChangeNatTrans_app_of_vanishing`.

```lean
public theorem isFiniteLocallyFree_pushforward_and_isIso_baseChange_of_isZero_higherDirectImage
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f) (F : X.Modules)
    [F.IsFinitePresentation] (hflat : IsFlatOver f.toLRSHom.toShHom F)
    (hsupp : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      ∃ Z : Closeds X, IsProperOver f Z ∧ SheafOfModules.supp F ⊆ (Z : Set X))
    (hvanish : ∀ i : ℤ, 0 < i →
      IsZero (((Scheme.Modules.pushforward f).rightDerivedPlus i).obj F)) :
    _root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (R := S.ringCatSheaf) ((Scheme.Modules.pushforward f).obj F) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (hsq : IsPullback g' f' f g),
        IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app F)
```

## Tag 0E62, a lemma

[Tag 0E62](https://stacks.math.columbia.edu/tag/0E62) in the Stacks Project.

**`StacksDraft.Perfect.UnitSplitting.exists_localization_iso_single_homology_biprod_truncGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/AffineLocalSplitting.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/AffineLocalSplitting.lean#L187). The attribute's comment: “PART (b) ONLY, and only in its AFFINE-LOCAL ALGEBRAIC FORM: the statement is about an abstract pseudo-coherent object K of D(R) for a commutative ring R, standing for E = Rf_*O_X restricted to an affine open of S, and NOTHING HERE IDENTIFIES K WITH A DERIVED DIRECT IMAGE. The source's proof has four steps and the first, geometric one is NOT performed: cohomology and base change (Tag 0B91), which gives that E is perfect and that its formation commutes with arbitrary base change, is not invoked at all. What is assumed of K instead is exactly what the source's remaining three steps use of E: pseudo-coherence (the part of perfectness Tag 0A1U asks for); the vanishing of H^i(K) for i < 0 and of H^{-1}(K tensor^L k(p)), which are the two consequences of `E has tor amplitude in [0, infinity)` that the source uses, taken as two separate vanishing statements because StacksDraft.TorAmplitude.HasTorAmplitude carries the derived tensor product, its comparison and its universal property as explicit parameters and nothing stronger is needed; and surjectivity of H^0(K) tensor k(p) --> H^0(K tensor^L k(p)) at p, which is the source's second step. WITHIN part (b), THE FIRST SUMMAND IS NOT IDENTIFIED WITH O_S. What is delivered is the splitting K_g = H^0(K)_g[0] (+) tau_{>=1}K_g after localizing away from a single element g outside p, with tau_{>=1}K_g perfect of tor amplitude in [1, infinity) -- the source's step 3, Tag 0A1U -- and with H^0(K)_g FINITE FREE over R_g, which is the half of the source's step 4 that Tags 0658 and 00NX supply. The remaining half of step 4, that the unit O_S --> H^0(E) is an isomorphism, is NOT carried, and that is also exactly PART (a) of this tag, `f_*O_X = O_S and this holds after any base change`, WHICH IS NOT DELIVERED ANYWHERE in this file: carrying it needs the map H^0(epsilon) : R --> H^0(K) induced by a unit epsilon : R[0] --> K, which this statement does not take as data, and then the transport of the fibrewise bijectivity of that map from the primes of R to the primes of R_g so that the isomorphism locus of Algebra Tag 00O0 (3) can be read at the prime of R_g above p; that locus result IS carried in this library, as Stacks.FiniteProjective.MapLocus.isOpen_isoLocus_and_localized, but neither the induced map nor the transport is written here. The statement is algebraic rather than geometric because Tags 0A1U and 0A1V are carried in this library only over a commutative ring, as StacksDraft.Perfect results about D(R) in StacksFrontier/Homology/Perfect/FibreCriterion.lean -- no declaration anywhere in the library carries either tag for the derived category of modules on a scheme -- so the geometric statement would need in addition the affine-local comparison of D(O_S)|_U with D(R) for U = Spec R an affine open, and the identification of H^0(E tensor^L k(s)) with H^0(X_s, O_{X_s}), which the module documentation of StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFibreEulerCharacteristic.lean records as absent from this library. What is PROVED here, assuming nothing beyond the stated hypotheses on K: that the degree -1 base-change map is surjective because its target vanishes, so that Tag 0A1V applies at degree 0; that the vanishing of H^i(K) below degree 0 places the localization K_g in degrees >= 0 and so kills the summand tau_{<=-1}K_g of the three-term decomposition of Tag 0A1V; and the assembly of the remaining two summands into the two-term splitting the source states”.

> **The affine-local algebraic form of part (b) of [Stacks, Tag 0E62].**
>
> Let `R` be a commutative ring, `p ⊂ R` a prime, and `K` a pseudo-coherent object of `D(R)` --
> standing for `E = Rf_*𝒪_X` restricted to an affine open of `S`. Assume
>
> * `Hⁱ(K) = 0` for `i < 0` and `H^{-1}(K ⊗_R^L κ(p)) = 0`, and
> * `H⁰(K) ⊗_R κ(p) → H⁰(K ⊗_R^L κ(p))` is surjective.
>
> Then there is `g ∈ R`, `g ∉ p`, such that over `R_g` the localization `K_g = K ⊗_R R_g` splits as
>
> `K_g ≅ H⁰(K)_g[0] ⊕ τ_{≥1}K_g`,
>
> where `H⁰(K)_g` is a finite free `R_g`-module and `τ_{≥1}K_g` is a perfect object of `D(R_g)` of
> Tor amplitude in `[1, ∞)`, recorded by a bounded complex of finite projective `R_g`-modules
> concentrated in degrees `≥ 1` representing it whose termwise tensor products have no cohomology
> below degree `1`.

```lean
theorem exists_localization_iso_single_homology_biprod_truncGE
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hneg : ∀ i : ℤ, i < 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K))
    (hfib : FibreCohomologyVanishes.{u, v} p K (-1))
    (hbase : CohomologyBaseChangeSurjective.{u, v} p K 0) :
    ∃ g : R, g ∉ p ∧
      let Rg := Localization.Away g
      let Kg := (PseudoCoherence.localizationAwayFunctorAux.{u, v} g).obj K
      let upper := (DerivedCategory.TStructure.t.truncGE 1).obj Kg
      let H0g := (ModuleCat.extendScalars (algebraMap R Rg)).obj
        ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) 0).obj K)
      Module.Finite Rg H0g ∧ Module.Free Rg H0g ∧ IsPerfect upper ∧
        (∃ (P : CochainComplex (ModuleCat.{max u v} Rg) ℤ) (b : ℤ),
          P.IsStrictlyGE 1 ∧ P.IsStrictlyLE b ∧
            (∀ j : ℤ, Module.Finite Rg (P.X j)) ∧
            (∀ j : ℤ, Module.Projective Rg (P.X j)) ∧
            Nonempty (upper ≅ DerivedCategory.Q.obj P) ∧
            ∀ (M : ModuleCat.{max u v} Rg) (j : ℤ), j < 1 →
              IsZero ((TorAmplitude.tensorComplex P M).homology j)) ∧
        Nonempty (Kg ≅
          (DerivedCategory.singleFunctor (ModuleCat.{max u v} Rg) 0).obj H0g ⊞ upper)
```

**`Stacks.AlgebraicGeometry.ProperFlatStructureSheafSplitting.properFlat_structureSheaf_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/StructureSheafSplitting.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/StructureSheafSplitting.lean#L499).

> **[Stacks, Tag 0E62].** Let `f : X ⟶ S` be a morphism of schemes which is proper, flat and of
> finite presentation, and assume that for every `s ∈ S` the canonical map
> `κ(s) → H⁰(X_s, 𝒪_{X_s})` is bijective. Then
>
> * (a) `f_*𝒪_X = 𝒪_S`, and this holds after any base change: for every cartesian square
>   `X' = X ×_S S'` the comparison `𝒪_{S'} ⟶ f'_*𝒪_{X'}` of sheaves of rings is an isomorphism;
> * (b) locally on `S` we have `Rf_*𝒪_X ≅ 𝒪_S ⊕ P` in `D(𝒪_S)` with `P` perfect of Tor amplitude
>   in `[1, ∞)`: every point of `S` lies in the image of an open immersion `ι : V ⟶ S` over which
>   the restriction of `Rf_*𝒪_X` is isomorphic to `𝒪_V ⊕ P` with `P` a perfect object of `D(𝒪_V)`
>   of Tor amplitude in `[1, b]` for some `b`.

```lean
theorem properFlat_structureSheaf_splitting {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [Flat f]
    (hfp : FinitePresentation f)
    (hfib : ∀ s : S, Function.Bijective ((Scheme.ΓSpecIso (S.residueField s)).inv ≫
      (f.fiberToSpecResidueField s).appTop)) :
    (IsIso f.c ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X),
        IsPullback g' f' f g → IsIso f'.c) ∧
    ∀ s : S, ∃ (V : Scheme.{u}) (ι : V ⟶ S) (_ : IsOpenImmersion ι)
      (P : DerivedCategory V.Modules),
      s ∈ Set.range ι ∧ RingedSpace.IsPerfect (X := V.toRingedSpace) P ∧
      (∃ b : ℤ, Stacks.Cohomology.TorAmplitude.HasTorAmplitude V.toRingedSpace P 1 b) ∧
      Nonempty ((Scheme.Modules.restrictFunctor ι).mapDerivedCategory.obj
          ((derivedPushforward f.toLRSHom.toShHom).obj
            ((DerivedCategory.singleFunctor X.Modules 0).obj (Scheme.unitModule X))) ≅
        ((DerivedCategory.singleFunctor V.Modules 0).obj (Scheme.unitModule V) ⊞ P :
          DerivedCategory V.Modules))
```

## Tag 0E0L, a lemma

[Tag 0E0L](https://stacks.math.columbia.edu/tag/0E0L) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperFlatStructureSheaf.isIso_c_and_isIso_c_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/GeometricFibresDirectImage.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatFamily/GeometricFibresDirectImage.lean#L64). The attribute's comment: “both conclusions: f_*O_X = O_S, as invertibility of the comparison f.c of sheaves of rings, and the same for every base change, stated for every cartesian square over S.”.

> **Stacks Project, Tag 0E0L.** Let `f : X ⟶ S` be proper, flat and of finite presentation, with
> geometric fibres reduced and connected. Then `f_*𝒪_X = 𝒪_S`, i.e. `f.c : 𝒪_S ⟶ f_*𝒪_X` is
> invertible, and this holds after any base change: for every cartesian square
> ```
> X' --g'--> X
> |f'        |f
> v          v
> S' --g---> S
> ```
> the comparison `f'.c : 𝒪_{S'} ⟶ f'_*𝒪_{X'}` is invertible.
>
> Finite presentation is `LocallyOfFinitePresentation f` together with quasi-compactness and
> quasi-separatedness, which properness supplies. The geometric fibres being reduced and connected
> is `GeometricallyReduced f` and `GeometricallyConnected f`.

```lean
theorem isIso_c_and_isIso_c_of_isPullback [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] [GeometricallyReduced f] [GeometricallyConnected f] :
    IsIso f.c ∧ ∀ {X' S' : Scheme.{u}} {g : S' ⟶ S} {g' : X' ⟶ X} {f' : X' ⟶ S'},
      IsPullback g' f' f g → IsIso f'.c
```

## Tag 0G7X, a lemma

[Tag 0G7X](https://stacks.math.columbia.edu/tag/0G7X) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Fibres.extendsOverNeighbourhood_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Fibres/IdempotentExtensionApproximation.lean, line 857](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Fibres/IdempotentExtensionApproximation.lean#L857).

> **[Stacks, Tag 0G7X].**  An idempotent global function on a fibre of a proper morphism is the
> restriction of a section of the structure sheaf over the inverse image of an open neighbourhood
> of the base point;  equivalently, it lies in the image of the stalk `(f_* 𝒪_X)_s`.  Nothing is
> assumed on the base:  its locally Noetherian case is
> `Stacks.FormalFunctions.extendsOverNeighbourhood_of_isLocallyNoetherian`, and the general case
> follows from it by the approximation argument above.

```lean
public theorem extendsOverNeighbourhood_of_isProper {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f]
    (s : S) (e : Γ(f.fiber s, ⊤)) (he : IsIdempotentElem e) :
    ExtendsOverNeighbourhood f s e
```

## Tag 0G7Y, a lemma

[Tag 0G7Y](https://stacks.math.columbia.edu/tag/0G7Y) in the Stacks Project.

**`StacksDraft.Perfect.GeomReducedFibre.exists_open_finiteEtale_and_derivedPushforward_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/GeomReducedFibre/Main.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/GeomReducedFibre/Main.lean#L115).

> **[Stacks, Tag 0G7Y].** Let `f : X ⟶ S` be proper, flat and of finite presentation and let
> `s ∈ S` be a point whose fibre `X_s` is geometrically reduced. Then there is an affine open
> neighbourhood `U` of `s` such that
>
> * `f_*𝒪_X` is a finite etale `𝒪_S`-algebra over `U`: for every affine open `V ⊆ U` the ring
>   map `Γ(S, V) → Γ(X, f⁻¹V)` is finite and etale;
> * `Rf_*𝒪_X ≅ f_*𝒪_X ⊕ P` in `D(𝒪_U)` with `P` perfect of Tor amplitude in `[1, b]` for some `b`
>   (so in `[1, ∞)`), at every model of the derived categories.

```lean
theorem exists_open_finiteEtale_and_derivedPushforward_splitting {X S : Scheme.{u}} (f : X ⟶ S)
    (hfp : FinitePresentation f) [IsProper f] [Flat f] (s : S)
    (hred : GeometricallyReduced (f.fiberToSpecResidueField s)) :
    ∃ U : S.Opens, s ∈ U ∧ IsAffineOpen U ∧
      (∀ V : S.affineOpens, V.1 ≤ U →
        letI : Algebra Γ(S, V.1) Γ(X, f ⁻¹ᵁ V.1) := (f.app V.1).hom.toAlgebra
        Module.Finite Γ(S, V.1) Γ(X, f ⁻¹ᵁ V.1) ∧ Algebra.Etale Γ(S, V.1) Γ(X, f ⁻¹ᵁ V.1)) ∧
      ∃ b : ℤ, 1 ≤ b ∧ ∀ (hX : HasDerivedCategory.{w} (f ⁻¹ᵁ U).toScheme.Modules)
        (hU : HasDerivedCategory.{w} U.toScheme.Modules),
        letI := hX
        letI := hU
        letI : HasDerivedCategory.{w}
          (SheafOfModules.{u} (structureSheafRing (f ⁻¹ᵁ U).toScheme.toSheafedSpace)) := hX
        letI : HasDerivedCategory.{w}
          (SheafOfModules.{u} (structureSheafRing U.toScheme.toSheafedSpace)) := hU
        ∃ P : DerivedCategory U.toScheme.Modules,
          @Stacks.Cohomology.PerfectComplexes.IsPerfect U.toScheme.toRingedSpace hU P ∧
          @Stacks.Cohomology.TorAmplitude.HasTorAmplitude U.toScheme.toRingedSpace hU P 1 b ∧
          Nonempty ((DerivedCategory.singleFunctor U.toScheme.Modules 0).obj
              ((Scheme.Modules.pushforward (f ∣_ U)).obj
                (Scheme.unitModule (f ⁻¹ᵁ U).toScheme)) ⊞ P ≅
            (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward
              (f ∣_ U).toLRSHom.toShHom).obj
              ((DerivedCategory.singleFunctor (f ⁻¹ᵁ U).toScheme.Modules 0).obj
                (Scheme.unitModule (f ⁻¹ᵁ U).toScheme)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.32, Tag 0BDM](https://stacks.math.columbia.edu/tag/0BDM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
