---
catalog: module
lean: Std.ExtDTreeMap.get?_filter_with_getKey_pfilter
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `Std.ExtDTreeMap`

`CompPoly.Data.ExtTreeMap.ExtDTreeMap`, in [CompPoly/Data/ExtTreeMap/ExtDTreeMap.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/ExtTreeMap/ExtDTreeMap.lean), by Markus Himmel.

> Bridge lemma lifting `DTreeMap.get?_filter_with_getKey_pfilter` to
> `Std.ExtDTreeMap`, used in turn by the `Std.ExtTreeMap` layer.
>
> Vendored from
> [`Verified-zkEVM/ExtTreeMapLemmas`](https://github.com/Verified-zkEVM/ExtTreeMapLemmas)
> (tag `v4.29.1`, commit `3fee686227f18dca03bb7fc42ca5a9275d6cfda6`).

`Std.ExtDTreeMap.get?_filter_with_getKey_pfilter` (theorem, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/ExtTreeMap/ExtDTreeMap.lean#L28))

```lean
theorem ExtDTreeMap.get?_filter_with_getKey_pfilter {cmp : α → α → Ordering} [TransCmp cmp]
    (m : ExtDTreeMap α (fun _ => β) cmp) (f : α → β → Bool) (k : α) :
    Const.get? (m.filter f) k =
    (Const.get? m k).pfilter (fun v h' =>
      f (m.getKey k
          (Const.contains_eq_isSome_get?.trans (Option.isSome_of_eq_some h'))) v)
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/ExtTreeMap/ExtDTreeMap.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/ExtTreeMap/ExtDTreeMap.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.ExtTreeMap.ExtDTreeMap.json)
