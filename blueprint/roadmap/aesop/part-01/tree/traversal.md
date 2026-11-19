---
catalog: module
lean: Aesop.TreeRef, Aesop.traverseDown, Aesop.traverseUp, Aesop.preTraverseDown, Aesop.preTraverseUp, Aesop.postTraverseDown, Aesop.postTraverseUp
statement: formalized
proof: formalized
---

# Traversal

`Aesop.Tree.Traversal`, in [Aesop/Tree/Traversal.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean), by Jannis Limperg.

`Aesop.TreeRef` (inductive type, [line 14](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L14))

```lean
inductive TreeRef
  | goal (gref : GoalRef)
  | rapp (rref : RappRef)
  | mvarCluster (cref : MVarClusterRef)
```

`Aesop.traverseDown` (definition, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L33))

```lean
partial def traverseDown : TreeRef → m Unit
```

`Aesop.traverseUp` (definition, [line 48](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L48))

```lean
partial def traverseUp : TreeRef → m Unit
```

`Aesop.preTraverseDown` (definition, [line 68](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L68))

```lean
def preTraverseDown (visitGoal : GoalRef → m Bool)
    (visitRapp : RappRef → m Bool) (visitMVarCluster : MVarClusterRef → m Bool) :
    TreeRef → m Unit
```

`Aesop.preTraverseUp` (definition, [line 80](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L80))

```lean
def preTraverseUp (visitGoal : GoalRef → m Bool) (visitRapp : RappRef → m Bool)
    (visitMVarCluster : MVarClusterRef → m Bool) : TreeRef → m Unit
```

`Aesop.postTraverseDown` (definition, [line 91](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L91))

```lean
def postTraverseDown (visitGoal : GoalRef → m Unit)
    (visitRapp : RappRef → m Unit) (visitMVarCluster : MVarClusterRef → m Unit) :
    TreeRef → m Unit
```

`Aesop.postTraverseUp` (definition, [line 103](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean#L103))

```lean
def postTraverseUp (visitGoal : GoalRef → m Unit) (visitRapp : RappRef → m Unit)
    (visitMVarCluster : MVarClusterRef → m Unit) : TreeRef → m Unit
```

## Depends on

- [Data](data.md)

## Sources

- [Aesop/Tree/Traversal.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Traversal.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Traversal.json)
