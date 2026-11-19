---
catalog: module
lean: Aesop.Frontend.AttrConfig, Aesop.Frontend.AttrConfig.«elab»
statement: formalized
proof: formalized
---

# Attribute

`Aesop.Frontend.Attribute`, in [Aesop/Frontend/Attribute.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Attribute.lean), by Jannis Limperg.

`Aesop.Frontend.AttrConfig` (structure, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Attribute.lean#L29))

```lean
structure AttrConfig where
  rules : Array RuleExpr
  deriving Inhabited
```

`Aesop.Frontend.AttrConfig.«elab»` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Attribute.lean#L35))

```lean
def «elab» (stx : Syntax) : TermElabM AttrConfig
```

## Depends on

- [RuleExpr](ruleexpr.md)

## Proof depends on

- [Frontend/Extension](extension.md)

## Sources

- [Aesop/Frontend/Attribute.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Frontend/Attribute.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Frontend.Attribute.json)
