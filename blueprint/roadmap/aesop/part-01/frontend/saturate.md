---
catalog: module
lean: Aesop.ElabM.runForwardElab, Aesop.Frontend.mkForwardOptions, Aesop.Frontend.elabGlobalRuleSets, Aesop.Frontend.elabForwardRule, Aesop.Frontend.mkHypForwardRule, Aesop.Frontend.isImplication, Aesop.Frontend.mkHypImplicationRule?, Aesop.Frontend.addLocalImplications, Aesop.Frontend.elabAdditionalForwardRules, Aesop.Frontend.elabForwardRuleSetCore, Aesop.Frontend.elabForwardRuleSet, Aesop.Frontend.evalSaturateCore, Aesop.Frontend.evalSaturate, Aesop.Frontend.evalSaturate?
statement: formalized
proof: formalized
---

# Frontend/Saturate

`Aesop.Frontend.Saturate`, in [Aesop/Frontend/Saturate.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean), by Jannis Limperg.

`Aesop.ElabM.runForwardElab` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L27))

```lean
def _root_.Aesop.ElabM.runForwardElab (goal : MVarId) (x : ElabM α) :
    TermElabM α
```

`Aesop.Frontend.mkForwardOptions` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L31))

```lean
def mkForwardOptions (maxDepth? : Option Nat) (traceScript : Bool) :
    CoreM Options'
```

`Aesop.Frontend.elabGlobalRuleSets` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L35))

```lean
def elabGlobalRuleSets (rsNames : Array Ident) :
    CoreM (Array (GlobalRuleSet × Name × Name))
```

`Aesop.Frontend.elabForwardRule` (definition, [line 40](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L40))

```lean
def elabForwardRule (term : Term) : ElabM LocalRuleSetMember
```

`Aesop.Frontend.mkHypForwardRule` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L49))

```lean
def mkHypForwardRule (fvarId : FVarId) : ElabM LocalRuleSetMember
```

`Aesop.Frontend.isImplication` (definition, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L53))

```lean
def isImplication (e : Expr) : MetaM Bool
```

`Aesop.Frontend.mkHypImplicationRule?` (definition, [line 57](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L57))

```lean
def mkHypImplicationRule? (fvarId : FVarId) :
    ElabM (Option LocalRuleSetMember)
```

`Aesop.Frontend.addLocalImplications` (definition, [line 67](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L67))

```lean
def addLocalImplications (rs : LocalRuleSet) : ElabM LocalRuleSet
```

`Aesop.Frontend.elabAdditionalForwardRules` (definition, [line 77](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L77))

```lean
def elabAdditionalForwardRules (rs : LocalRuleSet) (rules : Array (TSyntax ``additionalRule)) : ElabM LocalRuleSet
```

`Aesop.Frontend.elabForwardRuleSetCore` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L90))

```lean
def elabForwardRuleSetCore (rsNames : Array Ident)
    (additionalRules : Array (TSyntax ``additionalRule))
    (options : Options') : ElabM LocalRuleSet
```

`Aesop.Frontend.elabForwardRuleSet` (definition, [line 97](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L97))

```lean
def elabForwardRuleSet (rsNames? : Option (TSyntax ``usingRuleSets))
    (additionalRules? : Option (TSyntax ``additionalRules)) (options : Options') :
    ElabM LocalRuleSet
```

`Aesop.Frontend.evalSaturateCore` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L110))

```lean
def evalSaturateCore (stx : Syntax) (depth? : Option (TSyntax `num))
    (rules? : Option (TSyntax ``additionalRules))
    (rs? : Option (TSyntax ``usingRuleSets)) (traceScript : Bool) :
    TacticM Unit
```

`Aesop.Frontend.evalSaturate` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L129))

```lean
def evalSaturate : Tactic
```

`Aesop.Frontend.evalSaturate?` (definition, [line 135](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean#L135))

```lean
def evalSaturate? : Tactic
```

## Depends on

- [Builder/Forward](../builder/forward.md)
- [Frontend/Extension](extension.md)
- [Aesop/Saturate](../../part-02/saturate.md)
- [File](../stats/file.md)

## Sources

- [Aesop/Frontend/Saturate.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Saturate.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.Saturate.json)
