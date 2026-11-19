---
catalog: module
lean: Std.DTreeMap.Const.get?_foldl_no_touch, Std.DTreeMap.Const.get?_mergeWith, Std.DTreeMap.Internal.Impl.Const.get?_filter_with_getKey_pfilter, Std.DTreeMap.get?_filter_with_getKey_pfilter
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `Std.DTreeMap`

`CompPoly.Data.ExtTreeMap.DTreeMap`, in [CompPoly/Data/ExtTreeMap/DTreeMap.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean), by Markus Himmel.

> Lemmas about `mergeWith` and `filter` on `Std.DTreeMap` (and its internal
> implementation) that are used downstream by the multivariate polynomial
> representation in `CompPoly.Multivariate.Unlawful`.
>
> Vendored from
> [`Verified-zkEVM/ExtTreeMapLemmas`](https://github.com/Verified-zkEVM/ExtTreeMapLemmas)
> (tag `v4.29.1`, commit `3fee686227f18dca03bb7fc42ca5a9275d6cfda6`).

`Std.DTreeMap.Const.get?_foldl_no_touch` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean#L36))

```lean
theorem Const.get?_foldl_no_touch
    [TransCmp cmp] [LawfulEqCmp cmp]
    (k : α) (f : α → β → β → β)
    (l : List (α × β)) (t : DTreeMap α (fun _ => β) cmp)
    (hno : ∀ p ∈ l, cmp p.1 k ≠ .eq) :
    Const.get? (l.foldl (fun acc p =>
      Const.alter acc p.1 (fun
        | none => some p.2
        | some b₁ => some (f p.1 b₁ p.2))
    ) t) k = Const.get? t k
```

`Std.DTreeMap.Const.get?_mergeWith` (theorem, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean#L68))

```lean
theorem Const.get?_mergeWith [TransCmp cmp] [LawfulEqCmp cmp]
    (f : α → β → β → β) (t₁ t₂ : DTreeMap α (fun _ => β) cmp) (k : α) :
    get? (mergeWith f t₁ t₂) k =
      match get? t₁ k, get? t₂ k with
      | some v₁, some v₂ => some (f k v₁ v₂)
      | some v₁, none => some v₁
      | none, some v₂ => some v₂
      | none, none => none
```

`Std.DTreeMap.Internal.Impl.Const.get?_filter_with_getKey_pfilter` (theorem, [line 262](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean#L262))

```lean
theorem Internal.Impl.Const.get?_filter_with_getKey_pfilter [Ord α] [TransOrd α]
    (m : DTreeMap.Internal.Impl α (fun _ => β)) (h : m.WF) (f : α → β → Bool) (k : α) :
    Const.get? (m.filter f h.balanced).1 k =
      (Const.get? m k).pfilter (fun v h' =>
        f (m.getKey k ((contains_eq_isSome_get? h).trans
          (Option.isSome_of_eq_some h'))) v)
```

`Std.DTreeMap.get?_filter_with_getKey_pfilter` (theorem, [line 274](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean#L274))

```lean
theorem get?_filter_with_getKey_pfilter {cmp : α → α → Ordering} [TransCmp cmp]
    (m : DTreeMap α (fun _ => β) cmp) (f : α → β → Bool) (k : α) :
    Const.get? (m.filter f) k =
      (Const.get? m k).pfilter (fun v h' =>
        f (m.getKey k (Const.contains_eq_isSome_get?.trans
          (Option.isSome_of_eq_some h'))) v)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/ExtTreeMap/DTreeMap.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Data/ExtTreeMap/DTreeMap.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.ExtTreeMap.DTreeMap.json)
