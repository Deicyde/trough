---
catalog: module
lean: Aesop.PhaseName, Aesop.ScopeName, Aesop.BuilderName, Aesop.RuleName, Aesop.RuleName.compare, Aesop.RuleName.quickCompare, Aesop.getRuleNameForExpr, Aesop.DisplayRuleName
statement: formalized
proof: formalized
---

# Rule/Name

`Aesop.Rule.Name`, in [Aesop/Rule/Name.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean), by Jannis Limperg.

`Aesop.PhaseName` (inductive type, [line 17](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L17))

```lean
inductive PhaseName
  | norm
  | safe
  | «unsafe»
  deriving Inhabited, BEq, Hashable, ToJson
```

`Aesop.ScopeName` (inductive type, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L39))

```lean
inductive ScopeName
  | global
  | «local»
  deriving Inhabited, BEq, Hashable, ToJson
```

`Aesop.BuilderName` (inductive type, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L59))

```lean
inductive BuilderName
  | apply
  | cases
  | constructors
  | destruct
  | forward
  | simp
  | tactic
  | unfold
  deriving Inhabited, BEq, Hashable, ToJson
```

`Aesop.RuleName` (structure, [line 94](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L94))

```lean
structure RuleName where
  name : Name
  builder : BuilderName
  phase : PhaseName
  scope : ScopeName
  protected hash : UInt64 :=
    mixHash (hash name) $ mixHash (hash builder) $ mixHash (hash phase)
      (hash scope)
  deriving Inhabited
```

`Aesop.RuleName.compare` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L114))

```lean
protected def compare : (_ _ : RuleName) → Ordering
```

`Aesop.RuleName.quickCompare` (definition, [line 120](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L120))

```lean
protected def quickCompare (n₁ n₂ : RuleName) : Ordering
```

`Aesop.getRuleNameForExpr` (definition, [line 144](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L144))

```lean
def getRuleNameForExpr : Expr → MetaM Name
```

`Aesop.DisplayRuleName` (inductive type, [line 150](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean#L150))

```lean
inductive DisplayRuleName
  | ruleName (n : RuleName)
  | normSimp
  | normUnfold
  deriving Inhabited, BEq, Ord, Hashable
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Rule/Name.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Name.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Rule.Name.json)
