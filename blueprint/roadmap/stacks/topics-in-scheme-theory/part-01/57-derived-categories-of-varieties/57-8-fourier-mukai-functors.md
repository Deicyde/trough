---
declaration: section
origin: cited
lean: AlgebraicGeometry.fourierMukai, AlgebraicGeometry.isTriangulated_fourierMukai, AlgebraicGeometry.fourierMukaiOn, AlgebraicGeometry.isTriangulated_fourierMukaiOn, AlgebraicGeometry.IsFourierMukaiKernel, AlgebraicGeometry.IsFourierMukaiFunctor, AlgebraicGeometry.isQuasicoherent_homology_fourierMukai, AlgebraicGeometry.fourierMukaiConvolution
statement: formalized
proof: formalized
---

# 57.8 Fourier-Mukai functors

Section 57.8 of the Stacks Project, [Tag 0FYP](https://stacks.math.columbia.edu/tag/0FYP). 9 tags here are carried by 40 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FYQ, a definition

[Tag 0FYQ](https://stacks.math.columbia.edu/tag/0FYQ) in the Stacks Project.

**`AlgebraicGeometry.fourierMukai`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L201). The attribute's comment: “the Fourier-Mukai functor”.

> **Stacks Project, Tag 0FYQ (the functor).** The Fourier-Mukai functor
> `Φ_K : D(𝒪_X) ⟶ D(𝒪_Y)` attached to a complex `K` on `X ×_S Y`, namely
> `M ⟼ R pr_{2,*}(L pr_1^* M ⊗^𝐋_{𝒪_{X ×_S Y}} K)`.

```lean
def fourierMukai (K : DerivedCategory (Limits.pullback f g).Modules) :
    DerivedCategory X.Modules ⥤ DerivedCategory Y.Modules
```

**`AlgebraicGeometry.isTriangulated_fourierMukai`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L239). The attribute's comment: “exactness of the Fourier-Mukai functor”.

> **Stacks Project, Tag 0FYQ (exactness).** The Fourier-Mukai functor is an exact functor of
> triangulated categories: the derived pullback along `pr₁` is exact by Stacks 06YJ, tensoring
> with `K` is exact by Stacks 06YU, and the derived direct image along `pr₂` is exact because it
> is a right derived functor out of a Grothendieck abelian category.

```lean
instance isTriangulated_fourierMukai (K : DerivedCategory (Limits.pullback f g).Modules) :
    (fourierMukai f g K).IsTriangulated
```

**`AlgebraicGeometry.fourierMukaiOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L252). The attribute's comment: “the induced functor on a preserved pair of full subcategories”.

> **Stacks Project, Tag 0FYQ (the induced functor).** Suppose `Φ_K` carries every object of
> `D(𝒪_X)` with property `P` to an object of `D(𝒪_Y)` with property `Q`. Then it induces a functor
> between the corresponding full subcategories, which is again called a Fourier-Mukai functor;
> taking `P` and `Q` to be quasi-coherence of the cohomology sheaves, perfectness, or bounded
> coherence over a Noetherian base gives the three restricted versions of the definition.

```lean
def fourierMukaiOn (K : DerivedCategory (Limits.pullback f g).Modules)
    (P : ObjectProperty (DerivedCategory X.Modules))
    (Q : ObjectProperty (DerivedCategory Y.Modules))
    (h : ∀ M : P.FullSubcategory, Q ((fourierMukai f g K).obj M.obj)) :
    P.FullSubcategory ⥤ Q.FullSubcategory
```

**`AlgebraicGeometry.isTriangulated_fourierMukaiOn`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L283). The attribute's comment: “exactness of the induced functor”.

> **Stacks Project, Tag 0FYQ (exactness of the induced functor).** On a preserved pair of
> triangulated subcategories the induced functor is again exact, `Φ_K` being exact.

```lean
instance isTriangulated_fourierMukaiOn : (fourierMukaiOn f g K P Q h).IsTriangulated
```

**`AlgebraicGeometry.IsFourierMukaiKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L294). The attribute's comment: “the Fourier-Mukai kernel”.

> **Stacks Project, Tag 0FYQ (the kernel).** A complex `K` on `X ×_S Y` is a Fourier-Mukai
> kernel for a functor `Φ : D(𝒪_X) ⟶ D(𝒪_Y)` when `Φ` is isomorphic to the Fourier-Mukai functor
> `Φ_K` attached to `K`.

```lean
def IsFourierMukaiKernel (Φ : DerivedCategory X.Modules ⥤ DerivedCategory Y.Modules)
    (K : DerivedCategory (Limits.pullback f g).Modules) : Prop
```

**`AlgebraicGeometry.IsFourierMukaiFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Basic.lean#L302). The attribute's comment: “being a Fourier-Mukai functor”.

> **Stacks Project, Tag 0FYQ (the property of being a Fourier-Mukai functor).** A functor
> `D(𝒪_X) ⟶ D(𝒪_Y)` is a Fourier-Mukai functor when some complex on `X ×_S Y` is a Fourier-Mukai
> kernel for it.

```lean
def IsFourierMukaiFunctor (Φ : DerivedCategory X.Modules ⥤ DerivedCategory Y.Modules) : Prop
```

## Tag 0FYR, a lemma

[Tag 0FYR](https://stacks.math.columbia.edu/tag/0FYR) in the Stacks Project.

**`AlgebraicGeometry.isQuasicoherent_homology_fourierMukai`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/QuasiCoherent.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/QuasiCoherent.lean#L86).

> **[Stacks, Tag 0FYR].** Let `S` be a scheme, let `X` and `Y` be schemes over `S` with
> `f : X ⟶ S` quasi-compact and quasi-separated, and let `K` be a complex on `X ×_S Y` all of whose
> cohomology sheaves are quasi-coherent. Then the Fourier-Mukai functor `Φ_K` carries
> `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_Y)`: every cohomology sheaf of `Φ_K(M)` is quasi-coherent whenever
> every cohomology sheaf of `M` is.
>
> The three factors of `Φ_K` are applied in turn: `L pr_1^*` by [Stacks, Tag 08DW] part (1),
> `- ⊗^𝐋 K` by [Stacks, Tag 08DX] part (1), and `R pr_{2,*}` by [Stacks, Tag 08D5] part (1), whose
> hypothesis holds because `pr₂` is quasi-compact and quasi-separated by base change from `f`.

```lean
theorem isQuasicoherent_homology_fourierMukai [QuasiCompact f] [QuasiSeparated f]
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj
      K).IsQuasicoherent)
    (M : DerivedCategory X.Modules)
    (hM : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj M).IsQuasicoherent)
    (i : ℤ) :
    ((DerivedCategory.homologyFunctor Y.Modules i).obj
      ((fourierMukai f g K).obj M)).IsQuasicoherent
```

## Tag 0FYS, a lemma

[Tag 0FYS](https://stacks.math.columbia.edu/tag/0FYS) in the Stacks Project.

**`AlgebraicGeometry.fourierMukaiConvolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Composition.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Composition.lean#L317). The attribute's comment: “the convolution kernel `K''`”.

> **The convolution kernel of [Stacks, Tag 0FYS]**:
> `K'' = R pr_{13,*}(L pr_{12}^* K ⊗^𝐋_{𝒪_{X ×_S Y ×_S Z}} L pr_{23}^* K')`, a complex
> on `X ×_S Z`.

```lean
def fourierMukaiConvolution (K : DerivedCategory (pullback f g).Modules)
    (K' : DerivedCategory (pullback g h).Modules) : DerivedCategory (pullback f h).Modules
```

