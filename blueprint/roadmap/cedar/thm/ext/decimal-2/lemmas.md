---
catalog: module
lean: Cedar.Thm.Decimal.isDecimalValue_unique, Cedar.Thm.Decimal.isDecimalValue_toString, Cedar.Thm.Decimal.toString_isWfDecimal
statement: formalized
proof: formalized
---

# Decimal/Lemmas

`Cedar.Thm.Ext.Decimal.Lemmas`, in [Cedar/Thm/Ext/Decimal/Lemmas.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Lemmas.lean).

> ============================================================================================
> # Grammar ↔ parser bridge lemmas
>
> `IsDecimalValue` is phrased over the grammar's productions (`IsWfSign`/`IsNatural`/`IsWfFrac`)
> as a rendering `sign ++ natural ++ "." ++ fraction`, with the value read off those three
> fields. `Decimal.parse` instead splits on `'.'` first and parses the signed left field through
> `toInt?'`. These lemmas connect the views: the rendering splits back into its parts, a digit
> string is exactly one the stdlib parser accepts, and the two value expressions agree. Together
> they reduce `Decimal.parse s` on a string with a value to a single `Int64` range check
> (`parse_eq_decimal?_of_isDecimalValue`), which is what the soundness/completeness proofs
> consume.
>
> The `IsDigits` predicate and its `toNat?'` bridges (`no_underscore_of_isDigits`,
> `isNat_of_isDigits`, `isDigits_of_isNat`, `toNat?'_isSome_of_isDigits`,
> `isDigits_of_toNat?'_isSome`) are shared with the duration grammar and live in
> `Cedar.Thm.Data.String`; the integer-specific lemmas below build on them.
> ============================================================================================

`Cedar.Thm.Decimal.isDecimalValue_unique` (theorem, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Lemmas.lean#L278))

> The value spec is single-valued: a string has at most one value. Because the grammar puts
> exactly one `'.'` in the rendering and `Natural` is a non-empty digit run, the decomposition a
> witness supplies is forced, so `IsDecimalValue` is a function in relational clothing.

```lean
public theorem isDecimalValue_unique {s : String} {v₁ v₂ : Int}
    (h₁ : IsDecimalValue s v₁) (h₂ : IsDecimalValue s v₂) : v₁ = v₂
```

> ============================================================================================
> # `toString` well-formedness and value
> ============================================================================================

`Cedar.Thm.Decimal.isDecimalValue_toString` (theorem, [line 514](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Lemmas.lean#L514))

> The canonical string representation of a decimal is well-formed and denotes exactly that
> decimal's value. Together with `parse_toString_roundtrip` this is what rules out a vacuously
> satisfiable spec.

```lean
public theorem isDecimalValue_toString (d : Decimal) : IsDecimalValue (toString d) d.toInt
```

`Cedar.Thm.Decimal.toString_isWfDecimal` (theorem, [line 575](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Lemmas.lean#L575))

> The string produced by `toString d` is well-formed for parsing.

```lean
public theorem toString_isWfDecimal (d : Decimal) : IsWfDecimal (toString d)
```

## Depends on

- [Decimal grammar: definitions](grammar.md)

## Sources

- [Cedar/Thm/Ext/Decimal/Lemmas.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Decimal.Lemmas.json)
