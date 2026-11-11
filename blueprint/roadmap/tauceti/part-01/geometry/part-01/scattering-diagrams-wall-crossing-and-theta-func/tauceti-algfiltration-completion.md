---
declaration: def
origin: cited
lean: TauCeti.AlgFiltration.completion
statement: formalized
---

# TauCeti.AlgFiltration.completion

The completion is the subring of compatible families in the quotient tower.

```lean
TauCeti.AlgFiltration.completion.{u_1} {A : Type u_1} [Ring A] (F : TauCeti.AlgFiltration A) :
  Subring ((k : ℕᵒᵖ) → A ⧸ F.ideal (Opposite.unop k + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgFiltration.completion`](https://taucetiproject.org/docs/TauCeti/RingTheory/FilteredAlgebra/Completion.html#TauCeti.AlgFiltration.completion).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgFiltration.completion`](https://taucetiproject.org/docs/TauCeti/RingTheory/FilteredAlgebra/Completion.html#TauCeti.AlgFiltration.completion)
- [Source of `TauCeti.AlgFiltration.completion` in TauCeti/RingTheory/FilteredAlgebra/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FilteredAlgebra/Completion.lean#L66)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
