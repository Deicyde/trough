---
catalog: module
lean: Lean.Name.MatchUpToIndexSuffix, Lean.Name.matchUpToIndexSuffix, Lean.LocalContext.getUnusedUserNameIndex, Lean.LocalContext.getUnusedUserName, Lean.LocalContext.getUnusedUserNames, Lean.Meta.getUnusedUserName, Lean.Meta.getUnusedUserNames
statement: formalized
proof: formalized
---

# UnusedNames

`Batteries.Lean.Meta.UnusedNames`, in [Batteries/Lean/Meta/UnusedNames.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean), by Jannis Limperg.

`Lean.Name.MatchUpToIndexSuffix` (inductive type, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L27))

> Result type of `Lean.Name.matchUpToIndexSuffix`. See there for details.

```lean
inductive MatchUpToIndexSuffix
  /-- Exact match. -/
  |  exactMatch
  /-- No match. -/
  | noMatch
  /-- Match up to suffix. -/
  | suffixMatch (i : Nat)
```

`Lean.Name.matchUpToIndexSuffix` (definition, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L44))

> Succeeds if `n` is equal to `query`, except `n` may have an additional `_i`
> suffix for some natural number `i`. More specifically:
>
> - If `n = query`, the result is `exactMatch`.
> - If `n = query ++ "_i"` for some natural number `i`, the result is
>   `suffixMatch i`.
> - Otherwise the result is `noMatch`.

```lean
def matchUpToIndexSuffix (n : Name) (query : Name) :
    MatchUpToIndexSuffix
```

`Lean.LocalContext.getUnusedUserNameIndex` (definition, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L73))

> Obtain the least natural number `i` such that `suggestion ++ "_i"` is an unused
> name in the given local context. If `suggestion` itself is unused, the result
> is `none`.

```lean
def getUnusedUserNameIndex (lctx : LocalContext) (suggestion : Name) :
    Option Nat
```

`Lean.LocalContext.getUnusedUserName` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L97))

> Obtain a name `n` such that `n` is unused in the given local context and
> `suggestion` is a prefix of `n`. This is similar to `getUnusedName` but uses
> a different algorithm which may or may not be faster.

```lean
def getUnusedUserName (lctx : LocalContext) (suggestion : Name) : Name
```

`Lean.LocalContext.getUnusedUserNames` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L107))

> Obtain `n` distinct names such that each name is unused in the given local
> context and `suggestion` is a prefix of each name.

```lean
def getUnusedUserNames (lctx : LocalContext) (n : Nat) (suggestion : Name) :
    Array Name
```

`Lean.Meta.getUnusedUserName` (definition, [line 133](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L133))

> Obtain a name `n` such that `n` is unused in the current local context and
> `suggestion` is a prefix of `n`.

```lean
def getUnusedUserName [Monad m] [MonadLCtx m] (suggestion : Name) : m Name
```

`Lean.Meta.getUnusedUserNames` (definition, [line 140](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean#L140))

> Obtain `n` distinct names such that each name is unused in the current local
> context and `suggestion` is a prefix of each name.

```lean
def getUnusedUserNames [Monad m] [MonadLCtx m] (n : Nat) (suggestion : Name) :
    m (Array Name)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/Meta/UnusedNames.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/Meta/UnusedNames.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Lean.Meta.UnusedNames.json)
