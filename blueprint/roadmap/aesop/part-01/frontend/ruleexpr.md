---
catalog: module
lean: Aesop.Frontend.Priority, Aesop.Frontend.Priority.«elab», Aesop.Frontend.Priority.toInt?, Aesop.Frontend.Priority.toPercent?, Aesop.Frontend.PhaseName.«elab», Aesop.Frontend.DBuilderName, Aesop.Frontend.DBuilderName.«elab», Aesop.Frontend.DBuilderName.toBuilderName?, Aesop.Frontend.DBuilderName.toRuleBuilder, Aesop.Frontend.elabSingleIndexingMode, Aesop.Frontend.IndexingMode.elab, Aesop.Frontend.CasesPattern.elab, Aesop.Frontend.elabTransparency, Aesop.Frontend.BuilderOption, Aesop.Frontend.BuilderOption.«elab», Aesop.Frontend.addBuilderOption, Aesop.Frontend.RuleSetName.elab, Aesop.Frontend.RuleSets, Aesop.Frontend.RuleSets.«elab», Aesop.Frontend.Feature, Aesop.Frontend.Feature.«elab», Aesop.Frontend.RuleExpr, Aesop.Frontend.RuleExpr.«elab», Aesop.Frontend.RuleExpr.foldBranchesM, Aesop.Frontend.RuleConfig, Aesop.Frontend.RuleConfig.addFeature, Aesop.Frontend.RuleConfig.getPenalty, Aesop.Frontend.RuleConfig.getSuccessProbability, Aesop.Frontend.RuleConfig.getSimpPriority, Aesop.Frontend.RuleConfig.getTerm, Aesop.Frontend.RuleConfig.getPhase, Aesop.Frontend.RuleConfig.getBuilder, Aesop.Frontend.RuleConfig.getPhaseSpec, Aesop.Frontend.RuleConfig.getRuleBuilderInput, Aesop.Frontend.RuleConfig.buildRule, Aesop.Frontend.RuleConfig.buildGlobalRule, Aesop.Frontend.RuleConfig.buildLocalRule, Aesop.Frontend.RuleConfig.toRuleFilter, Aesop.Frontend.RuleConfig.validateForAdditionalRules, Aesop.Frontend.RuleExpr.toRuleConfigs, Aesop.Frontend.RuleExpr.toAdditionalRules, Aesop.Frontend.RuleExpr.toAdditionalGlobalRules, Aesop.Frontend.RuleExpr.buildAdditionalGlobalRules, Aesop.Frontend.RuleExpr.toAdditionalLocalRules, Aesop.Frontend.RuleExpr.buildAdditionalLocalRules, Aesop.Frontend.RuleExpr.toRuleFilters, Aesop.Frontend.RuleExpr.toGlobalRuleFilters, Aesop.Frontend.RuleExpr.toLocalRuleFilters
statement: formalized
proof: formalized
---

# RuleExpr

`Aesop.Frontend.RuleExpr`, in [Aesop/Frontend/RuleExpr.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean), by Jannis Limperg.

`Aesop.Frontend.Priority` (inductive type, [line 36](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L36))

```lean
inductive Priority
  | int (i : Int)
  | percent (p : Percent)
  deriving Inhabited
```

`Aesop.Frontend.Priority.«elab»` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L43))

```lean
def «elab» (stx : Syntax) : ElabM Priority
```

`Aesop.Frontend.Priority.toInt?` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L64))

```lean
def toInt? : Priority → Option Int
```

`Aesop.Frontend.Priority.toPercent?` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L68))

```lean
def toPercent? : Priority → Option Percent
```

`Aesop.Frontend.PhaseName.«elab»` (definition, [line 86](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L86))

```lean
def PhaseName.«elab» (stx : Syntax) : ElabM PhaseName
```

`Aesop.Frontend.DBuilderName` (inductive type, [line 111](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L111))

```lean
inductive DBuilderName
  | regular (b : BuilderName)
  | «default»
  deriving Inhabited
```

`Aesop.Frontend.DBuilderName.«elab»` (definition, [line 118](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L118))

```lean
def «elab» (stx : Syntax) : ElabM DBuilderName
```

`Aesop.Frontend.DBuilderName.toBuilderName?` (definition, [line 137](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L137))

```lean
def toBuilderName? : DBuilderName → Option BuilderName
```

`Aesop.Frontend.DBuilderName.toRuleBuilder` (definition, [line 141](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L141))

```lean
def toRuleBuilder : DBuilderName → RuleBuilder
```