**`AlgebraicGeometry.isQuasicoherent_homology_fourierMukaiConvolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Composition.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/Composition.lean#L458). The attribute's comment: “quasi-coherence of the convolution kernel; the clause making the statement of the lemma meaningful”.

> **The convolution kernel has quasi-coherent cohomology sheaves**, so the Fourier-Mukai
> functor it defines carries `D_QCoh(𝒪_X)` into `D_QCoh(𝒪_Z)` by [Stacks, Tag 0FYR]: pull back by
> [Stacks, Tag 08DW] part (1), tensor by [Stacks, Tag 08DX] part (1), and push forward along the
> quasi-compact and quasi-separated morphism `pr_{13}` by [Stacks, Tag 08D5] part (1).

```lean
theorem isQuasicoherent_homology_fourierMukaiConvolution
    {K : DerivedCategory (pullback f g).Modules}
    (hK : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (pullback f g).Modules j).obj
      K).IsQuasicoherent)
    {K' : DerivedCategory (pullback g h).Modules}
    (hK' : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (pullback g h).Modules j).obj
      K').IsQuasicoherent)
    (j : ℤ) :
    ((DerivedCategory.homologyFunctor (pullback f h).Modules j).obj
      (fourierMukaiConvolution f g h K K')).IsQuasicoherent
```

**`AlgebraicGeometry.quasiCoherentFourierMukaiCompNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/CompositionIso.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/CompositionIso.lean#L68). The attribute's comment: “composition of Fourier-Mukai functors, Phi\_\{K'} ∘ Phi\_K ≅ Phi\_\{K''} as a natural isomorphism of functors D\_QCoh(O\_X) to D\_QCoh(O\_Z), the source's equality of functors; with Stacks 08IB and 08EU discharged by their proofs”.

> **[Stacks, Tag 0FYS].**  Let `S` be a scheme and let `X`, `Y`, `Z` be schemes over `S`
> with `f : X ⟶ S`, `g : Y ⟶ S` and `h : Z ⟶ S` quasi-compact and quasi-separated.  Let `K` on
> `X ×_S Y` and `K'` on `Y ×_S Z` have quasi-coherent cohomology sheaves, and consider the
> Fourier-Mukai functors `Φ_K : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` and
> `Φ_{K'} : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_Z)`.  If `X` and `Z` are tor independent over `S` and `g` is
> flat, then `Φ_{K'} ∘ Φ_K ≅ Φ_{K''}` naturally, where
> `K'' = R pr_{13,*}(L pr_{12}^* K ⊗^𝐋 L pr_{23}^* K')` on `X ×_S Z`, a complex in
> `D_QCoh(𝒪_{X ×_S Z})`.
>
> The source writes the conclusion as an equality; the two functors are built from derived
> functors, determined up to canonical isomorphism, so the statement is a natural isomorphism.
> Derived base change ([Stacks, Tag 08IB]) and the projection formula ([Stacks, Tag 08EU]) enter
> through their proofs `AlgebraicGeometry.derivedBaseChangeIsIsoOnQuasicoherent` and
> `AlgebraicGeometry.projectionFormulaIsIsoOnQuasicoherent`.

```lean
def quasiCoherentFourierMukaiCompNatIso [Flat g] (htor : TorIndependent f h)
    {K : DerivedCategory (pullback f g).Modules}
    (hK : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (pullback f g).Modules j).obj
      K).IsQuasicoherent)
    {K' : DerivedCategory (pullback g h).Modules}
    (hK' : ∀ j : ℤ, ((DerivedCategory.homologyFunctor (pullback g h).Modules j).obj
      K').IsQuasicoherent) :
    quasiCoherentFourierMukai f g K hK ⋙ quasiCoherentFourierMukai g h K' hK' ≅
      quasiCoherentFourierMukai f h (fourierMukaiConvolution f g h K K')
        (isQuasicoherent_homology_fourierMukaiConvolution f g h hK hK')
```

## Tag 0FYT, a lemma

[Tag 0FYT](https://stacks.math.columbia.edu/tag/0FYT) in the Stacks Project.

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isCoherent_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L266). The attribute's comment: “clause (1), with Tag 08EV's own inputs carried: its two residues, a bound below on L pr₁^* M ⊗ᴸ K, and the support and Tor-dimension clauses read on that tensor, not on K”.

> **[Stacks, Tag 0FYT], clause (1).** Let `S` be a Noetherian scheme, let `X ⟶ S` and
> `Y ⟶ S` be of finite type and let `K` be an object of `D^b_{Coh}(𝒪_{X ×_S Y})`. Then `Φ_K` sends
> `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> The proof is the source's: `M` perfect on the Noetherian scheme `X` lies in `D^b_{Coh}(𝒪_X)` by
> [Stacks, Tag 0FXU], so the cohomology sheaves of `T = L pr_1^* M ⊗^𝐋 K` are coherent by the
> first half of the argument of [Stacks, Tag 0FYU]
> (`AlgebraicGeometry.isCoherent_homology_fourierMukaiTensor`) and `T` is bounded above by
> `AlgebraicGeometry.isLE_fourierMukaiPullback` and
> `AlgebraicGeometry.isLE_fourierMukaiTensor`; [Stacks, Tag 08EV] applied to
> `pr_2 : X ×_S Y ⟶ Y`, which is of finite type by base change and whose target is Noetherian
> because `Y ⟶ S` is of finite type, then gives the conclusion.
>
> Three of the four hypotheses of [Stacks, Tag 08EV] are therefore discharged. What is carried,
> beyond its two residues (see the implementation notes of this file), is:
>
> * `d` and `hGE`, a bound below on `T`. The source takes `T ∈ D^b_{Coh}` for granted here:
>   `L pr_1^* M` is perfect, so it has locally finite Tor amplitude, and `K` is bounded below, so
>   the tensor product is bounded below on each member of a covering and hence — `X ×_S Y` being
>   Noetherian — globally. The passage from locally finite Tor amplitude of one factor to a bound
>   below on a derived tensor product is not in this library: it has
>   `Stacks.DerivedTensor.RingedSite.isLE_derivedTensorProduct` for the bound above and nothing
>   for the bound below.
> * `hsupp`, the proper-support clause, read on the cohomology sheaves of `T` rather than on those
>   of `K` as the source states it. The two are joined by the inclusion
>   `supp H^i(L pr_1^* M ⊗^𝐋 K) ⊆ ⋃_j supp H^j(K)`, which this library has only for a tensor
>   product with a *complex* of modules with bounded support
>   (`Stacks.Cohomology.PerfectPushforward.supp_homology_derivedTensor_subset`) and not for a
>   second factor given as a derived object. When `X ⟶ S` is proper the clause is free, by
>   `AlgebraicGeometry.isProperOver_pullbackSnd_of_isProper`.
> * `hTor`, finiteness of the Tor dimension of `T` over `pr_2^{-1}𝒪_Y`, read on `T` rather than on
>   `K` as the source states it. The source's clause is on `K`, and the passage to `T` is
>   "tensoring with a perfect object preserves finite Tor dimension over `pr_2^{-1}𝒪_Y`", which is
>   the second assertion of [Stacks, Tag 0DI4] in the relative-perfectness form and is not
>   available at the absolute Tor-dimension predicate
>   `AlgebraicGeometry.RingedSpace.CertifiedDerivedSheafTensoring.HasFiniteTorDimension` this
>   clause of [Stacks, Tag 08EV] is written with.

```lean
theorem isPerfect_fourierMukai_of_isCoherent_kernel
    (D : RingedSpace.CertifiedDerivedSheafTensoring
      (RingedSpace.inverseImage Y.toRingedSpace (Limits.pullback.snd f g).base))
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun F : (Limits.pullback f g).Modules => F.IsCoherent) K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (d : ℤ) (hGE : (fourierMukaiKernelTensor f g K M).IsGE d)
    (hsupp : ∀ i : ℤ, ∃ Z : Closeds (Limits.pullback f g : Scheme.{u}),
      IsProperOver (Limits.pullback.snd f g) Z ∧
        SheafOfModules.supp ((DerivedCategory.homologyFunctor
            (Limits.pullback f g).Modules i).obj (fourierMukaiKernelTensor f g K M)) ⊆
          (Z : Set (Limits.pullback f g : Scheme.{u})))
    (hTor : D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction
      (Limits.pullback.snd f g)).obj (fourierMukaiKernelTensor f g K M)))
    (hpushforwardCoherence : Stacks.Cohomology.PerfectPushforward.PushforwardCoherenceResidue
      (Limits.pullback.snd f g) (derivedPushforwardOX (Limits.pullback.snd f g)))
    (hpushforwardTorDimension :
      Stacks.Cohomology.PerfectPushforward.PushforwardTorDimensionResidue
        (Limits.pullback.snd f g) D (derivedPushforwardOX (Limits.pullback.snd f g))) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_flatProperSupportComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L340). The attribute's comment: “clause (2), routed through the Noetherian form Tag 0DJQ of Tag 0A1H: Y is assumed Noetherian, the terms of the complex coherent (Tag 01XZ), and Tag 08EV's residues carried”.

> **[Stacks, Tag 0FYT], clause (2), over a Noetherian `Y`.** Let `X ⟶ S` be of finite
> presentation, let `𝒦^•` be a bounded complex of coherent `𝒪_{X ×_S Y}`-modules, flat over `Y`,
> with support proper over `Y`, and let `K` be an object of `D(𝒪_{X ×_S Y})` represented by `𝒦^•`.
> Then `Φ_K` sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> The source deduces the clause from [Stacks, Tag 0A1H], whose perfectness half this library does
> not carry: as the module documentation of
> `StacksFrontier/AlgebraicGeometry/Perfect/TensorFinitelyPresentedPushforwardBaseChange.lean`
> records, the source bridges that tag to its Noetherian form by a limit descent that is not
> assembled here. The route taken instead is that Noetherian form, [Stacks, Tag 0DJQ]
> (`Stacks.Cohomology.PerfectPushforward.isPerfect_derivedPushforward_derivedTensor`), applied to
> `pr_2 : X ×_S Y ⟶ Y` — which is locally of finite presentation, hence locally of finite type, by
> base change — with `E = L pr_1^* M`, perfect by [Stacks, Tag 09UA], and `𝒢 = 𝒦^•`.
>
> Two things are therefore weaker than the source's clause, and both come from using
> [Stacks, Tag 0DJQ] in place of [Stacks, Tag 0A1H]:
>
> * `IsNoetherian Y` is assumed, where the clause assumes nothing about `Y`;
> * the terms of `𝒦^•` are asked to be coherent rather than of finite presentation. Over the
>   Noetherian `X ×_S Y` the two conditions agree, by [Stacks, Tag 01XZ].
>
> Everything else is the source's, and three of the four hypotheses of [Stacks, Tag 08EV] for
> `L pr_1^* M ⊗^𝐋 𝒦^•` are *proved* inside [Stacks, Tag 0DJQ] — the support clause from the
> proper support of `𝒦^•`, the coherence clause, and the boundedness clause. What is carried is
> `hTor`, finiteness of the Tor dimension of `L pr_1^* M ⊗^𝐋 𝒦^•` over `pr_2^{-1}𝒪_Y`, which is
> the fourth clause and which [Stacks, Tag 0DJQ] carries as the `hasFiniteTorDimension` field of
> `Stacks.Cohomology.PerfectPushforward.TensorPushforwardData`, together with the two residues of
> [Stacks, Tag 08EV] described in the implementation notes of this file.

