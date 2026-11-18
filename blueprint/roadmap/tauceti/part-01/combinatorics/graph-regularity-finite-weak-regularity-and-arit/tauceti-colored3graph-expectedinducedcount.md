---
declaration: def
origin: cited
lean: TauCeti.Colored3Graph.expectedInducedCount
statement: formalized
---

# TauCeti.Colored3Graph.expectedInducedCount

The predicted number of induced copies of `F` in `H` over the triadic complex `C`: the sum of
the local predictions over all placements and routes.

```lean
TauCeti.Colored3Graph.expectedInducedCount.{u_1, u_2} {κ : Type u_1} {V : Type u_2} [Fintype V]
  [DecidableEq V] (C : TauCeti.TriadicComplex3 V) (F : TauCeti.FiniteColored3Pattern κ)
  (H : TauCeti.Colored3Graph κ V) [DecidableEq κ] : ℝ
```

## Depends on

- [TauCeti.TriadicComplex3](tauceti-triadiccomplex3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.expectedInducedCount`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/Placement.html#TauCeti.Colored3Graph.expectedInducedCount).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.expectedInducedCount`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/Placement.html#TauCeti.Colored3Graph.expectedInducedCount)
- [Source of `TauCeti.Colored3Graph.expectedInducedCount` in TauCeti/Combinatorics/Hypergraph/Triadic/Placement.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Hypergraph/Triadic/Placement.lean#L461)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Regularity/STATUS.md)
