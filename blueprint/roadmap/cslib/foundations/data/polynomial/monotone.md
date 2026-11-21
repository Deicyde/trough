---
catalog: module
lean: Polynomial.monotone_eval, Polynomial.eval_mono
statement: formalized
proof: formalized
---

# Monotonicity of polynomial evaluation

`Cslib.Foundations.Data.Polynomial.Monotone`, in [Cslib/Foundations/Data/Polynomial/Monotone.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Polynomial/Monotone.lean), by John Jennings, Bolton Bailey.

> Over a canonically ordered semiring (such as `ℕ`), every coefficient of a polynomial is
> nonnegative, so evaluation of the polynomial is a monotone function. This is useful for
> reasoning about polynomial time bounds.

`Polynomial.monotone_eval` (theorem, [line 31](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Polynomial/Monotone.lean#L31))

> Over a canonically ordered semiring, evaluation of a polynomial is monotone.

```lean
theorem monotone_eval : Monotone (fun x : R => p.eval x)
```

`Polynomial.eval_mono` (theorem, [line 39](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Polynomial/Monotone.lean#L39))

> Over a canonically ordered semiring, evaluation of a polynomial preserves `≤`.

```lean
theorem eval_mono {a b : R} (hab : a ≤ b) : p.eval a ≤ p.eval b
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Polynomial/Monotone.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Polynomial/Monotone.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Foundations.Data.Polynomial.Monotone.json)
