---
catalog: module
lean: Cslib.Logic.LogicalEquivalence
statement: formalized
proof: formalized
---

# LogicalEquivalence

`Cslib.Foundations.Logic.LogicalEquivalence`, in [Cslib/Foundations/Logic/LogicalEquivalence.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Logic/LogicalEquivalence.lean), by Fabrizio Montesi.

> Typeclass and notation for logical equivalence.

`Cslib.Logic.LogicalEquivalence` (class, [line 23](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Logic/LogicalEquivalence.lean#L23))

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

- [Cslib/Foundations/Logic/LogicalEquivalence.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Logic/LogicalEquivalence.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.Logic.LogicalEquivalence.json)
