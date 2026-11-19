---
catalog: module
lean: Aesop.Goal.stats, Aesop.collectGoalStatsIfEnabled
statement: formalized
proof: formalized
---

# Stats

`Aesop.Tree.Stats`, in [Aesop/Tree/Stats.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Stats.lean), by Jannis Limperg.

`Aesop.Goal.stats` (definition, [line 15](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Stats.lean#L15))

```lean
def Goal.stats (g : Goal) : TreeM GoalStats
```

`Aesop.collectGoalStatsIfEnabled` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Stats.lean#L28))

```lean
def collectGoalStatsIfEnabled : TreeM Unit
```

## Depends on

- [Traversal](traversal.md)
- [TreeM](treem.md)

## Sources

- [Aesop/Tree/Stats.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Stats.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Stats.json)
