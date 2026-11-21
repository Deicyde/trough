---
catalog: module
lean: List.waitAll
statement: formalized
proof: formalized
---

# Functions for manipulating a list of tasks

`Batteries.Lean.System.IO`, in [Batteries/Lean/System/IO.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/System/IO.lean), by Kim Morrison.

> * `IO.waitAny'` is a wrapper for `IO.waitAny` that also returns the remaining tasks.
> * `List.waitAll : List (Task α) → Task (List α)` gathers a list of tasks into a task returning
>   the list of all results.

`List.waitAll` (definition, [line 28](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/System/IO.lean#L28))

> Given a list of tasks, create the task returning the list of results,
> by waiting for each.

```lean
def List.waitAll (tasks : List (Task α)) : Task (List α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/System/IO.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/System/IO.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.System.IO.json)
