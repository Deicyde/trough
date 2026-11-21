---
catalog: module
lean: AesField.ghashRoot, AesField.ghashRoot_relation, AesField.toGhash, AesField.toGhash_apply, AesField.toGhash_gen, AesField.toGhash_injective
statement: formalized
proof: formalized
---

# The selected AES embedding into GHASH

`CompPoly.Fields.Binary.Aes.Ghash`, in [CompPoly/Fields/Binary/Aes/Ghash.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean), by CompPoly Contributors.

> AES byte bit `i` represents the coefficient of `X^i`. The selected embedding evaluates
> these eight coefficients at GHASH word `0x0dcb364640a222fe6b8330483c2e9849`, whose bit `i`
> likewise represents the coefficient of `X^i`. This sends AES byte 2 to that root, rather
> than interpreting the byte as the same GHASH word.
>
> The public ring homomorphism executes the finite coefficient evaluation. Its laws follow
> from the quotient universal property and a kernel-checked root identity. The selected root
> matches the field tables in the following pinned implementations; this module establishes
> the mathematical field embedding, not a proof of either implementation or a basis theorem
> for protocol weights.
>
> ## References
>
> * Binius64, revision `6e75a2d1d2e716578ae3ccb62806413fb1615176`,
>   `crates/field/src/fields/ghash.rs`.
>   https://github.com/binius-zk/binius64/blob/6e75a2d1d2e716578ae3ccb62806413fb1615176/crates/field/src/fields/ghash.rs
> * Flock, revision `387768741ce97386f4926786d59015e6cf3f73b4`,
>   `crates/flock-field/src/phi8.rs`.
>   https://github.com/succinctlabs/flock/blob/387768741ce97386f4926786d59015e6cf3f73b4/crates/flock-field/src/phi8.rs

`AesField.ghashRoot` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L42))

> The selected root of the AES modulus, in GHASH polynomial-basis coordinates.

```lean
def ghashRoot : ConcreteBF128Ghash
```

`AesField.ghashRoot_relation` (theorem, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L46))

> The selected GHASH element satisfies the AES defining relation.

```lean
theorem ghashRoot_relation :
    ghashRoot ^ 8 + ghashRoot ^ 4 + ghashRoot ^ 3 + ghashRoot + 1 = 0
```

`AesField.toGhash` (definition, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L70))

> Embed AES coefficients into GHASH by evaluating them at the selected AES root.

```lean
def toGhash : AesField →+* ConcreteBF128Ghash
```

`AesField.toGhash_apply` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L87))

> The embedding evaluates the eight ascending polynomial coefficients at the selected root.

```lean
theorem toGhash_apply (a : AesField) :
    toGhash a = ∑ i : Fin params.d,
      ZMod.castHom (dvd_refl 2) ConcreteBF128Ghash (Ext.coeff a i) * ghashRoot ^ (i : ℕ)
```

`AesField.toGhash_gen` (theorem, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L92))

> The AES polynomial generator maps to the selected GHASH root.

```lean
theorem toGhash_gen : toGhash gen = ghashRoot
```

`AesField.toGhash_injective` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean#L100))

> The selected field embedding identifies no distinct AES elements.

```lean
theorem toGhash_injective : Function.Injective toGhash
```

## Depends on

- [The certified AES polynomial field](basic.md)
- [GHASH Polynomial-Basis Field](../bf128ghash/part-01/impl.md)

## Sources

- [CompPoly/Fields/Binary/Aes/Ghash.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Binary/Aes/Ghash.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.Binary.Aes.Ghash.json)
