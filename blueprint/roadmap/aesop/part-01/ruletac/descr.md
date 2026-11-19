---
catalog: module
lean: Aesop.RuleTacDescr, Aesop.RuleTacDescr.forwardRuleMatches?
statement: formalized
proof: formalized
---

# Descr

`Aesop.RuleTac.Descr`, in [Aesop/RuleTac/Descr.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Descr.lean).

`Aesop.RuleTacDescr` (inductive type, [line 13](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Descr.lean#L13))

```lean
inductive RuleTacDescr
  | apply (term : RuleTerm) (md : TransparencyMode)
  | constructors (constructorNames : Array Name) (md : TransparencyMode)
  | forward (term : RuleTerm) (immediate : UnorderedArraySet PremiseIndex)
      (isDestruct : Bool)
  | cases (target : CasesTarget) (md : TransparencyMode)
      (isRecursiveType : Bool) (ctorNames : Array CtorNames)
  | tacticM (decl : Name)
  | ruleTac (decl : Name)
  | tacGen (decl : Name)
  | singleRuleTac (decl : Name)
  | tacticStx (stx : Syntax)
  | preprocess
  | forwardMatches (ms : Array ForwardRuleMatch)
  deriving Inhabited
```

`Aesop.RuleTacDescr.forwardRuleMatches?` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Descr.lean#L31))

```lean
def forwardRuleMatches? : RuleTacDescr → Option (Array ForwardRuleMatch)
```

## Depends on

- [Types](../forward/match-2/types.md)
- [Rule Tactic Types](basic.md)
- [CtorNames](../script/ctornames.md)

## Sources

- [Aesop/RuleTac/Descr.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RuleTac/Descr.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.RuleTac.Descr.json)
