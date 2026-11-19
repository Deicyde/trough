---
catalog: module
lean: Aesop.Goal.withHeadlineTraceNode, Aesop.Goal.traceMetadata, Aesop.Rapp.withHeadlineTraceNode, Aesop.Rapp.traceMetadata, Aesop.Goal.traceTreeCore, Aesop.Rapp.traceTreeCore, Aesop.Goal.traceTree, Aesop.Rapp.traceTree
statement: formalized
proof: formalized
---

# Tree/Tracing

`Aesop.Tree.Tracing`, in [Aesop/Tree/Tracing.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean).

`Aesop.Goal.withHeadlineTraceNode` (definition, [line 18](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L18))

```lean
def Goal.withHeadlineTraceNode (g : Goal) (traceOpt : TraceOption) (k : MetaM α)
    (collapsed := true) (transform : MessageData → MetaM MessageData := pure) :
    MetaM α
```

`Aesop.Goal.traceMetadata` (definition, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L29))

```lean
def Goal.traceMetadata (g : Goal) (traceOpt : TraceOption) : MetaM Unit
```

`Aesop.Rapp.withHeadlineTraceNode` (definition, [line 83](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L83))

```lean
def Rapp.withHeadlineTraceNode (r : Rapp) (traceOpt : TraceOption) (k : MetaM α)
    (collapsed := true) (transform : MessageData → MetaM MessageData := pure) :
    MetaM α
```

`Aesop.Rapp.traceMetadata` (definition, [line 90](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L90))

```lean
def Rapp.traceMetadata (r : Rapp) (traceOpt : TraceOption) : MetaM Unit
```

`Aesop.Goal.traceTreeCore` (definition, [line 106](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L106))

```lean
partial def Goal.traceTreeCore (g : Goal) (traceOpt : TraceOption) :
    MetaM Unit
```

`Aesop.Rapp.traceTreeCore` (definition, [line 116](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L116))

```lean
partial def Rapp.traceTreeCore (r : Rapp) (traceOpt : TraceOption) :
    MetaM Unit
```

`Aesop.Goal.traceTree` (definition, [line 125](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L125))

```lean
def Goal.traceTree (g : Goal) (traceOpt : TraceOption) : MetaM Unit
```

`Aesop.Rapp.traceTree` (definition, [line 129](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean#L129))

```lean
def Rapp.traceTree (r : Rapp) (traceOpt : TraceOption) : MetaM Unit
```

## Depends on

- [RunMetaM](runmetam.md)

## Sources

- [Aesop/Tree/Tracing.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/Tracing.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.Tracing.json)
