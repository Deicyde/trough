---
catalog: module
lean: Aesop.GoalRef.free, Aesop.RappRef.free, Aesop.MVarClusterRef.free, Aesop.freeTree
statement: formalized
proof: formalized
---

# Free

`Aesop.Tree.Free`, in [Aesop/Tree/Free.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean), by Jannis Limperg.

`Aesop.GoalRef.free` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean#L44))

```lean
def GoalRef.free (gref : GoalRef) : BaseIO Unit
```

`Aesop.RappRef.free` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean#L48))

```lean
def RappRef.free (rref : RappRef) : BaseIO Unit
```

`Aesop.MVarClusterRef.free` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean#L52))

```lean
def MVarClusterRef.free (cref : MVarClusterRef) : BaseIO Unit
```

`Aesop.freeTree` (definition, [line 56](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean#L56))

```lean
def freeTree : TreeM Unit
```

## Depends on

- [TreeM](treem.md)

## Sources

- [Aesop/Tree/Free.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Free.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Free.json)
