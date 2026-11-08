---
declaration: theorem
origin: cited
lean: TauCeti.morley_countableModelCount, TauCeti.morley_countableModelCount_le_aleph_one_or_hasPerfectlyMany
statement: formalized
proof: formalized
---

# Morley's theorem (cardinal form)

In a relational language with countably many relation
symbols of each arity, an infinitary sentence with countable branching has either at most `ℵ₁` or
`𝔠` countable models up to isomorphism. Neither the continuum hypothesis nor its negation is
assumed.

```lean
TauCeti.morley_countableModelCount.{u, v, uι} {L : FirstOrder.Language} [L.IsRelational]
  {ι : Type uι} [∀ (n : ℕ), Countable (L.Relations n)] [Countable ι] (φ : L.SentenceInf ι) :
  TauCeti.countableModelCount φ ≤ Cardinal.aleph 1 ∨
    TauCeti.countableModelCount φ = Cardinal.continuum
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Morley's dichotomy on the tier `ℕ`](morleys-dichotomy-on-the-tier-n.md)
- [Silver's theorem](../../other-areas/set-theory/silvers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.morley_countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.morley_countableModelCount).

## Other forms

**Morley's theorem (witnessed form).** Formalized in Tau Ceti as [`TauCeti.morley_countableModelCount_le_aleph_one_or_hasPerfectlyMany`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.morley_countableModelCount_le_aleph_one_or_hasPerfectlyMany).

```lean
TauCeti.morley_countableModelCount_le_aleph_one_or_hasPerfectlyMany.{u, v, uι}
  {L : FirstOrder.Language} [L.IsRelational] {ι : Type uι} [∀ (n : ℕ), Countable (L.Relations n)]
  [Countable ι] (φ : L.SentenceInf ι) :
  TauCeti.countableModelCount φ ≤ Cardinal.aleph 1 ∨ TauCeti.HasPerfectlyManyCountableModels φ
```

## Sources

- [Tau Ceti documentation: `TauCeti.morley_countableModelCount`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Morley.html#TauCeti.morley_countableModelCount)
- [Source of `TauCeti.morley_countableModelCount` in TauCeti/ModelTheory/Counting/Morley.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Counting/Morley.lean#L164)
