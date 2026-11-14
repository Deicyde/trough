---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.successProb, ProbabilisticTheory.UnitalPositiveLinearMap.advantage, ProbabilisticTheory.UnitalPositiveLinearMap.successProb_eq_add_advantage, ProbabilisticTheory.UnitalPositiveLinearMap.advantage_le, ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_advantage, ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_successProb, ProbabilisticTheory.UnitalPositiveLinearMap.optimalSuccessProb, ProbabilisticTheory.UnitalPositiveLinearMap.optimalSuccessProb_eq
statement: formalized
proof: formalized
---

# State discrimination (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.State.Discrimination`, [PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean): 15 declarations, 11 with a docstring.

> Two-state discrimination by a single effect and the Helstrom bound on the success probability.

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

**`ProbabilisticTheory.UnitalPositiveLinearMap.successProb`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L64).

> Probability of guessing right between `ω₀` (prior `p`) and `ω₁` (prior `1 - p`) using test
> `e`: guess `ω₀` on a click, `ω₁` otherwise.

```lean
def successProb (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.advantage`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L68).

> How much test `e` improves on the baseline of always guessing `ω₁`.

```lean
def advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.successProb_eq_add_advantage`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L72).

> Success probability equals the baseline `1 - p` plus the advantage of test `e`.

```lean
lemma successProb_eq_add_advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) :
    successProb ω₀ ω₁ p e = (1 - (p : ℝ)) + advantage ω₀ ω₁ p e
```

## B. The Helstrom bound

**`ProbabilisticTheory.UnitalPositiveLinearMap.advantage_le`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L82).

> No test's advantage beats the prior weight `p` of the state it favors.

```lean
lemma advantage_le (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) (e : Effect E) :
    advantage ω₀ ω₁ p e ≤ (p : ℝ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_advantage`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L89).

```lean
lemma bddAbove_advantage (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) :
    BddAbove (Set.range (advantage ω₀ ω₁ p))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_successProb`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L93).

```lean
lemma bddAbove_successProb (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) :
    BddAbove (Set.range (successProb ω₀ ω₁ p))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.optimalSuccessProb`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L98).

> The best a single test can do.

```lean
noncomputable def optimalSuccessProb (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.optimalSuccessProb_eq`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L103).

> The Helstrom bound: optimal success probability is the baseline `1 - p` plus the best
> advantage any test can give.

```lean
lemma optimalSuccessProb_eq (ω₀ ω₁ : 𝓢[ℝ, E]) (p : unitInterval) :
    optimalSuccessProb ω₀ ω₁ p = (1 - (p : ℝ)) + ⨆ e : Effect E, advantage ω₀ ω₁ p e
```

## C. Equal priors: the bound is the state distance

**`ProbabilisticTheory.UnitalPositiveLinearMap.sub_complement_eq_neg_sub`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L119).

> Complementing an effect negates `ω₀ e - ω₁ e`.

```lean
lemma sub_complement_eq_neg_sub (ω₀ ω₁ : 𝓢[ℝ, E]) (e : Effect E) :
    ω₀ ((Effect.complement e : E)) - ω₁ ((Effect.complement e : E))
      = -(ω₀ (e : E) - ω₁ (e : E))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_abs_sub`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L125).

```lean
lemma bddAbove_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun e : Effect E => |ω₀ (e : E) - ω₁ (e : E)|)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bddAbove_sub`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L133).

```lean
lemma bddAbove_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun e : Effect E => ω₀ (e : E) - ω₁ (e : E))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.ciSup_sub_eq_ciSup_abs_sub`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L140).

> The supremum of the state-value difference equals that of its absolute value: complementing
> an effect flips the sign.

```lean
lemma ciSup_sub_eq_ciSup_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    (⨆ e : Effect E, (ω₀ (e : E) - ω₁ (e : E))) = ⨆ e : Effect E, |ω₀ (e : E) - ω₁ (e : E)|
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_eq_ciSup_abs_sub`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L155).

> The state distance is the largest `|ω₀ e - ω₁ e|` over unit-ball effects
> (`Effect.effectEquiv`).

```lean
lemma dist_eq_ciSup_abs_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    dist ω₀ ω₁ =
      ⨆ e : Effect E, |ω₀ ((Effect.effectEquiv e : E)) - ω₁ ((Effect.effectEquiv e : E))|
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_eq_two_mul_ciSup_sub`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L170).

> The state distance is twice the largest state-value difference over all effects.

```lean
lemma dist_eq_two_mul_ciSup_sub (ω₀ ω₁ : 𝓢[ℝ, E]) :
    dist ω₀ ω₁ = 2 * ⨆ e : Effect E, (ω₀ (e : E) - ω₁ (e : E))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.optimalSuccessProb_half_half_eq`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean#L178).

> For equal priors, the Helstrom bound is `1/2` plus a quarter of the state distance.

```lean
lemma optimalSuccessProb_half_half_eq (ω₀ ω₁ : 𝓢[ℝ, E]) :
    optimalSuccessProb ω₀ ω₁ ⟨1 / 2, by norm_num, by norm_num⟩ = 1 / 2 + dist ω₀ ω₁ / 4
```

## Depends on

- [Complementary effects](../../../physlib/probabilistictheory/effect/complement.md)
- [The metric space of states (PhyslibAlpha)](metric.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Discrimination.lean)
