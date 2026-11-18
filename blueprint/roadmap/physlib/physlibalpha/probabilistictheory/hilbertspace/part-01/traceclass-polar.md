---
declaration: module
origin: cited
lean: ProbabilisticTheory.Polar.absOperator, ProbabilisticTheory.Polar.rangeClosure, ProbabilisticTheory.Polar.absIntoRange, ProbabilisticTheory.Polar.rangeInClosure, ProbabilisticTheory.Polar.rangeInClosure_apply, ProbabilisticTheory.Polar.denseRange_rangeInClosure, ProbabilisticTheory.Polar.absIntoRange_factor, ProbabilisticTheory.Polar.denseRange_absIntoRange
statement: formalized
proof: formalized
---

# Polar decomposition of bounded operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.Polar`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean): 24 declarations, 10 with a docstring.

> Polar decomposition `T = U |T|` of a bounded operator with a partial-isometry factor `U`.

## i. Overview

> For a bounded operator `T` with absolute value `|T|`, `‖T x‖ = ‖|T| x‖`. The resulting isometry from
> the range of `|T|` onto the range of `T` extends to the closure of that range and gives a partial
> isometry `U` with `T = U |T|` and `U⋆ T = |T|`.

## ii. Key results

> - `Polar.polarFactor` : the partial isometry of the polar decomposition.
> - `Polar.polarFactor_mul_absOperator` : `T = U |T|`.
> - `Polar.star_polarFactor_mul_self` : `U⋆ T = |T|`.
> - `Polar.polarFactor_opNorm_le` : the polar factor is a contraction.

## iv. References

> * None.

## A. The polar factor

**`ProbabilisticTheory.Polar.absOperator`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L60).

> The absolute value used in the polar construction.

```lean
noncomputable def absOperator (T : H →L[ℂ] H) : H →L[ℂ] H
```

**`ProbabilisticTheory.Polar.rangeClosure`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L63).

> The closed range subspace of the absolute value.

```lean
noncomputable def rangeClosure (T : H →L[ℂ] H) : Submodule ℂ H
```

**`ProbabilisticTheory.Polar.absIntoRange`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L67).

> The absolute value, with codomain restricted to its closed range.

```lean
noncomputable def absIntoRange (T : H →L[ℂ] H) : H →ₗ[ℂ] rangeClosure T
```

**`ProbabilisticTheory.Polar.rangeInClosure`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L73).

> The inclusion of `range |T|` into its closed range, bundled continuously.

```lean
noncomputable def rangeInClosure (T : H →L[ℂ] H) :
    (LinearMap.range (absOperator T).toLinearMap) →L[ℂ] rangeClosure T
```

**`ProbabilisticTheory.Polar.rangeInClosure_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L80).

```lean
lemma rangeInClosure_apply (T : H →L[ℂ] H) (x : LinearMap.range (absOperator T).toLinearMap) :
    (rangeInClosure T x : H) = x
```

**`ProbabilisticTheory.Polar.denseRange_rangeInClosure`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L83).

```lean
lemma denseRange_rangeInClosure (T : H →L[ℂ] H) : DenseRange (rangeInClosure T)
```

**`ProbabilisticTheory.Polar.absIntoRange_factor`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L105).

```lean
lemma absIntoRange_factor (T : H →L[ℂ] H) (x : H) :
    absIntoRange T x = rangeInClosure T ⟨absOperator T x, LinearMap.mem_range_self _ x⟩
```

**`ProbabilisticTheory.Polar.denseRange_absIntoRange`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L108).

```lean
lemma denseRange_absIntoRange (T : H →L[ℂ] H) : DenseRange (absIntoRange T)
```

**`ProbabilisticTheory.Polar.absIntoRange_apply`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L123).

```lean
lemma absIntoRange_apply (T : H →L[ℂ] H) (x : H) : (absIntoRange T x : H) = absOperator T x
```

**`ProbabilisticTheory.Polar.norm_apply_eq_norm_abs_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L125).

```lean
lemma norm_apply_eq_norm_abs_apply (T : H →L[ℂ] H) (x : H) : ‖T x‖ = ‖absOperator T x‖
```

