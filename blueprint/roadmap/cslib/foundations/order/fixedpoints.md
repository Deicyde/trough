---
catalog: module
lean: OrderHom.nextFixed_bot_coe, OrderHom.prevFixed_top_coe, OrderHom.nextFixed_le_of_map_le, OrderHom.le_prevFixed_of_map_ge, OrderHom.nextFixed_induction, OrderHom.prevFixed_induction
statement: formalized
proof: formalized
---

# Extensions to Mathlib's fixed point API

`Cslib.Foundations.Order.FixedPoints`, in [Cslib/Foundations/Order/FixedPoints.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean), by Thomas Waring.

`OrderHom.nextFixed_bot_coe` (theorem, [line 20](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L20))

```lean
theorem nextFixed_bot_coe : ↑(f.nextFixed ⊥ bot_le) = f.lfp
```

`OrderHom.prevFixed_top_coe` (theorem, [line 23](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L23))

```lean
theorem prevFixed_top_coe : ↑(f.prevFixed ⊤ le_top) = f.gfp
```

`OrderHom.nextFixed_le_of_map_le` (theorem, [line 27](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L27))

> Generalisation of `OrderHom.nextFixed_le` to prefixed points.

```lean
theorem nextFixed_le_of_map_le {x y : α} (hx : x ≤ f x) (hxy : x ≤ y) (hy : f y ≤ y) :
    ↑(f.nextFixed x hx) ≤ y
```

`OrderHom.le_prevFixed_of_map_ge` (theorem, [line 33](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L33))

> Generalisation of `OrderHom.le_prevFixed` to postfixed points.

```lean
theorem le_prevFixed_of_map_ge {x y : α} (hx : f x ≤ x) (hxy : y ≤ x) (hy : y ≤ f y) :
    y ≤ f.prevFixed x hx
```

`OrderHom.nextFixed_induction` (theorem, [line 39](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L39))

> Analogue of `OrderHom.lfp_induction` for `OrderHom.nextFixed`.

```lean
theorem nextFixed_induction {x : α} (hx : x ≤ f x) {p : α → Prop} (base : p x)
    (step : ∀ a, p a → x ≤ a → a ≤ f.nextFixed x hx → p (f a))
    (hSup : ∀ s, (∀ a ∈ s, p a) → p (sSup s)) : p (f.nextFixed x hx)
```

`OrderHom.prevFixed_induction` (theorem, [line 53](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean#L53))

> Analogue of `OrderHom.gfp_induction` for `OrderHom.prevFixed`.

```lean
theorem prevFixed_induction {x : α} (hx : f x ≤ x) {p : α → Prop} (base : p x)
    (step : ∀ a, p a → a ≤ x → f.prevFixed x hx ≤ a → p (f a))
    (hInf : ∀ s, (∀ a ∈ s, p a) → p (sInf s)) : p (f.prevFixed x hx)
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Order/FixedPoints.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Order/FixedPoints.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Order.FixedPoints.json)
