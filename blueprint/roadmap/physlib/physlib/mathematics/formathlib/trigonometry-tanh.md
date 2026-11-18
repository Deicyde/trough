---
declaration: module
origin: cited
lean: deriv_tanh, contDiff_tanh, hasDerivAt_tanh, tendsto_tanh_atTop, tendsto_tanh_atBot, iteratedDeriv_tanh_is_polynomial_of_tanh, polynomial_bounded_on_interval, polynomial_tanh_bounded
statement: formalized
proof: formalized
---

# Properties of Tanh

The module `Physlib.Mathematics.ForMathlib.Trigonometry.Tanh`, [Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean): 15 declarations, 15 with a docstring.

> We want to prove that the reflectionless potential is a Schwartz map.
> This means proving that pointwise multiplication of a Schwartz map with tanh is a Schwartz map.
> This means we need to prove that all derivatives of tanh are bounded and continuous, so that
> the nth derivative of a function multiplied by tanh decays faster than any polynomial.

…

**`deriv_tanh`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L32).

> The derivative of tanh(x) is 1 - tanh(x)^2

```lean
lemma deriv_tanh : deriv Real.tanh = fun x => 1 - Real.tanh x ^ 2
```

**`contDiff_tanh`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L49).

> Tanh(x) is n times continuously differentiable for all n

```lean
lemma contDiff_tanh {n : ℕ} : ContDiff ℝ n tanh
```

**`hasDerivAt_tanh`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L62).

> The derivative of tanh at `x` is `1 - tanh(x)^2`

```lean
lemma hasDerivAt_tanh (x : ℝ) : HasDerivAt Real.tanh (1 - Real.tanh x ^ 2) x
```

**`tendsto_tanh_atTop`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L67).

> tanh(x) tends to `1` as `x → ∞`

```lean
lemma tendsto_tanh_atTop : Filter.Tendsto Real.tanh Filter.atTop (nhds 1)
```

**`tendsto_tanh_atBot`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L80).

> tanh(x) tends to `-1` as `x → -∞`

```lean
lemma tendsto_tanh_atBot : Filter.Tendsto Real.tanh Filter.atBot (nhds (-1))
```

**`iteratedDeriv_tanh_is_polynomial_of_tanh`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L85).

> The nth derivative of Tanh(x) is a polynomial of Tanh(x)

```lean
lemma iteratedDeriv_tanh_is_polynomial_of_tanh (n : ℕ) : ∃ P : Polynomial ℝ, ∀ x,
    iteratedDeriv n Real.tanh x = P.eval (Real.tanh x)
```

**`polynomial_bounded_on_interval`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L120).

> For a polynomial P, show it's bounded on any bounded interval

```lean
lemma polynomial_bounded_on_interval (P : Polynomial ℝ) (a b : ℝ) :
    ∃ M : ℝ, ∀ x : ℝ, x ∈ Set.Icc a b → |P.eval x| ≤ M
```

**`polynomial_tanh_bounded`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L132).

> For a polynomial P, show that P (tanh x) is bounded on the real line

```lean
lemma polynomial_tanh_bounded (P : Polynomial ℝ) :
    ∃ C : ℝ, ∀ x : ℝ, |P.eval (Real.tanh x)| ≤ C
```

**`iteratedDeriv_tanh_bounded`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L148).

> The nth derivative of tanh is bounded on the real line

```lean
lemma iteratedDeriv_tanh_bounded (n : ℕ) :
    ∃ C : ℝ, ∀ x : ℝ, |iteratedDeriv n Real.tanh x| ≤ C
```

**`contDiff_top_tanh`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L158).

> tanh is infinitely differentiable

```lean
lemma contDiff_top_tanh : ContDiff ℝ ∞ Real.tanh
```

**`tanh_hasTemperateGrowth`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L163).

> tanh has temperate growth

```lean
lemma tanh_hasTemperateGrowth : Function.HasTemperateGrowth Real.tanh
```

**`iteratedDeriv_tanh_differentiable`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L181).

> Iterated derivative for scaled tanh is differentiable

```lean
lemma iteratedDeriv_tanh_differentiable (n : ℕ) : Differentiable ℝ (iteratedDeriv n tanh)
```

**`tanh_const_mul_iteratedDeriv_norm_eq_iteratedFDeriv_norm`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L190).

> Norm of Iterated derivative for scaled tanh is equal to the norm of its Fderiv

```lean
lemma tanh_const_mul_iteratedDeriv_norm_eq_iteratedFDeriv_norm (n : ℕ) (x : ℝ) :
    ‖iteratedFDeriv ℝ n (fun x => tanh (κ * x)) x‖
    = |iteratedDeriv n (fun x => tanh (κ * x)) x|
```

**`iteratedDeriv_tanh_const_mul`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L197).

> Iterated derivative for scaled tanh

```lean
lemma iteratedDeriv_tanh_const_mul (n : ℕ) (κ : ℝ) : ∀ x : ℝ,
    iteratedDeriv n (fun y => Real.tanh (κ * y)) x = κ^n * (iteratedDeriv n Real.tanh) (κ * x)
```

**`tanh_const_mul_hasTemperateGrowth`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean#L233).

> tanh(κx) has temperate growth

```lean
lemma tanh_const_mul_hasTemperateGrowth (κ : ℝ) :
    Function.HasTemperateGrowth (fun x => Real.tanh (κ * x))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/Trigonometry/Tanh.lean)
