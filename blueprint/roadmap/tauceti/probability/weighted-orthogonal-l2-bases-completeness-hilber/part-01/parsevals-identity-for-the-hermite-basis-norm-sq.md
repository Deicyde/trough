---
declaration: theorem
origin: cited
lean: TauCeti.tsum_norm_sq_inner_hermiteFunctionLp, Orthonormal.norm_starProjection_sq_eq_sum, OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq, TauCeti.tsum_norm_sq_integral_normalizedChebyshevT_mul_measureT, TauCeti.tsum_norm_sq_integral_normalizedChebyshevCosine_mul, TauCeti.tsum_norm_sq_intervalIntegral_normalizedChebyshevCosine_mul, TauCeti.tsum_star_integral_normalizedChebyshevCosine_mul_mul_integral, TauCeti.tsum_star_intervalIntegral_normalizedChebyshevCosine_mul_mul_intervalIntegral, TauCeti.tsum_inner_mul_inner_hermiteFunctionLp, TauCeti.tsum_inner_mul_inner_L2piMul_hermiteFunctionLp, TauCeti.tsum_norm_sq_inner_L2piMul_hermiteFunctionLp, HilbertBasis.tsum_enorm_sq_inner, HilbertBasis.hasSum_norm_sq_inner, HilbertBasis.tsum_norm_sq_inner
statement: formalized
proof: formalized
---

# Parseval's identity for the Hermite basis (norm-square form)

the squared Hermite
coordinates of `f` sum to `‖f‖²`.

```lean
TauCeti.tsum_norm_sq_inner_hermiteFunctionLp.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 MeasureTheory.volume)) :
  ∑' (n : ℕ), ‖inner 𝕜 (TauCeti.hermiteFunctionLp 𝕜 n) f‖ ^ 2 = ‖f‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `Fintype`-indexed product Hilbert basis](the-fintype-indexed-product-hilbert-basis.md)
- [The Chebyshev `T` polynomials are a Hilbert basis of `L²(measureT)`](the-chebyshev-t-polynomials-are-a-hilbert-basis.md)
- [The Hermite functions are a Hilbert basis of `L²(ℝ)`](the-hermite-functions-are-a-hilbert-basis-of-l2.md)
- [Moment determinacy, exponential-moment form (the roadmap's B1 hypothesis)](moment-determinacy-exponential-moment-form-the-r.md)
- [The weight ↔ measure isometry](the-weight-measure-isometry.md)
- [The weighted-measure basis](the-weighted-measure-basis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_inner_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.html#TauCeti.tsum_norm_sq_inner_hermiteFunctionLp).

## Other forms

**Parseval's identity on the span `U` of a finite orthonormal family.** Formalized in Tau Ceti as [`Orthonormal.norm_starProjection_sq_eq_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Family.html#Orthonormal.norm_starProjection_sq_eq_sum).

```lean
Orthonormal.norm_starProjection_sq_eq_sum.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {ι : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] {v : ι → E}
  (hv : Orthonormal 𝕜 v) {U : Submodule 𝕜 E} [U.HasOrthogonalProjection]
  (hU : Submodule.span 𝕜 (Set.range v) = U) (x : E) :
  ‖U.starProjection x‖ ^ 2 = ∑ i, ‖inner 𝕜 (v i) x‖ ^ 2
```

**Parseval's identity for a functional.** Formalized in Tau Ceti as [`OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq).

```lean
OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2}
  {E : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι]
  (b : OrthonormalBasis ι 𝕜 E) (A : E →L[𝕜] 𝕜) : ∑ i, ‖A (b i)‖ ^ 2 = ‖A‖ ^ 2
```

**Parseval's identity for the Chebyshev basis.** Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_integral_normalizedChebyshevT_mul_measureT`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Parseval.html#TauCeti.tsum_norm_sq_integral_normalizedChebyshevT_mul_measureT).

