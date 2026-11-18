---
declaration: theorem
origin: cited
lean: TauCeti.isCoveringMapOn_setOf_isRegularValue
statement: formalized
proof: formalized
---

# TauCeti.isCoveringMapOn_setOf_isRegularValue

A proper `C^n` map between finite-dimensional manifolds of equal dimension covers its
regular values. The covering need not be surjective: values outside the image have empty fibre.
The source is boundaryless; the target may have boundary or corners.

```lean
TauCeti.isCoveringMapOn_setOf_isRegularValue.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1}
  [RCLike 𝕜] {E : Type u_2} {H : Type u_3} {M : Type u_4} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [FiniteDimensional 𝕜 E] [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} [TopologicalSpace M]
  [ChartedSpace H M] {E' : Type u_5} {H' : Type u_6} {N : Type u_7} [NormedAddCommGroup E']
  [NormedSpace 𝕜 E'] [FiniteDimensional 𝕜 E'] [TopologicalSpace H'] {J : ModelWithCorners 𝕜 E' H'}
  [TopologicalSpace N] [ChartedSpace H' N] {n : WithTop ℕ∞} [IsManifold I n M] [IsManifold J n N]
  {f : M → N} [T2Space M] [BoundarylessManifold I M]
  (hdim : Module.finrank 𝕜 E = Module.finrank 𝕜 E') (hf : ContMDiff I J n f) (hn : 1 ≤ n)
  (hp : IsProperMap f) : IsCoveringMapOn f {y | TauCeti.IsRegularValue I J f y}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCoveringMapOn_setOf_isRegularValue`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/Covering.html#TauCeti.isCoveringMapOn_setOf_isRegularValue).

## Sources

- [Tau Ceti documentation: `TauCeti.isCoveringMapOn_setOf_isRegularValue`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/Covering.html#TauCeti.isCoveringMapOn_setOf_isRegularValue)
- [Source of `TauCeti.isCoveringMapOn_setOf_isRegularValue` in TauCeti/Geometry/Manifold/RegularValue/Covering.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/RegularValue/Covering.lean#L66)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
