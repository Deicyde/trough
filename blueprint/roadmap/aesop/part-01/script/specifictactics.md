---
catalog: module
lean: Aesop.Script.Tactic.skip, Aesop.Script.TacticBuilder.applyStx, Aesop.Script.TacticBuilder.apply, Aesop.Script.TacticBuilder.exactFVar, Aesop.Script.TacticBuilder.replace, Aesop.Script.TacticBuilder.assertHypothesis, Aesop.Script.TacticBuilder.clear, Aesop.Script.TacticBuilder.cases, Aesop.Script.TacticBuilder.obtain, Aesop.Script.TacticBuilder.casesOrObtain, Aesop.Script.TacticBuilder.renameInaccessibleFVars, Aesop.Script.TacticBuilder.unfold, Aesop.Script.TacticBuilder.unfoldAt, Aesop.Script.TacticBuilder.extN, Aesop.Script.TacticBuilder.simpAllOrSimpAtStarOnly, Aesop.Script.TacticBuilder.simpAllOrSimpAtStar, Aesop.Script.TacticBuilder.intros, Aesop.Script.TacticBuilder.splitTarget, Aesop.Script.TacticBuilder.splitAt, Aesop.Script.TacticBuilder.substFVars, Aesop.Script.TacticBuilder.substFVars', Aesop.assertHypothesisS, Aesop.applyS, Aesop.replaceFVarS, Aesop.clearS, Aesop.tryClearS, Aesop.tryClearManyS, Aesop.tryCasesS, Aesop.renameInaccessibleFVarsS, Aesop.unfoldManyTargetS, Aesop.unfoldManyAtS, Aesop.unfoldManyStarS, Aesop.introsS, Aesop.introsUnfoldingS, Aesop.straightLineExtS, Aesop.tryExactFVarS, Aesop.splitTargetS?, Aesop.splitFirstHypothesisS?
statement: formalized
proof: formalized
---

# SpecificTactics

`Aesop.Script.SpecificTactics`, in [Aesop/Script/SpecificTactics.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean), by Jannis Limperg.

`Aesop.Script.Tactic.skip` (definition, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L30))

```lean
def Tactic.skip : Tactic
```

`Aesop.Script.TacticBuilder.applyStx` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L35))

```lean
def applyStx (e : Term) (md : TransparencyMode) : TacticBuilder
```

`Aesop.Script.TacticBuilder.apply` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L39))

```lean
def apply (mvarId : MVarId) (e : Expr) (md : TransparencyMode) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.exactFVar` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L45))

```lean
def exactFVar (goal : MVarId) (fvarId : FVarId) (md : TransparencyMode) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.replace` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L51))

```lean
def replace (preGoal postGoal : MVarId) (fvarId : FVarId) (type : Expr)
    (proof : Expr) : TacticBuilder
```

`Aesop.Script.TacticBuilder.assertHypothesis` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L59))

```lean
def assertHypothesis (goal : MVarId) (h : Hypothesis) (md : TransparencyMode) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.clear` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L65))

```lean
def clear (goal : MVarId) (fvarIds : Array FVarId) : TacticBuilder
```

`Aesop.Script.TacticBuilder.cases` (definition, [line 70](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L70))

```lean
def cases (goal : MVarId) (e : Expr) (ctorNames : Array CtorNames) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.obtain` (definition, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L85))

```lean
def obtain (goal : MVarId) (e : Expr) (ctorNames : CtorNames) : TacticBuilder
```

`Aesop.Script.TacticBuilder.casesOrObtain` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L90))

```lean
def casesOrObtain (goal : MVarId) (e : Expr) (ctorNames : Array CtorNames) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.renameInaccessibleFVars` (definition, [line 97](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L97))

```lean
def renameInaccessibleFVars (postGoal : MVarId) (renamedFVars : Array FVarId) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.unfold` (definition, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L108))

```lean
def unfold (usedDecls : Array Name) (aesopUnfold : Bool) : TacticBuilder
```

`Aesop.Script.TacticBuilder.unfoldAt` (definition, [line 117](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L117))

```lean
def unfoldAt (goal : MVarId) (fvarId : FVarId) (usedDecls : Array Name)
    (aesopUnfold : Bool) : TacticBuilder
```

`Aesop.Script.TacticBuilder.extN` (definition, [line 130](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L130))

```lean
def extN (r : ExtResult) : TacticBuilder
```

`Aesop.Script.TacticBuilder.simpAllOrSimpAtStarOnly` (definition, [line 166](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L166))

```lean
def simpAllOrSimpAtStarOnly (simpAll : Bool) (inGoal : MVarId)
    (configStx? : Option Term) (usedTheorems : Simp.UsedSimps) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.simpAllOrSimpAtStar` (definition, [line 180](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L180))

```lean
def simpAllOrSimpAtStar (simpAll : Bool) (inGoal : MVarId)
    (configStx? : Option Term) (usedTheorems : Simp.UsedSimps) :
    TacticBuilder
```

