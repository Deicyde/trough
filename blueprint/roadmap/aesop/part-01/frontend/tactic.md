---
catalog: module
lean: Aesop.Frontend.elabConfigUnsafe, Aesop.Frontend.elabOptions, Aesop.Frontend.elabSimpConfig, Aesop.Frontend.elabSimpConfigCtx, Aesop.Frontend.TacticConfig, Aesop.Frontend.TacticConfig.parse, Aesop.Frontend.TacticConfig.updateRuleSet, Aesop.Frontend.TacticConfig.getRuleSet
statement: formalized
proof: formalized
---

# Frontend/Tactic

`Aesop.Frontend.Tactic`, in [Aesop/Frontend/Tactic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean), by Jannis Limperg.

`Aesop.Frontend.elabConfigUnsafe` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L73))

```lean
unsafe def elabConfigUnsafe (type : Name) (stx : Syntax) : TermElabM α
```

`Aesop.Frontend.elabOptions` (definition, [line 81](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L81))

```lean
def elabOptions : Syntax → TermElabM Aesop.Options
```

`Aesop.Frontend.elabSimpConfig` (definition, [line 84](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L84))

```lean
def elabSimpConfig : Syntax → TermElabM Simp.Config
```

`Aesop.Frontend.elabSimpConfigCtx` (definition, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L87))

```lean
def elabSimpConfigCtx : Syntax → TermElabM Simp.ConfigCtx
```

`Aesop.Frontend.TacticConfig` (structure, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L90))

```lean
structure TacticConfig where
  additionalRules : Array RuleExpr
  erasedRules : Array RuleExpr
  enabledRuleSets : Std.HashSet RuleSetName
  options : Aesop.Options
  simpConfig : Simp.Config
  simpConfigSyntax? : Option Term
```

`Aesop.Frontend.TacticConfig.parse` (definition, [line 100](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L100))

```lean
def parse (stx : Syntax) (goal : MVarId) : TermElabM TacticConfig
```

`Aesop.Frontend.TacticConfig.updateRuleSet` (definition, [line 170](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L170))

```lean
def updateRuleSet (rs : LocalRuleSet) (c : TacticConfig) (goal : MVarId):
    TermElabM LocalRuleSet
```

`Aesop.Frontend.TacticConfig.getRuleSet` (definition, [line 188](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean#L188))

```lean
def getRuleSet (goal : MVarId) (c : TacticConfig) :
    TermElabM LocalRuleSet
```

## Depends on

- [Frontend/Extension](extension.md)
- [RuleExpr](ruleexpr.md)

## Sources

- [Aesop/Frontend/Tactic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Tactic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.Tactic.json)
