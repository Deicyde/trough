---
catalog: module
lean: Aesop.EqualUpToIdsM.Context, Aesop.EqualUpToIdsM.State, Aesop.EqualUpToIdsM, Aesop.EqualUpToIdsM.run', Aesop.EqualUpToIdsM.run, Aesop.EqualUpToIds.readCommonMCtx?, Aesop.EqualUpToIds.readMCtx₁, Aesop.EqualUpToIds.readMCtx₂, Aesop.EqualUpToIds.readAllowAssignmentDiff, Aesop.EqualUpToIds.equalCommonLMVars?, Aesop.EqualUpToIds.equalCommonMVars?, Aesop.EqualUpToIds.GoalContext, Aesop.EqualUpToIds.MVarValue, Aesop.EqualUpToIds.Unsafe.levelsEqualUpToIdsCore, Aesop.EqualUpToIds.Unsafe.levelsEqualUpToIdsCore', Aesop.EqualUpToIds.levelsEqualUpToIdsCore, Aesop.EqualUpToIds.ExprsEqualUpToIdsM, Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₁, Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₂, Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₃, Aesop.EqualUpToIds.Unsafe.localDeclsEqualUpToIdsCore, Aesop.EqualUpToIds.Unsafe.localContextsEqualUpToIdsCore, Aesop.EqualUpToIds.Unsafe.unassignedMVarsEqualUpToIdsCore, Aesop.EqualUpToIds.exprsEqualUpToIdsCore, Aesop.EqualUpToIds.unassignedMVarsEqualUpToIdsCore, Aesop.EqualUpToIds.tacticStatesEqualUpToIdsCore, Aesop.exprsEqualUpToIds, Aesop.exprsEqualUpToIds', Aesop.unassignedMVarsEqualUptoIds, Aesop.unassignedMVarsEqualUptoIds', Aesop.tacticStatesEqualUpToIds, Aesop.tacticStatesEqualUpToIds'
statement: formalized
proof: formalized
---

# EqualUpToIds

`Aesop.Util.EqualUpToIds`, in [Aesop/Util/EqualUpToIds.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean), by Jannis Limperg.

`Aesop.EqualUpToIdsM.Context` (structure, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L22))

```lean
structure Context where
  commonMCtx? : Option MetavarContext
  mctx₁ : MetavarContext
  mctx₂ : MetavarContext
  /-- Allow metavariables to be unassigned on one side of the comparison and
  assigned on the other. So when we compare two expressions and we encounter
  a metavariable `?x` in one of them and a subexpression `e` in the other (at
  the same position), we consider `?x` equal to `e`. -/
  -- TODO we should also allow ?P x₁ ... xₙ = e
  allowAssignmentDiff : Bool
```

`Aesop.EqualUpToIdsM.State` (structure, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L33))

```lean
structure State where
  equalMVarIds : Std.HashMap MVarId MVarId := {}
  equalLMVarIds : Std.HashMap LMVarId LMVarId := {}
  /-- A map from metavariables which are unassigned in the left goal
  to their corresponding expression in the right goal. Only used when
  `allowAssignmentDiff = true`. -/
  leftUnassignedMVarValues : Std.HashMap MVarId Expr := {}
  /-- A map from metavariables which are unassigned in the right goal
  to their corresponding expression in the left goal. Only used when
  `allowAssignmentDiff = true`. -/
  rightUnassignedMVarValues : Std.HashMap MVarId Expr := {}
```

`Aesop.EqualUpToIdsM` (abbreviation, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L48))

```lean
abbrev EqualUpToIdsM
```

`Aesop.EqualUpToIdsM.run'` (definition, [line 57](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L57))

```lean
protected def EqualUpToIdsM.run' (x : EqualUpToIdsM α)
    (commonMCtx? : Option MetavarContext) (mctx₁ mctx₂ : MetavarContext)
    (allowAssignmentDiff : Bool) :
    MetaM (α × EqualUpToIdsM.State)
```

`Aesop.EqualUpToIdsM.run` (definition, [line 63](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L63))

```lean
protected def EqualUpToIdsM.run (x : EqualUpToIdsM α)
    (commonMCtx? : Option MetavarContext) (mctx₁ mctx₂ : MetavarContext)
    (allowAssignmentDiff : Bool) : MetaM α
```

`Aesop.EqualUpToIds.readCommonMCtx?` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L71))

```lean
def readCommonMCtx? : EqualUpToIdsM (Option MetavarContext)
```

`Aesop.EqualUpToIds.readMCtx₁` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L75))

```lean
def readMCtx₁ : EqualUpToIdsM MetavarContext
```

`Aesop.EqualUpToIds.readMCtx₂` (definition, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L79))

```lean
def readMCtx₂ : EqualUpToIdsM MetavarContext
```

