---
catalog: module
lean: CompPoly.CPolynomial.lcoeff, CompPoly.CPolynomial.lcoeff_apply, CompPoly.CPolynomial.degreeLE, CompPoly.CPolynomial.degreeLT, CompPoly.CPolynomial.mem_degreeLE, CompPoly.CPolynomial.mem_degreeLT, CompPoly.CPolynomial.mem_degreeLT_iff_size_le, CompPoly.CPolynomial.zero_mem_degreeLT, CompPoly.CPolynomial.add_mem_degreeLT, CompPoly.CPolynomial.nsmul_mem_degreeLT, CompPoly.CPolynomial.smul_mem_degreeLT, CompPoly.CPolynomial.degreeLTCoeffs, CompPoly.CPolynomial.degreeLTCoeffs_apply
statement: formalized
proof: formalized
---

# Linear Algebra API for Computable Univariate Polynomials

`CompPoly.Univariate.Linear`, in [CompPoly/Univariate/Linear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean), by Desmond Coles, Derek Sorensen.

> This file contains linear maps and instance-stable bounded-degree predicates for `CPolynomial`.

`CompPoly.CPolynomial.lcoeff` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L30))

> This is an R-linear function that returns the coefficient of X^n.

```lean
def lcoeff (n : ℕ) : (CPolynomial R) →ₗ[R] R
```

`CompPoly.CPolynomial.lcoeff_apply` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L37))

> Applying `lcoeff n` returns the coefficient of degree `n`.

```lean
theorem lcoeff_apply (n : ℕ) (p : CPolynomial R) : lcoeff n p = coeff p n
```

`CompPoly.CPolynomial.degreeLE` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L47))

> The set of `CPolynomial R` consisting of polynomials of degree ≤ `n`.

```lean
def degreeLE (n : WithBot ℕ) : Set (CPolynomial R)
```

`CompPoly.CPolynomial.degreeLT` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L51))

> The set of `CPolynomial R` consisting of polynomials of degree < `n`.

```lean
def degreeLT (n : ℕ) : Set (CPolynomial R)
```

`CompPoly.CPolynomial.mem_degreeLE` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L55))

> Membership in `degreeLE` is the corresponding degree bound.

```lean
theorem mem_degreeLE {n : WithBot ℕ} {p : CPolynomial R} :
    p ∈ degreeLE (R := R) n ↔ p.degree ≤ n
```

`CompPoly.CPolynomial.mem_degreeLT` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L60))

> Membership in `degreeLT` is the corresponding strict degree bound.

```lean
theorem mem_degreeLT {n : ℕ} {p : CPolynomial R} :
    p ∈ degreeLT (R := R) n ↔ p.degree < n
```

`CompPoly.CPolynomial.mem_degreeLT_iff_size_le` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L65))

> `degreeLT n` is exactly the bounded-size carrier storing at most `n` coefficients.

```lean
theorem mem_degreeLT_iff_size_le {n : ℕ} {p : CPolynomial R} :
    p ∈ degreeLT (R := R) n ↔ p.val.size ≤ n
```

`CompPoly.CPolynomial.zero_mem_degreeLT` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L74))

> The zero polynomial has bounded degree for every cutoff.

```lean
theorem zero_mem_degreeLT (n : ℕ) : (0 : CPolynomial R) ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.add_mem_degreeLT` (theorem, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L85))

> `degreeLT n` is closed under addition.

```lean
theorem add_mem_degreeLT {n : ℕ} {p q : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) (hq : q ∈ degreeLT (R := R) n) :
    p + q ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.nsmul_mem_degreeLT` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L96))

> `degreeLT n` is closed under additive scalar multiplication.

```lean
theorem nsmul_mem_degreeLT {n m : ℕ} {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    m • p ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.smul_mem_degreeLT` (theorem, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L107))

> `degreeLT n` is closed under semiring scalar multiplication.

```lean
theorem smul_mem_degreeLT {n : ℕ} (r : R) {p : CPolynomial R}
    (hp : p ∈ degreeLT (R := R) n) :
    r • p ∈ degreeLT (R := R) n
```

`CompPoly.CPolynomial.degreeLTCoeffs` (definition, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L189))

> The first `n` coefficients on `degreeLT n` form a computable linear map to `Fin n → R`.

```lean
def degreeLTCoeffs (n : ℕ) : ↥(degreeLT (R := R) n) →ₗ[R] (Fin n → R)
```

`CompPoly.CPolynomial.degreeLTCoeffs_apply` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean#L202))

> Applying `degreeLTCoeffs` returns the corresponding bounded coefficient.

```lean
theorem degreeLTCoeffs_apply (n : ℕ) (p : ↥(degreeLT (R := R) n)) (i : Fin n) :
    degreeLTCoeffs n p i = coeff p.1 i
```

## Depends on

- [Computable Univariate Polynomials](basic.md)

## Sources

- [CompPoly/Univariate/Linear.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Linear.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Linear.json)
