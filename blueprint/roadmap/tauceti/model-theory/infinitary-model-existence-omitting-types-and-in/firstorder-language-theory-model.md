---
declaration: def
origin: cited
lean: FirstOrder.Language.Theoryω.Model
statement: formalized
---

# FirstOrder.Language.Theoryω.Model

A structure is a **model** of an `L_{ω₁ω}` theory when it satisfies every sentence of the
theory.

```lean
FirstOrder.Language.Theoryω.Model.{u, v, w} {L : FirstOrder.Language} (T : L.Theoryω) (M : Type w)
  [L.Structure M] : Prop
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [FirstOrder.Language.Theoryω](firstorder-language-theory.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.Model`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.Model).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.Model`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.Model)
- [Source of `FirstOrder.Language.Theoryω.Model` in TauCeti/ModelTheory/Infinitary/Theory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/Theory.lean#L86)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
