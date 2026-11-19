---
catalog: module
lean: Aesop.CtorNames, Aesop.CtorNames.toRCasesPat, Aesop.CtorNames.toInductionAltLHS, Aesop.CtorNames.toInductionAlt, Aesop.CtorNames.toAltVarNames, Aesop.CtorNames.mkFreshArgNames, Aesop.ctorNamesToRCasesPats, Aesop.ctorNamesToInductionAlts, Aesop.mkCtorNames
statement: formalized
proof: formalized
---

# CtorNames

`Aesop.Script.CtorNames`, in [Aesop/Script/CtorNames.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean).

`Aesop.CtorNames` (structure, [line 12](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L12))

```lean
structure CtorNames where
  ctor : Name
  args : Array Name
  /-- Whether the constructor has at least one implicit argument. -/
  hasImplicitArg : Bool
```

`Aesop.CtorNames.toRCasesPat` (definition, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L20))

```lean
def toRCasesPat (cn : CtorNames) : TSyntax `rcasesPat
```

`Aesop.CtorNames.toInductionAltLHS` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L34))

```lean
def toInductionAltLHS (cn : CtorNames) :
    TSyntax ``inductionAltLHS
```

`Aesop.CtorNames.toInductionAlt` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L44))

```lean
def toInductionAlt (cn : CtorNames) (tacticSeq : Array Syntax.Tactic) :
    TSyntax ``inductionAlt
```

`Aesop.CtorNames.toAltVarNames` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L48))

```lean
def toAltVarNames (cn : CtorNames) : AltVarNames
```

`Aesop.CtorNames.mkFreshArgNames` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L52))

```lean
def mkFreshArgNames (lctx : LocalContext) (cn : CtorNames) :
    CtorNames × LocalContext
```

`Aesop.ctorNamesToRCasesPats` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L60))

```lean
def ctorNamesToRCasesPats (cns : Array CtorNames) : TSyntax ``rcasesPatMed
```

`Aesop.ctorNamesToInductionAlts` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L64))

```lean
def ctorNamesToInductionAlts (cns : Array (CtorNames × Array Syntax.Tactic)) :
    TSyntax ``inductionAlts
```

`Aesop.mkCtorNames` (definition, [line 69](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean#L69))

```lean
def mkCtorNames (iv : InductiveVal) : CoreM (Array CtorNames)
```

## Depends on

- [Util/Basic](../util/basic.md)

## Sources

- [Aesop/Script/CtorNames.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Script/CtorNames.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Script.CtorNames.json)