`Aesop.EqualUpToIds.readAllowAssignmentDiff` (definition, [line 83](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L83))

```lean
def readAllowAssignmentDiff : EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.equalCommonLMVars?` (definition, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L87))

```lean
def equalCommonLMVars? (lmvarId₁ lmvarId₂ : LMVarId) :
    EqualUpToIdsM (Option Bool)
```

`Aesop.EqualUpToIds.equalCommonMVars?` (definition, [line 98](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L98))

```lean
def equalCommonMVars? (mvarId₁ mvarId₂ : MVarId) :
    EqualUpToIdsM (Option Bool)
```

`Aesop.EqualUpToIds.GoalContext` (structure, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L108))

```lean
structure GoalContext where
  lctx₁ : LocalContext
  localInstances₁ : LocalInstances
  lctx₂ : LocalContext
  localInstances₂ : LocalInstances
  equalFVarIds : Std.HashMap FVarId FVarId := {}
```

`Aesop.EqualUpToIds.MVarValue` (inductive type, [line 115](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L115))

```lean
inductive MVarValue where
  | mvarId (mvarId : MVarId)
  | expr (e : Expr)
  | delayedAssignment (da : DelayedMetavarAssignment)
```

`Aesop.EqualUpToIds.Unsafe.levelsEqualUpToIdsCore` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L129))

```lean
unsafe def levelsEqualUpToIdsCore (l₁ l₂ : Level) : EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.Unsafe.levelsEqualUpToIdsCore'` (definition, [line 136](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L136))

```lean
unsafe def levelsEqualUpToIdsCore' : Level → Level → EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.levelsEqualUpToIdsCore` (opaque constant, [line 159](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L159))

```lean
opaque levelsEqualUpToIdsCore (l₁ l₂ : Level) : EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.ExprsEqualUpToIdsM` (abbreviation, [line 166](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L166))

```lean
abbrev ExprsEqualUpToIdsM
```

`Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₁` (definition, [line 174](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L174))

```lean
unsafe def exprsEqualUpToIdsCore₁ (e₁ e₂ : Expr) :
    ReaderT GoalContext EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₂` (definition, [line 181](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L181))

```lean
unsafe def exprsEqualUpToIdsCore₂ (e₁ e₂ : Expr) : ExprsEqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.Unsafe.exprsEqualUpToIdsCore₃` (definition, [line 203](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L203))

```lean
unsafe def exprsEqualUpToIdsCore₃ : Expr → Expr → ExprsEqualUpToIdsM Bool
  | .bvar i, .bvar j => return i == j
  | .fvar fvarId₁, .fvar fvarId₂ =>
    return fvarId₁ == fvarId₂ ||
           (← read).equalFVarIds[fvarId₁]? == some fvarId₂
  | .sort u, .sort v => levelsEqualUpToIdsCore u v
  | .const decl₁ lvls₁, .const decl₂ lvls₂ => do
    if decl₁ == decl₂ && lvls₁.length == lvls₂.length then
      for l₁ in lvls₁, l₂ in lvls₂ do
        if ! (← levelsEqualUpToIdsCore l₁ l₂) then
          return false
      return true
    else
      return false
  | .app f₁ x₁, .app f₂ x₂ =>
    exprsEqualUpToIdsCore₂ f₁ f₂ <&&> exprsEqualUpToIdsCore₂ x₁ x₂
  | .lam n₁ t₁ e₁ bi₁, .lam n₂ t₂ e₂ bi₂ =>
    pure (namesEqualUpToMacroScopes n₁ n₂ && bi₁ == bi₂) <&&>
    exprsEqualUpToIdsCore₂ t₁ t₂ <&&>
    exprsEqualUpToIdsCore₂ e₁ e₂
  | .forallE n₁ t₁ e₁ bi₁, .forallE n₂ t₂ e₂ bi₂ =>
    pure (namesEqualUpToMacroScopes n₁ n₂ && bi₁ == bi₂) <&&>
    exprsEqualUpToIdsCore₂ t₁ t₂ <&&>
    exprsEqualUpToIdsCore₂ e₁ e₂
  | .letE n₁ t₁ v₁ e₁ _, .letE n₂ t₂ v₂ e₂ _ =>
    pure (namesEqualUpToMacroScopes n₁ n₂) <&&>
    exprsEqualUpToIdsCore₂ t₁ t₂ <&&>
    exprsEqualUpToIdsCore₂ v₁ v₂ <&&>
    exprsEqualUpToIdsCore₂ e₁ e₂
  | .lit l₁, .lit l₂ => return l₁ == l₂
  | .mdata _ e₁, e₂ => exprsEqualUpToIdsCore₂ e₁ e₂
  | e₁, .mdata _ e₂ => exprsEqualUpToIdsCore₂ e₁ e₂
  | .proj n₁ i₁ e₁, .proj n₂ i₂ e₂ =>
    pure (n₁ == n₂ && i₁ == i₂) <&&> exprsEqualUpToIdsCore₂ e₁ e₂
  | .mvar m₁, .mvar m₂ => do
    let v₁ ← normalizeMVar (← readMCtx₁) m₁
    let v₂ ← normalizeMVar (← readMCtx₂) m₂
    compareMVarValues v₁ v₂
  | .mvar m₁, e₂ => do
    let v₁ ← normalizeMVar (← readMCtx₁) m₁
    compareMVarValues v₁ (.expr e₂)
  | e₁, .mvar m₂ => do
    let v₂ ← normalizeMVar (← readMCtx₂) m₂
    compareMVarValues (.expr e₁) v₂
  | _, _ => return false
```

