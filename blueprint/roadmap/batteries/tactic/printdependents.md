---
catalog: module
lean: Batteries.Tactic.CollectDependents.State, Batteries.Tactic.CollectDependents.M, Batteries.Tactic.CollectDependents.mkState, Batteries.Tactic.CollectDependents.collect
statement: formalized
proof: formalized
---

# `#print dependents` command

`Batteries.Tactic.PrintDependents`, in [Batteries/Tactic/PrintDependents.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean), by Mario Carneiro.

> This is a variation on `#print axioms` where one instead specifies the axioms to avoid,
> and it prints a list of all the theorems in the file that depend on that axiom, and the list
> of all theorems directly referenced that are "to blame" for this dependency. Useful for debugging
> unexpected dependencies.

`Batteries.Tactic.CollectDependents.State` (structure, [line 28](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean#L28))

> Collects the result of a `CollectDependents` query.

```lean
structure State where
  /-- If true, an axiom not in the initial list will be considered as marked. -/
  otherAxiom : Bool := true
  /-- The cached results on visited constants. -/
  result : NameMap Bool := {}
```

`Batteries.Tactic.CollectDependents.M` (abbreviation, [line 35](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean#L35))

> The monad used by `CollectDependents`.

```lean
abbrev M
```

`Batteries.Tactic.CollectDependents.mkState` (definition, [line 43](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean#L43))

> Constructs the initial state, marking the constants in `cs`. The result of `collect` will say
> whether a given declaration depends transitively on one of these constants.
>
> If `otherAxiom` is true, any axiom not specified in `cs` will also be tracked.

```lean
def mkState (cs : Array (Name × Bool)) (otherAxiom := true) : State
```

`Batteries.Tactic.CollectDependents.collect` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean#L47))

> Collect the results for a given constant.

```lean
partial def collect (c : Name) : M Bool
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/PrintDependents.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/PrintDependents.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.PrintDependents.json)
