---
catalog: module
lean: Aesop.BaseRuleSet, Aesop.GlobalRuleSet, Aesop.LocalRuleSet, Aesop.GlobalRuleSet.onBaseM, Aesop.GlobalRuleSet.onBase, Aesop.GlobalRuleSet.modifyBaseM, Aesop.GlobalRuleSet.modifyBase, Aesop.LocalRuleSet.onBaseM, Aesop.LocalRuleSet.onBase, Aesop.LocalRuleSet.modifyBaseM, Aesop.LocalRuleSet.modifyBase, Aesop.BaseRuleSet.trace, Aesop.GlobalRuleSet.trace, Aesop.LocalRuleSet.trace, Aesop.BaseRuleSet.empty, Aesop.GlobalRuleSet.empty, Aesop.LocalRuleSet.empty, Aesop.BaseRuleSet.contains, Aesop.GlobalRuleSet.contains, Aesop.LocalRuleSet.containsGlobalSimpTheorem, Aesop.LocalRuleSet.contains, Aesop.BaseRuleSet.merge, Aesop.BaseRuleSet.add, Aesop.LocalRuleSet.add, Aesop.BaseRuleSet.erase, Aesop.GlobalRuleSet.erase, Aesop.LocalRuleSet.erase, Aesop.LocalRuleSet.applicableNormalizationRulesWith, Aesop.LocalRuleSet.applicableNormalizationRules, Aesop.LocalRuleSet.applicableUnsafeRulesWith, Aesop.LocalRuleSet.applicableUnsafeRules, Aesop.LocalRuleSet.applicableSafeRulesWith, Aesop.LocalRuleSet.applicableSafeRules, Aesop.LocalRuleSet.applicableForwardRulesWith, Aesop.LocalRuleSet.applicableForwardRules, Aesop.LocalRuleSet.constForwardRuleMatches, Aesop.LocalRuleSet.forwardRulePatternSubstsInExpr, Aesop.LocalRuleSet.forwardRulePatternSubstsInLocalDecl, Aesop.LocalRuleSet.unindex, Aesop.unindexPredicate?, Aesop.mkLocalRuleSet
statement: formalized
proof: formalized
---

# RuleSet

`Aesop.RuleSet`, in [Aesop/RuleSet.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean), by Jannis Limperg.

`Aesop.BaseRuleSet` (structure, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L33))

> The Aesop-specific parts of an Aesop rule set. A `BaseRuleSet` stores global
> Aesop rules, e.g. safe and unsafe rules. It does not store simp theorems for
> the builtin norm simp rule; these are instead stored in a simp extension.

```lean
structure BaseRuleSet where
  /--
  Normalisation rules registered in this rule set.
  -/
  normRules : Index NormRuleInfo
  /--
  Unsafe rules registered in this rule set.
  -/
  unsafeRules : Index UnsafeRuleInfo
  /--
  Safe rules registered in this rule set.
  -/
  safeRules : Index SafeRuleInfo
  /--
  Rules for the builtin unfold rule. A pair `(decl, unfoldThm?)` in this map
  represents a declaration `decl` which should be unfolded. `unfoldThm?` should
  be the output of `getUnfoldEqnFor? decl` and is cached here for efficiency.
  -/
  -- TODO Don't cache equation name; this may lead to bugs and the performance
  -- cost is negligible.
  unfoldRules : PHashMap Name (Option Name)
  /--
  Forward rules. There's a special procedure for applying forward rules, so we
  don't store them in the regular indices.
  -/
  forwardRules : ForwardIndex
  /-- The names of all rules in `forwardRules`. -/
  -- HACK to be removed once we switch fully to stateful forward reasoning.
  forwardRuleNames : PHashSet RuleName
  /--
  An index for the rule patterns associated with rules contained in this rule
  set. When rules are removed from the rule set, their patterns are not removed
  from this index.
  -/
  rulePatterns : RulePatternIndex
  /--
  The set of rules that were erased from `normRules`, `unsafeRules`, `safeRules`
  and `forwardRules`. When we erase a rule which is present in any of these four
  indices, the rule is not removed from the indices but just added to this set.
  By contrast, when we erase a rule from `unfoldRules`, we actually delete it.
  -/
  erased : PHashSet RuleName
  /--
  A cache of the names of all rules registered in this rule set. Invariant:
  `ruleNames` contains exactly the names of the rules present in `normRules`,
  `unsafeRules`, `safeRules`, `forwardRules` and `unfoldRules` and not present
  in `erased`. We use this cache (a) to quickly determine whether a rule is
  present in the rule set and (b) to find the full rule names associated with
  the fvar or const identified by a name.
  -/
  ruleNames : PHashMap Name (UnorderedArraySet RuleName)
  deriving Inhabited
```

