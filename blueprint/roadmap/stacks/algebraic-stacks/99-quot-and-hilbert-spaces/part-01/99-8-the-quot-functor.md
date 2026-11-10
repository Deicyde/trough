---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuotSituation, AlgebraicGeometry.Space.QuotSituation.properlySupportedQuotients, AlgebraicGeometry.Space.QuotSituation.isProperlySupportedOver_modulePullback_quotientModule, AlgebraicGeometry.Space.QuotSituation.quotientPullback_mem_properlySupportedQuotients, AlgebraicGeometry.Space.QuotSituation.quotFunctor, AlgebraicGeometry.Space.QuotFamilyOver, AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf, AlgebraicGeometry.Space.QuotSituation.quotSitePresheafToBase
statement: formalized
proof: formalized
---

# 99.8 The Quot functor

Section 99.8 of the Stacks Project, [Tag 09TQ](https://stacks.math.columbia.edu/tag/09TQ). 5 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09TR, a situation

[Tag 09TR](https://stacks.math.columbia.edu/tag/09TR) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean#L75). The attribute's comment: “the standing data”.

> A quotient situation — a morphism `f : X ⟶ B` of algebraic spaces over `S` together with a
> quasi-coherent `𝒪_X`-module `F` — whose morphism is moreover of finite presentation.

```lean
structure QuotSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    extends QuotientSituation B S hS
```

**`AlgebraicGeometry.Space.QuotSituation.properlySupportedQuotients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean#L128). The attribute's comment: “the set of quotients”.

> The set `Quot_{F/X/B}(T)` of quotients of `F_T` which are quasi-coherent, of finite
> presentation, flat over the test scheme `T` and with support proper over `T`, each recorded by
> its kernel `K`, the quotient being `F_T / K`.

```lean
def properlySupportedQuotients (T : SchemesOver D.Y) :
    Set (Subobject (D.baseChangeModule T))
```

**`AlgebraicGeometry.Space.QuotSituation.isProperlySupportedOver_modulePullback_quotientModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctor.lean#L150). The attribute's comment: “the subfunctor of the finitely presented quotients”.

> For a quotient in `Quot_{F/X/B}(T)` and a morphism `U ⟶ T` of test schemes, the inverse
> image of that quotient along `X_U ⟶ X_T` again has support proper over the test scheme.

```lean
theorem isProperlySupportedOver_modulePullback_quotientModule {U T : SchemesOver D.Y}
    (h : U ⟶ T) {K : Subobject (D.baseChangeModule T)}
    (hK : K ∈ D.properlySupportedQuotients T) :
    D.IsProperlySupportedOver U
      ((modulePullback B S hS (D.relativeMap h)).obj (D.quotientModule T K))
```

**`AlgebraicGeometry.Space.QuotSituation.quotientPullback_mem_properlySupportedQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean#L102). The attribute's comment: “stability of the four conditions under pullback of quotients”.

> The pullback of a quotient in `Quot_{F/X/B}(T)` along a morphism `T' ⟶ T` of test schemes
> lies in `Quot_{F/X/B}(T')`.

```lean
theorem quotientPullback_mem_properlySupportedQuotients
    {T' T : SchemesOver D.Y} (h : T' ⟶ T)
    (K : Subobject (D.baseChangeModule T)) (hK : K ∈ D.properlySupportedQuotients T) :
    D.quotientPullback h K ∈ D.properlySupportedQuotients T'
```

**`AlgebraicGeometry.Space.QuotSituation.quotFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean#L119). The attribute's comment: “the Quot functor on the test schemes over the base”.

> The Quot functor `Quot_{F/X/B} : (Sch/B)ᵒᵖ ⥤ Sets` of `F/X/B`: its value at
> a test scheme `T` over `B` is the set `Quot_{F/X/B}(T)` of quotients of `F_T` that are
> quasi-coherent, of finite presentation, flat over `T` and with support proper over `T`, and its
> action on a morphism of test schemes is pullback of quotients.

```lean
def quotFunctor : (SchemesOver D.Y)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.QuotFamilyOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean#L160). The attribute's comment: “quotients over the schemes of the site”.

> A quotient classified by the Quot functor over a scheme of the big fppf site
> rather than over a test scheme of `B`: the morphism to `B` the quotient lies over, together with a
> quotient over the resulting test scheme.

```lean
structure QuotFamilyOver (D : QuotSituation B S hS) (T : BigFppfOver B S hS)
```

**`AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean#L245). The attribute's comment: “the presheaf on the schemes of the site”.

> The Quot functor read as a presheaf on the schemes of the big fppf site: a
> section over `T` is a morphism `T ⟶ B` together with a quotient of `F_T` for the resulting test
> scheme, and restriction pulls back both.

```lean
def quotSitePresheaf : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.QuotSituation.quotSitePresheafToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPresheaf.lean#L254). The attribute's comment: “the canonical morphism to the base”.

> The canonical morphism from the Quot presheaf to the universe lift of the base algebraic space
> `B`, sending a quotient to the morphism to `B` it lies over.

```lean
def quotSitePresheafToBase :
    D.quotSitePresheaf ⟶ D.Y.obj ⋙ uliftFunctor.{u + 1, u}
```

## Tag 09TT, a lemma

[Tag 09TT](https://stacks.math.columbia.edu/tag/09TT) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.quotFunctor_isSheaf_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean#L233).

> **Stacks 09TT.**  In Situation 09TR, the Quot functor `Quot_{F/X/B} : (Sch/B)ᵒᵖ ⥤ Sets`
> satisfies the sheaf property for the fpqc topology: for every fpqc covering `{T i ⟶ T}` of
> schemes over `B`, a family of quotients of the `F_{T i}` — quasi-coherent, of finite
> presentation, flat over `T i` and with support proper over `T i` — which agree on the overlaps
> comes from a unique such quotient of `F_T`.
>
> The topology is `AlgebraicGeometry.Space.fpqcTopology` on the test schemes over `B`.  The
> proof is the source's: the functor of finitely presented quotients is an fpqc sheaf
> (Stacks 082P, `…finitePresentationQuotientsFunctor_isSheaf_fpqcTopology`), and the condition of
> proper support descends along fpqc coverings of the test scheme
> (`AlgebraicGeometry.Space.QuotSituation.mem_properlySupportedQuotients_of_isFpqcCovering`).

```lean
theorem quotFunctor_isSheaf_fpqcTopology :
    Presheaf.IsSheaf (fpqcTopology D.Y) D.quotFunctor
```

**`AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf_isSheaf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean#L552). The attribute's comment: “the Quot functor read on the schemes over S together with its morphism to B”.

> **Stacks 09TT, for the presheaf of pairs on the big fppf site of `S`.**  The source also
> reads `Quot_{F/X/B}` as a functor on the schemes over `S` with a morphism to `B`: its value at
> `T` is the set of pairs `(h : T ⟶ B, Q)` with `Q` a member of `Quot_{F/X/B}(T)` for the test
> scheme `(T, h)`.  That presheaf, `AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf`,
> satisfies the sheaf property for the fpqc topology of the big fppf site of `S`.

```lean
theorem quotSitePresheaf_isSheaf_fpqc :
    Presheaf.IsSheaf ((Scheme.fpqcPrecoverage.comap (BigFppfOver.toScheme B S hS)).toGrothendieck)
      D.quotSitePresheaf
```

**`AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf_isSheaf`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorFpqcSheaf.lean#L589). The attribute's comment: “the fppf sheaf property of the Quot presheaf of pairs on the big fppf site over S, unconditionally; it is the consequence, for the coarser fppf topology, of the source's fpqc statement, which is `quotSitePresheaf_isSheaf_fpqc`. This name is an alias of `quotSitePresheaf_isSheaf_fppf`.”.

> **Stacks 09TT.**  The Quot functor `Quot_{F/X/B}` of Stacks 09TR, read as a presheaf on the
> schemes of the big fppf site of `S`, satisfies the sheaf condition for the fppf topology of that
> site: a compatible family, for an fppf covering of a scheme `T` of the site, of pairs consisting
> of a morphism to `B` and a quotient of the corresponding pullback of `F` which is quasi-coherent,
> of finite presentation, flat over the member and with support proper over it, comes from a
> unique such pair over `T`.
>
> This name is an alias of `AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf_isSheaf_fppf`,
> which has no hypothesis: the separatedness and glueing of quotients along a covering of a test
> scheme are the theorems
> `AlgebraicGeometry.Space.QuotSituation.quotientsSeparatedForCoverings_properlySupportedQuotients`
> and `…quotientsGlueAlongCoverings_properlySupportedQuotients`, and the sheaf property is
> deduced from the fpqc one, `AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf_isSheaf_fpqc`,
> as the fppf topology of the site is coarser than its fpqc topology.

```lean
alias quotSitePresheaf_isSheaf
```

## Tag 0D3V, a lemma

[Tag 0D3V](https://stacks.math.columbia.edu/tag/0D3V) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.morEquivSpaceProperlySupportedQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPoints.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPoints.lean#L219). The attribute's comment: “RESTRICTED: the displayed identification, read as a bijection, only for an algebraic space T that is a scheme of the big fppf site; the general case needs the fullness and effectivity of quasi-coherent descent, which this development lacks”.

> **Stacks 0D3V for a representable algebraic space.**  The morphisms of sheaves on the big
> fppf site of `S` from a scheme `U` of the site into `Quot_{F/X/B}` are the pairs `(h, Q)`
> consisting of a morphism `h : U ⟶ B` of algebraic spaces and a quotient of `F_U` which is
> quasi-coherent, of finite presentation, flat over `U` and has support proper over `U`, where
> `F_U` is the pullback of `F` to `X ×_{B, h} U`.
>
> This is the source's displayed identification in the case where the algebraic space `T` is a
> scheme of the site, which is the base of the source's proof: that proof chooses a scheme `U`
> with a surjective étale morphism `U ⟶ T`, reads the transformation at it as a pair over `U`, and
> descends.  The identification here is the Yoneda lemma for the sheaf of Stacks 09TT, whose value
> at `U` is the set of those pairs; the sheaf of the algebraic space of `U` is lifted to the
> universe of the Quot presheaf, which adds and loses no morphism.  The general case is not
> covered; see the implementation notes for the precise obstruction.

```lean
def morEquivSpaceProperlySupportedQuotient (U : BigFppfOver B S hS) :
    (uliftYoneda.{u + 1}.obj U ⟶ D.quotSitePresheaf) ≃
      D.SpaceProperlySupportedQuotients ((schemeSpaceFunctor B S hS).obj U)
```

**`AlgebraicGeometry.Space.QuotSituation.morEquivSpaceProperlySupportedQuotientOfAlgebraicSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPointsAlgebraicSpace.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorPointsAlgebraicSpace.lean#L105). The attribute's comment: “the displayed identification, read as a bijection, for an arbitrary algebraic space T over S”.

> In Situation 09TR, let `T` be an algebraic space over `S`. The morphisms of sheaves on the
> big fppf site of `S` from `T` into `Quot_{F/X/B}` are in bijection with the pairs `(h, F_T ⟶ Q)`
> consisting of a morphism `h : T ⟶ B` of algebraic spaces and a quotient `Q` of the pullback
> `F_T` of `F` to the algebraic space `X ×_{B, h} T`, with `Q` quasi-coherent, of finite
> presentation, flat over `T` and with support proper over `T`.
>
> The left-hand side is the Quot presheaf `AlgebraicGeometry.Space.QuotSituation.quotSitePresheaf`,
> with the sheaf of `T` lifted to its universe. The inverse sends a pair to the transformation
> restricting it along the chart `t : V ⟶ T` of every section `t` of `T` over a scheme `V` of the
> site.

```lean
def morEquivSpaceProperlySupportedQuotientOfAlgebraicSpace (T : AlgebraicSpaces B S hS) :
    (T.obj ⋙ uliftFunctor.{u + 1, u} ⟶ D.quotSitePresheaf) ≃
      D.SpaceProperlySupportedQuotients T
```

## Tag 09TU, a proposition

[Tag 09TU](https://stacks.math.columbia.edu/tag/09TU) in the Stacks Project.

**`AlgebraicGeometry.Space.QuotSituation.exists_quotSitePresheafModel_of_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpace.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpace.lean#L254). The attribute's comment: “the size clause: a model of the Quot presheaf in the universe of the site”.

> **Stacks 09TU, the size clause.** Assume that over every scheme `T` of the big fppf site of
> `S` the set of pairs consisting of a morphism `T ⟶ B` and a quotient of `F_T` which is
> quasi-coherent, of finite presentation, flat over `T` and with support proper over `T` is small.
> Then the Quot presheaf of Stacks 09TR has a model in the universe of the site: a presheaf of
> `Type u` whose sections over every scheme of the site are exactly those pairs and whose canonical
> morphism to `B` is the one of Stacks 09TR.
>
> This is the clause of Stacks 09TU which makes its two geometric clauses statable — an algebraic
> space takes values in the universe of the site, whereas quotients are recorded by subobjects and
> so live one universe up — and it is the content the source leaves to its set-theoretic
> conventions. The two geometric clauses, algebraicity of the model and local finite presentation
> of its morphism to `B`, are not proved; by
> `AlgebraicGeometry.Space.QuotSitePresheafModel.isAlgebraicSpace_and_lfp_of_model` they hold for
> the model produced here exactly when they hold for any model at all.

```lean
theorem exists_quotSitePresheafModel_of_small
    (hsmall : ∀ T : BigFppfOver B S hS, Small.{u} (QuotFamilyOver D T)) :
    ∃ M : QuotSitePresheafModel D,
      (∀ T : (BigFppfOver B S hS)ᵒᵖ, Nonempty (M.presheaf.obj T ≃ QuotFamilyOver D T.unop)) ∧
        Functor.whiskerRight M.toBase uliftFunctor.{u + 1, u} =
          M.iso.hom ≫ D.quotSitePresheafToBase
```

**`AlgebraicGeometry.Space.QuotSituation.isAlgebraicSpace_and_isLocallyOfFinitePresentation_quot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpaceSeparated.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpaceSeparated.lean#L94). The attribute's comment: “both assertions, f of finite presentation and separated: Quot\_\{F/X/B} is an algebraic space for F étale-locally generated by fewer than μ sections with μ below the cutoff of the site (every F of finite type), and it is locally of finite presentation over B for F of finite presentation; for an arbitrary quasi-coherent F the first assertion is false on the size-bounded site (F free of rank the cutoff plus one over a separably closed field)”.

> **Stacks 09TU.** Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is of finite
> presentation (a field of the standing datum `D` of Situation 09TR) and separated, and let `F` be
> a quasi-coherent `𝒪_X`-module.
>
> 1. If `F` is étale-locally generated by fewer than `μ` sections for some `μ` below the cutoff of
>    the site (for instance if `F` is of finite type), then `Quot_{F/X/B}` is an algebraic space:
>    a model of it in the universe of the site exists, and every such model is an algebraic space.
> 2. If `F` is of finite presentation, then every model of `Quot_{F/X/B}` is an algebraic space whose
>    morphism to `B` is locally of finite presentation.
>
> Without the bound on generators in (1), the first assertion fails on the size-bounded site: for
> `F` free of rank the cutoff plus one over the spectrum of a separably closed field, the Quot
> functor has at least `2 ^ cutoff` points, an algebraic space of the site fewer than the cutoff.

```lean
theorem isAlgebraicSpace_and_isLocallyOfFinitePresentation_quot
    (hsep : IsSeparated B S hS D.f.hom) :
    ((∃ μ < B.cutoff, IsEtaleLocallyGeneratedBelow B S hS μ D.F) →
        Nonempty (QuotSitePresheafModel D) ∧
          ∀ N : QuotSitePresheafModel D, IsAlgebraicSpace B S hS N.presheaf) ∧
      (D.F.IsFinitePresentationOnSite →
        ∀ N : QuotSitePresheafModel D,
          IsAlgebraicSpace B S hS N.presheaf ∧ IsLocallyOfFinitePresentation B S hS N.toBase)
```

**`AlgebraicGeometry.Space.QuotSituation.isAlgebraicSpace_quot_of_isFiniteTypeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpaceSeparated.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotFunctorAlgebraicSpaceSeparated.lean#L112). The attribute's comment: “the first assertion for F of finite type”.

> **Stacks 09TU, the first assertion for `F` of finite type.** If `f` is of finite presentation
> and separated and `F` is of finite type, then every model of `Quot_{F/X/B}` in the universe of
> the site is an algebraic space.

```lean
theorem isAlgebraicSpace_quot_of_isFiniteTypeOnSite (hsep : IsSeparated B S hS D.f.hom)
    (hF : SheafOfModules.IsFiniteTypeOnSite D.F) (N : QuotSitePresheafModel D) :
    IsAlgebraicSpace B S hS N.presheaf
```

## Tag 0CZW, a remark

[Tag 0CZW](https://stacks.math.columbia.edu/tag/0CZW) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_and_isLocallyOfFinitePresentation_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAlgebraic.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAlgebraic.lean#L54). The attribute's comment: “Quot\_\{F/X/S} is an algebraic space locally of finite presentation over S, by Artin's axioms (Stacks 07Y1)”.

> **`Quot_{F/X/S}` is an algebraic space locally of finite presentation over `S`.** Let `S` be
> Noetherian with all local rings G-rings, `f : X ⟶ S` separated and of finite presentation, and `F`
> a quasi-coherent `𝒪_X`-module of finite presentation, flat over `S`. Then every model of
> `Quot_{F/X/S}` in the universe of the site is an algebraic space whose morphism to `S` is locally
> of finite presentation.

```lean
theorem isAlgebraicSpace_and_isLocallyOfFinitePresentation_quotOverBase
    [AlgebraicGeometry.IsNoetherian S] (hG : ∀ s : S, IsGRing (S.presheaf.stalk s))
    (hsep : IsSeparated B S hS f.hom) (hFfp : F.IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS X.2 f.hom F) :
    ∀ N : QuotSitePresheafModel (quotOverBase X f hf F hF),
      IsAlgebraicSpace B S hS N.presheaf ∧ IsLocallyOfFinitePresentation B S hS N.toBase
```

**`AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_diag_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean#L540). The attribute's comment: “the diagonal of Quot\_\{F/X/S} is representable by algebraic spaces”.

> **Stacks 0CZW, the diagonal.** In the situation of the remark, the diagonal
> `Quot_{F/X/S} ⟶ Quot_{F/X/S} × Quot_{F/X/S}` is representable (by closed immersions of
> schemes, hence by algebraic spaces): for two quotients `F_T ⟶ 𝒬ᵢ`, the locus of `T` over which
> they agree is a closed subscheme of `T`, by Stacks 083M (the remark's own argument, through the
> vanishing of `𝒦₁ ⟶ 𝒬₂` and of `𝒦₂ ⟶ 𝒬₁`).

```lean
theorem isRepresentableByAlgebraicSpaces_diag_quotOverBase :
    IsRepresentableByAlgebraicSpaces B S hS (diag (quotOverBasePresheaf X f hf F hF))
```

**`AlgebraicGeometry.Space.isSheaf_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean#L548). The attribute's comment: “axiom [0]: Quot\_\{F/X/S} is a sheaf, for the fppf and hence for the étale topology”.

> **Stacks 0CZW, axiom [0].** In the situation of the remark, `Quot_{F/X/S}` is a sheaf for
> the étale topology (indeed for the fppf topology), by Stacks 09TT.

```lean
theorem isSheaf_quotOverBase :
    Presheaf.IsSheaf (BigFppfOver.topology B S hS) (quotOverBasePresheaf X f hf F hF) ∧
      Presheaf.IsSheaf ((AlgebraicGeometry.etaleTopology B).over (B.obj hS))
        (quotOverBasePresheaf X f hf F hF)
```

**`AlgebraicGeometry.Space.satisfiesRS_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinAxioms.lean#L561). The attribute's comment: “axiom [2]: Quot\_\{F/X/S} satisfies the Rim-Schlessinger condition (RS)”.

> **Stacks 0CZW, axiom [2].** In the situation of the remark, `Quot_{F/X/S}` satisfies the
> Rim–Schlessinger condition: for a pushout `Y' = Y ⨿_X X'` of spectra of Artinian local rings of
> finite type over `S` along a closed immersion `X ⟶ X'`, the map
> `Quot(Y') ⟶ Quot(Y) ×_{Quot(X)} Quot(X')` is bijective; equivalently the category fibred in sets
> `𝒮_{Quot}` satisfies (RS) of Stacks 07WP. This is Stacks 08IW together with the descent of the
> properness of the support across the thickening `Y ⟶ Y'`.

```lean
theorem satisfiesRS_quotOverBase :
    Deformation.Artin.SatisfiesRSFunctor B S hS (quotOverBasePresheaf X f hf F hF) ∧
      Deformation.Artin.SatisfiesRS B S hS
        (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).val.p
        (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).isFiberedInGroupoids
```

**`AlgebraicGeometry.Space.isEffective_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinEffective.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinEffective.lean#L172). The attribute's comment: “axiom [4]: formal objects of Quot\_\{F/X/S} are effective”.

> **Stacks 0CZW, axiom [4]: formal objects of `Quot_{F/X/S}` are effective.** For `f`
> separated and `F` of finite presentation, every formal object of `𝒮_{Quot_{F/X/S}}` over a
> Noetherian complete local ring is effective. This is Grothendieck's existence theorem (Stacks
> 08BE) applied to the quotient modules, together with the algebraization of the quotient maps
> (representability of `Hom` sheaves, Stacks 08K6) and their surjectivity, checked on the closed
> fibre.

```lean
theorem isEffective_quotOverBase (hsep : IsSeparated B S hS f.hom)
    (hFfp : F.IsFinitePresentationOnSite)
    (ξ : FormalObject B S hS
      (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).val.p) :
    FormalObject.IsEffective B S hS
      (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).val.p
      (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).property ξ
```

**`AlgebraicGeometry.Space.limitPreserving_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinLimits.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinLimits.lean#L115). The attribute's comment: “axiom [1]: Quot\_\{F/X/S} is limit preserving”.

> **Stacks 0CZW, axiom [1].** In the situation of the remark (`F` of finite presentation),
> `Quot_{F/X/S}` is limit preserving: for every cofiltered system of affine schemes `Tᵢ` of the site
> with limit `T` in schemes, the map `colim Quot(Tᵢ) ⟶ Quot(T)` is bijective. A quotient over the
> limit descends to a stage (Stacks 082Q, with the descent of flatness and of proper support), and
> two quotients over a stage agreeing over the limit agree at a later stage.

```lean
theorem limitPreserving_quotOverBase (hFfp : F.IsFinitePresentationOnSite) :
    AlgebraicGeometry.LimitPreserving.{u, u, u, u} (BigFppfOver.toScheme B S hS)
      (quotOverBasePresheaf X f hf F hF)
```

**`AlgebraicGeometry.Space.hasFiniteDimensionalTangentSpaces_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinTangentSpaces.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinTangentSpaces.lean#L493). The attribute's comment: “axiom [3]: the tangent spaces of Quot\_\{F/X/S} at finite type points are finite dimensional”.

> **Stacks 0CZW, axiom [3].** In the situation of the remark, with `F` of finite presentation
> and flat over `S`, the tangent spaces of `Quot_{F/X/S}` at the points over fields of finite type
> over `S` are finite-dimensional, for their canonical vector space structure.
>
> A lift over `k[V]` of a point `F_k ⟶ F_k/𝒦₀` is a quotient of `F_{k[V]}` flat over `k[V]`; its
> difference with the trivial lift is a morphism `𝒦₀ ⟶ (F_k/𝒦₀) ⊗ V`, natural in `V` and
> determining the lift, so the tangent space embeds `k`-linearly into `Hom(𝒦₀, F_k/𝒦₀)`
> (the deformation theory of quotients of Stacks 0CZV). That space is finite-dimensional because
> `𝒦₀` is coherent and `F_k/𝒦₀` is coherent with support proper over `k` (Stacks 0D0T).

```lean
theorem hasFiniteDimensionalTangentSpaces_quotOverBase (hFfp : F.IsFinitePresentationOnSite)
    (hflat : IsFlatOver B S hS X.2 f.hom F) :
    Stack.HasFiniteDimensionalTangentSpaces B S hS
      (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF))
```

**`AlgebraicGeometry.Space.isOpenVersality_quotOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/QuotArtinTower.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/QuotArtinTower.lean#L125). The attribute's comment: “axiom [5]: openness of versality for Quot\_\{F/X/S}”.

> **Stacks 0CZW, axiom [5]: openness of versality for `Quot_{F/X/S}`.** For `S` locally
> Noetherian, `f` separated and `F` of finite presentation, a finite type point of a scheme locally
> of finite type over `S` at which an object of `Quot_{F/X/S}` is versal has an open neighbourhood
> of finite type points at which it is versal. This is Stacks 0CXU: the diagonal is representable,
> (RS*) holds, `Quot_{F/X/S}` is limit preserving (axiom [1]), and towers of square-zero thickenings
> of affine schemes are effective, by Grothendieck existence for such towers (Stacks 0CXB),
> representability of `Hom` sheaves (Stacks 08K6) and Nakayama.

```lean
theorem isOpenVersality_quotOverBase [AlgebraicGeometry.IsLocallyNoetherian S]
    (hsep : IsSeparated B S hS f.hom) (hFfp : F.IsFinitePresentationOnSite) :
    ∀ U : Over S, LocallyOfFiniteType U.hom →
      ∀ (y : (Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).val.obj)
        (hy : ((Stack.fibredCategory B S hS (quotOverBasePresheaf X f hf F hF)).val.p ⋙
          Over.post B.inclusion).obj y = U)
        (u : U.left),
        AlgebraicGeometry.IsFiniteTypePoint u →
        Deformation.Artin.IsVersalAt U ((Stack.fibredCategory B S hS
          (quotOverBasePresheaf X f hf F hF)).val.p ⋙ Over.post B.inclusion) u y hy →
        ∃ V : U.left.Opens, u ∈ V.1 ∧
          ∀ u' ∈ V.1, AlgebraicGeometry.IsFiniteTypePoint u' →
            Deformation.Artin.IsVersalAt U ((Stack.fibredCategory B S hS
              (quotOverBasePresheaf X f hf F hF)).val.p ⋙ Over.post B.inclusion) u' y hy
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.8, Tag 09TQ](https://stacks.math.columbia.edu/tag/09TQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
