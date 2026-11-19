---
catalog: module
lean: Aesop.Script.StaticStructureM.State, Aesop.Script.StaticStructureM.Context, Aesop.Script.StaticStructureM, Aesop.Script.StaticStructureM.run, Aesop.Script.structureStaticCore, Aesop.Script.UScript.toSScriptStatic
statement: formalized
proof: formalized
---

# StructureStatic

`Aesop.Script.StructureStatic`, in [Aesop/Script/StructureStatic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean).

`Aesop.Script.StaticStructureM.State` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L16))

```lean
structure State where
  perfect : Bool := true
```

`Aesop.Script.StaticStructureM.Context` (structure, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L19))

```lean
structure Context where
  steps : Std.HashMap MVarId (Nat × Step)
```

`Aesop.Script.StaticStructureM` (abbreviation, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L24))

```lean
abbrev StaticStructureM
```

`Aesop.Script.StaticStructureM.run` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L27))

```lean
protected def StaticStructureM.run (script : UScript) (x : StaticStructureM α) :
    CoreM (α × Bool)
```

`Aesop.Script.structureStaticCore` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L39))

```lean
partial def structureStaticCore (tacticState : TacticState) (script : UScript) :
    CoreM (UScript × Bool)
```

`Aesop.Script.UScript.toSScriptStatic` (definition, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean#L72))

```lean
def UScript.toSScriptStatic (tacticState : TacticState) (uscript : UScript) :
    CoreM (SScript × Bool)
```

## Depends on

- [UScriptToSScript](uscripttosscript.md)

## Sources

- [Aesop/Script/StructureStatic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/StructureStatic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.StructureStatic.json)
