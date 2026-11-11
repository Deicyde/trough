---
declaration: theorem
origin: cited
lean: ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian
statement: formalized
proof: formalized
---

# Green's second identity against a test function

For `u` of class `C²` on the open set
`Ω` and a test function `φ` on `Ω`, `∫ Δφ • u ∂μ = ∫ φ • Δu ∂μ`: the classical Laplacian of a `C²`
function is its distributional Laplacian.

```lean
ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {Ω : TopologicalSpace.Opens E} {u : E → F} [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure]
  (hu : ContDiffOn ℝ 2 u ↑Ω) (φ : TestFunction Ω ℝ ⊤) :
  ∫ (x : E), Laplacian.laplacian (⇑φ) x • u x ∂μ = ∫ (x : E), φ x • Laplacian.laplacian u x ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Laplacian.html#ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian).

## Sources

- [Tau Ceti documentation: `ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/WeakDeriv/Laplacian.html#ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian)
- [Source of `ContDiffOn.integral_laplacian_smul_eq_integral_smul_laplacian` in TauCeti/Analysis/Sobolev/WeakDeriv/Laplacian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/WeakDeriv/Laplacian.lean#L114)
