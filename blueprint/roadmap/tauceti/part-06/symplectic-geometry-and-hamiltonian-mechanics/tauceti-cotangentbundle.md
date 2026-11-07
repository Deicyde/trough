---
declaration: abbrev
origin: cited
lean: TauCeti.CotangentBundle
statement: formalized
---

# TauCeti.CotangentBundle

The cotangent bundle of a manifold `M` modelled on `I`: the total space of the bundle whose
fibre at `x` is the space of continuous linear functionals on `TangentSpace I x`. It is a manifold
modelled on `I.prod 𝓘(𝕜, E →L[𝕜] 𝕜)`.

```lean
TauCeti.CotangentBundle.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {E : Type u_2} {H : Type u_3}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) (M : Type u_4) [TopologicalSpace M] [ChartedSpace H M] :
  Type (max u_4 u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CotangentBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.html#TauCeti.CotangentBundle).

## Sources

- [Tau Ceti documentation: `TauCeti.CotangentBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.html#TauCeti.CotangentBundle)
- [Source of `TauCeti.CotangentBundle` in TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/Cotangent/Basic.lean#L69)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
