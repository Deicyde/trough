---
catalog: module
lean: Aesop.indexConfig, Aesop.mkDiscrTreePath, Aesop.getUnify, Aesop.getMatch
statement: formalized
proof: formalized
---

# DiscrTreeConfig

`Aesop.Index.DiscrTreeConfig`, in [Aesop/Index/DiscrTreeConfig.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean), by Jannis Limperg.

`Aesop.indexConfig` (definition, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean#L21))

> The configuration used by all Aesop indices.

```lean
def indexConfig : ConfigWithKey
```

`Aesop.mkDiscrTreePath` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean#L24))

```lean
def mkDiscrTreePath (e : Expr) : MetaM (Array DiscrTree.Key)
```

`Aesop.getUnify` (definition, [line 27](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean#L27))

```lean
def getUnify (t : DiscrTree α) (e : Expr) : MetaM (Array α)
```

`Aesop.getMatch` (definition, [line 30](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean#L30))

```lean
def getMatch (t : DiscrTree α) (e : Expr) : MetaM (Array α)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Index/DiscrTreeConfig.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/DiscrTreeConfig.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Index.DiscrTreeConfig.json)
