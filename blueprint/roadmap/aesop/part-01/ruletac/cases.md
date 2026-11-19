---
catalog: module
lean: Aesop.CasesPattern.toExpr, Aesop.CasesTarget', Aesop.CasesTarget.toCasesTarget', Aesop.RuleTac.cases
statement: formalized
proof: formalized
---

# RuleTac/Cases

`Aesop.RuleTac.Cases`, in [Aesop/RuleTac/Cases.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean), by Jannis Limperg.

`Aesop.CasesPattern.toExpr` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean#L19))

```lean
def CasesPattern.toExpr (p : CasesPattern) : MetaM Expr
```

`Aesop.CasesTarget'` (inductive type, [line 23](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean#L23))

```lean
inductive CasesTarget' where
  | decl (decl : Name)
  | patterns (ps : Array (Expr × Meta.SavedState))
```

`Aesop.CasesTarget.toCasesTarget'` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean#L27))

```lean
def CasesTarget.toCasesTarget' : CasesTarget → MetaM CasesTarget'
```

`Aesop.RuleTac.cases` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean#L39))

```lean
partial def cases (target : CasesTarget) (md : TransparencyMode)
    (isRecursiveType : Bool) (ctorNames : Array CtorNames) : RuleTac
```

## Depends on

- [Rule Tactic Types](basic.md)
- [CtorNames](../script/ctornames.md)
- [ScriptM](../script/scriptm.md)

## Proof depends on

- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/RuleTac/Cases.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Cases.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.Cases.json)