`Aesop.GlobalRuleSet` (structure, [line 92](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L92))

> A global Aesop rule set. When we tag a declaration with `@[aesop]`, it is stored
> in one or more of these rule sets. Internally, a `GlobalRuleSet` is composed of
> a `BaseRuleSet` (stored in an Aesop rule set extension) plus a set of simp
> theorems (stored in a `SimpExtension`).

```lean
structure GlobalRuleSet extends BaseRuleSet where
  /--
  The simp theorems stored in this rule set.
  -/
  simpTheorems : SimpTheorems
  /--
  The simprocs stored in this rule set.
  -/
  simprocs : Simprocs
  deriving Inhabited
```

`Aesop.LocalRuleSet` (structure, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L108))

> The rule set used by an Aesop tactic call. A local rule set is produced by
> combining several global rule sets and possibly adding or erasing some
> individual rules.

```lean
structure LocalRuleSet extends BaseRuleSet where
  /--
  The simp theorems used by the builtin norm simp rule.
  -/
  simpTheoremsArray : Array (Name × SimpTheorems)
  /--
  The simp theorems array must contain at least one `SimpTheorems` structure.
  When a simp theorem is added to a `LocalRuleSet`, it is stored in this first
  `SimpTheorems` structure.
  -/
  simpTheoremsArrayNonempty : 0 < simpTheoremsArray.size
  /--
  The simprocs used by the builtin norm simp rule.
  -/
  simprocsArray : Array (Name × Simprocs)
  /--
  The simprocs array must contain at least one `Simprocs` structure, for the
  same reason as above.
  -/
  simprocsArrayNonempty : 0 < simprocsArray.size
  /--
  FVars that were explicitly added as simp rules.
  -/
  localNormSimpRules : Array LocalNormSimpRule
```

`Aesop.GlobalRuleSet.onBaseM` (definition, [line 139](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L139))

```lean
def onBaseM [Monad m] (f : BaseRuleSet → m (BaseRuleSet × α))
    (rs : GlobalRuleSet) : m (GlobalRuleSet × α)
```

`Aesop.GlobalRuleSet.onBase` (definition, [line 146](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L146))

```lean
def onBase (f : BaseRuleSet → BaseRuleSet × α) (rs : GlobalRuleSet) :
    GlobalRuleSet × α
```

`Aesop.GlobalRuleSet.modifyBaseM` (definition, [line 151](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L151))

```lean
def modifyBaseM [Monad m] (f : BaseRuleSet → m BaseRuleSet)
    (rs : GlobalRuleSet) : m GlobalRuleSet
```

`Aesop.GlobalRuleSet.modifyBase` (definition, [line 156](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L156))

```lean
def modifyBase (f : BaseRuleSet → BaseRuleSet) (rs : GlobalRuleSet) :
    GlobalRuleSet
```

`Aesop.LocalRuleSet.onBaseM` (definition, [line 166](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L166))

```lean
def onBaseM [Monad m] (f : BaseRuleSet → m (BaseRuleSet × α))
    (rs : LocalRuleSet) : m (LocalRuleSet × α)
```

`Aesop.LocalRuleSet.onBase` (definition, [line 172](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L172))

