---
catalog: module
lean: BabyBear.ext4Params, BabyBear.ext4Params_d, BabyBear.ext4Params_W, BabyBear.ext4Params_q, BabyBear.ext4Params_poly_irreducible, BabyBear.Ext4, BabyBear.ext4Gen, BabyBear.ext4Gen_eq_gen, BabyBear.toQuot_ext4Gen, BabyBear.ext4Gen_pow_four, BabyBear.aeval_ext4Gen, BabyBear.card_ext4
statement: formalized
proof: formalized
---

# The degree-4 extension of BabyBear

`CompPoly.Fields.BabyBear.Ext4`, in [CompPoly/Fields/BabyBear/Ext4.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean), by Derek Sorensen.

> `BabyBear[X] / (X^4 - 11)`, the challenge field used alongside the BabyBear base field in
> RISC Zero and Plonky3.
>
> Irreducibility of `X^4 - 11` is discharged by
> `Polynomial.irreducible_X_pow_four_sub_C`, whose two hypotheses are single
> exponentiations in the base field: `11^((p^4-1)/4) = 1` and `11^((p^2-1)/4) ≠ 1`.
>
> ## Main definitions
>
> * `BabyBear.ext4Params`: the `BinomialParams` for `X^4 - 11`.
> * `BabyBear.Ext4`: the extension field itself.

`BabyBear.ext4Params` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L46))

> The parameters of the quartic extension `BabyBear[X] / (X^4 - 11)`.

```lean
def ext4Params : BinomialParams Field
```

`BabyBear.ext4Params_d` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L55))

```lean
theorem ext4Params_d : ext4Params.d = 4
```

`BabyBear.ext4Params_W` (theorem, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L56))

```lean
theorem ext4Params_W : ext4Params.W = 11
```

`BabyBear.ext4Params_q` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L57))

```lean
theorem ext4Params_q : ext4Params.q = fieldSize
```

`BabyBear.ext4Params_poly_irreducible` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L60))

> `X^4 - 11` is irreducible over BabyBear, by the collapsed Rabin criterion.

```lean
theorem ext4Params_poly_irreducible : Irreducible ext4Params.poly
```

`BabyBear.Ext4` (abbreviation, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L77))

> The degree-4 extension field of BabyBear.

```lean
abbrev Ext4 : Type
```

`BabyBear.ext4Gen` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L80))

> The adjoined fourth root of `11`, as an element of `Ext4`.

```lean
def ext4Gen : Ext4
```

`BabyBear.ext4Gen_eq_gen` (theorem, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L90))

> `ext4Gen` is the framework's `Ext.gen`.
>
> Deliberately **not** `@[simp]`: as a rewrite it fires before `ext4Gen_pow_four` can match, which
> would knock that lemma out of the simp set. Use `simp [ext4Gen_eq_gen]` to reach the general
> `Ext.gen` lemmas (`Ext.coeff_gen`, `Ext.gen_pow_d`) when the specialized ones below are not
> enough.

```lean
theorem ext4Gen_eq_gen : ext4Gen = Ext.gen
```

`BabyBear.toQuot_ext4Gen` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L93))

> `ext4Gen` maps to the adjoined root of the specification.

```lean
theorem toQuot_ext4Gen : Ext.toQuot ext4Gen = Ext.rt ext4Params.toExtensionParams
```

`BabyBear.ext4Gen_pow_four` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L97))

> **The defining relation**, as a theorem rather than only an executable check.

```lean
theorem ext4Gen_pow_four : ext4Gen ^ 4 = Ext.ofBase (11 : Field)
```

`BabyBear.aeval_ext4Gen` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L101))

> `ext4Gen` is a root of `X^4 - 11`, in the form `aeval` expects.

```lean
theorem aeval_ext4Gen : aeval ext4Gen ext4Params.poly = 0
```

`BabyBear.card_ext4` (theorem, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean#L104))

```lean
theorem card_ext4 : Fintype.card Ext4 = fieldSize ^ 4
```

## Depends on

- [BabyBear Field `2^{31} - 2^{27} + 1`](basic.md)
- [Finiteness and cardinality of monic quotient presentations](../extension/cardinality.md)
- [The field structure on an extension](../extension/field.md)

## Proof depends on

- [Irreducibility of binomials `X^d - W` over a finite field](../extension/binomial.md)

## Sources

- [CompPoly/Fields/BabyBear/Ext4.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/BabyBear/Ext4.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.BabyBear.Ext4.json)
