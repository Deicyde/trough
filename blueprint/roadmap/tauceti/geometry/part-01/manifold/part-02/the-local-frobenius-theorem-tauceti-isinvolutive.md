---
declaration: theorem
origin: cited
lean: TauCeti.IsInvolutiveDistribution.exists_flatChart, TauCeti.IsDistributionFrameOn.exists_openPartialHomeomorph_map_fderiv_eq_ker_snd
statement: formalized
proof: formalized
---

# The local Frobenius theorem (`TauCeti.IsInvolutiveDistribution.exists_flatChart`)

An involutive `C^m` distribution `D` of rank `k`, for `1 ≤ m`,
on a `C^n` manifold with `m + 1 ≤ n`, modelled on a finite-dimensional real space, is constant in a
suitable chart around any interior point `x`: there are a chart `e` of the `C^m` maximal atlas whose
domain contains `x` and a `k`-dimensional subspace `W` of the model space such that the differential
of `I ∘ e` carries `D y` onto `W` at every point `y` of the domain of `e`. On a boundaryless
manifold `BoundarylessManifold.isInteriorPoint` gives the interior hypothesis at every point.

```lean
TauCeti.IsInvolutiveDistribution.exists_flatChart.{u, u_1, u_2} {E : Type u} {H : Type u_1}
  {M : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I 1 M] {m : ℕ∞} (hm : 1 ≤ m) {n : WithTop ℕ∞} (hmn : ↑m + 1 ≤ n) [IsManifold I n M]
  {k : ℕ} {D : (x : M) → Submodule ℝ (TangentSpace I x)}
  (hinv : TauCeti.IsInvolutiveDistribution I D) (hD : TauCeti.IsContMDiffDistribution I (↑m) k D)
  {x : M} (hx : I.IsInteriorPoint x) :
  ∃ e W,
    e ∈ IsManifold.maximalAtlas I (↑m) M ∧
      x ∈ e.source ∧
        Module.finrank ℝ ↥W = k ∧ ∀ y ∈ e.source, Submodule.map (↑(mfderiv% (↑I ∘ ↑e) y)) (D y) = W
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem produces a `C^n` inverse](../../../../analysis/part-01/calculus/part-01/the-inverse-function-theorem-produces-a-c-n-inve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsInvolutiveDistribution.exists_flatChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/FlatChart.html#TauCeti.IsInvolutiveDistribution.exists_flatChart).

## Other forms

**The local Frobenius theorem in product coordinates.** Formalized in Tau Ceti as [`TauCeti.IsDistributionFrameOn.exists_openPartialHomeomorph_map_fderiv_eq_ker_snd`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Transverse.html#TauCeti.IsDistributionFrameOn.exists_openPartialHomeomorph_map_fderiv_eq_ker_snd).

```lean
TauCeti.IsDistributionFrameOn.exists_openPartialHomeomorph_map_fderiv_eq_ker_snd.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {n : ℕ∞} {D : E × F → Submodule ℝ (E × F)}
  {U : Set (E × F)} (hU : IsOpen U)
  {X : Fin (Module.finrank ℝ E) → (p : E × F) → TangentSpace (modelWithCornersSelf ℝ (E × F)) p}
  (hX : TauCeti.IsDistributionFrameOn (modelWithCornersSelf ℝ (E × F)) (↑n + 1) D X U)
  (hinv : TauCeti.IsInvolutiveDistributionOn (modelWithCornersSelf ℝ (E × F)) D U) {p₀ : E × F}
  (hp₀U : p₀ ∈ U) (hp₀ : Disjoint (D p₀) (LinearMap.fst ℝ E F).ker) :
  ∃ φ,
    p₀ ∈ φ.source ∧
      ↑φ p₀ = p₀ ∧
        ContDiffOn ℝ (↑n + 1) (↑φ) φ.source ∧
          ContDiffOn ℝ (↑n + 1) (↑φ.symm) φ.target ∧
            ∀ p ∈ φ.source, Submodule.map (↑(fderiv ℝ (↑φ) p)) (D p) = (LinearMap.snd ℝ E F).ker
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsInvolutiveDistribution.exists_flatChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/FlatChart.html#TauCeti.IsInvolutiveDistribution.exists_flatChart)
- [Source of `TauCeti.IsInvolutiveDistribution.exists_flatChart` in TauCeti/Geometry/Manifold/Distribution/FlatChart.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Distribution/FlatChart.lean#L188)
