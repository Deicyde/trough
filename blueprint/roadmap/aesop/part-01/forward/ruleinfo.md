---
catalog: module
lean: Aesop.Slot, Aesop.ForwardRuleInfo, Aesop.ForwardRuleInfo.isConstant, Aesop.ForwardRuleInfo.ofExpr
statement: formalized
proof: formalized
---

# RuleInfo

`Aesop.Forward.RuleInfo`, in [Aesop/Forward/RuleInfo.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean), by Xavier Généreux, Jannis Limperg.

`Aesop.Slot` (structure, [line 29](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean#L29))

> A slot represents a maximal premise of a forward rule, i.e. a premise with
> no forward dependencies. The goal of forward reasoning is to assign a
> hypothesis to each slot in such a way that the assignments agree on all
> variables shared between them.
>
> Exceptionally, a slot can also represent the rule pattern substitution. Rules
> with a rule pattern have exactly one such slot, which is assigned an arbitrary
> premise index.

```lean
structure Slot where
  /-- Discrimination tree keys for the type of this slot. If the slot is for the
  rule pattern, it is not associated with a premise, so doesn't have
  discrimination tree keys. -/
  typeDiscrTreeKeys? : Option (Array DiscrTree.Key)
  /-- Index of the slot. Slots are always part of a list of slots, and `index`
  is the 0-based index of this slot in that list. -/
  index : SlotIndex
  /-- 0-based index of the premise represented by this slot in the rule type.
  Note that the slots array may use a different ordering than the original
  order of premises, so we *don't* always have `index ≤ premiseIndex`. Rule
  pattern slots are assigned an arbitrary premise index. -/
  premiseIndex : PremiseIndex
  /-- The previous premises that the premise of this slot depends on. -/
  deps : Std.HashSet PremiseIndex
  /-- Common variables shared between this slot and the previous slots. -/
  common : Std.HashSet PremiseIndex
  /-- The forward dependencies of this slot. These are all the premises that
  appear in slots *after* this one. -/
  forwardDeps : Array PremiseIndex
  deriving Inhabited
```

`Aesop.ForwardRuleInfo` (structure, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean#L58))

> Information about the decomposed type of a forward rule.

```lean
structure ForwardRuleInfo where
  /-- The rule's number of premises. -/
  numPremises : Nat
  /-- The number of distinct level parameters and level metavariables occurring
  in the rule's type. We expect that these turn into level metavariables when
  the rule is elaborated. -/
  numLevelParams : Nat
  /-- Slots representing the maximal premises of the forward rule, partitioned
  into metavariable clusters. -/
  slotClusters : Array (Array Slot)
  /-- The premises that appear in the rule's conclusion. -/
  conclusionDeps : Array PremiseIndex
  /-- The rule's rule pattern and the premise index that was assigned to it. -/
  rulePatternInfo? : Option (RulePattern × PremiseIndex)
  deriving Inhabited
```

`Aesop.ForwardRuleInfo.isConstant` (definition, [line 78](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean#L78))

> Is this rule a constant rule (i.e., does it have neither premises nor a rule
> pattern)? Note: the rule may still have instance arguments.

```lean
def isConstant (r : ForwardRuleInfo) : Bool
```

`Aesop.ForwardRuleInfo.ofExpr` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean#L82))

> Construct a `ForwardRuleInfo` for the theorem `thm`.

```lean
def ofExpr (thm : Expr) (rulePattern? : Option RulePattern)
    (immediate : UnorderedArraySet PremiseIndex) : MetaM ForwardRuleInfo
```

## Depends on

- [SlotIndex](slotindex.md)
- [Aesop/RulePattern](../../part-02/rulepattern.md)
- [UnionFind](../util/unionfind.md)

## Sources

- [Aesop/Forward/RuleInfo.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/RuleInfo.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.RuleInfo.json)
