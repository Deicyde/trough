---
catalog: module
lean: Aesop.replaceFVar, Aesop.introsUnfolding
statement: formalized
proof: formalized
---

# Util/Tactic

`Aesop.Util.Tactic`, in [Aesop/Util/Tactic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic.lean), by Jannis Limperg.

`Aesop.replaceFVar` (definition, [line 26](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic.lean#L26))

> A `MetaM` version of the `replace` tactic. If `fvarId` refers to the
> hypothesis `h`, this tactic asserts a new hypothesis `h : type` with proof
> `proof : type` and then tries to clear `fvarId`. Unlike `replaceLocalDecl`,
> `replaceFVar` always adds the new hypothesis at the end of the local context.
>
> `replaceFVar` returns the new goal, the `FVarId` of the newly asserted
> hypothesis and whether the old hypothesis was cleared.

```lean
def replaceFVar (goal : MVarId) (fvarId : FVarId) (type : Expr) (proof : Expr) :
    MetaM (MVarId × FVarId × Bool)
```

`Aesop.introsUnfolding` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic.lean#L37))

> Introduce as many binders as possible while unfolding definitions with the
> ambient transparency.

```lean
partial def introsUnfolding (mvarId : MVarId) : MetaM (Array FVarId × MVarId)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/Tactic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/Tactic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.Tactic.json)
