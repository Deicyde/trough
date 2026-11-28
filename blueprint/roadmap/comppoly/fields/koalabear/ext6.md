---
catalog: module
lean: KoalaBear.ext6Params, KoalaBear.ext6Params_d, KoalaBear.ext6Params_q, KoalaBear.ext6Params_poly, KoalaBear.Ext6, KoalaBear.ext6Gen, KoalaBear.ext6Gen_eq_gen, KoalaBear.toQuot_ext6Gen, KoalaBear.aeval_ext6Gen, KoalaBear.ext6Gen_pow_six, KoalaBear.ext6Gen_cubed_is_primitive_cube_root, KoalaBear.ext6Gen_pow_nine, KoalaBear.card_ext6
statement: formalized
proof: formalized
---

# The degree-6 extension of KoalaBear

`CompPoly.Fields.KoalaBear.Ext6`, in [CompPoly/Fields/KoalaBear/Ext6.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean), by Derek Sorensen.

> `KoalaBear[X] / (X^6 + X^3 + 1)`, a field of `p^6 ≈ 2^186` elements. The modulus is `Φ₉`, the
> ninth cyclotomic polynomial, so the adjoined root `θ` is a primitive 9th root of unity.
>
> As at degree 5, the modulus is necessarily *not* a binomial, and for a stronger reason: since
> `p - 1 = 2^24 · 127` we have `3 ∤ p - 1`, so `x ↦ x^3` is a bijection on KoalaBear and every `W`
> is a cube `V^3`, whence `X^6 - W = (X^2 - V)(X^4 + V X^2 + V^2)` factors for *every* `W`. So no
> degree-6 binomial extension of KoalaBear exists at all.
>
> `Φ₉` is chosen among the irreducible sextics because every entry of its reduction table
> `X^6 … X^10 mod f` is `±1` — reduction costs no base-field multiplications — and the same holds
> for its Frobenius matrix, since `p ≡ 2 mod 9` makes Frobenius `θ ↦ θ^2`. It also carries the
> `2`-then-`3` tower implicitly: `θ^3` is a primitive cube root of unity generating the `F_p²`
> subfield, because `Y^2 + Y + 1` is irreducible over KoalaBear.
>
> Irreducibility of `X^6 + X^3 + 1` is `KoalaBear.sexticPoly_irreducible`
> (`CompPoly/Fields/KoalaBear/Ext6/SexticIrreducible.lean`), proved by Rabin's test at a degree with
> two prime factors, with kernel-checked certificates for all three conditions. Supporting files
> live under `KoalaBear/Ext6/`.
>
> This sits alongside `KoalaBear.Ext5` rather than replacing it; the two are independent instances
> of the same framework.
>
> ## Main definitions
>
> * `KoalaBear.ext6Params`: the `ExtensionParams` for `X^6 + X^3 + 1`.
> * `KoalaBear.Ext6`: the extension field itself.

`KoalaBear.ext6Params` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L50))

> The parameters of the sextic extension `KoalaBear[X] / (X^6 + X^3 + 1)`: the lower
> coefficients of the monic modulus are `(1, 0, 0, 1, 0, 0)`.

```lean
def ext6Params : ExtensionParams Field
```

`KoalaBear.ext6Params_d` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L59))

```lean
theorem ext6Params_d : ext6Params.d = 6
```

`KoalaBear.ext6Params_q` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L60))

```lean
theorem ext6Params_q : ext6Params.q = fieldSize
```

`KoalaBear.ext6Params_poly` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L63))

> The defining polynomial of the parameters is the sextic `X^6 + X^3 + 1`.

```lean
theorem ext6Params_poly : ext6Params.poly = sexticPoly
```

`KoalaBear.Ext6` (abbreviation, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L88))

> The degree-6 extension field of KoalaBear.

```lean
abbrev Ext6 : Type
```

`KoalaBear.ext6Gen` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L92))

> The adjoined root of `X^6 + X^3 + 1`, a primitive 9th root of unity, as an element of
> `Ext6`.

```lean
def ext6Gen : Ext6
```

`KoalaBear.ext6Gen_eq_gen` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L100))

> `ext6Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext6Gen_pow_six` can match, which
> would knock that lemma out of the simp set.

```lean
theorem ext6Gen_eq_gen : ext6Gen = Ext.gen
```

`KoalaBear.toQuot_ext6Gen` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L103))

> `ext6Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext6Gen : Ext.toQuot ext6Gen = Ext.rt ext6Params
```

`KoalaBear.aeval_ext6Gen` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L106))

> `ext6Gen` is a root of `X^6 + X^3 + 1`, in the form `aeval` expects.

```lean
theorem aeval_ext6Gen : aeval ext6Gen ext6Params.poly = 0
```

`KoalaBear.ext6Gen_pow_six` (theorem, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L110))

> **The defining relation**: the adjoined root satisfies `θ^6 = -θ^3 - 1`. Every coefficient is
> `±1`, which is what makes reduction multiplication-free.

```lean
theorem ext6Gen_pow_six :
    ext6Gen ^ 6 = -(ext6Gen ^ 3) - Ext.ofBase (1 : Field)
```

`KoalaBear.ext6Gen_cubed_is_primitive_cube_root` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L120))

> `θ^3` is a primitive cube root of unity: it satisfies `Y^2 + Y + 1 = 0`, which is irreducible
> over KoalaBear because `3 ∤ p - 1`. So `F_p(θ^3)` is the `F_p²` subfield, and this is the
> `2`-then-`3` tower `F_p ⊂ F_p² ⊂ F_p⁶` presented inside a single sextic.

```lean
theorem ext6Gen_cubed_is_primitive_cube_root :
    (ext6Gen ^ 3) ^ 2 + ext6Gen ^ 3 + Ext.ofBase (1 : Field) = 0
```

`KoalaBear.ext6Gen_pow_nine` (theorem, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L126))

> **`θ` is a primitive 9th root of unity**: `θ^9 = 1`.

```lean
theorem ext6Gen_pow_nine : ext6Gen ^ 9 = 1
```

`KoalaBear.card_ext6` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean#L132))

```lean
theorem card_ext6 : Fintype.card Ext6 = fieldSize ^ 6
```

## Depends on

- [Finiteness and cardinality of monic quotient presentations](../extension/cardinality.md)
- [The field structure on an extension](../extension/field.md)
- [Irreducibility of `X^6 + X^3 + 1` over KoalaBear](ext6-2/sexticirreducible.md)

## Sources

- [CompPoly/Fields/KoalaBear/Ext6.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Ext6.json)
