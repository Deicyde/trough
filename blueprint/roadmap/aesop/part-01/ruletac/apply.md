---
catalog: module
lean: Aesop.RuleTac.applyExpr', Aesop.RuleTac.applyExpr, Aesop.RuleTac.applyConst, Aesop.RuleTac.applyTerm, Aesop.RuleTac.apply, Aesop.RuleTac.applyConsts
statement: formalized
proof: formalized
---

# RuleTac/Apply

`Aesop.RuleTac.Apply`, in [Aesop/RuleTac/Apply.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean), by Jannis Limperg.

`Aesop.RuleTac.applyExpr'` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L21))

```lean
def applyExpr' (goal : MVarId) (e : Expr) (eStx : Term)
    (patSubst? : Option Substitution) (md : TransparencyMode) :
    BaseM RuleApplication
```

`Aesop.RuleTac.applyExpr` (definition, [line 47](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L47))

```lean
def applyExpr (goal : MVarId) (e : Expr) (eStx : Term)
    (patSubsts? : Option (Array Substitution)) (md : TransparencyMode) :
    BaseM RuleTacOutput
```

`Aesop.RuleTac.applyConst` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L68))

```lean
def applyConst (decl : Name) (md : TransparencyMode) :
    RuleTac
```

`Aesop.RuleTac.applyTerm` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L73))

```lean
def applyTerm (stx : Term) (md : TransparencyMode) : RuleTac
```

`Aesop.RuleTac.apply` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L78))

```lean
def apply (t : RuleTerm) (md : TransparencyMode) : RuleTac
```

`Aesop.RuleTac.applyConsts` (definition, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean#L85))

```lean
def applyConsts (decls : Array Name) (md : TransparencyMode) :
    RuleTac
```

## Depends on

- [Rule Tactic Types](basic.md)
- [ElabRuleTerm](elabruleterm.md)
- [RuleTerm](ruleterm.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/RuleTac/Apply.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Apply.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.Apply.json)
