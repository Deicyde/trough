---
declaration: module
origin: cited
lean: PositiveLinearMap.conjugateₚ, ContinuousLinearMap.traceₚ, ContinuousLinearMap.traceₚ_isTracial, ContinuousLinearMap.traceMulOpₚ, ContinuousLinearMap.traceMulOpₚ_apply_of_nonneg, ContinuousLinearMap.traceMulOpₚ_apply_of_not_nonneg
statement: formalized
proof: formalized
---

# The trace as a positive map

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Trace`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean): 6 declarations, 4 with a docstring.

> The trace on bounded operators as a positive tracial functional, and the functional `Tr (x ρ)`.

## i. Overview

> The linear-algebra trace is a positive tracial functional on the bounded operators; on a
> finite-dimensional Hilbert space it is the usual trace. For positive `ρ`, `x ↦ Tr (x ρ)` is
> positive.

## ii. Key results

> - `PositiveLinearMap.conjugateₚ` : conjugation as a positive map.
> - `ContinuousLinearMap.traceₚ` : the trace as a positive map.
> - `ContinuousLinearMap.traceMulOpₚ` : `x ↦ Tr (x ρ)`.
> - `ContinuousLinearMap.traceₚ_isTracial` : the trace is tracial.

## iv. References

> * None.

## A. Conjugation as a positive map

**`PositiveLinearMap.conjugateₚ`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L62).

> Conjugation `x ↦ c * x * star x`, as a positive linear map.

```lean
def _root_.PositiveLinearMap.conjugateₚ (c : A) : A →ₚ[R] A
```

## B. The trace as a positive functional

**`ContinuousLinearMap.traceₚ`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L87).

> The trace on continuous linear maps, bundled as a positive linear map.

```lean
noncomputable def traceₚ : (E →L[ℂ] E) →ₚ[ℂ] ℂ
```

**`ContinuousLinearMap.traceₚ_isTracial`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L96).

> The trace is tracial.

```lean
lemma traceₚ_isTracial : (traceₚ (E := E)).toLinearMap.IsTracial
```

**`ContinuousLinearMap.traceMulOpₚ`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L102).

> The positive linear functional `x ↦ tr (√ρ * x * √ρ†)`.

```lean
noncomputable def traceMulOpₚ (ρ : E →L[ℂ] E) : (E →L[ℂ] E) →ₚ[ℂ] ℂ
```

**`ContinuousLinearMap.traceMulOpₚ_apply_of_nonneg`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L106).

```lean
lemma traceMulOpₚ_apply_of_nonneg {ρ : E →L[ℂ] E} (h : 0 ≤ ρ) (x : E →L[ℂ] E) :
    ρ.traceMulOpₚ x = (↑x * ↑ρ : E →ₗ[ℂ] E).trace ℂ E
```

**`ContinuousLinearMap.traceMulOpₚ_apply_of_not_nonneg`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean#L115).

```lean
lemma traceMulOpₚ_apply_of_not_nonneg {ρ : E →L[ℂ] E} (h : ¬0 ≤ ρ) (x : E →L[ℂ] E) :
    ρ.traceMulOpₚ x = 0
```

## Depends on

- [Tracial functionals](../../../../physlib/probabilistictheory/staralgebra/traciality.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Trace.lean)