```lean
theorem isPerfect_fourierMukai_of_flatProperSupportComplex [IsNoetherian Y]
    [LocallyOfFinitePresentation f]
    (D : RingedSpace.CertifiedDerivedSheafTensoring
      (RingedSpace.inverseImage Y.toRingedSpace (Limits.pullback.snd f g).base))
    (G : CochainComplex
      (StrictlyPerfect.OXMod.{u, u} (Limits.pullback f g).toRingedSpace) ℤ)
    (hG : Stacks.Cohomology.PerfectPushforward.FlatProperSupportComplex
      (Limits.pullback.snd f g) G)
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (e : DerivedCategory.Q.obj G ≅ K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (hTor : D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction
      (Limits.pullback.snd f g)).obj
        (fourierMukaiKernelTensor f g (DerivedCategory.Q.obj G) M)))
    (hpushforwardCoherence : Stacks.Cohomology.PerfectPushforward.PushforwardCoherenceResidue
      (Limits.pullback.snd f g) (derivedPushforwardOX (Limits.pullback.snd f g)))
    (hpushforwardTorDimension :
      Stacks.Cohomology.PerfectPushforward.PushforwardTorDimensionResidue
        (Limits.pullback.snd f g) D (derivedPushforwardOX (Limits.pullback.snd f g))) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L437). The attribute's comment: “clause (3), with Tag 08EV's two residues and its Tor-dimension clause for L pr₁^* M ⊗ᴸ K carried, and with Y assumed Noetherian”.

> **[Stacks, Tag 0FYT], clause (3).** Let `X ⟶ S` be a proper flat morphism of finite
> presentation and let `K` be a perfect object of `D(𝒪_{X ×_S Y})`. Then `Φ_K` sends
> `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> This is `AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel`. The source deduces the
> clause from [Stacks, Tag 0B91], whose perfectness half this library does not carry — see the
> module documentation of
> `StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChange.lean` — so the route
> taken instead is the Noetherian special case [Stacks, Tag 0B6F] of that tag, which is why
> `IsNoetherian Y` appears and `LocallyOfFinitePresentation f` does not enter the proof.

```lean
theorem isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlat [IsNoetherian Y] [IsProper f]
    [Flat f] [LocallyOfFinitePresentation f]
    (D : RingedSpace.CertifiedDerivedSheafTensoring
      (RingedSpace.inverseImage Y.toRingedSpace (Limits.pullback.snd f g).base))
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : IsPerfect (X := (Limits.pullback f g).toRingedSpace) K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (hTor : D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction
      (Limits.pullback.snd f g)).obj (fourierMukaiKernelTensor f g K M)))
    (hpushforwardCoherence : Stacks.Cohomology.PerfectPushforward.PushforwardCoherenceResidue
      (Limits.pullback.snd f g) (derivedPushforwardOX (Limits.pullback.snd f g)))
    (hpushforwardTorDimension :
      Stacks.Cohomology.PerfectPushforward.PushforwardTorDimensionResidue
        (Limits.pullback.snd f g) D (derivedPushforwardOX (Limits.pullback.snd f g))) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_noetherianBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L466). The attribute's comment: “clause (4), reduced to clause (3) by Tag 01TX; Tag 08EV's two residues and its Tor-dimension clause for L pr₁^* M ⊗ᴸ K are carried, and Y is assumed Noetherian”.

> **[Stacks, Tag 0FYT], clause (4).** Let `S` be Noetherian, let `X ⟶ S` be flat and proper
> and let `K` be a perfect object of `D(𝒪_{X ×_S Y})`. Then `Φ_K` sends `D_perf(𝒪_X)` into
> `D_perf(𝒪_Y)`.
>
> The source says: part (4) follows from part (3) and the fact that a finite type morphism of
> Noetherian schemes is of finite presentation, [Stacks, Tag 01TX]. That is what is done here:
> `X ⟶ S` is proper, hence of finite type, and `S` is Noetherian, so
> `AlgebraicGeometry.finitePresentation_of_finiteType` makes it of finite presentation and
> `AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlat` applies.

```lean
theorem isPerfect_fourierMukai_of_isPerfect_kernel_of_noetherianBase [IsNoetherian S]
    [IsNoetherian Y] [IsProper f] [Flat f]
    (D : RingedSpace.CertifiedDerivedSheafTensoring
      (RingedSpace.inverseImage Y.toRingedSpace (Limits.pullback.snd f g).base))
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : IsPerfect (X := (Limits.pullback f g).toRingedSpace) K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (hTor : D.HasFiniteTorDimension ((Scheme.Hom.derivedScalarRestriction
      (Limits.pullback.snd f g)).obj (fourierMukaiKernelTensor f g K M)))
    (hpushforwardCoherence : Stacks.Cohomology.PerfectPushforward.PushforwardCoherenceResidue
      (Limits.pullback.snd f g) (derivedPushforwardOX (Limits.pullback.snd f g)))
    (hpushforwardTorDimension :
      Stacks.Cohomology.PerfectPushforward.PushforwardTorDimensionResidue
        (Limits.pullback.snd f g) D (derivedPushforwardOX (Limits.pullback.snd f g))) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfectRelativeTo_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L551). The attribute's comment: “clause (5): K is Y-perfect; Tag 0DI4's own hypotheses are carried and Y is assumed Noetherian, Tag 0DJT being applied in its Noetherian-base form”.

> **The common core of clauses (5) and (6) of [Stacks, Tag 0FYT].** Let `X ⟶ S` be proper,
> flat and locally of finite presentation, let `Y` be Noetherian and let `K` be a `Y`-perfect
> object of `D(𝒪_{X ×_S Y})` in the sense of [Stacks, Tag 0DI0]. Then `Φ_K` sends `D_perf(𝒪_X)`
> into `D_perf(𝒪_Y)`.
>
> This is the source's route. `L pr_1^* M` is perfect by [Stacks, Tag 09UA]; the second assertion
> of [Stacks, Tag 0DI4] makes `T = L pr_1^* M ⊗^𝐋 K` `Y`-perfect, `pr_2 : X ×_S Y ⟶ Y` being
> proper, flat and locally of finite presentation by base change; and the perfectness clause of
> [Stacks, Tag 0DJT] then makes `R pr_{2,*} T` perfect.
>
> `IsNoetherian Y` is a hypothesis neither clause makes. It is what the form of
> [Stacks, Tag 0DJT] used here asks: `isPerfect_derivedPushforward_of_isPerfectRelativeTo` is the
> Noetherian case, stated for an arbitrary pinned certificate family `D`, while the tag over an
> arbitrary base (`isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap`) is stated at the
> canonical certificate family.
>
> Everything else carried below is a hypothesis of [Stacks, Tag 0DI4] in this library, passed
> through unchanged, and each is documented at its source:
>
> * `D` is the family of certified derived tensor products on the open subspaces of
>   `(X ×_S Y, pr_2^{-1}𝒪_Y)`, which is how part (3) of [Stacks, Tag 08CG] is expressed, and `hD`
>   pins its underived tensor product to the genuine one of [Stacks, Tag 06YU] — without that
>   pinning the Tor clause of relative perfectness carries no information.
> * `commShift` and `triangulated` are exactness of each `- ⊗^{L} ℱ[0]`, and `hrestricts` is
>   locality of finite Tor dimension; these are the hypotheses [Stacks, Tag 0DI3] is stated with
>   in this development.
> * `hcl` is the complex level of [Stacks, Tag 09J3] — the step the source states with "details
>   omitted".
> * `hind` is `AlgebraicGeometry.Scheme.Hom.StrictlyPerfectInduction`, the generic triangulated
>   induction peeling the top term off a bounded complex; it mentions neither `pr_2` nor `K`.
> * `Θ`, `ΘcommShift`, `Θtriangulated`, `Θunit` and `Θtensor` are the interaction of the derived
>   tensor product with restriction to open subspaces, as [Stacks, Tag 0DI4] asks for it here.

