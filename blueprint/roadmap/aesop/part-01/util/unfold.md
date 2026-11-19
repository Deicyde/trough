---
catalog: module
lean: Aesop.mkUnfoldSimpContext, Aesop.unfoldManyCore, Aesop.unfoldMany, Aesop.unfoldManyTarget, Aesop.unfoldManyAt, Aesop.unfoldManyStar
statement: formalized
proof: formalized
---

# Util/Unfold

`Aesop.Util.Unfold`, in [Aesop/Util/Unfold.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean), by Jannis Limperg.

`Aesop.mkUnfoldSimpContext` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L21))

```lean
def mkUnfoldSimpContext : MetaM Simp.Context
```

`Aesop.unfoldManyCore` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L25))

```lean
def unfoldManyCore (ctx : Simp.Context) (unfold? : Name → Option (Option Name))
    (e : Expr) : StateRefT (Array Name) MetaM Simp.Result
```

`Aesop.unfoldMany` (definition, [line 67](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L67))

```lean
def unfoldMany (unfold? : Name → Option (Option Name)) (e : Expr) :
    MetaM (Option (Expr × Array Name))
```

`Aesop.unfoldManyTarget` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L76))

```lean
def unfoldManyTarget (unfold? : Name → Option (Option Name)) (goal : MVarId) :
    MetaM (Option (MVarId × Array Name))
```

`Aesop.unfoldManyAt` (definition, [line 86](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L86))

```lean
def unfoldManyAt (unfold? : Name → Option (Option Name)) (goal : MVarId)
    (fvarId : FVarId) : MetaM (Option (MVarId × Array Name))
```

`Aesop.unfoldManyStar` (definition, [line 99](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean#L99))

```lean
def unfoldManyStar (unfold? : Name → Option (Option Name)) (goal : MVarId) :
    MetaM (Option MVarId)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/Unfold.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Unfold.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.Unfold.json)
