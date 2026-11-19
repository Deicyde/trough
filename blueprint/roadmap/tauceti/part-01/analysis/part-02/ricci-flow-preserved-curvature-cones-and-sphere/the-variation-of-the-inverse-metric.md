---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse
statement: formalized
proof: formalized
---

# The variation of the inverse metric

If the pairings of a one-parameter family `g_s` of
nondegenerate metrics at `y` have parameter derivative `h` at `t`, then the inverses
`g_s⁻¹ : T_y^* M → T_y M` of the flat maps have derivative `-g_t⁻¹ ∘ h ∘ g_t⁻¹` at `t`.

```lean
TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [FiniteDimensional ℝ E]
  {g : ℝ → TauCeti.Manifold.ContMDiffNondegenerateMetric} {y : M}
  {h : TangentSpace I y →L[ℝ] TangentSpace I y →L[ℝ] ℝ} {t : ℝ}
  (hh :
    ∀ (v w : TangentSpace I y),
      HasDerivAt (fun s => (((g s).toContMDiffSection y) v) w) ((h v) w) t) :
  HasDerivAt (fun s => ((g s).toContMDiffSection y).inverse)
    (-((g t).toContMDiffSection y).inverse ∘SL h ∘SL ((g t).toContMDiffSection y).inverse) t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.html#TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse)
- [Source of `TauCeti.Manifold.ContMDiffNondegenerateMetric.hasDerivAt_inverse` in TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/VectorBundle/NondegenerateMetric/Variation.lean#L91)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)
