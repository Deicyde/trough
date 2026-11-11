---
declaration: def
origin: cited
lean: TauCeti.SmoothSimplex.integral
statement: formalized
---

# TauCeti.SmoothSimplex.integral

The integral of a `p`-form `φ` over a smooth singular `p`-simplex `σ`: the integral over the
full-dimensional simplex `Δᵖ ⊆ ℝᵖ` of the pullback `σ^*φ` evaluated on the standard basis, with the
derivative of `σ` taken within `Δᵖ`. To form that derivative, `σ` is extended to `ℝᵖ`
(`TauCeti.SmoothSimplex.extension`); only its values on `Δᵖ` matter
(`TauCeti.SmoothSimplex.integral_eq_setIntegral_mpullbackWithin`).

This is a Bochner integral: it is meaningful when `F` is complete and the integrand is integrable,
as for continuous forms (`TauCeti.SmoothSimplex.integrableOn_mpullbackWithin`), and it is `0`
otherwise.

```lean
TauCeti.SmoothSimplex.integral.{u, u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ℕ} (σ : TauCeti.SmoothSimplex I M p) (φ : TauCeti.RoughForm I M F p) : F
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothSimplex.integral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Integral.html#TauCeti.SmoothSimplex.integral).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothSimplex.integral`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Integral.html#TauCeti.SmoothSimplex.integral)
- [Source of `TauCeti.SmoothSimplex.integral` in TauCeti/Geometry/Manifold/SmoothSingular/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SmoothSingular/Integral.lean#L77)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
