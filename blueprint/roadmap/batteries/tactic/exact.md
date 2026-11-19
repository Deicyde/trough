---
catalog: module
lean: Lean.MVarId.assignIfDefEq
statement: formalized
proof: formalized
---

# `exact` tactic (`MetaM` version)

`Batteries.Tactic.Exact`, in [Batteries/Tactic/Exact.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Exact.lean), by Mario Carneiro.

`Lean.MVarId.assignIfDefEq` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Exact.lean#L20))

> `MetaM` version of `Lean.Elab.Tactic.evalExact`: add `mvarId := x` to the metavariable assignment.
> This method wraps `Lean.MVarId.assign`, checking whether `mvarId` is already assigned, and whether
> the expression has the right type.

```lean
def Lean.MVarId.assignIfDefEq (g : MVarId) (e : Expr) : MetaM Unit
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/Exact.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Exact.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.Exact.json)
