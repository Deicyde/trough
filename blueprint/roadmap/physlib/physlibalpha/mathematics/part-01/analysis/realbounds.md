---
declaration: module
origin: cited
lean: Real.ciSup_add, Real.le_of_forall_nat_le_add, Real.abs_sum_mul_sub_le
statement: formalized
proof: formalized
---

# Elementary real bounds

The module `PhyslibAlpha.Mathematics.Analysis.RealBounds`, [PhyslibAlpha/Mathematics/Analysis/RealBounds.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/RealBounds.lean): 3 declarations, 3 with a docstring.

> Elementary real estimates: suprema of sums, bounds up to `1 / (n + 1)`, and weighted averages.

## i. Overview

> Three elementary estimates for real numbers: suprema of sums over a codirected family, inequalities
> up to `1 / (n + 1)` for every `n`, and averages that put almost all weight on one term.

## ii. Key results

> - `Real.ciSup_add` : suprema add along a family in which any two indices are dominated by a third.
> - `Real.le_of_forall_nat_le_add` : `a ≤ b` if `a ≤ b + 1 / (n + 1)` for every `n`.
> - `Real.abs_sum_mul_sub_le` : an average with weight at least `1 - θ` on one term is within
>   `2 * A * θ` of it, for terms bounded by `A`.

## iv. References

> * None.

## A. Suprema

**`Real.ciSup_add`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/RealBounds.lean#L48).

> Suprema of two bounded families add when any two indices are dominated by a common one.

```lean
lemma ciSup_add {ι : Type*} [Nonempty ι] {f g : ι → ℝ} (hf : BddAbove (Set.range f))
    (hg : BddAbove (Set.range g)) (h : ∀ i j, ∃ k, f i ≤ f k ∧ g j ≤ g k) :
    ⨆ i, (f i + g i) = (⨆ i, f i) + ⨆ i, g i
```

**`Real.le_of_forall_nat_le_add`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/RealBounds.lean#L60).

> A real number that is at most `b + 1 / (n + 1)` for every `n` is at most `b`.

```lean
lemma le_of_forall_nat_le_add {a b : ℝ} (h : ∀ n : ℕ, a ≤ b + 1 / (n + 1)) : a ≤ b
```

## B. Averages

**`Real.abs_sum_mul_sub_le`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/RealBounds.lean#L69).

> An average of numbers bounded by `A`, with weight at least `1 - θ` on the `i`-th number, is
> within `2 * A * θ` of it.

```lean
lemma abs_sum_mul_sub_le {ι : Type*} [Fintype ι] [DecidableEq ι] {q c : ι → ℝ}
    (hq0 : ∀ l, 0 ≤ q l) (hq1 : ∑ l, q l = 1) (i : ι) {θ A : ℝ} (hqi : 1 - θ ≤ q i)
    (hc : ∀ l, |c l| ≤ A) : |∑ l, c l * q l - c i| ≤ 2 * A * θ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Analysis/RealBounds.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Analysis/RealBounds.lean)
