---
catalog: module
lean: MLList.whileAtLeastHeartbeatsPercent
statement: formalized
proof: formalized
---

# Truncate a `MLList` when running out of available heartbeats

`Batteries.Data.MLList.Heartbeats`, in [Batteries/Data/MLList/Heartbeats.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Heartbeats.lean), by Kim Morrison.

`MLList.whileAtLeastHeartbeatsPercent` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Heartbeats.lean#L30))

> Take an initial segment of a monadic lazy list,
> stopping when there is less than `percent` of the remaining allowed heartbeats.
>
> If `getMaxHeartbeats` returns `0`, then this passes through the original list unmodified.
>
> The `initial` heartbeat counter is recorded when the first element of the list is requested.
> Then each time an element is requested from the wrapped list the heartbeat counter is checked, and
> if `current * 100 / initial < percent` then that element is returned,
> but no further elements.

```lean
def MLList.whileAtLeastHeartbeatsPercent [Monad m] [MonadLiftT CoreM m]
    (L : MLList m α) (percent : Nat := 10) : MLList m α
```

## Depends on

- [Monadic lazy lists](basic.md)

## Sources

- [Batteries/Data/MLList/Heartbeats.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/MLList/Heartbeats.lean)
