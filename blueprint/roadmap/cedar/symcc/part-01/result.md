---
catalog: module
lean: Cedar.SymCC.Error, Cedar.SymCC.Result, Cedar.SymCC.coeResult
statement: formalized
proof: formalized
---

# Result

`Cedar.SymCC.Result`, in [Cedar/SymCC/Result.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Result.lean).

> This file defines the Result type for symbolic compilation.

`Cedar.SymCC.Error` (inductive type, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Result.lean#L25))

```lean
public inductive Error where
  | noSuchEntityType
  | noSuchAttribute
  | typeError
  | unsupportedError
```

`Cedar.SymCC.Result` (abbreviation, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Result.lean#L31))

```lean
public abbrev Result (α)
```

`Cedar.SymCC.coeResult` (instance, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Result.lean#L35))

```lean
public instance coeResult : Coe α (Result α)
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/SymCC/Result.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Result.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Result.json)
