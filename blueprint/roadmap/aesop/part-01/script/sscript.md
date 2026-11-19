---
catalog: module
lean: Aesop.Script.SScript, Aesop.Script.SScript.takeNConsecutiveFocusAndSolve?, Aesop.Script.SScript.render
statement: formalized
proof: formalized
---

# SScript

`Aesop.Script.SScript`, in [Aesop/Script/SScript.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SScript.lean).

`Aesop.Script.SScript` (inductive type, [line 14](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SScript.lean#L14))

```lean
inductive SScript
  | empty
  | onGoal (goalPos : Nat) (step : Step) (tail : SScript)
  | focusAndSolve (goalPos : Nat) (here tail : SScript)
  deriving Inhabited
```

`Aesop.Script.SScript.takeNConsecutiveFocusAndSolve?` (definition, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SScript.lean#L22))

```lean
def takeNConsecutiveFocusAndSolve? (acc : Array SScript) :
    Nat → SScript → Option (Array SScript × SScript)
```

`Aesop.Script.SScript.render` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SScript.lean#L31))

```lean
partial def render (script : SScript) : m (Array Syntax.Tactic)
```

## Depends on

- [Step](step.md)

## Sources

- [Aesop/Script/SScript.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SScript.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.SScript.json)
