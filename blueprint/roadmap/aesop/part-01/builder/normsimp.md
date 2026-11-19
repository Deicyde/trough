---
catalog: module
lean: Aesop.PhaseSpec.getSimpPrio, Aesop.RuleBuilder.simpCore, Aesop.RuleBuilder.simp
statement: formalized
proof: formalized
---

# NormSimp

`Aesop.Builder.NormSimp`, in [Aesop/Builder/NormSimp.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/NormSimp.lean), by Jannis Limperg.

`Aesop.PhaseSpec.getSimpPrio` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/NormSimp.lean#L31))

```lean
def PhaseSpec.getSimpPrio [Monad m] [MonadError m] : PhaseSpec → m Nat
```

`Aesop.RuleBuilder.simpCore` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/NormSimp.lean#L41))

```lean
def simpCore (decl : Name) (phase : PhaseSpec) : MetaM LocalRuleSetMember
```

`Aesop.RuleBuilder.simp` (definition, [line 50](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/NormSimp.lean#L50))

```lean
def simp : RuleBuilder
```

## Depends on

- [Builder/Basic](basic.md)

## Sources

- [Aesop/Builder/NormSimp.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Builder/NormSimp.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Builder.NormSimp.json)
