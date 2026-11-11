---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Theoryω.Entails.realize
statement: formalized
proof: formalized
---

# Universe invariance of entailment

A sentence entailed by a countable theory holds in every
nonempty model of the theory, of any cardinality and in any universe.

```lean
FirstOrder.Language.Theoryω.Entails.realize.{u, v, w} {L : FirstOrder.Language} {T : L.Theoryω}
  {φ : L.Sentenceω} (hT : Set.Countable T) (h : T.Entails φ) (M : Type w) [L.Structure M]
  [Nonempty M] (hM : T.Model M) : FirstOrder.Language.SentenceInf.Realize φ M
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Countability](countability.md)
- [Downward Löwenheim–Skolem for fragments](downward-lowenheim-skolem-for-fragments.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.Entails.realize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/CountableModel.html#FirstOrder.Language.Theory%CF%89.Entails.realize).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.Entails.realize`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/CountableModel.html#FirstOrder.Language.Theory%CF%89.Entails.realize)
- [Source of `FirstOrder.Language.Theoryω.Entails.realize` in TauCeti/ModelTheory/ModelExistence/CountableModel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/CountableModel.lean#L130)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
