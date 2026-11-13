---
declaration: section
origin: cited
lean: PrimeSpectrum, PrimeSpectrum.zeroLocus, PrimeSpectrum.basicOpen, PrimeSpectrum.basicOpen_eq_top_iff_isUnit, PrimeSpectrum.basicOpen_eq_of_unit_mul, PrimeSpectrum.exists_basicOpen_disjoint_zeroLocus, PrimeSpectrum.iUnion_basicOpen_eq_compl_zeroLocus, Ideal.exists_maximal
statement: formalized
proof: formalized
---

# 10.17 The spectrum of a ring

Section 10.17 of the Stacks Project, [Tag 00DY](https://stacks.math.columbia.edu/tag/00DY). 9 tags here are carried by 9 declarations of the repository (4 in StacksCore and 5 in StacksFrontier) and 25 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00DZ, a definition

[Tag 00DZ](https://stacks.math.columbia.edu/tag/00DZ) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L8) (StacksCore). References: EGA I (1.1.1); EGA IV (10.4.4); EGA IV (10.5.1).
- [`PrimeSpectrum.zeroLocus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L9) (StacksCore). References: EGA 0 (16.3.1); EGA I (1.1.1); EGA I (1.1.5).
- [`PrimeSpectrum.basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.basicOpen#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L9) (StacksCore). References: EGA I (1.1.1); EGA IV (20.2.9), “special case”.

## Tag 00E0, a lemma

[Tag 00E0](https://stacks.math.columbia.edu/tag/00E0) in the Stacks Project.

**`PrimeSpectrum.basicOpen_eq_top_iff_isUnit`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L33). The attribute's comment: “17”.

```lean
theorem basicOpen_eq_top_iff_isUnit {f : R} :
    basicOpen f = ⊤ ↔ IsUnit f
```

**`PrimeSpectrum.basicOpen_eq_of_unit_mul`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L39). The attribute's comment: “13”. References: EGA I (1.1.9), “last clause”.

```lean
theorem basicOpen_eq_of_unit_mul {f f' u : R} (hu : IsUnit u) (h : f = u * f') :
    basicOpen f = basicOpen f'
```

**`PrimeSpectrum.exists_basicOpen_disjoint_zeroLocus`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L44). The attribute's comment: “14”.

```lean
theorem exists_basicOpen_disjoint_zeroLocus {I : Ideal R} {p : PrimeSpectrum R}
    (hp : p ∉ zeroLocus (I : Set R)) : ∃ f : R, p ∈ basicOpen f ∧
      (basicOpen f : Set (PrimeSpectrum R)) ∩ zeroLocus (I : Set R) = ∅
```

**`PrimeSpectrum.iUnion_basicOpen_eq_compl_zeroLocus`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L56). The attribute's comment: “16”. References: EGA I (1.1.1), “more general”.

```lean
theorem iUnion_basicOpen_eq_compl_zeroLocus {ι : Type*} (f : ι → R) :
    (⋃ i, (basicOpen (f i) : Set (PrimeSpectrum R))) = (zeroLocus (Set.range f))ᶜ
```

Declarations registered for the tag:

