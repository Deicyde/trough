---
catalog: module
lean: Aesop.StatsFileRecord, Aesop.StatsFileRecord.ofStats, Aesop.appendStatsToStatsFileIfEnabled
statement: formalized
proof: formalized
---

# File

`Aesop.Stats.File`, in [Aesop/Stats/File.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/File.lean), by Jannis Limperg.

`Aesop.StatsFileRecord` (structure, [line 14](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/File.lean#L14))

```lean
public structure StatsFileRecord extends Stats where
  «syntax» : String
  file : String
  position : Option Position
  declaration : Option Name
  goalSolved : Bool
  deriving ToJson
```

`Aesop.StatsFileRecord.ofStats` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/File.lean#L25))

```lean
public protected def ofStats (aesopStx : Syntax) (goalSolved : Bool) (stats : Stats) :
    m StatsFileRecord
```

`Aesop.appendStatsToStatsFileIfEnabled` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/File.lean#L37))

```lean
public def appendStatsToStatsFileIfEnabled (aesopStx : Syntax) (stats : Stats)
    (allGoalsSolved : Bool) : m Unit
```

## Depends on

- [Stats/Basic](basic.md)

## Sources

- [Aesop/Stats/File.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/File.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Stats.File.json)
