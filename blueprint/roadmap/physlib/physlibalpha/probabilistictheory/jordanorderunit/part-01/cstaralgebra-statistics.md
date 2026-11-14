---
declaration: module
origin: cited
lean: ProbabilisticTheory.JB.jpow_eq_pow, ProbabilisticTheory.JB.moment_eq_integral, ProbabilisticTheory.JB.apply_eq_integral, ProbabilisticTheory.JB.variance_eq_integral_sq_sub
statement: formalized
proof: formalized
---

# Spectral formulas for Jordan moments

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.CStarAlgebra.Statistics`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean): 4 declarations, 4 with a docstring.

> Jordan moments and the variance of an observable as integrals against its spectral measure.

## i. Overview

> The statistics of an observable `a` in a state `ω` of a C⋆-algebra are given by its spectral
> measure `μ_{ω,a}`: `ω(f(a)) = ∫ f dμ_{ω,a}`. The Jordan moments of `a` are defined through Jordan
> powers `a^{[n]}`. For a single observable these agree with the ordinary powers `aⁿ` of the
> C⋆-algebra, so every moment, and in particular the variance, is an integral against the spectral
> measure.

## ii. Key results

> - `JB.jpow_eq_pow` : Jordan powers of a single observable are ordinary powers.
> - `JB.moment_eq_integral` : `moment n (ω.onObservables) a = ∫ y, y^n ∂(realSpectralMeasure ω a)`
> - `JB.variance_eq_integral_sq_sub` : the variance as `∫y² dμ - (∫y dμ)²`
> - `JB.apply_eq_integral` : the expectation `ω a` as `∫ y dμ`.

## iv. References

> * None.

## A. Jordan powers of a single element are ordinary powers

**`ProbabilisticTheory.JB.jpow_eq_pow`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean#L60).

> Jordan powers of a self-adjoint element are its ordinary powers.

```lean
lemma jpow_eq_pow (a : selfAdjoint A) (n : ℕ) :
    ((JordanAlgebra.jpow a n : selfAdjoint A) : A) = (a : A) ^ n
```

## B. Moments as integrals against the outcome distribution

**`ProbabilisticTheory.JB.moment_eq_integral`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean#L77).

> The `n`-th moment of `a` in the
> state `ω` (restricted from a state on the whole C⋆-algebra) is `∫ y^n dμ_{ω,a}` — exactly
> `m_n(a) = ∫λⁿ dμ_{ω,a}`.

```lean
lemma moment_eq_integral (ω : 𝓢[ℂ, A]) (a : selfAdjoint A) (n : ℕ) :
    IsJordanOrderUnit.moment n ω.onObservables a =
      ∫ y, y ^ n ∂(realSpectralMeasure ω a)
```

**`ProbabilisticTheory.JB.apply_eq_integral`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean#L92).

> **The mean is the first moment, as an integral.** Specializing `moment_eq_integral` to `n = 1`
> gives `ω(a) = ∫ y \, d\mu_{\omega,a}`, since `IsJordanOrderUnit.moment_one` identifies the first
> moment with `ω(a)` itself.

```lean
lemma apply_eq_integral (ω : 𝓢[ℂ, A]) (a : selfAdjoint A) :
    ω.onObservables a = ∫ y, y ∂(realSpectralMeasure ω a)
```

**`ProbabilisticTheory.JB.variance_eq_integral_sq_sub`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean#L99).

> **The variance is `∫ y² dμ - (∫ y dμ)²`** for the distribution `μ` of the observable.

```lean
lemma variance_eq_integral_sq_sub (ω : 𝓢[ℂ, A]) (a : selfAdjoint A) :
    IsJordanOrderUnit.variance ω.onObservables a =
      (∫ y, y ^ 2 ∂(realSpectralMeasure ω a)) - (∫ y, y ∂(realSpectralMeasure ω a)) ^ 2
```

## Depends on

- [The distribution of an observable](../../cstaralgebra/spectralmeasure.md)
- [The self-adjoint part of a C⋆-algebra is a JB-algebra](cstaralgebra-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Statistics.lean)
