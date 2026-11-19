---
catalog: module
lean: Aesop.BestFirstQueue.ActiveGoal, Aesop.BestFirstQueue.ActiveGoal.le, Aesop.BestFirstQueue.ActiveGoal.ofGoalRef, Aesop.BestFirstQueue, Aesop.BestFirstQueue.init, Aesop.BestFirstQueue.addGoals, Aesop.BestFirstQueue.popGoal, Aesop.LIFOQueue, Aesop.LIFOQueue.init, Aesop.LIFOQueue.addGoals, Aesop.LIFOQueue.popGoal, Aesop.FIFOQueue, Aesop.FIFOQueue.init, Aesop.FIFOQueue.addGoals, Aesop.FIFOQueue.popGoal, Aesop.Options.queue
statement: formalized
proof: formalized
---

# Queue

`Aesop.Search.Queue`, in [Aesop/Search/Queue.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean), by Jannis Limperg.

`Aesop.BestFirstQueue.ActiveGoal` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L18))

```lean
structure ActiveGoal where
  goal : GoalRef
  priority : Percent
  lastExpandedInIteration : Iteration
    -- Iteration of the search loop when this goal was last expanded (counting
    -- from 1), or 0 if the goal was never expanded.
  addedInIteration : Iteration
```

`Aesop.BestFirstQueue.ActiveGoal.le` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L41))

```lean
protected def le (g h : ActiveGoal) : Bool
```

`Aesop.BestFirstQueue.ActiveGoal.ofGoalRef` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L48))

```lean
protected def ofGoalRef (gref : GoalRef) : BaseIO ActiveGoal
```

`Aesop.BestFirstQueue` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L59))

```lean
def BestFirstQueue
```

`Aesop.BestFirstQueue.init` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L64))

```lean
protected def init : BestFirstQueue
```

`Aesop.BestFirstQueue.addGoals` (definition, [line 67](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L67))

```lean
protected def addGoals (q : BestFirstQueue) (grefs : Array GoalRef) :
    BaseIO BestFirstQueue
```

`Aesop.BestFirstQueue.popGoal` (definition, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L72))

```lean
protected def popGoal (q : BestFirstQueue) : Option GoalRef × BestFirstQueue
```

`Aesop.LIFOQueue` (structure, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L85))

```lean
structure LIFOQueue where
  goals : Array GoalRef
```

`Aesop.LIFOQueue.init` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L90))

```lean
protected def init : LIFOQueue
```

`Aesop.LIFOQueue.addGoals` (definition, [line 93](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L93))

```lean
protected def addGoals (q : LIFOQueue) (grefs : Array GoalRef) : LIFOQueue
```

`Aesop.LIFOQueue.popGoal` (definition, [line 96](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L96))

```lean
protected def popGoal (q : LIFOQueue) : Option GoalRef × LIFOQueue
```

`Aesop.FIFOQueue` (structure, [line 109](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L109))

```lean
structure FIFOQueue where
  goals : Array GoalRef
  pos : Nat
```

`Aesop.FIFOQueue.init` (definition, [line 115](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L115))

```lean
protected def init : FIFOQueue
```

`Aesop.FIFOQueue.addGoals` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L118))

```lean
protected def addGoals (q : FIFOQueue) (grefs : Array GoalRef) : FIFOQueue
```

`Aesop.FIFOQueue.popGoal` (definition, [line 121](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L121))

```lean
protected def popGoal (q : FIFOQueue) : Option GoalRef × FIFOQueue
```

`Aesop.Options.queue` (definition, [line 134](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean#L134))

```lean
def Options.queue (opts : Aesop.Options) : Σ Q, Queue Q
```

## Depends on

- [Class](queue-2/class.md)

## Sources

- [Aesop/Search/Queue.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Queue.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Search.Queue.json)
