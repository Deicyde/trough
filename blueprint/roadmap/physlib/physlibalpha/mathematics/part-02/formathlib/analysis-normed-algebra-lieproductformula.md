---
declaration: module
origin: cited
lean: NormedSpace.norm_exp_le_exp_norm, NormedSpace.norm_pow_sub_pow_le, NormedSpace.tendsto_nat_smul_exp_mul_exp_sub_exp, NormedSpace.tendsto_exp_mul_exp_pow
statement: formalized
proof: formalized
---

# The Lie product formula

The module `PhyslibAlpha.Mathematics.ForMathlib.Analysis.Normed.Algebra.LieProductFormula`, [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean): 4 declarations, 4 with a docstring.

> The exponential of a sum as a limit of products of exponentials.

## i. Overview

> In a complete normed algebra over `ℝ` with `‖1‖ = 1`,
> `(exp (X / n) exp (Y / n)) ^ n → exp (X + Y)` as `n → ∞`. This is the Lie product formula,
> known in physics as the Trotter product formula. It is what makes the generators of the
> one-parameter subgroups of a closed group of matrices closed under addition.
>
> The proof compares `a = exp (X / n) exp (Y / n)` with `b = exp ((X + Y) / n)`, whose `n`-th
> power is `exp (X + Y)`. Both have norm at most `M = exp ((‖X‖ + ‖Y‖) / n)`, so telescoping
> gives `‖a ^ n − b ^ n‖ ≤ n M ^ n ‖a − b‖`, with `M ^ n = exp (‖X‖ + ‖Y‖)`. The two curves
> `t ↦ exp (t X) exp (t Y)` and `t ↦ exp (t (X + Y))` agree at `t = 0` together with their
> derivatives, so `‖a − b‖` is small compared with `1 / n`, and `n ‖a − b‖ → 0`.

## ii. Key results

> - `NormedSpace.norm_exp_le_exp_norm` : `‖exp x‖ ≤ exp ‖x‖`.
> - `NormedSpace.norm_pow_sub_pow_le` : `‖a ^ n − b ^ n‖ ≤ n M ^ n ‖a − b‖` when `‖a‖, ‖b‖ ≤ M`
>   and `1 ≤ M`.
> - `NormedSpace.tendsto_exp_mul_exp_pow` : the Lie product formula.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. Norm bounds

**`NormedSpace.norm_exp_le_exp_norm`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean#L64).

> The exponential is bounded by the real exponential of the norm, term by term in the
> exponential series.

```lean
lemma norm_exp_le_exp_norm (x : 𝔸) : ‖exp x‖ ≤ Real.exp ‖x‖
```

**`NormedSpace.norm_pow_sub_pow_le`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean#L75).

> The difference of two `n`-th powers, by telescoping:
> `‖a ^ n − b ^ n‖ ≤ n M ^ n ‖a − b‖` when `‖a‖, ‖b‖ ≤ M` and `1 ≤ M`.

```lean
lemma norm_pow_sub_pow_le {a b : 𝔸} {M : ℝ} (hM : 1 ≤ M) (ha : ‖a‖ ≤ M) (hb : ‖b‖ ≤ M)
    (n : ℕ) : ‖a ^ n - b ^ n‖ ≤ n * M ^ n * ‖a - b‖
```

## B. The Lie product formula

**`NormedSpace.tendsto_nat_smul_exp_mul_exp_sub_exp`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean#L103).

> The curves `t ↦ exp (t X) exp (t Y)` and `t ↦ exp (t (X + Y))` agree to first order at
> `t = 0`: `n (exp (X / n) exp (Y / n) − exp ((X + Y) / n)) → 0`.

```lean
lemma tendsto_nat_smul_exp_mul_exp_sub_exp (X Y : 𝔸) :
    Tendsto (fun n : ℕ => (n : ℝ) • (exp ((n : ℝ)⁻¹ • X) * exp ((n : ℝ)⁻¹ • Y) -
      exp ((n : ℝ)⁻¹ • (X + Y)))) atTop (𝓝 0)
```

**`NormedSpace.tendsto_exp_mul_exp_pow`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean#L120).

> **The Lie product formula**: `(exp (X / n) exp (Y / n)) ^ n → exp (X + Y)`.

```lean
lemma tendsto_exp_mul_exp_pow (X Y : 𝔸) :
    Tendsto (fun n : ℕ => (exp ((n : ℝ)⁻¹ • X) * exp ((n : ℝ)⁻¹ • Y)) ^ n) atTop
      (𝓝 (exp (X + Y)))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/Mathematics/ForMathlib/Analysis/Normed/Algebra/LieProductFormula.lean)
