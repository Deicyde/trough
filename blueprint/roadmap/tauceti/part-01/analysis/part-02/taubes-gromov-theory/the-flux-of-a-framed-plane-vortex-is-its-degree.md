---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow
statement: formalized
proof: formalized
---

# The flux of a framed plane vortex is its degree

Let `x` be a `C²` vortex on the whole
plane whose section has the degree-`m` end framing `α(z) (z / |z|)⁻ᵐ → 1`. Then the curvature
coefficient `∂₁ b₂ - ∂₂ b₁` integrates to `-2π m`; equivalently, since
`iF_a = -(∂₁ b₂ - ∂₂ b₁) ds ∧ dt`, the flux `(2π)⁻¹ ∫ iF_a` is `m`.

```lean
TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow
  {x : ℂ → EuclideanSpace ℝ (Fin 4)} (hb₁ : ContDiff ℝ 2 fun w => (x w).ofLp 0)
  (hb₂ : ContDiff ℝ 2 fun w => (x w).ofLp 1) (hp : ContDiff ℝ 2 fun w => (x w).ofLp 2)
  (hq : ContDiff ℝ 2 fun w => (x w).ofLp 3) (hsol : ∀ (z : ℂ), TauCeti.Vortex.equation x z = 0)
  {m : ℕ}
  (hframe :
    Filter.Tendsto (fun z => TauCeti.Vortex.sectionValue x z * ((z / ↑‖z‖) ^ m)⁻¹)
      (Filter.cocompact ℂ) (nhds 1)) :
  ∫ (z : ℂ), TauCeti.Vortex.curvature x z = -(2 * Real.pi * ↑m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`](../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/the-cauchy-pompeiu-formula-for-a-compactly-suppo.md)
- [Green's second identity against a test function](../../part-03/sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Radial fundamental theorem of calculus](../../../measure-theory/constructions/radial-fundamental-theorem-of-calculus.md)
- [TauCeti.cauchyTransform](../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-cauchytransform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Flux.html#TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Flux.html#TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow)
- [Source of `TauCeti.Vortex.integral_curvature_eq_of_tendsto_sectionValue_mul_inv_pow` in TauCeti/Analysis/PDE/Vortex/Flux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Vortex/Flux.lean#L404)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
