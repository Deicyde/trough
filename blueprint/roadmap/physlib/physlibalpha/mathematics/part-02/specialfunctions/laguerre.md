---
declaration: module
origin: cited
lean: PhyslibAlpha.laguerreCoeff, PhyslibAlpha.laguerre, PhyslibAlpha.eval_laguerre, PhyslibAlpha.eval_laguerre_zero, PhyslibAlpha.eval_derivative_laguerre, PhyslibAlpha.eval_derivative_derivative_laguerre, PhyslibAlpha.laguerreCoeff_succ_mul, PhyslibAlpha.laguerre_ode
statement: formalized
proof: formalized
---

# Generalised Laguerre polynomials

The module `PhyslibAlpha.Mathematics.SpecialFunctions.Laguerre`, [PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean): 22 declarations, 13 with a docstring.

> The generalised Laguerre polynomials `L_N^(α)` for natural `N` and `α`, their differential
> equation, their moments against `x^q e^(-x)` and the four weighted integrals of `L_N^(α)²` that
> give the radial expectation values of the hydrogen atom.

## i. Overview

> We define `L_N^(α)(x) = Σ_{i ≤ N} (-1)^i C(N + α, N - i) x^i / i!` as an explicit polynomial and
> check the Laguerre equation `x L'' + (α + 1 - x) L' + N L = 0` coefficientwise.
>
> The moments `Σ_i c_i (q + i)!` of the coefficients reduce, by the Chu–Vandermonde identity for
> the generalised binomial coefficient `Ring.choose`, to `q! · C(N + α - q - 1, N)`. With Euler's
> integral `∫₀^∞ x^q e^(-x) dx = q!` this evaluates
>
> `∫₀^∞ x^e e^(-x) L_N^(α)(x)² dx`
>
> for `e = α + 1, α, α - 1, α - 2`: the terms with large `i` vanish because the upper argument of
> the binomial coefficient is a natural number below `N`, and the remaining ones are
> `C(-1, N) = (-1)^N` and `C(-2, N) = (-1)^N (N + 1)`.

## ii. Key results

> - `laguerre`: the polynomial `L_N^(α)`.
> - `laguerre_ode`: the Laguerre differential equation.
> - `sum_laguerreCoeff_mul_factorial`: the moment identity.
> - `integral_laguerre_sq_alpha`: `∫ x^α e^(-x) L² = (N + α)!/N!`.
> - `integral_laguerre_sq_alpha_add_one`: `∫ x^(α+1) e^(-x) L² = (N + α)!/N! · (2N + α + 1)`.
> - `integral_laguerre_sq_alpha_sub_one`, `integral_laguerre_sq_alpha_sub_two`: the weights
>   `x^(α-1)` and `x^(α-2)`.

## iv. References

> - NIST Digital Library of Mathematical Functions, chapter 18, https://dlmf.nist.gov/18.
> - H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*, Springer
>   (1957).

## A. Definition and differential equation

**`PhyslibAlpha.laguerreCoeff`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L71).

> The coefficient `(-1)^i C(N + α, N - i) / i!` of `x^i` in `L_N^(α)`.

```lean
def laguerreCoeff (N α i : ℕ) : ℝ
```

**`PhyslibAlpha.laguerre`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L74).

> The generalised Laguerre polynomial `L_N^(α)(x) = Σ_i (-1)^i C(N + α, N - i) x^i / i!`.

```lean
def laguerre (N α : ℕ) : ℝ[X]
```

**`PhyslibAlpha.eval_laguerre`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L79).

```lean
lemma eval_laguerre (x : ℝ) :
    (laguerre N α).eval x = ∑ i ∈ Finset.range (N + 1), laguerreCoeff N α i * x ^ i
```

**`PhyslibAlpha.eval_laguerre_zero`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L83).

```lean
lemma eval_laguerre_zero : (laguerre N α).eval 0 = ((N + α).choose N : ℝ)
```

**`PhyslibAlpha.eval_derivative_laguerre`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L90).

```lean
lemma eval_derivative_laguerre (x : ℝ) :
    (derivative (laguerre N α)).eval x =
      ∑ i ∈ Finset.range (N + 1), laguerreCoeff N α i * ((i : ℝ) * x ^ (i - 1))
```

**`PhyslibAlpha.eval_derivative_derivative_laguerre`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L97).

```lean
lemma eval_derivative_derivative_laguerre (x : ℝ) :
    (derivative (derivative (laguerre N α))).eval x =
      ∑ i ∈ Finset.range (N + 1),
        laguerreCoeff N α i * ((i : ℝ) * ((i - 1 : ℕ) : ℝ) * x ^ (i - 1 - 1))
```

**`PhyslibAlpha.laguerreCoeff_succ_mul`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L106).

> The two-term recursion of the coefficients.

```lean
lemma laguerreCoeff_succ_mul {i : ℕ} (hi : i < N) :
    laguerreCoeff N α (i + 1) * (((i : ℝ) + 1) * ((i : ℝ) + 1 + α)) =
      -((N : ℝ) - i) * laguerreCoeff N α i
```

**`PhyslibAlpha.laguerre_ode`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L130).

> **Laguerre's differential equation** `x L'' + (α + 1 - x) L' + N L = 0`.

```lean
lemma laguerre_ode (x : ℝ) :
    x * (derivative (derivative (laguerre N α))).eval x +
      ((α : ℝ) + 1 - x) * (derivative (laguerre N α)).eval x +
        (N : ℝ) * (laguerre N α).eval x = 0
