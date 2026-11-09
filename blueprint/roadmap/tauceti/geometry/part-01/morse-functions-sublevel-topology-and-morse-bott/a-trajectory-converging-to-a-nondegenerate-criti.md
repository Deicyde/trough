---
declaration: theorem
origin: cited
lean: TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient
statement: formalized
proof: formalized
---

# A trajectory converging to a nondegenerate critical point converges exponentially fast in the Riemannian distance

If the maximal integral curve `γ` of `-grad f` through `x` exists for
all positive time and converges to a nondegenerate critical point `p`, then the Riemannian
distance from `γ t` to `p` is at most `C * exp (-μ * t)` for some `μ, C > 0` and all large `t`.
This is the manifold counterpart, for an arbitrary `C¹` metric, of the vector-space theorem
`IsIntegralCurveOn.exists_norm_sub_le_mul_exp_atTop`.

```lean
TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient.{u_1, u_2, u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [IsManifold I 2 M] [BoundarylessManifold I M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] {f : M → ℝ} {x p : M}
  (hp : TauCeti.IsManifoldNondegenerateCriticalPoint I f p)
  (hx : Set.Ici 0 ⊆ maximalIntegralCurveInterval (-TauCeti.Manifold.mgradient I f) x)
  (hconv :
    Filter.Tendsto (maximalIntegralCurve (-TauCeti.Manifold.mgradient I f) x) Filter.atTop (nhds p))
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 f) :
  ∃ μ > 0,
    ∃ C > 0,
      ∀ᶠ (t : ℝ) in Filter.atTop,
        Manifold.riemannianEDist I (maximalIntegralCurve (-TauCeti.Manifold.mgradient I f) x t) p ≤
          ENNReal.ofReal (C * Real.exp (-(μ * t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse form of Łojasiewicz's gradient inequality on a Riemannian manifold](the-morse-form-of-ojasiewiczs-gradient-inequalit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.html#TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.html#TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient)
- [Source of `TauCeti.exists_riemannianEDist_le_mul_exp_maximalIntegralCurve_neg_mgradient` in TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/ExponentialConvergence.lean#L313)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
