---
declaration: theorem
origin: cited
lean: SimpleGraph.g0_dichotomy
statement: formalized
proof: formalized
---

# The Kechris–Solecki–Todorcevic G₀ dichotomy

A simple graph on a Polish space whose edge
relation is analytic has a measurable coloring by `ℕ`, or receives a continuous homomorphism from
`gZero`, and not both.

```lean
SimpleGraph.g0_dichotomy.{u_1} {X : Type u_1} [TopologicalSpace X] [PolishSpace X]
  [MeasurableSpace X] [BorelSpace X] (G : SimpleGraph X)
  (hG : MeasureTheory.AnalyticSet {p | G.Adj p.1 p.2}) :
  Xor (∃ c, Measurable ⇑c) (∃ φ, Continuous ⇑φ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The G₀ dichotomy, oriented form](the-g0-dichotomy-oriented-form.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.g0_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#SimpleGraph.g0_dichotomy).

## Sources

- [Tau Ceti documentation: `SimpleGraph.g0_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#SimpleGraph.g0_dichotomy)
- [Source of `SimpleGraph.g0_dichotomy` in TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean#L433)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
