---
catalog: module
lean: Cslib.Circuits.Boolean.computableFunctions, Cslib.Circuits.Boolean.mem_computableFunctions, Cslib.Circuits.Boolean.card_computableFunctions_mul_factorial_le
statement: formalized
proof: formalized
---

# Counting De Morgan circuits

`Cslib.Computability.Circuit.Boolean.Counting`, in [Cslib/Computability/Circuit/Boolean/Counting.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Counting.lean), by Samuel Schlesinger.

> This file specializes the generic circuit counting bound to the five De Morgan operations,
> all of arity at most two. The resulting factorial correction is used in Shannon's lower bound.

`Cslib.Circuits.Boolean.computableFunctions` (abbreviation, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Counting.lean#L27))

> Boolean functions on `n` inputs computable with at most `s` De Morgan gates.

```lean
noncomputable abbrev computableFunctions (n s : ℕ) : Finset (BooleanFunction n)
```

`Cslib.Circuits.Boolean.mem_computableFunctions` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Counting.lean#L30))

```lean
theorem mem_computableFunctions {f : BooleanFunction n} :
    f ∈ computableFunctions n s ↔
      ∃ c : Circuit signature n 1, c.Computes interpretation (single f) ∧ c.size ≤ s
```

`Cslib.Circuits.Boolean.card_computableFunctions_mul_factorial_le` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Counting.lean#L36))

> The De Morgan counting bound, accounting for gate relabelings.

```lean
theorem card_computableFunctions_mul_factorial_le (n s : ℕ) :
    (computableFunctions n s).card * s.factorial ≤
      (s + 1) * (5 * (n + s + 1) ^ 2) ^ s * (n + s)
```

## Depends on

- [Boolean circuits](basic.md)
- [Counting functions computed by finite circuits](../counting.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Counting.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Counting.lean)