```lean
def onBase (f : BaseRuleSet → (BaseRuleSet × α)) (rs : LocalRuleSet) :
    LocalRuleSet × α
```

`Aesop.LocalRuleSet.modifyBaseM` (definition, [line 176](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L176))

```lean
def modifyBaseM [Monad m] (f : BaseRuleSet → m BaseRuleSet) (rs : LocalRuleSet) :
    m LocalRuleSet
```

`Aesop.LocalRuleSet.modifyBase` (definition, [line 180](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L180))

```lean
def modifyBase (f : BaseRuleSet → BaseRuleSet) (rs : LocalRuleSet) :
    LocalRuleSet
```

`Aesop.BaseRuleSet.trace` (definition, [line 187](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L187))

```lean
def BaseRuleSet.trace (rs : BaseRuleSet) (traceOpt : TraceOption) :
    CoreM Unit
```

`Aesop.GlobalRuleSet.trace` (definition, [line 209](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L209))

```lean
def GlobalRuleSet.trace (rs : GlobalRuleSet) (traceOpt : TraceOption) :
    CoreM Unit
```

`Aesop.LocalRuleSet.trace` (definition, [line 218](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L218))

```lean
def LocalRuleSet.trace (rs : LocalRuleSet) (traceOpt : TraceOption) :
    CoreM Unit
```

`Aesop.BaseRuleSet.empty` (definition, [line 235](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L235))

```lean
def BaseRuleSet.empty : BaseRuleSet
```

`Aesop.GlobalRuleSet.empty` (definition, [line 241](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L241))

```lean
def GlobalRuleSet.empty : GlobalRuleSet
```

`Aesop.LocalRuleSet.empty` (definition, [line 247](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L247))

```lean
def LocalRuleSet.empty : LocalRuleSet
```

`Aesop.BaseRuleSet.contains` (definition, [line 265](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L265))

```lean
def BaseRuleSet.contains (rs : BaseRuleSet) (n : RuleName) : Bool
```

`Aesop.GlobalRuleSet.contains` (definition, [line 272](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L272))

```lean
def GlobalRuleSet.contains (rs : GlobalRuleSet) (n : RuleName) : Bool
```

`Aesop.LocalRuleSet.containsGlobalSimpTheorem` (definition, [line 277](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L277))

```lean
def LocalRuleSet.containsGlobalSimpTheorem (rs : LocalRuleSet) (decl : Name) :
    Bool
```

`Aesop.LocalRuleSet.contains` (definition, [line 282](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L282))

```lean
def LocalRuleSet.contains (rs : LocalRuleSet) (n : RuleName) : Bool
```

`Aesop.BaseRuleSet.merge` (definition, [line 290](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L290))

```lean
def BaseRuleSet.merge (rs₁ rs₂ : BaseRuleSet) : BaseRuleSet
```

`Aesop.BaseRuleSet.add` (definition, [line 314](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L314))

```lean
def BaseRuleSet.add (rs : BaseRuleSet) (r : BaseRuleSetMember) :
    BaseRuleSet
```

`Aesop.LocalRuleSet.add` (definition, [line 366](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L366))

```lean
def LocalRuleSet.add (rs : LocalRuleSet) :
    LocalRuleSetMember → LocalRuleSet
```

`Aesop.BaseRuleSet.erase` (definition, [line 382](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L382))

```lean
def BaseRuleSet.erase (rs : BaseRuleSet) (f : RuleFilter) :
    BaseRuleSet × Bool
```

`Aesop.GlobalRuleSet.erase` (definition, [line 408](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L408))

```lean
def GlobalRuleSet.erase (rs : GlobalRuleSet) (f : RuleFilter) :
    GlobalRuleSet × Bool
```

`Aesop.LocalRuleSet.erase` (definition, [line 417](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L417))

```lean
def LocalRuleSet.erase (rs : LocalRuleSet) (f : RuleFilter) :
    LocalRuleSet × Bool
```

