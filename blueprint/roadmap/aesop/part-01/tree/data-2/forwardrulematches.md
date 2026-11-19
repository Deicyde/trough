---
catalog: module
lean: Aesop.ForwardRuleMatches, Aesop.ForwardRuleMatches.empty, Aesop.ForwardRuleMatches.insert, Aesop.ForwardRuleMatches.insertMany, Aesop.ForwardRuleMatches.erase, Aesop.ForwardRuleMatches.eraseMany, Aesop.ForwardRuleMatches.ofArray, Aesop.ForwardRuleMatches.eraseHyps, Aesop.ForwardRuleMatches.eraseHyp, Aesop.ForwardRuleMatches.update, Aesop.ForwardRuleMatches.normRules, Aesop.ForwardRuleMatches.safeRules, Aesop.ForwardRuleMatches.unsafeRules, Aesop.ForwardRuleMatches.size
statement: formalized
proof: formalized
---

# ForwardRuleMatches

`Aesop.Tree.Data.ForwardRuleMatches`, in [Aesop/Tree/Data/ForwardRuleMatches.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean), by Jannis Limperg.

`Aesop.ForwardRuleMatches` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L20))

> Sets of complete matches for norm/safe/unsafe rules.

```lean
structure ForwardRuleMatches where
  /-- Complete matches of norm rules. -/
  normMatches   : PHashSet ForwardRuleMatch
  /-- Complete matches of safe rules. -/
  safeMatches   : PHashSet ForwardRuleMatch
  /-- Complete matches of unsafe rules. -/
  unsafeMatches : PHashSet ForwardRuleMatch
  deriving Inhabited
```

`Aesop.ForwardRuleMatches.empty` (definition, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L32))

> Empty `ForwardRuleMatches`.

```lean
protected def empty : ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.insert` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L41))

> Add a complete match.

```lean
def insert (m : ForwardRuleMatch) (ms : ForwardRuleMatches) :
    ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.insertMany` (definition, [line 49](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L49))

> Add several complete matches.

```lean
def insertMany (ms : Array ForwardRuleMatch) (ms' : ForwardRuleMatches) :
    ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.erase` (definition, [line 54](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L54))

> Erase a complete match.

```lean
def erase (m : ForwardRuleMatch) (ms : ForwardRuleMatches) :
    ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.eraseMany` (definition, [line 62](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L62))

> Erase several complete matches.

```lean
def eraseMany (ms : Array ForwardRuleMatch) (ms' : ForwardRuleMatches) :
    ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.ofArray` (definition, [line 67](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L67))

> Build a `ForwardRuleMatches` structure containing the matches from `ms`.

```lean
def ofArray (ms : Array ForwardRuleMatch) : ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.eraseHyps` (definition, [line 71](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L71))

> Erase matches containing any of the hypotheses `hs` from `ms`.

```lean
def eraseHyps (hs : Std.HashSet FVarId) (ms : ForwardRuleMatches) :
    ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.eraseHyp` (definition, [line 83](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L83))

> Erase matches containing the hypothesis `h` from `ms`.

```lean
def eraseHyp (h : FVarId) (ms : ForwardRuleMatches) : ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.update` (definition, [line 92](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L92))

> Update the `ForwardRuleMatches` of a goal so that they are suitable for a
> child goal. `newMatches` are new forward rule matches obtained by updating the
> old goal's `ForwardState` with new hypotheses from the new goal. `erasedHyps`
> are the hypotheses from the old goal that no longer appear in the new goal.
> `consumedForwardRuleMatches` contains forward rule matches that were applied as
> rules to transform the old goal into the new goal.

```lean
def update (newMatches : Array ForwardRuleMatch)
    (erasedHyps : Std.HashSet FVarId)
    (consumedForwardRuleMatches : Array ForwardRuleMatch)
    (forwardRuleMatches : ForwardRuleMatches) : ForwardRuleMatches
```

`Aesop.ForwardRuleMatches.normRules` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L105))

> Get the norm rules corresponding to the norm rule matches.

```lean
def normRules (ms : ForwardRuleMatches) : Array NormRule
```

`Aesop.ForwardRuleMatches.safeRules` (definition, [line 109](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L109))

> Get the safe rules corresponding to the safe rule matches.

```lean
def safeRules (ms : ForwardRuleMatches) : Array SafeRule
```

`Aesop.ForwardRuleMatches.unsafeRules` (definition, [line 113](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L113))

> Get the unsafe rules corresponding to the unsafe rule matches.

```lean
def unsafeRules (ms : ForwardRuleMatches) : Array UnsafeRule
```

`Aesop.ForwardRuleMatches.size` (definition, [line 117](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean#L117))

> `O(n)` Number of matches in `ms`.

```lean
def size (ms : ForwardRuleMatches) : Nat
```

## Depends on

- [Match](../../forward/match.md)

## Sources

- [Aesop/Tree/Data/ForwardRuleMatches.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Data/ForwardRuleMatches.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Tree.Data.ForwardRuleMatches.json)
