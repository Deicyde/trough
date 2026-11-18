---
declaration: module
origin: cited
lean: IteratedFDerivBounds.norm_iteratedFDeriv_comp_clm_le, IteratedFDerivBounds.norm_iteratedFDeriv_mul_le_two_pow
statement: formalized
proof: formalized
---

# Bounds on iterated derivatives

The module `PhyslibAlpha.Mathematics.Calculus.IteratedFDerivBounds`, [PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean): 2 declarations, 2 with a docstring.

> Norm bounds for iterated Fréchet derivatives of a composition with a continuous linear map and of
> a product.

## i. Overview

> Composing with a continuous linear map `L` multiplies the `n`th derivative by at most `‖L‖ⁿ`. The
> `k`th derivative of a product of two smooth real functions is bounded by `2ᵏ` times the product of
> bounds of the factors. These estimates control the seminorms of Schwartz functions under linear
> changes of variables and under multiplication with smooth cutoffs.

## ii. Key results

> - `IteratedFDerivBounds.norm_iteratedFDeriv_comp_clm_le` : composition with a linear map.
> - `IteratedFDerivBounds.norm_iteratedFDeriv_mul_le_two_pow` : the Leibniz bound for a product.

## iv. References

> None.

## A. Composition with a linear map

> - `IteratedFDerivBounds.norm_iteratedFDeriv_comp_clm_le` : composition with a linear map.

## B. Products

> - `IteratedFDerivBounds.norm_iteratedFDeriv_mul_le_two_pow` : the Leibniz bound for a product.

**`IteratedFDerivBounds.norm_iteratedFDeriv_comp_clm_le`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean#L59).

> Composing with a continuous linear map costs the operator norm to the order of the
> derivative.

```lean
lemma norm_iteratedFDeriv_comp_clm_le {G : Type*} [NormedAddCommGroup G] [NormedSpace ℝ G]
    {H : Type*} [NormedAddCommGroup H] [NormedSpace ℝ H] (L : G →L[ℝ] E) {f : E → H}
    (hf : ContDiff ℝ ∞ f) (n : ℕ) (y : G) :
    ‖iteratedFDeriv ℝ n (f ∘ L) y‖ ≤ ‖iteratedFDeriv ℝ n f (L y)‖ * ‖L‖ ^ n
```

**`IteratedFDerivBounds.norm_iteratedFDeriv_mul_le_two_pow`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean#L69).

> **The Leibniz bound.** If the derivatives of order up to `k` of `b` and `v` are bounded by `B`
> and `S` at `x` then the `k`th derivative of `b * v` is bounded by `2 ^ k * B * S`.

```lean
lemma norm_iteratedFDeriv_mul_le_two_pow (b v : E → ℝ) (hb : ContDiff ℝ ∞ b)
    (hv : ContDiff ℝ ∞ v) (x : E) (k : ℕ) {B S : ℝ}
    (hB : ∀ i ≤ k, ‖iteratedFDeriv ℝ i b x‖ ≤ B) (hS : ∀ j ≤ k, ‖iteratedFDeriv ℝ j v x‖ ≤ S) :
    ‖iteratedFDeriv ℝ k (fun y => b y * v y) x‖ ≤ 2 ^ k * B * S
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Calculus/IteratedFDerivBounds.lean)
