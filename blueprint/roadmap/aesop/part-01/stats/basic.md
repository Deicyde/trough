---
catalog: module
lean: Aesop.ForwardInstantiationStats, Aesop.ForwardClusterStateStats, Aesop.ForwardRuleStateStats, Aesop.ForwardStateStats, Aesop.GoalKind, Aesop.GoalStats, Aesop.RuleStats, Aesop.ScriptGenerated.Method, Aesop.ScriptGenerated, Aesop.ScriptGenerated.toString, Aesop.Stats, Aesop.Stats.empty, Aesop.RuleStatsTotals, Aesop.RuleStatsTotals.empty, Aesop.RuleStatsTotals.compareByTotalElapsed, Aesop.Stats.ruleStatsTotals, Aesop.sortRuleStatsTotals, Aesop.Stats.trace, Aesop.StatsRef, Aesop.MonadStats, Aesop.enableStatsCollection, Aesop.enableStatsTracing, Aesop.enableStatsFile, Aesop.enableStats, Aesop.profiling, Aesop.profilingRuleSelection, Aesop.profilingRule, Aesop.profilingForwardState, Aesop.modifyStatsIfEnabled, Aesop.recordScriptGenerated
statement: formalized
proof: formalized
---

# Stats/Basic

`Aesop.Stats.Basic`, in [Aesop/Stats/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean), by Jannis Limperg.

`Aesop.ForwardInstantiationStats` (structure, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L18))

```lean
structure ForwardInstantiationStats where
  «matches» : Nat
  hyps : Nat
  deriving Inhabited, ToJson
```

`Aesop.ForwardClusterStateStats` (structure, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L23))

```lean
structure ForwardClusterStateStats where
  slots : Nat
  instantiationStats : Array ForwardInstantiationStats
  deriving Inhabited, ToJson
```

`Aesop.ForwardRuleStateStats` (structure, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L28))

```lean
structure ForwardRuleStateStats where
  ruleName : RuleName
  clusterStateStats : Array ForwardClusterStateStats
  deriving Inhabited, ToJson
```

`Aesop.ForwardStateStats` (structure, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L33))

```lean
structure ForwardStateStats where
  ruleStateStats : Array ForwardRuleStateStats
  deriving Inhabited, ToJson
```

`Aesop.GoalKind` (inductive type, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L37))

```lean
inductive GoalKind
  | preNorm
  | postNorm
  deriving Inhabited, ToJson
```

`Aesop.GoalStats` (structure, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L42))

```lean
structure GoalStats where
  goalId : Nat -- We don't use GoalId to avoid an import cycle
  goalKind : GoalKind
  /-- Number of fvars in the local context, excluding implementation detail
  fvars. -/
  lctxSize : Nat
  /-- This goal's depth in the search tree. -/
  depth : Nat
  forwardStateStats : ForwardStateStats
  deriving Inhabited, ToJson
```

`Aesop.RuleStats` (structure, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L53))

```lean
structure RuleStats where
  rule : DisplayRuleName
  elapsed : Nanos
  successful : Bool
  deriving Inhabited, ToJson
```

`Aesop.ScriptGenerated.Method` (inductive type, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L68))

```lean
inductive ScriptGenerated.Method where
  | static
  | dynamic
  deriving Inhabited, ToJson
```

`Aesop.ScriptGenerated` (structure, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L78))

```lean
structure ScriptGenerated where
  method : ScriptGenerated.Method
  perfect : Bool
  hasMVar : Bool
  deriving Inhabited, ToJson
```

`Aesop.ScriptGenerated.toString` (definition, [line 86](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L86))

```lean
protected def toString (g : ScriptGenerated) : String
```

`Aesop.Stats` (structure, [line 91](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L91))

```lean
structure Stats where
  total : Nanos
  configParsing : Nanos
  ruleSetConstruction : Nanos
  search : Nanos
  ruleSelection : Nanos
  script : Nanos
  forwardState : Nanos
  scriptGenerated : Option ScriptGenerated
  ruleStats : Array RuleStats
  goalStats : Array GoalStats
  deriving Inhabited
```

