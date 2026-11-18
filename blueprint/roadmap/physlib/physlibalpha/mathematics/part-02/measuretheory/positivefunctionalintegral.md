---
declaration: module
origin: cited
lean: ContinuousMap.instPosSMulMono, ker_le_ker_of_nonneg, rangeFunctional, rangeFunctional_apply, exists_positive_extension, exists_regular_probabilityMeasure_integral_eq
statement: formalized
proof: formalized
---

# Positive functionals are integrals

The module `PhyslibAlpha.Mathematics.MeasureTheory.PositiveFunctionalIntegral`, [PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean): 6 declarations, 3 with a docstring.

> A positive functional given on part of `C(X, ℝ)` is integration against a probability measure.

## i. Overview

> On a compact space `X`, a positive linear functional on continuous functions is integration against
> a measure. This is the Riesz–Markov–Kakutani theorem. Often the functional is only known on some
> continuous functions, for example on observables seen as functions on the pure states.
>
> Here the functional `φ` is given through a linear map `T : V → C(X, ℝ)` whose range contains the
> constant `1`. Suppose `φ v ≥ 0` whenever `T v ≥ 0`, and `φ` equals `1` at a preimage of `1`. Then
> `φ` is integration of `T` against a regular probability measure. The M. Riesz extension theorem
> first extends `φ` positively to all continuous functions.

## ii. Key results

> - `ContinuousMap.instPosSMulMono` proves that scaling by a nonnegative number preserves the order of
>   continuous functions.
> - `exists_positive_extension` proves that `φ` extends to a positive functional on `C(X, ℝ)`.
> - `exists_regular_probabilityMeasure_integral_eq` proves that `φ` is an integral.

## iv. References

> * None.

## A. Scaling continuous functions preserves their order

**`ContinuousMap.instPosSMulMono`**, an instance, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L56).

```lean
instance ContinuousMap.instPosSMulMono {X : Type*} [TopologicalSpace X] :
    PosSMulMono ℝ C(X, ℝ)
```

## B. Positive functionals are integrals

**`ker_le_ker_of_nonneg`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L72).

```lean
lemma ker_le_ker_of_nonneg : LinearMap.ker T ≤ LinearMap.ker φ
```

**`rangeFunctional`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L80).

> The functional `φ` on the range of `T`.

```lean
noncomputable def rangeFunctional : C(X, ℝ) →ₗ.[ℝ] ℝ
```

**`rangeFunctional_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L85).

```lean
lemma rangeFunctional_apply (v : V) : rangeFunctional T φ hpos ⟨T v, v, rfl⟩ = φ v
```

**`exists_positive_extension`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L97).

> **M. Riesz extension**: `φ` extends to a positive functional on all continuous functions.

```lean
lemma exists_positive_extension : ∃ Λ : C(X, ℝ) →ₗ[ℝ] ℝ,
    (∀ v, Λ (T v) = φ v) ∧ ∀ g, 0 ≤ g → 0 ≤ Λ g
```

**`exists_regular_probabilityMeasure_integral_eq`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean#L108).

> **Positive functionals are integrals**: a positive linear functional through `T`, equal to `1`
> on a preimage of `1`, is integration against a regular probability measure.

```lean
lemma exists_regular_probabilityMeasure_integral_eq (hφ : φ one = 1) :
    ∃ μ : Measure X, μ.Regular ∧ IsProbabilityMeasure μ ∧ ∀ v, ∫ x, T v x ∂μ = φ v
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/PositiveFunctionalIntegral.lean)
