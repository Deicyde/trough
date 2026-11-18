---
catalog: module
lean: Nat.eventually_mul_pow_le_pow, Nat.eventually_add_one_le_pow_div, Nat.eventually_mul_log_le, Nat.eventually_mul_log2_le
statement: formalized
proof: formalized
---

# Asymptotic bounds on natural numbers

`Cslib.Foundations.Data.Nat.Asymptotics`, in [Cslib/Foundations/Data/Nat/Asymptotics.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean), by Samuel Schlesinger.

> For any natural base greater than one, exponentials eventually dominate fixed multiples of
> powers, and fixed multiples of logarithms are eventually at most the input. The inequalities
> are stated in `ℕ`; the polynomial bound specializes Mathlib's
> `isLittleO_pow_const_const_pow_of_one_lt`.

`Nat.eventually_mul_pow_le_pow` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean#L31))

> Every fixed multiple of a power is eventually at most an exponential of base greater
> than one.

```lean
theorem eventually_mul_pow_le_pow (c k : ℕ) {b : ℕ} (hb : 1 < b) :
    ∀ᶠ n : ℕ in atTop, c * n ^ k ≤ b ^ n
```

`Nat.eventually_add_one_le_pow_div` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean#L41))

> The quotient of an exponential of base greater than one by the input is eventually
> at least the input plus one.

```lean
theorem eventually_add_one_le_pow_div {b : ℕ} (hb : 1 < b) :
    ∀ᶠ n : ℕ in atTop, n + 1 ≤ b ^ n / n
```

`Nat.eventually_mul_log_le` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean#L49))

> Every fixed multiple of the logarithm in a base greater than one is eventually at most
> the input.

```lean
theorem eventually_mul_log_le (c : ℕ) {b : ℕ} (hb : 1 < b) :
    ∀ᶠ n : ℕ in atTop, c * log b n ≤ n
```

`Nat.eventually_mul_log2_le` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean#L59))

> Every fixed multiple of the binary logarithm is eventually at most the input.

```lean
theorem eventually_mul_log2_le (c : ℕ) :
    ∀ᶠ n : ℕ in atTop, c * log2 n ≤ n
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Nat/Asymptotics.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/Asymptotics.lean)
