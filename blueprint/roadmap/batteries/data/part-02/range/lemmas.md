---
catalog: module
lean: Std.Legacy.Range.size_stop_le_start, Std.Legacy.Range.size_step_1
statement: formalized
proof: formalized
---

# Range/Lemmas

`Batteries.Data.Range.Lemmas`, in [Batteries/Data/Range/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Range/Lemmas.lean), by Mario Carneiro.

`Std.Legacy.Range.size_stop_le_start` (theorem, [line 12](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Range/Lemmas.lean#L12))

```lean
theorem size_stop_le_start : ∀ r : Range, r.stop ≤ r.start → r.size = 0
```

`Std.Legacy.Range.size_step_1` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Range/Lemmas.lean#L17))

```lean
theorem size_step_1 (start stop) : size ⟨start, stop, 1, by decide⟩ = stop - start
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Range/Lemmas.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Range/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Range.Lemmas.json)
