---
catalog: module
lean: Aesop.ForwardRulePriority, Aesop.ForwardRulePriority.penalty?, Aesop.ForwardRulePriority.successProbability?, Aesop.ForwardRulePriority.compare, Aesop.ForwardRule, Aesop.ForwardRule.destruct
statement: formalized
proof: formalized
---

# Rule/Forward

`Aesop.Rule.Forward`, in [Aesop/Rule/Forward.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean), by Xavier Généreux, Jannis Limperg.

`Aesop.ForwardRulePriority` (inductive type, [line 21](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L21))

> The priority of a forward rule.

```lean
inductive ForwardRulePriority : Type where
  /-- If the rule is a norm or safe rule, its priority is an integer. -/
  | normSafe (n : Int) : ForwardRulePriority
  /-- If the rule is an unsafe rule, its priority is a percentage representing
  the rule's success probability. -/
  | «unsafe» (p : Percent) : ForwardRulePriority
  deriving Inhabited, BEq
```

`Aesop.ForwardRulePriority.penalty?` (definition, [line 32](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L32))

> If a `ForwardRulePriority` contains a penalty, extract it.

```lean
def penalty? : ForwardRulePriority → Option Int
```

`Aesop.ForwardRulePriority.successProbability?` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L37))

> If a `ForwardRulePriority` contains a success probability, extract it.

```lean
def successProbability? : ForwardRulePriority → Option Percent
```

`Aesop.ForwardRulePriority.compare` (definition, [line 44](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L44))

> Compare two rule priorities. Less means higher priority ('better').
> Norm/safe rules have higher priority than unsafe rules. Among norm/safe rules,
> lower penalty is better. Among unsafe rules, higher percentage is better.

```lean
protected def compare : (p₁ p₂ : ForwardRulePriority) → Ordering
```

`Aesop.ForwardRule` (structure, [line 61](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L61))

> A forward rule.

```lean
structure ForwardRule extends ForwardRuleInfo where
  /-- The rule's name. Should be unique among all rules in a rule set. -/
  name : RuleName
  /-- The theorem from which this rule is derived. -/
  term : RuleTerm
  /-- The rule's priority. -/
  prio : ForwardRulePriority
  deriving Inhabited
```

`Aesop.ForwardRule.destruct` (definition, [line 85](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean#L85))

> Is this rule a `destruct` rule (i.e., should we clear matched hyps)?

```lean
def destruct (r : ForwardRule) : Bool
```

## Depends on

- [RuleInfo](../forward/ruleinfo.md)
- [Percent](../../part-02/percent.md)
- [RuleTerm](../ruletac/ruleterm.md)

## Sources

- [Aesop/Rule/Forward.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Rule/Forward.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Rule.Forward.json)
