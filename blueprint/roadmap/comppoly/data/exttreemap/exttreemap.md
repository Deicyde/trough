---
catalog: module
lean: Std.ExtTreeMap.getElem?_pfilter, Std.ExtTreeMap.filter_empty, Std.ExtTreeMap.getElem?_mergeWith_at, Std.ExtTreeMap.mergeWith_of_mem_mem, Std.ExtTreeMap.mergeWith_of_mem_left, Std.ExtTreeMap.mergeWith_of_mem_right, Std.ExtTreeMap.mergeWith_of_not_mem, Std.ExtTreeMap.mergeWith_empty, Std.ExtTreeMap.mergeWith_of_comm, Std.ExtTreeMap.toList_ofList, Std.ExtTreeMap.getElem?_filter_with_getKey, Std.ExtTreeMap.filter_mem, Std.ExtTreeMap.filter_not_mem, Std.ExtTreeMap.filter_not_pred
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `Std.ExtTreeMap`

`CompPoly.Data.ExtTreeMap.ExtTreeMap`, in [CompPoly/Data/ExtTreeMap/ExtTreeMap.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean), by Markus Himmel.

> `mergeWith` and `filter` lemmas for `Std.ExtTreeMap`, used by the multivariate
> polynomial representation in `CompPoly.Multivariate.Unlawful`.
>
> Vendored from
> [`Verified-zkEVM/ExtTreeMapLemmas`](https://github.com/Verified-zkEVM/ExtTreeMapLemmas)
> (tag `v4.29.1`, commit `3fee686227f18dca03bb7fc42ca5a9275d6cfda6`). The original
> imported `Mathlib.Tactic` wholesale; here we narrow to the specific tactic
> modules actually needed by the proofs below.

`Std.ExtTreeMap.getElem?_pfilter` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L39))

```lean
theorem getElem?_pfilter
    {cmp : α → α → Ordering} [TransCmp cmp]
    {m : ExtTreeMap α β cmp} {f : α → β → Bool} {k : α} :
    (m.filter f)[k]? =
    m[k]?.pfilter (fun v h' =>
      f (m.getKey k
          (contains_eq_isSome_getElem?.trans (Option.isSome_of_eq_some h'))) v)
```

`Std.ExtTreeMap.filter_empty` (lemma, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L54))

```lean
lemma filter_empty {f : α → β → Bool} :
    filter f (∅ : Std.ExtTreeMap α β cmp) = ∅
```

`Std.ExtTreeMap.getElem?_mergeWith_at` (theorem, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L60))

```lean
theorem getElem?_mergeWith_at
    {m₁ m₂ : ExtTreeMap α β cmp} {f : α → β → β → β} {k : α} :
  (m₁.mergeWith f m₂)[k]? =
  match m₁[k]?, m₂[k]? with
  | .some v₁, .some v₂ => .some (f k v₁ v₂)
  | .some v₁, .none    => .some v₁
  | .none,    .some v₂ => .some v₂
  | .none,    .none    => .none
```

`Std.ExtTreeMap.mergeWith_of_mem_mem` (lemma, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L86))

```lean
lemma mergeWith_of_mem_mem (h₁ : k ∈ m₁) (h₂ : k ∈ m₂) :
    (m₁.mergeWith f m₂)[k]? = .some (f k m₁[k] m₂[k])
```

`Std.ExtTreeMap.mergeWith_of_mem_left` (lemma, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L94))

```lean
lemma mergeWith_of_mem_left (h₁ : k ∈ m₁) (h₂ : k ∉ m₂) :
    (m₁.mergeWith f m₂)[k]? = m₁[k]?
```

`Std.ExtTreeMap.mergeWith_of_mem_right` (lemma, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L102))

```lean
lemma mergeWith_of_mem_right (h₁ : k ∉ m₁) (h₂ : k ∈ m₂) :
    (m₁.mergeWith f m₂)[k]? = m₂[k]?
```

`Std.ExtTreeMap.mergeWith_of_not_mem` (lemma, [line 110](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L110))

```lean
lemma mergeWith_of_not_mem (h₁ : k ∉ m₁) (h₂ : k ∉ m₂) :
    (m₁.mergeWith f m₂)[k]? = .none
```

`Std.ExtTreeMap.mergeWith_empty` (lemma, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L124))

```lean
lemma mergeWith_empty {f : α → β → β → β}
    {cmp : α → α → Ordering} [Std.TransCmp cmp] [Std.LawfulEqCmp cmp]
    {t : ExtTreeMap α β cmp} :
    mergeWith f t ∅ = t
```

`Std.ExtTreeMap.mergeWith_of_comm` (lemma, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L130))

```lean
lemma mergeWith_of_comm (h : ∀ {x}, Std.Commutative (f x)) :
    m₁.mergeWith f m₂ = m₂.mergeWith f m₁
```

`Std.ExtTreeMap.toList_ofList` (lemma, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L138))

```lean
lemma toList_ofList [BEq α] [LawfulBEq α] : ofList (toList m) cmp = m
```

`Std.ExtTreeMap.getElem?_filter_with_getKey` (lemma, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L142))

```lean
lemma getElem?_filter_with_getKey {f : α → β → Bool} {k : α} {m : ExtTreeMap α β cmp} :
    (m.filter f)[k]? = m[k]?.filter (f k)
```

`Std.ExtTreeMap.filter_mem` (lemma, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L149))

```lean
lemma filter_mem (h : k ∈ m) : f k m[k] → (filter f m)[k]? = .some m[k]
```

`Std.ExtTreeMap.filter_not_mem` (lemma, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L154))

```lean
lemma filter_not_mem (h : k ∉ m) : (filter f m)[k]? = .none
```

`Std.ExtTreeMap.filter_not_pred` (lemma, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean#L158))

```lean
lemma filter_not_pred (h : k ∈ m) : ¬ (f k m[k]) → (filter f m)[k]? = .none
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Proof depends on

- [Auxiliary lemmas for `Std.DTreeMap`](dtreemap.md)
- [Auxiliary lemmas for `Std.ExtDTreeMap`](extdtreemap.md)

## Sources

- [CompPoly/Data/ExtTreeMap/ExtTreeMap.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/ExtTreeMap.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.ExtTreeMap.ExtTreeMap.json)
