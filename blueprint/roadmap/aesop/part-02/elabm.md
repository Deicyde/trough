---
catalog: module
lean: Aesop.ElabM.Context, Aesop.ElabM.Context.forAdditionalRules, Aesop.ElabM.Context.forAdditionalGlobalRules, Aesop.ElabM.Context.forErasing, Aesop.ElabM.Context.forGlobalErasing, Aesop.ElabM, Aesop.ElabM.run, Aesop.shouldParsePriorities, Aesop.getGoal
statement: formalized
proof: formalized
---

# ElabM

`Aesop.ElabM`, in [Aesop/ElabM.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean), by Jannis Limperg.

`Aesop.ElabM.Context` (structure, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L16))

```lean
structure Context where
  parsePriorities : Bool
  goal : MVarId
```

`Aesop.ElabM.Context.forAdditionalRules` (definition, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L22))

```lean
def forAdditionalRules (goal : MVarId) : Context
```

`Aesop.ElabM.Context.forAdditionalGlobalRules` (definition, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L29))

```lean
def forAdditionalGlobalRules : MetaM Context
```

`Aesop.ElabM.Context.forErasing` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L33))

```lean
def forErasing (goal : MVarId) : Context
```

`Aesop.ElabM.Context.forGlobalErasing` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L38))

```lean
def forGlobalErasing : MetaM Context
```

`Aesop.ElabM` (abbreviation, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L45))

```lean
abbrev ElabM
```

`Aesop.ElabM.run` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L52))

```lean
protected def ElabM.run (ctx : Context) (x : ElabM α) : TermElabM α
```

`Aesop.shouldParsePriorities` (definition, [line 55](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L55))

```lean
def shouldParsePriorities : ElabM Bool
```

`Aesop.getGoal` (definition, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean#L58))

```lean
def getGoal : ElabM MVarId
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/ElabM.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/ElabM.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.ElabM.json)
