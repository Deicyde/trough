---
catalog: module
lean: List.waitAll
statement: formalized
proof: formalized
---

# Functions for manipulating a list of tasks

`Batteries.Lean.System.IO`, in [Batteries/Lean/System/IO.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/System/IO.lean), by Kim Morrison.

> * `IO.waitAny'` is a wrapper for `IO.waitAny` that also returns the remaining tasks.
> * `List.waitAll : List (Task α) → Task (List α)` gathers a list of tasks into a task returning
>   the list of all results.

`List.waitAll` (definition, [line 28](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/System/IO.lean#L28))

> Given a list of tasks, create the task returning the list of results,
> by waiting for each.

```lean
def List.waitAll (tasks : List (Task α)) : Task (List α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/System/IO.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/System/IO.lean)
