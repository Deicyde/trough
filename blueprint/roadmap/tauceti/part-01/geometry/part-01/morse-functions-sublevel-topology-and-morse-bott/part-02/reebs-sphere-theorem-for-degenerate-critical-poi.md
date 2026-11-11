---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints
statement: formalized
proof: formalized
---

# Reeb's sphere theorem for degenerate critical points

If a smooth function on a compact
boundaryless manifold `M` modelled on a real vector space of dimension `m > 0` has exactly two
critical points, then `M` is homeomorphic to the sphere `Sᵐ`. The critical points may be
degenerate, for instance with vanishing Hessian. The conclusion is a homeomorphism only: `M` need
not be diffeomorphic to the standard sphere.

```lean
TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ}
  (hdim : 0 < Module.finrank ℝ E) (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  (h2 : TauCeti.totalCriticalCount I f = 2) : Nonempty (M ≃ₜ ↑(Metric.sphere 0 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's theorem on inverse sets](../../../../topology/other-results/browns-theorem-on-inverse-sets.md)
- [Fermat's theorem on a manifold](../part-01/fermats-theorem-on-a-manifold.md)
- [The Jordan–Brouwer separation theorem](../../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.html#TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.html#TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints)
- [Source of `TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints` in TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.lean#L141)
