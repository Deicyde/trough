---
catalog: module
lean: Nat.exists_primeFactor_dvd_div_of_dvd, Polynomial.irreducible_of_rabin, Polynomial.rabin_of_irreducible, Polynomial.irreducible_iff_rabin
statement: formalized
proof: formalized
---

# Rabin's irreducibility test

`CompPoly.Data.Polynomial.Rabin`, in [CompPoly/Data/Polynomial/Rabin.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean), by Derek Sorensen.

> A polynomial `f` of degree `d` over a finite field `F` with `q = |F|` elements is irreducible
> exactly when
>
> * `f ∣ X^(q^d) - X`, and
> * `f` is coprime to `X^(q^(d/ℓ)) - X` for every prime `ℓ ∣ d`.
>
> The first condition says every irreducible factor of `f` has degree dividing `d`; the second
> rules out all *proper* divisors of `d` as factor degrees, forcing `f` itself to be irreducible.
> Both rest on the fundamental correspondence
> `Polynomial.irreducible_dvd_X_pow_sub_X_iff_natDegree_dvd` from
> `CompPoly/Data/Polynomial/Frobenius.lean`.
>
> This generalizes `irreducible_of_rabin_128_passed_over_GF2`
> (`CompPoly/Fields/Binary/BF128Ghash/Basic.lean`), which is the `d = 128`, `F = GF(2)`
> specialization, to arbitrary degree over any finite field.
>
> ## Main statements
>
> * `Polynomial.irreducible_of_rabin`: the two conditions imply irreducibility.
> * `Polynomial.rabin_of_irreducible`: the converse, so the test is exact.
> * `Polynomial.irreducible_iff_rabin`: the resulting characterization.
>
> All three take the field size as a numeral `q` with `hcard : Fintype.card F = q`; see "The shape
> of these statements" below for why, and pass `rfl` if you have no numeral.
>
> ## References
>
> * [Rabin80] Michael O. Rabin, *Probabilistic Algorithms in Finite Fields*,
>   SIAM Journal on Computing 9(2), 1980.

`Nat.exists_primeFactor_dvd_div_of_dvd` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean#L57))

> If `m` is a proper divisor of a nonzero `d`, then `m` divides `d / ℓ` for some prime factor `ℓ`
> of `d`.
>
> This is the arithmetic core of Rabin's test: it is why checking the prime-index quotients
> `d / ℓ` suffices to rule out *every* proper divisor of `d`.

```lean
theorem exists_primeFactor_dvd_div_of_dvd {m d : ℕ} (hd : d ≠ 0) (hmd : m ∣ d) (hne : m ≠ d) :
    ∃ ℓ ∈ d.primeFactors, m ∣ d / ℓ
```

> ### The shape of these statements
>
> Each test below takes the field size as a numeral `q` together with `hcard : Fintype.card F = q`,
> rather than reading it off as `Fintype.card F`, and substitutes it away internally. Both kinds of
> caller are served: a concrete field supplies `hcard` as `ZMod.card _` (or its own cardinality
> lemma) and states its conditions at the numeral its certificates were generated for; a caller with
> no numeral in hand passes `rfl` and gets the `Fintype.card F` statement back verbatim.
>
> The alternative — stating the conditions at `Fintype.card F` and having concrete callers cast each
> one with `rw [hcard]` — is what this shape exists to rule out. Such a cast leaves an `Eq.mpr`
> transport around a certificate argument whose type carries a huge exponent (`X ^ (q ^ d)`), and a
> kernel replay from an empty environment need not follow the same normalization path the elaborator
> took: one such transport has been observed to send the kernel into
> `Polynomial.pow → npowRec → Nat.rec`, unfolding the power one exponent step at a time until the
> deep-recursion guard fired. Since there is only one form of each statement, that cast has no
> occasion to appear. `docs/wiki/field-extensions.md` records the history, and
> `CompPoly/Data/Polynomial/RabinCertificate.lean` packages these tests at concrete degrees.

`Polynomial.irreducible_of_rabin` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean#L113))

> **Rabin's irreducibility test (soundness).**
>
> If a degree-`d` polynomial `f` over a finite field with `q` elements divides `X^(q^d) - X` and is
> coprime to `X^(q^(d/ℓ)) - X` for every prime `ℓ ∣ d`, then `f` is irreducible.

```lean
theorem irreducible_of_rabin {f : F[X]} {d q : ℕ} (hcard : Fintype.card F = q)
    (h_deg : f.natDegree = d) (h_pos : 0 < d)
    (h_trace : f ∣ X ^ (q ^ d) - X)
    (h_coprime : ∀ ℓ ∈ d.primeFactors, IsCoprime f (X ^ (q ^ (d / ℓ)) - X)) :
    Irreducible f
```

`Polynomial.rabin_of_irreducible` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean#L141))

> **Rabin's irreducibility test (completeness).**
>
> An irreducible polynomial of degree `d` satisfies both Rabin conditions.

```lean
theorem rabin_of_irreducible {f : F[X]} {d q : ℕ} (hcard : Fintype.card F = q)
    (h_deg : f.natDegree = d) (h_pos : 0 < d) (h_irr : Irreducible f) :
    f ∣ X ^ (q ^ d) - X ∧
      ∀ ℓ ∈ d.primeFactors, IsCoprime f (X ^ (q ^ (d / ℓ)) - X)
```

`Polynomial.irreducible_iff_rabin` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean#L162))

> **Rabin's irreducibility test.** For a polynomial of positive degree `d` over a finite field
> with `q` elements, irreducibility is equivalent to the two Rabin conditions.

```lean
theorem irreducible_iff_rabin {f : F[X]} {d q : ℕ} (hcard : Fintype.card F = q)
    (h_deg : f.natDegree = d) (h_pos : 0 < d) :
    Irreducible f ↔
      (f ∣ X ^ (q ^ d) - X ∧
        ∀ ℓ ∈ d.primeFactors, IsCoprime f (X ^ (q ^ (d / ℓ)) - X))
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Frobenius polynomial identities](frobenius.md)
- [Small-factor extraction for reducible polynomials](../../tomathlib/polynomial/irreducible.md)

## Sources

- [CompPoly/Data/Polynomial/Rabin.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Polynomial/Rabin.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Polynomial.Rabin.json)
