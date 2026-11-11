---
declaration: theorem
origin: cited
lean: TauCeti.g0_dichotomy_oriented
statement: formalized
proof: formalized
---

# The G₀ dichotomy, oriented form

An analytic relation `G` on a Polish space has a
countable Borel coloring, or there is a continuous map of Cantor space sending every oriented
edge of `orientedGS canonicalWords` to a pair of `G`, and not both.

```lean
TauCeti.g0_dichotomy_oriented.{u_1} {X : Type u_1} [TopologicalSpace X] [PolishSpace X]
  [MeasurableSpace X] [BorelSpace X] {G : SetRel X X} (hG : MeasureTheory.AnalyticSet G) :
  Xor G.HasCountableBorelColoring
    (∃ φ,
      Continuous φ ∧
        ∀ ⦃y z : ℕ → Bool⦄, (y, z) ∈ TauCeti.orientedGS TauCeti.canonicalWords → (φ y, φ z) ∈ G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Amalgamation across a fresh edge keeps analytic families from being small](amalgamation-across-a-fresh-edge-keeps-analytic.md)
- [Miller's independence lemma](../descriptive/millers-independence-lemma.md)
- [SetRel.IsSmallFamily](setrel-issmallfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.g0_dichotomy_oriented`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#TauCeti.g0_dichotomy_oriented).

## Sources

- [Tau Ceti documentation: `TauCeti.g0_dichotomy_oriented`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GZeroDichotomy.html#TauCeti.g0_dichotomy_oriented)
- [Source of `TauCeti.g0_dichotomy_oriented` in TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/GZeroDichotomy.lean#L416)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
