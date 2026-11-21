---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_square_iff_isSquare, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_nonsquare_iff_pow_eq_neg_one, CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_zero, CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_square, CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_nonsquare, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_pair_separated_probability_ge_half
statement: formalized
proof: formalized
---

# Euler Bucket Counting for Odd Cantor-Zassenhaus Splitting

`CompPoly.Univariate.Roots.LasVegas.Probability.OddBuckets`, in [CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean), by Valerii Huhnin.

> Finite-field counting facts about the deterministic Euler bucket classifier
> `oddCZBucket`: the Euler criterion bridge, the bucket cardinalities
> `1`, `(q - 1) / 2`, and `(q - 1) / 2`, and the resulting probability that two
> independent uniform field values land in different buckets.
>
> These theorems are field-theoretic, not algorithmic: they do not mention
> `CPolynomial`, gcds, or the Las Vegas loop.

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_square_iff_isSquare` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L65))

> Euler criterion bridge: the square bucket consists of the nonzero squares.

```lean
theorem oddCZBucket_eq_square_iff_isSquare {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q : Nat} (hodd : q % 2 = 1) (hcard : Fintype.card F = q) (x : F) :
    oddCZBucket q x = OddCZBucket.square ↔ x ≠ 0 ∧ IsSquare x
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_nonsquare_iff_pow_eq_neg_one` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L88))

> Euler criterion bridge: over an odd field of cardinality `q`, the residual
> nonsquare bucket is exactly the locus `x ^ ((q - 1) / 2) = -1`.

```lean
theorem oddCZBucket_eq_nonsquare_iff_pow_eq_neg_one {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q : Nat} (hodd : q % 2 = 1) (hcard : Fintype.card F = q) (x : F) :
    oddCZBucket q x = OddCZBucket.nonsquare ↔ x ^ ((q - 1) / 2) = -1
```

`CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_zero` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L111))

> The zero Euler bucket has exactly one element.

```lean
theorem card_oddCZBucket_zero {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F] (q : Nat) :
    (Finset.univ.filter fun x : F ↦ oddCZBucket q x = OddCZBucket.zero).card = 1
```

`CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_square` (theorem, [line 194](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L194))

> The square Euler bucket of an odd field of cardinality `q` has `(q - 1) / 2` elements.

```lean
theorem card_oddCZBucket_square {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q : Nat} (hodd : q % 2 = 1) (hcard : Fintype.card F = q) :
    (Finset.univ.filter fun x : F ↦ oddCZBucket q x = OddCZBucket.square).card =
      (q - 1) / 2
```

`CompPoly.CPolynomial.Roots.FiniteField.card_oddCZBucket_nonsquare` (theorem, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L205))

> The nonsquare Euler bucket of an odd field of cardinality `q` has `(q - 1) / 2` elements.

```lean
theorem card_oddCZBucket_nonsquare {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q : Nat} (hodd : q % 2 = 1) (hcard : Fintype.card F = q) :
    (Finset.univ.filter fun x : F ↦ oddCZBucket q x = OddCZBucket.nonsquare).card =
      (q - 1) / 2
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_pair_separated_probability_ge_half` (theorem, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean#L223))

> Two independent uniform field values land in different Euler buckets with
> probability at least `1 / 2`.
>
> Every Euler bucket has at most `(q - 1) / 2` elements, so for each first value
> at least `q - (q - 1) / 2 = (q + 1) / 2` choices of the second value land in a
> different bucket, giving separation probability at least `(q + 1) / (2 * q)`.

```lean
theorem oddCZBucket_pair_separated_probability_ge_half {F : Type*}
    [Field F] [Fintype F] [BEq F] [LawfulBEq F]
    {q : Nat} (enumeration : UniformFieldEnumeration F q)
    (hodd : q % 2 = 1) (hcard : Fintype.card F = q) :
    (2 : ℝ≥0∞)⁻¹ ≤
      eventProbability
        ((uniformFieldElementPMF enumeration.toFieldEnumeration).bind
          fun x ↦ (uniformFieldElementPMF enumeration.toFieldEnumeration).map
            fun y ↦ (x, y))
        {xy | oddCZBucket q xy.1 ≠ oddCZBucket q xy.2}
```

## Depends on

- [Euler Buckets for Odd Cantor-Zassenhaus Splitting](../oddbucket.md)
- [Uniform Probe Distributions for Las Vegas Root Splitting](uniform.md)

## Sources

- [CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/Probability/OddBuckets.lean)
- [Declaration ledger](../../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.Probability.OddBuckets.json)
