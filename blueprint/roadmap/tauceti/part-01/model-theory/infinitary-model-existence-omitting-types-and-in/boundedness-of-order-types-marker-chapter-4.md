---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Sentenceω.wellOrder_type_boundedness
statement: formalized
proof: formalized
---

# Boundedness of order types (Marker, Chapter 4)

If `lt` well-orders every model of `φ` in
`Type w`, of any cardinality, then their order types are bounded by a countable ordinal.

```lean
FirstOrder.Language.Sentenceω.wellOrder_type_boundedness.{u, v, w} {L : FirstOrder.Language}
  {φ : L.Sentenceω} {lt : L.Relations 2}
  (hwo :
    ∀ (M : Type w) (x : L.Structure M),
      FirstOrder.Language.SentenceInf.Realize φ M →
        IsWellOrder M fun x_1 y => FirstOrder.Language.Structure.RelMap lt ![x_1, y]) :
  ∃ α < Ordinal.omega 1,
    ∀ (M : Type w) (inst : L.Structure M) (h : FirstOrder.Language.SentenceInf.Realize φ M),
      (Ordinal.type fun x y => FirstOrder.Language.Structure.RelMap lt ![x, y]) < α
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Model existence](model-existence.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Sentenceω.wellOrder_type_boundedness`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.Sentence%CF%89.wellOrder_type_boundedness).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Sentenceω.wellOrder_type_boundedness`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.Sentence%CF%89.wellOrder_type_boundedness)
- [Source of `FirstOrder.Language.Sentenceω.wellOrder_type_boundedness` in TauCeti/ModelTheory/WellOrdering.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/WellOrdering.lean#L689)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
