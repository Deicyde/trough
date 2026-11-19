---
catalog: module
lean: Aesop.RuleBuilder.hasConst, Aesop.RuleBuilder.checkUnfoldableConst, Aesop.RuleBuilder.unfoldCore, Aesop.RuleBuilder.unfold
statement: formalized
proof: formalized
---

# Builder/Unfold

`Aesop.Builder.Unfold`, in [Aesop/Builder/Unfold.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean), by Jannis Limperg.

`Aesop.RuleBuilder.hasConst` (definition, [line 19](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean#L19))

```lean
def hasConst (c : Name) (e : Expr) : Bool
```

`Aesop.RuleBuilder.checkUnfoldableConst` (definition, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean#L22))

```lean
def checkUnfoldableConst (decl : Name) : MetaM (Option Name)
```

`Aesop.RuleBuilder.unfoldCore` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean#L39))

```lean
def unfoldCore (decl : Name) : MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.unfold` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean#L44))

```lean
def unfold : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)
- [Util/Unfold](../util/unfold.md)

## Sources

- [Aesop/Builder/Unfold.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/Unfold.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.Unfold.json)
