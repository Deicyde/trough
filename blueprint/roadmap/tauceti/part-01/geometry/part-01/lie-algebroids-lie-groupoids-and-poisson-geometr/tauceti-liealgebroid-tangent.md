---
declaration: def
origin: cited
lean: TauCeti.LieAlgebroid.tangent
statement: formalized
---

# TauCeti.LieAlgebroid.tangent

The tangent Lie algebroid of `M`: the tangent bundle with the identity anchor and the Lie
bracket of smooth vector fields.

```lean
TauCeti.LieAlgebroid.tangent.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H] (I : ModelWithCorners ℝ E H)
  (M : Type u_3) [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] :
  TauCeti.LieAlgebroid I E (TangentSpace I)
```

## Depends on

- [TauCeti.LieAlgebroid](tauceti-liealgebroid.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieAlgebroid.tangent`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Tangent.html#TauCeti.LieAlgebroid.tangent).

## Sources

- [Tau Ceti documentation: `TauCeti.LieAlgebroid.tangent`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LieAlgebroid/Tangent.html#TauCeti.LieAlgebroid.tangent)
- [Source of `TauCeti.LieAlgebroid.tangent` in TauCeti/Geometry/Manifold/LieAlgebroid/Tangent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/LieAlgebroid/Tangent.lean#L40)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
