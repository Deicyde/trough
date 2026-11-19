---
catalog: module
lean: Aesop.Script.UScript.checkIfEnabled, Aesop.checkRenderedScriptIfEnabled
statement: formalized
proof: formalized
---

# Script/Check

`Aesop.Script.Check`, in [Aesop/Script/Check.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Check.lean), by Jannis Limperg.

`Aesop.Script.UScript.checkIfEnabled` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Check.lean#L18))

```lean
def UScript.checkIfEnabled (uscript : UScript) : MetaM Unit
```

`Aesop.checkRenderedScriptIfEnabled` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Check.lean#L28))

```lean
def checkRenderedScriptIfEnabled (script : TSyntax ``tacticSeq)
    (preState : Meta.SavedState) (goal : MVarId) (expectCompleteProof : Bool) :
    MetaM Unit
```

## Depends on

- [Aesop/Check](../check.md)
- [UScript](uscript.md)

## Sources

- [Aesop/Script/Check.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Check.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.Check.json)
