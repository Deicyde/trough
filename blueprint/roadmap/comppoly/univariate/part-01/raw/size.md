---
catalog: module
lean: CompPoly.CPolynomial.Raw.size_C, CompPoly.CPolynomial.Raw.add_size, CompPoly.CPolynomial.Raw.size_mulRaw_le
statement: formalized
proof: formalized
---

# Sizes of raw polynomial operations

`CompPoly.Univariate.Raw.Size`, in [CompPoly/Univariate/Raw/Size.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Size.lean), by Alexander Hicks.

> These bounds concern stored coefficient arrays, including trailing zero coefficients.
> Raw multiplication retains the padding of its shifted rows even when the right input is empty.
> `CompPoly.Univariate.Raw.Ops` states the size equations of `smul`, `mulPowX`, `addRaw` and
> `mulRaw`, next to the operations. This module imports it publicly. The product bound
> `size_mulRaw_le` was ported from ArkLib's raw-size adapter under Apache 2.0. The file header keeps
> its original copyright attribution.

`CompPoly.CPolynomial.Raw.size_C` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Size.lean#L28))

> A raw constant stores one coefficient, including when that coefficient is zero.

```lean
theorem size_C {R : Type*} (x : R) : (C x).size = 1
```

`CompPoly.CPolynomial.Raw.add_size` (alias, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Size.lean#L33))

> Compatibility name for the public theorem previously provided by `Raw.Proofs`.

```lean
alias add_size
```

`CompPoly.CPolynomial.Raw.size_mulRaw_le` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Size.lean#L36))

> The raw product's stored size is at most the sum of the input sizes minus one.

```lean
theorem size_mulRaw_le {R : Type*} [Semiring R] (p q : Raw R) :
    (mulRaw p q).size ≤ p.size + q.size - 1
```

## Depends on

- [Raw Univariate Polynomial Operations](ops.md)

## Sources

- [CompPoly/Univariate/Raw/Size.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Size.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Size.json)
