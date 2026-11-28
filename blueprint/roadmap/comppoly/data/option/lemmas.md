---
catalog: module
lean: Option.filter_eq_self
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `Option`

`CompPoly.Data.Option.Lemmas`, in [CompPoly/Data/Option/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Option/Lemmas.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa.

`Option.filter_eq_self` (theorem, [line 20](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Option/Lemmas.lean#L20))

> `Option.filter` leaves its argument alone exactly when the predicate holds of the contained
> value. The `Option` analogue of `List.filter_eq_self` and `Array.filter_eq_self`.

```lean
theorem filter_eq_self {α : Type*} {o : Option α} {p : α → Bool} :
    o.filter p = o ↔ ∀ a ∈ o, p a
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/Option/Lemmas.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Data/Option/Lemmas.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.Option.Lemmas.json)
