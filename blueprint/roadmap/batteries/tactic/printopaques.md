---
catalog: module
lean: Batteries.Tactic.CollectOpaques.State, Batteries.Tactic.CollectOpaques.M, Batteries.Tactic.CollectOpaques.collect
statement: formalized
proof: formalized
---

# PrintOpaques

`Batteries.Tactic.PrintOpaques`, in [Batteries/Tactic/PrintOpaques.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintOpaques.lean), by Mario Carneiro.

`Batteries.Tactic.CollectOpaques.State` (structure, [line 19](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintOpaques.lean#L19))

> Collects the result of a `CollectOpaques` query.

```lean
structure State where
  /-- The set visited constants. -/
  visited : NameSet := {}
  /-- The collected opaque defs. -/
  opaques : Array Name := #[]
```

`Batteries.Tactic.CollectOpaques.M` (abbreviation, [line 26](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintOpaques.lean#L26))

> The monad used by `CollectOpaques`.

```lean
abbrev M
```

`Batteries.Tactic.CollectOpaques.collect` (definition, [line 29](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintOpaques.lean#L29))

> Collect the results for a given constant.

```lean
partial def collect (c : Name) : M Unit
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/PrintOpaques.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Tactic/PrintOpaques.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.PrintOpaques.json)
