---
catalog: module
lean: Cedar.Thm.map_make_filterMap_find?, Cedar.Thm.map_make_filterMap_find?_none, Cedar.Thm.app_table_make_filterMap, Cedar.Thm.map_make_filterMap_flatten_find?
statement: formalized
proof: formalized
---

# UDF

`Cedar.Thm.SymCC.Term.UDF`, in [Cedar/Thm/SymCC/Term/UDF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean).

> Some lemmas to simplify `UDF`s.

`Cedar.Thm.map_make_filterMap_find?` (theorem, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean#L31))

> For simplifying `Factory.app` on a `UDF` with a table
> of the form `make (m.toList.filterMap f)`.

```lean
theorem map_make_filterMap_find?
  [BEq α] [LawfulBEq α]
  [DecidableEq γ] [LT γ] [DecidableLT γ] [StrictLT γ]
  {m : Map α β}
  {k : α} {v : β} {k' : γ} {v' : κ}
  {f : α × β → Option (γ × κ)}
  (hfind : m.find? k = .some v)
  (hkv : f (k, v) = .some (k', v'))
  (hf : ∀ kv, (∃ v'', f kv = .some (k', v'')) → kv.1 = k) :
  (Map.make (m.toList.filterMap f)).find? k' = .some v'
```

`Cedar.Thm.map_make_filterMap_find?_none` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean#L65))

> Similar to above but for the `none` case

```lean
theorem map_make_filterMap_find?_none
  [LT α] [DecidableLT α] [StrictLT α] [DecidableEq α]
  [DecidableEq γ] [LT γ] [DecidableLT γ] [StrictLT γ]
  {m : Map α β}
  {k : α} {k' : γ}
  {f : α × β → Option (γ × κ)}
  (hfind : m.find? k = .none)
  (hf : ∀ kv, (∃ v'', f kv = .some (k', v'')) → kv.1 = k) :
  (Map.make (m.toList.filterMap f)).find? k' = .none
```

`Cedar.Thm.app_table_make_filterMap` (theorem, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean#L93))

> Simplifying `Factory.app` on a `UDF` with a table
> of the form `make (m.toList.filterMap f)`.

```lean
theorem app_table_make_filterMap
  [BEq α] [LawfulBEq α]
  {arg : TermType} {out : TermType} {default : Term}
  {m : Map α β} {k : α} {v : β}
  {t : Term} {r : Term}
  {f : α × β → Option (Term × Term)}
  (hfind : m.find? k = .some v)
  (hkv : f (k, v) = .some (t, r))
  (hf : ∀ kv, (∃ v'', f kv = .some (t, v'')) → kv.1 = k)
  (hlit : t.isLiteral) :
  Factory.app
    (.udf {
      arg := arg,
      out := out,
      table := Map.make (m.toList.filterMap f),
      default := default,
    }) t
  = r
```

`Cedar.Thm.map_make_filterMap_flatten_find?` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean#L124))

> For simplifying `Factory.app` on a `UDF` with a table
> of the form `make (m.toList.filterMap f).flatten`.

```lean
theorem map_make_filterMap_flatten_find?
  [BEq α] [BEq β] [LawfulBEq α] [LawfulBEq β]
  [DecidableEq γ] [LT γ] [DecidableLT γ] [StrictLT γ]
  {m : Map α β}
  {k : α} {v : β} {k' : γ} {v' : κ}
  {f : α × β → Option (List (γ × κ))}
  (hfind : m.find? k = .some v)
  (hkv : ∃ l, f (k, v) = .some l ∧ l.find? (λ x => x.1 == k') = .some (k', v'))
  (hf : ∀ kv, (∃ l, f kv = .some l ∧ (l.find? (λ x => x.1 == k')).isSome) → kv.1 = k) :
  (Map.make (m.toList.filterMap f).flatten).find? k' = .some v'
```

## Depends on

- [Factory](../../../symcc/part-01/factory.md)

## Proof depends on

- [Map properties](../../data/map.md)
- [Strict ordering of Cedar terms](../data/lt.md)

## Sources

- [Cedar/Thm/SymCC/Term/UDF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/UDF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Term.UDF.json)
