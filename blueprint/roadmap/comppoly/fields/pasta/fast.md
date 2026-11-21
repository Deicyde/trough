---
catalog: module
lean: Pallas.Fast.instMont64x8Field, Pallas.Fast.Field, Pallas.Fast.ofField, Pallas.Fast.ringEquiv, Vesta.Fast.instMont64x8Field, Vesta.Fast.Field, Vesta.Fast.ofField, Vesta.Fast.ringEquiv
statement: formalized
proof: formalized
---

# Fast Pasta base fields

`CompPoly.Fields.Pasta.Fast`, in [CompPoly/Fields/Pasta/Fast.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean), by Gregor Mitscha-Baude.

> Native-word Montgomery implementations of the Pallas and Vesta base field arithmetic.  The
> shared algorithms and proofs live in `CompPoly.Fields.Montgomery.Native64x8Field`; this module
> supplies the two sets of constants and the concrete API.
>
> Both Pasta primes are `1 mod 2 ^ 32`, so both have `montgomeryNegInv = 2 ^ 32 - 1`.

> ## Parameters and carrier

`Pallas.Fast.instMont64x8Field` (instance, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L31))

> The per-field data realizing the Pallas base field as a fast eight-limb Montgomery
> field.

```lean
instance instMont64x8Field : Mont64x8Field Pallas.baseFieldSize
```

`Pallas.Fast.Field` (abbreviation, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L42))

> The fast native-word Pallas base field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`Pallas.Fast.ofField` (definition, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L48))

> Convert from the canonical `ZMod` Pallas base field into fast Montgomery form.

```lean
def ofField (x : Pallas.BaseField) : Field
```

> ## Canonical bridge

`Pallas.Fast.ringEquiv` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L54))

> Ring equivalence between the fast Montgomery representation and `Pallas.BaseField`.

```lean
def ringEquiv : Field ≃+* Pallas.BaseField
```

> ## Parameters and carrier

`Vesta.Fast.instMont64x8Field` (instance, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L67))

> The per-field data realizing the Vesta base field as a fast eight-limb Montgomery
> field.

```lean
instance instMont64x8Field : Mont64x8Field Vesta.baseFieldSize
```

`Vesta.Fast.Field` (abbreviation, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L78))

> The fast native-word Vesta base field carrier, stored as a Montgomery residue.

```lean
abbrev Field : Type
```

> ## Conversions

`Vesta.Fast.ofField` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L84))

> Convert from the canonical `ZMod` Vesta base field into fast Montgomery form.

```lean
def ofField (x : Vesta.BaseField) : Field
```

> ## Canonical bridge

`Vesta.Fast.ringEquiv` (definition, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean#L90))

> Ring equivalence between the fast Montgomery representation and `Vesta.BaseField`.

```lean
def ringEquiv : Field ≃+* Vesta.BaseField
```

## Depends on

- [Fast eight-limb Montgomery fields](../montgomery/native64x8field.md)
- [The Pasta (Pallas / Vesta) base prime fields](basic.md)

## Sources

- [CompPoly/Fields/Pasta/Fast.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Fields/Pasta/Fast.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Fields.Pasta.Fast.json)
