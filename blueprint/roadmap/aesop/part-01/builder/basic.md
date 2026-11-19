---
catalog: module
lean: Aesop.RuleBuilderOptions, Aesop.RuleBuilderOptions.default, Aesop.CoreRuleBuilderOutput, Aesop.PhaseSpec, Aesop.PhaseSpec.phase, Aesop.PhaseSpec.toRule, Aesop.RuleBuilderInput, Aesop.RuleBuilderInput.phaseName, Aesop.RuleBuilder, Aesop.elabGlobalRuleIdent, Aesop.elabInductiveRuleIdent
statement: formalized
proof: formalized
---

# Builder/Basic

`Aesop.Builder.Basic`, in [Aesop/Builder/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean), by Jannis Limperg.

`Aesop.RuleBuilderOptions` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L20))

> Options for the builders. Most options are only relevant for certain builders.

```lean
structure RuleBuilderOptions where
  immediatePremises? : Option (Array Name)
  indexingMode? : Option IndexingMode
  casesPatterns? : Option (Array CasesPattern)
  pattern? : Option Term
  /-- The transparency used by the rule tactic. -/
  transparency? : Option TransparencyMode
  /-- The transparency used for indexing the rule. Currently, the rule is not
  indexed unless this is `.reducible`. -/
  indexTransparency? : Option TransparencyMode
  deriving Inhabited
```

`Aesop.RuleBuilderOptions.default` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L34))

```lean
protected def default : RuleBuilderOptions
```

`Aesop.CoreRuleBuilderOutput` (structure, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L42))

```lean
structure CoreRuleBuilderOutput where
  ruleExprName : Name
  builderName : BuilderName
  scopeName : ScopeName
  tac : RuleTacDescr
  indexingMode : IndexingMode
  pattern? : Option RulePattern
```

`Aesop.PhaseSpec` (inductive type, [line 50](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L50))

```lean
inductive PhaseSpec
  | safe (info : SafeRuleInfo)
  | norm (info : NormRuleInfo)
  | «unsafe» (info : UnsafeRuleInfo)
  deriving Inhabited
```

`Aesop.PhaseSpec.phase` (definition, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L58))

```lean
def phase : PhaseSpec → PhaseName
```

`Aesop.PhaseSpec.toRule` (definition, [line 63](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L63))

```lean
def toRule (phase : PhaseSpec) (ruleExprName : Name) (builder : BuilderName)
    (scope : ScopeName) (tac : RuleTacDescr) (indexingMode : IndexingMode)
    (pattern? : Option RulePattern) : BaseRuleSetMember
```

`Aesop.RuleBuilderInput` (structure, [line 88](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L88))

```lean
structure RuleBuilderInput where
  term : Term
  options : RuleBuilderOptions
  phase : PhaseSpec
  deriving Inhabited
```

`Aesop.RuleBuilderInput.phaseName` (definition, [line 96](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L96))

```lean
def phaseName (input : RuleBuilderInput) : PhaseName
```

`Aesop.RuleBuilder` (abbreviation, [line 102](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L102))

```lean
abbrev RuleBuilder
```

`Aesop.elabGlobalRuleIdent` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L105))

```lean
def elabGlobalRuleIdent (builderName : BuilderName) (term : Term) :
    TermElabM Name
```

`Aesop.elabInductiveRuleIdent` (definition, [line 112](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean#L112))

```lean
def elabInductiveRuleIdent (builderName : BuilderName) (term : Term) (md : TransparencyMode) :
    TermElabM (Name × InductiveVal)
```

## Depends on

- [Member](../ruleset/member.md)
- [ElabRuleTerm](../ruletac/elabruleterm.md)

## Sources

- [Aesop/Builder/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Basic.json)