```lean
theorem isPerfect_fourierMukai_of_isPerfectRelativeTo_kernel [IsNoetherian Y]
    (hD : IsGenuineTensorFamily (Limits.pullback.snd f g) D)
    (hrestricts : RingedSpace.FiniteTorDimensionRestricts (fourierMukaiInverseImage f g) D)
    (hind : Scheme.Hom.StrictlyPerfectInduction.{u + 1, u})
    (hcl : Stacks.Cohomology.PseudoCoherentTensor.ComplexLevel.{u})
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (Θ : ∀ (V : Opens (fourierMukaiInverseImage f g).carrier)
        (W : Opens (Limits.pullback f g : Scheme.{u}).toRingedSpace.carrier),
        (∀ x, x ∈ V → x ∈ W) →
      DerivedCategory (StrictlyPerfect.OXMod.{u, u}
        ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding)) ⥤
        DerivedCategory (StrictlyPerfect.OXMod.{u, u}
          ((fourierMukaiInverseImage f g).restrict V.isOpenEmbedding)))
    (ΘcommShift : ∀ V W h, (Θ V W h).CommShift ℤ)
    (Θtriangulated : ∀ V W h, have := ΘcommShift V W h; (Θ V W h).IsTriangulated)
    (Θunit : ∀ V W h, (Θ V W h).obj ((DerivedCategory.singleFunctor
        (StrictlyPerfect.OXMod.{u, u}
          ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding)) 0).obj
          (StrictlyPerfect.structureModule
            ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding))) ≅
      (RingedSpace.derivedRestrictModules (fourierMukaiInverseImage f g) V).obj
        ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.snd f g)).obj K))
    (Θtensor : ∀ (V W h) (A : DerivedCategory
        (StrictlyPerfect.OXMod.{u, u} (Limits.pullback f g).toRingedSpace)),
      (Θ V W h).obj
          ((RingedSpace.derivedRestrictModules (Limits.pullback f g).toRingedSpace W).obj A) ≅
        (RingedSpace.derivedRestrictModules (fourierMukaiInverseImage f g) V).obj
          ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.snd f g)).obj
            (((Stacks.Cohomology.PseudoCoherentTensor.derivedTensorProduct
              (Limits.pullback f g).toRingedSpace).tensor.obj A).obj K)))
    (hK : (Limits.pullback.snd f g).IsPerfectRelativeTo D K) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfectRelativeTo_kernel_of_noetherianBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservation.lean#L634). The attribute's comment: “clause (6), reduced to clause (5) by Tag 01TX part (1); Tag 0DI4's own hypotheses are carried and Y is assumed Noetherian”.

> **[Stacks, Tag 0FYT], clause (6).** Let `S` be Noetherian, let `X ⟶ S` be flat and proper,
> let `Y` be Noetherian and let `K` be a `Y`-perfect object of `D(𝒪_{X ×_S Y})`. Then `Φ_K` sends
> `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> The source says: part (6) follows from part (5) in the same way that part (4) follows from
> part (3), that is through [Stacks, Tag 01TX]. That is what happens here, and it happens by
> instance search: `X ⟶ S` is proper, hence locally of finite type, and `S` is Noetherian, hence
> locally Noetherian, so part (1) of [Stacks, Tag 01TX] — Mathlib's
> `AlgebraicGeometry.instLocallyOfFinitePresentationOfIsLocallyNoetherianOfLocallyOfFiniteType`,
> recorded against that tag in
> `StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/LocallyNoetherian.lean` — supplies
> the `AlgebraicGeometry.LocallyOfFinitePresentation` instance that
> `AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfectRelativeTo_kernel` asks for, and no other
> hypothesis changes.
>
> `IsNoetherian Y` is carried for the same reason as in clause (5): the form of
> [Stacks, Tag 0DJT] used there is its Noetherian case, and `S` Noetherian says nothing about
> `Y`.

```lean
theorem isPerfect_fourierMukai_of_isPerfectRelativeTo_kernel_of_noetherianBase [IsNoetherian Y]
    (hD : IsGenuineTensorFamily (Limits.pullback.snd f g) D)
    (hrestricts : RingedSpace.FiniteTorDimensionRestricts (fourierMukaiInverseImage f g) D)
    (hind : Scheme.Hom.StrictlyPerfectInduction.{u + 1, u})
    (hcl : Stacks.Cohomology.PseudoCoherentTensor.ComplexLevel.{u})
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M)
    (Θ : ∀ (V : Opens (fourierMukaiInverseImage f g).carrier)
        (W : Opens (Limits.pullback f g : Scheme.{u}).toRingedSpace.carrier),
        (∀ x, x ∈ V → x ∈ W) →
      DerivedCategory (StrictlyPerfect.OXMod.{u, u}
        ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding)) ⥤
        DerivedCategory (StrictlyPerfect.OXMod.{u, u}
          ((fourierMukaiInverseImage f g).restrict V.isOpenEmbedding)))
    (ΘcommShift : ∀ V W h, (Θ V W h).CommShift ℤ)
    (Θtriangulated : ∀ V W h, have := ΘcommShift V W h; (Θ V W h).IsTriangulated)
    (Θunit : ∀ V W h, (Θ V W h).obj ((DerivedCategory.singleFunctor
        (StrictlyPerfect.OXMod.{u, u}
          ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding)) 0).obj
          (StrictlyPerfect.structureModule
            ((Limits.pullback f g).toRingedSpace.restrict W.isOpenEmbedding))) ≅
      (RingedSpace.derivedRestrictModules (fourierMukaiInverseImage f g) V).obj
        ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.snd f g)).obj K))
    (Θtensor : ∀ (V W h) (A : DerivedCategory
        (StrictlyPerfect.OXMod.{u, u} (Limits.pullback f g).toRingedSpace)),
      (Θ V W h).obj
          ((RingedSpace.derivedRestrictModules (Limits.pullback f g).toRingedSpace W).obj A) ≅
        (RingedSpace.derivedRestrictModules (fourierMukaiInverseImage f g) V).obj
          ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.snd f g)).obj
            (((Stacks.Cohomology.PseudoCoherentTensor.derivedTensorProduct
              (Limits.pullback f g).toRingedSpace).tensor.obj A).obj K)))
    (hK : (Limits.pullback.snd f g).IsPerfectRelativeTo D K) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_boundedCoherent_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L177). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0FYT], clause (1).** Let `S` be Noetherian, let `X ⟶ S` and `Y ⟶ S` be of
> finite type and let `K ∈ D^b_{Coh}(𝒪_{X ×_S Y})` be such that the support of every `H^i(K)` is
> proper over `Y` and `K` has finite Tor dimension as an object of `D(pr_2^{-1}𝒪_Y)`. Then `Φ_K`
> sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> The support of a coherent `H^i(K)` is closed, and `hsupp` asks that this closed subset be proper
> over `Y`. The proof is [Stacks, Tag 08EV] for `pr_2` applied to `T = L pr_1^* M ⊗^𝐋 K`, with each
> of its hypotheses on `T` derived from those on `K`; see the module documentation.

```lean
theorem isPerfect_fourierMukai_of_boundedCoherent_kernel
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun F : (Limits.pullback f g).Modules => F.IsCoherent) K)
    (hsupp : ∀ (j : ℤ) (hcl : IsClosed (SheafOfModules.supp
      ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj K))),
      IsProperOver (Limits.pullback.snd f g) ⟨_, hcl⟩)
    (hTor : Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension
      (RingedSpace.inverseImage Y.toRingedSpace (Limits.pullback.snd f g).base)
      ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.snd f g)).obj K))
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_flatProperSupportFinitelyPresented_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L226). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0FYT], clause (2).** Let `X ⟶ S` be of finite presentation and let `K` be
> represented by a bounded complex `𝒦^•` of finitely presented `𝒪_{X ×_S Y}`-modules, flat over
> `Y`, with support proper over `Y`. Then `Φ_K` sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> This is [Stacks, Tag 0A1H] for `pr_2 : X ×_S Y ⟶ Y`, which is of finite presentation by base
> change, with `E = L pr_1^* M`, perfect by [Stacks, Tag 09UA].

```lean
theorem isPerfect_fourierMukai_of_flatProperSupportFinitelyPresented_kernel
    [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (G : CochainComplex (Limits.pullback f g).Modules ℤ)
    (hG : FlatProperSupportFinitelyPresented (Limits.pullback.snd f g) G)
    (K : DerivedCategory (Limits.pullback f g).Modules) (e : DerivedCategory.Q.obj G ≅ K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlatFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L255). The attribute's comment: “part (3)”.

> **[Stacks, Tag 0FYT], clause (3).** Let `X ⟶ S` be a proper flat morphism of finite
> presentation and let `K` be perfect. Then `Φ_K` sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> `T = L pr_1^* M ⊗^𝐋 K` is perfect, hence `Y`-perfect by the first assertion of
> [Stacks, Tag 0DI4], and [Stacks, Tag 0DJT] for the proper, flat, finitely presented `pr_2` makes
> `R pr_{2,*} T` perfect.

```lean
theorem isPerfect_fourierMukai_of_isPerfect_kernel_of_properFlatFinitePresentation
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : IsPerfect (X := (Limits.pullback f g).toRingedSpace) K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isPerfect_kernel_of_noetherian_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L273). The attribute's comment: “part (4)”.

