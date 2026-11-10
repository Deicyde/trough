---
declaration: section
origin: cited
lean: Stacks.Cohomology.ProperSupportPerfection.isPerfect_derivedPushforward_of_properSupport, Stacks.AlgebraicGeometry.ProperSupportCoherent.isPseudoCoherent_derivedPushforward_of_isProperOver_supp_unconditional, Stacks.AlgebraicGeometry.ProperSupportCoherent.isPerfect_derivedPushforward_of_isProperOver_supp, Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensor, Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensorProductFunctor, Stacks.Cohomology.PerfectInternalHomPushforward.isPerfect_derivedPushforward_derivedSheafHom_of_flatProperSupport, Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_of_flat_of_isProper
statement: formalized
proof: formalized
---

# 36.27 Producing perfect complexes

Section 36.27 of the Stacks Project, [Tag 0A1E](https://stacks.math.columbia.edu/tag/0A1E). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08EV, a lemma

[Tag 08EV](https://stacks.math.columbia.edu/tag/08EV) in the Stacks Project.

**`Stacks.Cohomology.ProperSupportPerfection.isPerfect_derivedPushforward_of_properSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperSupportPerfection.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperSupportPerfection.lean#L314). The attribute's comment: “the direct image is the derived pushforward, not an arbitrary functor; carried are Tag 08E2 for the object and the source's closing Tor-dimension estimate, both named hypotheses about that functor; this theorem is what Tag 0DJQ and Tag 0B6F consume, so neither of those assumes this tag any longer”.

> **[Stacks, Tag 08EV].**  Let `S` be a locally Noetherian scheme and `f : X ⟶ S` a morphism
> locally of finite type.  Let `K` be an object of `D(𝒪_X)` which
>
> 1. is bounded with coherent cohomology sheaves, that is, lies in `D^b_{Coh}(𝒪_X)`;
> 2. has the support of each of its cohomology sheaves inside a closed subset proper over `S`; and
> 3. has finite Tor dimension as an object of `D(f⁻¹𝒪_S)`.
>
> Then `Rf_*K` is a perfect object of `D(𝒪_S)`, with `Rf_*` the derived direct image
> `Stacks.Cohomology.ProperSupportPerfection.derivedPushforwardOX` — the total right derived functor
> of degreewise pushforward — and not an arbitrary functor.
>
> Two hypotheses beyond those are carried, and they are the two statements of the source's proof
> that this repository does not have; each is a statement about that same `Rf_*`, and see the
> implementation notes of this file for why each is unavoidable here.  `hpushforwardCoherence` is
> [Stacks, Tag 08E2] for `K`, read through
> [Stacks, Tag 08E8]: granted a closed subset proper over `S` carrying the cohomological support,
> and granted coherence of the cohomology sheaves, `Rf_*K` is pseudo-coherent.
> `hpushforwardTorDimension` is the closing step of the source's proof for `K`: granted the same
> closed subset and clause (3), `Rf_*K` has finite Tor dimension over `𝒪_S`.  Neither mentions
> perfectness; what is proved here is the production of the closed subset — the source's "let
> `T ⊂ X` be the union of the supports of the `H^i(E)`" — and the passage from the two residues to
> perfectness through [Stacks, Tag 08CQ].

```lean
theorem isPerfect_derivedPushforward_of_properSupport [IsLocallyNoetherian S]
    (hbounded : ∃ a b : ℤ, ∀ i : ℤ, i ∉ Set.Icc a b →
      Limits.IsZero ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) i).obj K))
    (hcoherent : ∀ i : ℤ,
      ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) i).obj K).IsCoherent)
    (hproperSupport : ∀ i : ℤ, ∃ Z : Closeds X, IsProperOver f Z ∧
      SheafOfModules.supp
          ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) i).obj K) ⊆
        (Z : Set X))
    (hTor : D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction f).obj K))
    (hpushforwardCoherence : ∀ T : Closeds X, IsProperOver f T → SuppHomologySubset K T →
      (∀ i : ℤ,
        ((DerivedCategory.homologyFunctor (OXMod.{u, u} X.toRingedSpace) i).obj K).IsCoherent) →
      RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
        ((derivedPushforwardOX f).obj K))
    (hpushforwardTorDimension : ∀ T : Closeds X, IsProperOver f T → SuppHomologySubset K T →
      D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction f).obj K) →
      Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension S.toRingedSpace
        ((derivedPushforwardOX f).obj K)) :
    RingedSpace.IsPerfect (X := S.toRingedSpace) ((derivedPushforwardOX f).obj K)
