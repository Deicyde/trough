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

- [The Kechris–Solecki–Todorcevic lemma](the-kechris-solecki-todorcevic-lemma.md)
- [Miller's independence lemma](millers-independence-lemma.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.g0_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#SimpleGraph.g0_dichotomy).

## Sources

- [Tau Ceti documentation: `SimpleGraph.g0_dichotomy`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#SimpleGraph.g0_dichotomy)
- [Source of `SimpleGraph.g0_dichotomy` in TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean#L428)