> **[Stacks, Tag 0FYT], clause (4).** Let `S` be Noetherian, let `X ⟶ S` be flat and proper and
> let `K` be perfect. Then `Φ_K` sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> As in the source this is clause (3): `X ⟶ S` is of finite type over a Noetherian scheme, hence
> locally of finite presentation by [Stacks, Tag 01TX], an instance found by instance search.

```lean
theorem isPerfect_fourierMukai_of_isPerfect_kernel_of_noetherian_properFlat [IsNoetherian S]
    [IsProper f] [Flat f]
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : IsPerfect (X := (Limits.pullback f g).toRingedSpace) K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isRelativelyPerfect_kernel_of_properFlatFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L290). The attribute's comment: “part (5)”.

> **[Stacks, Tag 0FYT], clause (5).** Let `X ⟶ S` be a proper flat morphism of finite
> presentation and let `K` be `Y`-perfect ([Stacks, Tag 0DI0]). Then `Φ_K` sends `D_perf(𝒪_X)`
> into `D_perf(𝒪_Y)`.
>
> The second assertion of [Stacks, Tag 0DI4] makes `T = L pr_1^* M ⊗^𝐋 K` `Y`-perfect, and
> [Stacks, Tag 0DJT] for `pr_2` makes `R pr_{2,*} T` perfect.

```lean
theorem isPerfect_fourierMukai_of_isRelativelyPerfect_kernel_of_properFlatFinitePresentation
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : (Limits.pullback.snd f g).IsRelativelyPerfect K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

**`AlgebraicGeometry.isPerfect_fourierMukai_of_isRelativelyPerfect_kernel_of_noetherian_properFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectPreservationCriteria.lean#L308). The attribute's comment: “part (6)”.

> **[Stacks, Tag 0FYT], clause (6).** Let `S` be Noetherian, let `X ⟶ S` be flat and proper and
> let `K` be `Y`-perfect. Then `Φ_K` sends `D_perf(𝒪_X)` into `D_perf(𝒪_Y)`.
>
> This is clause (5), `X ⟶ S` being locally of finite presentation by [Stacks, Tag 01TX].

```lean
theorem isPerfect_fourierMukai_of_isRelativelyPerfect_kernel_of_noetherian_properFlat
    [IsNoetherian S] [IsProper f] [Flat f]
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : (Limits.pullback.snd f g).IsRelativelyPerfect K)
    (M : DerivedCategory X.Modules) (hM : IsPerfect (X := X.toRingedSpace) M) :
    IsPerfect (X := Y.toRingedSpace) ((fourierMukai f g K).obj M)
```

## Tag 0FYU, a lemma

[Tag 0FYU](https://stacks.math.columbia.edu/tag/0FYU) in the Stacks Project.

**`AlgebraicGeometry.fourierMukai_derivedCategoryBBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/BoundedCoherentConditions.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/BoundedCoherentConditions.lean#L543). The attribute's comment: “Φ\_K maps D^b\_Coh(O\_X) into D^b\_Coh(O\_Y) under each of (1)-(4); the support requirement is automatic when X → S is proper”. References: SGA 6 I (5.8.4), “5.8.4 b), special case”.

> **[Stacks, Tag 0FYU].** Let `S` be a Noetherian scheme, let `X` and `Y` be schemes of finite
> type over `S` and let `K ∈ D^b_Coh(𝒪_{X ×_S Y})`. The Fourier-Mukai functor `Φ_K` sends
> `D^b_Coh(𝒪_X)` into `D^b_Coh(𝒪_Y)` if at least one of the following holds:
>
> 1. the support of `H^i(K)` is proper over `Y` for all `i`, and `K` has finite Tor dimension as
>    an object of `D(pr_1^{-1}𝒪_X)`;
> 2. `K` can be represented by a bounded complex `𝒦^•` of coherent `𝒪_{X ×_S Y}`-modules, flat
>    over `X`, with support proper over `Y`;
> 3. the support of `H^i(K)` is proper over `Y` for all `i`, and `X` is a regular scheme;
> 4. `K` is perfect, the support of `H^i(K)` is proper over `Y` for all `i`, and `Y ⟶ S` is flat.
>
> Furthermore, in each case the support condition is automatic if `X ⟶ S` is proper: then every
> closed subset of `X ×_S Y` is proper over `Y`.
>
> The support of a bounded complex of coherent modules is the union of the supports of its
> finitely many nonzero terms; it is written as a closed subset proper over `Y` containing each of
> them. Finite Tor dimension over `pr_1^{-1}𝒪_X` is [Stacks, Tag 08CG] on the inverse-image ringed
> space `(X ×_S Y, pr_1^{-1}𝒪_X)`, after restriction of scalars along
> `pr_1^{-1}𝒪_X ⟶ 𝒪_{X ×_S Y}`.

```lean
theorem fourierMukai_derivedCategoryBBounded
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun F : (Limits.pullback f g).Modules => F.IsCoherent) K) :
    ((((∀ (i : ℤ) (hcl : IsClosed (SheafOfModules.supp
          ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).obj K))),
          IsProperOver (Limits.pullback.snd f g) ⟨_, hcl⟩) ∧
        Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension
          (RingedSpace.inverseImage X.toRingedSpace (Limits.pullback.fst f g).base)
          ((Scheme.Hom.derivedScalarRestriction (Limits.pullback.fst f g)).obj K)) ∨
      (∃ C : CochainComplex (Limits.pullback f g).Modules ℤ,
        (∃ a b : ℤ, C.IsStrictlyGE a ∧ C.IsStrictlyLE b) ∧
        (∀ i : ℤ, (C.X i).IsCoherent) ∧
        (∀ i : ℤ, IsFlatOver (Limits.pullback.fst f g).toLRSHom.toShHom (C.X i)) ∧
        (∃ Z : Closeds (Limits.pullback f g : Scheme.{u}),
          IsProperOver (Limits.pullback.snd f g) Z ∧
          ∀ i : ℤ, SheafOfModules.supp (C.X i) ⊆ (Z : Set (Limits.pullback f g : Scheme.{u}))) ∧
        Nonempty (DerivedCategory.Q.obj C ≅ K)) ∨
      ((∀ (i : ℤ) (hcl : IsClosed (SheafOfModules.supp
          ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).obj K))),
          IsProperOver (Limits.pullback.snd f g) ⟨_, hcl⟩) ∧ IsRegular X) ∨
      (RingedSpace.IsPerfect (X := (Limits.pullback f g).toRingedSpace) K ∧
        (∀ (i : ℤ) (hcl : IsClosed (SheafOfModules.supp
          ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).obj K))),
          IsProperOver (Limits.pullback.snd f g) ⟨_, hcl⟩) ∧ Flat g)) →
      ∀ M : DerivedCategory X.Modules,
        DerivedCategoryB.derivedCategoryBBounded (fun F : X.Modules => F.IsCoherent) M →
        DerivedCategoryB.derivedCategoryBBounded (fun N : Y.Modules => N.IsCoherent)
          ((fourierMukai f g K).obj M)) ∧
    (IsProper f → ∀ T : Closeds (Limits.pullback f g : Scheme.{u}),
      IsProperOver (Limits.pullback.snd f g) T)
```

## Tag 0FYV, an example

