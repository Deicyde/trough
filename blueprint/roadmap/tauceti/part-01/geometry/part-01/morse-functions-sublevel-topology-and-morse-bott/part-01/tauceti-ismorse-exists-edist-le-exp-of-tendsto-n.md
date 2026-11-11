---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient
statement: formalized
proof: formalized
---

# TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient

A convergent prescribed forward trajectory of a Morse function satisfies an exponential
Riemannian extended-distance bound for every nonnegative time. No compact trap or criticality
hypothesis on the limit needs to be supplied.

```lean
TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [PseudoEMetricSpace M] [ChartedSpace H M]
  [T2Space M] [IsManifold I 2 M] [BoundarylessManifold I M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x] [IsRiemannianManifold I M]
  {f : M → ℝ} {γ : ℝ → M} {p : M} (hf : TauCeti.IsMorse I f)
  (hγ : IsMIntegralCurveOn γ (-TauCeti.Manifold.mgradient I f) (Set.Ici 0))
  (hconv : Filter.Tendsto γ Filter.atTop (nhds p)) :
  ∃ C > 0, ∃ c > 0, ∀ t ≥ 0, edist (γ t) p ≤ ENNReal.ofReal (C * Real.exp (-(c * t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Schwarz inequality](../../../../measure-theory/integral/part-01/the-cauchy-schwarz-inequality.md)
- [The Morse form of Łojasiewicz's gradient inequality on a Riemannian manifold](the-morse-form-of-ojasiewiczs-gradient-inequalit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Trajectory.html#TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Trajectory.html#TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient)
- [Source of `TauCeti.IsMorse.exists_edist_le_exp_of_tendsto_neg_mgradient` in TauCeti/Geometry/Manifold/Morse/Trajectory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Trajectory.lean#L182)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
