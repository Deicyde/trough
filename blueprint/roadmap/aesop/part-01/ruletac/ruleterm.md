---
catalog: module
lean: Aesop.RuleTerm, Aesop.ElabRuleTerm, Aesop.ElabRuleTerm.expr, Aesop.ElabRuleTerm.scope, Aesop.ElabRuleTerm.name, Aesop.ElabRuleTerm.toRuleTerm, Aesop.ElabRuleTerm.ofElaboratedTerm
statement: formalized
proof: formalized
---

# RuleTerm

`Aesop.RuleTac.RuleTerm`, in [Aesop/RuleTac/RuleTerm.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean).

`Aesop.RuleTerm` (inductive type, [line 11](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L11))

```lean
inductive RuleTerm
  | const (decl : Name)
  | term (term : Term)
  deriving Inhabited
```

`Aesop.ElabRuleTerm` (inductive type, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L21))

```lean
inductive ElabRuleTerm
  | const (decl : Name)
  | term (term : Term) (expr : Expr)
  deriving Inhabited
```

`Aesop.ElabRuleTerm.expr` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L33))

```lean
def expr : ElabRuleTerm → MetaM Expr
```

`Aesop.ElabRuleTerm.scope` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L37))

```lean
def scope : ElabRuleTerm → ScopeName
```

`Aesop.ElabRuleTerm.name` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L41))

```lean
def name : ElabRuleTerm → MetaM Name
```

`Aesop.ElabRuleTerm.toRuleTerm` (definition, [line 45](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L45))

```lean
def toRuleTerm : ElabRuleTerm → RuleTerm
```

`Aesop.ElabRuleTerm.ofElaboratedTerm` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean#L49))

```lean
def ofElaboratedTerm (tm : Term) (expr : Expr) : ElabRuleTerm
```

## Depends on

- [Rule/Name](../rule/name.md)

## Sources

- [Aesop/RuleTac/RuleTerm.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/RuleTerm.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.RuleTerm.json)
