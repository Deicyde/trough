---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.expectation_ofDensity, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.covariance_ofDensity, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.variance_ofDensity, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.robertson_schrodinger_ofDensity, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.trace_rankOne_self, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity_rankOne
statement: formalized
proof: formalized
---

# Uncertainty in density-operator states

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.State.DensityUncertainty`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean): 6 declarations, 6 with a docstring.

> Expectation, covariance, variance and Robertson–Schrödinger for density-operator states.

## i. Overview

> The state of a density operator `ρ` is a state on the C⋆-algebra of bounded operators, so the
> uncertainty relations of C⋆-algebras apply to it. Its expectation, covariance and variance are
> traces against `ρ`, and the state of a rank-one projection `|ψ⟩⟨ψ|` is the vector state of `ψ`.

## ii. Key results

> - `UnitalPositiveLinearMap.expectation_ofDensity` : the expectation of `a` is `Re Tr(a ρ)`.
> - `UnitalPositiveLinearMap.covariance_ofDensity`, `UnitalPositiveLinearMap.variance_ofDensity` :
>   covariance and variance as traces.
> - `UnitalPositiveLinearMap.robertson_schrodinger_ofDensity` : the Robertson–Schrödinger relation for
>   density operators.
> - `UnitalPositiveLinearMap.ofDensity_rankOne` : rank-one density operators give vector states.

## iv. References

> * None.

## A. Statistics of density states as traces

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.expectation_ofDensity`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L61).

> The expectation of an observable in a density state is the real part of `Tr(a ρ)`.

```lean
lemma expectation_ofDensity (a : Observable (H →L[ℂ] H)) :
    (ofDensity hpos hnorm)⟨a⟩ = ((↑(a : H →L[ℂ] H) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.covariance_ofDensity`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L66).

> The covariance in a density state is `Re Tr(δa δb ρ)` for the centered observables.

```lean
lemma covariance_ofDensity (a b : Observable (H →L[ℂ] H)) :
    covariance (ofDensity hpos hnorm) a b =
      ((↑((centered (ofDensity hpos hnorm) a : H →L[ℂ] H) *
        centered (ofDensity hpos hnorm) b) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.variance_ofDensity`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L73).

> The variance in a density state is `Re Tr(δa² ρ)` for the centered observable.

```lean
lemma variance_ofDensity (a : Observable (H →L[ℂ] H)) :
    variance (ofDensity hpos hnorm) a =
      ((↑((centered (ofDensity hpos hnorm) a : H →L[ℂ] H) *
        centered (ofDensity hpos hnorm) a) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re
```

## B. Robertson–Schrödinger for density operators

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.robertson_schrodinger_ofDensity`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L85).

> **Robertson–Schrödinger relation for mixed states.** For a density operator `ρ` and
> observables `a`, `b` with centered parts `δa`, `δb`,
> `(Re Tr(δa δb ρ))² + (Re Tr(⁅a, b⁆ ρ))² ≤ Re Tr(δa² ρ) · Re Tr(δb² ρ)`,
> where `⁅a, b⁆ = -(i/2)(ab - ba)`.

```lean
lemma robertson_schrodinger_ofDensity (a b : Observable (H →L[ℂ] H)) :
    ((↑((centered (ofDensity hpos hnorm) a : H →L[ℂ] H) *
        centered (ofDensity hpos hnorm) b) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re ^ 2 +
      ((↑((⁅a, b⁆ : Observable (H →L[ℂ] H)) : H →L[ℂ] H) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re ^ 2 ≤
      ((↑((centered (ofDensity hpos hnorm) a : H →L[ℂ] H) *
        centered (ofDensity hpos hnorm) a) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re *
      ((↑((centered (ofDensity hpos hnorm) b : H →L[ℂ] H) *
        centered (ofDensity hpos hnorm) b) * ↑ρ : H →ₗ[ℂ] H).trace ℂ H).re
```

## C. Vector states as rank-one density states

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.trace_rankOne_self`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L103).

> For a unit vector `ψ`, the projection `|ψ⟩⟨ψ|` has trace one.

```lean
lemma trace_rankOne_self {ψ : H} (h : ‖ψ‖ = 1) :
    ((InnerProductSpace.rankOne ℂ ψ ψ : H →L[ℂ] H) : H →ₗ[ℂ] H).trace ℂ H = 1
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity_rankOne`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean#L110).

> The density state of the projection `|ψ⟩⟨ψ|` is the vector state of `ψ`: pure states are
> the rank-one mixed states.

```lean
lemma ofDensity_rankOne {ψ : H} (h : ‖ψ‖ = 1) :
    ofDensity (nonneg_iff_isPositive.mpr (InnerProductSpace.isPositive_rankOne_self ψ))
      (trace_rankOne_self h) = ofVec h
```

## Depends on

- [Density operators](state-density.md)
- [Vector states](state-vector.md)
- [The Lie bracket of observables](../../staralgebra/lie.md)
- [Expectation, variance and covariance](../../staralgebra/statistics.md)

## Proof depends on

- [Uncertainty relations](../../cstaralgebra/uncertainty.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/DensityUncertainty.lean)
