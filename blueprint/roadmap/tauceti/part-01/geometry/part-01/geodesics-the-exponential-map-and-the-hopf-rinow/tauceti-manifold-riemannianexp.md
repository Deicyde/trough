---
declaration: def
origin: cited
lean: TauCeti.Manifold.riemannianExp
statement: formalized
---

# TauCeti.Manifold.riemannianExp

The Riemannian exponential map at `p`: the value at time `1` of the maximal geodesic from `p`
with initial velocity `v`.  Outside `expDomain I M p` it takes the junk value `p`.

```lean
TauCeti.Manifold.riemannianExp.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] (I : ModelWithCorners ℝ E H) (M : Type u_3)
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsManifold I (↑⊤) M]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] (p : M) (v : TangentSpace I p) :
  M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.riemannianExp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential.html#TauCeti.Manifold.riemannianExp).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.riemannianExp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential.html#TauCeti.Manifold.riemannianExp)
- [Source of `TauCeti.Manifold.riemannianExp` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Geodesic/Exponential.lean#L110)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HopfRinow/STATUS.md)
