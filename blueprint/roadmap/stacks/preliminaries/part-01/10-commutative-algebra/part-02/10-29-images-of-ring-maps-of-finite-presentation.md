---
declaration: section
origin: cited
lean: QuasiSeparatedSpace.isRetrocompact_iff_isCompact, PrimeSpectrum.isCompact_isOpen_iff, PrimeSpectrum.isCompact_isOpen_iff_ideal, PrimeSpectrum.isCompact_preimage_comap_of_isOpen, PrimeSpectrum.isConstructible_preimage_comap, PrimeSpectrum.exists_constructibleSetData_iff, PrimeSpectrum.BasicConstructibleSetData, PrimeSpectrum.BasicConstructibleSetData.toSet
statement: formalized
proof: formalized
---

# 10.29 Images of ring maps of finite presentation

Section 10.29 of the Stacks Project, [Tag 00F5](https://stacks.math.columbia.edu/tag/00F5). 10 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00F6, a lemma

[Tag 00F6](https://stacks.math.columbia.edu/tag/00F6) in the Stacks Project.

Declarations registered for the tag:

- [`QuasiSeparatedSpace.isRetrocompact_iff_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiSeparatedSpace.isRetrocompact_iff_isCompact#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L27) (StacksFrontier): “(1) ↔ (2)”. References: EGA 0 (9.1.6); SGA 3 VIA (2.6.3), “special case”.
- [`PrimeSpectrum.isCompact_isOpen_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isCompact_isOpen_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L28) (StacksFrontier): “(2) ↔ (3)”.
- [`PrimeSpectrum.isCompact_isOpen_iff_ideal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isCompact_isOpen_iff_ideal#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L29) (StacksFrontier): “(2) ↔ (4)”.

## Tag 00F7, a lemma

[Tag 00F7](https://stacks.math.columbia.edu/tag/00F7) in the Stacks Project.

**`PrimeSpectrum.isCompact_preimage_comap_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L76). The attribute's comment: “(1)”.

> Stacks 00F7 (first assertion): for a ring map `φ : R → S`, the induced
> continuous map `Spec(S) → Spec(R)` is quasi-compact, i.e. the preimage of
> every quasi-compact open of `Spec(R)` is quasi-compact in `Spec(S)`.

```lean
theorem PrimeSpectrum.isCompact_preimage_comap_of_isOpen
    {R S : Type*} [CommSemiring R] [CommSemiring S] (φ : R →+* S)
    (V : Set (PrimeSpectrum R)) (hV : IsOpen V) (hVc : IsCompact V) :
    IsCompact ((PrimeSpectrum.comap φ) ⁻¹' V)
```

**`PrimeSpectrum.isConstructible_preimage_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L91). The attribute's comment: “(2)”.

> Stacks 00F7 (second assertion): for a ring map `φ : R → S` and any
> constructible subset `E ⊆ Spec(R)`, the preimage `(comap φ)⁻¹(E)` is
> constructible in `Spec(S)`.

```lean
theorem PrimeSpectrum.isConstructible_preimage_comap
    {R S : Type*} [CommSemiring R] [CommSemiring S] (φ : R →+* S)
    (E : Set (PrimeSpectrum R)) (hE : Topology.IsConstructible E) :
    Topology.IsConstructible ((PrimeSpectrum.comap φ) ⁻¹' E)
```

## Tag 0G1P, a lemma

[Tag 0G1P](https://stacks.math.columbia.edu/tag/0G1P) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.exists_constructibleSetData_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.exists_constructibleSetData_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L31) (StacksFrontier).
- [`PrimeSpectrum.BasicConstructibleSetData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.BasicConstructibleSetData#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L32) (StacksFrontier): “the data of a `D(f) ∩ V(g₁, …, gₘ)`”.
- [`PrimeSpectrum.BasicConstructibleSetData.toSet`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.BasicConstructibleSetData.toSet#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L34) (StacksFrontier): “the set it describes”.
- [`PrimeSpectrum.ConstructibleSetData.toSet`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.ConstructibleSetData.toSet#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Defs.lean#L35) (StacksFrontier): “the finite union”.

## Tag 00F8, a lemma

[Tag 00F8](https://stacks.math.columbia.edu/tag/00F8) in the Stacks Project.

**`PrimeSpectrum.exists_range_eq_of_isConstructible_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Image.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Image.lean#L31).

> **Stacks 00F8.** Every constructible subset of `Spec R` is the image of `Spec S` for a
> finitely presented `R`-algebra `S`.

```lean
theorem exists_range_eq_of_isConstructible_finitePresentation {R : Type u} [CommRing R]
    {s : Set (PrimeSpectrum R)} (hs : IsConstructible s) :
    ∃ (S : Type u) (_ : CommRing S) (f : R →+* S),
      f.FinitePresentation ∧ Set.range (comap f) = s
```

## Tag 00F9, a lemma

[Tag 00F9](https://stacks.math.columbia.edu/tag/00F9) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.localization_away_isOpenEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.localization_away_isOpenEmbedding#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L103) (StacksFrontier): “`Spec R_f → Spec R` is an open embedding”. References: EGA I (1.3.6), “partial”; EGA I (1.6.2), “special case”.
- [`Topology.IsConstructible.image_of_isOpenEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsConstructible.image_of_isOpenEmbedding#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L105) (StacksFrontier): “constructibility transports along an open embedding with retrocompact range”. References: SGA 3 VIB (3.7), “partial”.
- [`PrimeSpectrum.localization_away_comap_range`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.localization_away_comap_range#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L108) (StacksFrontier): “the range of `Spec R_f → Spec R` is `D(f)`”. References: EGA I (1.2.6), “special case”; EGA I (1.6.2), “special case”.
- [`PrimeSpectrum.isRetrocompact_basicOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isRetrocompact_basicOpen#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L112) (StacksFrontier): “`D(f)` is retrocompact”.

## Tag 00FA, a lemma

[Tag 00FA](https://stacks.math.columbia.edu/tag/00FA) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.isClosedEmbedding_comap_of_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isClosedEmbedding_comap_of_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L117) (StacksFrontier): “`Spec (R/I) → Spec R` is a closed embedding”. References: EGA I (1.2.4), “more general”.
- [`PrimeSpectrum.isRetrocompact_zeroLocus_compl_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isRetrocompact_zeroLocus_compl_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L119) (StacksFrontier): “the complement of `V(I)` is retrocompact for a finitely generated `I`”.
- [`Topology.IsConstructible.image_of_isClosedEmbedding`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Topology.IsConstructible.image_of_isClosedEmbedding#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L121) (StacksFrontier): “constructibility transports along a closed embedding with retrocompact range”.
- [`range_comap_of_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=range_comap_of_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L123) (StacksFrontier): “the range of `Spec (R/I) → Spec R` is `V(I)`”.

## Tag 00FB, a lemma

[Tag 00FB](https://stacks.math.columbia.edu/tag/00FB) in the Stacks Project.

**`Polynomial.image_comap_C_basicOpen_eq_biUnion_basicOpen_coeffs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Polynomial.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Polynomial.lean#L103). The attribute's comment: “Second part”.

> **Stacks 00FB**, second part. Let `R` be a ring and `f ∈ R[x]`. The image of the standard open
> `D(f) ⊆ Spec(R[x])` under the map `Spec(R[x]) → Spec(R)` is the union of the standard opens `D(a)`,
> `a` running over the coefficients of `f`; in particular it is a quasi-compact open.

```lean
public theorem image_comap_C_basicOpen_eq_biUnion_basicOpen_coeffs {R : Type*} [CommRing R]
    (f : R[X]) :
    PrimeSpectrum.comap (C : R →+* R[X]) '' (basicOpen f : Set (PrimeSpectrum R[X])) =
      ⋃ a ∈ f.coeffs, (basicOpen a : Set (PrimeSpectrum R))
```

## Tag 00FC, a lemma

[Tag 00FC](https://stacks.math.columbia.edu/tag/00FC) in the Stacks Project.

**`PrimeSpectrum.isNilpotent_baseChange_mulLeft_iff_mem_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L190).

> For `A` free of rank `n` over `R` and `f : A`, the set of primes `p` at which
> multiplication by `f` becomes nilpotent over the residue field is the zero locus of the first
> `n` coefficients of the characteristic polynomial of multiplication by `f`.

```lean
theorem PrimeSpectrum.isNilpotent_baseChange_mulLeft_iff_mem_zeroLocus
    {R A : Type*} [CommRing R] [CommRing A] [Algebra R A]
    (n : ℕ) (e : A ≃ₗ[R] (Fin n → R))
    (f : A) (p : PrimeSpectrum R) :
    IsNilpotent
        (LinearMap.baseChange p.asIdeal.ResidueField
          (LinearMap.mulLeft R f)) ↔
      p ∈ PrimeSpectrum.zeroLocus
        ((fun i : Fin n =>
            (charPolyOfEquiv e (LinearMap.mulLeft R f)).coeff i) '' Set.univ)
```

## Tag 00FD, a lemma

[Tag 00FD](https://stacks.math.columbia.edu/tag/00FD) in the Stacks Project.

**`image_comap_C_basicOpen_inter_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L216).

> **Stacks Tag 00FD.** Let `R` be a ring and `f, g ∈ R[x]` polynomials whose
> leading coefficient of `g` is a unit of `R`. Then the image of `D(f) ∩ V(g)`
> under the structure map `Spec(R[x]) → Spec(R)` is a finite union of standard
> opens: there exist `r_1, …, r_n ∈ R` with image `= ⋃ᵢ D(rᵢ)`.
>
> Since the leading coefficient of `g` is a unit, `g` is associate to the monic
> polynomial `g' = (leadingCoeff g)⁻¹ • g`, so `V(g) = V(g')`. For monic `g'`,
> `R[x]/(g')` is finite free over `R`, and Mathlib's
> `Polynomial.exists_image_comap_of_monic` produces a finite set `t ⊆ R` with
> image `= (V(t))ᶜ = ⋃_{r ∈ t} D(r)`, which we reindex by `Fin n`.

```lean
theorem image_comap_C_basicOpen_inter_zeroLocus
    {R : Type*} [CommRing R] (f g : R[X]) (hg : IsUnit g.leadingCoeff) :
    ∃ (n : ℕ) (r : Fin n → R),
      comap (C : R →+* R[X]) ''
          ((basicOpen f : Set (PrimeSpectrum R[X])) ∩ zeroLocus {g}) =
        ⋃ i, (basicOpen (r i) : Set (PrimeSpectrum R))
```

## Tag 00FE, a theorem

[Tag 00FE](https://stacks.math.columbia.edu/tag/00FE) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.isConstructible_comap_image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isConstructible_comap_image#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L251) (StacksFrontier): “Chevalley's theorem”. References: EGA IV (1.8.4.1), “affine source”; EGA IV (1.9.5), “(viii), special case”; EGA IV (1.8.4), “affine case”; EGA IV (1.8.5), “affine case”; EGA IV (9.5.1), “affine case”; SGA 3 VIB (3.7), “special case”; SGA 3 VIB (4.2), “special case”; SGA 1 IV (6.2), “affine case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.29, Tag 00F5](https://stacks.math.columbia.edu/tag/00F5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
