---
catalog: module
lean: Batteries.Tactic.Lint.impossibleInstance, Batteries.Tactic.Lint.nonClassInstance
statement: formalized
proof: formalized
---

# TypeClass

`Batteries.Tactic.Lint.TypeClass`, in [Batteries/Tactic/Lint/TypeClass.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/TypeClass.lean), by Gabriel Ebner.

`Batteries.Tactic.Lint.impossibleInstance` (definition, [line 23](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/TypeClass.lean#L23))

> Lints for instances with arguments that cannot be filled in, like
> ```
> instance {α β : Type} [Group α] : Mul α where ...
> ```

```lean
def impossibleInstance : Linter
```

`Batteries.Tactic.Lint.nonClassInstance` (definition, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/TypeClass.lean#L48))

> A linter for checking if any declaration whose type is not a class is marked as an instance.

```lean
def nonClassInstance : Linter
```

## Depends on

- [Basic linter types and attributes](basic.md)

## Sources

- [Batteries/Tactic/Lint/TypeClass.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Tactic/Lint/TypeClass.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Tactic.Lint.TypeClass.json)
