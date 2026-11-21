---
catalog: module
lean: KoalaBear.ext4Params, KoalaBear.ext4Params_d, KoalaBear.ext4Params_W, KoalaBear.ext4Params_q, KoalaBear.ext4Params_poly_irreducible, KoalaBear.Ext4, KoalaBear.ext4Gen, KoalaBear.ext4Gen_eq_gen, KoalaBear.toQuot_ext4Gen, KoalaBear.ext4Gen_pow_four, KoalaBear.aeval_ext4Gen, KoalaBear.card_ext4
statement: formalized
proof: formalized
---

# The degree-4 extension of KoalaBear

`CompPoly.Fields.KoalaBear.Ext4`, in [CompPoly/Fields/KoalaBear/Ext4.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean), by Derek Sorensen.

> `KoalaBear[X] / (X^4 - 3)`, the challenge field used alongside the KoalaBear base field in
> Plonky3-style STARKs.
>
> Irreducibility of `X^4 - 3` is discharged by `Polynomial.irreducible_X_pow_four_sub_C`,
> whose two hypotheses are single exponentiations in the base field:
> `3^((p^4-1)/4) = 1` and `3^((p^2-1)/4) ≠ 1`. Both are closed by `reduce_mod_char`, which does
> modular repeated squaring at elaboration time — no `native_decide`, and no generated
> certificate file.
>
> ## Main definitions
>
> * `KoalaBear.ext4Params`: the `BinomialParams` for `X^4 - 3`.
> * `KoalaBear.Ext4`: the extension field itself.

`KoalaBear.ext4Params` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L48))

> The parameters of the quartic extension `KoalaBear[X] / (X^4 - 3)`.

```lean
def ext4Params : BinomialParams Field
```

`KoalaBear.ext4Params_d` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L57))

```lean
theorem ext4Params_d : ext4Params.d = 4
```

`KoalaBear.ext4Params_W` (theorem, [line 58](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L58))

```lean
theorem ext4Params_W : ext4Params.W = 3
```

`KoalaBear.ext4Params_q` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L59))

```lean
theorem ext4Params_q : ext4Params.q = fieldSize
```

`KoalaBear.ext4Params_poly_irreducible` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L62))

> `X^4 - 3` is irreducible over KoalaBear, by the collapsed Rabin criterion.

```lean
theorem ext4Params_poly_irreducible : Irreducible ext4Params.poly
```

`KoalaBear.Ext4` (abbreviation, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L79))

> The degree-4 extension field of KoalaBear.

```lean
abbrev Ext4 : Type
```

`KoalaBear.ext4Gen` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L82))

> The adjoined fourth root of `3`, as an element of `Ext4`.

```lean
def ext4Gen : Ext4
```

`KoalaBear.ext4Gen_eq_gen` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L92))

> `ext4Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext4Gen_pow_four` can match, which
> would knock that lemma out of the simp set. Use `simp [ext4Gen_eq_gen]` to reach the general
> `Ext.gen` lemmas (`Ext.coeff_gen`, `Ext.gen_pow_d`) when the specialized ones below are not
> enough.

```lean
theorem ext4Gen_eq_gen : ext4Gen = Ext.gen
```

`KoalaBear.toQuot_ext4Gen` (theorem, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L95))

> `ext4Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext4Gen : Ext.toQuot ext4Gen = Ext.rt ext4Params.toExtensionParams
```

`KoalaBear.ext4Gen_pow_four` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L99))

> **The defining relation**, as a theorem rather than only an executable check.

```lean
theorem ext4Gen_pow_four : ext4Gen ^ 4 = Ext.ofBase (3 : Field)
```

`KoalaBear.aeval_ext4Gen` (theorem, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L103))

> `ext4Gen` is a root of `X^4 - 3`, in the form `aeval` expects.

```lean
theorem aeval_ext4Gen : aeval ext4Gen ext4Params.poly = 0
```

`KoalaBear.card_ext4` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean#L106))

```lean
theorem card_ext4 : Fintype.card Ext4 = fieldSize ^ 4
```

## Depends on

- [Finiteness and cardinality of monic quotient presentations](../extension/cardinality.md)
- [The field structure on an extension](../extension/field.md)
- [KoalaBear Field `2^{31} - 2^{24} + 1`](basic.md)

## Proof depends on

- [Irreducibility of binomials `X^d - W` over a finite field](../extension/binomial.md)

## Sources

- [CompPoly/Fields/KoalaBear/Ext4.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/KoalaBear/Ext4.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Ext4.json)
