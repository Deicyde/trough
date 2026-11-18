---
catalog: module
lean: Cslib.Logic.LogicalEquivalence
statement: formalized
proof: formalized
---

# LogicalEquivalence

`Cslib.Foundations.Logic.LogicalEquivalence`, in [Cslib/Foundations/Logic/LogicalEquivalence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/LogicalEquivalence.lean), by Fabrizio Montesi.

> Typeclass and notation for logical equivalence.

`Cslib.Logic.LogicalEquivalence` (class, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/LogicalEquivalence.lean#L23))

> A logical equivalence `eqv` for an inference system `S` is a congruence on propositions (of type
> `α`) that preserves validity of judgements under any judgemental context.

```lean
class LogicalEquivalence S (eqv : α → α → Prop)
    [HasContext α] [Congruence eqv] [HasHContext Judgement α] [InferenceSystem S Judgement]
    extends LawfulCongruence eqv where
  /-- Validity is preserved for any judgemental context. -/
  eqvFillValid (heqv : a ≡[eqv] b) (c : HasHContext.Context Judgement α)
    (h : S⇓(c<[a])) : S⇓(c<[b])
```

## Depends on

- [Inference systems](inferencesystem/defs.md)
- [Congruence](../syntax/congruence.md)

## Sources

- [Cslib/Foundations/Logic/LogicalEquivalence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/LogicalEquivalence.lean)
