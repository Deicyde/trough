---
declaration: theorem
origin: cited
lean: Arxiv.«1701.08900».second_moment, Arxiv.«1701.08900».second_moment_one_extra_worker
statement: formalized
---

# Pittel's second-moment conjecture for nearly balanced markets

> *Reference:* B. Pittel, [On Likely Solutions of the Stable Matching Problem with Unequal Numbers
> of Men and Women](https://arxiv.org/abs/1701.08900) (2017), unnumbered conjecture on
> [page 7](https://arxiv.org/pdf/1701.08900#page=7), following Theorem 1.3.
>
> There are $n$ firms and $n+d_n$ workers with complete independent uniform strict preferences.
> Every partner is preferable to being unmatched.

*Quoted from [FormalConjectures/Arxiv/1701.08900/SecondMoment.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1701.08900/SecondMoment.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `Arxiv.«1701.08900».second_moment`

Open: stated without proof.

> Pittel conjectures that if $d_n \ge 1$ and $d_n/n \to 0$, then the second moment of the number
> $S_n$ of stable matchings is $O((\mathbb{E}[S_n])^2)$. The bound may depend on the sequence $d_n$.

```lean
theorem second_moment (d : ℕ → ℕ) (hd : ∀ n, 1 ≤ d n)
    (hd_limit : Tendsto (fun n ↦ (d n : ℝ) / n) atTop (𝓝 0)) :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop,
      secondMomentNumStableMatchings n (n + d n) ≤
        C * (expectedNumStableMatchings n (n + d n)) ^ 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Arxiv/1701.08900/SecondMoment.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1701.08900/SecondMoment.lean#L45).

## `Arxiv.«1701.08900».second_moment_one_extra_worker`

Open: stated without proof.

> Pittel's second-moment conjecture for a market with exactly one more worker than firm.

```lean
theorem second_moment_one_extra_worker :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop,
      secondMomentNumStableMatchings n (n + 1) ≤
        C * (expectedNumStableMatchings n (n + 1)) ^ 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Arxiv/1701.08900/SecondMoment.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1701.08900/SecondMoment.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1701.08900/SecondMoment.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1701.08900/SecondMoment.lean)
- [On Likely Solutions of the Stable Matching Problem with Unequal Numbers
of Men and Women](https://arxiv.org/abs/1701.08900)
