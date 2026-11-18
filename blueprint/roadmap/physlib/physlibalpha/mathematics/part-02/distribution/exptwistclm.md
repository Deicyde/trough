---
declaration: module
origin: cited
lean: ExpTwist.twistCLM, ExpTwist.twistCLM_apply, ExpTwist.iterDerivCLM, ExpTwist.iterDerivCLM_apply, ExpTwist.norm_iteratedFDeriv_le_iterDerivCLM, ExpTwist.norm_iterDerivCLM_le, ExpTwist.twistConst, ExpTwist.dnorm_twistCLM_sub_le
statement: formalized
proof: formalized
---

# Exponential twists on test functions

The module `PhyslibAlpha.Mathematics.Distribution.ExpTwistCLM`, [PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean): 17 declarations, 6 with a docstring.

> Conjugating a continuous linear operator on test functions by the exponential twist moves its
> values by `O (|a|)` in every derivative.

## i. Overview

> The twist `x ↦ exp (a ℓ x)` multiplies a test function. The derivatives of a test function are
> bounded continuous functions, and `iterDerivCLM` makes them a continuous linear map. A
> distribution of finite order is bounded on a fixed compact set by finitely many of these norms.
> Together with the estimates for the twist this gives the convergence
> `T (M_a C M_{-a} φ) → T (C φ)` for a continuous linear `C` with values in a fixed ball.

## ii. Key results

> - `ExpTwist.twistCLM` : the multiplication by the twist as a map of test functions.
> - `ExpTwist.iterDerivCLM` : the `k`-th derivative as a continuous linear map to bounded functions.
> - `ExpTwist.tendsto_twistCLM` : the twisted test function tends to the test function.
> - `ExpTwist.exists_bound_of_tsupport_subset` : a distribution has finite order on a compact set.
> - `ExpTwist.tendsto_distribution_twist` : the conjugation limit.

## iv. References

> None.

## A. Test functions and their derivatives

> - `ExpTwist.twistCLM` : the multiplication by the twist.
> - `ExpTwist.iterDerivCLM` : the `k`-th derivative as a continuous linear map.

## B. Estimates for the twist

> - `ExpTwist.dnorm_twistCLM_sub_le` : the derivatives of `M_a φ - φ`.
> - `ExpTwist.tendsto_twistCLM` : convergence in the test function topology.
> - `ExpTwist.exists_bound_of_tsupport_subset` : finite order on a compact set.

## C. The conjugation limit

> - `ExpTwist.tendsto_distribution_twist` : the conjugation limit.

**`ExpTwist.twistCLM`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L72).

> Multiplication of a test function by the twist.

```lean
def twistCLM (a : ℝ) : 𝓓((⊤ : Opens E), ℝ) →L[ℝ] 𝓓((⊤ : Opens E), ℝ)
```

**`ExpTwist.twistCLM_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L75).

```lean
lemma twistCLM_apply (a : ℝ) (φ : 𝓓((⊤ : Opens E), ℝ)) (x : E) :
    twistCLM ℓ a φ x = φ x * twist ℓ a x
```

**`ExpTwist.iterDerivCLM`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L80).

> The `k`-th derivative of a test function as a bounded continuous function.

```lean
def iterDerivCLM (k : ℕ) : 𝓓((⊤ : Opens E), ℝ) →L[ℝ] (E →ᵇ (E [×k]→L[ℝ] ℝ))
```

**`ExpTwist.iterDerivCLM_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L97).

```lean
lemma iterDerivCLM_apply (k : ℕ) (φ : 𝓓((⊤ : Opens E), ℝ)) (x : E) :
    iterDerivCLM E k φ x = iteratedFDeriv ℝ k φ x
```

**`ExpTwist.norm_iteratedFDeriv_le_iterDerivCLM`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L102).

```lean
lemma norm_iteratedFDeriv_le_iterDerivCLM (k : ℕ) (φ : 𝓓((⊤ : Opens E), ℝ)) (x : E) :
    ‖iteratedFDeriv ℝ k φ x‖ ≤ ‖iterDerivCLM E k φ‖
```

**`ExpTwist.norm_iterDerivCLM_le`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L107).

```lean
lemma norm_iterDerivCLM_le (k : ℕ) (φ : 𝓓((⊤ : Opens E), ℝ)) {C : ℝ} (hC : 0 ≤ C)
    (h : ∀ x, ‖iteratedFDeriv ℝ k φ x‖ ≤ C) : ‖iterDerivCLM E k φ‖ ≤ C
```

**`ExpTwist.twistConst`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L115).

> The constant in the twist estimate.

