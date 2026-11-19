---
catalog: module
lean: Aesop.sortedPercentileD, Aesop.sortedMedianD, Aesop.StatsReport, Aesop.StatsReport.default, Aesop.StatsReport.scriptsCore, Aesop.StatsReport.scripts, Aesop.StatsReport.scriptsNontrivial
statement: formalized
proof: formalized
---

# Report

`Aesop.Stats.Report`, in [Aesop/Stats/Report.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean), by Jannis Limperg.

`Aesop.sortedPercentileD` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L19))

> Assumes that `xs` is ascending. We use a simple nearest-rank definition of
> percentiles.

```lean
def sortedPercentileD (p : Percent) (dflt : α) (xs : Array α) : α
```

`Aesop.sortedMedianD` (definition, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L26))

```lean
def sortedMedianD (dflt : α) (xs : Array α) : α
```

`Aesop.StatsReport` (abbreviation, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L29))

```lean
abbrev StatsReport
```

`Aesop.StatsReport.default` (definition, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L36))

```lean
def default : StatsReport
```

`Aesop.StatsReport.scriptsCore` (definition, [line 83](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L83))

```lean
def scriptsCore (nSlowest := 30) (nontrivialOnly := false) :
    StatsReport
```

`Aesop.StatsReport.scripts` (definition, [line 151](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L151))

```lean
def scripts
```

`Aesop.StatsReport.scriptsNontrivial` (definition, [line 152](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean#L152))

```lean
def scriptsNontrivial
```

## Depends on

- [Percent](../../part-02/percent.md)
- [Stats/Extension](extension.md)

## Sources

- [Aesop/Stats/Report.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Report.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Stats.Report.json)
