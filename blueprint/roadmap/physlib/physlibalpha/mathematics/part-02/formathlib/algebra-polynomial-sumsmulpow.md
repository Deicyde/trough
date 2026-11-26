---
declaration: module
origin: cited
lean: eq_zero_of_forall_sum_smul_pow_eq_zero
statement: formalized
proof: formalized
---

# Vector-valued polynomial functions of a real variable

The module `PhyslibAlpha.Mathematics.ForMathlib.Algebra.Polynomial.SumSmulPow`, [PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/SumSmulPow.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/SumSmulPow.lean): 1 declaration, 1 with a docstring.

> A polynomial function of a real variable with values in a real vector space vanishes
> identically only if all its coefficients vanish.

## i. Overview

> A sum `∑ m < n, t ^ m • b m` with coefficients `b m` in a real vector space `V` is a
> polynomial function of the real variable `t`. If it vanishes for every `t`, then so does its
> pairing with any linear functional on `V`, which is a real polynomial with infinitely many
> roots, hence zero. Linear functionals separate the points of `V`, so every coefficient
> vanishes.

## ii. Key results

> - `eq_zero_of_forall_sum_smul_pow_eq_zero` : the coefficients of an identically vanishing
>   polynomial function of a real variable vanish.

## iv. References

> * None.

## A. Identically vanishing polynomial functions

**`eq_zero_of_forall_sum_smul_pow_eq_zero`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/SumSmulPow.lean#L52).

> A `V`-valued polynomial function of one real variable that vanishes identically has
> vanishing coefficients. Pair with real-linear functionals, which separate points, and use
> that a real polynomial vanishing everywhere is zero.

```lean
lemma eq_zero_of_forall_sum_smul_pow_eq_zero {V : Type*} [AddCommGroup V] [Module ℝ V]
    {n : ℕ} {b : ℕ → V} (h : ∀ t : ℝ, ∑ m ∈ Finset.range n, t ^ m • b m = 0) :
    ∀ m ∈ Finset.range n, b m = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/SumSmulPow.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/SumSmulPow.lean)
