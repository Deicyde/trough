---
catalog: module
lean: Aesop.GoalDiff, Aesop.isGoalDiffDefeqExpr, Aesop.isGoalDiffDefeqTarget, Aesop.isGoalDiffDefeqLDecl, Aesop.getNewFVars, Aesop.diffGoals, Aesop.GoalDiff.comp, Aesop.GoalDiff.checkCore, Aesop.GoalDiff.check
statement: formalized
proof: formalized
---

# GoalDiff

`Aesop.RuleTac.GoalDiff`, in [Aesop/RuleTac/GoalDiff.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean), by Jannis Limperg.

`Aesop.GoalDiff` (structure, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L45))

> A representation of the differences between two goals. Each Aesop rule produces
> a `GoalDiff` between the goal on which the rule was run (the 'old goal') and
> each of the subgoals produced by the rule (the 'new goals').
>
> We use the produced `GoalDiff`s to update stateful data structures which cache
> information about Aesop goals and for which it is more efficient to update the
> cached information than to recompute it for each goal.
>
> Hypotheses are identified by their `FVarId` *and* type and value (if any).
> This means that when a hypothesis `h : T` with `FVarId` `i` appears in the old
> goal and `h : T'` with `FVarId` `i` appears in the new goal, but `T` is not
> defeq to `T'`, then `h` is treated as both added (with the new type) and
> removed (with the old type). This can happen when the type of a hyp changes to
> another type that is definitionally equal at `default`, but not at `reducible`
> transparency.
>
> The target is identified up to defeq. All defeq comparisons are made at
> reducible transparency and metavariables are treated as rigid.

```lean
structure GoalDiff where
  /-- The old goal. -/
  oldGoal : MVarId
  /-- The new goal. -/
  newGoal : MVarId
  /-- `FVarId`s that appear in the new goal, but not (or with a different type)
  in the old goal. -/
  addedFVars : Std.HashSet FVarId
  /-- `FVarId`s that appear in the old goal, but not (or with a different type)
  in the new goal. -/
  removedFVars : Std.HashSet FVarId
  /-- Is the old goal's target defeq to the new goal's target? -/
  targetChanged : Bool
  deriving Inhabited
```

`Aesop.isGoalDiffDefeqExpr` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L64))

```lean
def isGoalDiffDefeqExpr (oldExpr newExpr : Expr) : MetaM Bool
```

`Aesop.isGoalDiffDefeqTarget` (definition, [line 69](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L69))

```lean
def isGoalDiffDefeqTarget (oldGoal newGoal : MVarId) : MetaM Bool
```

`Aesop.isGoalDiffDefeqLDecl` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L73))

```lean
def isGoalDiffDefeqLDecl (oldLDecl newLDecl : LocalDecl) :
    MetaM Bool
```

`Aesop.getNewFVars` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L82))

```lean
def getNewFVars (newGoal : MVarId) (oldLCtx newLCtx : LocalContext) :
    MetaM (Std.HashSet FVarId)
```

`Aesop.diffGoals` (definition, [line 98](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L98))

> Diff two goals.

```lean
def diffGoals (oldGoal newGoal : MVarId) : BaseM GoalDiff
```

`Aesop.GoalDiff.comp` (definition, [line 121](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L121))

> If `diff₁` is the difference between goals `g₁` and `g₂` and `diff₂` is the
> difference between `g₂` and `g₃`, then `diff₁.comp diff₂` is the difference
> between `g₁` and `g₃`.
>
> We assume that a hypothesis which changed between `g₁` and `g₂` does not
> change back, i.e. the hypothesis is still different between `g₁` and `g₃`, and
> similar for the targets.

```lean
def comp (diff₁ diff₂ : GoalDiff) : GoalDiff
```

`Aesop.GoalDiff.checkCore` (definition, [line 138](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L138))

```lean
def checkCore (diff : GoalDiff) (old new : MVarId) :
    BaseM (Option MessageData)
```

`Aesop.GoalDiff.check` (definition, [line 204](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean#L204))

```lean
def check (diff : GoalDiff) (old new : MVarId) :
    BaseM (Option MessageData)
```

## Depends on

- [BaseM](../basem.md)

## Sources

- [Aesop/RuleTac/GoalDiff.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/GoalDiff.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.GoalDiff.json)
