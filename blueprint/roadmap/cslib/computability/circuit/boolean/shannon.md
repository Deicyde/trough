---
catalog: module
lean: Cslib.Circuits.Boolean.Shannon.tendsto_card_computableFunctions_div, Cslib.Circuits.Boolean.Shannon.exists_hard_function, Cslib.Circuits.Boolean.Shannon.lt_complexity
statement: formalized
proof: formalized
---

# Shannon's lower bound for De Morgan circuits

`Cslib.Computability.Circuit.Boolean.Shannon`, in [Cslib/Computability/Circuit/Boolean/Shannon.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Shannon.lean), by Samuel Schlesinger.

> This is the De Morgan specialization of `Cslib.Circuits.Shannon`: almost all Boolean functions
> on `n` inputs require more than `2ⁿ/n` gates, so for large `n` some function does, stated for
> circuits and for circuit complexity. Together with Lupanov's construction, it gives the
> asymptotically sharp gate count `2ⁿ/n`.

`Cslib.Circuits.Boolean.Shannon.tendsto_card_computableFunctions_div` (theorem, [line 28](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Shannon.lean#L28))

> Almost all Boolean functions on `n` inputs require more than `2ⁿ/n` De Morgan gates: the
> fraction computable within that budget tends to zero.

```lean
theorem tendsto_card_computableFunctions_div :
    Tendsto (fun n : ℕ => ((computableFunctions interpretation n (2 ^ n / n)).ncard : ℝ) /
      2 ^ 2 ^ n) atTop (𝓝 0)
```

`Cslib.Circuits.Boolean.Shannon.exists_hard_function` (theorem, [line 36](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Shannon.lean#L36))

> For all sufficiently large `n`, some Boolean function on `n` inputs requires
> more than `2ⁿ/n` De Morgan gates, counting constants and negations.

```lean
theorem exists_hard_function :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : BooleanFunction n,
      ∀ c : Circuit signature n 1,
        c.Computes interpretation (single f) → 2 ^ n / (n : ℝ) < (c.size : ℝ)
```

`Cslib.Circuits.Boolean.Shannon.lt_complexity` (theorem, [line 45](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Shannon.lean#L45))

> Shannon's lower bound for circuit complexity: for all sufficiently large `n`, some Boolean
> function on `n` inputs has complexity more than `2ⁿ/n`.

```lean
theorem lt_complexity :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : BooleanFunction n,
      2 ^ n / (n : ℝ) < (complexity interpretation (single f) : ℝ)
```

## Depends on

- [Completeness of the De Morgan basis](complexity.md)
- [Counting functions computed by finite circuits](../counting.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Proof depends on

- [Shannon's lower bounds for finite carriers](../shannon.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Shannon.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Circuit/Boolean/Shannon.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Circuit.Boolean.Shannon.json)
