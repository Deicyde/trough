---
declaration: theorem
origin: cited
lean: TauCeti.finrank_deRhamCohomology_sphere
statement: formalized
proof: formalized
---

# The de Rham cohomology of spheres

For `n ≥ 1`, the de Rham cohomology `H^k(Sⁿ)` of the
unit sphere `Sⁿ` of an `(n + 1)`-dimensional real inner product space is one-dimensional in degrees
`0` and `n`, and zero in every other degree.

```lean
TauCeti.finrank_deRhamCohomology_sphere.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] (hn : 0 < n) (k : ℕ) :
  Module.finrank ℝ
      (TauCeti.deRhamCohomology (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n)))
        (↑(Metric.sphere 0 1)) k) =
    if k = 0 ∨ k = n then 1 else 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré lemma on manifolds](../../../part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_deRhamCohomology_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Sphere.html#TauCeti.finrank_deRhamCohomology_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_deRhamCohomology_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Sphere.html#TauCeti.finrank_deRhamCohomology_sphere)
- [Source of `TauCeti.finrank_deRhamCohomology_sphere` in TauCeti/Geometry/Manifold/DeRham/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/Sphere.lean#L264)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
