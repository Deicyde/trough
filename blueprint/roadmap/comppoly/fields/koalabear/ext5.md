---
catalog: module
lean: KoalaBear.ext5Params, KoalaBear.ext5Params_d, KoalaBear.ext5Params_q, KoalaBear.ext5Params_poly, KoalaBear.Ext5, KoalaBear.ext5Gen, KoalaBear.ext5Gen_eq_gen, KoalaBear.toQuot_ext5Gen, KoalaBear.aeval_ext5Gen, KoalaBear.ext5Gen_pow_five, KoalaBear.card_ext5
statement: formalized
proof: formalized
---

# The degree-5 extension of KoalaBear

`CompPoly.Fields.KoalaBear.Ext5`, in [CompPoly/Fields/KoalaBear/Ext5.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean), by Derek Sorensen.

> `KoalaBear[X] / (X^5 + X^2 - 1)`. The modulus is necessarily *not* a binomial: since
> `gcd(5, p - 1) = 1`, the map `x ↦ x^5` is a bijection on KoalaBear, so every `X^5 - W` has a
> root and no degree-5 binomial extension exists. This is the first consumer of the general
> monic-modulus side of the extension framework (`CompPoly.Extension.ExtensionParams`).
>
> Irreducibility of `X^5 + X^2 - 1` is `KoalaBear.quinticPoly_irreducible`
> (`CompPoly/Fields/KoalaBear/Ext5/QuinticIrreducible.lean`), proved by Rabin's test at prime
> degree with kernel-checked certificates. Supporting files live under `KoalaBear/Ext5/`.
>
> ## Main definitions
>
> * `KoalaBear.ext5Params`: the `ExtensionParams` for `X^5 + X^2 - 1`.
> * `KoalaBear.Ext5`: the extension field itself.

`KoalaBear.ext5Params` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L37))

> The parameters of the quintic extension `KoalaBear[X] / (X^5 + X^2 - 1)`: the lower
> coefficients of the monic modulus are `(-1, 0, 1, 0, 0)`.

```lean
def ext5Params : ExtensionParams Field
```

`KoalaBear.ext5Params_d` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L46))

```lean
theorem ext5Params_d : ext5Params.d = 5
```

`KoalaBear.ext5Params_q` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L47))

```lean
theorem ext5Params_q : ext5Params.q = fieldSize
```

`KoalaBear.ext5Params_poly` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L50))

> The defining polynomial of the parameters is the quintic `X^5 + X^2 - 1`.

```lean
theorem ext5Params_poly : ext5Params.poly = quinticPoly
```

`KoalaBear.Ext5` (abbreviation, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L73))

> The degree-5 extension field of KoalaBear.

```lean
abbrev Ext5 : Type
```

`KoalaBear.ext5Gen` (definition, [line 76](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L76))

> The adjoined root of `X^5 + X^2 - 1`, as an element of `Ext5`.

```lean
def ext5Gen : Ext5
```

`KoalaBear.ext5Gen_eq_gen` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L84))

> `ext5Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext5Gen_pow_five` can match, which
> would knock that lemma out of the simp set.

```lean
theorem ext5Gen_eq_gen : ext5Gen = Ext.gen
```

`KoalaBear.toQuot_ext5Gen` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L87))

> `ext5Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext5Gen : Ext.toQuot ext5Gen = Ext.rt ext5Params
```

`KoalaBear.aeval_ext5Gen` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L90))

> `ext5Gen` is a root of `X^5 + X^2 - 1`, in the form `aeval` expects.

```lean
theorem aeval_ext5Gen : aeval ext5Gen ext5Params.poly = 0
```

`KoalaBear.ext5Gen_pow_five` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L93))

> **The defining relation**: the adjoined root satisfies `g^5 = 1 - g^2`.

```lean
theorem ext5Gen_pow_five : ext5Gen ^ 5 = Ext.ofBase (1 : Field) - ext5Gen ^ 2
```

`KoalaBear.card_ext5` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean#L99))

```lean
theorem card_ext5 : Fintype.card Ext5 = fieldSize ^ 5
```

## Depends on

- [Finiteness and cardinality of monic quotient presentations](../extension/cardinality.md)
- [The field structure on an extension](../extension/field.md)
- [Irreducibility of `X^5 + X^2 - 1` over KoalaBear](ext5-2/quinticirreducible.md)

## Sources

- [CompPoly/Fields/KoalaBear/Ext5.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext5.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Ext5.json)
