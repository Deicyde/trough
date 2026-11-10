---
declaration: section
origin: cited
lean: LTSeries.mk, RelSeries.length, ringKrullDim, IsLocalization.AtPrime.ringKrullDim_eq_height, ringKrullDim_eq_iSup_height, ringKrullDim_eq_iSup_height_maximal, IsLocalRing.ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero, isArtinianRing_iff_krullDimLE_zero
statement: formalized
proof: formalized
---

# 10.60 Dimension

Section 10.60 of the Stacks Project, [Tag 00KD](https://stacks.math.columbia.edu/tag/00KD). 13 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GIE, a definition

[Tag 0GIE](https://stacks.math.columbia.edu/tag/0GIE) in the Stacks Project.

Declarations registered for the tag:

- [`LTSeries.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LTSeries.mk#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L51) (StacksFrontier): “chains of prime ideals”.
- [`RelSeries.length`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RelSeries.length#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L52) (StacksFrontier): “the length of a chain of prime ideals”.

## Tag 00KE, a definition

[Tag 00KE](https://stacks.math.columbia.edu/tag/00KE) in the Stacks Project.

Declarations registered for the tag:

- [`ringKrullDim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ringKrullDim#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L15) (StacksFrontier): “the Krull dimension of a ring”. References: EGA 0 (16.3.1); EGA II (7.1.5); EGA II (8.10.3); EGA IV (10.5.1); EGA IV (17.15.8); EGA 0 (16.1.1), “definition of dim A”; SGA 2 XI (3.10).

## Tag 00KF, a definition

[Tag 00KF](https://stacks.math.columbia.edu/tag/00KF) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalization.AtPrime.ringKrullDim_eq_height`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.AtPrime.ringKrullDim_eq_height#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L24) (StacksFrontier). References: EGA 0 (16.1.3), “dim(A_p) = ht(p)”; EGA 0 (16.3.1), “more general”.

## Tag 00KG, a lemma

[Tag 00KG](https://stacks.math.columbia.edu/tag/00KG) in the Stacks Project.

**`ringKrullDim_eq_iSup_height`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L28).

> The Krull dimension of `R` equals the supremum of the heights of its prime ideals.

```lean
theorem ringKrullDim_eq_iSup_height (R : Type*) [CommRing R] :
    ringKrullDim R = ⨆ (I : PrimeSpectrum R), (I.asIdeal.height : WithBot ℕ∞)
```

**`ringKrullDim_eq_iSup_height_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Defs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Defs.lean#L35).

> The Krull dimension of `R` equals the supremum of the heights of its maximal ideals.

```lean
theorem ringKrullDim_eq_iSup_height_maximal (R : Type*) [CommRing R] :
    ringKrullDim R =
      ⨆ (I : {I : PrimeSpectrum R // I.asIdeal.IsMaximal}),
        (I.val.asIdeal.height : WithBot ℕ∞)
```

## Tag 00KI, a lemma

[Tag 00KI](https://stacks.math.columbia.edu/tag/00KI) in the Stacks Project.

**`IsLocalRing.ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean#L123). The attribute's comment: “The source reads this off from `d(R) = 0` if and only if `R` has finite length; here it is read off from `d(M) = dim Supp(M)` (Lemma 00L8) for `M = R`.”.

> A Noetherian local ring has dimension zero exactly when its Hilbert–Samuel degree `d(R)`
> is zero.

```lean
theorem ringKrullDim_eq_zero_iff_hilbertSamuelDegree_eq_zero :
    ringKrullDim R = 0 ↔ Module.hilbertSamuelDegree R R = 0
```

Declarations registered for the tag:

- [`isArtinianRing_iff_krullDimLE_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isArtinianRing_iff_krullDimLE_zero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks00KI.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Stacks00KI.lean#L10) (StacksFrontier): “dimension zero implies d=0”. References: EGA 0 (16.1.1), “partial”; EGA 0 (16.2.5), “special case”.
- [`isArtinianRing_iff_isFiniteLength`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isArtinianRing_iff_isFiniteLength#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks00KI.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Stacks00KI.lean#L13) (StacksFrontier): “d=0 characterization”. References: SGA 3 VIIB (0.1), “partial”; SGA 3 VIIB (0.4.2), “more general”.

## Tag 00KJ, a proposition

[Tag 00KJ](https://stacks.math.columbia.edu/tag/00KJ) in the Stacks Project.

**`isArtinianRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/TFAE.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Artinian/TFAE.lean#L272). The attribute's comment: “Items (1)-(10); see the module docstring for the form of (2), (5), (6) and (7).”. References: EGA 0 (14.1.9), “affine case: X = Spec R”; EGA 0 (16.1.10), “case M = A”; EGA I (6.2.2), “affine case”; EGA IV (10.4.3), “partial”; SGA 3 VIIB (0.1.1), “partial”; SGA 3 VIIB (3.2), “U = C”.

> **Characterizations of Artinian rings.** For a commutative ring `R` the following are
> equivalent: `R` is Artinian; `R` is Noetherian of Krull dimension zero; `R` has finite length as
> a module over itself; `R` is a finite product of Artinian local rings; `R` is Noetherian with
> discrete prime spectrum; `R` is a finite product of Noetherian local rings of dimension zero;
> `R` is a finite product of Noetherian local rings of finite length; `R` is a finite product of
> Noetherian local rings with nilpotent maximal ideal; `R` is Noetherian with finitely many
> maximal ideals and nilpotent Jacobson radical; and `R` is Noetherian with no strict inclusions
> among its primes.

```lean
public theorem isArtinianRing_tfae (R : Type u) [CommRing R] :
    List.TFAE
      [ IsArtinianRing R,
        IsNoetherianRing R ∧ Ring.KrullDimLE 0 R,
        IsFiniteLength R R,
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)), (∀ i, IsArtinianRing (S i)) ∧ Nonempty (R ≃+* ∀ i, S i),
        IsNoetherianRing R ∧ DiscreteTopology (PrimeSpectrum R),
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)), (∀ i, IsNoetherianRing (S i) ∧ Ring.KrullDimLE 0 (S i)) ∧
            Nonempty (R ≃+* ∀ i, S i),
        ∃ (ι : Type u) (_ : Finite ι) (S : ι → Type u) (_ : ∀ i, CommRing (S i))
          (_ : ∀ i, IsLocalRing (S i)), (∀ i, IsFiniteLength (S i) (S i)) ∧
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

**`IsLocalRing.ringKrullDim_eq_one_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/DimensionOneNoetherianLocal.lean#L134). The attribute's comment: “Items (1)-(5), in the source's order. The ideal generated by zero elements is `⊥`; an ideal of definition is an ideal with radical `m`.”. References: EGA IV (5.1.6), “special case”.

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

**`IsLocalRing.ringKrullDim_eq_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/DimensionTheorem.lean, line 1000](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/DimensionTheorem.lean#L1000). The attribute's comment: “Items (1)-(3); see the module docstring for the form of (2) and (3).”. References: EGA 0 (16.2.5), “local case”; EGA 0 (16.2.5), “local case”; EGA IV (5.1.6).

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

**`IsLocalRing.IsSystemOfParameters`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Defs.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters/Defs.lean#L116). The attribute's comment: “Item (1). Item (2)'s predicate on the ring is Mathlib's `IsRegularLocalRing`, tagged 00KU there; a regular system of parameters is `Ideal.ofList rs = maximalIdeal R` together with `ringKrullDim R = rs.length`, a composite for which no name is introduced. See the module docstring.”. References: EGA 0 (16.3.6), “case M = R, local”.

> **System of parameters of a local ring**. A sequence `rs` of elements of a local ring `(R, m)`
> is a *system of parameters* of `R` if it generates an ideal of definition of `R`, that is an ideal
> with radical `m`, and has `dim R` entries. Over a Noetherian local ring this is the source's
> notion: `dim R` elements of `m` generating an ideal of definition, `dim R` being the least number
> of generators an ideal of definition can have. A *regular* system of parameters is one generating
> `m` itself; the rings admitting one are the regular local rings, `IsRegularLocalRing`.

```lean
public def IsLocalRing.IsSystemOfParameters {R : Type*} [CommRing R] [IsLocalRing R]
    (rs : List R) : Prop
```

## Tag 00KV, a lemma

[Tag 00KV](https://stacks.math.columbia.edu/tag/00KV) in the Stacks Project.

**`Ideal.not_lt_of_lt_of_mem_minimalPrimes_sup_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean#L321). The attribute's comment: “Item (2); item (1) is Mathlib's Krull principal ideal theorem.”.

> **Krull's principal ideal theorem, chain form.** Let `R` be a Noetherian ring, `x : R`, and
> let `p` be a prime ideal. If a prime `q` is minimal over `p + (x)`, then no prime `r` lies
> strictly between `p` and `q`.

```lean
public theorem Ideal.not_lt_of_lt_of_mem_minimalPrimes_sup_span_singleton {R : Type*}
    [CommRing R] [IsNoetherianRing R] {x : R} {p q r : Ideal R} [p.IsPrime] [r.IsPrime]
    (hq : q ∈ (p ⊔ Ideal.span {x}).minimalPrimes) (hpr : p < r) : ¬r < q
```

## Tag 0BBZ, a lemma

[Tag 0BBZ](https://stacks.math.columbia.edu/tag/0BBZ) in the Stacks Project.

**`Ideal.map_height_le_spanRank_toENat_of_mem_minimalPrimes_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/KrullsHeightTheorem.lean#L180). The attribute's comment: “Item (2), for an arbitrary ideal in place of the prime; item (1) is Mathlib's `Ideal.height_le_spanRank_toENat_of_mem_minimalPrimes`.”. References: EGA 0 (16.3.1), “b ⇒ a”; EGA 0 (16.3.2), “more general”.

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

**`Ideal.height_le_height_map_add_encard_of_span_eq_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/AffineIntersection.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/AffineIntersection.lean#L86). The attribute's comment: “through a surjection”.

> **Krull's height theorem through a surjection.** If `δ` is a surjective ring map whose
> kernel is generated by a set `s`, and `M` is a prime containing `s`, then the height of `M` is
> at most the height of its image plus the cardinality of `s`. This is the iterated form of
> Stacks Tag 00KW that the reduction to the diagonal consumes.

```lean
theorem Ideal.height_le_height_map_add_encard_of_span_eq_ker {T C : Type*} [CommRing T]
    [CommRing C] [IsNoetherianRing T] (δ : T →+* C) (hδ : Function.Surjective δ) (s : Set T)
    (hspan : Ideal.span s = RingHom.ker δ) (M : Ideal T) [M.IsPrime] (hsM : s ⊆ M) :
    M.height ≤ (M.map δ).height + s.encard
```

## Tag 02IE, a lemma

[Tag 02IE](https://stacks.math.columbia.edu/tag/02IE) in the Stacks Project.

**`ringKrullDim_add_length_eq_ringKrullDim_of_radical_ofList_append_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/SystemOfParameters.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/SystemOfParameters.lean#L247). References: EGA 0 (16.2.3.1), “(ii), special case”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
