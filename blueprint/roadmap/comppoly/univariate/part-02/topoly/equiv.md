---
catalog: module
lean: CompPoly.CPolynomial.Raw.toPoly_neg, CompPoly.CPolynomial.toPoly_neg, CompPoly.CPolynomial.toPoly_add, CompPoly.CPolynomial.Raw.toPoly_sub, CompPoly.CPolynomial.toPoly_sub, CompPoly.CPolynomial.Raw.toPoly_mul_coeff, CompPoly.CPolynomial.Raw.toPoly_mul, CompPoly.CPolynomial.toPoly_mul_coeffC, CompPoly.CPolynomial.toPoly_mul, CompPoly.CPolynomial.eval₂_C, CompPoly.CPolynomial.Raw.toPoly_C, CompPoly.CPolynomial.Raw.toPoly_one, CompPoly.CPolynomial.toPoly_one, CompPoly.CPolynomial.Raw.toPoly_pow, CompPoly.CPolynomial.Raw.toPoly_zero, CompPoly.CPolynomial.toPoly_zero, CompPoly.CPolynomial.Raw.toPoly_X, CompPoly.CPolynomial.toPoly_pow, CompPoly.CPolynomial.toPoly_sum, CompPoly.CPolynomial.toPoly_prod, CompPoly.CPolynomial.ringEquiv, CompPoly.CPolynomial.ringEquiv_apply
statement: formalized
proof: formalized
---

# `toPoly` Equivalence

`CompPoly.Univariate.ToPoly.Equiv`, in [CompPoly/Univariate/ToPoly/Equiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean), by Quang Dao, Gregor Mitscha-Baude, Derek Sorensen.

> Ring equivalences between computable univariate polynomials and `Polynomial`.

`CompPoly.CPolynomial.Raw.toPoly_neg` (lemma, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L32))

```lean
lemma Raw.toPoly_neg {R : Type*} [Ring R] [BEq R] [LawfulBEq R] (p : CPolynomial.Raw R) :
    (-p).toPoly = -p.toPoly
```

`CompPoly.CPolynomial.toPoly_neg` (lemma, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L40))

```lean
lemma toPoly_neg {R : Type*} [Ring R] [BEq R] [LawfulBEq R] (p : CPolynomial R) :
    (-p).toPoly = -p.toPoly
```

`CompPoly.CPolynomial.toPoly_add` (lemma, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L45))

```lean
lemma toPoly_add [LawfulBEq R] (p q : CPolynomial R) :
    (p + q).toPoly = p.toPoly + q.toPoly
```

`CompPoly.CPolynomial.Raw.toPoly_sub` (lemma, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L50))

```lean
lemma Raw.toPoly_sub {R : Type*} [Ring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial.Raw R) :
    (p - q).toPoly = p.toPoly - q.toPoly
```

`CompPoly.CPolynomial.toPoly_sub` (lemma, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L57))

```lean
lemma toPoly_sub {R : Type*} [Ring R] [BEq R] [LawfulBEq R] (p q : CPolynomial R) :
    (p - q).toPoly = p.toPoly - q.toPoly
```

`CompPoly.CPolynomial.Raw.toPoly_mul_coeff` (lemma, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L63))

```lean
lemma Raw.toPoly_mul_coeff [LawfulBEq R] (p q : CPolynomial.Raw R) (i : ℕ) :
    (p * q).toPoly.coeff i = (p.toPoly * q.toPoly).coeff i
```

`CompPoly.CPolynomial.Raw.toPoly_mul` (lemma, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L82))

```lean
lemma Raw.toPoly_mul [LawfulBEq R] (p q : CPolynomial.Raw R) :
    (p * q).toPoly = p.toPoly * q.toPoly
```

`CompPoly.CPolynomial.toPoly_mul_coeffC` (lemma, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L88))

```lean
lemma toPoly_mul_coeffC [LawfulBEq R] (p q : CPolynomial R) (i : ℕ) :
    (p.val * q.val).toPoly.coeff i = (p.val.toPoly * q.val.toPoly).coeff i
```