```

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.isPseudoCoherent_derivedPushforward_of_isProperOver_supp_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/PerfectDirectImageSupplement.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/PerfectDirectImageSupplement.lean#L48). The attribute's comment: “the pseudo-coherence half of the conclusion only: Rf_*E is a pseudo-coherent object of D(𝒪_S). Perfectness is pseudo-coherence together with locally finite Tor dimension by Tag 08CQ, and the Tor-dimension half is not proved here: it needs the clause (2) implies (1) of Tag 08EA and the projection formula of Tag 08EU at a general target complex, neither of which is in the tree. Rf_*E is nowhere asserted here to be of locally finite Tor dimension, nor to be perfect”. References: SGA 6 IV (2.11.1), “partial”; SGA 6 XIV (2.2), “special case”.

> **[Stacks, Tag 08EV], the pseudo-coherence half of the conclusion.** Let `S` be a Noetherian
> scheme, `f : X ⟶ S` locally of finite type and `E` a bounded object of `D(𝒪_X)` whose cohomology
> sheaves are coherent with support proper over `S`. Then `Rf_*E` is a pseudo-coherent object of
> `D(𝒪_S)`.
>
> By [Stacks, Tag 08CQ] perfectness is pseudo-coherence together with locally finite Tor
> dimension; this is the first of the two, obtained from [Stacks, Tag 08E2] and
> [Stacks, Tag 08E8].

```lean
theorem isPseudoCoherent_derivedPushforward_of_isProperOver_supp_unconditional [IsNoetherian S]
    [LocallyOfFiniteType f] (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsCoherent)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hcoh j).isFiniteType⟩)
    (a b : ℤ) (hGE : E.IsGE a) (hLE : E.IsLE b) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
      ((derivedPushforwardModules f).obj E)
```

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.isPerfect_derivedPushforward_of_isProperOver_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TorDimensionDirectImage.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TorDimensionDirectImage.lean#L345). References: SGA 6 0 (3.1), “more general”; SGA 6 0 (4.1), “more general”; SGA 6 XIV (2.2), “special case”.

> Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of finite type and `E` an
> object of `D(𝒪_X)` such that
>
> 1. `E` is in `D^b_{Coh}(𝒪_X)`: it is bounded, `E ∈ D^{≥ a} ∩ D^{≤ b}`, and its cohomology sheaves
>    are coherent;
> 2. the support of `H^i(E)` is proper over `S` for every `i`;
> 3. `E` has finite Tor dimension as an object of `D(f⁻¹𝒪_S)`.
>
> Then `Rf_*E` is a perfect object of `D(𝒪_S)`.

```lean
theorem isPerfect_derivedPushforward_of_isProperOver_supp {X S : Scheme.{u}} (f : X ⟶ S)
    [IsNoetherian S] [LocallyOfFiniteType f] (E : DerivedCategory X.Modules)
    (a b : ℤ) (hGE : E.IsGE a) (hLE : E.IsLE b)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsCoherent)
    (hsupp : ∀ j : ℤ, IsProperOver f
      ⟨SheafOfModules.supp ((DerivedCategory.homologyFunctor X.Modules j).obj E),
        @SheafOfModules.isClosed_supp _ _ _ (hcoh j).isFiniteType⟩)
    (htor : Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension
      (RingedSpace.inverseImage S.toRingedSpace f.base)
      ((Scheme.Hom.derivedScalarRestriction f).obj E)) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforwardModules f).obj E)
```

## Tag 0DJQ, a lemma

[Tag 0DJQ](https://stacks.math.columbia.edu/tag/0DJQ) in the Stacks Project.

**`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforward.lean, line 1543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforward.lean#L1543). The attribute's comment: “the direct image is the derived pushforward, not an arbitrary functor; Tag 08EV is proved in ProperSupportPerfection and applied here, so what stands in its place are its own two residues about that same functor, Tag 08E2 for it and the source's closing Tor-dimension estimate; of Tag 08EV's four clauses for the derived tensor product three are proved here and the fourth, finiteness of the Tor dimension over the inverse image of the structure sheaf of the base, is carried, with the geometric step it runs on proved as exists_local_tensorComplex_models”.

