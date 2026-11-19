---
catalog: module
lean: Aesop.isForwardOrDestructRuleName, Aesop.SaturateM.Context, Aesop.SaturateM, Aesop.SaturateM.run, Aesop.getSingleGoal, Aesop.saturateCore, Aesop.Stateful.saturateCore, Aesop.saturateMain', Aesop.saturateMain, Aesop.saturate
statement: formalized
proof: formalized
---

# Aesop/Saturate

`Aesop.Saturate`, in [Aesop/Saturate.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean), by Jannis Limperg.

`Aesop.isForwardOrDestructRuleName` (definition, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L23))

```lean
def isForwardOrDestructRuleName (n : RuleName) : Bool
```

`Aesop.SaturateM.Context` (structure, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L26))

```lean
structure SaturateM.Context where
  options : Aesop.Options'
  deriving Inhabited
```

`Aesop.SaturateM` (abbreviation, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L30))

```lean
abbrev SaturateM
```

`Aesop.SaturateM.run` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L34))

```lean
def run (options : Aesop.Options') (x : SaturateM α) : MetaM (α × Stats)
```

`Aesop.getSingleGoal` (definition, [line 40](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L40))

```lean
def getSingleGoal [Monad m] [MonadError m] (o : RuleTacOutput) :
    m (GoalDiff × Meta.SavedState × Option (Array Script.LazyStep))
```

`Aesop.saturateCore` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L51))

```lean
partial def saturateCore (rs : LocalRuleSet) (goal : MVarId) : SaturateM MVarId
```

`Aesop.Stateful.saturateCore` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L129))

```lean
partial def saturateCore (rs : LocalRuleSet) (goal : MVarId) : SaturateM MVarId
```

`Aesop.saturateMain'` (definition, [line 186](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L186))

```lean
def saturateMain' (rs : LocalRuleSet) (goal : MVarId) : SaturateM MVarId
```

`Aesop.saturateMain` (definition, [line 213](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L213))

```lean
def saturateMain (rs : LocalRuleSet) (goal : MVarId) : SaturateM MVarId
```

`Aesop.saturate` (definition, [line 218](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean#L218))

```lean
def saturate (rs : LocalRuleSet) (goal : MVarId) (options : Aesop.Options') :
    MetaM (MVarId × Stats)
```

## Depends on

- [Initial](../part-01/forward/state-2/initial.md)
- [Script/Check](../part-01/script/check.md)

## Proof depends on

- [RuleTac](ruletac.md)
- [Expansion/Basic](../part-01/search/expansion-2/basic.md)

## Sources

- [Aesop/Saturate.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Saturate.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.Saturate.json)
