---
catalog: module
lean: Cslib.PolynomiallyBounded, Cslib.polynomiallyBounded_iff_isBigO, Cslib.polynomiallyBounded_iff_le
statement: formalized
proof: formalized
---

# Polynomial bounds on natural-valued functions

`Cslib.Foundations.Data.Nat.PolynomialBound`, in [Cslib/Foundations/Data/Nat/PolynomialBound.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/PolynomialBound.lean), by Samuel Schlesinger.

> `PolynomiallyBounded f` means that `f n ≤ n ^ d` eventually, for some fixed degree `d`.
> This is equivalent to a real-valued `IsBigO` bound and to a bound `c * (n + 1) ^ d`
> at every input. It is a growth condition and does not assert computability.

`Cslib.PolynomiallyBounded` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/PolynomialBound.lean#L29))

> A function is polynomially bounded if a fixed power eventually bounds its values.

```lean
def PolynomiallyBounded (f : ℕ → ℕ) : Prop
```

`Cslib.polynomiallyBounded_iff_isBigO` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/PolynomialBound.lean#L33))

> Polynomial growth is equivalent to a big-O bound after casting to the reals.

```lean
theorem polynomiallyBounded_iff_isBigO {f : ℕ → ℕ} :
    PolynomiallyBounded f ↔
      ∃ d : ℕ, (fun n => (f n : ℝ)) =O[atTop] (fun n => (n : ℝ) ^ d)
```

`Cslib.polynomiallyBounded_iff_le` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/PolynomialBound.lean#L49))

> A polynomial bound can absorb every finite prefix into its constant factor.

```lean
theorem polynomiallyBounded_iff_le {f : ℕ → ℕ} :
    PolynomiallyBounded f ↔ ∃ c d : ℕ, ∀ n, f n ≤ c * (n + 1) ^ d
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/Nat/PolynomialBound.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/Nat/PolynomialBound.lean)
