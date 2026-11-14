---
declaration: module
origin: cited
lean: eqOn_Icc_zero_of_integral_contDiff_smul_eq_zero
statement: formalized
proof: formalized
---

# Fundamental lemma on an interval

The module `Physlib.Mathematics.VariationalCalculus.Interval`, [Physlib/Mathematics/VariationalCalculus/Interval.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Interval.lean): 1 declaration, 1 with a docstring.

> The fundamental lemma of variational calculus on `[a, b]`.

## i. Overview

> A covector-valued `f` continuous on `[a, b]` with zero integral against every smooth `ψ`
> supported in `(a, b)` vanishes. This is the step from a stationary action to the Euler-Lagrange
> equations, see `LagrangianSystem.eulerLagrange_eq_zero_of_isCriticalPoint`.

## ii. Key results

> - `eqOn_Icc_zero_of_integral_contDiff_smul_eq_zero`: the fundamental lemma on `[a, b]`

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]
> * L. D. Landau and E. M. Lifshitz, Mechanics. [ref: landau\_mechanics]

## A. The fundamental lemma

**`eqOn_Icc_zero_of_integral_contDiff_smul_eq_zero`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Interval.lean#L47).

> If `f : ℝ → V →L[ℝ] ℝ` is continuous on `[a, b]` and `∫ x in a..b, f x (ψ x • v) = 0` for
> every smooth `ψ` supported in `(a, b)` and every `v : V`, then `f = 0` on `[a, b]`.

```lean
lemma eqOn_Icc_zero_of_integral_contDiff_smul_eq_zero {f : ℝ → V →L[ℝ] ℝ} {a b : ℝ}
    (hf : ContinuousOn f (Icc a b)) (hab : a < b)
    (hint : ∀ ψ : ℝ → ℝ, ContDiff ℝ ∞ ψ → tsupport ψ ⊆ Ioo a b →
      ∀ v : V, ∫ x in a..b, f x (ψ x • v) = 0) :
    ∀ x ∈ Icc a b, f x = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/VariationalCalculus/Interval.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/Interval.lean)
