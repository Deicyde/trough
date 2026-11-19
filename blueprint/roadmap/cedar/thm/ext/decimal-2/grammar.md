---
catalog: module
lean: Cedar.Thm.Decimal.IsNatural, Cedar.Thm.Decimal.IsWfFrac, Cedar.Thm.Decimal.DecimalProduction, Cedar.Thm.Decimal.IsWfDecimal, Cedar.Thm.Decimal.value, Cedar.Thm.Decimal.IsDecimalValue, Cedar.Thm.Decimal.normalize
statement: formalized
proof: formalized
---

# Decimal grammar: definitions

`Cedar.Thm.Ext.Decimal.Grammar`, in [Cedar/Thm/Ext/Decimal/Grammar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean).

> This file contains only the grammar-level definitions — the well-formedness predicates and the
> value relation — as a direct, parser-independent transcription of the decimal grammar.
> `DecimalProduction` relates a rendering to its grammar fields, `IsWfDecimal` existentially hides
> those fields, `value` gives their denotation, and `IsDecimalValue s v` adds that denotation to the
> same production witness. The lemmas connecting these definitions to `Decimal.parse` (in
> particular the digit-string ↔ `toInt?'`/`toNat?'` bridges) live in
> `Cedar.Thm.Ext.Decimal.Lemmas`.
>
> `Sign ::= ['-']` uses the shared `IsWfSign` predicate. The decimal-specific `Natural` and
> `Fraction` productions are named locally using the shared digit predicates `IsDigits` and
> `IsAtMostNDigits`. Their value readers (`natOf`, `signOf`, and `lenOf`) and string-to-number bridges
> live in `Cedar.Thm.Data.String`.

`Cedar.Thm.Decimal.IsNatural` (abbreviation, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L47))

> The grammar's `Natural ::= Digit⁺`: the unsigned natural-number production. An `abbrev` for
> the shared `IsDigits` predicate, so every `IsDigits` lemma applies without unfolding.

```lean
public abbrev IsNatural (s : String) : Prop
```

`Cedar.Thm.Decimal.IsWfFrac` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L51))

> The grammar's `Fraction ::= Digit{1,4}`: 1 to `DECIMAL_DIGITS` digits, an instance of the
> shared bounded-digits predicate.

```lean
public def IsWfFrac (s : String) : Prop
```

`Cedar.Thm.Decimal.DecimalProduction` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L56))

> A decimal grammar production: `s` is the rendering of well-formed `Sign`, `Natural`, and
> `Fraction` fields, concatenated around the literal decimal point.

```lean
public def DecimalProduction (s sign natural fraction : String) : Prop
```

`Cedar.Thm.Decimal.IsWfDecimal` (definition, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L65))

> Well-formed decimal syntax: `s` is the rendering of a well-formed `Sign ::= ['-']`,
> `Natural ::= Digit⁺`, `'.'`, and `Fraction ::= Digit{1,4}`, concatenated in that order.
> This is the direct grammar transcription; it does not compute a value or invoke a parser.

```lean
public def IsWfDecimal (s : String) : Prop
```

`Cedar.Thm.Decimal.value` (definition, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L74))

> The grammar's value function, applied to an already-decomposed literal:
>
>   value = sign × (nat(Natural) × 10⁴ + nat(Fraction) × 10^(4 − |Fraction|))
>
> `IsWfFrac fraction` bounds `lenOf fraction ≤ DECIMAL_DIGITS`, so converting the second
> exponent to `Nat` does not clamp a negative value on a well-formed field.

```lean
public def value (sign natural fraction : String) : Int
```

`Cedar.Thm.Decimal.IsDecimalValue` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L86))

> `v` is the value of the decimal literal `s`: `s` is the rendering of a well-formed
> `Sign ::= ['-']`, `Natural ::= Digit⁺`, `'.'`, and `Fraction ::= Digit{1,4}`, concatenated in
> that order, and `v` is what the grammar's value function assigns to those fields.
>
> The existential supplies the split, so no string surgery (`front`/`drop`/`splitToList`) and no
> `Option` appear here. The relation is single-valued (`isDecimalValue_unique`), and a string is
> well-formed exactly when it has some value (`wf_iff_exists_value`).

```lean
public def IsDecimalValue (s : String) (v : Int) : Prop
```

`Cedar.Thm.Decimal.normalize` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean#L93))

> Canonical-form normalizer: parse the string and re-serialize.
> Returns `none` for malformed or out-of-range inputs.

```lean
public def normalize (s : String) : Option String
```

## Depends on

- [Spec/Ext/Decimal](../../../spec/ext-2/decimal.md)
- [String](../../data/string.md)

## Sources

- [Cedar/Thm/Ext/Decimal/Grammar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal/Grammar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Decimal.Grammar.json)
