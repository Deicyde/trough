---
catalog: module
lean: Cedar.Thm.Duration.parse_eq_duration?_of_isDurationValue, Cedar.Thm.Duration.isDurationValue_unique
statement: formalized
proof: formalized
---

# Duration/Lemmas

`Cedar.Thm.Ext.Duration.Lemmas`, in [Cedar/Thm/Ext/Duration/Lemmas.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Lemmas.lean).

> ============================================================================================
> # Duration parser lemmas
>
> Duration quantity tokens are the `Digit⁺` strings characterized by `IsDigits`; the
> `IsDigits.ne_empty` / `IsDigits.toNat?'_isSome` / `IsDigits.all_isDigit` projections (in
> `Cedar.Thm.Data.String`) recover the facts these proofs consume.
> ============================================================================================

`Cedar.Thm.Duration.parse_eq_duration?_of_isDurationValue` (theorem, [line 2753](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Lemmas.lean#L2753))

> On a rendering to which the grammar assigns `v`, `Duration.parse` reaches the range check with
> exactly `v`. Thus acceptance is decided by `duration?` alone.

```lean
public theorem parse_eq_duration?_of_isDurationValue {str : String} {v : Int}
    (h : IsDurationValue str v) :
    Duration.parse str = duration? v
```

`Cedar.Thm.Duration.isDurationValue_unique` (theorem, [line 2805](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Lemmas.lean#L2805))

> The declarative value relation is single-valued: a duration string denotes at most one
> integer, including when that integer lies outside the parser's `Int64` range.

```lean
public theorem isDurationValue_unique {str : String} {v₁ v₂ : Int}
    (h₁ : IsDurationValue str v₁) (h₂ : IsDurationValue str v₂) : v₁ = v₂
```

## Depends on

- [Duration grammar: definitions](grammar.md)

## Sources

- [Cedar/Thm/Ext/Duration/Lemmas.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Duration.Lemmas.json)
