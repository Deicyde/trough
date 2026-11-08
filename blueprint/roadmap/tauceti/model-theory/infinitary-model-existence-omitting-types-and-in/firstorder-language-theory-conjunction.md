---
declaration: def
origin: cited
lean: FirstOrder.Language.Theoryω.conjunction
statement: formalized
---

# FirstOrder.Language.Theoryω.conjunction

The **conjunction of a countable theory**: its sentences, enumerated into the carrier `ℕ`
along `IndexCoding.ofEncodableWith`, joined by one countable conjunction. Indices that code no
sentence carry `⊤`.

```lean
FirstOrder.Language.Theoryω.conjunction.{u, v} {L : FirstOrder.Language} (T : L.Theoryω)
  (hT : Set.Countable T) : L.Sentenceω
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [FirstOrder.Language.Theoryω](firstorder-language-theory.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.conjunction`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.conjunction).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.conjunction`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.conjunction)
- [Source of `FirstOrder.Language.Theoryω.conjunction` in TauCeti/ModelTheory/Infinitary/Theory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/Theory.lean#L173)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
