---
catalog: module
lean: Lean.getMatchingConstants
statement: formalized
proof: formalized
---

# EnvSearch

`Batteries.Lean.Util.EnvSearch`, in [Batteries/Lean/Util/EnvSearch.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Util/EnvSearch.lean), by Shing Tak Lam, Daniel Selsam, Mario Carneiro.

`Lean.getMatchingConstants` (definition, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Util/EnvSearch.lean#L16))

> Find constants in current environment that match find options and predicate.

```lean
public meta def getMatchingConstants {m} [Monad m] [MonadEnv m]
    (p : ConstantInfo → m Bool)
    (includeImports := true)
    : m (Array ConstantInfo)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Util/EnvSearch.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Util/EnvSearch.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Util.EnvSearch.json)