[Tag 0FYV](https://stacks.math.columbia.edu/tag/0FYV) in the Stacks Project.

**`AlgebraicGeometry.diagonalKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernel.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernel.lean#L117). The attribute's comment: “the diagonal kernel `𝒪_Δ = RΔ_{X/S,*}𝒪_X` as an object of `D(𝒪_{X ×_S X})`; the clause that it is of finite type and flat over either projection is not covered, and the clause that `Φ_{𝒪_Δ}` is the identity functor of `D(𝒪_X)` is carried by `AlgebraicGeometry.fourierMukaiDiagonalKernelIso` in `FourierMukai/DiagonalKernelIdentity.lean`”.

> **The diagonal kernel of [Stacks, Tag 0FYV]**: the object
>
> `𝒪_Δ = RΔ_{X/S,*}𝒪_X ∈ D(𝒪_{X ×_S X})`,
>
> the derived direct image along the diagonal `Δ : X ⟶ X ×_S X` of the structure sheaf of `X`
> placed in degree `0`.
>
> This is the object the source's Example 0FYV introduces, and the one against which the
> convolution of [Stacks, Tag 0FYS] is compared in the definition of a relative equivalence,
> [Stacks, Tag 0G0I]. The source writes it as `Δ_*𝒪_X` and identifies that with `RΔ_*𝒪_X` using
> that `Δ` is a closed immersion for separated `f`; the derived spelling is taken here, so no
> hypothesis on `f` is needed, and the identification with the ordinary direct image is not
> formalized. That `Φ_{𝒪_Δ}` is the identity is
> `AlgebraicGeometry.fourierMukaiDiagonalKernelIso`; the assertion of 0FYV that `𝒪_Δ` is of
> finite type and flat over either projection is not formalized — see the module docstring.

```lean
def diagonalKernel : DerivedCategory (Limits.pullback f f).Modules
```

**`AlgebraicGeometry.isQuasicoherent_homology_diagonalKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernel.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernel.lean#L130). The attribute's comment: “quasi-coherence of the diagonal kernel `𝒪_Δ`, for `f` separated”.

> **The diagonal kernel of a separated morphism has quasi-coherent cohomology**, which is the
> assertion of [Stacks, Tag 0FYV] that `𝒪_Δ` is a quasi-coherent `𝒪_{X ×_S X}`-module.
>
> The structure sheaf of `X` is quasi-coherent, and the derived direct image along a quasi-compact
> quasi-separated morphism preserves quasi-coherence of cohomology ([Stacks, Tag 08D5] part (1),
> here in the single-degree case). The diagonal of a separated morphism is a closed immersion,
> hence affine, hence quasi-compact; and it is a split mono, hence separated, hence
> quasi-separated.

```lean
theorem isQuasicoherent_homology_diagonalKernel [IsSeparated f] (i : ℤ) :
    ((DerivedCategory.homologyFunctor (Limits.pullback f f).Modules i).obj
      (diagonalKernel f)).IsQuasicoherent
```

**`AlgebraicGeometry.fourierMukaiPullbackTensorDiagonalKernelIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean#L106). The attribute's comment: “the chain the example displays, `L pr_1^*(-) ⊗^𝐋 𝒪_Δ ≅ RΔ_*(-)`, as an isomorphism of functors, for `f` separated”.

> **The chain [Stacks, Tag 0FYV] displays.**  For a separated morphism of schemes `f : X ⟶ S`
> and any `M ∈ D(𝒪_X)`,
>
> `L pr_1^*M ⊗^𝐋_{𝒪_{X ×_S X}} 𝒪_Δ = RΔ_*(LΔ^*L pr_1^*M ⊗^𝐋_{𝒪_X} 𝒪_X) = RΔ_*M`,
>
> read as an isomorphism of functors `D(𝒪_X) ⥤ D(𝒪_{X ×_S X})`, hence natural in `M`.
>
> The first equality is `AlgebraicGeometry.dtenDerivedPushforwardUnitIso` at the closed immersion
> `Δ`: the projection formula [Stacks, Tag 0B55], which is the source's own justification for it,
> with the factor `𝒪_X` absorbed by the unitor.  The second is the composition isomorphism of
> [Stacks, Tag 0D5S], `AlgebraicGeometry.dpullCompFstIso`, followed by `pr_1 ∘ Δ = 𝟙_X`, again as
> in the source.  Pushing this forward along `pr_2` is the source's closing sentence and gives
> `AlgebraicGeometry.fourierMukaiDiagonalKernelIso` below.

```lean
def fourierMukaiPullbackTensorDiagonalKernelIso :
    fourierMukaiPullback f f ⋙ fourierMukaiTensor f f (diagonalKernel f) ≅
      dpush (Limits.pullback.diagonal f)
```

**`AlgebraicGeometry.fourierMukaiDiagonalKernelIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean#L131). The attribute's comment: “the Fourier-Mukai functor of the diagonal kernel is the identity, for `f` separated”.

> **The closing assertion of [Stacks, Tag 0FYV].**  For a separated morphism of schemes
> `f : X ⟶ S` the Fourier-Mukai functor of the diagonal kernel `𝒪_Δ = RΔ_{X/S,*}𝒪_X` is the
> identity functor of `D(𝒪_X)`:
>
> `Φ_{𝒪_Δ} = R pr_{2,*}(L pr_1^*(-) ⊗^𝐋_{𝒪_{X ×_S X}} 𝒪_Δ) ≅ 𝟭`.
>
> The diagonal is a closed immersion and a section of the second projection, so
> `AlgebraicGeometry.fourierMukaiIsoDerivedPullback_of_comp_snd_eq_id` — the general computation of
> `Φ_{Rs_*𝒪_Z}` at a closed immersion `s` into the product, specialised to a section — gives
> `Φ_{𝒪_Δ} ≅ L(Δ ≫ pr_1)^*`; and `Δ ≫ pr_1 = 𝟙_X`, whose derived pullback is the identity by
> `AlgebraicGeometry.dpullIdIso`.

```lean
def fourierMukaiDiagonalKernelIso :
    fourierMukai f f (diagonalKernel f) ≅ 𝟭 (DerivedCategory X.Modules)
```

**`AlgebraicGeometry.isFourierMukaiKernel_diagonalKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalKernelIdentity.lean#L141). The attribute's comment: “the diagonal kernel is a Fourier-Mukai kernel for the identity functor”.

> **`𝒪_Δ` is a Fourier-Mukai kernel for the identity functor**, in the sense of
> `AlgebraicGeometry.IsFourierMukaiKernel`; this is [Stacks, Tag 0FYV] read through the
> vocabulary of [Stacks, Tag 0FYQ].

```lean
theorem isFourierMukaiKernel_diagonalKernel :
    IsFourierMukaiKernel f f (𝟭 (DerivedCategory X.Modules)) (diagonalKernel f)
```

**`AlgebraicGeometry.diagonalModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L114). The attribute's comment: “the `𝒪_{X ×_S X}`-module `𝒪_Δ = Δ_{X/S,*}𝒪_X`”.

> **The structure sheaf of the diagonal, [Stacks, Tag 0FYV]**: the `𝒪_{X ×_S X}`-module
>
> `𝒪_Δ = Δ_{X/S,*}𝒪_X`,
>
> the ordinary direct image along the diagonal `Δ : X ⟶ X ×_S X` of the structure sheaf of `X`.
>
> This is the module the source's Example 0FYV writes `Δ_*\mathcal{O}_X`; its identification with
> the derived direct image `RΔ_*𝒪_X`, which is `AlgebraicGeometry.diagonalKernel`, is
> `AlgebraicGeometry.diagonalKernelIsoDiagonalModule`.

```lean
def diagonalModule : (Limits.pullback f f).Modules
```

**`AlgebraicGeometry.diagonalModule_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L129). The attribute's comment: “`𝒪_Δ = Δ_*𝒪_X` is a quasi-coherent `𝒪_{X ×_S X}`-module, for `f` separated”.

> **`𝒪_Δ` is a quasi-coherent `𝒪_{X ×_S X}`-module**, part of the assertion of
> [Stacks, Tag 0FYV].  The diagonal of a separated morphism is a closed immersion, hence an
> affine morphism, and the direct image of the structure sheaf along an affine morphism is
> quasi-coherent.

```lean
theorem diagonalModule_isQuasicoherent [IsSeparated f] :
    (diagonalModule f).IsQuasicoherent
```

**`AlgebraicGeometry.diagonalModule_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L143). The attribute's comment: “`𝒪_Δ = Δ_*𝒪_X` is of finite type, for `f` separated”.

> **`𝒪_Δ` is of finite type**, part of the assertion of [Stacks, Tag 0FYV].  Finite type is
> Mathlib's `SheafOfModules.IsFiniteType`, [Stacks, Tag 01B4]: locally generated by finitely many
> sections.
>
> The canonical map `𝒪_{X ×_S X} ⟶ Δ_*𝒪_X` is an epimorphism of `𝒪_{X ×_S X}`-modules, because
> the comorphism of structure sheaves of a closed immersion is locally surjective; the structure
> sheaf is of finite type, being generated by the single section `1`; and finite type passes to
> quotients.

```lean
theorem diagonalModule_isFiniteType [IsSeparated f] :
    (diagonalModule f).IsFiniteType
```

**`AlgebraicGeometry.diagonalModule_isFlatOver_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L183). The attribute's comment: “`𝒪_Δ = Δ_*𝒪_X` is flat over `X` under the first projection, for `f` separated”.

> **`𝒪_Δ` is flat over `X` under the first projection**, part of the assertion of
> [Stacks, Tag 0FYV].

```lean
theorem diagonalModule_isFlatOver_fst [IsSeparated f] :
    IsFlatOver (Limits.pullback.fst f f).toLRSHom.toShHom (diagonalModule f)
```

**`AlgebraicGeometry.diagonalModule_isFlatOver_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L190). The attribute's comment: “`𝒪_Δ = Δ_*𝒪_X` is flat over `X` under the second projection, for `f` separated”.

> **`𝒪_Δ` is flat over `X` under the second projection**, part of the assertion of
> [Stacks, Tag 0FYV].

```lean
theorem diagonalModule_isFlatOver_snd [IsSeparated f] :
    IsFlatOver (Limits.pullback.snd f f).toLRSHom.toShHom (diagonalModule f)
```

