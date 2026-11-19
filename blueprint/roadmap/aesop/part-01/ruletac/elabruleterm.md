---
catalog: module
lean: Aesop.elabGlobalRuleIdent?, Aesop.matchInductiveTypeSynonym?, Aesop.elabInductiveRuleIdent?, Aesop.runTacticMAsTermElabM, Aesop.runTacticMAsElabM, Aesop.withFullElaboration, Aesop.elabRuleTermForApplyLikeCore, Aesop.elabRuleTermForApplyLikeMetaM, Aesop.elabRuleTermForApplyLike, Aesop.elabSimpTheorems, Aesop.mkSimpArgs, Aesop.elabRuleTermForSimpCore, Aesop.checkElabRuleTermForSimp, Aesop.elabRuleTermForSimpMetaM
statement: formalized
proof: formalized
---

# ElabRuleTerm

`Aesop.RuleTac.ElabRuleTerm`, in [Aesop/RuleTac/ElabRuleTerm.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean), by Jannis Limperg.

`Aesop.elabGlobalRuleIdent?` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L19))

```lean
def elabGlobalRuleIdent? (stx : Term) : TermElabM (Option Name)
```

`Aesop.matchInductiveTypeSynonym?` (definition, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L29))

```lean
def matchInductiveTypeSynonym? (decl : Name) : MetaM (Option InductiveVal)
```

`Aesop.elabInductiveRuleIdent?` (definition, [line 46](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L46))

> Elaborate an identifier for a rule that applies to inductive types, e.g.
> `cases`. The identifier must unambiguously refer to a global constant that is
> either an inductive type or reduces to one. For the reduction test, we use
> the larger transparency among `default` and `md`.

```lean
def elabInductiveRuleIdent? (stx : Term) (md : TransparencyMode) :
    TermElabM (Option (Name × InductiveVal))
```

`Aesop.runTacticMAsTermElabM` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L60))

```lean
def runTacticMAsTermElabM (goal : MVarId) (x : TacticM α) : TermElabM α
```

`Aesop.runTacticMAsElabM` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L65))

```lean
def runTacticMAsElabM (x : TacticM α) : ElabM α
```

`Aesop.withFullElaboration` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L68))

```lean
def withFullElaboration (x : TermElabM α) : TermElabM α
```

`Aesop.elabRuleTermForApplyLikeCore` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L71))

```lean
def elabRuleTermForApplyLikeCore (goal : MVarId) (stx : Term): TermElabM Expr
```

`Aesop.elabRuleTermForApplyLikeMetaM` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L75))

```lean
def elabRuleTermForApplyLikeMetaM (goal : MVarId) (stx : Term) : MetaM Expr
```

`Aesop.elabRuleTermForApplyLike` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L78))

```lean
def elabRuleTermForApplyLike (stx : Term) : ElabM Expr
```

`Aesop.elabSimpTheorems` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L82))

```lean
def elabSimpTheorems (stx : Syntax) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (isSimpAll : Bool) :
    TacticM (Simp.Context × Simp.SimprocsArray)
```

`Aesop.mkSimpArgs` (definition, [line 96](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L96))

```lean
def mkSimpArgs (simpTheorem : Term) : Syntax
```

`Aesop.elabRuleTermForSimpCore` (definition, [line 104](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L104))

```lean
def elabRuleTermForSimpCore (goal : MVarId) (term : Term) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (isSimpAll : Bool) :
    TermElabM (Simp.Context × Simp.SimprocsArray)
```

`Aesop.checkElabRuleTermForSimp` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L110))

```lean
def checkElabRuleTermForSimp (term : Term) (isSimpAll : Bool) : ElabM Unit
```

`Aesop.elabRuleTermForSimpMetaM` (definition, [line 115](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean#L115))

```lean
def elabRuleTermForSimpMetaM (goal : MVarId) (term : Term) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (isSimpAll : Bool) :
    MetaM (Simp.Context × Simp.SimprocsArray)
```

## Depends on

- [ElabM](../../part-02/elabm.md)

## Sources

- [Aesop/RuleTac/ElabRuleTerm.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/ElabRuleTerm.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.ElabRuleTerm.json)
