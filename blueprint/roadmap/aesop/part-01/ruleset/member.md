---
catalog: module
lean: Aesop.BaseRuleSetMember, Aesop.BaseRuleSetMember.name, Aesop.GlobalRuleSetMember, Aesop.GlobalRuleSetMember.name, Aesop.LocalRuleSetMember, Aesop.LocalRuleSetMember.name, Aesop.LocalRuleSetMember.toGlobalRuleSetMember?
statement: formalized
proof: formalized
---

# Member

`Aesop.RuleSet.Member`, in [Aesop/RuleSet/Member.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean), by Jannis Limperg.

`Aesop.BaseRuleSetMember` (inductive type, [line 14](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L14))

```lean
inductive BaseRuleSetMember
  | normRule (r : NormRule)
  | unsafeRule (r : UnsafeRule)
  | safeRule (r : SafeRule)
  | unfoldRule (r : UnfoldRule)
  | normForwardRule (r₁ : ForwardRule) (r₂ : NormRule)
  | unsafeForwardRule (r₁ : ForwardRule) (r₂ : UnsafeRule)
  | safeForwardRule (r₁ : ForwardRule) (r₂ : SafeRule)
  deriving Inhabited
```

`Aesop.BaseRuleSetMember.name` (definition, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L24))

```lean
def BaseRuleSetMember.name : BaseRuleSetMember → RuleName
```

`Aesop.GlobalRuleSetMember` (inductive type, [line 33](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L33))

```lean
inductive GlobalRuleSetMember
  | base (m : BaseRuleSetMember)
  | normSimpRule (e : NormSimpRule)
  deriving Inhabited
```

`Aesop.GlobalRuleSetMember.name` (definition, [line 38](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L38))

```lean
def GlobalRuleSetMember.name : GlobalRuleSetMember → RuleName
```

`Aesop.LocalRuleSetMember` (inductive type, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L42))

```lean
inductive LocalRuleSetMember
  | global (m : GlobalRuleSetMember)
  | localNormSimpRule (r : LocalNormSimpRule)
  deriving Inhabited
```

`Aesop.LocalRuleSetMember.name` (definition, [line 47](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L47))

```lean
def LocalRuleSetMember.name : LocalRuleSetMember → RuleName
```

`Aesop.LocalRuleSetMember.toGlobalRuleSetMember?` (definition, [line 51](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean#L51))

```lean
def LocalRuleSetMember.toGlobalRuleSetMember? :
    LocalRuleSetMember → Option GlobalRuleSetMember
```

## Depends on

- [Rule](../../part-02/rule.md)

## Sources

- [Aesop/RuleSet/Member.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleSet/Member.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleSet.Member.json)
