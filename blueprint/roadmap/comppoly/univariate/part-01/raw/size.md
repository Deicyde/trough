---
catalog: module
lean: CompPoly.CPolynomial.Raw.size_C, CompPoly.CPolynomial.Raw.size_smul, CompPoly.CPolynomial.Raw.size_mulPowX, CompPoly.CPolynomial.Raw.size_addRaw, CompPoly.CPolynomial.Raw.add_size, CompPoly.CPolynomial.Raw.size_mulRaw, CompPoly.CPolynomial.Raw.size_mulRaw_le
statement: formalized
proof: formalized
---

# Sizes of raw polynomial operations

`CompPoly.Univariate.Raw.Size`, in [CompPoly/Univariate/Raw/Size.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean), by Alexander Hicks.

> These bounds concern stored coefficient arrays, including trailing zero coefficients.
> Raw multiplication retains the padding of its shifted rows even when the right input is empty.
> The scalar, shift and product facts were ported from ArkLib's raw-size adapter under Apache 2.0;
> its original copyright attribution is retained.

`CompPoly.CPolynomial.Raw.size_C` (theorem, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L26))

> A raw constant stores one coefficient, including when that coefficient is zero.

```lean
theorem size_C {R : Type*} (x : R) : (C x).size = 1
```

`CompPoly.CPolynomial.Raw.size_smul` (theorem, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L31))

> Scalar multiplication preserves the stored coefficient count.

```lean
theorem size_smul {R : Type*} [Mul R] (x : R) (p : Raw R) :
    (smul x p).size = p.size
```

`CompPoly.CPolynomial.Raw.size_mulPowX` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L37))

> Multiplication by `X^i` retains all of the prepended zero coefficients.

```lean
theorem size_mulPowX {R : Type*} [Zero R] (i : Nat) (p : Raw R) :
    (mulPowX i p).size = i + p.size
```

`CompPoly.CPolynomial.Raw.size_addRaw` (theorem, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L43))

> Padded raw addition stores the larger input size.

```lean
theorem size_addRaw {Q : Type*} [Zero Q] [Add Q] {p q : Raw Q} :
    (addRaw p q).size = max p.size q.size
```

`CompPoly.CPolynomial.Raw.add_size` (alias, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L50))

> Compatibility name for the public theorem previously provided by `Raw.Proofs`.

```lean
alias add_size
```

`CompPoly.CPolynomial.Raw.size_mulRaw` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L53))

> Raw multiplication retains every shifted row, including padding from an empty right array.

```lean
theorem size_mulRaw {R : Type*} [Semiring R] (p q : Raw R) :
    (mulRaw p q).size = if p.size = 0 then 0 else q.size + p.size - 1
```

`CompPoly.CPolynomial.Raw.size_mulRaw_le` (theorem, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean#L74))

> The raw product's stored size is at most the sum of the input sizes minus one.

```lean
theorem size_mulRaw_le {R : Type*} [Semiring R] (p q : Raw R) :
    (mulRaw p q).size ≤ p.size + q.size - 1
```

## Depends on

- [Raw Univariate Polynomial Operations](ops.md)

## Sources

- [CompPoly/Univariate/Raw/Size.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Raw/Size.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Size.json)
