---
catalog: module
lean: Aesop.Script.UScript.optimize, Aesop.checkAndTraceScript
statement: formalized
proof: formalized
---

# Script/Main

`Aesop.Script.Main`, in [Aesop/Script/Main.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Main.lean), by Jannis Limperg.

`Aesop.Script.UScript.optimize` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Main.lean#L23))

```lean
def UScript.optimize (uscript : UScript) (proofHasMVar : Bool)
    (preState : Meta.SavedState) (goal : MVarId) :
    MetaM (Option (TSyntax ``tacticSeq × ScriptGenerated))
```

`Aesop.checkAndTraceScript` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Main.lean#L65))

```lean
def checkAndTraceScript (uscript : UScript)
    (sscript? : Option (TSyntax ``tacticSeq × ScriptGenerated)) (preState : Meta.SavedState)
    (goal : MVarId) (options : Aesop.Options') (expectCompleteProof : Bool)
    (tacticName : String) :
    m Unit
```

## Depends on

- [Internal](../options/internal.md)
- [Script/Check](check.md)
- [OptimizeSyntax](optimizesyntax.md)
- [SScript](sscript.md)
- [Stats/Basic](../stats/basic.md)

## Proof depends on

- [StructureDynamic](structuredynamic.md)
- [StructureStatic](structurestatic.md)

## Sources

- [Aesop/Script/Main.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/Main.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.Main.json)
