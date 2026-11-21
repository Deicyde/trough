---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.OddCZBucket, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_zero_iff, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_square_iff, CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_nonsquare_iff
statement: formalized
proof: formalized
---

# Euler Buckets for Odd Cantor-Zassenhaus Splitting

`CompPoly.Univariate.Roots.LasVegas.OddBucket`, in [CompPoly/Univariate/Roots/LasVegas/OddBucket.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean), by Valerii Huhnin.

> Deterministic three-way classifier for field values seen by one odd-field
> Cantor-Zassenhaus probe: zero values, nonzero values whose Euler power
> `x ^ ((q - 1) / 2)` equals one, and the remaining nonzero values.
>
> This module is shared by the deterministic correctness surface and the
> probability surface, so it must stay free of `PMF` and measure-theory imports.

`CompPoly.CPolynomial.Roots.FiniteField.OddCZBucket` (inductive type, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean#L33))

> Euler bucket of a field value under one odd Cantor-Zassenhaus probe.

```lean
inductive OddCZBucket where
  | zero
  | square
  | nonsquare
  deriving DecidableEq, Repr
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean#L46))

> Classify a value by its Euler power `x ^ ((q - 1) / 2)`.
>
> The `nonsquare` bucket is the residual branch `x ≠ 0 ∧ x ^ ((q - 1) / 2) ≠ 1`;
> identifying it with `x ^ ((q - 1) / 2) = -1` additionally needs `q` to be the
> odd cardinality of the field, which is a probability-side bridge lemma.

```lean
def oddCZBucket {F : Type*} [MonoidWithZero F] [BEq F] [LawfulBEq F]
    (q : Nat) (x : F) : OddCZBucket
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_zero_iff` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean#L56))

> The zero bucket contains exactly the zero value.

```lean
theorem oddCZBucket_eq_zero_iff {F : Type*} [MonoidWithZero F] [BEq F] [LawfulBEq F]
    (q : Nat) (x : F) :
    oddCZBucket q x = OddCZBucket.zero ↔ x = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_square_iff` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean#L64))

> The square bucket contains exactly the nonzero values with Euler power one.

```lean
theorem oddCZBucket_eq_square_iff {F : Type*} [MonoidWithZero F] [BEq F] [LawfulBEq F]
    (q : Nat) (x : F) :
    oddCZBucket q x = OddCZBucket.square ↔ x ≠ 0 ∧ x ^ ((q - 1) / 2) = 1
```

`CompPoly.CPolynomial.Roots.FiniteField.oddCZBucket_eq_nonsquare_iff` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean#L72))

> The nonsquare bucket is the residual branch of the classifier.

```lean
theorem oddCZBucket_eq_nonsquare_iff {F : Type*} [MonoidWithZero F] [BEq F] [LawfulBEq F]
    (q : Nat) (x : F) :
    oddCZBucket q x = OddCZBucket.nonsquare ↔ x ≠ 0 ∧ x ^ ((q - 1) / 2) ≠ 1
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Univariate/Roots/LasVegas/OddBucket.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/LasVegas/OddBucket.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.LasVegas.OddBucket.json)