`Aesop.Script.TacticBuilder.intros` (definition, [line 204](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L204))

```lean
def intros (postGoal : MVarId) (newFVarIds : Array FVarId)
    (md : TransparencyMode) : TacticBuilder
```

`Aesop.Script.TacticBuilder.splitTarget` (definition, [line 212](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L212))

```lean
def splitTarget : TacticBuilder
```

`Aesop.Script.TacticBuilder.splitAt` (definition, [line 215](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L215))

```lean
def splitAt (goal : MVarId) (fvarId : FVarId) : TacticBuilder
```

`Aesop.Script.TacticBuilder.substFVars` (definition, [line 220](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L220))

```lean
def substFVars (goal : MVarId) (fvarIds : Array FVarId) : TacticBuilder
```

`Aesop.Script.TacticBuilder.substFVars'` (definition, [line 226](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L226))

```lean
def substFVars' (fvarUserNames : Array Name) : TacticBuilder
```

`Aesop.assertHypothesisS` (definition, [line 235](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L235))

```lean
def assertHypothesisS (goal : MVarId) (h : Hypothesis) (md : TransparencyMode) :
    ScriptM (MVarId × Array FVarId)
```

`Aesop.applyS` (definition, [line 243](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L243))

```lean
def applyS (goal : MVarId) (e : Expr) (eStx? : Option Term)
    (md : TransparencyMode) : ScriptM (Array MVarId)
```

`Aesop.replaceFVarS` (definition, [line 253](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L253))

```lean
def replaceFVarS (goal : MVarId) (fvarId : FVarId) (type : Expr) (proof : Expr) :
    ScriptM (MVarId × FVarId × Bool)
```

`Aesop.clearS` (definition, [line 260](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L260))

```lean
def clearS (goal : MVarId) (fvarId : FVarId) : ScriptM MVarId
```

`Aesop.tryClearS` (definition, [line 266](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L266))

```lean
def tryClearS (goal : MVarId) (fvarId : FVarId) : ScriptM (Option MVarId)
```

`Aesop.tryClearManyS` (definition, [line 272](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L272))

```lean
def tryClearManyS (goal : MVarId) (fvarIds : Array FVarId) :
    ScriptM (MVarId × Array FVarId)
```

`Aesop.tryCasesS` (definition, [line 279](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L279))

```lean
def tryCasesS (goal : MVarId) (fvarId : FVarId) (ctorNames : Array CtorNames) :
    ScriptM (Option (Array CasesSubgoal))
```

`Aesop.renameInaccessibleFVarsS` (definition, [line 294](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L294))

```lean
def renameInaccessibleFVarsS (goal : MVarId) :
    ScriptM (MVarId × Array FVarId)
```

`Aesop.unfoldManyTargetS` (definition, [line 302](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L302))

```lean
def unfoldManyTargetS (unfold? : Name → Option (Option Name)) (goal : MVarId) :
    ScriptM (Option (MVarId × Array Name))
```

`Aesop.unfoldManyAtS` (definition, [line 318](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L318))

```lean
def unfoldManyAtS (unfold? : Name → Option (Option Name)) (goal : MVarId)
    (fvarId : FVarId) : ScriptM (Option (MVarId × Array Name))
```

`Aesop.unfoldManyStarS` (definition, [line 334](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L334))

```lean
def unfoldManyStarS (goal : MVarId) (unfold? : Name → Option (Option Name))  :
    ScriptM (Option MVarId)
```

`Aesop.introsS` (definition, [line 351](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L351))

```lean
def introsS (goal : MVarId) : ScriptM (MVarId × Array FVarId)
```

`Aesop.introsUnfoldingS` (definition, [line 359](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L359))

```lean
def introsUnfoldingS (goal : MVarId) (md : TransparencyMode) :
    ScriptM (MVarId × Array FVarId)
```

`Aesop.straightLineExtS` (definition, [line 369](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L369))

```lean
def straightLineExtS (goal : MVarId) : ScriptM ExtResult
```

`Aesop.tryExactFVarS` (definition, [line 375](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L375))

```lean
def tryExactFVarS (goal : MVarId) (fvarId : FVarId) (md : TransparencyMode) :
    ScriptM Bool
```

`Aesop.splitTargetS?` (definition, [line 398](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L398))

```lean
def splitTargetS? (goal : MVarId) :
    ScriptM (Option (Array MVarId))
```

`Aesop.splitFirstHypothesisS?` (definition, [line 407](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean#L407))

```lean
def splitFirstHypothesisS? (goal : MVarId) :
    ScriptM (Option (Array MVarId))
```

## Depends on

- [CtorNames](ctornames.md)
- [ScriptM](scriptm.md)
- [Util/Tactic](../util/tactic.md)
- [Tactic/Ext](../util/tactic-2/ext.md)
- [Util/Unfold](../util/unfold.md)

## Sources

- [Aesop/Script/SpecificTactics.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/SpecificTactics.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.SpecificTactics.json)
