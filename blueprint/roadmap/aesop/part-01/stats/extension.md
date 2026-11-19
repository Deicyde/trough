---
catalog: module
lean: Aesop.StatsExtensionEntry, Aesop.StatsExtensionEntry.forCurrentFile, Aesop.StatsExtension, Aesop.StatsExtension.importedEntries, Aesop.recordStatsIfEnabled, Aesop.recordStatsForCurrentFileIfEnabled, Aesop.StatsArray, Aesop.mkStatsArray, Aesop.getStatsArray
statement: formalized
proof: formalized
---

# Stats/Extension

`Aesop.Stats.Extension`, in [Aesop/Stats/Extension.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean), by Jannis Limperg.

`Aesop.StatsExtensionEntry` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L16))

```lean
structure StatsExtensionEntry where
  /--
  The Aesop call for which stats were collected.
  -/
  aesopStx : Syntax
  /-
  The file in which Aesop was called.
  -/
  fileName : String
  /-
  The position in the file where Aesop was called.
  -/
  position? : Option Position
  /--
  The collected stats.
  -/
  stats : Stats
```

`Aesop.StatsExtensionEntry.forCurrentFile` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L36))

```lean
def forCurrentFile [Monad m] [MonadLog m] (stx : Syntax) (stats : Stats) :
    m StatsExtensionEntry
```

`Aesop.StatsExtension` (abbreviation, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L45))

```lean
abbrev StatsExtension
```

`Aesop.StatsExtension.importedEntries` (definition, [line 47](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L47))

```lean
def StatsExtension.importedEntries (env : Environment) (ext : StatsExtension) :
    Array (Array StatsExtensionEntry)
```

`Aesop.recordStatsIfEnabled` (definition, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L58))

```lean
def recordStatsIfEnabled [Monad m] [MonadEnv m] [MonadOptions m]
    (s : StatsExtensionEntry) : m Unit
```

`Aesop.recordStatsForCurrentFileIfEnabled` (definition, [line 63](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L63))

```lean
def recordStatsForCurrentFileIfEnabled [Monad m] [MonadEnv m] [MonadOptions m]
    [MonadLog m] (aesopStx : Syntax) (stats : Stats) : m Unit
```

`Aesop.StatsArray` (abbreviation, [line 69](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L69))

```lean
abbrev StatsArray
```

`Aesop.mkStatsArray` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L71))

```lean
def mkStatsArray (localEntries : List StatsExtensionEntry)
    (importedEntries : Array (Array StatsExtensionEntry)) :
    StatsArray
```

`Aesop.getStatsArray` (definition, [line 81](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean#L81))

```lean
def getStatsArray [Monad m] [MonadEnv m] : m StatsArray
```

## Depends on

- [Stats/Basic](basic.md)

## Sources

- [Aesop/Stats/Extension.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Extension.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Stats.Extension.json)
