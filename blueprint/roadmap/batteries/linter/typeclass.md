---
catalog: module
lean: Batteries.Linter.impossibleInstance, Batteries.Linter.nonClassInstance, Batteries.Tactic.Lint.impossibleInstance, Batteries.Tactic.Lint.nonClassInstance
statement: formalized
proof: formalized
---

# TypeClass

`Batteries.Linter.TypeClass`, in [Batteries/Linter/TypeClass.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean), by Gabriel Ebner.

`Batteries.Linter.impossibleInstance` (definition, [line 24](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean#L24))

> Lints for instances with arguments that cannot be filled in, like
> ```
> instance {α β : Type} [Group α] : Mul α where ...
> ```

```lean
def impossibleInstance : Linter
```

`Batteries.Linter.nonClassInstance` (definition, [line 49](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean#L49))

> A linter for checking if any declaration whose type is not a class is marked as an instance.

```lean
def nonClassInstance : Linter
```

> Deprecated aliases for the former `Batteries.Tactic.Lint` namespace.

`Batteries.Tactic.Lint.impossibleInstance` (alias, [line 65](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean#L65))

```lean
alias impossibleInstance
```

`Batteries.Tactic.Lint.nonClassInstance` (alias, [line 67](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean#L67))

```lean
alias nonClassInstance
```

## Depends on

- [Basic linter types and attributes](basic.md)

## Sources

- [Batteries/Linter/TypeClass.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Linter/TypeClass.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Linter.TypeClass.json)