`Aesop.Stats.empty` (definition, [line 106](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L106))

```lean
protected def empty : Stats
```

`Aesop.RuleStatsTotals` (structure, [line 115](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L115))

```lean
structure RuleStatsTotals where
  /--
  Number of successful applications of a rule.
  -/
  numSuccessful : Nat
  /--
  Number of failed applications of a rule.
  -/
  numFailed : Nat
  /--
  Total elapsed time of successful applications of a rule.
  -/
  elapsedSuccessful : Nanos
  /--
  Total elapsed time of failed applications of a rule.
  -/
  elapsedFailed : Nanos
```

`Aesop.RuleStatsTotals.empty` (definition, [line 135](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L135))

```lean
protected def empty : RuleStatsTotals
```

`Aesop.RuleStatsTotals.compareByTotalElapsed` (definition, [line 144](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L144))

```lean
def compareByTotalElapsed : (x y : RuleStatsTotals) → Ordering
```

`Aesop.Stats.ruleStatsTotals` (definition, [line 152](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L152))

```lean
def ruleStatsTotals (p : Stats)
    (init : Std.HashMap DisplayRuleName RuleStatsTotals := ∅) :
    Std.HashMap DisplayRuleName RuleStatsTotals
```

`Aesop.sortRuleStatsTotals` (definition, [line 169](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L169))

```lean
def _root_.Aesop.sortRuleStatsTotals
    (ts : Array (DisplayRuleName × RuleStatsTotals)) :
    Array (DisplayRuleName × RuleStatsTotals)
```

`Aesop.Stats.trace` (definition, [line 178](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L178))

```lean
def trace (p : Stats) (opt : TraceOption) : CoreM Unit
```

`Aesop.StatsRef` (abbreviation, [line 202](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L202))

```lean
abbrev StatsRef
```

`Aesop.MonadStats` (class, [line 204](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L204))

```lean
class MonadStats (m) extends MonadOptions m where
  modifyGetStats : (Stats → α × Stats) → m α
  getStats : m Stats :=
    modifyGetStats λ s => (s, s)
  modifyStats : (Stats → Stats) → m Unit :=
    λ f => modifyGetStats λ s => ((), f s)
```

`Aesop.enableStatsCollection` (definition, [line 231](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L231))

```lean
def enableStatsCollection [MonadOptions m] : m Bool
```

`Aesop.enableStatsTracing` (definition, [line 235](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L235))

```lean
def enableStatsTracing [MonadOptions m] : m Bool
```

`Aesop.enableStatsFile` (definition, [line 239](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L239))

```lean
def enableStatsFile [MonadOptions m] : m Bool
```

`Aesop.enableStats` (definition, [line 243](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L243))

```lean
def enableStats [MonadOptions m] : m Bool
```

`Aesop.profiling` (definition, [line 249](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L249))

```lean
def profiling (recordStats : Stats → α → Nanos → Stats) (x : m α) : m α
```

`Aesop.profilingRuleSelection` (definition, [line 258](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L258))

```lean
def profilingRuleSelection : m α → m α
```

`Aesop.profilingRule` (definition, [line 263](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L263))

```lean
def profilingRule (rule : DisplayRuleName) (wasSuccessful : α → Bool) :
    m α → m α
```

`Aesop.profilingForwardState` (definition, [line 270](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L270))

```lean
def profilingForwardState : m α → m α
```

`Aesop.modifyStatsIfEnabled` (definition, [line 274](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L274))

```lean
def modifyStatsIfEnabled (f : Stats → Stats) : m Unit
```

`Aesop.recordScriptGenerated` (definition, [line 278](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean#L278))

```lean
def recordScriptGenerated (x : ScriptGenerated) : m Unit
```

## Depends on

- [Public](../options/public.md)
- [Rule/Name](../rule/name.md)
- [Aesop/Tracing](../../part-02/tracing.md)

## Sources

- [Aesop/Stats/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Stats/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Stats.Basic.json)
