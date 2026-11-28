---
catalog: module
lean: CompPoly.CMlPolynomial.monomialOfNat, CompPoly.CMlPolynomial.eq_monomialOfNat_iff_eq_bitRepr, CompPoly.CMlPolynomial.toMvPolynomial, CompPoly.CMlPolynomial.toMvPolynomial_is_multilinear, CompPoly.CMlPolynomial.coeff_of_toMvPolynomial_eq_coeff_of_CMlPolynomial, CompPoly.CMlPolynomial.toMvPolynomialDeg1, CompPoly.CMlPolynomial.ofMvPolynomialDeg1, CompPoly.CMlPolynomial.equivMvPolynomialDeg1, CompPoly.CMlPolynomial.linearEquivMvPolynomialDeg1, CompPoly.CMlPolynomialEval.toMvPolynomial, CompPoly.CMlPolynomialEval.toMvPolynomialDeg1, CompPoly.CMlPolynomialEval.eqPolynomial, CompPoly.CMlPolynomialEval.eqPolynomialDeg1
statement: formalized
proof: formalized
---

# Equivalence between `CMlPolynomial` and multilinear polynomials in `MvPolynomial`

`CompPoly.Multilinear.Equiv`, in [CompPoly/Multilinear/Equiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean), by Quang Dao, Chung Thai Nguyen.

> This file establishes the mathematical foundations for `CMlPolynomial` by proving:
> 1. Basis properties for the coefficient representation
> 2. Change-of-basis matrices between different representations
> 3. Equivalences with mathlib's `MvPolynomial.restrictDegree`: `equivMvPolynomialDeg1`
> 4. Arithmetic operation compatibilities

> ### Equivalence with Mathlib MvPolynomial
> - Note: maybe we have to add more restrictions on `CMlPolynomial R n` and `CMlPolynomialEval R n`
>   so we can differentiate them?

`CompPoly.CMlPolynomial.monomialOfNat` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L42))

> Converts a natural number to a monomial with 0/1 exponents.
> Uses little‑endian bit encoding: bit 0 is the least significant bit.
> The exponent at variable j is `Nat.getBit j i ∈ {0,1}`.

```lean
noncomputable def monomialOfNat (i : ℕ) : (Fin n) →₀ ℕ
```

`CompPoly.CMlPolynomial.eq_monomialOfNat_iff_eq_bitRepr` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L46))

```lean
theorem eq_monomialOfNat_iff_eq_bitRepr (m : Fin n →₀ ℕ)
    (h_binary : ∀ j : Fin n, m j ≤ 1) (i: Fin (2^n)) :
  monomialOfNat i = m ↔ i = Nat.binaryFinMapToNat m h_binary
```

`CompPoly.CMlPolynomial.toMvPolynomial` (definition, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L87))

> Converts an `CMlPolynomial` to a mathlib multivariate polynomial.
> Sums over all indices `i : Fin (2^n)` with monomial exponents from `monomialOfNat i`
> and coefficients `p[i]`.

```lean
def toMvPolynomial (p : CMlPolynomial R n) : MvPolynomial (Fin n) R
```

`CompPoly.CMlPolynomial.toMvPolynomial_is_multilinear` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L92))

```lean
theorem toMvPolynomial_is_multilinear (p : CMlPolynomial R n) :
    (toMvPolynomial p) ∈ MvPolynomial.restrictDegree (Fin n) R 1
```

`CompPoly.CMlPolynomial.coeff_of_toMvPolynomial_eq_coeff_of_CMlPolynomial` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L123))

```lean
theorem coeff_of_toMvPolynomial_eq_coeff_of_CMlPolynomial (p : CMlPolynomial R n) (m : Fin n →₀ ℕ) :
    (toMvPolynomial p).coeff m =
    if h_binary : (∀ j : Fin n, m j ≤ 1) then
        let i_of_m : ℕ := Nat.binaryFinMapToNat (m := m) (h_binary := h_binary)
        p[i_of_m]
      else
        0
```

`CompPoly.CMlPolynomial.toMvPolynomialDeg1` (definition, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L183))

> Converts an `CMlPolynomial` to a mathlib restricted-degree multivariate polynomial.
> Wraps `toMvPolynomial` with a proof that the result is multilinear (i.e. individual degrees ≤ 1).

```lean
def toMvPolynomialDeg1 (p : CMlPolynomial R n) : MvPolynomial.restrictDegree (Fin n) R 1
```

`CompPoly.CMlPolynomial.ofMvPolynomialDeg1` (definition, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L190))

> Converts a mathlib restricted-degree multivariate polynomial to an `CMlPolynomial`.
> Extracts coefficients using `monomialOfNat` to map indices to monomials.

```lean
def ofMvPolynomialDeg1 (p : MvPolynomial.restrictDegree (Fin n) R 1) : CMlPolynomial R n
```

`CompPoly.CMlPolynomial.equivMvPolynomialDeg1` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L200))

> Equivalence between `CMlPolynomial` and mathlib's restricted-degree multivariate polynomials.
> Establishes that both representations are isomorphic via coefficient extraction/insertion.

```lean
def equivMvPolynomialDeg1 : CMlPolynomial R n ≃ MvPolynomial.restrictDegree (Fin n) R 1
```

`CompPoly.CMlPolynomial.linearEquivMvPolynomialDeg1` (definition, [line 299](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L299))

> Linear equivalence between `CMlPolynomial` and `MvPolynomial.restrictDegree`

```lean
noncomputable def linearEquivMvPolynomialDeg1 :
  CMlPolynomial R n ≃ₗ[R] MvPolynomial.restrictDegree (Fin n) R 1
```

`CompPoly.CMlPolynomialEval.toMvPolynomial` (definition, [line 337](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L337))

> Converts a hypercube-evaluation representation to a Mathlib multivariate polynomial by first
> recovering the monomial-basis representation.

```lean
def toMvPolynomial (p : CMlPolynomialEval R n) : MvPolynomial (Fin n) R
```

`CompPoly.CMlPolynomialEval.toMvPolynomialDeg1` (definition, [line 342](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L342))

> Converts a hypercube-evaluation representation to a Mathlib restricted-degree multivariate
> polynomial.

```lean
def toMvPolynomialDeg1 (p : CMlPolynomialEval R n) :
    MvPolynomial.restrictDegree (Fin n) R 1
```

`CompPoly.CMlPolynomialEval.eqPolynomial` (definition, [line 347](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L347))

> The multilinear equality polynomial centered at `w`.

```lean
def eqPolynomial (w : Vector R n) : MvPolynomial (Fin n) R
```

`CompPoly.CMlPolynomialEval.eqPolynomialDeg1` (definition, [line 351](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean#L351))

> The restricted-degree multilinear equality polynomial centered at `w`.

```lean
def eqPolynomialDeg1 (w : Vector R n) :
    MvPolynomial.restrictDegree (Fin n) R 1
```

## Depends on

- [Multilinear Polynomials](basic.md)

## Sources

- [CompPoly/Multilinear/Equiv.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/Equiv.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multilinear.Equiv.json)
