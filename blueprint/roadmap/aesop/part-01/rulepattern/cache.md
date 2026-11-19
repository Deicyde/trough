---
catalog: module
lean: Aesop.RulePatternCache.Entry, Aesop.RulePatternCache
statement: formalized
proof: formalized
---

# Cache

`Aesop.RulePattern.Cache`, in [Aesop/RulePattern/Cache.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern/Cache.lean), by Jannis Limperg.

`Aesop.RulePatternCache.Entry` (definition, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern/Cache.lean#L20))

> Entry of the rule pattern cache.

```lean
def RulePatternCache.Entry
```

`Aesop.RulePatternCache` (structure, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern/Cache.lean#L24))

> A cache for the rule pattern index.

```lean
structure RulePatternCache where
  map : Std.HashMap Expr RulePatternCache.Entry
  deriving Inhabited
```

## Depends on

- [Substitution](../forward/substitution.md)
- [Rule/Name](../rule/name.md)

## Sources

- [Aesop/RulePattern/Cache.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern/Cache.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RulePattern.Cache.json)