- [`Ideal.exists_maximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.exists_maximal#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Maximal.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Maximal.lean#L16) (StacksCore): “2”.
- [`Ideal.nonempty_minimalPrimes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.nonempty_minimalPrimes#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/MinimalPrime/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/MinimalPrime/Basic.lean#L8) (StacksCore): “3”. References: EGA 0 (1.0.6), “more general”.
- [`Ideal.exists_minimalPrimes_le`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.exists_minimalPrimes_le#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/MinimalPrime/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/MinimalPrime/Basic.lean#L9) (StacksCore): “4”.
- [`Ideal.radical_eq_sInf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.radical_eq_sInf#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Ideal/Operations.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Ideal/Operations.lean#L11) (StacksCore): “7”. References: EGA 0 (1.1.1), “partial”; EGA I (1.1.1), “more general”; EGA I (1.1.5), “partial”.
- [`PrimeSpectrum.isEmpty_iff_subsingleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isEmpty_iff_subsingleton#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L10) (StacksCore): “1”. References: EGA I (1.1.1), “more general”.
- [`PrimeSpectrum.zeroLocus_span`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_span#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L11) (StacksCore): “5”.
- [`PrimeSpectrum.zeroLocus_radical`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_radical#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L12) (StacksCore): “6”. References: EGA I (1.1.2), “(v) for ideals”.
- [`PrimeSpectrum.zeroLocus_empty_iff_eq_top`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_empty_iff_eq_top#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L13) (StacksCore): “8”.
- [`PrimeSpectrum.zeroLocus_inf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_inf#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L14) (StacksCore): “9”. References: EGA 0 (1.7.4), “two ideals, special case”; EGA I (1.1.5), “more general”.
- [`PrimeSpectrum.zeroLocus_iUnion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zeroLocus_iUnion#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Basic.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Basic.lean#L15) (StacksCore): “10”. References: EGA I (1.1.2), “(iii): V(⋃E\_λ)=⋂V(E\_λ)”.
- [`PrimeSpectrum.basicOpen_eq_zeroLocus_compl`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.basicOpen_eq_zeroLocus_compl#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L10) (StacksCore): “11”. References: EGA I (1.1.1), “more general”.
- [`PrimeSpectrum.basicOpen_eq_bot_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.basicOpen_eq_bot_iff#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L11) (StacksCore): “12”.
- [`PrimeSpectrum.basicOpen_mul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.basicOpen_mul#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L12) (StacksCore): “15”. References: EGA I (1.1.9), “more general”; EGA III (6.7.1), “special case”.

## Tag 00E1, a definition

[Tag 00E1](https://stacks.math.columbia.edu/tag/00E1) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.zariskiTopology`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.zariskiTopology#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L13) (StacksCore).

## Tag 00E2, a lemma

[Tag 00E2](https://stacks.math.columbia.edu/tag/00E2) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.comap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.comap#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L14) (StacksCore). References: EGA 0 (14.1.12); EGA I (1.2.1); EGA I (1.7.2), “partial”; EGA I (10.2.1), “special case”.
- [`PrimeSpectrum.comap_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.comap_basicOpen#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L15) (StacksCore). References: EGA I (1.2.2), “more general”; EGA I (1.6.1), “more general”; EGA I (10.2.1), “special case”.

## Tag 00E3, a lemma

[Tag 00E3](https://stacks.math.columbia.edu/tag/00E3) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.primeSpectrumOrderIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.primeSpectrumOrderIso#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/Ideal.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/Ideal.lean#L14) (StacksCore). References: EGA 0 (1.2.6); EGA I (1.2.6), “partial”; EGA IV (10.7.3), “partial”.
- [`PrimeSpectrum.localization_comap_isInducing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.localization_comap_isInducing#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L16) (StacksCore). References: EGA I (1.6.2), “partial”.

## Tag 00E4, a lemma

[Tag 00E4](https://stacks.math.columbia.edu/tag/00E4) in the Stacks Project.

**`PrimeSpectrum.localizationAwayHomeomorphBasicOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/LocalizationAwayHomeomorph.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/LocalizationAwayHomeomorph.lean#L34). The attribute's comment: “the homeomorphism `Spec(R_f) → D(f)`”.

> **Stacks 00E4**: for `S` a localization of `R` away from `f` (such as `R_f`), the map
> `Spec S → Spec R` induced by `R → S` is a homeomorphism onto the standard open `D(f)`.
>
> The forward map is `comap (algebraMap R S)` (`localizationAwayHomeomorphBasicOpen_apply_coe`)
> and the inverse sends `𝔭` to `𝔭 · S` (`localizationAwayHomeomorphBasicOpen_symm_apply_asIdeal`).
> It is assembled from Mathlib's `localization_away_isOpenEmbedding` (a homeomorphism onto the
> range) and `localization_away_comap_range` (the range is `D(f)`).

```lean
noncomputable def localizationAwayHomeomorphBasicOpen (S : Type*) [CommSemiring S] [Algebra R S]
    (f : R) [IsLocalization.Away f S] : PrimeSpectrum S ≃ₜ basicOpen f
```

**`PrimeSpectrum.localizationAwayHomeomorphBasicOpen_symm_apply_asIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/LocalizationAwayHomeomorph.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/LocalizationAwayHomeomorph.lean#L50). The attribute's comment: “the inverse is `𝔭 ↦ 𝔭 · R_f`”.

> **Stacks 00E4**, the inverse: the inverse of `Spec S → D(f)` sends `𝔭 ∈ D(f)` to the prime
> `𝔭 · S`, the ideal of `S` generated by the image of `𝔭`.

```lean
theorem localizationAwayHomeomorphBasicOpen_symm_apply_asIdeal (S : Type*) [CommSemiring S]
    [Algebra R S] (f : R) [IsLocalization.Away f S] (p : basicOpen f) :
    ((localizationAwayHomeomorphBasicOpen S f).symm p).asIdeal =
      Ideal.map (algebraMap R S) (p : PrimeSpectrum R).asIdeal
```

Declarations registered for the tag:

- [`PrimeSpectrum.localization_away_isOpenEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.localization_away_isOpenEmbedding#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L17) (StacksCore). References: EGA I (1.3.6), “partial”; EGA I (1.6.2), “special case”.

## Tag 00E5, a lemma

[Tag 00E5](https://stacks.math.columbia.edu/tag/00E5) in the Stacks Project.

**`Ideal.primeSpectrumQuotientHomeomorphZeroLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean#L29).

> **Stacks 00E5**: the quotient map `R → R ⧸ I` induces, via `PrimeSpectrum.comap`, a
> homeomorphism `Spec (R ⧸ I) ≃ₜ V(I)`. The forward map is `comap (Ideal.Quotient.mk I)`
> (`Ideal.coe_primeSpectrumQuotientHomeomorphZeroLocus_apply`), and the inverse sends `𝔭` to
> `𝔭 / I = 𝔭.map (Ideal.Quotient.mk I)`
> (`Ideal.primeSpectrumQuotientHomeomorphZeroLocus_symm_apply`).
>
> The underlying bijection is Mathlib's `Ideal.primeSpectrumQuotientOrderIsoZeroLocus`; it is a
> homeomorphism because `comap (Ideal.Quotient.mk I)` is an embedding
> (`PrimeSpectrum.isEmbedding_comap_of_surjective`).

```lean
noncomputable def primeSpectrumQuotientHomeomorphZeroLocus :
    PrimeSpectrum (R ⧸ I) ≃ₜ PrimeSpectrum.zeroLocus (R := R) I
```

**`Ideal.coe_primeSpectrumQuotientHomeomorphZeroLocus_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean#L38). The attribute's comment: “the map is `comap` of the quotient map”.

> **Stacks 00E5**, the forward map: the homeomorphism `Spec (R ⧸ I) ≃ₜ V(I)` is induced by the
> quotient map `R → R ⧸ I` via the functoriality of `Spec`.

```lean
theorem coe_primeSpectrumQuotientHomeomorphZeroLocus_apply (p : PrimeSpectrum (R ⧸ I)) :
    (I.primeSpectrumQuotientHomeomorphZeroLocus p : PrimeSpectrum R) =
      PrimeSpectrum.comap (Quotient.mk I) p
```

**`Ideal.primeSpectrumQuotientHomeomorphZeroLocus_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/QuotientHomeomorph.lean#L46). The attribute's comment: “the inverse is `𝔭 ↦ 𝔭 / I`”.

> **Stacks 00E5**, the inverse: the inverse of `Spec (R ⧸ I) ≃ₜ V(I)` sends `𝔭 ⊇ I` to
> `𝔭 / I`, the image of `𝔭` in `R ⧸ I`.

```lean
theorem primeSpectrumQuotientHomeomorphZeroLocus_symm_apply
    (p : PrimeSpectrum.zeroLocus (R := R) I) :
    (I.primeSpectrumQuotientHomeomorphZeroLocus.symm p).asIdeal =
      p.1.asIdeal.map (Quotient.mk I)
```

Declarations registered for the tag:

- [`PrimeSpectrum.isClosedEmbedding_comap_of_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isClosedEmbedding_comap_of_surjective#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L18) (StacksCore). References: EGA I (1.2.4), “more general”.

## Tag 00E8, a lemma

[Tag 00E8](https://stacks.math.columbia.edu/tag/00E8) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.compactSpace#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L19) (StacksCore). References: EGA I (1.1.10), “more general”.

## Tag 04PM, a lemma

[Tag 04PM](https://stacks.math.columbia.edu/tag/04PM) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.instSpectralSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.instSpectralSpace#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Spectrum/Prime/Topology.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Spectrum/Prime/Topology.lean#L22) (StacksCore). References: EGA I (1.1.8), “more general”; EGA I (1.1.10), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.17, Tag 00DY](https://stacks.math.columbia.edu/tag/00DY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
