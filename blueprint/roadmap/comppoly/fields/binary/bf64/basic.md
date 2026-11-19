---
catalog: module
lean: BF64.basePoly, BF64.toPoly_modulus, BF64.basePoly_natDegree, BF64.basePoly_degree, BF64.basePoly_ne_zero, BF64.basePoly_irreducible, BF64.baseTail, BF64.baseTail_eq, BF64.basePoly_eq, BF64.basePoly_eq_add_tail, BF64.mul_pow_reduce, BF64.BF64Quot, BF64.card_bf64Quot
statement: formalized
proof: formalized
---

# `GF(2^64)` in a polynomial basis

`CompPoly.Fields.Binary.BF64.Basic`, in [CompPoly/Fields/Binary/BF64/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean), by Nicolas Schleicher.

> The field
>
> ```text
> GF(2)[x] / (x^64 + x^4 + x^3 + x + 1)
> ```
>
> as a *flat* quotient by a single irreducible degree-64 polynomial, with an element
> represented by the 64-bit word whose bit `i` is the coefficient of `x^i`. The modulus is
> the standard low-weight pentanomial for this width, and its tail `x^4 + x^3 + x + 1`
> (the constant `0x1B`) is what makes the reduction in `BF64/Reduce.lean` cheap.
>
> This is a different presentation from the binary tower in
> `CompPoly/Fields/Binary/Tower/`, which builds `GF(2^64)` as an iterated quadratic
> extension. The two fields are abstractly isomorphic but use different bases, so their
> bit-level encodings disagree: on the same bit patterns `2 * 3` is `6` here and `1` in the
> tower's rung. Neither is a substitute for the other where the encoding is observable.
>
> ## Main definitions
>
> * `basePoly` — the modulus, as a `Polynomial (ZMod 2)`. Specification only.
> * `BF64Quot` — the field, as `AdjoinRoot basePoly`.
> * `baseTail` — the modulus below its leading term, `x^4 + x^3 + x + 1`.
>
> ## Main statements
>
> * `basePoly_irreducible` — irreducibility, by Rabin's test against the kernel-checked
>   chains in `BF64.BaseCert`.
> * `mul_pow_reduce` — the reduction identity `x^64 ≡ x^4 + x^3 + x + 1`.
> * `card_bf64Quot` — `Fintype.card BF64Quot = 2 ^ 64`.
>
> ## Implementation notes
>
> `basePoly` is `noncomputable` because Mathlib's `Polynomial` is a `Finsupp`, which has no
> executable representation. It exists to state irreducibility and is never evaluated.
> `CompPoly.Extension.ExtensionParams.poly` makes the same choice.
>
> `BF64Quot` is the *quotient* presentation, used for cardinality and as the target of the
> bridge. The computable presentation that arithmetic runs on is `BF64` in
> `CompPoly/Fields/Binary/BF64/Impl.lean`, a nominal type storing a `BitVec 64`;
> the two are related by
> `BF64.toQuot`, which `BF64.toQuot_injective` and `BF64.toQuot_surjective` show is a
> bijection.
>
> ## References
>
> * [Rabin80] Michael O. Rabin. Probabilistic Algorithms in Finite Fields.
>   SIAM Journal on Computing, 9(2):273-280, 1980. https://doi.org/10.1137/0209024

`BF64.basePoly` (definition, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L76))

> The modulus `x^64 + x^4 + x^3 + x + 1` over `GF(2)`. Part of the specification only;
> it is never evaluated.

```lean
noncomputable def basePoly : Polynomial (ZMod 2)
```

`BF64.toPoly_modulus` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L79))

> The certificate's bitmask encoding of the modulus denotes `basePoly`.

```lean
theorem toPoly_modulus : toPoly modulus = basePoly
```

`BF64.basePoly_natDegree` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L84))

> The modulus has degree `64`: the leading `X ^ 64` dominates the tail.

```lean
theorem basePoly_natDegree : basePoly.natDegree = 64
```

`BF64.basePoly_degree` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L88))

> `basePoly_natDegree` in `degree` form, as the division lemmas expect.

```lean
theorem basePoly_degree : basePoly.degree = (64 : ℕ)
```

`BF64.basePoly_ne_zero` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L92))

> The modulus is nonzero, so it can be divided by.

```lean
theorem basePoly_ne_zero : basePoly ≠ 0
```

`BF64.basePoly_irreducible` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L112))

> `x^64 + x^4 + x^3 + x + 1` is irreducible over `GF(2)`, by Rabin's test against the
> kernel-checked bitmask chains in `BF64.BaseCert`.
>
> Degree `64 = 2 ^ 6` has the single prime factor `2`, so the trace condition is joined by one
> coprimality check, at exponent `2^32`. Note that the collapsed
> `irreducible_of_rabin_prime_degree` is *unsound* at this degree — it would accept a
> product of equal-degree factors — so `irreducible_of_rabin_prime_power` is used, which
> is the prime-power collapse and is sound here.
>
> The field size enters as the numeral `2` via `ZMod.card 2`, so each certificate discharges its
> condition directly, with no cardinality rewrite around it; see the section comment in
> `CompPoly/Data/Polynomial/Rabin.lean`.

```lean
theorem basePoly_irreducible : Irreducible basePoly
```

> ## The reduction identity

`BF64.baseTail` (definition, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L127))

> The modulus below its leading term: `x^4 + x^3 + x + 1`, denoted by the reduction
> constant `0x1B`.

```lean
noncomputable def baseTail : Polynomial (ZMod 2)
```

`BF64.baseTail_eq` (theorem, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L130))

> The defining equation of `baseTail`, for rewriting.

```lean
theorem baseTail_eq : baseTail = X ^ 4 + X ^ 3 + X + 1
```

`BF64.basePoly_eq` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L133))

> The defining equation of `basePoly`, for rewriting.

```lean
theorem basePoly_eq : basePoly = X ^ 64 + X ^ 4 + X ^ 3 + X + 1
```

`BF64.basePoly_eq_add_tail` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L136))

> The modulus split into its leading term and its tail.

```lean
theorem basePoly_eq_add_tail : basePoly = X ^ 64 + baseTail
```

`BF64.mul_pow_reduce` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L141))

> `x^64 ≡ x^4 + x^3 + x + 1` modulo the modulus: multiplying by `X ^ 64` may be
> replaced by multiplying by `baseTail`.

```lean
theorem mul_pow_reduce (A : Polynomial (ZMod 2)) :
    (A * X ^ 64) % basePoly = (A * baseTail) % basePoly
```

> ## The base field

`BF64.BF64Quot` (abbreviation, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L154))

> `GF(2^64)` as the quotient `GF(2)[x] / (x^64 + x^4 + x^3 + x + 1)`.
>
> This is the specification-side presentation. Arithmetic runs on the computable `BF64` in
> `CompPoly/Fields/Binary/BF64/Impl.lean`.

```lean
noncomputable abbrev BF64Quot : Type
```

`BF64.card_bf64Quot` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean#L167))

> `BF64Quot` has `2^64` elements.

```lean
theorem card_bf64Quot : Fintype.card BF64Quot = 2 ^ 64
```

## Depends on

- [Rabin certificate data for `p = 2` (BaseCertificate)](basecertificate.md)

## Sources

- [CompPoly/Fields/Binary/BF64/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Binary/BF64/Basic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.BF64.Basic.json)
