---
declaration: theorem
origin: cited
lean: FirstOrder.Language.craig_interpolation
statement: formalized
proof: formalized
---

# Craig interpolation for `L_{ω₁ω}`

In any language `L` (of any cardinality, with function
symbols, and in any universes), if an `L_{ω₁ω}` sentence `φ` entails `ψ`, there is an `L_{ω₁ω}`
sentence `θ` whose function symbols lie in `φ.functionsIn ∩ ψ.functionsIn` and whose relation
symbols lie in `φ.relationsIn ∩ ψ.relationsIn` such that `φ` entails `θ` and `θ` entails `ψ`.
Equality is logical, so `θ` may use it freely.

```lean
FirstOrder.Language.craig_interpolation.{u, v} {L : FirstOrder.Language} (φ ψ : L.Sentenceω)
  (h : φ.Entails ψ) :
  ∃ θ,
    FirstOrder.Language.BoundedFormulaInf.functionsIn θ ⊆
        FirstOrder.Language.BoundedFormulaInf.functionsIn φ ∩
          FirstOrder.Language.BoundedFormulaInf.functionsIn ψ ∧
      FirstOrder.Language.BoundedFormulaInf.relationsIn θ ⊆
          FirstOrder.Language.BoundedFormulaInf.relationsIn φ ∩
            FirstOrder.Language.BoundedFormulaInf.relationsIn ψ ∧
        φ.Entails θ ∧ θ.Entails ψ
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [FirstOrder.Language.BoundedFormulaInf.relationalize](firstorder-language-boundedformulainf-relational.md)
- [Model existence](model-existence.md)
- [Universe invariance of entailment](universe-invariance-of-entailment.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.craig_interpolation`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Interpolation/Craig.html#FirstOrder.Language.craig_interpolation).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.craig_interpolation`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Interpolation/Craig.html#FirstOrder.Language.craig_interpolation)
- [Source of `FirstOrder.Language.craig_interpolation` in TauCeti/ModelTheory/Interpolation/Craig.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Interpolation/Craig.lean#L99)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
