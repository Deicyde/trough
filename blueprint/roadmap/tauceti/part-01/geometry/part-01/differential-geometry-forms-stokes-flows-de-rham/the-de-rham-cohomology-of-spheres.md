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

- [Homotopy invariance of de Rham cohomology](homotopy-invariance-of-de-rham-cohomology.md)
- [The Mayer–Vietoris short exact sequence of de Rham complexes](the-mayer-vietoris-short-exact-sequence-of-de-rh.md)
- [The Poincaré lemma on manifolds](../../part-02/manifold/part-02/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_deRhamCohomology_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Sphere.html#TauCeti.finrank_deRhamCohomology_sphere).

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_deRhamCohomology_sphere`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Sphere.html#TauCeti.finrank_deRhamCohomology_sphere)
- [Source of `TauCeti.finrank_deRhamCohomology_sphere` in TauCeti/Geometry/Manifold/DeRham/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/Sphere.lean#L264)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
