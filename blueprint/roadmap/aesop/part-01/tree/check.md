---
catalog: module
lean: Aesop.MVarClusterRef.checkIds, Aesop.MVarClusterRef.checkAcyclic, Aesop.MVarClusterRef.checkConsistentParentChildLinks, Aesop.MVarClusterRef.checkState, Aesop.MVarClusterRef.checkIrrelevance, Aesop.MVarClusterRef.checkMVars, Aesop.MVarClusterRef.checkIntroducedMVars, Aesop.MVarClusterRef.checkInvariants, Aesop.MVarClusterRef.checkInvariantsIfEnabled, Aesop.checkInvariantsIfEnabled
statement: formalized
proof: formalized
---

# Tree/Check

`Aesop.Tree.Check`, in [Aesop/Tree/Check.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean), by Jannis Limperg.

`Aesop.MVarClusterRef.checkIds` (definition, [line 22](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L22))

```lean
def checkIds (root : MVarClusterRef) : CoreM Unit
```

`Aesop.MVarClusterRef.checkAcyclic` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L41))

```lean
def checkAcyclic (root : MVarClusterRef) : CoreM Unit
```

`Aesop.MVarClusterRef.checkConsistentParentChildLinks` (definition, [line 62](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L62))

```lean
def checkConsistentParentChildLinks (root : MVarClusterRef) : CoreM Unit
```

`Aesop.MVarClusterRef.checkState` (definition, [line 89](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L89))

```lean
def checkState (root : MVarClusterRef) : CoreM Unit
```

`Aesop.MVarClusterRef.checkIrrelevance` (definition, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L108))

```lean
def checkIrrelevance (root : MVarClusterRef) : CoreM Unit
```

`Aesop.MVarClusterRef.checkMVars` (definition, [line 130](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L130))

```lean
def checkMVars (root : MVarClusterRef) (rootMetaState : Meta.SavedState) :
    MetaM Unit
```

`Aesop.MVarClusterRef.checkIntroducedMVars` (definition, [line 203](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L203))

```lean
def checkIntroducedMVars (root : MVarClusterRef)
    (rootMetaState : Meta.SavedState) : MetaM Unit
```

`Aesop.MVarClusterRef.checkInvariants` (definition, [line 222](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L222))

```lean
def checkInvariants (root : MVarClusterRef) (rootMetaState : Meta.SavedState) :
    MetaM Unit
```

`Aesop.MVarClusterRef.checkInvariantsIfEnabled` (definition, [line 232](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L232))

```lean
def checkInvariantsIfEnabled (root : MVarClusterRef)
    (rootMetaState : Meta.SavedState) : MetaM Unit
```

`Aesop.checkInvariantsIfEnabled` (definition, [line 239](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean#L239))

```lean
def checkInvariantsIfEnabled : TreeM Unit
```

## Depends on

- [Tree/State](state.md)
- [TreeM](treem.md)

## Proof depends on

- [RunMetaM](runmetam.md)

## Sources

- [Aesop/Tree/Check.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Check.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Check.json)