`Aesop.Frontend.elabSingleIndexingMode` (definition, [line 165](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L165))

```lean
def elabSingleIndexingMode (stx : Syntax) : ElabM IndexingMode
```

`Aesop.Frontend.IndexingMode.elab` (definition, [line 177](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L177))

```lean
def IndexingMode.elab (stxs : Array Syntax) : ElabM IndexingMode
```

`Aesop.Frontend.CasesPattern.elab` (definition, [line 180](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L180))

```lean
def CasesPattern.elab (stx : Syntax) : TermElabM CasesPattern
```

`Aesop.Frontend.elabTransparency` (definition, [line 191](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L191))

```lean
def elabTransparency : TSyntax ``transparency → TermElabM TransparencyMode
```

`Aesop.Frontend.BuilderOption` (inductive type, [line 211](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L211))

```lean
inductive BuilderOption
  | immediate (names : Array Name)
  | index (imode : IndexingMode)
  | pattern (stx : Term)
  | casesPatterns (pats : Array CasesPattern)
  | transparency (md : TransparencyMode) (alsoForIndex : Bool)
```

`Aesop.Frontend.BuilderOption.«elab»` (definition, [line 220](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L220))

```lean
def «elab» (stx : TSyntax `Aesop.builder_option) : ElabM BuilderOption
```

`Aesop.Frontend.addBuilderOption` (definition, [line 243](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L243))

```lean
def addBuilderOption (bos : RuleBuilderOptions) :
    BuilderOption → RuleBuilderOptions
```

`Aesop.Frontend.RuleSetName.elab` (definition, [line 263](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L263))

```lean
def RuleSetName.elab (stx : Syntax) : RuleSetName
```

`Aesop.Frontend.RuleSets` (structure, [line 270](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L270))

```lean
structure RuleSets where
  ruleSets : Array RuleSetName
  deriving Inhabited
```

`Aesop.Frontend.RuleSets.«elab»` (definition, [line 276](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L276))

```lean
def «elab» (stx : Syntax) : ElabM RuleSets
```

`Aesop.Frontend.Feature` (inductive type, [line 306](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L306))

```lean
inductive Feature
  | phase (p : PhaseName)
  | priority (p : Priority)
  | builder (b : DBuilderName)
  | builderOption (o : BuilderOption)
  | term (i : Term)
  | ruleSets (rs : RuleSets)
  deriving Inhabited
```

`Aesop.Frontend.Feature.«elab»` (definition, [line 319](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L319))

```lean
partial def «elab» (stx : Syntax) : ElabM Feature
```

`Aesop.Frontend.RuleExpr` (inductive type, [line 351](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L351))

```lean
inductive RuleExpr
  | node (f : Feature) (children : Array RuleExpr)
  deriving Inhabited
```

`Aesop.Frontend.RuleExpr.«elab»` (definition, [line 357](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L357))

```lean
partial def «elab» (stx : Syntax) : ElabM RuleExpr
```

`Aesop.Frontend.RuleExpr.foldBranchesM` (definition, [line 370](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L370))

```lean
partial def foldBranchesM {m} [Monad m] (f : σ → Feature → m σ) (init : σ)
    (e : RuleExpr) : m (Array σ)
```

`Aesop.Frontend.RuleConfig` (structure, [line 384](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L384))

```lean
structure RuleConfig where
  term? : Option Term
  phase? : Option PhaseName
  priority? : Option Priority
  builder? : Option DBuilderName
  builderOptions : RuleBuilderOptions
  ruleSets : RuleSets
