---
catalog: module
lean: CompPoly.CPolynomial.QuotientCPolynomial.toPoly_resp, CompPoly.CPolynomial.QuotientCPolynomial.toPoly, CompPoly.CPolynomial.QuotientCPolynomial.ofPoly, CompPoly.CPolynomial.QuotientCPolynomial.toPoly_ofPoly, CompPoly.CPolynomial.QuotientCPolynomial.ofPoly_toPoly, CompPoly.CPolynomial.QuotientCPolynomial.ringEquiv
statement: formalized
proof: formalized
---

# QuotientCPolynomial <-> Polynomial Isomorphism

`CompPoly.Univariate.Quotient.Equiv`, in [CompPoly/Univariate/Quotient/Equiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean), by Aristotle (Harmonic), Elias Judin.

> This file establishes the ring equivalence between `QuotientCPolynomial R`
> (the quotient of `CPolynomial.Raw R` by coefficient-wise equivalence) and
> mathlib's `Polynomial R`.
>
> ## Main declarations
>
> * `QuotientCPolynomial.toPoly` - quotient -> Polynomial via `Quotient.lift` on `Raw.toPoly`
> * `QuotientCPolynomial.ofPoly` - Polynomial -> quotient via `Quotient.mk` on `Polynomial.toImpl`
> * `QuotientCPolynomial.toPoly_ofPoly` - round-trip identity `toPoly ∘ ofPoly = id`
> * `QuotientCPolynomial.ofPoly_toPoly` - round-trip identity `ofPoly ∘ toPoly = id`
> * `QuotientCPolynomial.ringEquiv` - the ring equivalence `QuotientCPolynomial R ≃+* Polynomial R`

`CompPoly.CPolynomial.QuotientCPolynomial.toPoly_resp` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L42))

> Well-definedness: equivalent raw polynomials map to the same `Polynomial`.

```lean
theorem toPoly_resp (p q : CPolynomial.Raw R) (h : p ≈ q) :
    p.toPoly = q.toPoly
```

`CompPoly.CPolynomial.QuotientCPolynomial.toPoly` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L52))

> Convert a `QuotientCPolynomial` to a mathlib `Polynomial R`.
>
> Defined by lifting `Raw.toPoly` through the quotient; well-definedness follows from
> the fact that equivalent raw polynomials have equal coefficients.

```lean
noncomputable def toPoly (p : QuotientCPolynomial R) : Polynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.ofPoly` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L59))

> Convert a mathlib `Polynomial R` to a `QuotientCPolynomial R`.
>
> Defined by extracting coefficients via `Polynomial.toImpl` and taking the
> equivalence class.

```lean
def ofPoly (p : Polynomial R) : QuotientCPolynomial R
```

`CompPoly.CPolynomial.QuotientCPolynomial.toPoly_ofPoly` (theorem, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L64))

> Round-trip identity: `toPoly ∘ ofPoly = id`.

```lean
theorem toPoly_ofPoly (p : Polynomial R) : toPoly (ofPoly p) = p
```

`CompPoly.CPolynomial.QuotientCPolynomial.ofPoly_toPoly` (theorem, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L69))

> Round-trip identity: `ofPoly ∘ toPoly = id`.

```lean
theorem ofPoly_toPoly [BEq R] [LawfulBEq R] (q : QuotientCPolynomial R) :
    ofPoly (toPoly q) = q
```

`CompPoly.CPolynomial.QuotientCPolynomial.ringEquiv` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean#L85))

> The ring equivalence between `QuotientCPolynomial R` and `Polynomial R`.
>
> The forward map is `toPoly` (quotient-lift of `Raw.toPoly`); the inverse is
> `ofPoly` (coefficient extraction via `Polynomial.toImpl`).
> Preserves both addition and multiplication.

```lean
noncomputable def ringEquiv [BEq R] [LawfulBEq R] : QuotientCPolynomial R ≃+* Polynomial R
```

## Depends on

- [Quotient of Univariate Polynomials](core.md)
- [Computable Univariate To `Polynomial`](../../part-02/topoly/core.md)

## Proof depends on

- [`toPoly` Equivalence](../../part-02/topoly/equiv.md)

## Sources

- [CompPoly/Univariate/Quotient/Equiv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Quotient/Equiv.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Quotient.Equiv.json)
