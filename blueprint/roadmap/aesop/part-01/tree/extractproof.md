---
catalog: module
lean: Aesop.Goal.extractProof, Aesop.extractProof, Aesop.Goal.extractSafePrefix, Aesop.extractSafePrefix
statement: formalized
proof: formalized
---

# ExtractProof

`Aesop.Tree.ExtractProof`, in [Aesop/Tree/ExtractProof.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean), by Jannis Limperg.

`Aesop.Goal.extractProof` (definition, [line 176](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean#L176))

```lean
def Goal.extractProof (root : Goal) : MetaM Unit
```

`Aesop.extractProof` (definition, [line 179](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean#L179))

```lean
def extractProof : TreeM Unit
```

`Aesop.Goal.extractSafePrefix` (definition, [line 182](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean#L182))

```lean
def Goal.extractSafePrefix (root : Goal) : MetaM (Array MVarId)
```

`Aesop.extractSafePrefix` (definition, [line 186](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean#L186))

```lean
def extractSafePrefix : TreeM (Array MVarId)
```

## Depends on

- [TreeM](treem.md)

## Sources

- [Aesop/Tree/ExtractProof.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Tree/ExtractProof.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Tree.ExtractProof.json)
