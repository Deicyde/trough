---
catalog: module
lean: Aesop.BuiltinRules.destructProductsCore, Aesop.BuiltinRules.destructProducts
statement: formalized
proof: formalized
---

# DestructProducts

`Aesop.BuiltinRules.DestructProducts`, in [Aesop/BuiltinRules/DestructProducts.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/DestructProducts.lean), by Jannis Limperg.

`Aesop.BuiltinRules.destructProductsCore` (definition, [line 86](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/DestructProducts.lean#L86))

```lean
meta partial def destructProductsCore (goal : MVarId) (md : TransparencyMode) :
    BaseM (MVarId × Array LazyStep)
```

`Aesop.BuiltinRules.destructProducts` (definition, [line 124](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/DestructProducts.lean#L124))

```lean
meta def destructProducts : RuleTac
```

## Depends on

- [Rule Tactic Types](../ruletac/basic.md)
- [ScriptM](../script/scriptm.md)

## Proof depends on

- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/BuiltinRules/DestructProducts.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/BuiltinRules/DestructProducts.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.BuiltinRules.DestructProducts.json)
