---
declaration: theorem
origin: cited
lean: IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn
statement: formalized
proof: formalized
---

# The Morse form of the convergence theorem

A negative gradient trajectory confined to a
compact set on which `fderiv ℝ f` is continuous and every critical point of `f` is nondegenerate
converges to a critical point of `f` in that set.

Nondegeneracy enters only through the finiteness of the critical locus, which is
`TauCeti.HasNondegenerateCriticalPointsOn.finite_setOfPred_fderiv_eq_zero`; the differentiability
and the continuity of the gradient are read off the continuity of `fderiv ℝ f` on `K`, the
gradient being the differential transported by the Riesz isometry.

```lean
IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [CompleteSpace E] {f : E → ℝ} {γ : ℝ → E}
  {K : Set E} (hγ : IsIntegralCurveOn γ (fun x x_1 => -gradient f x_1) (Set.Ici 0))
  (hK : IsCompact K) (hmaps : Set.MapsTo γ (Set.Ici 0) K) (hdiff : ∀ y ∈ K, DifferentiableAt ℝ f y)
  (hfderiv : ContinuousOn (fderiv ℝ f) K) (hM : TauCeti.HasNondegenerateCriticalPointsOn f K) :
  ∃ p ∈ K, gradient f p = 0 ∧ Filter.Tendsto γ Filter.atTop (nhds p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Convergence.html#IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn).

## Sources

- [Tau Ceti documentation: `IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Convergence.html#IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn)
- [Source of `IsIntegralCurveOn.exists_tendsto_atTop_of_hasNondegenerateCriticalPointsOn` in TauCeti/Analysis/Calculus/Morse/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Convergence.lean#L278)