**`AlgebraicGeometry.diagonalKernelIsoDiagonalModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L205). The attribute's comment: “`𝒪_Δ = Δ_*𝒪_X = RΔ_*𝒪_X`: the ordinary and the derived direct image of `𝒪_X` along the diagonal agree, for `f` separated”.

> **`Δ_*𝒪_X = RΔ_*𝒪_X`**, the source's identification in [Stacks, Tag 0FYV]: for `f`
> separated the diagonal kernel `𝒪_Δ = RΔ_*𝒪_X` of `AlgebraicGeometry.diagonalKernel` is the
> ordinary direct image `Δ_*𝒪_X` placed in degree zero.
>
> The diagonal of a separated morphism is a closed immersion, along which pushforward of sheaves
> of modules is exact ([Stacks, Tag 08KS]); so `RΔ_*` is the functor `Δ_*` induces on derived
> categories, and an exact functor commutes with placing a module in degree zero.

```lean
def diagonalKernelIsoDiagonalModule [IsSeparated f] :
    diagonalKernel f ≅
      (DerivedCategory.singleFunctor (Limits.pullback f f).Modules 0).obj (diagonalModule f)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsSeparated.isClosedImmersion_diagonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsSeparated.isClosedImmersion_diagonal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/DiagonalModule.lean#L121) (StacksFrontier): “the diagonal `Δ : X ⟶ X ×_S X` of a separated morphism is a closed immersion”.

## Tag 0FYW, a lemma

[Tag 0FYW](https://stacks.math.columbia.edu/tag/0FYW) in the Stacks Project.

**`AlgebraicGeometry.fourierMukaiRightAdjointComparison_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RightAdjoint.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/RightAdjoint.lean#L357).

> **[Stacks, Tag 0FYW].** Let `X ⟶ S` and `Y ⟶ S` be morphisms of quasi-compact and
> quasi-separated schemes. Let `Φ : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` be the Fourier-Mukai functor of a
> pseudo-coherent kernel `K ∈ D_QCoh(𝒪_{X ×_S Y})` (`AlgebraicGeometry.fourierMukaiTransform`),
> let `a : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_{X ×_S Y})` be the right adjoint of `Rpr_{2,*}`
> ([Stacks, Tag 0A9E]), let `K' = (Y ×_S X → X ×_S Y)^* R𝓗om(K, a(𝒪_Y))`
> (`AlgebraicGeometry.fourierMukaiRightAdjointKernel`) and let `Φ' : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)` be
> its Fourier-Mukai transform (`AlgebraicGeometry.fourierMukaiRightAdjoint`). Then:
> * `K'` lies in `D_QCoh(𝒪_{Y ×_S X})`;
> * the canonical map `Hom_X(M, Φ'(N)) ⟶ Hom_Y(Φ(M), N)`
>   (`AlgebraicGeometry.fourierMukaiRightAdjointComparison`) is functorial in `M ∈ D_QCoh(𝒪_X)` and
>   `N ∈ D_QCoh(𝒪_Y)`;
> * it is an isomorphism if (1) `N` is perfect, or (2) `K` is perfect and `X ⟶ S` is proper, flat
>   and of finite presentation.
>
> The quasi-compactness and quasi-separatedness of the morphisms and of the two fibre products, which
> the constructions ask for, follow from the hypotheses
> (`AlgebraicGeometry.fourierMukaiRightAdjoint_instances`).

```lean
theorem fourierMukaiRightAdjointComparison_spec
    (K : @DerivedCategory (pullback f g).Modules _ _ (HasDerivedCategory.standard _))
    (hK : ∀ j : ℤ, ((@DerivedCategory.homologyFunctor (pullback f g).Modules _ _
      (HasDerivedCategory.standard _) j).obj K).IsQuasicoherent)
    (hpc : @RingedSpace.IsPseudoCoherent (pullback f g).toRingedSpace
      (HasDerivedCategory.standard _) K) :
    haveI : QuasiCompact f := (fourierMukaiRightAdjoint_instances f g).1
    haveI : QuasiSeparated f := (fourierMukaiRightAdjoint_instances f g).2.1
    haveI : QuasiCompact g := (fourierMukaiRightAdjoint_instances f g).2.2.1
    haveI : QuasiSeparated g := (fourierMukaiRightAdjoint_instances f g).2.2.2.1
    haveI : CompactSpace (pullback f g : Scheme.{u}) :=
      (fourierMukaiRightAdjoint_instances f g).2.2.2.2.1
    haveI : QuasiSeparatedSpace (pullback f g : Scheme.{u}) :=
      (fourierMukaiRightAdjoint_instances f g).2.2.2.2.2.1
    haveI : CompactSpace (pullback g f : Scheme.{u}) :=
      (fourierMukaiRightAdjoint_instances f g).2.2.2.2.2.2.1
    haveI : QuasiSeparatedSpace (pullback g f : Scheme.{u}) :=
      (fourierMukaiRightAdjoint_instances f g).2.2.2.2.2.2.2
    (∀ j : ℤ, ((@DerivedCategory.homologyFunctor (pullback g f).Modules _ _
        (HasDerivedCategory.standard _) j).obj
          (fourierMukaiRightAdjointKernel f g K hK hpc)).IsQuasicoherent) ∧
    (∀ {M M' : StdQCoh X} (m : M' ⟶ M) (N : StdQCoh Y)
        (v : M ⟶ (fourierMukaiRightAdjoint f g K hK hpc).obj N),
      fourierMukaiRightAdjointComparison f g K hK hpc M' N (m ≫ v) =
        (fourierMukaiTransform f g K hK).map m ≫
          fourierMukaiRightAdjointComparison f g K hK hpc M N v) ∧
    (∀ (M : StdQCoh X) {N N' : StdQCoh Y} (n : N ⟶ N')
        (v : M ⟶ (fourierMukaiRightAdjoint f g K hK hpc).obj N),
      fourierMukaiRightAdjointComparison f g K hK hpc M N'
          (v ≫ (fourierMukaiRightAdjoint f g K hK hpc).map n) =
        fourierMukaiRightAdjointComparison f g K hK hpc M N v ≫ n) ∧
    (∀ (M : StdQCoh X) (N : StdQCoh Y),
      @Stacks.Cohomology.PerfectComplexes.IsPerfect Y.toRingedSpace
        (HasDerivedCategory.standard _) N.obj →
      Function.Bijective (fourierMukaiRightAdjointComparison f g K hK hpc M N)) ∧
    (IsProper f → Flat f → LocallyOfFinitePresentation f →
      @Stacks.Cohomology.PerfectComplexes.IsPerfect (pullback f g).toRingedSpace
        (HasDerivedCategory.standard _) K →
      ∀ (M : StdQCoh X) (N : StdQCoh Y),
        Function.Bijective (fourierMukaiRightAdjointComparison f g K hK hpc M N))
```

## Tag 0FYX, a lemma