`CompPoly.CPolynomial.toPoly_mul` (lemma, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L93))

```lean
lemma toPoly_mul [LawfulBEq R] (p q : CPolynomial R) :
    (p * q).toPoly = p.toPoly * q.toPoly
```

`CompPoly.CPolynomial.eval₂_C` (lemma, [line 98](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L98))

```lean
lemma eval₂_C {R : Type*} [Semiring R] {S : Type*} [Semiring S]
    (f : R →+* S) (x : S) (r : R) :
    (Raw.C r).eval₂ f x = f r
```

`CompPoly.CPolynomial.Raw.toPoly_C` (lemma, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L106))

```lean
lemma Raw.toPoly_C {R : Type*} [Semiring R] (r : R) :
    (Raw.C r).toPoly = Polynomial.C r
```

`CompPoly.CPolynomial.Raw.toPoly_one` (lemma, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L112))

```lean
lemma Raw.toPoly_one {R : Type*} [Semiring R] :
    (1 : CPolynomial.Raw R).toPoly = 1
```

`CompPoly.CPolynomial.toPoly_one` (lemma, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L119))

```lean
lemma toPoly_one [LawfulBEq R] [Nontrivial R] :
    (1 : CPolynomial R).toPoly = 1
```

`CompPoly.CPolynomial.Raw.toPoly_pow` (lemma, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L124))

```lean
lemma Raw.toPoly_pow [LawfulBEq R] (p : CPolynomial.Raw R) :
    ∀ n : ℕ, (p ^ n).toPoly = p.toPoly ^ n
```

`CompPoly.CPolynomial.Raw.toPoly_zero` (lemma, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L133))

```lean
lemma Raw.toPoly_zero {R : Type*} [Semiring R] : (0 : CPolynomial.Raw R).toPoly = 0
```

`CompPoly.CPolynomial.toPoly_zero` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L138))

```lean
lemma toPoly_zero {R : Type*} [Semiring R] : (0 : CPolynomial R).toPoly = 0
```

`CompPoly.CPolynomial.Raw.toPoly_X` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L142))

```lean
lemma Raw.toPoly_X {R : Type*} [Semiring R] :
    (Raw.X : CPolynomial.Raw R).toPoly = Polynomial.X
```

`CompPoly.CPolynomial.toPoly_pow` (lemma, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L148))

```lean
lemma toPoly_pow [Nontrivial R] [LawfulBEq R] (p : CPolynomial R) (n : ℕ) :
    (p ^ n).toPoly = p.toPoly ^ n
```

`CompPoly.CPolynomial.toPoly_sum` (lemma, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L155))

```lean
lemma toPoly_sum.{u} {R : Type*} [Semiring R] [BEq R] [LawfulBEq R] {ι : Type u}
    [DecidableEq ι]
    {s : Finset ι} {f : ι → CPolynomial R} :
      (∑ j ∈ s, f j).toPoly = ∑ j ∈ s, ((f j).toPoly)
```

`CompPoly.CPolynomial.toPoly_prod` (lemma, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L166))

```lean
lemma toPoly_prod.{u} {R : Type*} [CommSemiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    {ι : Type u} [DecidableEq ι]
    {s : Finset ι} {f : ι → CPolynomial R} :
      (∏ j ∈ s, f j).toPoly = ∏ j ∈ s, ((f j).toPoly)
```

`CompPoly.CPolynomial.ringEquiv` (definition, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L176))

```lean
noncomputable def ringEquiv [LawfulBEq R] [Nontrivial R] :
  CPolynomial R ≃+* Polynomial R
```

`CompPoly.CPolynomial.ringEquiv_apply` (theorem, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean#L191))

> The forward map of `ringEquiv` is `toPoly`.

```lean
theorem ringEquiv_apply [LawfulBEq R] [Nontrivial R] (p : CPolynomial R) :
    ringEquiv p = p.toPoly
```

## Depends on

- [Computable Univariate To `Polynomial`](core.md)

## Sources

- [CompPoly/Univariate/ToPoly/Equiv.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/ToPoly/Equiv.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ToPoly.Equiv.json)
