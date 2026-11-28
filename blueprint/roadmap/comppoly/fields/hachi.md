---
catalog: module
lean: Hachi.fieldSize, Hachi.Field, Hachi.is_prime, Hachi.pBits, Hachi.twoAdicity, Hachi.fieldSize_sub_one_factorization
statement: formalized
proof: formalized
---

# Hachi prime field `2^32 - 99`

`CompPoly.Fields.Hachi`, in [CompPoly/Fields/Hachi.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean), by Derek Sorensen.

> A 32-bit prime field. The name is provisional.
>
> `p - 1 = 2^2 · 3 · 13 · 67 · 163 · 2521`, so:
>
> * `p ≡ 1 mod 4`, which is what makes `X^4 - W` irreducible for any non-square `W`
>   (see `CompPoly/Fields/Hachi/Ext4.lean`);
> * the two-adicity is only **2**, so unlike BabyBear and KoalaBear this field admits no large
>   smooth multiplicative subgroup and therefore **no radix-2 NTT domain**. That is irrelevant for
>   degree-4 extension arithmetic, which is schoolbook, but it does rule out the
>   `CompPoly/Univariate/NTT*` fast-multiplication paths for polynomials over this field.
>
> ## Implementation notes
>
> There is deliberately no `FastField` (Montgomery) implementation for this modulus.
> `Montgomery/Native32Field.lean` requires `modulus < 2 ^ 31`, because radix-`2^32` Montgomery
> reduction needs `x + m * p < 2 ^ 64`; at `p ≈ 2 ^ 32` that overflows `UInt64`. A 64-bit-radix
> (or two-limb) Montgomery layer would be needed, and is orthogonal to the extension framework —
> `CompPoly/Fields/Extension/` is generic over the base-field carrier and would pick it up
> unchanged.

`Hachi.fieldSize` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L42))

> The Hachi field modulus, `2^32 - 99`.

```lean
def fieldSize : Nat
```

`Hachi.Field` (abbreviation, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L45))

> The Hachi prime field as a `ZMod`.

```lean
abbrev Field
```

`Hachi.is_prime` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L48))

> The Hachi modulus is prime.

```lean
theorem is_prime : Nat.Prime fieldSize
```

`Hachi.pBits` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L60))

> Bit width of the Hachi modulus.

```lean
def pBits : Nat
```

`Hachi.twoAdicity` (definition, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L65))

> The two-adicity of `fieldSize - 1`, i.e. `2` — deliberately small; see the module
> docstring.

```lean
def twoAdicity : Nat
```

`Hachi.fieldSize_sub_one_factorization` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean#L67))

```lean
theorem fieldSize_sub_one_factorization : fieldSize - 1 = 2 ^ twoAdicity * 1073741799
```

## Depends on

- [Non-binary fields and polynomial utilities](basic.md)

## Proof depends on

- [The Lucas test for primes](prattcertificate.md)

## Sources

- [CompPoly/Fields/Hachi.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Fields.Hachi.json)