**`ProbabilisticTheory.Polar.norm_absIntoRange_apply`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L148).

```lean
lemma norm_absIntoRange_apply (T : H →L[ℂ] H) (x : H) :
    ‖absIntoRange T x‖ = ‖absOperator T x‖
```

**`ProbabilisticTheory.Polar.instCompleteSpaceRangeClosure`**, an instance, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L153).

> The closed-range subspace is complete, so it admits the orthogonal projection used to define
> the bounded polar factor.

```lean
noncomputable instance instCompleteSpaceRangeClosure (T : H →L[ℂ] H) :
    CompleteSpace (rangeClosure T)
```

**`ProbabilisticTheory.Polar.polarOnRange`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L159).

> The polar factor on the closed range of `|T|`.

```lean
noncomputable def polarOnRange (T : H →L[ℂ] H) : rangeClosure T →L[ℂ] H
```

**`ProbabilisticTheory.Polar.polarOnRange_eq_on_abs`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L162).

```lean
lemma polarOnRange_eq_on_abs (T : H →L[ℂ] H) (x : H) :
    polarOnRange T (absIntoRange T x) = T x
```

**`ProbabilisticTheory.Polar.polarOnRange_norm_le`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L170).

```lean
lemma polarOnRange_norm_le (T : H →L[ℂ] H) (x : rangeClosure T) : ‖polarOnRange T x‖ ≤ ‖x‖
```

**`ProbabilisticTheory.Polar.polarFactor`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L181).

> The bounded polar factor, obtained by extending the range isometry by zero on the orthogonal
> complement of `closure (range |T|)`.

```lean
noncomputable def polarFactor (T : H →L[ℂ] H) : H →L[ℂ] H
```

**`ProbabilisticTheory.Polar.polarFactor_eq_on_abs`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L184).

```lean
lemma polarFactor_eq_on_abs (T : H →L[ℂ] H) (x : H) : polarFactor T (absOperator T x) = T x
```

**`ProbabilisticTheory.Polar.polarFactor_norm_le`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L193).

```lean
lemma polarFactor_norm_le (T : H →L[ℂ] H) (x : H) : ‖polarFactor T x‖ ≤ ‖x‖
```

**`ProbabilisticTheory.Polar.polarFactor_opNorm_le`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L201).

```lean
lemma polarFactor_opNorm_le (T : H →L[ℂ] H) : ‖polarFactor T‖ ≤ 1
```

**`ProbabilisticTheory.Polar.polarFactor_mul_absOperator`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L205).

```lean
lemma polarFactor_mul_absOperator (T : H →L[ℂ] H) : polarFactor T * absOperator T = T
```

### A.1. The partial-isometry adjoint identity

**`ProbabilisticTheory.Polar.polarOnRange_norm_eq`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L210).

```lean
lemma polarOnRange_norm_eq (T : H →L[ℂ] H) (y : rangeClosure T) :
    ‖polarOnRange T y‖ = ‖y‖
```

**`ProbabilisticTheory.Polar.adjoint_polarOnRange_comp_self`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L222).

> `polarOnRange T` is an isometry: its adjoint is a left inverse.

```lean
lemma adjoint_polarOnRange_comp_self (T : H →L[ℂ] H) :
    ContinuousLinearMap.adjoint (polarOnRange T) ∘L polarOnRange T = 1
```

**`ProbabilisticTheory.Polar.star_polarFactor_mul_polarFactor`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L229).

> `star (polarFactor T) * polarFactor T` is exactly the orthogonal projection onto
> `rangeClosure T`.

```lean
lemma star_polarFactor_mul_polarFactor (T : H →L[ℂ] H) :
    star (polarFactor T) * polarFactor T = (rangeClosure T).starProjection
```

**`ProbabilisticTheory.Polar.star_polarFactor_mul_self`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean#L245).

> **`U⋆ T = |T|`** for the polar factor `U` of any bounded operator `T`.

```lean
lemma star_polarFactor_mul_self (T : H →L[ℂ] H) : star (polarFactor T) * T = absOperator T
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Polar.lean)