```

## B. Moments

**`PhyslibAlpha.sum_choose_mul_choose_neg`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L168).

> `Σ_i (-1)^i C(N + α, N - i) C(q + i, i) = C(N + α - q - 1, N)`, the Chu–Vandermonde identity
> with a negative upper index.

```lean
lemma sum_choose_mul_choose_neg (q : ℕ) :
    ∑ i ∈ Finset.range (N + 1), (-1 : ℤ) ^ i * ((N + α).choose (N - i) : ℤ) * ((q + i).choose i) =
      Ring.choose ((N + α : ℤ) - q - 1) N
```

**`PhyslibAlpha.sum_laguerreCoeff_mul_factorial`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L185).

> **Moments.** `Σ_i c_i (q + i)! = q! C(N + α - q - 1, N)`, the integral of `x^q e^(-x) L_N^(α)`
> with the integer binomial coefficient `Ring.choose`.

```lean
lemma sum_laguerreCoeff_mul_factorial (q : ℕ) :
    ∑ i ∈ Finset.range (N + 1), laguerreCoeff N α i * ((q + i).factorial : ℝ) =
      (q.factorial : ℝ) * ((Ring.choose ((N + α : ℤ) - q - 1) N : ℤ) : ℝ)
```

**`PhyslibAlpha.ringChoose_natCast_of_lt`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L199).

```lean
lemma ringChoose_natCast_of_lt {t : ℕ} (h : t < N) : Ring.choose (t : ℤ) N = 0
```

**`PhyslibAlpha.ringChoose_neg_one`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L202).

```lean
lemma ringChoose_neg_one : Ring.choose (-1 : ℤ) N = (-1) ^ N
```

**`PhyslibAlpha.ringChoose_neg_two`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L207).

```lean
lemma ringChoose_neg_two : Ring.choose (-2 : ℤ) N = (-1) ^ N * (N + 1)
```

## C. Integrals

**`PhyslibAlpha.integrableOn_pow_mul_exp_neg`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L220).

```lean
lemma integrableOn_pow_mul_exp_neg (q : ℕ) :
    IntegrableOn (fun x : ℝ => x ^ q * Real.exp (-x)) (Ioi 0)
```

**`PhyslibAlpha.integral_pow_mul_exp_neg`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L228).

> `∫₀^∞ x^q e^(-x) dx = q!`.

```lean
lemma integral_pow_mul_exp_neg (q : ℕ) :
    ∫ x in Ioi (0 : ℝ), x ^ q * Real.exp (-x) = q.factorial
```

**`PhyslibAlpha.integral_pow_mul_exp_neg_mul_laguerre_sq`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L238).

> `∫₀^∞ x^e e^(-x) L(x)² dx = Σ_j c_j Σ_i c_i (e + j + i)!`.

```lean
lemma integral_pow_mul_exp_neg_mul_laguerre_sq (e : ℕ) :
    ∫ x in Ioi (0 : ℝ), x ^ e * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ∑ j ∈ Finset.range (N + 1), laguerreCoeff N α j *
        ∑ i ∈ Finset.range (N + 1), laguerreCoeff N α i * ((e + j + i).factorial : ℝ)
```

**`PhyslibAlpha.integral_pow_mul_exp_neg_mul_laguerre_sq_eq`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L262).

> The integrals through the moments.

```lean
lemma integral_pow_mul_exp_neg_mul_laguerre_sq_eq (e : ℕ) :
    ∫ x in Ioi (0 : ℝ), x ^ e * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ∑ j ∈ Finset.range (N + 1), laguerreCoeff N α j * (((e + j).factorial : ℝ) *
        ((Ring.choose ((N + α : ℤ) - (e + j : ℕ) - 1) N : ℤ) : ℝ))
```

**`PhyslibAlpha.neg_one_pow_mul_self`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L269).

```lean
lemma neg_one_pow_mul_self (n : ℕ) : (-1 : ℝ) ^ n * (-1) ^ n = 1
```

**`PhyslibAlpha.integral_laguerre_sq_alpha`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L273).

> `∫₀^∞ x^α e^(-x) L_N^(α)(x)² dx = (N + α)!/N!`.

```lean
lemma integral_laguerre_sq_alpha :
    ∫ x in Ioi (0 : ℝ), x ^ α * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ((N + α).factorial : ℝ) / N.factorial
```

**`PhyslibAlpha.integral_laguerre_sq_alpha_add_one`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L289).

> `∫₀^∞ x^(α+1) e^(-x) L_N^(α)(x)² dx = (N + α)!/N! · (2N + α + 1)`.

```lean
lemma integral_laguerre_sq_alpha_add_one :
    ∫ x in Ioi (0 : ℝ), x ^ (α + 1) * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ((N + α).factorial : ℝ) / N.factorial * (2 * N + α + 1)
```

**`PhyslibAlpha.integral_laguerre_sq_alpha_sub_one`**, a lemma, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L320).

> `∫₀^∞ x^(α-1) e^(-x) L_N^(α)(x)² dx = (N + α)!/(N! α)`.

```lean
lemma integral_laguerre_sq_alpha_sub_one (hα : 1 ≤ α) :
    ∫ x in Ioi (0 : ℝ), x ^ (α - 1) * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ((N + α).factorial : ℝ) / (N.factorial * α)
```

**`PhyslibAlpha.integral_laguerre_sq_alpha_sub_two`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean#L341).

> `∫₀^∞ x^(α-2) e^(-x) L_N^(α)(x)² dx = (N + α)! (2N + α + 1)/(N! (α - 1) α (α + 1))`.

```lean
lemma integral_laguerre_sq_alpha_sub_two (hα : 2 ≤ α) :
    ∫ x in Ioi (0 : ℝ), x ^ (α - 2) * Real.exp (-x) * ((laguerre N α).eval x) ^ 2 =
      ((N + α).factorial : ℝ) * (2 * N + α + 1) /
        (N.factorial * (((α : ℝ) - 1) * α * (α + 1)))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/SpecialFunctions/Laguerre.lean)
