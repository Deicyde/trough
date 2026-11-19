---
catalog: module
lean: Aesop.Script.StepTree, Aesop.Script.StepTree.toMessageData?, Aesop.Script.StepTree.toMessageData, Aesop.Script.UScript.toStepTree, Aesop.Script.sortDedupArrays, Aesop.Script.isConsecutiveSequence, Aesop.Script.StepTree.focusableGoals, Aesop.Script.StepTree.numSiblings, Aesop.Script.orderedUScriptToSScript
statement: formalized
proof: formalized
---

# UScriptToSScript

`Aesop.Script.UScriptToSScript`, in [Aesop/Script/UScriptToSScript.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean), by Jannis Limperg.

`Aesop.Script.StepTree` (inductive type, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L17))

```lean
inductive StepTree where
  | empty
  | node (step : Step) (index : Nat) (children : Array StepTree)
  deriving Nonempty
```

`Aesop.Script.StepTree.toMessageData?` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L24))

```lean
protected partial def toMessageData? : StepTree → Option MessageData
```

`Aesop.Script.StepTree.toMessageData` (definition, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L29))

```lean
protected def toMessageData (t : StepTree) : MessageData
```

`Aesop.Script.UScript.toStepTree` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L37))

```lean
partial def UScript.toStepTree (s : UScript) : StepTree
```

`Aesop.Script.sortDedupArrays` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L52))

```lean
def sortDedupArrays [Ord α] (as : Array (Array α)) : Array α
```

`Aesop.Script.isConsecutiveSequence` (definition, [line 57](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L57))

```lean
def isConsecutiveSequence (ns : Array Nat) : Bool
```

`Aesop.Script.StepTree.focusableGoals` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L68))

```lean
partial def focusableGoals (t : StepTree) : Std.HashMap MVarId Nat
```

`Aesop.Script.StepTree.numSiblings` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L82))

```lean
partial def numSiblings (t : StepTree) : Std.HashMap MVarId Nat
```

`Aesop.Script.orderedUScriptToSScript` (definition, [line 94](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean#L94))

```lean
partial def orderedUScriptToSScript (uscript : UScript) (tacticState : TacticState) : CoreM SScript
```

## Depends on

- [SScript](sscript.md)
- [UScript](uscript.md)

## Sources

- [Aesop/Script/UScriptToSScript.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/UScriptToSScript.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.UScriptToSScript.json)
