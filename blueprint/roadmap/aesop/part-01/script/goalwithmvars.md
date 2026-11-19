---
catalog: module
lean: Aesop.GoalWithMVars, Aesop.GoalWithMVars.ofMVarId
statement: formalized
proof: formalized
---

# GoalWithMVars

`Aesop.Script.GoalWithMVars`, in [Aesop/Script/GoalWithMVars.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/GoalWithMVars.lean).

`Aesop.GoalWithMVars` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/GoalWithMVars.lean#L12))

```lean
structure GoalWithMVars where
  goal : MVarId
  mvars : Std.HashSet MVarId
  deriving Inhabited
```

`Aesop.GoalWithMVars.ofMVarId` (definition, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/GoalWithMVars.lean#L26))

```lean
def ofMVarId (goal : MVarId) : MetaM GoalWithMVars
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Script/GoalWithMVars.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/GoalWithMVars.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.GoalWithMVars.json)
