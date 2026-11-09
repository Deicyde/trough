---
declaration: def
origin: cited
lean: TauCeti.Colored3Graph.TopRegularOverMostPolyads
statement: formalized
---

# TauCeti.Colored3Graph.TopRegularOverMostPolyads

`H` is `(η, r)`-top-regular over most polyads of `C`: the polyads over which `H` is not
`(η, r)`-top-regular carry at most an `ε`-proportion of the selected support.

```lean
TauCeti.Colored3Graph.TopRegularOverMostPolyads.{u_1, u_2} {V : Type u_1} [Fintype V]
  [DecidableEq V] {κ : Type u_2} [DecidableEq κ] (H : TauCeti.Colored3Graph κ V)
  (C : TauCeti.TriadicComplex3 V) (η ε : ℝ) (r : ℕ) : Prop
```

## Depends on

- [TauCeti.Colored3Graph.IsTopRegularOverPolyad](tauceti-colored3graph-istopregularoverpolyad.md)
- [TauCeti.TriadicComplex3](tauceti-triadiccomplex3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.TopRegularOverMostPolyads`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/Basic.html#TauCeti.Colored3Graph.TopRegularOverMostPolyads).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.TopRegularOverMostPolyads`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/Basic.html#TauCeti.Colored3Graph.TopRegularOverMostPolyads)
- [Source of `TauCeti.Colored3Graph.TopRegularOverMostPolyads` in TauCeti/Combinatorics/Hypergraph/Triadic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Hypergraph/Triadic/Basic.lean#L362)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
