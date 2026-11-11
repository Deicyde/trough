---
declaration: theorem
origin: cited
lean: TauCeti.deRhamCohomology.map_eq_of_homotopy
statement: formalized
proof: formalized
---

# Homotopy invariance of de Rham cohomology

If `F : M × [0, 1] → M'` is a smooth
homotopy from `f` to `g`, then `f` and `g` induce the same map on de Rham cohomology. The source
`M` may have boundary or corners.

```lean
TauCeti.deRhamCohomology.map_eq_of_homotopy.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  {H : Type u_2} {E' : Type u_3} {H' : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H']
  {I : ModelWithCorners ℝ E H} {I' : ModelWithCorners ℝ E' H'} {M : Type u_5} {M' : Type u_6}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [TopologicalSpace M']
  [ChartedSpace H' M'] [IsManifold I' 2 M'] {f g : M → M'} (hf : ContMDiff I I' (↑⊤) f)
  (hg : ContMDiff I I' (↑⊤) g) {F : M × ↑(Set.Icc 0 1) → M'}
  (hF : ContMDiff (I.prod (modelWithCornersEuclideanHalfSpace 1)) I' (↑⊤) F)
  (h₀ : ∀ (x : M), F (x, 0) = f x) (h₁ : ∀ (x : M), F (x, 1) = g x) (k : ℕ) :
  TauCeti.deRhamCohomology.map f hf k = TauCeti.deRhamCohomology.map g hg k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.deRhamCohomology.map_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomotopyInvariance.html#TauCeti.deRhamCohomology.map_eq_of_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.deRhamCohomology.map_eq_of_homotopy`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/HomotopyInvariance.html#TauCeti.deRhamCohomology.map_eq_of_homotopy)
- [Source of `TauCeti.deRhamCohomology.map_eq_of_homotopy` in TauCeti/Geometry/Manifold/DeRham/HomotopyInvariance.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DeRham/HomotopyInvariance.lean#L102)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