> **[Stacks, Tag 0DJQ].**  Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of
> finite type, `E` a perfect object of `D(𝒪_X)` and `𝒢` a bounded complex of coherent
> `𝒪_X`-modules, flat over `S`, whose support is proper over `S`.  Then
> `Rf_*(E ⊗^L_{𝒪_X} 𝒢)` is a perfect object of `D(𝒪_S)`, with `Rf_*` the derived direct image
> `Stacks.Cohomology.ProperSupportPerfection.derivedPushforwardOX f` — the total right derived
> functor of degreewise pushforward — and not a functor left unspecified.
>
> [Stacks, Tag 08EV] itself is *not* a hypothesis: it is proved in
> `StacksFrontier/AlgebraicGeometry/Perfect/ProperSupportPerfection.lean`, and
> `Stacks.Cohomology.PerfectPushforward.pushforwardPerfectionCriterion_of_residues` turns it into
> the criterion this proof consumes.  What is carried in its place are that theorem's own two
> residues, `hcoh` and `htor` — [Stacks, Tag 08E2] for `Rf_*` and the source's closing
> Tor-dimension estimate, both statements about that same functor — each of which is strictly
> smaller than the conclusion, with its obstruction identified in its own docstring.
>
> One of the four clauses of [Stacks, Tag 08EV]'s hypothesis for `E ⊗^L_{𝒪_X} 𝒢` is still
> carried, as the `hasFiniteTorDimension` field of `h`.  The support clause is
> proved: see `Stacks.Cohomology.PerfectPushforward.supp_homology_derivedTensor_subset` and
> `Stacks.Cohomology.PerfectPushforward.TensorPushforwardData.input`.  So is the boundedness
> clause: see
> `Stacks.Cohomology.PerfectPushforward.exists_isZero_homology_derivedTensor` and
> `Stacks.Cohomology.PerfectPushforward.TensorPushforwardData.bounded`.  So is coherence: see
> `Stacks.Cohomology.PerfectPushforward.isCoherent_homology_derivedTensor` and
> `Stacks.Cohomology.PerfectPushforward.TensorPushforwardData.isCoherent`.  The geometric step the
> remaining clause runs on — that `E ⊗^L_{𝒪_X} 𝒢` is, locally on a covering of `X`, the total tensor
> complex of a strictly perfect complex with the restriction of `𝒢` — is proved above, as
> `Stacks.Cohomology.PerfectPushforward.exists_local_tensorComplex_models`; what reading it off that
> still needs is listed in the implementation notes of this file.

```lean
theorem isPerfect_derivedPushforward_derivedTensor [IsNoetherian S] [LocallyOfFiniteType f]
    (D : RingedSpace.CertifiedDerivedSheafTensoring
      (RingedSpace.inverseImage S.toRingedSpace f.base))
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.toRingedSpace.sheaf)
    [(Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, u, u, u} X.toRingedSpace.sheaf).Additive]
    [∀ M, ((Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, u, u, u} X.toRingedSpace.sheaf).obj M).Additive]
    [∀ K L : CochainComplex (Stacks.DerivedTensor.RingedSite.Modules X.toRingedSpace.sheaf) ℤ,
      HomologicalComplex.HasMapBifunctor K L
        (Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, u, u, u} X.toRingedSpace.sheaf) (ComplexShape.up ℤ)]
    (hcoh : PushforwardCoherenceResidue f (derivedPushforwardOX f))
    (htor : PushforwardTorDimensionResidue f D (derivedPushforwardOX f))
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (G : CochainComplex (OXMod.{u, u} X.toRingedSpace) ℤ)
    (h : TensorPushforwardData f D T E G) :
    RingedSpace.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforwardOX f).obj ((T.tensor.obj E).obj (DerivedCategory.Q.obj G)))
```

