---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.localCohomology_vanishing_tfae, Stacks.LocalCohomology.cohomologicalDimension, Stacks.LocalCohomology.exists_localCohomologyBound, Stacks.LocalCohomology.cohomologicalDimension_le_card_affine_cover, Stacks.LocalCohomology.cohomologicalDimension_le_card_zeroLocus_generators, Stacks.LocalCohomology.cohomologicalDimension_le_card_generators, Stacks.LocalCohomology.cohomologicalDimension_add_le, Stacks.LocalCohomology.cohomologicalDimension_map_le
statement: formalized
proof: formalized
---

# 51.4 Cohomological dimension

Section 51.4 of the Stacks Project, [Tag 0DX6](https://stacks.math.columbia.edu/tag/0DX6). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DX7, a lemma

[Tag 0DX7](https://stacks.math.columbia.edu/tag/0DX7) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomology_vanishing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/HighBoundTFAE.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/HighBoundTFAE.lean#L141).

> **[Stacks, Tag 0DX7].** Let `I` be a finitely generated ideal of a commutative ring `A`, let
> `Y = V(I) ⊆ X = Spec A` and let `d ≥ -1` be an integer. The following are equivalent:
> `H^i_Y(A) = 0` for `i > d`; `H^i_Y(M) = 0` for `i > d` for every `A`-module `M`; and the
> geometric condition that `Y = ∅` if `d = -1`, that `Y` be open and closed in `X` if `d = 0`, and
> that `H^n(X \ Y, ℱ) = 0` for `n ≥ d` for every quasi-coherent `𝒪_{X∖Y}`-module `ℱ` if `d > 0`.
>
> The three regimes of the third condition are proved separately:
> `Stacks.LocalCohomology.localCohomology_vanishing_tfae_of_nonpos` for `-1 ≤ d ≤ 0`, where the
> condition is one on `Y` itself, and
> `Stacks.LocalCohomology.localCohomology_vanishing_tfae_of_one_le` for `d ≥ 1`, where it is the
> acyclicity of the complement.

```lean
theorem localCohomology_vanishing_tfae
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (d : ℤ) (hd : (-1 : ℤ) ≤ d) :
    List.TFAE [
      ∀ (i : ℤ), d < i →
        IsZero (localCohomologyModule A I hI (ModuleCat.of A A) i),
      ∀ (M : ModuleCat.{max u v} A) (i : ℤ), d < i →
        IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj
          ((Dualizing.derivedPowerTorsionProperty A I hI).ι.obj
            ((Dualizing.localCohomologyFunctor A I hI).obj
              ((DerivedCategory.singleFunctor (ModuleCat.{max u v} A) 0).obj M)))),
      ((d = -1 → PrimeSpectrum.zeroLocus (I : Set A) = ∅) ∧
        (d = 0 → IsClopen (PrimeSpectrum.zeroLocus (I : Set A))) ∧
        (0 < d →
          let U : (Spec (CommRingCat.of A)).Opens :=
            ⟨(PrimeSpectrum.zeroLocus (I : Set A))ᶜ,
              (PrimeSpectrum.isClosed_zeroLocus (I : Set A)).isOpen_compl⟩
          ∀ (F : (U : Scheme).Modules),
            F.IsQuasicoherent → ∀ (n : ℕ), d ≤ (n : ℤ) →
              IsZero (Hgroup (U : Scheme).ringCatSheaf ⊤ n F)))]
```

## Tag 0DX8, a definition

[Tag 0DX8](https://stacks.math.columbia.edu/tag/0DX8) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/CohomologicalDimension.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/CohomologicalDimension.lean#L58). The attribute's comment: “the least integer”.

> **Stacks Project, Tag 0DX8.** The cohomological dimension of a finitely generated ideal is
> the least integer `d ≥ -1` above which its local cohomology vanishes.

```lean
def cohomologicalDimension
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) : ℤ
```

**`Stacks.LocalCohomology.exists_localCohomologyBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/CohomologicalDimension.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/CohomologicalDimension.lean#L65). The attribute's comment: “existence of a vanishing bound”.

> Finite generation gives a finite upper bound on the degrees in which local cohomology is
> nonzero; equivalently, the set defining the cohomological dimension is nonempty.

```lean
theorem exists_localCohomologyBound
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    ∃ d : ℤ, IsLocalCohomologyBound A I hI d
```

## Tag 0DX9, a lemma

[Tag 0DX9](https://stacks.math.columbia.edu/tag/0DX9) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_le_card_affine_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineCover.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineCover.lean#L100). The attribute's comment: “part (3): the bound by an affine cover of the complement”.

> **Stacks Project, Tag 0DX9 (3).** The cohomological dimension of a finitely generated ideal
> `I` of `A` is at most the number of members of an affine open cover of `Spec A ∖ V(I)`.

```lean
theorem cohomologicalDimension_le_card_affine_cover
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    {c : ℕ} (V : Fin c → (Spec (CommRingCat.of A)).Opens)
    (hV : ∀ i, IsAffineOpen (V i))
    (hcov : ⨆ i, V i = complZeroLocusOpen A I) :
    cohomologicalDimension A I hI ≤ (c : ℤ)
```

**`Stacks.LocalCohomology.cohomologicalDimension_le_card_zeroLocus_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimensionBounds.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimensionBounds.lean#L92). The attribute's comment: “part (2): the bound by a family cutting out the same zero locus”.

> The cohomological dimension is at most the number of equations in any finite family
> defining the same zero locus.

```lean
theorem cohomologicalDimension_le_card_zeroLocus_generators
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    {n : ℕ} (f : Fin n → A)
    (hf : PrimeSpectrum.zeroLocus ((Ideal.span (Set.range f) : Ideal A) : Set A) =
      PrimeSpectrum.zeroLocus (I : Set A)) :
    cohomologicalDimension A I hI ≤ (n : ℤ)
```

**`Stacks.LocalCohomology.cohomologicalDimension_le_card_generators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimensionBounds.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimensionBounds.lean#L111). The attribute's comment: “part (1): the bound by the number of generators”.

> The cohomological dimension is at most the number of generators in any finite generating
> family of the ideal.

```lean
theorem cohomologicalDimension_le_card_generators
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    {n : ℕ} (f : Fin n → A) (hf : I = Ideal.span (Set.range f)) :
    cohomologicalDimension A I hI ≤ (n : ℤ)
```

## Tag 0ECP, a lemma

[Tag 0ECP](https://stacks.math.columbia.edu/tag/0ECP) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_add_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Sum.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Sum.lean#L67).

> **[Stacks, Tag 0ECP].** For finitely generated ideals `I` and `J` of a commutative ring `A`,
> the cohomological dimension of `I + J` is at most the sum of those of `I` and `J`, bounded below
> by `-1` because a cohomological dimension always is.

```lean
theorem cohomologicalDimension_add_le (A : Type u) [CommRing A] (I J : Ideal A)
    (hI : I.FG) (hJ : J.FG) :
    cohomologicalDimension A (I + J) (Submodule.FG.sup hI hJ) ≤
      max (-1 : ℤ) (cohomologicalDimension A I hI + cohomologicalDimension A J hJ)
```

## Tag 0DXA, a lemma

[Tag 0DXA](https://stacks.math.columbia.edu/tag/0DXA) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_map_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/ChangeOfRings.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/ChangeOfRings.lean#L195). The attribute's comment: “inequality under a ring map”.

> **Stacks Project, Tag 0DXA.** Cohomological dimension does not increase under extension of
> the ideal along a ring homomorphism.

```lean
theorem cohomologicalDimension_map_le
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    (f : A →+* B) (I : Ideal A) (hI : I.FG) :
    cohomologicalDimension B (I.map f) (hI.map f) ≤ cohomologicalDimension A I hI
```

**`Stacks.LocalCohomology.cohomologicalDimension_map_eq_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/ChangeOfRings.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/ChangeOfRings.lean#L229). The attribute's comment: “equality under faithfully flat extension”.

> **Stacks Project, Tag 0DXA.** Faithfully flat extension preserves cohomological
> dimension.

```lean
theorem cohomologicalDimension_map_eq_of_faithfullyFlat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B]
    (f : A →+* B) (hf : f.FaithfullyFlat) (I : Ideal A) (hI : I.FG) :
    cohomologicalDimension B (I.map f) (hI.map f) = cohomologicalDimension A I hI
```

## Tag 0DXB, a lemma

[Tag 0DXB](https://stacks.math.columbia.edu/tag/0DXB) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_eq_sSup_localizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Localization.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/Localization.lean#L144).

> **Stacks Project, Tag 0DXB.** The cohomological dimension of a finitely generated ideal is
> the supremum of the cohomological dimensions of its extensions to the local rings of the
> spectrum.

```lean
theorem cohomologicalDimension_eq_sSup_localizations
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) :
    cohomologicalDimension A I hI =
      sSup (insert (-1 : ℤ) (Set.range fun p : PrimeSpectrum A =>
        cohomologicalDimension (Localization.AtPrime p.asIdeal)
          (I.map (algebraMap A (Localization.AtPrime p.asIdeal)))
          (hI.map (algebraMap A (Localization.AtPrime p.asIdeal)))))
```

## Tag 0DXC, a lemma

[Tag 0DXC](https://stacks.math.columbia.edu/tag/0DXC) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_le_of_ringKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/KrullDimension.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/KrullDimension.lean#L129). The attribute's comment: “the bound of the cohomological dimension by the Krull dimension”.

> **Stacks Project, Tag 0DXC.** The cohomological dimension of a finitely generated ideal of a
> commutative ring is at most the Krull dimension of the ring.
>
> By Stacks 0DXB the cohomological dimension is the supremum of the cohomological dimensions of
> the localizations `A_𝔭`, each local of dimension `ht 𝔭 ≤ dim A`.

```lean
theorem cohomologicalDimension_le_of_ringKrullDim_le
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG) (d : ℕ)
    (hd : ringKrullDim A ≤ (d : WithBot ℕ∞)) :
    cohomologicalDimension A I hI ≤ (d : ℤ)
```

**`Stacks.LocalCohomology.isZero_localCohomologyModule_of_supportDim_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/KrullDimension.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/KrullDimension.lean#L147). The attribute's comment: “the vanishing above the dimension of the support”. References: SGA 2 V (3.1), “(i)”.

> **Stacks Project, Tag 0DXC.** For a finite module `M` over a commutative ring `A` and a
> finitely generated ideal `I ⊆ A`, the local cohomology `H^i_{V(I)}(M)` vanishes in every degree
> `i` above the dimension of the support of `M`.
>
> With `𝔞 = ann(M)` and `B = A/𝔞` one has `Spec B = Supp M`, so `dim B = dim Supp M < i`; the
> bound `cd(B, IB) ≤ i - 1` then gives the vanishing through Stacks 0BJB and the implication
> (1) ⇒ (2) of Stacks 0DX7. A subsingleton module is treated separately, the dimension of an empty
> support being `⊥`.

```lean
theorem isZero_localCohomologyModule_of_supportDim_lt
    (A : Type u) [CommRing A] (I : Ideal A) (hI : I.FG)
    (M : ModuleCat.{max u v} A) [Module.Finite A M] (i : ℤ)
    (hi : Module.supportDim A M < (i.toNat : WithBot ℕ∞)) :
    IsZero (localCohomologyModule A I hI M i)
```

## Tag 0DXD, a lemma

[Tag 0DXD](https://stacks.math.columbia.edu/tag/0DXD) in the Stacks Project.

**`Stacks.LocalCohomology.nonempty_compl_zeroLocus_of_cohomologicalDimension_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean#L117). The attribute's comment: “nonemptiness”.

> **Stacks Project, Tag 0DXD.** If a finitely generated ideal has cohomological dimension one,
> the complement of its zero locus in the prime spectrum is nonempty.

```lean
theorem nonempty_compl_zeroLocus_of_cohomologicalDimension_eq_one
    (hcd : cohomologicalDimension A I hI = 1) :
    (PrimeSpectrum.zeroLocus (I : Set A))ᶜ.Nonempty
```

**`Stacks.LocalCohomology.isAffine_complZeroLocusOpen_of_cohomologicalDimension_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean#L157). The attribute's comment: “affineness”.

> **Stacks Project, Tag 0DXD.** If a finitely generated ideal has cohomological dimension one,
> the complement of its zero locus, as an open subscheme of `Spec A`, is affine.
>
> Serre's criterion for affineness (Stacks 01XF) applies to the complement
> `U = complZeroLocusOpen A I`: it is quasi-compact by `compactSpace_complZeroLocusOpen`, and the
> `d = 1` instance of Stacks 0DX7
> (`isZero_hgroup_complement_of_isZero_localCohomologyModule_self`) turns the vanishing of
> `H^i_{V(I)}(A)` for `i > 1`, which is what cohomological dimension one means, into the vanishing
> of `H¹(U, F)` for every quasi-coherent `F` on `U`, in particular for every quasi-coherent ideal
> sheaf.

```lean
theorem isAffine_complZeroLocusOpen_of_cohomologicalDimension_eq_one
    (hcd : cohomologicalDimension A I hI = 1) :
    IsAffine (complZeroLocusOpen A I).toScheme
```

**`Stacks.LocalCohomology.nonempty_and_isAffine_complZeroLocusOpen_of_cohomologicalDimension_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/AffineComplement.lean#L181).

> **Stacks Project, Tag 0DXD.** Let `I` be a finitely generated ideal of a commutative ring
> `A`. If the cohomological dimension `cd(A, I)` equals `1`, then `Spec A ∖ V(I)` is a nonempty
> affine scheme.
>
> This is the source statement, both of its assertions made about the single open subscheme
> `complZeroLocusOpen A I = Spec A ∖ V(I)`: nonemptiness from
> `nonempty_compl_zeroLocus_of_cohomologicalDimension_eq_one` and affineness from
> `isAffine_complZeroLocusOpen_of_cohomologicalDimension_eq_one`.

```lean
theorem nonempty_and_isAffine_complZeroLocusOpen_of_cohomologicalDimension_eq_one
    (hcd : cohomologicalDimension A I hI = 1) :
    Nonempty (complZeroLocusOpen A I).toScheme ∧
      IsAffine (complZeroLocusOpen A I).toScheme
```

## Tag 0DXE, a lemma

[Tag 0DXE](https://stacks.math.columbia.edu/tag/0DXE) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_maximalIdeal_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean#L222). The attribute's comment: “cohomological dimension of the maximal ideal; existence of a normalized dualizing complex on the completion, the local case of Stacks 0BFR, is an explicit hypothesis”.

> Let `(A, 𝔪)` be a Noetherian local ring of dimension `d` whose completion carries a normalized
> dualizing complex. Then `cd(A, 𝔪) = d`.

```lean
theorem cohomologicalDimension_maximalIdeal_eq
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hm : (IsLocalRing.maximalIdeal A).FG)
    (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞))
    (hBFR : ∃ ω : DerivedCategory
        (ModuleCat.{u} (AdicCompletion (IsLocalRing.maximalIdeal A) A)),
      Dualizing.IsNormalizedDualizingComplex.{u, u} ω) :
    cohomologicalDimension A (IsLocalRing.maximalIdeal A) hm = (d : ℤ)
```

**`Stacks.LocalCohomology.not_isZero_topLocalCohomologyModule_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean#L258). The attribute's comment: “nonvanishing of top local cohomology; existence of a normalized dualizing complex on the completion, the local case of Stacks 0BFR, is an explicit hypothesis”. References: SGA 2 V (3.1), “(iii), special case”.

> Let `(A, 𝔪)` be a Noetherian local ring of dimension `d` whose completion carries a normalized
> dualizing complex. Then `H^d_𝔪(A)` is nonzero.

```lean
theorem not_isZero_topLocalCohomologyModule_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hm : (IsLocalRing.maximalIdeal A).FG)
    (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞))
    (hBFR : ∃ ω : DerivedCategory
        (ModuleCat.{u} (AdicCompletion (IsLocalRing.maximalIdeal A) A)),
      Dualizing.IsNormalizedDualizingComplex.{u, u} ω) :
    ¬ IsZero (localCohomologyModule A (IsLocalRing.maximalIdeal A) hm
      (ModuleCat.of A A) (d : ℤ))
```

**`Stacks.LocalCohomology.cohomologicalDimension_maximalIdeal_eq'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean#L294).

> Let `(A, 𝔪)` be a Noetherian local ring of dimension `d`. Then `cd(A, 𝔪) = d`.

```lean
theorem cohomologicalDimension_maximalIdeal_eq'
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hm : (IsLocalRing.maximalIdeal A).FG)
    (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞)) :
    cohomologicalDimension A (IsLocalRing.maximalIdeal A) hm = (d : ℤ)
```

**`Stacks.LocalCohomology.not_isZero_topLocalCohomologyModule_maximalIdeal'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/TopLocalCohomology.lean#L304). References: SGA 2 V (3.1), “(iii), special case”.

> Let `(A, 𝔪)` be a Noetherian local ring of dimension `d`. Then `H^d_𝔪(A)` is nonzero.

```lean
theorem not_isZero_topLocalCohomologyModule_maximalIdeal'
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hm : (IsLocalRing.maximalIdeal A).FG)
    (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞)) :
    ¬ IsZero (localCohomologyModule A (IsLocalRing.maximalIdeal A) hm
      (ModuleCat.of A A) (d : ℤ))
```

## Tag 0DXF, a lemma

[Tag 0DXF](https://stacks.math.columbia.edu/tag/0DXF) in the Stacks Project.

**`Stacks.LocalCohomology.ringKrullDim_quotient_le_cohomologicalDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IsolatedPrime.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IsolatedPrime.lean#L133). The attribute's comment: “existence of a normalized dualizing complex on the completion of A/𝔭, the local case of Stacks 0BFR, is an explicit hypothesis”.

> **Stacks Project, Tag 0DXF.** Let `(A, 𝔪)` be a Noetherian local ring, `I ⊆ A` a finitely
> generated ideal and `𝔭 ⊆ A` a prime ideal with `V(𝔭) ∩ V(I) = {𝔪}`. Then
> `dim(A/𝔭) ≤ cd(A, I)`.
>
> The extension of `I` to `A/𝔭` has the same zero locus as `𝔪/𝔭`, so its cohomological dimension
> is `dim(A/𝔭)` by Stacks 0DXE, and extending an ideal along a ring map cannot raise the
> cohomological dimension by Stacks 0DXA.

```lean
theorem ringKrullDim_quotient_le_cohomologicalDimension
    (I : Ideal A) (hI : I.FG)
    (hinter : PrimeSpectrum.zeroLocus (p : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
      {IsLocalRing.closedPoint A})
    (d : ℕ) (hdim : ringKrullDim (A ⧸ p) = (d : WithBot ℕ∞))
    (hBFR : ∃ ω : DerivedCategory (ModuleCat.{u} (AdicCompletion
        (IsLocalRing.maximalIdeal (A ⧸ p)) (A ⧸ p))),
      Dualizing.IsNormalizedDualizingComplex.{u, u} ω) :
    (d : ℤ) ≤ cohomologicalDimension A I hI
```

**`Stacks.LocalCohomology.ringKrullDim_quotient_le_cohomologicalDimension'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IsolatedPrime.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/CohomologicalDimension/IsolatedPrime.lean#L197).

> **Stacks Project, Tag 0DXF.** Let `(A, 𝔪)` be a Noetherian local ring, `I ⊆ A` a finitely
> generated ideal and `𝔭 ⊆ A` a prime ideal with `V(𝔭) ∩ V(I) = {𝔪}`. Then
> `dim(A/𝔭) ≤ cd(A, I)`.
>
> This is `Stacks.LocalCohomology.ringKrullDim_quotient_le_cohomologicalDimension` with its
> hypothesis on the completion of `A/𝔭` discharged by
> `Stacks.LocalCohomology.exists_isNormalizedDualizingComplex_adicCompletion`.

```lean
theorem ringKrullDim_quotient_le_cohomologicalDimension'
    (I : Ideal A) (hI : I.FG)
    (hinter : PrimeSpectrum.zeroLocus (p : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
      {IsLocalRing.closedPoint A})
    (d : ℕ) (hdim : ringKrullDim (A ⧸ p) = (d : WithBot ℕ∞)) :
    (d : ℤ) ≤ cohomologicalDimension A I hI
```

## Tag 0EHU, a lemma

[Tag 0EHU](https://stacks.math.columbia.edu/tag/0EHU) in the Stacks Project.

**`Stacks.LocalCohomology.cohomologicalDimension_le_of_blowUp_fibre_dim_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/BlowupFibreDimension.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/VanishingTFAE/BlowupFibreDimension.lean#L178). The attribute's comment: “cd(A, I) ≤ d from fibres of the blowup of dimension ≤ d - 1”.

> Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `b : X' ⟶ X = Spec A` the blowup of `I`.
> If every fibre of `b` has dimension `< d`, that is at most `d - 1`, then the cohomological
> dimension `cd(A, I)` is at most `d`.
>
> Set `U = Spec A \ V(I)`. The canonical open immersion `j : U ⟶ X'` is affine, because the
> exceptional divisor is an effective Cartier divisor, so `Rᵖ j_* 𝓕 = 0` for `p > 0` and every
> quasi-coherent `𝓕` on `U`; and `Rᵠ b_* (j_* 𝓕) = 0` for `q ≥ d` by [Stacks, Tag 0E7D] part (1),
> which over the locally Noetherian base `Spec A` is
> `FibreDimension.isZero_stalk_rightDerivedPlus_of_fiber_dimension_le_of_isQuasicoherent`.
> The Leray spectral sequence then gives `Rⁿ (b ∘ j)_* 𝓕 = 0` for `n ≥ d`, hence
> `Hⁿ(U, 𝓕) = 0` for `n ≥ d`, which is `cd(A, I) ≤ d` by definition.

```lean
theorem cohomologicalDimension_le_of_blowUp_fibre_dim_lt
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) (d : ℕ)
    (hdim : ∀ y : Spec (CommRingCat.of A),
      topologicalKrullDim ((blowUpToBase (specIdealSheaf A I)).fiber y) < (d : WithBot ℕ∞)) :
    cohomologicalDimension A I I.fg_of_isNoetherianRing ≤ (d : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.4, Tag 0DX6](https://stacks.math.columbia.edu/tag/0DX6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
