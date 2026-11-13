---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProperSupportCoherent.isPerfect_derivedPushforward_of_isProperOver_supp, Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensorProductFunctor, Stacks.Cohomology.PerfectInternalHomPushforward.isPerfect_derivedPushforward_derivedSheafHom_of_flatProperSupport, Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_of_flat_of_isProper
statement: formalized
proof: formalized
---

# 36.27 Producing perfect complexes

Section 36.27 of the Stacks Project, [Tag 0A1E](https://stacks.math.columbia.edu/tag/0A1E). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08EV, a lemma

[Tag 08EV](https://stacks.math.columbia.edu/tag/08EV) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.isPerfect_derivedPushforward_of_isProperOver_supp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TorDimensionDirectImage.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TorDimensionDirectImage.lean#L366). The attribute's comment: “the source's statement and hypotheses: S Noetherian, f locally of finite type, E bounded with coherent cohomology sheaves whose supports are proper over S and of finite Tor dimension over f⁻¹𝒪\_S for its canonical derived tensor product; Rf\_* is the total right derived functor of degreewise pushforward. The Tor-dimension half is proved by a Mayer–Vietoris induction from the affine case rather than through Tag 08EU and Tag 08EA”. References: SGA 6 0 (3.1), “more general”; SGA 6 0 (4.1), “more general”; SGA 6 XIV (2.2), “special case”.

> **[Stacks, Tag 08EV].** Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of
> finite type and `E` an object of `D(𝒪_X)` such that
>
> 1. `E` is in `D^b_{Coh}(𝒪_X)`: it is bounded, `E ∈ D^{≥ a} ∩ D^{≤ b}`, and its cohomology sheaves
>    are coherent;
> 2. the support of `H^i(E)` is proper over `S` for every `i`;
> 3. `E` has finite Tor dimension as an object of `D(f⁻¹𝒪_S)`.
>
> Then `Rf_*E` is a perfect object of `D(𝒪_S)`.
>
> `Rf_*` is `AlgebraicGeometry.derivedPushforwardModules`, the total right derived functor of
> degreewise pushforward, and clause (3) is Tor dimension over the inverse-image ringed space
> `(X, f⁻¹𝒪_S)` for its canonical derived tensor product. As in the source, the proof splits the
> conclusion by [Stacks, Tag 08CQ]: pseudo-coherence comes from [Stacks, Tag 08E2] and
> [Stacks, Tag 08E8], and locally finite Tor dimension from
> `AlgebraicGeometry.locallyHasFiniteTorDimension_derivedPushforward_of_isProperOver`. That second
> half follows the source's reduction — one closed subset proper over `S` carrying all the
> cohomological support ([Stacks, Tag 0CYR]), and a quasi-compact open neighbourhood of it over each
> affine open of `S` — and then replaces the source's appeal to [Stacks, Tag 08EU] and
> [Stacks, Tag 08EA] by a Mayer--Vietoris induction from the affine case, where the statement is
> commutative algebra.

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

**`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensorProductFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean#L76).

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

**`Stacks.Cohomology.PerfectInternalHomPushforward.isPerfect_derivedPushforward_derivedSheafHom_of_flatProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectInternalHomPushforwardUnconditional.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectInternalHomPushforwardUnconditional.lean#L96).

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

**`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_of_flat_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/PerfectPushforwardCanonicalTensor.lean#L98).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
