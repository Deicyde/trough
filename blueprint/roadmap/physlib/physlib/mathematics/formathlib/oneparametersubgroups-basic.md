---
declaration: module
origin: cited
lean: OneParameterSubgroup.exists_isUnit_intervalIntegral, OneParameterSubgroup.mul_intervalIntegral_eq_sub, OneParameterSubgroup.differentiable, OneParameterSubgroup.apply_eq_exp_smul_deriv, OneParameterSubgroup.generator_unique
statement: formalized
proof: formalized
---

# One-parameter subgroups of real Banach algebras

The module `Physlib.Mathematics.ForMathlib.OneParameterSubgroups.Basic`, [Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean): 6 declarations (1 instance with no name), 3 with a docstring.

## i. Overview

> Let `E` be a real Banach algebra. This file proves that every continuous additive character
> `U : AddChar ℝ E` has the form `U(t) = exp (t • A)`, where `A = deriv U 0`.
>
> This is the Banach-algebra argument underlying the correspondence between norm-continuous unitary
> one-parameter groups and bounded self-adjoint generators. See
> `Physlib.Mathematics.ForMathlib.OneParameterSubgroups.Unitary` for that correspondence.
>
> **Proof outline.** Continuity at zero implies that, for sufficiently small `d > 0`, the integral of
> `U` over `[0, d]` is close to `d • 1` and therefore invertible. If `I` is the indefinite integral of
> `U`, the homomorphism law gives `U(t) * I(d) = I(t + d) - I(t)`. This identity proves that `U` is
> differentiable. Setting `A` to the derivative at zero then gives the differential equation
> `U'(t) = U(t)A`. Consequently `U(t) * exp (-tA)` has zero derivative and is constant. Uniqueness
> follows by differentiating two exponential representations at zero.

## ii. Key results

> * `OneParameterSubgroup.apply_eq_exp_smul_deriv`: A continuous one-parameter subgroup is the
>   exponential of its derivative at zero.
> * `OneParameterSubgroup.generator_unique`: Any exponential generator equals the derivative at zero.

## iii. References

> * None.

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L56).

> `NormedSpace.exp`'s API wants a `ℚ`-algebra structure (for the `1/n!` coefficients), which
> isn't automatic from `NormedAlgebra ℝ E` alone; derive it once here rather than at each use site.

```lean
local instance : NormedAlgebra ℚ E
```

**`OneParameterSubgroup.exists_isUnit_intervalIntegral`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L58).

```lean
lemma exists_isUnit_intervalIntegral [Nontrivial E] (U : AddChar ℝ E) (hU : Continuous U) :
    ∃ d : ℝ, 0 < d ∧ IsUnit (∫ x in (0 : ℝ)..d, U x)
```

**`OneParameterSubgroup.mul_intervalIntegral_eq_sub`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L95).

> Translating a one-parameter subgroup translates its interval integral.

```lean
lemma mul_intervalIntegral_eq_sub (U : AddChar ℝ E) (hU : Continuous U) (s t : ℝ) :
    U s * ∫ x in (0 : ℝ)..t, U x =
      (∫ x in (0 : ℝ)..(s + t), U x) - ∫ x in (0 : ℝ)..s, U x
```

**`OneParameterSubgroup.differentiable`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L115).

```lean
lemma differentiable [Nontrivial E] (U : AddChar ℝ E) (hU : Continuous U) :
    Differentiable ℝ U
```

**`OneParameterSubgroup.apply_eq_exp_smul_deriv`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L138).

```lean
lemma apply_eq_exp_smul_deriv (U : AddChar ℝ E) (hU : Continuous U) (t : ℝ) :
    U t = NormedSpace.exp (t • deriv U 0)
```

**`OneParameterSubgroup.generator_unique`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean#L182).

> Any exponential generator of a one-parameter subgroup is its derivative at zero.

```lean
lemma generator_unique (U : AddChar ℝ E) (A : E)
    (h : ∀ t : ℝ, U t = NormedSpace.exp (t • A)) : A = deriv U 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/OneParameterSubgroups/Basic.lean)
