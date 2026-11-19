---
catalog: module
lean: String.IsDigits, String.IsFixedDigits, String.IsAtMostNDigits, String.IsWfSign, String.natOf, String.lenOf, String.signOf, String.toNat?'_toString, String.toNat?'_repr, String.isDigits_toString, String.isDigits_repr
statement: formalized
proof: formalized
---

# String

`Cedar.Thm.Data.String`, in [Cedar/Thm/Data/String.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean).

> ==============================================================================================
> # Digit strings (`Digit⁺`) and their correspondence with `toNat?'`
>
> `IsDigits` is the grammar-level notion of a non-empty run of digit characters — the
> `Digit⁺` production common to numeric grammars. These lemmas connect it to the stdlib
> natural-number parser `toNat?'`: a digit string is exactly one `toNat?'` accepts (modulo the
> `'_'` separator, which `toNat?'` rejects and `Char.isDigit` never admits). The `IsDigits.*`
> projections at the end give dot-notation for the facts parser proofs consume.
> ==============================================================================================

`String.IsDigits` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L41))

> `Digit⁺`: a non-empty string all of whose characters are decimal digits.

```lean
public def IsDigits (s : String) : Prop
```

`String.IsFixedDigits` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L46))

> `Digit{n}`: a run of exactly `n` decimal digits. The fixed-width refinement of `IsDigits`,
> used wherever a grammar pins a field's width (the datetime grammar's `YYYY`, `MM`, `SSS`, …).

```lean
public def IsFixedDigits (n : Nat) (s : String) : Prop
```

`String.IsAtMostNDigits` (definition, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L51))

> `Digit{1,n}`: between one and `n` decimal digits. `IsDigits` supplies the lower bound and the
> length constraint the upper (the decimal grammar's `Fraction ::= Digit{1,4}`).

```lean
public def IsAtMostNDigits (n : Nat) (s : String) : Prop
```

`String.IsWfSign` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L56))

> `['-']`: an optional leading minus sign, either present or absent. Shared by the numeric
> grammars that admit a signed literal (decimal's `Sign`, duration's leading `'-'`).

```lean
public def IsWfSign (s : String) : Prop
```

`String.natOf` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L61))

> Natural-number value of a captured decimal digit string, defaulting to `0` when parsing fails.
> On a field satisfying `IsDigits`, the default is never taken.

```lean
public def natOf (s : String) : Nat
```

`String.lenOf` (definition, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L64))

> Length of a captured string as an integer, for use in grammar value formulas.

```lean
public def lenOf (s : String) : Int
```

`String.signOf` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L67))

> Sign denoted by a captured optional-minus field.

```lean
public def signOf (s : String) : Int
```

`String.toNat?'_toString` (theorem, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L142))

> Rendering a natural number and parsing it with Cedar's underscore-rejecting parser
> recovers the original number.

```lean
public theorem toNat?'_toString (n : Nat) : toNat?' (toString n) = some n
```

`String.toNat?'_repr` (theorem, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L153))

> `Nat.repr` is accepted by Cedar's natural-number parser.

```lean
public theorem toNat?'_repr (n : Nat) : toNat?' (Nat.repr n) = some n
```

`String.isDigits_toString` (theorem, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L157))

> The canonical decimal rendering of a natural number is a nonempty digit string.

```lean
public theorem isDigits_toString (n : Nat) : IsDigits (toString n)
```

`String.isDigits_repr` (theorem, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean#L161))

> `Nat.repr` is a nonempty digit string.

```lean
public theorem isDigits_repr (n : Nat) : IsDigits (Nat.repr n)
```

> ==============================================================================================
> # Splitting a string on a separator
> ==============================================================================================

> ==============================================================================================
> # `toString`/`repr` of naturals contains no `'.'`
> ==============================================================================================

> ==============================================================================================
> # Digit-accumulating folds and `Nat.toDigits` roundtrip
> ==============================================================================================

## Depends on

- [Ext/Util](../../spec/ext-2/util.md)

## Sources

- [Cedar/Thm/Data/String.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/String.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.String.json)
