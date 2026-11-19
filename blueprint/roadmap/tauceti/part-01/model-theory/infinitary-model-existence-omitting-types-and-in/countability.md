---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Fragment.generated_countable
statement: formalized
proof: formalized
---

# Countability

A countable set of formulas generates a countable fragment, over any
language: every member is reached from a generator along a finite list of component steps, each
coded by a pair of natural numbers.

```lean
FirstOrder.Language.Fragment.generated_countable.{u, v} {L : FirstOrder.Language}
  {S : Set ((n : ℕ) × L.BoundedFormulaω Empty n)} (hS : S.Countable) :
  (↑(FirstOrder.Language.Fragment.generated S)).Countable
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Fragment.generated_countable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Fragment.html#FirstOrder.Language.Fragment.generated_countable).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Fragment.generated_countable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Fragment.html#FirstOrder.Language.Fragment.generated_countable)
- [Source of `FirstOrder.Language.Fragment.generated_countable` in TauCeti/ModelTheory/Infinitary/Fragment.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Infinitary/Fragment.lean#L370)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
