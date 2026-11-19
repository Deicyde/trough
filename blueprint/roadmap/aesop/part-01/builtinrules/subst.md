---
catalog: module
lean: Aesop.BuiltinRules.matchSubstitutableIff?, Aesop.BuiltinRules.prepareIff?, Aesop.BuiltinRules.prepareIffs, Aesop.BuiltinRules.substEqs?, Aesop.BuiltinRules.substEqsAndIffs?, Aesop.BuiltinRules.subst
statement: formalized
proof: formalized
---

# Subst

`Aesop.BuiltinRules.Subst`, in [Aesop/BuiltinRules/Subst.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean), by Jannis Limperg.

`Aesop.BuiltinRules.matchSubstitutableIff?` (definition, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L17))

```lean
meta def matchSubstitutableIff? (e : Expr) : Option (Expr × Expr)
```

`Aesop.BuiltinRules.prepareIff?` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L25))

```lean
meta def prepareIff? (mvarId : MVarId) (fvarId : FVarId) :
    ScriptM (Option (MVarId × FVarId))
```

`Aesop.BuiltinRules.prepareIffs` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L41))

```lean
meta def prepareIffs (mvarId : MVarId) (fvarIds : Array FVarId) :
    ScriptM (MVarId × Array FVarId)
```

`Aesop.BuiltinRules.substEqs?` (definition, [line 53](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L53))

```lean
meta def substEqs? (goal : MVarId) (fvarIds : Array FVarId) :
    ScriptM (Option MVarId)
```

`Aesop.BuiltinRules.substEqsAndIffs?` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L76))

```lean
meta def substEqsAndIffs? (goal : MVarId) (fvarIds : Array FVarId) :
    ScriptM (Option MVarId)
```

`Aesop.BuiltinRules.subst` (definition, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean#L87))

```lean
meta def subst : RuleTac
```

## Depends on

- [Rule Tactic Types](../ruletac/basic.md)
- [Forward/Basic](../ruletac/forward-2/basic.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/BuiltinRules/Subst.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/Subst.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.BuiltinRules.Subst.json)
