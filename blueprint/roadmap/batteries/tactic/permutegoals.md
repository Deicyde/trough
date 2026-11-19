---
catalog: module
lean: Batteries.Tactic.elabGoalNum
statement: formalized
proof: formalized
---

# The `on_goal`, `pick_goal`, and `swap` tactics

`Batteries.Tactic.PermuteGoals`, in [Batteries/Tactic/PermuteGoals.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/PermuteGoals.lean), by Arthur Paulino, Mario Carneiro.

> `pick_goal n` moves the `n`-th goal to the front. If `n` is negative this is counted from the back.
>
> `on_goal n => tacSeq` focuses on the `n`-th goal and runs a tactic block `tacSeq`.
> If `tacSeq` does not close the goal any resulting subgoals are inserted back into the list of goals.
> If `n` is negative this is counted from the back.
>
> `swap` is a shortcut for `pick_goal 2`, which interchanges the 1st and 2nd goals.

`Batteries.Tactic.elabGoalNum` (definition, [line 34](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/PermuteGoals.lean#L34))

> Turn the given `goalNum` syntax into a (zero-based) index in the current `getGoals` list.

```lean
def elabGoalNum (goalNum : Syntax) : TacticM Nat
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/PermuteGoals.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/PermuteGoals.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.PermuteGoals.json)
