---
catalog: module
lean: CompPoly.Bytes.equivFin, CompPoly.Bytes.instFintypeVectorUInt8, CompPoly.Bytes.card_vector_uint8, CompPoly.CanonicalNat.ofNat_eq_iff, CompPoly.CanonicalNat.fiberEquiv, CompPoly.CanonicalNat.instFintypeFiber, CompPoly.CanonicalNat.card_fiber_ofBytesModOrder, CompPoly.CanonicalNat.abs_card_fiber_div_sub_le, CompPoly.CanonicalNat.tv_ofBytesModOrder_le
statement: formalized
proof: formalized
---

# Bias of the reduce-modulo-order decoder

`CompPoly.Data.Bytes.Bias`, in [CompPoly/Data/Bytes/Bias.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean), by Derek Sorensen.

> A challenge squeezed from a byte sponge is `CanonicalNat.ofBytesModOrder`: `n` bytes read as a
> little-endian integer and reduced modulo `bound`. Reducing the `256 ^ n` strings modulo `bound`
> hits every residue `256 ^ n / bound` or `256 ^ n / bound + 1` times, so the induced distribution
> on `F` is within `bound / 256 ^ n` of uniform in total variation. Sixteen bytes beyond the
> field's width make that below `2 ^ -128`, which is the margin spongefish uses.
>
> * `Bytes.equivFin`: `n`-byte strings are the naturals below `256 ^ n`.
> * `CanonicalNat.card_fiber_ofBytesModOrder`: the exact fiber count, from Mathlib's
>   `Nat.count_modEq_card`.
> * `CanonicalNat.tv_ofBytesModOrder_le`: the total-variation bound, over `ℚ`.
>
> Everything here is counting; no probability theory is imported. ArkLib's
> `Deserialize.CloseToUniform` instance for `ZMod p` is derived from the last theorem by casting
> into its `PMF` distance.

`CompPoly.Bytes.equivFin` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L39))

> Little-endian byte strings of length `n` are the naturals below `256 ^ n`.

```lean
def equivFin (n : ℕ) : Vector UInt8 n ≃ Fin (256 ^ n)
```

`CompPoly.Bytes.instFintypeVectorUInt8` (instance, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L46))

> `n`-byte strings are finite, through `equivFin`.

```lean
instance instFintypeVectorUInt8 (n : ℕ) : Fintype (Vector UInt8 n)
```

`CompPoly.Bytes.card_vector_uint8` (theorem, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L49))

```lean
theorem card_vector_uint8 (n : ℕ) : Fintype.card (Vector UInt8 n) = 256 ^ n
```

`CompPoly.CanonicalNat.ofNat_eq_iff` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L60))

```lean
theorem ofNat_eq_iff {m : ℕ} {x : F} : ofNat m = x ↔ m % bound F = toNat x
```

`CompPoly.CanonicalNat.fiberEquiv` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L69))

> The `n`-byte strings decoding to `x` modulo the order, as the naturals below `256 ^ n`
> congruent to `toNat x`.

```lean
def fiberEquiv (n : ℕ) (x : F) :
    {v : Vector UInt8 n // ofBytesModOrder v = x}
      ≃ {k : ℕ // k < 256 ^ n ∧ k ≡ toNat x [MOD bound F]}
```

`CompPoly.CanonicalNat.instFintypeFiber` (instance, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L88))

```lean
instance instFintypeFiber [DecidableEq F] (n : ℕ) (x : F) :
    Fintype {v : Vector UInt8 n // ofBytesModOrder v = x}
```

`CompPoly.CanonicalNat.card_fiber_ofBytesModOrder` (theorem, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L96))

> Exactly how many `n`-byte strings decode to `x` modulo the order: the quotient
> `256 ^ n / bound`, plus one for the residues below the remainder.

```lean
theorem card_fiber_ofBytesModOrder (n : ℕ) (x : F) :
    Fintype.card {v : Vector UInt8 n // ofBytesModOrder v = x}
      = 256 ^ n / bound F + if toNat x < 256 ^ n % bound F then 1 else 0
```

`CompPoly.CanonicalNat.abs_card_fiber_div_sub_le` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L105))

> Every fiber is within one of the ideal `256 ^ n / bound`, so each residue's probability is
> within `1 / 256 ^ n` of uniform.

```lean
theorem abs_card_fiber_div_sub_le (n : ℕ) (x : F) :
    |((Fintype.card {v : Vector UInt8 n // ofBytesModOrder v = x} : ℚ) / 256 ^ n)
      - 1 / bound F| ≤ 1 / 256 ^ n
```

`CompPoly.CanonicalNat.tv_ofBytesModOrder_le` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean#L139))

> The total-variation distance of `ofBytesModOrder` on `n` bytes from the uniform
> distribution on `F` is at most `bound / 256 ^ n`: sixteen bytes beyond the width give
> `2 ^ -128`. Stated over `ℚ`; ArkLib derives its `PMF` form from it.

```lean
theorem tv_ofBytesModOrder_le [Fintype F] (n : ℕ) :
    ∑ x : F, |((Fintype.card {v : Vector UInt8 n // ofBytesModOrder v = x} : ℚ) / 256 ^ n)
      - 1 / bound F| ≤ bound F / 256 ^ n
```

## Depends on

- [Byte codecs from canonical naturals](canonicalnat.md)

## Sources

- [CompPoly/Data/Bytes/Bias.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/Bytes/Bias.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Bytes.Bias.json)
