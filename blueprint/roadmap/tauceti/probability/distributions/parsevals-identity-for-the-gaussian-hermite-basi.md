---
declaration: theorem
origin: cited
lean: TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal, TauCeti.tsum_inner_mul_inner_L2piMul_gaussianHermiteHilbertBasis, TauCeti.tsum_norm_sq_integral_prod_hermite_mul_pi_gaussianReal
statement: formalized
proof: formalized
---

# Parseval's identity for the Gaussian Hermite basis

The squared norms of the Gaussian
Hermite coefficients of `f` sum to `‖f‖²`.

```lean
TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 (ProbabilityTheory.gaussianReal 0 1))) :
  ∑' (n : ℕ),
      ‖∫ (x : ℝ),
            (algebraMap ℝ 𝕜) ((Polynomial.aeval x) (Polynomial.hermite n) / √↑n.factorial) *
              ↑↑f x ∂ProbabilityTheory.gaussianReal 0 1‖ ^
        2 =
    ‖f‖ ^ 2
```

## Depends on

- [The weighted-measure basis](../weighted-orthogonal-l2-bases-completeness-hilber/part-01/the-weighted-measure-basis.md)

## Proof depends on

- [The `Fintype`-indexed product Hilbert basis](../weighted-orthogonal-l2-bases-completeness-hilber/part-01/the-fintype-indexed-product-hilbert-basis.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](../weighted-orthogonal-l2-bases-completeness-hilber/part-01/moment-determinacy-exponential-moment-form-the-r.md)
- [Parseval's identity for the Hermite basis (norm-square form)](../weighted-orthogonal-l2-bases-completeness-hilber/part-01/parsevals-identity-for-the-hermite-basis-norm-sq.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Hermite/Parseval.html#TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal).

## Other forms

**Parseval's identity for the multivariate Gaussian Hermite basis (polarized form).** Formalized in Tau Ceti as [`TauCeti.tsum_inner_mul_inner_L2piMul_gaussianHermiteHilbertBasis`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Hermite/Pi/Parseval.html#TauCeti.tsum_inner_mul_inner_L2piMul_gaussianHermiteHilbertBasis).

```lean
TauCeti.tsum_inner_mul_inner_L2piMul_gaussianHermiteHilbertBasis.{u_1, u_2} {𝕜 : Type u_1}
  [RCLike 𝕜] {ι : Type u_2} [Fintype ι]
  (f g :
    ↥(MeasureTheory.Lp 𝕜 2
        (MeasureTheory.Measure.pi fun x => ProbabilityTheory.gaussianReal 0 1))) :
  ∑' (a : ι → ℕ),
      inner 𝕜 f (TauCeti.L2piMul fun i => (TauCeti.gaussianHermiteHilbertBasis 𝕜) (a i)) *
        inner 𝕜 (TauCeti.L2piMul fun i => (TauCeti.gaussianHermiteHilbertBasis 𝕜) (a i)) g =
    inner 𝕜 f g
```

**Parseval's identity for the multivariate Gaussian Hermite basis.** Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_integral_prod_hermite_mul_pi_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Hermite/Pi/Parseval.html#TauCeti.tsum_norm_sq_integral_prod_hermite_mul_pi_gaussianReal).

```lean
TauCeti.tsum_norm_sq_integral_prod_hermite_mul_pi_gaussianReal.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜]
  {ι : Type u_2} [Fintype ι]
  (f :
    ↥(MeasureTheory.Lp 𝕜 2
        (MeasureTheory.Measure.pi fun x => ProbabilityTheory.gaussianReal 0 1))) :
  ∑' (a : ι → ℕ),
      ‖∫ (x : ι → ℝ),
            (∏ i,
                (algebraMap ℝ 𝕜)
                  ((Polynomial.aeval (x i)) (Polynomial.hermite (a i)) / √↑(a i).factorial)) *
              ↑↑f x ∂MeasureTheory.Measure.pi fun x => ProbabilityTheory.gaussianReal 0 1‖ ^
        2 =
    ‖f‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Gaussian/Hermite/Parseval.html#TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal)
- [Source of `TauCeti.tsum_norm_sq_integral_hermite_mul_gaussianReal` in TauCeti/Probability/Distributions/Gaussian/Hermite/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/Gaussian/Hermite/Parseval.lean#L59)