```

`Aesop.Frontend.RuleConfig.addFeature` (definition, [line 394](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L394))

```lean
def addFeature (c : RuleConfig) : Feature → m RuleConfig
```

`Aesop.Frontend.RuleConfig.getPenalty` (definition, [line 409](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L409))

```lean
def getPenalty (phase : PhaseName) (c : RuleConfig) : m Int
```

`Aesop.Frontend.RuleConfig.getSuccessProbability` (definition, [line 416](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L416))

```lean
def getSuccessProbability (c : RuleConfig) : m Percent
```

`Aesop.Frontend.RuleConfig.getSimpPriority` (definition, [line 423](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L423))

```lean
def getSimpPriority (c : RuleConfig) : m Nat
```

`Aesop.Frontend.RuleConfig.getTerm` (definition, [line 432](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L432))

```lean
def getTerm (c : RuleConfig) : m Term
```

`Aesop.Frontend.RuleConfig.getPhase` (definition, [line 437](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L437))

```lean
def getPhase (c : RuleConfig) : m PhaseName
```

`Aesop.Frontend.RuleConfig.getBuilder` (definition, [line 442](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L442))

```lean
def getBuilder (c : RuleConfig) : m DBuilderName
```

`Aesop.Frontend.RuleConfig.getPhaseSpec` (definition, [line 447](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L447))

```lean
def getPhaseSpec (c : RuleConfig) : m PhaseSpec
```

`Aesop.Frontend.RuleConfig.getRuleBuilderInput` (definition, [line 456](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L456))

```lean
def getRuleBuilderInput (c : RuleConfig) : TermElabM RuleBuilderInput
```

`Aesop.Frontend.RuleConfig.buildRule` (definition, [line 462](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L462))

```lean
def buildRule (c : RuleConfig) :
    ElabM (LocalRuleSetMember × Array RuleSetName)
```

`Aesop.Frontend.RuleConfig.buildGlobalRule` (definition, [line 469](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L469))

```lean
def buildGlobalRule (c : RuleConfig) :
    ElabM (GlobalRuleSetMember × Array RuleSetName)
```

`Aesop.Frontend.RuleConfig.buildLocalRule` (definition, [line 477](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L477))

```lean
def buildLocalRule (c : RuleConfig) : ElabM LocalRuleSetMember
```

`Aesop.Frontend.RuleConfig.toRuleFilter` (definition, [line 480](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L480))

```lean
def toRuleFilter (c : RuleConfig) : ElabM (RuleSetNameFilter × RuleFilter)
```

`Aesop.Frontend.RuleConfig.validateForAdditionalRules` (definition, [line 507](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L507))

```lean
def validateForAdditionalRules (c : RuleConfig) (defaultRuleSet : RuleSetName) :
    m RuleConfig
```

`Aesop.Frontend.RuleExpr.toRuleConfigs` (definition, [line 552](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L552))

```lean
def toRuleConfigs (e : RuleExpr) (init : RuleConfig) :
    m (Array RuleConfig)
```

`Aesop.Frontend.RuleExpr.toAdditionalRules` (definition, [line 556](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L556))

```lean
def toAdditionalRules (e : RuleExpr) (init : RuleConfig)
    (defaultRuleSet : RuleSetName) : m (Array RuleConfig)
```

`Aesop.Frontend.RuleExpr.toAdditionalGlobalRules` (definition, [line 561](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L561))

```lean
def toAdditionalGlobalRules (decl? : Option Name) (e : RuleExpr) :
    m (Array RuleConfig)
```

`Aesop.Frontend.RuleExpr.buildAdditionalGlobalRules` (definition, [line 573](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L573))

```lean
def buildAdditionalGlobalRules (decl? : Option Name) (e : RuleExpr) :
    TermElabM (Array (GlobalRuleSetMember × Array RuleSetName))
```

`Aesop.Frontend.RuleExpr.toAdditionalLocalRules` (definition, [line 579](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L579))

```lean
def toAdditionalLocalRules (e : RuleExpr) : MetaM (Array RuleConfig)
```

`Aesop.Frontend.RuleExpr.buildAdditionalLocalRules` (definition, [line 590](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L590))

```lean
def buildAdditionalLocalRules (goal : MVarId) (e : RuleExpr) :
    TermElabM (Array LocalRuleSetMember)
```

`Aesop.Frontend.RuleExpr.toRuleFilters` (definition, [line 595](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L595))

```lean
def toRuleFilters (e : RuleExpr) :
    ElabM (Array (RuleSetNameFilter × RuleFilter))
```

`Aesop.Frontend.RuleExpr.toGlobalRuleFilters` (definition, [line 608](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L608))

```lean
def toGlobalRuleFilters (e : RuleExpr) :
    TermElabM (Array (RuleSetNameFilter × RuleFilter))
```

`Aesop.Frontend.RuleExpr.toLocalRuleFilters` (definition, [line 612](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean#L612))

```lean
def toLocalRuleFilters (e : RuleExpr) : ElabM (Array RuleFilter)
```

## Depends on

- [Builder/Cases](../builder/cases.md)
- [Default](../builder/default.md)
- [Builder/Forward](../builder/forward.md)
- [Builder/Unfold](../builder/unfold.md)
- [Filter](../ruleset/filter.md)

## Sources

- [Aesop/Frontend/RuleExpr.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/RuleExpr.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.RuleExpr.json)
