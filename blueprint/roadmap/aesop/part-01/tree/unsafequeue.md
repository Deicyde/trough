---
catalog: module
lean: Aesop.PostponedSafeRule, Aesop.PostponedSafeRule.toUnsafeRule, Aesop.UnsafeQueueEntry, Aesop.UnsafeQueueEntry.successProbability, Aesop.UnsafeQueueEntry.name, Aesop.UnsafeQueue, Aesop.UnsafeQueue.initial, Aesop.UnsafeQueue.entriesToMessageData
statement: formalized
proof: formalized
---

# UnsafeQueue

`Aesop.Tree.UnsafeQueue`, in [Aesop/Tree/UnsafeQueue.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean), by Jannis Limperg.

`Aesop.PostponedSafeRule` (structure, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L17))

```lean
structure PostponedSafeRule where
  rule : SafeRule
  output : RuleTacOutput
  deriving Inhabited
```

`Aesop.PostponedSafeRule.toUnsafeRule` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L24))

```lean
def toUnsafeRule (r : PostponedSafeRule) : UnsafeRule
```

`Aesop.UnsafeQueueEntry` (inductive type, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L30))

```lean
inductive UnsafeQueueEntry
  | unsafeRule (r : IndexMatchResult UnsafeRule)
  | postponedSafeRule (r : PostponedSafeRule)
  deriving Inhabited
```

`Aesop.UnsafeQueueEntry.successProbability` (definition, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L42))

```lean
def successProbability : UnsafeQueueEntry → Percent
```

`Aesop.UnsafeQueueEntry.name` (definition, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L46))

```lean
def name : UnsafeQueueEntry → RuleName
```

`Aesop.UnsafeQueue` (definition, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L58))

```lean
def UnsafeQueue
```

`Aesop.UnsafeQueue.initial` (definition, [line 70](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L70))

```lean
def initial (postponedSafeRules : Array PostponedSafeRule)
    (unsafeRules : Array (IndexMatchResult UnsafeRule)) : UnsafeQueue
```

`Aesop.UnsafeQueue.entriesToMessageData` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean#L78))

```lean
def entriesToMessageData (q : UnsafeQueue) : Array MessageData
```

## Depends on

- [Constants](../constants.md)
- [Rule](../../part-02/rule.md)

## Sources

- [Aesop/Tree/UnsafeQueue.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/UnsafeQueue.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.UnsafeQueue.json)
