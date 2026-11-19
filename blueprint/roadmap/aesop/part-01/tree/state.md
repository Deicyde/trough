---
catalog: module
lean: Aesop.Goal.isIrrelevantNoCache, Aesop.Rapp.isIrrelevantNoCache, Aesop.MVarCluster.isIrrelevantNoCache, Aesop.TreeRef.markSubtreeIrrelevant, Aesop.GoalRef.markSubtreeIrrelevant, Aesop.RappRef.markSubtreeIrrelevant, Aesop.MVarClusterRef.markSubtreeIrrelevant, Aesop.Goal.isProvenByNormalizationNoCache, Aesop.Goal.isProvenByRuleApplicationNoCache, Aesop.Goal.isProvenNoCache, Aesop.Rapp.isProvenNoCache, Aesop.MVarCluster.isProvenNoCache, Aesop.GoalRef.markProvenByNormalization, Aesop.RappRef.markProven, Aesop.Goal.isUnprovableNoCache, Aesop.Rapp.isUnprovableNoCache, Aesop.MVarCluster.isUnprovableNoCache, Aesop.GoalRef.markUnprovable, Aesop.GoalRef.markForcedUnprovable, Aesop.GoalRef.checkAndMarkUnprovable, Aesop.Goal.stateNoCache, Aesop.Rapp.stateNoCache, Aesop.MVarCluster.stateNoCache
statement: formalized
proof: formalized
---

# Tree/State

`Aesop.Tree.State`, in [Aesop/Tree/State.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean), by Jannis Limperg.

> ## Marking Nodes As Proven/Unprovable/Irrelevant

> ### Irrelevant

`Aesop.Goal.isIrrelevantNoCache` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L27))

```lean
def Goal.isIrrelevantNoCache (g : Goal) : BaseIO Bool
```

`Aesop.Rapp.isIrrelevantNoCache` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L31))

```lean
def Rapp.isIrrelevantNoCache (r : Rapp) : BaseIO Bool
```

`Aesop.MVarCluster.isIrrelevantNoCache` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L35))

```lean
def MVarCluster.isIrrelevantNoCache (c : MVarCluster) : BaseIO Bool
```

`Aesop.TreeRef.markSubtreeIrrelevant` (definition, [line 41](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L41))

```lean
def TreeRef.markSubtreeIrrelevant : TreeRef → BaseIO Unit
```

`Aesop.GoalRef.markSubtreeIrrelevant` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L59))

```lean
def GoalRef.markSubtreeIrrelevant (gref : GoalRef) : BaseIO Unit
```

`Aesop.RappRef.markSubtreeIrrelevant` (definition, [line 62](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L62))

```lean
def RappRef.markSubtreeIrrelevant (rref : RappRef) : BaseIO Unit
```

`Aesop.MVarClusterRef.markSubtreeIrrelevant` (definition, [line 65](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L65))

```lean
def MVarClusterRef.markSubtreeIrrelevant (cref : MVarClusterRef) : BaseIO Unit
```

> ### Proven

`Aesop.Goal.isProvenByNormalizationNoCache` (definition, [line 73](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L73))

```lean
def Goal.isProvenByNormalizationNoCache (g : Goal) : Bool
```

`Aesop.Goal.isProvenByRuleApplicationNoCache` (definition, [line 76](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L76))

```lean
def Goal.isProvenByRuleApplicationNoCache (g : Goal) : BaseIO Bool
```

`Aesop.Goal.isProvenNoCache` (definition, [line 79](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L79))

```lean
def Goal.isProvenNoCache (g : Goal) : BaseIO Bool
```

`Aesop.Rapp.isProvenNoCache` (definition, [line 84](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L84))

```lean
def Rapp.isProvenNoCache (r : Rapp) : BaseIO Bool
```

`Aesop.MVarCluster.isProvenNoCache` (definition, [line 88](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L88))

```lean
def MVarCluster.isProvenNoCache (c : MVarCluster) : BaseIO Bool
```

`Aesop.GoalRef.markProvenByNormalization` (definition, [line 128](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L128))

```lean
def GoalRef.markProvenByNormalization (gref : GoalRef) : BaseIO Unit
```

`Aesop.RappRef.markProven` (definition, [line 135](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L135))

```lean
def RappRef.markProven (rref : RappRef) : BaseIO Unit
```

> ### Unprovable

`Aesop.Goal.isUnprovableNoCache` (definition, [line 142](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L142))

```lean
def Goal.isUnprovableNoCache (g : Goal) : BaseIO Bool
```

`Aesop.Rapp.isUnprovableNoCache` (definition, [line 148](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L148))

```lean
def Rapp.isUnprovableNoCache (r : Rapp) : BaseIO Bool
```

`Aesop.MVarCluster.isUnprovableNoCache` (definition, [line 152](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L152))

```lean
def MVarCluster.isUnprovableNoCache (c : MVarCluster) : BaseIO Bool
```

`Aesop.GoalRef.markUnprovable` (definition, [line 191](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L191))

```lean
def GoalRef.markUnprovable (gref : GoalRef) : BaseIO Unit
```

`Aesop.GoalRef.markForcedUnprovable` (definition, [line 197](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L197))

```lean
def GoalRef.markForcedUnprovable (gref : GoalRef) : BaseIO Unit
```

`Aesop.GoalRef.checkAndMarkUnprovable` (definition, [line 201](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L201))

```lean
def GoalRef.checkAndMarkUnprovable (gref : GoalRef) : BaseIO Unit
```

> ### Uncached Node States

`Aesop.Goal.stateNoCache` (definition, [line 213](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L213))

```lean
def Goal.stateNoCache (g : Goal) : BaseIO GoalState
```

`Aesop.Rapp.stateNoCache` (definition, [line 223](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L223))

```lean
def Rapp.stateNoCache (r : Rapp) : BaseIO NodeState
```

`Aesop.MVarCluster.stateNoCache` (definition, [line 231](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean#L231))

```lean
def MVarCluster.stateNoCache (c : MVarCluster) : BaseIO NodeState
```

## Depends on

- [Traversal](traversal.md)

## Sources

- [Aesop/Tree/State.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/State.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.State.json)
