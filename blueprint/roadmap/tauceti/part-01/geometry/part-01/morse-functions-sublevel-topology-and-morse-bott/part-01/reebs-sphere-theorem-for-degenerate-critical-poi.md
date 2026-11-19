---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints
statement: formalized
proof: formalized
---

# Reeb's sphere theorem for degenerate critical points

If a smooth function on a compact
boundaryless manifold `M` modelled on a real vector space of dimension `m` has exactly two critical
points, then `M` is homeomorphic to the sphere `Sᵐ`. The critical points may be degenerate, for
instance with vanishing Hessian. In dimension `0` every point is critical, so `M` consists of two
points, as does `S⁰`. The conclusion is a homeomorphism only: `M` need not be diffeomorphic to the
standard sphere.

```lean
TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (h2 : TauCeti.totalCriticalCount I f = 2) :
  Nonempty (M ≃ₜ ↑(Metric.sphere 0 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Brown's theorem on inverse sets](../../../../../part-02/topology/other-results/browns-theorem-on-inverse-sets.md)
- [Fermat's theorem on a manifold](fermats-theorem-on-a-manifold.md)
- [The Jordan–Brouwer separation theorem](../../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.html#TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.html#TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints)
- [Source of `TauCeti.nonempty_homeomorph_sphere_of_two_criticalPoints` in TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/TwoCriticalPoints.lean#L144)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
