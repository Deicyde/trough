---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.successProb, UnitalPositiveLinearMap.advantage, UnitalPositiveLinearMap.successProb_eq_add_advantage, UnitalPositiveLinearMap.advantage_le, UnitalPositiveLinearMap.bddAbove_advantage, UnitalPositiveLinearMap.optimalSuccessProb, UnitalPositiveLinearMap.optimalSuccessProb_eq, UnitalPositiveLinearMap.sub_complement_eq_neg_sub
statement: formalized
proof: formalized
---

# State discrimination

The module `Physlib.ProbabilisticTheory.State.Discrimination`, [Physlib/ProbabilisticTheory/State/Discrimination.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean): 14 declarations, 14 with a docstring.

> Optimal binary discrimination probabilities and their relation to the state distance.

## i. Overview

> A system is prepared in state `ω₀` (with probability `p`) or `ω₁` (with probability `1 - p`). We
> get to run a single yes/no test on it — an effect `e` — and have to guess which state it was,
> based only on whether `e` "clicked". We guess `ω₀` on a click and `ω₁` otherwise; `successProb`
> is the probability that guess is right.
>
> Always guessing `ω₁`, without even looking at the system, is already right with probability
> `1 - p` — that's our baseline. Running a test can only add to it: its `advantage` is how much
> extra success probability it buys over that baseline. Taking the supremum over all tests gives the
> classic Helstrom bound (`optimalSuccessProb_eq`), without assuming an optimizing test exists.
>
> For equal priors (`p = 1/2`) the bound simplifies to `1/2 + dist ω₀ ω₁ / 4`.
> Two equally likely states are easier to tell apart exactly when they sit farther apart.

## ii. Key results

> - `UnitalPositiveLinearMap.optimalSuccessProb_eq` : the Helstrom bound.
> - `UnitalPositiveLinearMap.optimalSuccessProb_half_half_eq` : for equal priors, the bound is the
>   state distance.

## iv. References

> - C.W. Helstrom, *Quantum Detection and Estimation Theory*, Academic Press, 1976.

## A. Success probability and the advantage of a test

**`UnitalPositiveLinearMap.successProb`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L64).

> Probability of guessing right between `ω₀` (prior `p`) and `ω₁` (prior `1 - p`) using test
> `e`: guess `ω₀` on a click, `ω₁` otherwise.

```lean
def successProb (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) : ℝ
```

**`UnitalPositiveLinearMap.advantage`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L68).

> How much test `e` improves on the baseline of always guessing `ω₁`.

```lean
def advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) : ℝ
```

**`UnitalPositiveLinearMap.successProb_eq_add_advantage`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L72).

> Success probability equals the baseline `1 - p` plus the advantage of test `e`.

```lean
lemma successProb_eq_add_advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) :
    successProb ω₀ ω₁ p e = (1 - p) + advantage ω₀ ω₁ p e
```

## B. The Helstrom bound

**`UnitalPositiveLinearMap.advantage_le`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L80).

> No test's advantage beats the prior weight `p` of the state it favors.

```lean
lemma advantage_le (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) :
    advantage ω₀ ω₁ p e ≤ p
```

**`UnitalPositiveLinearMap.bddAbove_advantage`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L86).

> Advantages of tests are bounded above.

```lean
lemma bddAbove_advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) :
    BddAbove (Set.range (advantage ω₀ ω₁ p))
```

**`UnitalPositiveLinearMap.optimalSuccessProb`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L91).

> The best a single test can do.

```lean
noncomputable def optimalSuccessProb (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) : ℝ
```

**`UnitalPositiveLinearMap.optimalSuccessProb_eq`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L96).

> The Helstrom bound: optimal success probability is the baseline `1 - p` plus the best
> advantage any test can give.

```lean
lemma optimalSuccessProb_eq (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) :
    optimalSuccessProb ω₀ ω₁ p = (1 - p) + ⨆ e : Effect E, advantage ω₀ ω₁ p e
```

## C. Equal priors: the bound is the state distance

**`UnitalPositiveLinearMap.sub_complement_eq_neg_sub`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L104).

> Complementing an effect negates `ω₀ e - ω₁ e`.

```lean
lemma sub_complement_eq_neg_sub (ω₀ ω₁ : 𝓢[ℝ, E]) (e : Effect E) :
    ω₀ (complement e) - ω₁ (complement e) = -(ω₀ e - ω₁ e)
```

**`UnitalPositiveLinearMap.bddAbove_abs_sub`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L109).

> The differences `|ω₀ e - ω₁ e|` over effects are bounded above.

```lean
lemma bddAbove_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun e : Effect E => |ω₀ e - ω₁ e|)
```

**`UnitalPositiveLinearMap.bddAbove_sub`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L117).

> The differences `ω₀ e - ω₁ e` over effects are bounded above.

```lean
lemma bddAbove_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun e : Effect E => ω₀ e - ω₁ e)
```

**`UnitalPositiveLinearMap.ciSup_sub_eq_ciSup_abs_sub`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L125).

> The supremum of the state-value difference equals that of its absolute value: complementing
> an effect flips the sign.

```lean
lemma ciSup_sub_eq_ciSup_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    (⨆ e : Effect E, (ω₀ e - ω₁ e)) = ⨆ e : Effect E, |ω₀ e - ω₁ e|
```

**`UnitalPositiveLinearMap.dist_eq_ciSup_abs_sub`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L142).

> The state distance is the supremum of the differences on recentered effects.

```lean
lemma dist_eq_ciSup_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    dist ω₀ ω₁ =
      ⨆ e : Effect E, |ω₀ (effectEquiv e) - ω₁ (effectEquiv e)|
```

**`UnitalPositiveLinearMap.dist_eq_two_mul_ciSup_sub`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L148).

> The state distance is twice the largest state-value difference over all effects.

```lean
lemma dist_eq_two_mul_ciSup_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    dist ω₀ ω₁ = 2 * ⨆ e : Effect E, (ω₀ e - ω₁ e)
```

**`UnitalPositiveLinearMap.optimalSuccessProb_half_half_eq`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean#L154).

> For equal priors, the Helstrom bound is `1/2` plus a quarter of the state distance.

```lean
lemma optimalSuccessProb_half_half_eq (ω₀ ω₁ : 𝓢[ℝ, E]) :
    optimalSuccessProb ω₀ ω₁ ⟨1 / 2, by norm_num, by norm_num⟩ = 1 / 2 + dist ω₀ ω₁ / 4
```

## Depends on

- [Complementary effects](../effect/complement.md)
- [The metric space of states](metric.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Discrimination.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Discrimination.lean)