[Tag 0FYX](https://stacks.math.columbia.edu/tag/0FYX) in the Stacks Project.

**`AlgebraicGeometry.fourierMukaiLeftAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/LeftAdjoint.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/LeftAdjoint.lean#L181).

> **[Stacks, Tag 0FYX].** Let `S` be a Noetherian scheme, `g : Y ⟶ S` a flat proper Gorenstein
> morphism and `f : X ⟶ S` a morphism of finite type. Let `K` be a perfect object of
> `D_QCoh(𝒪_{X ×_S Y})`, `Φ : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` its Fourier-Mukai transform, and `Φ'`
> the Fourier-Mukai transform `D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)` of
> `K' = (Y ×_S X → X ×_S Y)^*(K^∨ ⊗ᴸ Lpr_2^*ω^•_{Y/S})`
> (`AlgebraicGeometry.fourierMukaiLeftAdjointKernel`). Then `Φ'` is left adjoint to `Φ`: there is a
> canonical bijection `Hom_Y(N, Φ(M)) ≃ Hom_X(Φ'(N), M)`, natural in `M ∈ D_QCoh(𝒪_X)` and
> `N ∈ D_QCoh(𝒪_Y)` (`CategoryTheory.Adjunction.homEquiv`).
>
> The hypothesis `hfib`, that the fibres of `g` are locally Noetherian, is part of the definition
> `AlgebraicGeometry.Scheme.Hom.IsGorenstein` of a Gorenstein morphism; it holds for every `g` of
> finite type. The quasi-separatedness of `f`, which the Fourier-Mukai transform `Φ` asks for, is a
> consequence of the hypotheses (`AlgebraicGeometry.fourierMukaiLeftAdjoint_instances`).

```lean
def fourierMukaiLeftAdjunction (hfib : ∀ s : S, IsLocallyNoetherian (g.fiber s))
    (hG : g.IsGorenstein hfib)
    (K : @DerivedCategory (pullback f g).Modules _ _ (HasDerivedCategory.standard _))
    (hK : ∀ j : ℤ, ((@DerivedCategory.homologyFunctor (pullback f g).Modules _ _
      (HasDerivedCategory.standard _) j).obj K).IsQuasicoherent)
    (hperf : @Stacks.Cohomology.PerfectComplexes.IsPerfect (pullback f g).toRingedSpace
      (HasDerivedCategory.standard _) K) :
    haveI : QuasiSeparated f := (fourierMukaiLeftAdjoint_instances f g).2.2.2.1
    quasiCoherentFourierMukai g f (fourierMukaiLeftAdjointKernel f g K hK hperf)
        (isQuasicoherent_homology_fourierMukaiLeftAdjointKernel f g K hK hperf) ⊣
      quasiCoherentFourierMukai f g K hK
```

## Tag 0FYY, a lemma

[Tag 0FYY](https://stacks.math.columbia.edu/tag/0FYY) in the Stacks Project.

**`AlgebraicGeometry.perfectFourierMukaiOfProperFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean#L104). The attribute's comment: “(1): the Fourier-Mukai functor D\_perf(O\_X) -> D\_perf(O\_Y) of a perfect kernel, for X flat, proper and of finite presentation over S, which the source's S Noetherian and X, Y proper flat over S imply”.

> **[Stacks, Tag 0FYY] (1).** For `f : X ⟶ S` flat, proper and of finite presentation and `K`
> a perfect object of `D(𝒪_{X ×_S Y})`, the Fourier-Mukai functor `Φ_K` restricts to a functor
> `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`.
>
> This holds when `S` is Noetherian and `X`, `Y` are proper and flat over `S`, the source's
> situation: a proper morphism to a Noetherian scheme is of finite presentation.

```lean
def perfectFourierMukaiOfProperFlat [Flat f] [IsProper f] [LocallyOfFinitePresentation f]
    (K : PerfectDerivedCategory (pullback f g)) :
    PerfectDerivedCategory X ⥤ PerfectDerivedCategory Y
```

**`AlgebraicGeometry.perfectFourierMukaiOfProperFlatComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean#L131). The attribute's comment: “(2): Phi\_\{K'} o Phi\_K = Phi\_\{K''} on D\_perf with K'' the convolution of Lemma 0FYS, as a natural isomorphism; for X, Y flat, proper and of finite presentation over S and Z quasi-compact quasi-separated over S, which the source's S Noetherian and X, Y, Z proper flat over S imply”.

> **[Stacks, Tag 0FYY] (2).** Let `f : X ⟶ S` and `g : Y ⟶ S` be flat, proper and of finite
> presentation and let `h : Z ⟶ S` be quasi-compact and quasi-separated. For perfect `K` on
> `X ×_S Y` and `K'` on `Y ×_S Z`, the composite `Φ_{K'} ∘ Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Z)` is
> `Φ_{K''}`, where `K'' = R pr_{13,*}(L pr_{12}^*K ⊗^𝐋 L pr_{23}^*K')` is the convolution of
> [Stacks, Tag 0FYS], perfect on `X ×_S Z` (`isPerfect_fourierMukaiConvolution_triple`).
>
> The source's equality of functors is rendered as a natural isomorphism; it is the one of
> [Stacks, Tag 0FYS], `quasiCoherentFourierMukaiCompNatIso`, on perfect objects. The hypotheses hold
> when `S` is Noetherian and `X`, `Y`, `Z` are proper and flat over `S`.

```lean
def perfectFourierMukaiOfProperFlatComp [Flat f] [IsProper f] [LocallyOfFinitePresentation f]
    [Flat g] [IsProper g] [LocallyOfFinitePresentation g] [QuasiCompact h] [QuasiSeparated h]
    (K : PerfectDerivedCategory (pullback f g)) (K' : PerfectDerivedCategory (pullback g h)) :
    perfectFourierMukaiOfProperFlat f g K ⋙ perfectFourierMukaiOfProperFlat g h K' ≅
      perfectFourierMukaiOfProperFlat f h
        ⟨fourierMukaiConvolution f g h K.obj K'.obj,
          isPerfect_fourierMukaiConvolution_triple f g h K.property K'.property⟩
```

**`AlgebraicGeometry.perfectFourierMukaiOfProperFlatRightAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean#L207). The attribute's comment: “(3): for X -> S Gorenstein, Phi\_\{K'} : D\_perf(O\_Y) -> D\_perf(O\_X) is right adjoint to Phi\_K, K' the pullback of Lpr\_1^* omega\_\{X/S} (x)^L K^dual by Y x\_S X -> X x\_S Y”.

> **[Stacks, Tag 0FYY] (3).** Let `S` be Noetherian, let `X` and `Y` be proper and flat over
> `S`, let `X ⟶ S` be Gorenstein, and let `K` be a perfect object of `D(𝒪_{X ×_S Y})`. Then
> `Φ_{K'} : D_perf(𝒪_Y) ⥤ D_perf(𝒪_X)` is right adjoint to `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`, where
> `K'`, an object of `D_perf(𝒪_{Y ×_S X})`, is the pullback of `Lpr_1^*ω^•_{X/S} ⊗^𝐋 K^∨` by
> `Y ×_S X ⟶ X ×_S Y` (`AlgebraicGeometry.fourierMukaiRightAdjointKernelDualizingFirst`, perfect by
> `AlgebraicGeometry.isPerfect_fourierMukaiRightAdjointKernelDualizingFirst`).
>
> Gorensteinness `AlgebraicGeometry.Scheme.Hom.IsGorenstein` is stated for a morphism with locally
> Noetherian fibres; the fibres of `f`, a morphism of finite type, are locally Noetherian, and `hG`
> is read at that proof. The `haveI` lines of the statement record that `X` and `Y` are
> quasi-compact and quasi-separated, which the kernel's construction asks for and the hypotheses
> imply.

```lean
def perfectFourierMukaiOfProperFlatRightAdjunction
    (hG : f.IsGorenstein fun s =>
      LocallyOfFiniteType.isLocallyNoetherian (f.fiberToSpecResidueField s))
    (K : PerfectDerivedCategory (pullback f g)) :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : CompactSpace Y := QuasiCompact.compactSpace_of_compactSpace g
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : QuasiSeparatedSpace Y := quasiSeparatedSpace_of_quasiSeparated g
    perfectFourierMukaiOfProperFlat f g K ⊣ perfectFourierMukaiOfProperFlat g f
      ⟨fourierMukaiRightAdjointKernelDualizingFirst f g K.obj
          (PerfectApproximation.isQuasicoherent_homology_of_isPerfect _ K.obj K.property)
          K.property,
        isPerfect_fourierMukaiRightAdjointKernelDualizingFirst f g _ hG K.obj
          (PerfectApproximation.isQuasicoherent_homology_of_isPerfect _ K.obj K.property)
          K.property⟩
```

**`AlgebraicGeometry.perfectFourierMukaiOfProperFlatLeftAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/FourierMukai/PerfectFunctor.lean#L246). The attribute's comment: “(4): for Y -> S Gorenstein, Phi\_\{K''} : D\_perf(O\_Y) -> D\_perf(O\_X) is left adjoint to Phi\_K, K'' the pullback of Lpr\_2^* omega\_\{Y/S} (x)^L K^dual by Y x\_S X -> X x\_S Y”.

> **[Stacks, Tag 0FYY] (4).** Let `S` be Noetherian, let `X` and `Y` be proper and flat over
> `S`, let `Y ⟶ S` be Gorenstein, and let `K` be a perfect object of `D(𝒪_{X ×_S Y})`. Then
> `Φ_{K''} : D_perf(𝒪_Y) ⥤ D_perf(𝒪_X)` is left adjoint to `Φ_K : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)`, where
> `K''`, an object of `D_perf(𝒪_{Y ×_S X})`, is the pullback of `Lpr_2^*ω^•_{Y/S} ⊗^𝐋 K^∨` by
> `Y ×_S X ⟶ X ×_S Y` (`AlgebraicGeometry.fourierMukaiLeftAdjointKernelDualizingFirst`, perfect by
> `AlgebraicGeometry.isPerfect_fourierMukaiLeftAdjointKernelDualizingFirst`).
>
> Gorensteinness `AlgebraicGeometry.Scheme.Hom.IsGorenstein` is stated for a morphism with locally
> Noetherian fibres; the fibres of `g`, a morphism of finite type, are locally Noetherian, and `hG`
> is read at that proof.

```lean
def perfectFourierMukaiOfProperFlatLeftAdjunction
    (hG : g.IsGorenstein fun s =>
      LocallyOfFiniteType.isLocallyNoetherian (g.fiberToSpecResidueField s))
    (K : PerfectDerivedCategory (pullback f g)) :
    perfectFourierMukaiOfProperFlat g f
        ⟨fourierMukaiLeftAdjointKernelDualizingFirst f g K.obj
            (PerfectApproximation.isQuasicoherent_homology_of_isPerfect _ K.obj K.property)
            K.property,
          isPerfect_fourierMukaiLeftAdjointKernelDualizingFirst f g _ hG K.obj
            (PerfectApproximation.isQuasicoherent_homology_of_isPerfect _ K.obj K.property)
            K.property⟩ ⊣
      perfectFourierMukaiOfProperFlat f g K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.8, Tag 0FYP](https://stacks.math.columbia.edu/tag/0FYP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
