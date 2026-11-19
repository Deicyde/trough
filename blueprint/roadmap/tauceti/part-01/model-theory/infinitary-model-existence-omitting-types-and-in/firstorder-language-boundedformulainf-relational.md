---
declaration: def
origin: cited
lean: FirstOrder.Language.BoundedFormulaInf.relationalize
statement: formalized
---

# FirstOrder.Language.BoundedFormulaInf.relationalize

The **translation into the graph language** of an `L_{ω₁ω}` formula of `L`. Connectives and
quantifiers are translated structurally. An equation `t₁ = t₂` becomes
`∃ y, (t₁ = y) ∧ (t₂ = y)`, and a relational atom `R(t₀, …, t_{l-1})` becomes
`∃ y₀ … y_{l-1}, (⋀ᵢ tᵢ = yᵢ) ∧ R(y₀, …, y_{l-1})`, where each `t = y` is a term graph.

```lean
FirstOrder.Language.BoundedFormulaInf.relationalize.{u, v, u'} {L : FirstOrder.Language}
  {α : Type u'} {n : ℕ} : L.BoundedFormulaω α n → L.graphLanguage.BoundedFormulaω α n
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.BoundedFormulaInf.relationalize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/GraphTranslation/Relationalize.html#FirstOrder.Language.BoundedFormulaInf.relationalize).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.BoundedFormulaInf.relationalize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/GraphTranslation/Relationalize.html#FirstOrder.Language.BoundedFormulaInf.relationalize)
- [Source of `FirstOrder.Language.BoundedFormulaInf.relationalize` in TauCeti/ModelTheory/Infinitary/GraphTranslation/Relationalize.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Infinitary/GraphTranslation/Relationalize.lean#L168)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