`Aesop.EqualUpToIds.Unsafe.localDeclsEqualUpToIdsCore` (definition, [line 290](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L290))

```lean
unsafe def localDeclsEqualUpToIdsCore (ldecl₁ ldecl₂ : LocalDecl) :
    ReaderT GoalContext EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.Unsafe.localContextsEqualUpToIdsCore` (definition, [line 305](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L305))

```lean
unsafe def localContextsEqualUpToIdsCore (lctx₁ lctx₂ : LocalContext)
    (localInstances₁ localInstances₂ : LocalInstances) :
    EqualUpToIdsM (Option GoalContext)
```

`Aesop.EqualUpToIds.Unsafe.unassignedMVarsEqualUpToIdsCore` (definition, [line 332](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L332))

```lean
unsafe def unassignedMVarsEqualUpToIdsCore (mvarId₁ mvarId₂ : MVarId) :
    EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.exprsEqualUpToIdsCore` (opaque constant, [line 368](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L368))

```lean
opaque exprsEqualUpToIdsCore (e₁ e₂ : Expr) : ReaderT GoalContext EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.unassignedMVarsEqualUpToIdsCore` (opaque constant, [line 371](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L371))

```lean
opaque unassignedMVarsEqualUpToIdsCore (mvarId₁ mvarId₂ : MVarId) :
    EqualUpToIdsM Bool
```

`Aesop.EqualUpToIds.tacticStatesEqualUpToIdsCore` (definition, [line 375](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L375))

```lean
def tacticStatesEqualUpToIdsCore (goals₁ goals₂ : Array MVarId) :
    EqualUpToIdsM Bool
```

`Aesop.exprsEqualUpToIds` (definition, [line 386](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L386))

```lean
def exprsEqualUpToIds (mctx₁ mctx₂ : MetavarContext)
    (lctx₁ lctx₂ : LocalContext)
    (localInstances₁ localInstances₂ : LocalInstances) (e₁ e₂ : Expr)
    (allowAssignmentDiff := false) : MetaM Bool
```

`Aesop.exprsEqualUpToIds'` (definition, [line 394](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L394))

```lean
def exprsEqualUpToIds' (e₁ e₂ : Expr) (allowAssignmentDiff := false) :
    MetaM Bool
```

`Aesop.unassignedMVarsEqualUptoIds` (definition, [line 402](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L402))

```lean
def unassignedMVarsEqualUptoIds (commonMCtx? : Option MetavarContext)
    (mctx₁ mctx₂ : MetavarContext) (mvarId₁ mvarId₂ : MVarId)
    (allowAssignmentDiff := false) : MetaM Bool
```

`Aesop.unassignedMVarsEqualUptoIds'` (definition, [line 408](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L408))

```lean
def unassignedMVarsEqualUptoIds' (commonMCtx? : Option MetavarContext)
    (mctx₁ mctx₂ : MetavarContext) (mvarId₁ mvarId₂ : MVarId)
    (allowAssignmentDiff := false) :
    MetaM (Bool × EqualUpToIdsM.State)
```

`Aesop.tacticStatesEqualUpToIds` (definition, [line 415](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L415))

```lean
def tacticStatesEqualUpToIds (commonMCtx? : Option MetavarContext)
    (mctx₁ mctx₂ : MetavarContext) (goals₁ goals₂ : Array MVarId)
    (allowAssignmentDiff := false) : MetaM Bool
```

`Aesop.tacticStatesEqualUpToIds'` (definition, [line 421](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean#L421))

```lean
def tacticStatesEqualUpToIds' (commonMCtx? : Option MetavarContext)
    (mctx₁ mctx₂ : MetavarContext) (goals₁ goals₂ : Array MVarId)
    (allowAssignmentDiff := false) :
    MetaM (Bool × EqualUpToIdsM.State)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/EqualUpToIds.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/EqualUpToIds.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.EqualUpToIds.json)