`Aesop.LocalRuleSet.applicableNormalizationRulesWith` (definition, [line 473](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L473))

```lean
def applicableNormalizationRulesWith (rs : LocalRuleSet)
    (fms : ForwardRuleMatches) (goal : MVarId)
    (include? : NormRule → Bool) : BaseM (Array (IndexMatchResult NormRule))
```

`Aesop.LocalRuleSet.applicableNormalizationRules` (definition, [line 483](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L483))

```lean
def applicableNormalizationRules (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) : BaseM (Array (IndexMatchResult NormRule))
```

`Aesop.LocalRuleSet.applicableUnsafeRulesWith` (definition, [line 487](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L487))

```lean
def applicableUnsafeRulesWith (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) (include? : UnsafeRule → Bool) :
    BaseM (Array (IndexMatchResult UnsafeRule))
```

`Aesop.LocalRuleSet.applicableUnsafeRules` (definition, [line 497](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L497))

```lean
def applicableUnsafeRules (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) : BaseM (Array (IndexMatchResult UnsafeRule))
```

`Aesop.LocalRuleSet.applicableSafeRulesWith` (definition, [line 501](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L501))

```lean
def applicableSafeRulesWith (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) (include? : SafeRule → Bool) :
    BaseM (Array (IndexMatchResult SafeRule))
```

`Aesop.LocalRuleSet.applicableSafeRules` (definition, [line 511](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L511))

```lean
def applicableSafeRules (rs : LocalRuleSet) (fms : ForwardRuleMatches)
    (goal : MVarId) : BaseM (Array (IndexMatchResult SafeRule))
```

`Aesop.LocalRuleSet.applicableForwardRulesWith` (definition, [line 515](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L515))

```lean
def applicableForwardRulesWith (rs : LocalRuleSet) (e : Expr)
    (include? : ForwardRule → Bool) :
    MetaM (Array (ForwardRule × PremiseIndex))
```

`Aesop.LocalRuleSet.applicableForwardRules` (definition, [line 530](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L530))

```lean
def applicableForwardRules (rs : LocalRuleSet) (e : Expr) :
    MetaM (Array (ForwardRule × PremiseIndex))
```

`Aesop.LocalRuleSet.constForwardRuleMatches` (definition, [line 534](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L534))

```lean
def constForwardRuleMatches (rs : LocalRuleSet) : Array ForwardRuleMatch
```

`Aesop.LocalRuleSet.forwardRulePatternSubstsInExpr` (definition, [line 544](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L544))

```lean
def forwardRulePatternSubstsInExpr (rs : LocalRuleSet) (e : Expr) :
    BaseM (Array (ForwardRule × Substitution))
```

`Aesop.LocalRuleSet.forwardRulePatternSubstsInLocalDecl` (definition, [line 554](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L554))

```lean
def forwardRulePatternSubstsInLocalDecl (rs : LocalRuleSet) (ldecl : LocalDecl) :
    BaseM (Array (ForwardRule × Substitution))
```

`Aesop.LocalRuleSet.unindex` (definition, [line 567](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L567))

```lean
def unindex (rs : LocalRuleSet) (p : RuleName → Bool) : LocalRuleSet
```

`Aesop.unindexPredicate?` (definition, [line 578](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L578))

```lean
def unindexPredicate? (options : Options') : Option (RuleName → Bool)
```

`Aesop.mkLocalRuleSet` (definition, [line 584](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean#L584))

```lean
def mkLocalRuleSet (rss : Array (GlobalRuleSet × Name × Name))
    (options : Options') : CoreM LocalRuleSet
```

## Depends on

- [Index](index.md)
- [Index/Forward](../part-01/index/forward.md)
- [Filter](../part-01/ruleset/filter.md)
- [Member](../part-01/ruleset/member.md)
- [ForwardRuleMatches](../part-01/tree/data-2/forwardrulematches.md)

## Sources

- [Aesop/RuleSet.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.RuleSet.json)
