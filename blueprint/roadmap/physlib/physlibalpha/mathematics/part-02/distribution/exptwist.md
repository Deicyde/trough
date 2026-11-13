---
declaration: module
origin: cited
lean: ExpTwist.twist, ExpTwist.contDiff_twist, ExpTwist.norm_iteratedFDeriv_exp, ExpTwist.norm_iteratedFDeriv_twist_le, ExpTwist.abs_exp_sub_one_le, ExpTwist.abs_twist_sub_one_le, ExpTwist.norm_iteratedFDeriv_twist_sub_one_le, ExpTwist.norm_iteratedFDeriv_twist_mul_sub_le
statement: formalized
proof: formalized
---

# Exponential twists of compactly supported functions

The module `PhyslibAlpha.Mathematics.Distribution.ExpTwist`, [PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean): 8 declarations, 2 with a docstring.

> Multiplying a compactly supported function by `exp (a ℓ x)` moves it by `O (|a|)` in every
> derivative.

## i. Overview

> For a continuous linear functional `ℓ` the twist `x ↦ exp (a ℓ x)` is smooth. Its derivatives of
> order `i` are bounded by `(|a| ‖ℓ‖)^i exp (|a| ‖ℓ‖ ‖x‖)`. The twist minus one is bounded by
> `|a| ‖ℓ‖ ‖x‖ exp (|a| ‖ℓ‖ ‖x‖)`. A Leibniz estimate turns these into a bound for the derivatives
> of `twist * v - v` by `|a|` times a constant and the derivative bounds of `v`.

## ii. Key results

> - `ExpTwist.twist` : the function `x ↦ exp (a ℓ x)`.
> - `ExpTwist.norm_iteratedFDeriv_twist_le` : the derivatives of the twist.
> - `ExpTwist.norm_iteratedFDeriv_twist_mul_sub_le` : the derivatives of `twist * v - v`.

## iv. References

> None.

## A. The twist

> - `ExpTwist.twist` : the function `x ↦ exp (a ℓ x)`.
> - `ExpTwist.norm_iteratedFDeriv_twist_le` : the derivatives of the twist.

## B. The Leibniz estimate

> - `ExpTwist.norm_iteratedFDeriv_twist_mul_sub_le` : the derivatives of `twist * v - v`.

**`ExpTwist.twist`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L61).

> exp (a ℓ x)

```lean
def twist (ℓ : E →L[ℝ] ℝ) (a : ℝ) (x : E) : ℝ
```

**`ExpTwist.contDiff_twist`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L63).

```lean
lemma contDiff_twist (ℓ : E →L[ℝ] ℝ) (a : ℝ) : ContDiff ℝ ∞ (twist ℓ a)
```

**`ExpTwist.norm_iteratedFDeriv_exp`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L66).

```lean
lemma norm_iteratedFDeriv_exp (i : ℕ) (y : ℝ) :
    ‖iteratedFDeriv ℝ i Real.exp y‖ = Real.exp y
```

**`ExpTwist.norm_iteratedFDeriv_twist_le`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L71).

```lean
lemma norm_iteratedFDeriv_twist_le (ℓ : E →L[ℝ] ℝ) (a : ℝ) (i : ℕ) (x : E) :
    ‖iteratedFDeriv ℝ i (twist ℓ a) x‖ ≤ (|a| * ‖ℓ‖) ^ i * Real.exp (|a| * ‖ℓ‖ * ‖x‖)
```

**`ExpTwist.abs_exp_sub_one_le`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L93).

```lean
lemma abs_exp_sub_one_le (y : ℝ) : |Real.exp y - 1| ≤ |y| * Real.exp |y|
```

**`ExpTwist.abs_twist_sub_one_le`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L108).

```lean
lemma abs_twist_sub_one_le (ℓ : E →L[ℝ] ℝ) (a : ℝ) (x : E) :
    |twist ℓ a x - 1| ≤ |a| * ‖ℓ‖ * ‖x‖ * Real.exp (|a| * ‖ℓ‖ * ‖x‖)
```

**`ExpTwist.norm_iteratedFDeriv_twist_sub_one_le`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L119).

```lean
lemma norm_iteratedFDeriv_twist_sub_one_le (ℓ : E →L[ℝ] ℝ) {a R : ℝ} (ha : |a| ≤ 1) {x : E}
    (hx : ‖x‖ ≤ R) (k i : ℕ) (hi : i ≤ k) :
    ‖iteratedFDeriv ℝ i (fun y => twist ℓ a y - 1) x‖ ≤
      |a| * ((1 + R) * (1 + ‖ℓ‖) ^ (k + 1) * Real.exp (‖ℓ‖ * R))
```

**`ExpTwist.norm_iteratedFDeriv_twist_mul_sub_le`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean#L172).

> **The twist moves a compactly supported function by `O(|a|)` in every derivative.**

```lean
lemma norm_iteratedFDeriv_twist_mul_sub_le (ℓ : E →L[ℝ] ℝ) {a R : ℝ} (hR : 0 ≤ R) (ha : |a| ≤ 1)
    (v : E → ℝ) (hv : ContDiff ℝ ∞ v) (hvs : tsupport v ⊆ Metric.closedBall 0 R) (k : ℕ) {S : ℝ}
    (hS : ∀ j ≤ k, ∀ y, ‖iteratedFDeriv ℝ j v y‖ ≤ S) (x : E) :
    ‖iteratedFDeriv ℝ k (fun y => twist ℓ a y * v y - v y) x‖ ≤
      2 ^ k * (|a| * ((1 + R) * (1 + ‖ℓ‖) ^ (k + 1) * Real.exp (‖ℓ‖ * R))) * S
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Bounds on iterated derivatives](../../part-01/calculus/iteratedfderivbounds.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwist.lean)
