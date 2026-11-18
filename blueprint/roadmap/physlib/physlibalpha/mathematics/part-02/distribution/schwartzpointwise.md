---
declaration: module
origin: cited
lean: SchwartzMap.norm_le_rpow_neg_mul, SchwartzMap.exists_norm_le_rpow_neg
statement: formalized
proof: formalized
---

# Pointwise polynomial decay of Schwartz functions

The module `PhyslibAlpha.Mathematics.Distribution.SchwartzPointwise`, [PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean): 2 declarations, 2 with a docstring.

> A Schwartz function decays faster than every power of `1 + ‖z‖`.

## i. Overview

> The estimate `‖h z‖ ≤ 2ᵏ⁻¹ (p₀ h + pₖ h) (1 + ‖z‖)⁻ᵏ` follows from the binomial bound
> `(1 + t)ᵏ ≤ 2ᵏ⁻¹ (1 + tᵏ)` and the two seminorms `p₀` and `pₖ`. The constant is a seminorm of
> `h`. So it is uniform on bounded sets of Schwartz functions.

## ii. Key results

> - `SchwartzMap.norm_le_rpow_neg_mul` : the pointwise decay with an explicit constant.
> - `SchwartzMap.exists_norm_le_rpow_neg` : the decay with an unspecified constant.

## iv. References

> None.

## A. Decay

> - `SchwartzMap.norm_le_rpow_neg_mul` : the pointwise decay with an explicit constant.
> - `SchwartzMap.exists_norm_le_rpow_neg` : the decay with an unspecified constant.

**`SchwartzMap.norm_le_rpow_neg_mul`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean#L53).

> **Decay of a Schwartz function with an explicit constant.**

```lean
lemma norm_le_rpow_neg_mul (h : 𝓢(V, F)) (k : ℕ) (z : V) :
    ‖h z‖ ≤ 2 ^ (k - 1) * (SchwartzMap.seminorm 𝕜 0 0 h + SchwartzMap.seminorm 𝕜 k 0 h) *
      (1 + ‖z‖) ^ (-(k : ℝ))
```

**`SchwartzMap.exists_norm_le_rpow_neg`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean#L70).

> A Schwartz function decays like `(1 + ‖z‖)⁻ᵏ` for every `k`. The constant is nonnegative.

```lean
lemma exists_norm_le_rpow_neg (h : 𝓢(V, F)) (k : ℕ) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ z : V, ‖h z‖ ≤ C * (1 + ‖z‖) ^ (-(k : ℝ))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/SchwartzPointwise.lean)
