---
catalog: module
lean: Aesop.Match, Aesop.Match.equiv, Aesop.CompleteMatch, Aesop.ForwardRuleMatch, Aesop.ForwardRuleMatch.ord, Aesop.ForwardRuleMatch.le
statement: formalized
proof: formalized
---

# Types

`Aesop.Forward.Match.Types`, in [Aesop/Forward/Match/Types.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean).

`Aesop.Match` (structure, [line 15](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L15))

> A match associates hypotheses to (a prefix of) the slots of a slot
> cluster.

```lean
structure Match where
  /-- The substitution induced by the hyps or pattern substitutions added to
  the slots. -/
  subst : Substitution
  /-- The pattern substitutions that have been added to the match. -/
  patInstSubsts : Array Substitution
  /-- The match's level is the index of the maximal slot for which a hyp or
  pattern substitution has been added to the match. -/
  level : SlotIndex
  /-- Premises that appear in slots which are as yet unassigned in this match
  (i.e., in slots with index greater than `level`). This is a property of the
  rule, but we include it here because it's used to check whether two matches
  are equivalent. -/
  forwardDeps : Array PremiseIndex
  /-- Premises that appear in the rule's conclusion. This is a property of the
  rule, but we include it here because it's used to check whether two matches
  are equivalent. -/
  conclusionDeps : Array PremiseIndex
  deriving Inhabited
```

`Aesop.Match.equiv` (definition, [line 52](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L52))

> Two matches are equivalent if (a) they have the same level; (b) for each
> premise that appears in a slot greater than the matches' level, their
> substitution assigns the same value; (c) for each premise that appears in the
> rule's conclusion, their substitution assigns the same value.
>
> If we already have a match `m₁` and we obtain an equivalent match `m₂`, then
> `m₂` is redundant. This is because if the matches are partial, then `m₂` can be
> completed by exactly the hypotheses that complete `m₁`, since they agree on the
> premise instantiations that are relevant for the possible completions. And if
> the matches are complete, then they assign the same instantiations to the
> variables that appear in the rule's conclusion, and these are the only ones that
> ultimately matter.

```lean
protected def equiv (m₁ m₂ : Match) : Bool
```

`Aesop.CompleteMatch` (structure, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L82))

> A complete match contains complete matches for each slot cluster. This means
> there is one match for each slot cluster and each such match contains a
> hypothesis for each of the slots.

```lean
structure CompleteMatch where
  clusterMatches : Array Match
  deriving Inhabited, BEq, Hashable
```

`Aesop.ForwardRuleMatch` (structure, [line 96](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L96))

> An entry in the forward state queues. Represents a complete match.

```lean
structure ForwardRuleMatch where
  /-- The rule to which this match belongs. -/
  rule : ForwardRule
  /-- The match. -/
  «match» : CompleteMatch
  deriving Inhabited, BEq, Hashable
```

`Aesop.ForwardRuleMatch.ord` (instance, [line 108](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L108))

> Compare two queue entries by rule priority, rule name and the expressions
> contained in the match. Higher-priority rules are considered less (since the
> queues are min-queues). The ordering on expressions is arbitrary.

```lean
protected instance ord : Ord ForwardRuleMatch
```

`Aesop.ForwardRuleMatch.le` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean#L114))

```lean
protected def le (m₁ m₂ : ForwardRuleMatch) : Bool
```

## Depends on

- [Rule/Forward](../../rule/forward.md)

## Sources

- [Aesop/Forward/Match/Types.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match/Types.lean)
- [Declaration ledger](../../../../../sources/aesop/Aesop.Forward.Match.Types.json)
