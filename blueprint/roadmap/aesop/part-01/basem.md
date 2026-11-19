---
catalog: module
lean: Aesop.BaseM.State, Aesop.BaseM, Aesop.BaseM.run
statement: formalized
proof: formalized
---

# BaseM

`Aesop.BaseM`, in [Aesop/BaseM.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BaseM.lean), by Jannis Limperg.

`Aesop.BaseM.State` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BaseM.lean#L20))

> State of the `BaseM` monad.

```lean
structure BaseM.State where
  /-- The rule pattern cache. -/
  rulePatternCache : RulePatternCache
  /-- Stats collected during an Aesop call. -/
  stats : Stats
  deriving Inhabited
```

`Aesop.BaseM` (abbreviation, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BaseM.lean#L32))

> Aesop's base monad. Contains no interesting data, only various caches and
> stats.

```lean
abbrev BaseM
```

`Aesop.BaseM.run` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BaseM.lean#L37))

> Run a `BaseM` action.

```lean
protected def run (x : BaseM α) (stats : Stats := ∅) : MetaM (α × Stats)
```

## Depends on

- [Cache](rulepattern/cache.md)
- [Stats/Basic](stats/basic.md)

## Sources

- [Aesop/BaseM.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BaseM.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.BaseM.json)
