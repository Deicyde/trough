---
catalog: module
lean: Cslib.Circuits.Boolean.Shannon.exists_hard_function, Cslib.Circuits.Boolean.Shannon.lt_complexity
statement: formalized
proof: formalized
---

# Shannon's lower bound for De Morgan circuits

`Cslib.Computability.Circuit.Boolean.Shannon`, in [Cslib/Computability/Circuit/Boolean/Shannon.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Shannon.lean), by Samuel Schlesinger.

> This is the De Morgan specialization of `Cslib.Circuits.Shannon.exists_hard_function`,
> stated for circuits and for circuit complexity. Together with Lupanov's construction, it
> gives the asymptotically sharp gate count `2ⁿ/n`.

`Cslib.Circuits.Boolean.Shannon.exists_hard_function` (theorem, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Shannon.lean#L25))

> For all sufficiently large `n`, some Boolean function on `n` inputs requires
> more than `2ⁿ/n` De Morgan gates, counting constants and negations.

```lean
theorem exists_hard_function :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : BooleanFunction n,
      ∀ c : Circuit signature n 1,
        c.Computes interpretation (single f) → 2 ^ n / (n : ℝ) < (c.size : ℝ)
```

`Cslib.Circuits.Boolean.Shannon.lt_complexity` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Shannon.lean#L34))

> Shannon's lower bound for circuit complexity: for all sufficiently large `n`, some Boolean
> function on `n` inputs has complexity more than `2ⁿ/n`.

```lean
theorem lt_complexity :
    ∃ N : ℕ, ∀ n ≥ N, ∃ f : BooleanFunction n,
      2 ^ n / (n : ℝ) < (complexity interpretation (single f) : ℝ)
```

## Depends on

- [Completeness of the De Morgan basis](complexity.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Proof depends on

- [Shannon's lower bound for finite carriers and binary bases](../shannon.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Shannon.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Shannon.lean)
