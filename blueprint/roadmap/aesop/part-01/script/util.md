---
catalog: module
lean: Aesop.Script.findFirstStep?, Aesop.Script.matchGoals
statement: formalized
proof: formalized
---

# Util

`Aesop.Script.Util`, in [Aesop/Script/Util.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Util.lean), by Jannis Limperg.

`Aesop.Script.findFirstStep?` (definition, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Util.lean#L20))

```lean
def findFirstStep? {α β : Type} (goals : Array α) (step? : α → Option β)
     (stepOrder : β → Nat) : Option (Nat × α × β)
```

`Aesop.Script.matchGoals` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Util.lean#L35))

```lean
def matchGoals (postState₁ postState₂ : Meta.SavedState)
    (goals₁ goals₂ : Array MVarId) : MetaM (Option (Std.HashMap MVarId MVarId))
```

## Depends on

- [EqualUpToIds](../util/equaluptoids.md)

## Proof depends on

- [Util/Basic](../util/basic.md)

## Sources

- [Aesop/Script/Util.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Util.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.Util.json)