```lean
TauCeti.tsum_norm_sq_integral_normalizedChebyshevT_mul_measureT.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 Polynomial.Chebyshev.measureT)) :
  ∑' (n : ℕ),
      ‖∫ (x : ℝ),
            (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevT n x) *
              ↑↑f x ∂Polynomial.Chebyshev.measureT‖ ^
        2 =
    ‖f‖ ^ 2
```

**Parseval's identity for the Chebyshev cosine basis (norm-square form).** Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_integral_normalizedChebyshevCosine_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Cosine/Parseval.html#TauCeti.tsum_norm_sq_integral_normalizedChebyshevCosine_mul).

```lean
TauCeti.tsum_norm_sq_integral_normalizedChebyshevCosine_mul.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 TauCeti.chebyshevAngleMeasure)) :
  ∑' (n : ℕ),
      ‖∫ (θ : ℝ),
            (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) *
              ↑↑f θ ∂TauCeti.chebyshevAngleMeasure‖ ^
        2 =
    ‖f‖ ^ 2
```

**Parseval's identity for the Chebyshev cosine basis (interval-integral form).** Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_intervalIntegral_normalizedChebyshevCosine_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Cosine/Parseval.html#TauCeti.tsum_norm_sq_intervalIntegral_normalizedChebyshevCosine_mul).

```lean
TauCeti.tsum_norm_sq_intervalIntegral_normalizedChebyshevCosine_mul.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f : ↥(MeasureTheory.Lp 𝕜 2 TauCeti.chebyshevAngleMeasure)) :
  ∑' (n : ℕ),
      ‖∫ (θ : ℝ) in 0..Real.pi, (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) * ↑↑f θ‖ ^
        2 =
    ‖f‖ ^ 2
```

**Parseval's identity for the Chebyshev cosine basis (polarized form).** Formalized in Tau Ceti as [`TauCeti.tsum_star_integral_normalizedChebyshevCosine_mul_mul_integral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Cosine/Parseval.html#TauCeti.tsum_star_integral_normalizedChebyshevCosine_mul_mul_integral).

```lean
TauCeti.tsum_star_integral_normalizedChebyshevCosine_mul_mul_integral.{u_1} {𝕜 : Type u_1}
  [RCLike 𝕜] (f g : ↥(MeasureTheory.Lp 𝕜 2 TauCeti.chebyshevAngleMeasure)) :
  ∑' (n : ℕ),
      star
          (∫ (θ : ℝ),
            (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) *
              ↑↑f θ ∂TauCeti.chebyshevAngleMeasure) *
        ∫ (θ : ℝ),
          (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) *
            ↑↑g θ ∂TauCeti.chebyshevAngleMeasure =
    inner 𝕜 f g
```

**Parseval's identity for the Chebyshev cosine basis (polarized interval-integral form).** Formalized in Tau Ceti as [`TauCeti.tsum_star_intervalIntegral_normalizedChebyshevCosine_mul_mul_intervalIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/Chebyshev/Cosine/Parseval.html#TauCeti.tsum_star_intervalIntegral_normalizedChebyshevCosine_mul_mul_intervalIntegral).

```lean
TauCeti.tsum_star_intervalIntegral_normalizedChebyshevCosine_mul_mul_intervalIntegral.{u_1}
  {𝕜 : Type u_1} [RCLike 𝕜] (f g : ↥(MeasureTheory.Lp 𝕜 2 TauCeti.chebyshevAngleMeasure)) :
  ∑' (n : ℕ),
      star
          (∫ (θ : ℝ) in 0..Real.pi,
            (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) * ↑↑f θ) *
        ∫ (θ : ℝ) in 0..Real.pi, (algebraMap ℝ 𝕜) (TauCeti.normalizedChebyshevCosine n θ) * ↑↑g θ =
    inner 𝕜 f g
```

