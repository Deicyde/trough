---
catalog: module
lean: Cslib.FinFun.update, Cslib.FinFun.update_coe, Cslib.FinFun.update_apply, Cslib.FinFun.update_support, Cslib.FinFun.update_idem, Cslib.FinFun.update_comm, Cslib.FinFun.update_self, Cslib.FinFun.update_support_subseteq
statement: formalized
proof: formalized
---

# Update for finite functions

`Cslib.Foundations.Data.FinFun.Update`, in [Cslib/Foundations/Data/FinFun/Update.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean), by Fabrizio Montesi.

> This module defines the update operation for finite functions, that is, the equivalent of
> `Function.update` for `FinFun`.

`Cslib.FinFun.update` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L27))

> `FinFun` equivalent of `Function.update`.

```lean
def update (f : α →₀ β) (a : α) (b : β) : α →₀ β
```

`Cslib.FinFun.update_coe` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L37))

> `FinFun.update` is consistent with `Function.update`.

```lean
theorem update_coe (f : α →₀ β) : (f.update a b : α → β) = Function.update f a b
```

`Cslib.FinFun.update_apply` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L42))

> Conditional characterisation of the functional interface of `FinFun.update`.

```lean
theorem update_apply (f : α →₀ β) : ((f.update a' b) a) = if a = a' then b else f a
```

`Cslib.FinFun.update_support` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L47))

> Conditional characterisation of the support of an updated `FinFun`.

```lean
theorem update_support (f : α →₀ β) :
    (f.update a b).support = if b = 0 then f.support \ {a} else f.support ∪ {a}
```

`Cslib.FinFun.update_idem` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L52))

> Updating a finite function on the same key is the same as doing the last update.

```lean
theorem update_idem (f : α →₀ β) : (f.update a b).update a b' = f.update a b'
```

`Cslib.FinFun.update_comm` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L56))

> Updates on different keys commute.

```lean
theorem update_comm (f : α →₀ β) (h : a ≠ a') :
    (f.update a b).update a' b' = (f.update a' b').update a b
```

`Cslib.FinFun.update_self` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L62))

> Updates that do not change mappings are redundant.

```lean
theorem update_self (f : α →₀ β) : (f.update a (f a)) = f
```

`Cslib.FinFun.update_support_subseteq` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean#L66))

> Updating a function never grows its support more than adding the key.

```lean
theorem update_support_subseteq (f : α →₀ β) : (f.update a b).support ⊆ f.support ∪ {a}
```

## Depends on

- [DecidableEqZero](../decidableeqzero.md)
- [Finite functions](basic.md)

## Sources

- [Cslib/Foundations/Data/FinFun/Update.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Update.lean)
