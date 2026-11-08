---
declaration: theorem
origin: cited
lean: TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq
statement: formalized
proof: formalized
---

# The Morse form of Łojasiewicz's gradient inequality on a Riemannian manifold

Near a
nondegenerate critical point `p` of `f`, the absolute energy difference `|f y - f p|` is bounded by
a multiple of the squared Riemannian length of the gradient of `f` at `y`, for any continuous
Riemannian metric.

```lean
TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I 1 M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] {f : M → ℝ} {p : M}
  (hp : TauCeti.IsManifoldNondegenerateCriticalPoint I f p) :
  ∃ lam > 0, ∀ᶠ (y : M) in nhds p, lam * |f y - f p| ≤ ‖TauCeti.Manifold.mgradient I f y‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse form of Łojasiewicz's gradient inequality](../../../analysis/part-01/calculus/part-01/the-morse-form-of-ojasiewiczs-gradient-inequalit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.html#TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq)
- [Source of `TauCeti.IsManifoldNondegenerateCriticalPoint.exists_mul_abs_sub_le_norm_mgradient_sq` in TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.lean#L114)
