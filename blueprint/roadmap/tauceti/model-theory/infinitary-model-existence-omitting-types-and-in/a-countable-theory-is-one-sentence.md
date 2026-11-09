---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Theoryω.realize_conjunction_iff
statement: formalized
proof: formalized
---

# A countable theory is one sentence

A structure satisfies the conjunction of a countable
theory exactly when it is a model of the theory.

```lean
FirstOrder.Language.Theoryω.realize_conjunction_iff.{u, v, w} {L : FirstOrder.Language}
  {T : L.Theoryω} {M : Type w} [L.Structure M] (hT : Set.Countable T) :
  FirstOrder.Language.SentenceInf.Realize (T.conjunction hT) M ↔ T.Model M
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [FirstOrder.Language.Theoryω](firstorder-language-theory.md)
- [FirstOrder.Language.Theoryω.conjunction](firstorder-language-theory-conjunction.md)
- [FirstOrder.Language.Theoryω.Model](firstorder-language-theory-model.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.realize_conjunction_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.realize_conjunction_iff).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.realize_conjunction_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.Theory%CF%89.realize_conjunction_iff)
- [Source of `FirstOrder.Language.Theoryω.realize_conjunction_iff` in TauCeti/ModelTheory/Infinitary/Theory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/Theory.lean#L186)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
