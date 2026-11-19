---
catalog: module
lean: Batteries.panicWith, Batteries.panicWith_eq
statement: formalized
proof: formalized
---

# Panic

`Batteries.Util.Panic`, in [Batteries/Util/Panic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Panic.lean), by François G. Dorais.

`Batteries.panicWith` (definition, [line 13](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Panic.lean#L13))

> Panic with a specific default value `v`.

```lean
def panicWith (v : α) (msg : String) : α
```

`Batteries.panicWith_eq` (theorem, [line 15](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Panic.lean#L15))

```lean
theorem panicWith_eq (v : α) (msg) : panicWith v msg = v
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/Panic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Util/Panic.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.Panic.json)
