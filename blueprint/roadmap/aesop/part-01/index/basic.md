---
catalog: module
lean: Aesop.IndexingMode, Aesop.IndexingMode.format, Aesop.IndexingMode.targetMatchingConclusion, Aesop.IndexingMode.hypsMatchingConst, Aesop.IndexMatchLocation, Aesop.IndexMatchResult
statement: formalized
proof: formalized
---

# Index/Basic

`Aesop.Index.Basic`, in [Aesop/Index/Basic.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean), by Jannis Limperg.

`Aesop.IndexingMode` (inductive type, [line 16](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L16))

```lean
inductive IndexingMode : Type
  | unindexed
  | target (keys : Array DiscrTree.Key)
  | hyps (keys : Array DiscrTree.Key)
  | or (imodes : Array IndexingMode)
  deriving Inhabited
```

`Aesop.IndexingMode.format` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L25))

```lean
protected partial def format : IndexingMode → Format
```

`Aesop.IndexingMode.targetMatchingConclusion` (definition, [line 34](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L34))

```lean
def targetMatchingConclusion (type : Expr) : MetaM IndexingMode
```

`Aesop.IndexingMode.hypsMatchingConst` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L38))

```lean
def hypsMatchingConst (decl : Name) : MetaM IndexingMode
```

`Aesop.IndexMatchLocation` (inductive type, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L51))

> The source of a rule match reported by the index. We assume that
> only IndexMatchLocations belonging to the same goal are equated or compared.

```lean
inductive IndexMatchLocation
  | none
  | target
  | hyp (ldecl : LocalDecl)
  deriving Inhabited
```

`Aesop.IndexMatchResult` (structure, [line 98](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean#L98))

> A rule that, according to the index, should be applied to the current goal.
> In addition to the rule, this data structure contains information about how the
> rule should be applied. For example, if the rule has rule patterns, we report
> the substitutions obtained by matching the rule patterns against the current
> goal.

```lean
structure IndexMatchResult (α : Type) where
  /-- The rule that should be applied. -/
  rule : α
  /-- Goal locations where the rule matched. The rule's `indexingMode`
  determines which locations can be contained in this set. The array contains
  no duplicates. -/
  locations : Array IndexMatchLocation
  /-- Pattern substitutions for this rule that were found in the goal. `none`
  iff the rule doesn't have a pattern. The array contains no duplicates. -/
  patternSubsts? : Option (Array Substitution)
  deriving Inhabited
```

## Depends on

- [Substitution](../forward/substitution.md)
- [Util/Basic](../util/basic.md)

## Sources

- [Aesop/Index/Basic.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Index/Basic.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Index.Basic.json)
