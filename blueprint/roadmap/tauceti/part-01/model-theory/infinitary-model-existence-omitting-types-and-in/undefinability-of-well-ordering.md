---
declaration: theorem
origin: cited
lean: FirstOrder.Language.wellOrdering_undefinable
statement: formalized
proof: formalized
---

# Undefinability of well-ordering

No `L_{ω₁ω}` sentence has as its models exactly the
structures in `Type w` in which `lt` is a well-order.

```lean
FirstOrder.Language.wellOrdering_undefinable.{u, v, w} {L : FirstOrder.Language}
  (lt : L.Relations 2) :
  ¬∃ φ,
      ∀ (M : Type w) (x : L.Structure M),
        FirstOrder.Language.SentenceInf.Realize φ M ↔
          IsWellOrder M fun x_1 y => FirstOrder.Language.Structure.RelMap lt ![x_1, y]
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Model existence](model-existence.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.wellOrdering_undefinable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.wellOrdering_undefinable).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.wellOrdering_undefinable`](https://taucetiproject.org/docs/TauCeti/ModelTheory/WellOrdering.html#FirstOrder.Language.wellOrdering_undefinable)
- [Source of `FirstOrder.Language.wellOrdering_undefinable` in TauCeti/ModelTheory/WellOrdering.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/WellOrdering.lean#L722)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
