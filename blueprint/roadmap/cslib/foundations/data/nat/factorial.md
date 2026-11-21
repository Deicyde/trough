---
catalog: module
lean: Nat.mul_log_sub_le_log_factorial
statement: formalized
proof: formalized
---

# A logarithmic lower bound for the factorial

`Cslib.Foundations.Data.Nat.Factorial`, in [Cslib/Foundations/Data/Nat/Factorial.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Nat/Factorial.lean), by Samuel Schlesinger.

> Bounding one term of the exponential series gives `n log n - n ≤ log (n!)`, including at zero.

`Nat.mul_log_sub_le_log_factorial` (theorem, [line 22](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Nat/Factorial.lean#L22))

> The logarithm of the factorial is at least `n log n - n`.

```lean
theorem mul_log_sub_le_log_factorial (n : ℕ) :
    (n : ℝ) * Real.log n - n ≤ Real.log n.factorial
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Nat/Factorial.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Foundations/Data/Nat/Factorial.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Foundations.Data.Nat.Factorial.json)
