---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.successProb, ProbabilisticTheory.State.advantage, ProbabilisticTheory.State.successProb_eq_add_advantage, ProbabilisticTheory.State.advantage_le, ProbabilisticTheory.State.bddAbove_advantage, ProbabilisticTheory.State.optimalSuccessProb, ProbabilisticTheory.State.optimalSuccessProb_eq, ProbabilisticTheory.State.sub_complement_eq_neg_sub
statement: formalized
proof: formalized
---

# State discrimination (Physlib)

The module `Physlib.ProbabilisticTheory.State.Discrimination`, [Physlib/ProbabilisticTheory/State/Discrimination.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean): 14 declarations, 14 with a docstring.

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

> - `ProbabilisticTheory.State.optimalSuccessProb_eq` : the Helstrom bound.
> - `ProbabilisticTheory.State.optimalSuccessProb_half_half_eq` : for equal priors, the bound is the
>   state distance.

## iv. References

> - C.W. Helstrom, *Quantum Detection and Estimation Theory*, Academic Press, 1976.

## A. Success probability and the advantage of a test

**`ProbabilisticTheory.State.successProb`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L62).

> Probability of guessing right between `ω₀` (prior `p`) and `ω₁` (prior `1 - p`) using test
> `e`: guess `ω₀` on a click, `ω₁` otherwise.

```lean
def successProb (ω₀ ω₁ : P.State) (p : unitInterval) (e : P.Effect) : ℝ
```

**`ProbabilisticTheory.State.advantage`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L66).

> How much test `e` improves on the baseline of always guessing `ω₁`.

```lean
def advantage (ω₀ ω₁ : P.State) (p : unitInterval) (e : P.Effect) : ℝ
```

**`ProbabilisticTheory.State.successProb_eq_add_advantage`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L70).

> Success probability equals the baseline `1 - p` plus the advantage of test `e`.

```lean
lemma successProb_eq_add_advantage (ω₀ ω₁ : P.State) (p : unitInterval) (e : P.Effect) :
    successProb ω₀ ω₁ p e = (1 - p) + advantage ω₀ ω₁ p e
```

## B. The Helstrom bound

**`ProbabilisticTheory.State.advantage_le`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L78).

> No test's advantage beats the prior weight `p` of the state it favors.

```lean
lemma advantage_le (ω₀ ω₁ : P.State) (p : unitInterval) (e : P.Effect) :
    advantage ω₀ ω₁ p e ≤ p
```

**`ProbabilisticTheory.State.bddAbove_advantage`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L84).

> Advantages of tests are bounded above.

```lean
lemma bddAbove_advantage (ω₀ ω₁ : P.State) (p : unitInterval) :
    BddAbove (Set.range (advantage ω₀ ω₁ p))
```

**`ProbabilisticTheory.State.optimalSuccessProb`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L89).

> The best a single test can do.

```lean
noncomputable def optimalSuccessProb (ω₀ ω₁ : P.State) (p : unitInterval) : ℝ
```

**`ProbabilisticTheory.State.optimalSuccessProb_eq`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L94).

> The Helstrom bound: optimal success probability is the baseline `1 - p` plus the best
> advantage any test can give.

```lean
lemma optimalSuccessProb_eq (ω₀ ω₁ : P.State) (p : unitInterval) :
    optimalSuccessProb ω₀ ω₁ p = (1 - p) + ⨆ e : P.Effect, advantage ω₀ ω₁ p e
```

## C. Equal priors: the bound is the state distance

**`ProbabilisticTheory.State.sub_complement_eq_neg_sub`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L102).

> Complementing an effect negates `ω₀ e - ω₁ e`.

```lean
lemma sub_complement_eq_neg_sub (ω₀ ω₁ : P.State) (e : P.Effect) :
    ω₀ (complement e) - ω₁ (complement e) = -(ω₀ e - ω₁ e)
```

**`ProbabilisticTheory.State.bddAbove_abs_sub`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L107).

> The differences `|ω₀ e - ω₁ e|` over effects are bounded above.

```lean
lemma bddAbove_abs_sub (ω₀ ω₁ : P.State) :
    BddAbove (Set.range fun e : P.Effect => |ω₀ e - ω₁ e|)
```

**`ProbabilisticTheory.State.bddAbove_sub`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L115).

> The differences `ω₀ e - ω₁ e` over effects are bounded above.

```lean
lemma bddAbove_sub (ω₀ ω₁ : P.State) :
    BddAbove (Set.range fun e : P.Effect => ω₀ e - ω₁ e)
```

**`ProbabilisticTheory.State.ciSup_sub_eq_ciSup_abs_sub`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L123).

> The supremum of the state-value difference equals that of its absolute value: complementing
> an effect flips the sign.

```lean
lemma ciSup_sub_eq_ciSup_abs_sub (ω₀ ω₁ : P.State) :
    (⨆ e : P.Effect, (ω₀ e - ω₁ e)) = ⨆ e : P.Effect, |ω₀ e - ω₁ e|
```

**`ProbabilisticTheory.State.dist_eq_ciSup_abs_sub`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L132).

> The state distance is the supremum of the differences on recentered effects.

```lean
lemma dist_eq_ciSup_abs_sub (ω₀ ω₁ : P.State) :
    dist ω₀ ω₁ =
      ⨆ e : P.Effect, |ω₀ (effectEquiv e) - ω₁ (effectEquiv e)|
```

**`ProbabilisticTheory.State.dist_eq_two_mul_ciSup_sub`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L138).

> The state distance is twice the largest state-value difference over all effects.

```lean
lemma dist_eq_two_mul_ciSup_sub (ω₀ ω₁ : P.State) :
    dist ω₀ ω₁ = 2 * ⨆ e : P.Effect, (ω₀ e - ω₁ e)
```

**`ProbabilisticTheory.State.optimalSuccessProb_half_half_eq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean#L144).

> For equal priors, the Helstrom bound is `1/2` plus a quarter of the state distance.

```lean
lemma optimalSuccessProb_half_half_eq (ω₀ ω₁ : P.State) :
    optimalSuccessProb ω₀ ω₁ ⟨1 / 2, by norm_num, by norm_num⟩ = 1 / 2 + dist ω₀ ω₁ / 4
```

## Depends on

- [Complementary effects (Physlib)](../effect/complement.md)
- [The metric space of states (Physlib)](metric.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Discrimination.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Discrimination.lean)
