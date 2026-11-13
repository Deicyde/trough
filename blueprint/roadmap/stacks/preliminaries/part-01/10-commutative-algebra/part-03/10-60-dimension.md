---
declaration: section
origin: cited
lean: LTSeries.mk, RelSeries.length, ringKrullDim, IsLocalization.AtPrime.ringKrullDim_eq_height, ringKrullDim_eq_iSup_height, ringKrullDim_eq_iSup_height_maximal, IsLocalRing.ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero, isArtinianRing_iff_krullDimLE_zero
statement: formalized
proof: formalized
---

# 10.60 Dimension

Section 10.60 of the Stacks Project, [Tag 00KD](https://stacks.math.columbia.edu/tag/00KD). 13 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GIE, a definition

[Tag 0GIE](https://stacks.math.columbia.edu/tag/0GIE) in the Stacks Project.

Declarations registered for the tag:

- [`LTSeries.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LTSeries.mk#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L51) (StacksFrontier): “chains of prime ideals”.
- [`RelSeries.length`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RelSeries.length#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L52) (StacksFrontier): “the length of a chain of prime ideals”.

## Tag 00KE, a definition

[Tag 00KE](https://stacks.math.columbia.edu/tag/00KE) in the Stacks Project.

Declarations registered for the tag:

- [`ringKrullDim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ringKrullDim#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L15) (StacksFrontier): “the Krull dimension of a ring”. References: EGA 0 (16.3.1); EGA II (7.1.5); EGA II (8.10.3); EGA IV (10.5.1); EGA IV (17.15.8); EGA 0 (16.1.1), “definition of dim A”; SGA 2 XI (3.10).

## Tag 00KF, a definition

[Tag 00KF](https://stacks.math.columbia.edu/tag/00KF) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.AtPrime.ringKrullDim_eq_height`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.AtPrime.ringKrullDim_eq_height#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L24) (StacksFrontier). References: EGA 0 (16.1.3), “dim(A\_p) = ht(p)”; EGA 0 (16.3.1), “more general”.

## Tag 00KG, a lemma

[Tag 00KG](https://stacks.math.columbia.edu/tag/00KG) in the Stacks Project.

**`ringKrullDim_eq_iSup_height`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L28).

> The Krull dimension of `R` equals the supremum of the heights of its prime ideals.

```lean
theorem ringKrullDim_eq_iSup_height (R : Type*) [CommRing R] :
    ringKrullDim R = ⨆ (I : PrimeSpectrum R), (I.asIdeal.height : WithBot ℕ∞)
```

**`ringKrullDim_eq_iSup_height_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L35).

> The Krull dimension of `R` equals the supremum of the heights of its maximal ideals.

```lean
theorem ringKrullDim_eq_iSup_height_maximal (R : Type*) [CommRing R] :
    ringKrullDim R =
      ⨆ (I : {I : PrimeSpectrum R // I.asIdeal.IsMaximal}),
        (I.val.asIdeal.height : WithBot ℕ∞)
```

## Tag 00KI, a lemma

[Tag 00KI](https://stacks.math.columbia.edu/tag/00KI) in the Stacks Project.

**`IsLocalRing.ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean#L123). The attribute's comment: “The source reads this off from `d(R) = 0` if and only if `R` has finite length; here it is read off from `d(M) = dim Supp(M)` (Lemma 00L8) for `M = R`.”.

> A Noetherian local ring has dimension zero exactly when its Hilbert–Samuel degree `d(R)`
> is zero.

```lean
theorem ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero :
    ringKrullDim R = 0 ↔ Module.hilbertSamuelDegree R R = 0
```

Declarations registered for the tag:

- [`isArtinianRing_iff_krullDimLE_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isArtinianRing_iff_krullDimLE_zero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks00KI.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks00KI.lean#L10) (StacksFrontier): “dimension zero implies d=0”. References: EGA 0 (16.1.1), “partial”; EGA 0 (16.2.5), “special case”.
- [`isArtinianRing_iff_isFiniteLength`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isArtinianRing_iff_isFiniteLength#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks00KI.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks00KI.lean#L13) (StacksFrontier): “d=0 characterization”. References: SGA 3 VIIB (0.1), “partial”; SGA 3 VIIB (0.4.2), “more general”.

## Tag 00KJ, a proposition

[Tag 00KJ](https://stacks.math.columbia.edu/tag/00KJ) in the Stacks Project.

**`isArtinianRing_tfae_hilbertSamuelDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/HilbertSamuelTFAE.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/HilbertSamuelTFAE.lean#L111). The attribute's comment: “Items (1)-(10) in the source's order. Item (2) reads `dim(R) = 0` as `ringKrullDim R ≤ 0` (`Ring.KrullDimLE 0 R`), which is the literal equality for every nonzero ring (`isArtinianRing_iff_isNoetherianRing_and_ringKrullDim_eq_zero`) and the correct form for the zero ring, whose dimension is `-∞` by Topology, Definition 0055. In (7), `d(R_i)` is `Module.hilbertSamuelDegree` of Definition 00KA. A finite product of local rings is a finite index type and a ring isomorphism `R ≃+* ∀ i, S i`.”.

> **Characterizations of Artinian rings.** For a commutative ring `R` the following are
> equivalent: (1) `R` is Artinian; (2) `R` is Noetherian of Krull dimension at most zero; (3) `R`
> has finite length as a module over itself; (4) `R` is a finite product of Artinian local rings;
> (5) `R` is Noetherian and `Spec(R)` is a finite discrete space; (6) `R` is a finite product of
> Noetherian local rings of Krull dimension `0`; (7) `R` is a finite product of Noetherian local
> rings `R_i` with Hilbert–Samuel degree `d(R_i) = 0`; (8) `R` is a finite product of Noetherian
> local rings with nilpotent maximal ideals; (9) `R` is Noetherian with finitely many maximal
> ideals and nilpotent Jacobson radical; and (10) `R` is Noetherian with no strict inclusions among
> its prime ideals.

```lean
theorem isArtinianRing_tfae_hilbertSamuelDegree (R : Type u) [CommRing R] :
    List.TFAE
      [ IsArtinianRing R,
        IsNoetherianRing R ∧ Ring.KrullDimLE 0 R,
        IsFiniteLength R R,
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)), (∀ i, IsArtinianRing (S i)) ∧ Nonempty (R ≃+* ∀ i, S i),
        IsNoetherianRing R ∧ Finite (PrimeSpectrum R) ∧ DiscreteTopology (PrimeSpectrum R),
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)), (∀ i, IsNoetherianRing (S i) ∧ ringKrullDim (S i) = 0) ∧
            Nonempty (R ≃+* ∀ i, S i),
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)),
          (∀ i, IsNoetherianRing (S i) ∧ Module.hilbertSamuelDegree (S i) (S i) = 0) ∧
            Nonempty (R ≃+* ∀ i, S i),
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)),
          (∀ i, IsNoetherianRing (S i) ∧ IsNilpotent (IsLocalRing.maximalIdeal (S i))) ∧
            Nonempty (R ≃+* ∀ i, S i),
        IsNoetherianRing R ∧ Finite (MaximalSpectrum R) ∧ IsNilpotent (Ring.jacobson R),
        IsNoetherianRing R ∧ ∀ p q : Ideal R, p.IsPrime → q.IsPrime → p ≤ q → p = q ]
```

## Tag 00KK, a lemma

[Tag 00KK](https://stacks.math.columbia.edu/tag/00KK) in the Stacks Project.

**`IsLocalRing.ringKrullDim_eq_one_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean#L134). The attribute's comment: “Items (1)-(5), in the source's order. The ideal generated by zero elements is `⊥`; an ideal of definition is an ideal with radical `m`.”. References: EGA IV (5.1.6), “special case”.

> **Noetherian local rings of dimension one.** For a Noetherian local ring `(R, m)` the
> following are equivalent: `dim(R) = 1`; `d(R) = 1`; there is a non-nilpotent `x ∈ m` with
> `V(x) = {m}`; there is a non-nilpotent `x ∈ m` with `m = √(x)`; some ideal of definition is
> generated by one element, and the ideal `(0)` generated by zero elements is not an ideal of
> definition.

```lean
theorem ringKrullDim_eq_one_tfae :
    List.TFAE
      [ringKrullDim R = 1,
        Module.hilbertSamuelDegree R R = 1,
        ∃ x ∈ maximalIdeal R, ¬ IsNilpotent x ∧ zeroLocus {x} = {closedPoint R},
        ∃ x ∈ maximalIdeal R, ¬ IsNilpotent x ∧ (Ideal.span {x}).radical = maximalIdeal R,
        (∃ x : R, (Ideal.span {x}).radical = maximalIdeal R) ∧
          (⊥ : Ideal R).radical ≠ maximalIdeal R]
```

## Tag 00KQ, a proposition

[Tag 00KQ](https://stacks.math.columbia.edu/tag/00KQ) in the Stacks Project.

**`IsLocalRing.ringKrullDim_eq_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/DimensionTheorem.lean, line 1000](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/HilbertSamuel/DimensionTheorem.lean#L1000). The attribute's comment: “Items (1)-(3); see the module docstring for the form of (2) and (3).”. References: EGA 0 (16.2.5), “local case”; EGA IV (5.1.6).

> **Dimension of a Noetherian local ring.** For a Noetherian local ring `(R, m)` and a natural
> number `d` the following are equivalent: `dim(R) = d`; the Hilbert–Samuel function
> `n ↦ length_R (R / m ^ (n + 1))` is eventually a `ℤ`-combination
> `∑_{i ≤ d} (n choose i) * a i` of binomial coefficients with `a d ≠ 0`, i.e. `d(R) = d`; and `d`
> is the least number of generators of an ideal of definition of `R`, i.e. some ideal of definition
> is generated by `d` elements and none is generated by fewer.

```lean
public theorem IsLocalRing.ringKrullDim_eq_tfae {R : Type*} [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] (d : ℕ) :
    List.TFAE
      [ringKrullDim R = d,
        ∃ a : ℕ → ℤ,
          a d ≠ 0 ∧
            ∀ᶠ n : ℕ in Filter.atTop,
              ∃ p : ℕ,
                Module.length R (R ⧸ maximalIdeal R ^ (n + 1)) = p ∧
                  (p : ℤ) = ∑ i ∈ Finset.range (d + 1), (n.choose i : ℤ) * a i,
        IsLeast {n : ℕ | ∃ I : Ideal R, I.radical = maximalIdeal R ∧ I.spanFinrank = n} d]
```

## Tag 00KU, a definition

[Tag 00KU](https://stacks.math.columbia.edu/tag/00KU) in the Stacks Project.

**`IsLocalRing.IsSystemOfParameters`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Defs.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Defs.lean#L118). The attribute's comment: “Item (1). Item (2) is `IsLocalRing.IsRegularSystemOfParametersList` (a regular system of parameters) and `IsLocalRing.HasRegularSystemOfParameters` (a regular local ring), the latter equivalent over a Noetherian local ring to Mathlib's `IsRegularLocalRing` by `IsLocalRing.isRegularLocalRing_iff_hasRegularSystemOfParameters`.”. References: EGA 0 (16.3.6), “case M = R, local”.

> **System of parameters of a local ring**. A sequence `rs` of elements of a local ring `(R, m)`
> is a *system of parameters* of `R` if it generates an ideal of definition of `R`, that is an ideal
> with radical `m`, and has `dim R` entries. Over a Noetherian local ring this is the source's
> notion: `dim R` elements of `m` generating an ideal of definition, `dim R` being the least number
> of generators an ideal of definition can have. A *regular* system of parameters is one generating
> `m` itself, `IsLocalRing.IsRegularSystemOfParametersList`; the rings admitting one are the regular
> local rings, `IsLocalRing.HasRegularSystemOfParameters` (Mathlib's `IsRegularLocalRing`).

```lean
public def IsLocalRing.IsSystemOfParameters {R : Type*} [CommRing R] [IsLocalRing R]
    (rs : List R) : Prop
```

**`IsLocalRing.IsRegularSystemOfParametersList`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Regular.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Regular.lean#L56). The attribute's comment: “Item (2), the sequence notion: a regular system of parameters, `m = (x_1, …, x_d)` with `d = dim R`.”.

> **Regular system of parameters** (Stacks 00KU, item (2)). A sequence `rs` of elements of a
> local ring `(R, m)` is a *regular system of parameters* of `R` if it generates the maximal ideal
> `m` and has `dim R` entries. Its entries then lie in `m`.

```lean
def IsRegularSystemOfParametersList (rs : List R) : Prop
```

**`IsLocalRing.HasRegularSystemOfParameters`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Regular.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Regular.lean#L67). The attribute's comment: “Item (2), the predicate on the ring: there exist `x_1, …, x_d ∈ m` with `m = (x_1, …, x_d)`, `d = dim R`. Equivalent to Mathlib's `IsRegularLocalRing` over a Noetherian local ring by `isRegularLocalRing_iff_hasRegularSystemOfParameters`.”.

> **Regular local ring, Stacks' definition** (Stacks 00KU, item (2)). A local ring `R` is
> regular in the sense of the source if it admits a regular system of parameters, i.e. its maximal
> ideal is generated by `dim R` elements. Over a Noetherian local ring this is Mathlib's
> `IsRegularLocalRing`, see `IsLocalRing.isRegularLocalRing_iff_hasRegularSystemOfParameters`.

```lean
def HasRegularSystemOfParameters : Prop
```

## Tag 00KV, a lemma

[Tag 00KV](https://stacks.math.columbia.edu/tag/00KV) in the Stacks Project.

**`Ideal.height_le_one_of_mem_minimalPrimes_span_singleton_and_not_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean#L336). The attribute's comment: “Item (1) is Mathlib's Krull principal ideal theorem `Ideal.height_le_one_of_isPrincipal_of_mem_minimalPrimes` applied to `Ideal.span {x}`; item (2) is `Ideal.not_lt_of_lt_of_mem_minimalPrimes_sup_span_singleton`.”.

> **Stacks 00KV.** Let `R` be a Noetherian ring and `x ∈ R`.
> 1. If a prime `p` is minimal over `(x)`, then `p` has height `0` or `1`, that is, height `≤ 1`.
> 2. If `p` is a prime and the prime `q` is minimal over `(p, x)`, then there is no prime strictly
>    between `p` and `q`: no prime `r` satisfies `p < r < q`.

```lean
public theorem Ideal.height_le_one_of_mem_minimalPrimes_span_singleton_and_not_lt {R : Type*}
    [CommRing R] [IsNoetherianRing R] (x : R) :
    (∀ p ∈ (Ideal.span {x}).minimalPrimes, p.height ≤ 1) ∧
      ∀ p q : Ideal R, p.IsPrime → q ∈ (p ⊔ Ideal.span {x}).minimalPrimes →
        ∀ r : Ideal R, r.IsPrime → p < r → ¬r < q
```

## Tag 0BBZ, a lemma

[Tag 0BBZ](https://stacks.math.columbia.edu/tag/0BBZ) in the Stacks Project.

**`Ideal.map_height_le_spanRank_toENat_of_mem_minimalPrimes_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean#L180). The attribute's comment: “Item (2), for an arbitrary ideal in place of the prime; item (1) is Mathlib's `Ideal.height_le_spanRank_toENat_of_mem_minimalPrimes`.”. References: EGA 0 (16.3.1), “b ⇒ a”; EGA 0 (16.3.2), “more general”.

> **Stacks 0BBZ (2), Krull's height theorem in relative form.** Let `R` be a Noetherian ring
> and let `I`, `J` be ideals of `R`. If a prime `q` is minimal over `I + J`, then the height of
> `q / I` in `R / I` is at most the minimal number of generators of `J`; equivalently, every chain
> of primes between `I` and `q` has length at most that number.

```lean
public theorem Ideal.map_height_le_spanRank_toENat_of_mem_minimalPrimes_sup {R : Type*}
    [CommRing R] [IsNoetherianRing R] {I J q : Ideal R} (hq : q ∈ (I ⊔ J).minimalPrimes) :
    (q.map (Ideal.Quotient.mk I)).height ≤ J.spanRank.toENat
```

## Tag 00KW, a lemma

[Tag 00KW](https://stacks.math.columbia.edu/tag/00KW) in the Stacks Project.

**`ringKrullDim_le_quotient_span_singleton_add_one_and_eq_of_notMem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Regular.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Regular.lean#L57). The attribute's comment: “both the inequality and the equality when x avoids the minimal primes”.

> **Stacks 00KW.** Let `R` be a Noetherian local ring and `x ∈ 𝔪`. Then
> `dim R ≤ dim R/xR + 1`, and if `x` is contained in no minimal prime of `R` then
> `dim R/xR + 1 = dim R`.

```lean
theorem ringKrullDim_le_quotient_span_singleton_add_one_and_eq_of_notMem_minimalPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] {x : R}
    (hx : x ∈ maximalIdeal R) :
    ringKrullDim R ≤ ringKrullDim (R ⧸ span {x}) + 1 ∧
      ((∀ p ∈ minimalPrimes R, x ∉ p) → ringKrullDim (R ⧸ span {x}) + 1 = ringKrullDim R)
```

## Tag 02IE, a lemma

[Tag 02IE](https://stacks.math.columbia.edu/tag/02IE) in the Stacks Project.

**`ringKrullDim_add_length_eq_ringKrullDim_of_radical_ofList_append_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters.lean#L247). References: EGA 0 (16.2.3.1), “(ii), special case”.

> **Dimension of a quotient by part of a system of parameters.** Let `(R, m)` be a Noetherian
> local ring and let `x₁, …, x_d ∈ m` generate an ideal of definition of `R`, with
> `d ≤ dim R` — equivalently, `x₁, …, x_d` is a system of parameters. Then killing any part
> `l` of the sequence drops the dimension by exactly the number of elements killed:
> `dim R/(l) + |l| = dim R`. Taking `l` to be the prefix `x₁, …, x_i` gives
> `dim R/(x₁, …, x_i) = d - i`.

```lean
public theorem ringKrullDim_add_length_eq_ringKrullDim_of_radical_ofList_append_eq_maximalIdeal
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] (l l' : List R)
    (hdef : (Ideal.ofList (l ++ l')).radical = IsLocalRing.maximalIdeal R)
    (hdim : ((l.length + l'.length : ℕ) : WithBot ℕ∞) ≤ ringKrullDim R) :
    ringKrullDim (R ⧸ Ideal.ofList l) + l.length =
      ringKrullDim R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.60, Tag 00KD](https://stacks.math.columbia.edu/tag/00KD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
