---
declaration: section
origin: cited
lean: IsUniversallyJapaneseRing, IsNagataRing, IsIntegralClosure.finite_of_essFiniteType_of_isReduced, isUniversallyJapanese_of_finiteType_isN1, isUniversallyJapanese_of_isEssentiallyOfFiniteType, isNagataRing_of_quasiFinite, isNagata_of_isLocalization, isUniversallyJapaneseRing_and_isNagataRing_of_localizationSpan
statement: formalized
proof: formalized
---

# 10.162 Nagata rings

Section 10.162 of the Stacks Project, [Tag 032E](https://stacks.math.columbia.edu/tag/032E). 17 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 032R, a definition

[Tag 032R](https://stacks.math.columbia.edu/tag/032R) in the Stacks Project.

**`IsUniversallyJapaneseRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Defs.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Defs.lean#L119). The attribute's comment: “(1)”. References: EGA 0 (23.1.1); EGA IV (7.7.1).

> A ring `R` is **universally Japanese** if for every finite-type ring map `R → S` with `S` a
> domain, the domain `S` is N-2 (Japanese), i.e. satisfies `IsJapaneseRing`.

```lean
class IsUniversallyJapaneseRing (R : Type u) [CommRing R] : Prop
```

**`IsNagataRing`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Defs.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Defs.lean#L129). The attribute's comment: “(2)”.

> A ring `R` is a **Nagata ring** if `R` is Noetherian and for every prime ideal `p ⊆ R` the
> quotient domain `R ⧸ p` is N-2 (Japanese), i.e. satisfies `IsJapaneseRing`.

```lean
class IsNagataRing (R : Type u) [CommRing R] : Prop
```

## Tag 03GH, a lemma

[Tag 03GH](https://stacks.math.columbia.edu/tag/03GH) in the Stacks Project.

**`IsIntegralClosure.finite_of_essFiniteType_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/IntegralClosure.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/IntegralClosure.lean#L264). References: EGA II (6.3.10), “special case”.

> **A Nagata ring has finite integral closure in a reduced algebra essentially of finite type.**
>
> Let `R` be a Nagata ring, that is, a Noetherian ring such that `R ⧸ p` is N-2 (Japanese) for
> every prime `p`, and let `S` be a reduced `R`-algebra essentially of finite type. Then the
> integral closure `A` of `R` in `S` is a finite `R`-module.

```lean
public theorem IsIntegralClosure.finite_of_essFiniteType_of_isReduced
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    {S : Type u} [CommRing S] [Algebra R S] [Algebra.EssFiniteType R S] [IsReduced S]
    {A : Type v} [CommRing A] [Algebra R A] [Algebra A S] [IsScalarTower R A S]
    [IsIntegralClosure A R S]
    (hR : ∀ (p : Ideal R) [p.IsPrime], IsJapaneseRing (R ⧸ p)) :
    Module.Finite R A
```

## Tag 0351, a lemma

[Tag 0351](https://stacks.math.columbia.edu/tag/0351) in the Stacks Project.

**`isUniversallyJapanese_of_finiteType_isN1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Japanese/N1Criterion.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Japanese/N1Criterion.lean#L258). References: EGA IV (7.7.1), “N-1 ⇒ univ. Japanese”.

> **Stacks Tag 0351.** Let `R` be a ring such that for every finite type ring map
> `R → S` with `S` a domain, the domain `S` is N-1. Then `R` is universally Japanese.

```lean
theorem isUniversallyJapanese_of_finiteType_isN1 (R : Type u) [CommRing R]
    (H : ∀ (S : Type u) [CommRing S] [IsDomain S] [Algebra R S] [Algebra.FiniteType R S], IsN1 S) :
    IsUniversallyJapaneseRing R
```

## Tag 032S, a lemma

[Tag 032S](https://stacks.math.columbia.edu/tag/032S) in the Stacks Project.

**`isUniversallyJapanese_of_isEssentiallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Japanese/EssFiniteType.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Japanese/EssFiniteType.lean#L372). References: EGA IV (7.7.2), “moreover clause”.

> (Stacks Tag 032S, Lemma 10.162.4) If `R` is universally Japanese then any
> `R`-algebra `A` essentially of finite type over `R` is universally Japanese.

```lean
theorem isUniversallyJapanese_of_isEssentiallyOfFiniteType (R : Type u) [CommRing R] (A : Type u)
    [CommRing A] [Algebra R A] (hR : IsUniversallyJapanese R)
    (hA : IsEssentiallyOfFiniteType R A (algebraMap R A)) : IsUniversallyJapanese A
```

## Tag 032T, a lemma

[Tag 032T](https://stacks.math.columbia.edu/tag/032T) in the Stacks Project.

**`isNagataRing_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/QuasiFinite.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/QuasiFinite.lean#L154).

> **A quasi-finite algebra over a Nagata ring is a Nagata ring.** If `R` is a Nagata ring —
> Noetherian, with every quotient `R ⧸ p` by a prime N-2 — and `R → S` is quasi-finite, that is of
> finite type with finite-dimensional fibres (for example module-finite), then `S` is a Nagata ring.
>
> Quasi-finiteness in the sense of [Stacks, Tag 00PL] is the conjunction
> `[Algebra.FiniteType R S] [Algebra.QuasiFinite R S]`, Mathlib's `Algebra.QuasiFinite` omitting the
> finite type condition. No injectivity is required: the map `R → S` is arbitrary.

```lean
public theorem isNagataRing_of_quasiFinite {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FiniteType R S] [Algebra.QuasiFinite R S] (hR : IsNagataRing R) :
    IsNagataRing S
```

## Tag 032U, a lemma

[Tag 032U](https://stacks.math.columbia.edu/tag/032U) in the Stacks Project.

**`isNagata_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Japanese/Localization.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Japanese/Localization.lean#L211). References: EGA IV (7.7.2).

> (Stacks Tag 032U) A localization of a Nagata ring is a Nagata ring.
>
> Here `T` is an arbitrary `R`-algebra realizing `T = M⁻¹R` for a submonoid `M ⊆ R`
> (`IsLocalization M T`), which is exactly Definition 4 of a localization. The single-element
> case `R_f` (`M = {1, f, f², …}`) and the prime case `R_p` (`M = R ∖ p`) are special cases.
>
> Proof structure (Stacks: "clear from Tag 032G"):
> * Noetherianity of `T` is `IsLocalization.isNoetherianRing M T hR.isNoetherianRing`.
> * For a prime `q ⊆ T`, set `p := q.comap (R → T)` (prime by `Ideal.comap_isPrime`). Then
>   `R/p` is N-2 (`hR.isJapaneseRing_quotient p`), and `T/q ≅ M̄⁻¹(R/p)` is a localization of the
>   domain `R/p` at the image `M̄` of `M`, which lies in the nonzerodivisors of `R/p`. By
>   `isN2_of_isLocalization_domain`, `T/q` is N-2. Hence `T` is Nagata.

```lean
theorem isNagata_of_isLocalization (R : Type u) [CommRing R] (M : Submonoid R) (T : Type u)
    [CommRing T] [Algebra R T] [IsLocalization M T] (hR : IsNagataRing R) :
    IsNagataRing T
```

## Tag 032V, a lemma

[Tag 032V](https://stacks.math.columbia.edu/tag/032V) in the Stacks Project.

**`isUniversallyJapaneseRing_and_isNagataRing_of_localizationSpan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Descent.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Descent.lean#L288).

> **Universally Japanese and Nagata descend along a principal open cover.** Let `t ⊆ R`
> generate the unit ideal and for `g ∈ t` let `Rₚ g` be a localization of `R` away from `g`. If
> every `Rₚ g` is universally Japanese then so is `R`, and if every `Rₚ g` is a Nagata ring then so
> is `R`.
>
> The source states the two parts for finitely many `f₁, …, f_n`; they are the two conjuncts
> here, and an arbitrary spanning set is the same hypothesis.

```lean
public theorem isUniversallyJapaneseRing_and_isNagataRing_of_localizationSpan {R : Type u}
    [CommRing R] (t : Set R) (ht : Ideal.span t = ⊤) (Rₚ : ∀ _ : t, Type u)
    [∀ g, CommRing (Rₚ g)] [∀ g, Algebra R (Rₚ g)] [∀ g, IsLocalization.Away g.val (Rₚ g)] :
    ((∀ g, IsUniversallyJapaneseRing (Rₚ g)) → IsUniversallyJapaneseRing R) ∧
      ((∀ g, IsNagataRing (Rₚ g)) → IsNagataRing R)
```

## Tag 032W, a lemma

[Tag 032W](https://stacks.math.columbia.edu/tag/032W) in the Stacks Project.

**`IsNagataRing.of_isPrecomplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/CompleteLocalRing.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/CompleteLocalRing.lean#L290). References: EGA 0 (23.1.5), “more general”.

> **A Noetherian complete local ring is a Nagata ring.** If `R` is Noetherian, local, and
> complete for the topology defined by its maximal ideal `m`, then `R` is a Nagata ring: for every
> prime `p ⊆ R` the quotient domain `R ⧸ p` is N-2 (Japanese).
>
> Completeness is asked for as `IsPrecomplete (IsLocalRing.maximalIdeal R) R`; the Hausdorff half
> of `IsAdicComplete` is automatic for a Noetherian local ring, so a ring with
> `IsAdicComplete (IsLocalRing.maximalIdeal R) R` satisfies the hypothesis by inference.

```lean
public theorem IsNagataRing.of_isPrecomplete_maximalIdeal {R : Type u} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] [IsPrecomplete (IsLocalRing.maximalIdeal R) R] :
    IsNagataRing R
```

## Tag 032X, a definition

[Tag 032X](https://stacks.math.columbia.edu/tag/032X) in the Stacks Project.

**`IsAnalyticallyUnramified`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Defs.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AnalyticallyUnramified/Defs.lean#L107). References: SGA 1 I (9.4).

> A local ring `R` with maximal ideal `m` is **analytically unramified** if its completion
> `R^ = lim_n R ⧸ mⁿ` is reduced.
>
> The source asks for `R` Noetherian; that hypothesis is not needed to state the condition and is
> carried by the lemmas about it. A prime ideal `p ⊂ R` is analytically unramified when the local
> ring `R ⧸ p` is, i.e. when `IsAnalyticallyUnramified (R ⧸ p)` holds.

```lean
public def IsAnalyticallyUnramified (R : Type*) [CommRing R] [IsLocalRing R] : Prop
```

## Tag 032Y, a lemma

[Tag 032Y](https://stacks.math.columbia.edu/tag/032Y) in the Stacks Project.

**`isAnalyticallyUnramified_iff_minimalPrimes_and_isN1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/MinimalPrimes.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/MinimalPrimes.lean#L638).

> **Tag 032Y.** Let `(R, m)` be a Noetherian local ring. Then `R` is analytically unramified if
> and only if `R` is reduced and each of its minimal primes `q` is analytically unramified, i.e.
> each local ring `R ⧸ q` is; and an analytically unramified `R` is N-1, i.e. the integral closure
> of `R` in its total ring of fractions `Q(R)` is a finite `R`-module.
>
> The first conjunct is parts (1), (2) and (3) of the source, the forward direction being (1) and
> (2) and the converse being (3); the second conjunct is part (4), and part (5) is that conjunct
> with `[IsDomain R]` adjoined.

```lean
public theorem isAnalyticallyUnramified_iff_minimalPrimes_and_isN1 (R : Type*) [CommRing R]
    [IsLocalRing R] [IsNoetherianRing R] :
    (IsAnalyticallyUnramified R ↔
        IsReduced R ∧
          ∀ q ∈ minimalPrimes R, ∀ [IsLocalRing (R ⧸ q)], IsAnalyticallyUnramified (R ⧸ q)) ∧
      (IsAnalyticallyUnramified R → IsN1 R)
```

## Tag 032Z, a lemma

[Tag 032Z](https://stacks.math.columbia.edu/tag/032Z) in the Stacks Project.

**`exists_isDiscreteValuationRing_atPrime_of_analyticallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/AnalyticallyUnramified.lean, line 1235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AdicCompletion/AnalyticallyUnramified.lean#L1235).

> **Stacks Tag 032Z.** Let `R` be a Noetherian local ring and `p ⊂ R` a prime
> ideal such that the localization `R_p` is a discrete valuation ring and `p` is
> analytically unramified (`R^ / p R^` is reduced). Then for every associated prime
> `q` of the `R^`-module `R^ / p R^`, the local ring `(R^)_q` is a discrete
> valuation ring.

```lean
theorem exists_isDiscreteValuationRing_atPrime_of_analyticallyUnramified {R : Type*} [CommRing R]
  [IsLocalRing R] [IsNoetherianRing R] (p : Ideal R)
    [p.IsPrime]
    -- (1) `R_p` is a discrete valuation ring (hence a domain).
    [IsDomain (Localization.AtPrime p)] (hdvr : IsDiscreteValuationRing (Localization.AtPrime p))
    -- (2) `p` is analytically unramified: `R^ / p R^` is reduced.
    (hunr : AnalyticallyUnramifiedPrime p)
    -- `q` is an associated prime of the `R^`-module `R^ / p R^`.
    (q : Ideal (mCompletion R)) (hq : IsAssociatedPrime q (mCompletion R ⧸ pCompletion p)) :
    -- Conclusion: `(R^)_q` is a discrete valuation ring (in particular a domain).
    ∃ (_ : q.IsPrime) (_ : IsDomain (Localization.AtPrime q)),
      IsDiscreteValuationRing (Localization.AtPrime q)
```

## Tag 0330, a lemma

[Tag 0330](https://stacks.math.columbia.edu/tag/0330) in the Stacks Project.

**`IsAnalyticallyUnramified.of_associatedPrimes_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/CuttingByNonzerodivisor.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/CuttingByNonzerodivisor.lean#L507). The attribute's comment: “The source's `R` a domain with `x ≠ 0` is generalized to `x` a nonzerodivisor, which is all the proof uses; `R ⧸ xR` having no embedded primes is spelled as every associated prime of `R ⧸ xR` being minimal over `xR`, there being no predicate for it in this library.”.

> **Stacks Tag 0330.** Let `(R, 𝔪)` be a Noetherian local ring and let `x ∈ 𝔪` be a
> nonzerodivisor. If `R ⧸ xR` has no embedded primes — every associated prime of the module `R ⧸ xR`
> is minimal over `xR` — and every associated prime `𝔭` of `R ⧸ xR` has `R_𝔭` regular and is
> analytically unramified, then `R` is analytically unramified.
>
> The source assumes `R` a domain and `x ≠ 0`; only `x ∈ nonZeroDivisors R` is used, and it is what
> those two amount to.

```lean
public theorem IsAnalyticallyUnramified.of_associatedPrimes_quotient_span_singleton {R : Type*}
    [CommRing R] [IsNoetherianRing R] [IsLocalRing R] {x : R} (hx : x ∈ nonZeroDivisors R)
    (hxm : x ∈ maximalIdeal R)
    (hemb : associatedPrimes R (R ⧸ Ideal.span {x}) ⊆ (Ideal.span {x}).minimalPrimes)
    (hp :
      ∀ (p : Ideal R) [p.IsPrime] [IsLocalRing (R ⧸ p)],
        p ∈ associatedPrimes R (R ⧸ Ideal.span {x}) →
          IsRegularLocalRing (Localization.AtPrime p) ∧ IsAnalyticallyUnramified (R ⧸ p)) :
    IsAnalyticallyUnramified R
```

## Tag 0331, a lemma

[Tag 0331](https://stacks.math.columbia.edu/tag/0331) in the Stacks Project.

**`IsAnalyticallyUnramified.of_isNagataRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/NagataDomain.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AnalyticallyUnramified/Criteria/NagataDomain.lean#L316). The attribute's comment: “Nagata is `IsNagataRing` of Definition 032R(2), whose first conjunct is `IsNoetherianRing R`, so the source's Noetherian hypothesis is absorbed rather than restated; analytically unramified is the predicate of Tag 032X, reducedness of the `𝔪`-adic completion.”.

> **Stacks Tag 0331.** A local ring `(R, 𝔪)` which is a domain and a Nagata ring is
> analytically unramified: its completion `R^ = lim_n R ⧸ 𝔪ⁿ` is reduced.
>
> The source also assumes `R` Noetherian; that is the first conjunct of `IsNagataRing R`.

```lean
public theorem IsAnalyticallyUnramified.of_isNagataRing {R : Type*} [CommRing R] [IsLocalRing R]
    [IsDomain R] (hR : IsNagataRing R) : IsAnalyticallyUnramified R
```

## Tag 0BI2, a lemma

[Tag 0BI2](https://stacks.math.columbia.edu/tag/0BI2) in the Stacks Project.

**`isNagataRing_tfae_isAnalyticallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/AnalyticallyUnramified.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/AnalyticallyUnramified.lean#L236).

> **Stacks 0BI2.** For a Noetherian local ring `R`, the following are equivalent:
>
> 1. `R` is a Nagata ring;
> 2. for every finite `R`-algebra `S` which is a domain and every maximal ideal `𝔪'` of `S`, the
>    localization `S_{𝔪'}` is analytically unramified;
> 3. for every finite local homomorphism `R → S` to a local domain `S`, the ring `S` is analytically
>    unramified.

```lean
theorem isNagataRing_tfae_isAnalyticallyUnramified {R : Type u} [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] :
    [IsNagataRing R,
      ∀ (S : Type (max u v)) [CommRing S] [IsDomain S] [Algebra R S] [Module.Finite R S]
        (m' : Ideal S) [m'.IsMaximal], IsAnalyticallyUnramified (Localization.AtPrime m'),
      ∀ (S : Type (max u w)) [CommRing S] [IsDomain S] [IsLocalRing S] [Algebra R S]
        [Module.Finite R S] [IsLocalHom (algebraMap R S)], IsAnalyticallyUnramified S].TFAE
```

## Tag 0334, a proposition

[Tag 0334](https://stacks.math.columbia.edu/tag/0334) in the Stacks Project.

**`isNagataRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/FiniteType.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/FiniteType.lean#L478). The attribute's comment: “Items (1)-(3) as a `List.TFAE`. Nagata is `IsNagataRing` (032R(2)) and universally Japanese is `IsUniversallyJapaneseRing` (032R(1)); item (2), the condition the source's proof calls universally Nagata, is stated as the quantification over finite-type `R`-algebras rather than through a predicate of its own. See the module docstring.”. References: EGA IV (7.7.2), “a) <=> b)”; EGA IV (10.4.10), “more general”.

> **Nagata's theorem.** For a ring `R` the following are equivalent: `R` is a Nagata ring;
> every finite-type `R`-algebra is a Nagata ring; `R` is universally Japanese and Noetherian.
>
> In particular an algebra of finite type over a Nagata ring is a Nagata ring. Nagata is
> `IsNagataRing` and universally Japanese is `IsUniversallyJapaneseRing`, the two conditions of
> Definition 032R.

```lean
public theorem isNagataRing_tfae {R : Type u} [CommRing R] :
    List.TFAE
      [ IsNagataRing R,
        ∀ (S : Type u) [CommRing S] [Algebra R S] [Algebra.FiniteType R S], IsNagataRing S,
        IsUniversallyJapaneseRing R ∧ IsNoetherianRing R ]
```

## Tag 0335, a proposition

[Tag 0335](https://stacks.math.columbia.edu/tag/0335) in the Stacks Project.

**`isNagataRing_field_and_int_and_isDedekindDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L128). The attribute's comment: “Items (1), (3) and (4) as one conjunction, since they share one proof; each is available separately as `IsNagataRing.of_field`, `Int.isNagataRing` and `IsNagataRing.of_isDedekindDomain_of_charZero`. Item (2) is Tag 032W and item (5) with the closing clause "and in particular universally Japanese" is Tag 0334, both tagged 0335 below. Nagata is `IsNagataRing` (032R(2)) and universally Japanese is `IsUniversallyJapaneseRing` (032R(1)). See the module docstring.”.

> **Fields, `ℤ` and Dedekind domains whose fraction field has characteristic zero are Nagata
> rings**, hence in particular universally Japanese. These are items (1), (3) and (4) of the source,
> in its order; they share the one argument that inspects `R ⧸ 𝔭` for each prime `𝔭`.
>
> The three classes on their own are `IsNagataRing.of_field`, `Int.isNagataRing` and
> `IsNagataRing.of_isDedekindDomain_of_charZero`, which is how they are applied; see the module
> docstring.

```lean
public theorem isNagataRing_field_and_int_and_isDedekindDomain :
    (∀ (K : Type u) [Field K], IsNagataRing K) ∧
    IsNagataRing ℤ ∧
    ∀ (R : Type u) [CommRing R] [IsDedekindDomain R] [CharZero R], IsNagataRing R
```

**`IsNagataRing.of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L138). The attribute's comment: “(1) Fields.”.

> **Stacks 0335 (1).** A field is a Nagata ring, hence in particular universally Japanese: the
> only prime of a field `K` is `0`, and `K ⧸ 0 = K` is N-2 because the integral closure of `K` in a
> finite extension `L` of `K` is `L` itself, a finite `K`-module.

```lean
public theorem IsNagataRing.of_field {K : Type u} [Field K] : IsNagataRing K
```

**`Int.isNagataRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L146). The attribute's comment: “(3) The ring `ℤ`.”. References: EGA IV (7.7.4), “in particular Z”; EGA IV (7.8.3), “(vi), special case”.

> **Stacks 0335 (3).** The ring `ℤ` is a Nagata ring, hence in particular universally Japanese.
> This is the case `R = ℤ` of `IsNagataRing.of_isDedekindDomain_of_charZero`.

```lean
public theorem Int.isNagataRing : IsNagataRing ℤ
```

**`IsNagataRing.of_isDedekindDomain_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L162). The attribute's comment: “(4) Dedekind domains with fraction field of characteristic zero, the latter read as `CharZero R`.”. References: EGA IV (7.7.4), “Dedekind char 0”; EGA IV (7.8.3), “(vi), special case”; EGA IV (7.8.4), “special case”.

> **Stacks 0335 (4).** A Dedekind domain whose fraction field has characteristic zero is a
> Nagata ring, hence in particular universally Japanese. For a prime `𝔭 ≠ 0` the quotient `R ⧸ 𝔭` is
> a field and so is N-2; for `𝔭 = 0` the quotient is `R` itself, which is N-1 because it is
> integrally closed, and N-1 implies N-2 in characteristic zero (Tag 032M).
>
> The condition on the fraction field is stated as `CharZero R`, which for a domain `R` is
> equivalent since `R → Frac R` is injective. It cannot be dropped: a one-dimensional Noetherian
> integrally closed domain in characteristic `p` need not be N-2.

```lean
public theorem IsNagataRing.of_isDedekindDomain_of_charZero {R : Type u} [CommRing R]
    [IsDedekindDomain R] [CharZero R] : IsNagataRing R
```

Declarations registered for the tag:

- [`IsNagataRing.of_isPrecomplete_maximalIdeal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/CompleteLocalRing.lean#L290), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L170) (StacksFrontier): “(2) Noetherian complete local rings, which is Tag 032W.”.
- [`isNagataRing_tfae`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/FiniteType.lean#L478), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Nagata/Examples.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/Examples.lean#L177) (StacksFrontier): “(5) Finite type ring extensions of any of the above, which is the implication (1) ⇒ (2) of Tag 0334, and the closing clause "and in particular universally Japanese", which is its implication (1) ⇒ (3).”.

## Tag 09E2, a lemma

[Tag 09E2](https://stacks.math.columbia.edu/tag/09E2) in the Stacks Project.

**`IsNagataRing.exists_pow_eq_iff_exists_pow_eq_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/PthRoot.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Nagata/PthRoot.lean#L479). The attribute's comment: “Stated as a biconditional, the reverse implication being `map_pow` on the completion map. Noetherian is absorbed into `IsNagataRing` (Definition 032R(2)), primality of `p` into `p ≠ 0` over a domain (`CharP.char_is_prime_or_zero`), and the characteristic of `Frac A` is read off `A`. The completion is `AdicCompletion (maximalIdeal A) A` as in Tag 032X.”.

> **Stacks Tag 09E2.** Let `(A, 𝔪)` be a local domain which is a Nagata ring and has
> characteristic `p ≠ 0`, and let `A^ = lim_n A ⧸ 𝔪ⁿ` be its completion. An element `a : A` has a
> `p`-th root in `A` if and only if it has one in `A^`.
>
> The source also assumes `A` Noetherian, which is the first conjunct of `IsNagataRing A`, and
> assumes `p` prime, which follows from `p ≠ 0` because `A` is a domain. The source's
> characteristic assumption is on the fraction field of `A`; that is the same condition as
> `CharP A p`.

```lean
public theorem IsNagataRing.exists_pow_eq_iff_exists_pow_eq_adicCompletion {A : Type*}
    [CommRing A] [IsLocalRing A] [IsDomain A] (hA : IsNagataRing A) {p : ℕ} [CharP A p]
    (hp : p ≠ 0) (a : A) :
    (∃ b : A, b ^ p = a) ↔
      ∃ α : AdicCompletion (IsLocalRing.maximalIdeal A) A,
        α ^ p = algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A) a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.162, Tag 032E](https://stacks.math.columbia.edu/tag/032E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
