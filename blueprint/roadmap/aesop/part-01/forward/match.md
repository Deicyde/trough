---
catalog: module
lean: Aesop.elabForwardRuleTerm, Aesop.Match.initial, Aesop.Match.addHypOrPatSubst, Aesop.Match.containsHyp, Aesop.Match.containsPatSubst, Aesop.CompleteMatch.reconstructArgs, Aesop.CompleteMatch.toMessageData, Aesop.ForwardRuleMatch.foldHypsM, Aesop.ForwardRuleMatch.foldHyps, Aesop.ForwardRuleMatch.anyHyp, Aesop.ForwardRuleMatch.getPropHyps, Aesop.ForwardRuleMatch.getProof, Aesop.ForwardRuleMatch.apply, Aesop.forwardRuleMatchesToNormRules?, Aesop.forwardRuleMatchesToSafeRules?, Aesop.forwardRuleMatchesToUnsafeRules?
statement: formalized
proof: formalized
---

# Match

`Aesop.Forward.Match`, in [Aesop/Forward/Match.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean), by Xavier Généreux, Jannis Limperg.

`Aesop.elabForwardRuleTerm` (definition, [line 25](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L25))

> Elaborate the term of a forward rule in the current goal.

```lean
def elabForwardRuleTerm (goal : MVarId) : RuleTerm → MetaM Expr
```

`Aesop.Match.initial` (definition, [line 37](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L37))

> Create a one-element match. `subst` is the substitution that results from
> matching a hypothesis against slot 0, or from a pattern substitution.
> `isPatSubst` is `true` if the substitution resulted from a rule pattern.
> `forwardDeps` are the forward dependencies of slot 0. `conclusionDeps` are the
> conclusion dependencies of the rule to which this match belongs.

```lean
def initial (subst : Substitution) (isPatSubst : Bool)
    (forwardDeps conclusionDeps : Array PremiseIndex) : Match
```

`Aesop.Match.addHypOrPatSubst` (definition, [line 50](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L50))

> Add a hyp or pattern substitution to the match. `subst` is the substitution
> that results from matching a hypothesis against slot `m.level + 1`, or from the
> pattern. `isPatSubst` is `true` if the substitution resulted from a pattern
> substitution. `forwardDeps` are the forward dependencies of slot
> `m.level + 1`.

```lean
def addHypOrPatSubst (subst : Substitution) (isPatSubst : Bool)
    (forwardDeps : Array PremiseIndex) (m : Match) : Match
```

`Aesop.Match.containsHyp` (definition, [line 60](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L60))

> Returns `true` if the match contains the given hyp.

```lean
def containsHyp (hyp : FVarId) (m : Match) : Bool
```

`Aesop.Match.containsPatSubst` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L64))

> Returns `true` if the match contains the given pattern substitution.

```lean
def containsPatSubst (subst : Substitution) (m : Match) : Bool
```

`Aesop.CompleteMatch.reconstructArgs` (definition, [line 74](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L74))

> Given a complete match `m` for `r`, get arguments to `r` contained in the
> match's slots and substitution. For non-immediate arguments, we return `none`.
> The returned levels are suitable assignments for the level mvars of `r`.

```lean
def reconstructArgs (r : ForwardRule) (m : CompleteMatch) :
    Array (Option Expr) × Array (Option Level)
```

`Aesop.CompleteMatch.toMessageData` (definition, [line 89](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L89))

```lean
protected def toMessageData (r : ForwardRule) (m : CompleteMatch) :
    MessageData
```

`Aesop.ForwardRuleMatch.foldHypsM` (definition, [line 101](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L101))

> Fold over the hypotheses contained in a match.

```lean
def foldHypsM [Monad M] (f : σ → FVarId → M σ) (init : σ)
    (m : ForwardRuleMatch) : M σ
```

`Aesop.ForwardRuleMatch.foldHyps` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L110))

> Fold over the hypotheses contained in a match.

```lean
def foldHyps (f : σ → FVarId → σ) (init : σ) (m : ForwardRuleMatch) : σ
```

`Aesop.ForwardRuleMatch.anyHyp` (definition, [line 114](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L114))

> Returns `true` if any hypothesis contained in `m` satisfies `f`.

```lean
def anyHyp (m : ForwardRuleMatch) (f : FVarId → Bool) : Bool
```

`Aesop.ForwardRuleMatch.getPropHyps` (definition, [line 122](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L122))

> Get the hypotheses from the match whose types are propositions.

```lean
def getPropHyps (m : ForwardRuleMatch) : MetaM (Array FVarId)
```

`Aesop.ForwardRuleMatch.getProof` (definition, [line 127](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L127))

> Construct the proof of the new hypothesis represented by `m`.

```lean
def getProof (goal : MVarId) (m : ForwardRuleMatch) : MetaM (Option Expr)
```

`Aesop.ForwardRuleMatch.apply` (definition, [line 168](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L168))

> Apply a forward rule match to a goal. This adds the hypothesis corresponding
> to the match to the local context. Returns the new goal, the added hypothesis
> and the hypotheses that were removed (if any). Hypotheses may be removed if the
> match is for a `destruct` rule. If `skipExistingProps` is `true`, propositional
> hypotheses are not added if another hypothesis with the same type is already
> present in the goal.

```lean
def apply (goal : MVarId) (m : ForwardRuleMatch) (skipExistingProps : Bool) :
    ScriptT BaseM (Option (MVarId × FVarId × Array FVarId))
```

`Aesop.forwardRuleMatchesToNormRules?` (definition, [line 218](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L218))

> Convert forward rule matches to norm rules. Fails if any of the matches is
> not a norm rule match.

```lean
def forwardRuleMatchesToNormRules? (ms : Array ForwardRuleMatch) :
    Option (Array NormRule)
```

`Aesop.forwardRuleMatchesToSafeRules?` (definition, [line 225](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L225))

> Convert forward rule matches to safe rules. Fails if any of the matches is
> not a safe rule match.

```lean
def forwardRuleMatchesToSafeRules? (ms : Array ForwardRuleMatch) :
    Option (Array SafeRule)
```

`Aesop.forwardRuleMatchesToUnsafeRules?` (definition, [line 232](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean#L232))

> Convert forward rule matches to unsafe rules. Fails if any of the matches
> is not an unsafe rule match.

```lean
def forwardRuleMatchesToUnsafeRules? (ms : Array ForwardRuleMatch) :
    Option (Array UnsafeRule)
```

## Depends on

- [Rule](../../part-02/rule.md)
- [ElabRuleTerm](../ruletac/elabruleterm.md)
- [Forward/Basic](../ruletac/forward-2/basic.md)
- [SpecificTactics](../script/specifictactics.md)

## Sources

- [Aesop/Forward/Match.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Match.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.Match.json)
