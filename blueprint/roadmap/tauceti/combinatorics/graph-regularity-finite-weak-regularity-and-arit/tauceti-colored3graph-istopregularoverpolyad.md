---
declaration: def
origin: cited
lean: TauCeti.Colored3Graph.IsTopRegularOverPolyad
statement: formalized
---

# TauCeti.Colored3Graph.IsTopRegularOverPolyad

`H` is `(δ, r)`-top-regular over the polyad `P` when, for every top color `c` and every
family of `r` subpolyads of `P` whose union support has at least `δ` times the size of the
support of `P`, the relative density of `c` on that union is within `δ` of the relative density
of `c` over `P`. Members of the family may repeat, so this tests unions of at most `r`
subpolyads.

```lean
TauCeti.Colored3Graph.IsTopRegularOverPolyad.{u_1, u_2, u_3} {κ : Type u_1} {κ₂ : Type u_2}
  {V : Type u_3} [Fintype V] [DecidableEq V] {S : TauCeti.PairSkeleton3 κ₂ V}
  (P : TauCeti.Polyad3 S) [DecidableEq κ] (H : TauCeti.Colored3Graph κ V) (δ : ℝ) (r : ℕ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.IsTopRegularOverPolyad`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.html#TauCeti.Colored3Graph.IsTopRegularOverPolyad).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.IsTopRegularOverPolyad`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.html#TauCeti.Colored3Graph.IsTopRegularOverPolyad)
- [Source of `TauCeti.Colored3Graph.IsTopRegularOverPolyad` in TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Hypergraph/Polyad/TopRegular.lean#L83)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Regularity/STATUS.md)
