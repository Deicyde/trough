---
catalog: module
lean: Aesop.Queue, Aesop.Queue.init'
statement: formalized
proof: formalized
---

# Class

`Aesop.Search.Queue.Class`, in [Aesop/Search/Queue/Class.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue/Class.lean), by Jannis Limperg.

`Aesop.Queue` (class, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue/Class.lean#L16))

```lean
class Queue (Q : Type) where
  init : BaseIO Q
  addGoals : Q → Array GoalRef → BaseIO Q
  popGoal : Q → BaseIO (Option GoalRef × Q)
```

`Aesop.Queue.init'` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue/Class.lean#L23))

```lean
def init' [Queue Q] (grefs : Array GoalRef) : BaseIO Q
```

## Depends on

- [Data](../../tree/data.md)

## Sources

- [Aesop/Search/Queue/Class.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue/Class.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Search.Queue.Class.json)