```lean
def twistConst (R : ℝ) (k : ℕ) : ℝ
```

**`ExpTwist.dnorm_twistCLM_sub_le`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L118).

```lean
lemma dnorm_twistCLM_sub_le {a R : ℝ} (hR : 0 ≤ R) (ha : |a| ≤ 1) (φ : 𝓓((⊤ : Opens E), ℝ))
    (hs : tsupport φ ⊆ Metric.closedBall 0 R) (k : ℕ) :
    ‖iterDerivCLM E k (twistCLM ℓ a φ - φ)‖ ≤
      |a| * twistConst ℓ R k * ∑ j ∈ Finset.range (k + 1), ‖iterDerivCLM E j φ‖
```

**`ExpTwist.tendsto_twistCLM`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L141).

```lean
lemma tendsto_twistCLM (φ : 𝓓((⊤ : Opens E), ℝ)) :
    Filter.Tendsto (fun a : ℝ => twistCLM ℓ a φ) (nhds 0) (nhds φ)
```

**`ExpTwist.exists_bound_of_tsupport_subset`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L191).

> **Finite order.** A distribution is bounded on test functions supported in a compact set by
> finitely many sup norms of derivatives.

```lean
lemma exists_bound_of_tsupport_subset (T : 𝓓((⊤ : Opens E), ℝ) →L[ℝ] ℝ) (K : Compacts E) :
    ∃ (N : ℕ) (c : ℝ), 0 ≤ c ∧ ∀ w : 𝓓((⊤ : Opens E), ℝ), tsupport w ⊆ K →
      |T w| ≤ c * ∑ k ∈ Finset.range (N + 1), ‖iterDerivCLM E k w‖
```

**`ExpTwist.dsum`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L223).

> The sum of the sup norms of the derivatives up to the order `N`.

```lean
def dsum (N : ℕ) (w : 𝓓((⊤ : Opens E), ℝ)) : ℝ
```

**`ExpTwist.dsum_nonneg`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L226).

```lean
lemma dsum_nonneg (N : ℕ) (w : 𝓓((⊤ : Opens E), ℝ)) : 0 ≤ dsum E N w
```

**`ExpTwist.dsum_add_le`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L229).

```lean
lemma dsum_add_le (N : ℕ) (v w : 𝓓((⊤ : Opens E), ℝ)) :
    dsum E N (v + w) ≤ dsum E N v + dsum E N w
```

**`ExpTwist.dsum_neg`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L237).

```lean
lemma dsum_neg (N : ℕ) (w : 𝓓((⊤ : Opens E), ℝ)) : dsum E N (-w) = dsum E N w
```

**`ExpTwist.dsum_twistCLM_sub_le`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L243).

```lean
lemma dsum_twistCLM_sub_le {a R : ℝ} (hR : 0 ≤ R) (ha : |a| ≤ 1) (N : ℕ)
    (φ : 𝓓((⊤ : Opens E), ℝ)) (hs : tsupport φ ⊆ Metric.closedBall 0 R) :
    dsum E N (twistCLM ℓ a φ - φ) ≤
      |a| * (∑ k ∈ Finset.range (N + 1), twistConst ℓ R k) * dsum E N φ
```

**`ExpTwist.tsupport_twistCLM_subset`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L261).

```lean
lemma tsupport_twistCLM_subset (a : ℝ) (g : 𝓓((⊤ : Opens E), ℝ)) :
    tsupport ⇑(twistCLM ℓ a g) ⊆ tsupport g
```

**`ExpTwist.tendsto_distribution_twist`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean#L267).

> **Conjugation by the twist.** For a continuous linear `C` with values supported in a ball and
> a distribution `T`, the twisted values `T (M_a C M_{-a} φ)` converge to `T (C φ)`.

```lean
lemma tendsto_distribution_twist [ProperSpace E] (T : 𝓓((⊤ : Opens E), ℝ) →L[ℝ] ℝ)
    (C : 𝓓((⊤ : Opens E), ℝ) →L[ℝ] 𝓓((⊤ : Opens E), ℝ)) (φ : 𝓓((⊤ : Opens E), ℝ)) {R : ℝ}
    (hR : 0 ≤ R) (hC : ∀ g, tsupport ⇑(C g) ⊆ Metric.closedBall 0 R) :
    Filter.Tendsto (fun a : ℝ => T (twistCLM ℓ a (C (twistCLM ℓ (-a) φ)))) (nhds 0)
      (nhds (T (C φ)))
```

## Depends on

- [Exponential twists of compactly supported functions](exptwist.md)

## Sources

- [PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Distribution/ExpTwistCLM.lean)
