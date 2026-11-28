---
catalog: module
lean: MLList.ofTaskList
statement: formalized
proof: formalized
---

# IO operations using monadic lazy lists

`Batteries.Data.MLList.IO`, in [Batteries/Data/MLList/IO.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/MLList/IO.lean), by Kim Morrison.

`MLList.ofTaskList` (definition, [line 22](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/MLList/IO.lean#L22))

> Give a list of tasks, return the monadic lazy list which
> returns the values as they become available.

```lean
def ofTaskList (tasks : List (Task α)) : MLList BaseIO α
```

## Depends on

- [Monadic lazy lists](basic.md)

## Sources

- [Batteries/Data/MLList/IO.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/MLList/IO.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.MLList.IO.json)