**`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensorProductFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean#L70).

> **[Stacks, Tag 0DJQ].** Let `S` be a Noetherian scheme and `f : X ⟶ S` a morphism of schemes
> which is locally of finite type. Let `E` be a perfect object of `D(𝒪_X)` and let `𝒢` be a bounded
> complex of coherent `𝒪_X`-modules, flat over `S`, with support proper over `S`
> (`Stacks.Cohomology.PerfectPushforward.FlatProperSupportComplex`). Then
> `Rf_*(E ⊗^L_{𝒪_X} 𝒢)` is a perfect object of `D(𝒪_S)`.

```lean
theorem isPerfect_derivedPushforward_derivedTensorProductFunctor [IsNoetherian S]
    [LocallyOfFiniteType f] (G : CochainComplex (OXMod.{u, u} X.toRingedSpace) ℤ)
    (hG : FlatProperSupportComplex f G) :
    letI := HasDerivedCategory.standard (OXMod.{u, u} X.toRingedSpace)
    letI := HasDerivedCategory.standard
      (Stacks.DerivedTensor.RingedSite.Modules X.toRingedSpace.sheaf)
    letI := HasDerivedCategory.standard (OXMod.{u, u} S.toRingedSpace)
    ∀ E : DerivedCategory (OXMod.{u, u} X.toRingedSpace),
      RingedSpace.IsPerfect (X := X.toRingedSpace) E →
        RingedSpace.IsPerfect (X := S.toRingedSpace)
          ((derivedPushforwardOX f).obj
            (((derivedTensorProductFunctor X.toRingedSpace.sheaf).obj E).obj
              (DerivedCategory.Q.obj G)))
```

## Tag 0DJR, a lemma

[Tag 0DJR](https://stacks.math.columbia.edu/tag/0DJR) in the Stacks Project.

**`Stacks.Cohomology.PerfectInternalHomPushforward.isPerfect_derivedPushforward_derivedSheafHom_of_flatProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectInternalHomPushforwardUnconditional.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectInternalHomPushforwardUnconditional.lean#L96).

> **[Stacks, Tag 0DJR].**  Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of
> finite type, `E` a perfect object of `D(𝒪_X)` and `𝒢` a bounded complex of coherent
> `𝒪_X`-modules, flat over `S`, with support proper over `S`.  Then `Rf_*RSheafHom(E, 𝒢)` is a
> perfect object of `D(𝒪_S)`, with `Rf_*` the derived direct image
> `Stacks.Cohomology.ProperSupportPerfection.derivedPushforwardOX f`.
>
> The source's proof: `E^∨` is perfect and `RSheafHom(E, 𝒢) ≅ E^∨ ⊗^L 𝒢` by [Stacks, Tag 08DQ]
> (`derivedSheafHomObjIsoDualTensor`), and [Stacks, Tag 0DJQ] applies to `(E^∨, 𝒢)`.

```lean
theorem isPerfect_derivedPushforward_derivedSheafHom_of_flatProperSupport [IsNoetherian S]
    [LocallyOfFiniteType f]
    (E : DerivedCategory (OXMod.{u, u} X.toRingedSpace))
    (G : CochainComplex (OXMod.{u, u} X.toRingedSpace) ℤ)
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E) (hG : FlatProperSupportComplex f G) :
    RingedSpace.IsPerfect (X := S.toRingedSpace)
      ((derivedPushforwardOX f).obj (derivedSheafHomObj (X := X) E G))
```

## Tag 0B6F, a lemma

[Tag 0B6F](https://stacks.math.columbia.edu/tag/0B6F) in the Stacks Project.

**`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_of_flat_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean#L92).

> **[Stacks, Tag 0B6F].** Let `S` be a Noetherian scheme and `f : X ⟶ S` a flat proper morphism
> of schemes. Let `E` be a perfect object of `D(𝒪_X)`. Then `Rf_*E` is a perfect object of
> `D(𝒪_S)`.

```lean
theorem isPerfect_derivedPushforward_of_flat_of_isProper [IsNoetherian S] [Flat f] [IsProper f] :
    letI := HasDerivedCategory.standard (OXMod.{u, u} X.toRingedSpace)
    letI := HasDerivedCategory.standard (OXMod.{u, u} S.toRingedSpace)
    ∀ E : DerivedCategory (OXMod.{u, u} X.toRingedSpace),
      RingedSpace.IsPerfect (X := X.toRingedSpace) E →
        RingedSpace.IsPerfect (X := S.toRingedSpace) ((derivedPushforwardOX f).obj E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.27, Tag 0A1E](https://stacks.math.columbia.edu/tag/0A1E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
