---
catalog: module
lean: Aesop.SimpResult, Aesop.SimpResult.newGoal?, Aesop.addLetDeclsToSimpTheorems, Aesop.addLetDeclsToSimpTheoremsUnlessZetaDelta, Aesop.simpGoal, Aesop.simpGoalWithAllHypotheses, Aesop.simpAll
statement: formalized
proof: formalized
---

# Simp

`Aesop.Search.Expansion.Simp`, in [Aesop/Search/Expansion/Simp.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean), by Jannis Limperg.

`Aesop.SimpResult` (inductive type, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L17))

```lean
inductive SimpResult
  | solved (usedTheorems : Simp.UsedSimps)
  | unchanged
  | simplified (newGoal : MVarId) (usedTheorems : UsedSimps)
```

`Aesop.SimpResult.newGoal?` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L24))

```lean
def newGoal? : SimpResult → Option MVarId
```

`Aesop.addLetDeclsToSimpTheorems` (definition, [line 43](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L43))

> Add all `let` hypotheses in the local context as `simp` theorems.
>
> Background: by default, in the goal `x : _ := v ⊢ P[x]`, `simp` does not
> substitute `x` by `v` in the target. The `simp` option `zetaDelta` can be used
> to make `simp` perform this substitution, but we don't want to set it because
> then Aesop `simp` would diverge from default `simp`, so we would have to adjust
> the `aesop?` output as well. Instead, we add `let` hypotheses explicitly. This
> way, `simp?` picks them up as well.
>
> See lean4#3520.

```lean
def addLetDeclsToSimpTheorems (ctx : Simp.Context) : MetaM Simp.Context
```

`Aesop.addLetDeclsToSimpTheoremsUnlessZetaDelta` (definition, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L53))

```lean
def addLetDeclsToSimpTheoremsUnlessZetaDelta (ctx : Simp.Context) :
    MetaM Simp.Context
```

`Aesop.simpGoal` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L60))

```lean
def simpGoal (mvarId : MVarId) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (discharge? : Option Simp.Discharge := none)
    (simplifyTarget : Bool := true) (fvarIdsToSimp : Array FVarId := #[])
    (stats : Simp.Stats := {}) : MetaM SimpResult
```

`Aesop.simpGoalWithAllHypotheses` (definition, [line 77](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L77))

```lean
def simpGoalWithAllHypotheses (mvarId : MVarId) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (discharge? : Option Simp.Discharge := none)
    (simplifyTarget : Bool := true) (stats : Simp.Stats := {}) :
    MetaM SimpResult
```

`Aesop.simpAll` (definition, [line 92](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean#L92))

```lean
def simpAll (mvarId : MVarId) (ctx : Simp.Context)
    (simprocs : Simp.SimprocsArray) (stats : Simp.Stats := {}) :
    MetaM SimpResult
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Search/Expansion/Simp.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Search/Expansion/Simp.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Search.Expansion.Simp.json)