**Parseval's identity for the Hermite basis (polarized form).** Formalized in Tau Ceti as [`TauCeti.tsum_inner_mul_inner_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.html#TauCeti.tsum_inner_mul_inner_hermiteFunctionLp).

```lean
TauCeti.tsum_inner_mul_inner_hermiteFunctionLp.{u_1} {𝕜 : Type u_1} [RCLike 𝕜]
  (f g : ↥(MeasureTheory.Lp 𝕜 2 MeasureTheory.volume)) :
  ∑' (n : ℕ),
      inner 𝕜 f (TauCeti.hermiteFunctionLp 𝕜 n) * inner 𝕜 (TauCeti.hermiteFunctionLp 𝕜 n) g =
    inner 𝕜 f g
```

**Parseval's identity for the multi-index Hermite basis (polarized form).** Formalized in Tau Ceti as [`TauCeti.tsum_inner_mul_inner_L2piMul_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Pi/Parseval.html#TauCeti.tsum_inner_mul_inner_L2piMul_hermiteFunctionLp).

```lean
TauCeti.tsum_inner_mul_inner_L2piMul_hermiteFunctionLp.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜]
  {ι : Type u_2} [Fintype ι]
  (f g : ↥(MeasureTheory.Lp 𝕜 2 (MeasureTheory.Measure.pi fun x => MeasureTheory.volume))) :
  ∑' (a : ι → ℕ),
      inner 𝕜 f (TauCeti.L2piMul fun i => TauCeti.hermiteFunctionLp 𝕜 (a i)) *
        inner 𝕜 (TauCeti.L2piMul fun i => TauCeti.hermiteFunctionLp 𝕜 (a i)) g =
    inner 𝕜 f g
```

**Parseval's identity for the multi-index Hermite basis (norm-square form).** Formalized in Tau Ceti as [`TauCeti.tsum_norm_sq_inner_L2piMul_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Pi/Parseval.html#TauCeti.tsum_norm_sq_inner_L2piMul_hermiteFunctionLp).

```lean
TauCeti.tsum_norm_sq_inner_L2piMul_hermiteFunctionLp.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜]
  {ι : Type u_2} [Fintype ι]
  (f : ↥(MeasureTheory.Lp 𝕜 2 (MeasureTheory.Measure.pi fun x => MeasureTheory.volume))) :
  ∑' (a : ι → ℕ), ‖inner 𝕜 (TauCeti.L2piMul fun i => TauCeti.hermiteFunctionLp 𝕜 (a i)) f‖ ^ 2 =
    ‖f‖ ^ 2
```

**Parseval's identity, extended-nonnegative form.** Formalized in Tau Ceti as [`HilbertBasis.tsum_enorm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.tsum_enorm_sq_inner).

```lean
HilbertBasis.tsum_enorm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  ∑' (i : ι), ‖inner 𝕜 (b i) x‖ₑ ^ 2 = ‖x‖ₑ ^ 2
```

**Parseval's identity, norm-square form.** Formalized in Tau Ceti as [`HilbertBasis.hasSum_norm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.hasSum_norm_sq_inner).

```lean
HilbertBasis.hasSum_norm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  HasSum (fun i => ‖inner 𝕜 (b i) x‖ ^ 2) (‖x‖ ^ 2)
```

**Parseval's identity, norm-square form (`tsum` version of `HilbertBasis.hasSum_norm_sq_inner`).** Formalized in Tau Ceti as [`HilbertBasis.tsum_norm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.tsum_norm_sq_inner).

```lean
HilbertBasis.tsum_norm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  ∑' (i : ι), ‖inner 𝕜 (b i) x‖ ^ 2 = ‖x‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_norm_sq_inner_hermiteFunctionLp`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.html#TauCeti.tsum_norm_sq_inner_hermiteFunctionLp)
- [Source of `TauCeti.tsum_norm_sq_inner_hermiteFunctionLp` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Parseval.lean#L57)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalL2Bases/STATUS.md)
