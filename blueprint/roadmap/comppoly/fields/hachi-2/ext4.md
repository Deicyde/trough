---
catalog: module
lean: Hachi.ext4Params, Hachi.ext4Params_d, Hachi.ext4Params_W, Hachi.ext4Params_q, Hachi.ext4Params_poly_irreducible, Hachi.Ext4, Hachi.ext4Gen, Hachi.ext4Gen_eq_gen, Hachi.toQuot_ext4Gen, Hachi.ext4Gen_pow_four, Hachi.aeval_ext4Gen, Hachi.card_ext4
statement: formalized
proof: formalized
---

# The degree-4 extension of Hachi

`CompPoly.Fields.Hachi.Ext4`, in [CompPoly/Fields/Hachi/Ext4.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean), by Derek Sorensen.

> `Hachi[X] / (X^4 - 2)`, the degree-4 extension of the 32-bit prime field `2^32 - 99`.
>
> `W = 2` is the smallest non-square modulo `p`, which also makes multiplication by `W` a
> doubling. Because `p ≡ 1 mod 4`, `X^4 - W` is irreducible for any non-square `W`; concretely
> this is discharged by `Polynomial.irreducible_X_pow_four_sub_C` from
> `2^((p^4-1)/4) = 1` and `2^((p^2-1)/4) ≠ 1`.
>
> ## Main definitions
>
> * `Hachi.ext4Params`: the `BinomialParams` for `X^4 - 2`.
> * `Hachi.Ext4`: the extension field itself.

`Hachi.ext4Params` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L46))

> The parameters of the quartic extension `Hachi[X] / (X^4 - 2)`.

```lean
def ext4Params : BinomialParams Field
```

`Hachi.ext4Params_d` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L55))

```lean
theorem ext4Params_d : ext4Params.d = 4
```

`Hachi.ext4Params_W` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L56))

```lean
theorem ext4Params_W : ext4Params.W = 2
```

`Hachi.ext4Params_q` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L57))

```lean
theorem ext4Params_q : ext4Params.q = fieldSize
```

`Hachi.ext4Params_poly_irreducible` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L60))

> `X^4 - 2` is irreducible over Hachi, by the collapsed Rabin criterion.

```lean
theorem ext4Params_poly_irreducible : Irreducible ext4Params.poly
```

`Hachi.Ext4` (abbreviation, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L77))

> The degree-4 extension field of Hachi.

```lean
abbrev Ext4 : Type
```

`Hachi.ext4Gen` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L80))

> The adjoined fourth root of `2`, as an element of `Ext4`.

```lean
def ext4Gen : Ext4
```

`Hachi.ext4Gen_eq_gen` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L90))

> `ext4Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext4Gen_pow_four` can match, which
> would knock that lemma out of the simp set. Use `simp [ext4Gen_eq_gen]` to reach the general
> `Ext.gen` lemmas (`Ext.coeff_gen`, `Ext.gen_pow_d`) when the specialized ones below are not
> enough.

```lean
theorem ext4Gen_eq_gen : ext4Gen = Ext.gen
```

`Hachi.toQuot_ext4Gen` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L93))

> `ext4Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext4Gen : Ext.toQuot ext4Gen = Ext.rt ext4Params.toExtensionParams
```

`Hachi.ext4Gen_pow_four` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L97))

> **The defining relation**, as a theorem rather than only an executable check.

```lean
theorem ext4Gen_pow_four : ext4Gen ^ 4 = Ext.ofBase (2 : Field)
```

`Hachi.aeval_ext4Gen` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L101))

> `ext4Gen` is a root of `X^4 - 2`, in the form `aeval` expects.

```lean
theorem aeval_ext4Gen : aeval ext4Gen ext4Params.poly = 0
```

`Hachi.card_ext4` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean#L104))

```lean
theorem card_ext4 : Fintype.card Ext4 = fieldSize ^ 4
```

## Depends on

- [Finiteness and cardinality of monic quotient presentations](../extension/cardinality.md)
- [The field structure on an extension](../extension/field.md)
- [Hachi prime field `2^32 - 99`](../hachi.md)

## Proof depends on

- [Irreducibility of binomials `X^d - W` over a finite field](../extension/binomial.md)

## Sources

- [CompPoly/Fields/Hachi/Ext4.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/Hachi/Ext4.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Hachi.Ext4.json)
