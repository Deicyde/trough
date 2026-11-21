---
catalog: module
lean: Bool.lt_wfRel, Bool.gt_wfRel
statement: formalized
proof: formalized
---

# Bool

`Batteries.Data.Bool`, in [Batteries/Data/Bool.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Bool.lean), by Chad Sharp.

> This file contains `WellFoundedRelation` instances `Bool`.
>
> They are provided as defs rather than instances, despite WellFoundedRelation being a class, as we
> provide versions for both < and >. If you need instances, you may use the WellFoundedLT and
> WellFoundedGT classes available in Mathlib.

`Bool.lt_wfRel` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Bool.lean#L20))

> Boolean '<' is well founded

```lean
def Bool.lt_wfRel : WellFoundedRelation Bool
```

`Bool.gt_wfRel` (definition, [line 28](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Bool.lean#L28))

> Boolean '>' is well founded

```lean
def Bool.gt_wfRel : WellFoundedRelation Bool
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Bool.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Bool.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.Bool.json)
