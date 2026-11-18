---
declaration: structure
origin: cited
lean: TauCeti.FinitePolyhedralComplex
statement: formalized
---

# TauCeti.FinitePolyhedralComplex

A finite complex of rational-normal polyhedra, allowing unbounded cells and lineality.

```lean
TauCeti.FinitePolyhedralComplex.{u_1, u_2} {N : Type u_1} {V : Type u_2} [AddCommGroup N]
  [NormedAddCommGroup V] [NormedSpace ℝ V] {i : N →+ V} (h : TauCeti.Toric.IsIntegralLattice i) :
  Type u_2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FinitePolyhedralComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralComplex/Basic.html#TauCeti.FinitePolyhedralComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.FinitePolyhedralComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralComplex/Basic.html#TauCeti.FinitePolyhedralComplex)
- [Source of `TauCeti.FinitePolyhedralComplex` in TauCeti/Geometry/Convex/PolyhedralComplex/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Convex/PolyhedralComplex/Basic.lean#L62)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
