---
catalog: module
lean: Aesop.Script.DynStructureM.Context, Aesop.Script.DynStructureM.State, Aesop.Script.DynStructureM.Context.updateMVarIds, Aesop.Script.DynStructureM, Aesop.Script.DynStructureM.run, Aesop.Script.withUpdatedMVarIds, Aesop.Script.DynStructureResult, Aesop.Script.structureDynamicCore, Aesop.Script.UScript.toSScriptDynamic
statement: formalized
proof: formalized
---

# StructureDynamic

`Aesop.Script.StructureDynamic`, in [Aesop/Script/StructureDynamic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean), by Jannis Limperg.

`Aesop.Script.DynStructureM.Context` (structure, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L30))

```lean
structure Context where
  /-- The tactic invocation steps corresponding to the original unstructured
  script, but with `MVarId` keys adjusted to fit the current `MetaM` state. This
  state evolves during dynamic structuring and we continually update the `steps`
  so that this map's keys refer to metavariables which exist in the current
  `MetaM` state. -/
  steps : PHashMap MVarId (Nat × Step)
  deriving Inhabited
```

`Aesop.Script.DynStructureM.State` (structure, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L39))

```lean
structure State where
  perfect : Bool := true
```

`Aesop.Script.DynStructureM.Context.updateMVarIds` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L48))

> Given a bijective map `map` from new `MVarId`s to old `MVarId`s, update the
> `steps` of the context `c` such that each entry whose key is an old `MVarId` `m`
> is replaced with an entry whose key is the corresponding new `MVarId`
> `map⁻¹ m`.

```lean
def Context.updateMVarIds (c : Context) (map : Std.HashMap MVarId MVarId) :
    Context
```

`Aesop.Script.DynStructureM` (abbreviation, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L59))

```lean
abbrev DynStructureM
```

`Aesop.Script.DynStructureM.run` (definition, [line 62](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L62))

```lean
def DynStructureM.run (x : DynStructureM α) (script : UScript) :
    MetaM (α × Bool)
```

`Aesop.Script.withUpdatedMVarIds` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L71))

```lean
def withUpdatedMVarIds
    (oldPostState newPostState : Meta.SavedState)
    (oldPostGoals newPostGoals : Array MVarId) (onFailure : DynStructureM α)
    (onSuccess : DynStructureM α) : DynStructureM α
```

`Aesop.Script.DynStructureResult` (structure, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L79))

```lean
structure DynStructureResult where
  script : List Step
  postState : Meta.SavedState
```

`Aesop.Script.structureDynamicCore` (definition, [line 83](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L83))

```lean
partial def structureDynamicCore (preState : Meta.SavedState) (preGoal : MVarId)
    (uscript : UScript) : MetaM (Option (UScript × Bool))
```

`Aesop.Script.UScript.toSScriptDynamic` (definition, [line 162](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean#L162))

```lean
def UScript.toSScriptDynamic (preState : Meta.SavedState) (preGoal : MVarId)
    (uscript : UScript) : MetaM (Option (SScript × Bool))
```

## Depends on

- [UScriptToSScript](uscripttosscript.md)
- [Util](util.md)

## Sources

- [Aesop/Script/StructureDynamic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureDynamic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.StructureDynamic.json)
