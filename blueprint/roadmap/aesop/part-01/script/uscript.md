---
catalog: module
lean: Aesop.Script.UScript, Aesop.Script.UScript.render, Aesop.Script.UScript.renderTacticSeq, Aesop.Script.UScript.validate
statement: formalized
proof: formalized
---

# UScript

`Aesop.Script.UScript`, in [Aesop/Script/UScript.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean), by Jannis Limperg.

`Aesop.Script.UScript` (abbreviation, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean#L18))

```lean
abbrev UScript
```

`Aesop.Script.UScript.render` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean#L23))

```lean
def render (tacticState : TacticState) (s : UScript) :
    m (Array Syntax.Tactic)
```

`Aesop.Script.UScript.renderTacticSeq` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean#L33))

```lean
def renderTacticSeq (uscript : UScript) (preState : Meta.SavedState)
    (goal : MVarId) : MetaM (TSyntax ``tacticSeq)
```

`Aesop.Script.UScript.validate` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean#L38))

```lean
def validate (s : UScript) : MetaM Unit
```

## Depends on

- [Step](step.md)

## Sources

- [Aesop/Script/UScript.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScript.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.UScript.json)
