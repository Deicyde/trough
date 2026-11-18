---
catalog: module
lean: Cslib.Crypto.Negligible, Cslib.Crypto.negligible_iff, Cslib.Crypto.negligible_zero, Cslib.Crypto.Negligible.congr', Cslib.Crypto.Negligible.add, Cslib.Crypto.Negligible.mul, Cslib.Crypto.Negligible.sum, Cslib.Crypto.negligible_of_eventually_le, Cslib.Crypto.negligible_of_le, Cslib.Crypto.Negligible.polynomiallyBounded_mul
statement: formalized
proof: formalized
---

# Negligible functions

`Cslib.Crypto.Negligible`, in [Cslib/Crypto/Negligible.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean), by Samuel Schlesinger.

> Negligible bounds are nonnegative real-valued functions with Mathlib's superpolynomial decay at
> natural security parameters. This module supplies zero, addition, multiplication, fixed finite
> sums, eventual comparison, and polynomial-loss bounds for security games. Changing finitely many
> values preserves negligibility.
>
> The decay bound may depend on the whole algorithm. Security definitions quantify over that
> algorithm before asserting negligibility; this module does not change that quantifier order.

`Cslib.Crypto.Negligible` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L33))

> An advantage is negligible when it decays faster than every inverse polynomial in the
> security parameter. The nonnegative codomain records that advantages are magnitudes;
> the decay condition is Mathlib's superpolynomial decay in the nonnegative reals.

```lean
def Negligible (ε : ℕ → ℝ≥0) : Prop
```

`Cslib.Crypto.negligible_iff` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L36))

```lean
theorem negligible_iff (ε : ℕ → ℝ≥0) :
    Negligible ε ↔ ∀ k : ℕ, ∀ δ > (0 : ℝ≥0), ∃ m : ℕ, ∀ n ≥ m, n ^ k * ε n < δ
```

`Cslib.Crypto.negligible_zero` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L41))

> The zero advantage is negligible.

```lean
theorem negligible_zero : Negligible (fun _ => 0)
```

`Cslib.Crypto.Negligible.congr'` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L46))

> Changing the value of a negligible bound at finitely many security parameters preserves
> negligibility.

```lean
theorem Negligible.congr' {ε δ : ℕ → ℝ≥0} (hε : Negligible ε)
    (h : ε =ᶠ[Filter.atTop] δ) : Negligible δ
```

`Cslib.Crypto.Negligible.add` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L51))

> The sum of two negligible bounds is negligible.

```lean
theorem Negligible.add {ε δ : ℕ → ℝ≥0} (hε : Negligible ε) (hδ : Negligible δ) :
    Negligible (ε + δ)
```

`Cslib.Crypto.Negligible.mul` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L56))

> The product of two negligible bounds is negligible.

```lean
theorem Negligible.mul {ε δ : ℕ → ℝ≥0} (hε : Negligible ε) (hδ : Negligible δ) :
    Negligible (ε * δ)
```

`Cslib.Crypto.Negligible.sum` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L61))

> A sum over a fixed finite set of negligible bounds is negligible.

```lean
theorem Negligible.sum {ι : Type*} (s : Finset ι) {ε : ι → ℕ → ℝ≥0}
    (hε : ∀ i ∈ s, Negligible (ε i)) : Negligible (∑ i ∈ s, ε i)
```

`Cslib.Crypto.negligible_of_eventually_le` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L66))

> An eventually smaller advantage is negligible.

```lean
theorem negligible_of_eventually_le {ε δ : ℕ → ℝ≥0} (hδ : Negligible δ)
    (hle : ε ≤ᶠ[Filter.atTop] δ) : Negligible ε
```

`Cslib.Crypto.negligible_of_le` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L71))

> A pointwise smaller advantage is negligible.

```lean
theorem negligible_of_le {ε δ : ℕ → ℝ≥0} (hδ : Negligible δ)
    (hle : ∀ n, ε n ≤ δ n) : Negligible ε
```

`Cslib.Crypto.Negligible.polynomiallyBounded_mul` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean#L76))

> Polynomially bounded factors preserve negligible decay.

```lean
theorem Negligible.polynomiallyBounded_mul {ε : ℕ → ℝ≥0} {p : ℕ → ℕ}
    (hε : Negligible ε) (hp : PolynomiallyBounded p) :
    Negligible (fun n => (p n : ℝ≥0) * ε n)
```

## Depends on

- [Polynomial bounds on natural-valued functions](../foundations/data/nat/polynomialbound.md)

## Sources

- [Cslib/Crypto/Negligible.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Crypto/Negligible.lean)
