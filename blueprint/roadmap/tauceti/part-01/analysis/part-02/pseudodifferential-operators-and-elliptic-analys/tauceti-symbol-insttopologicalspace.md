---
declaration: instance
origin: cited
lean: TauCeti.Symbol.instTopologicalSpace
statement: formalized
---

# TauCeti.Symbol.instTopologicalSpace

The topology of the symbol class: the locally convex topology of the seminorms
`p_{K,α,β}`.

```lean
TauCeti.Symbol.instTopologicalSpace.{u_1, u_2} {n : ℕ} {V : Type u_1} {W : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W] {m : ℝ} :
  TopologicalSpace (TauCeti.Symbol n V W m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.instTopologicalSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Topology.html#TauCeti.Symbol.instTopologicalSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.instTopologicalSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Topology.html#TauCeti.Symbol.instTopologicalSpace)
- [Source of `TauCeti.Symbol.instTopologicalSpace` in TauCeti/Analysis/Pseudodifferential/Symbol/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Symbol/Topology.lean#L277)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
