---
declaration: theorem
origin: cited
lean: TauCeti.GromovWassersteinSpace.completeSpace_iff
statement: formalized
proof: formalized
---

# Characterization of completeness of the Gromov–Wasserstein space (BMNN Theorem 39)

For
every `1 ≤ p ≤ ∞`, `GromovWassersteinSpace.{u} p Z` is complete if and only if the ground metric
space `Z` is complete.

```lean
TauCeti.GromovWassersteinSpace.completeSpace_iff.{u, v} {p : ENNReal} {Z : Type v} [MetricSpace Z]
  [Fact (1 ≤ p)] : CompleteSpace (TauCeti.GromovWassersteinSpace p Z) ↔ CompleteSpace Z
```

## Depends on

- [TauCeti.GromovWassersteinSpace](tauceti-gromovwassersteinspace.md)

## Proof depends on

- [Fatou's lemma for `Lᵖ` approximation](../function/part-01/fatous-lemma-for-lp-approximation.md)
- [Lusin's theorem](../function/part-01/lusins-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GromovWassersteinSpace.completeSpace_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Complete.html#TauCeti.GromovWassersteinSpace.completeSpace_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GromovWassersteinSpace.completeSpace_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Complete.html#TauCeti.GromovWassersteinSpace.completeSpace_iff)
- [Source of `TauCeti.GromovWassersteinSpace.completeSpace_iff` in TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Complete.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/GromovWasserstein/Complete.lean#L370)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OptimalTransport/STATUS.md)
