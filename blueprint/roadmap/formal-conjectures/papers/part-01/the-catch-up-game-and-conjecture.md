---
declaration: theorem
origin: cited
lean: CatchUp.value_of_even_mul_succ_self_div_two
statement: formalized
---

# The Catch-Up game and conjecture

> The game **Catch-Up** (Isaksen–Ismail–Brams–Nealen, 2015) is a two-player, perfect-information game
> played on a finite nonempty set `S` of positive integers. Each time a player removes a number from
> `S`, that number is added to the player’s score.
>
> **Rules.**
> * The scores start at `0`. Player `p1` starts by removing **exactly one** number from `S`.
> * After the first move, players alternate turns. On a turn, the current player removes **one or more**
>   numbers from `S`, one at a time, and must keep removing numbers until their score becomes
>   **at least** the opponent’s score; before the final pick they must remain **strictly behind**.
> * If the current player cannot catch up (in particular, even taking all remaining numbers would still
>   leave them behind), the game ends immediately: the current player receives all remaining numbers.
>
> When `S` is empty, the player with higher score wins; equal scores give a draw.
>
> In this file we define:
> * `Player` and `Outcome`,
> * the recursive evaluator `value` (optimal play),
> * the conjecture `value_of_even_mul_succ_self_div_two`.
>
> ## Example
> For `S = {1,2,3,4}` one play is: `p1` takes `2`, `p2` takes `1` then `4`, and `p1` takes `3`,
> ending with scores `(5,5)`.
>
> ## References
> A. Isaksen, M. Ismail, S. J. Brams, A. Nealen,
> *Catch-Up: A Game in Which the Lead Alternates,* Game & Puzzle Design 1(2), 38–49 (2015).

*Quoted from [FormalConjectures/Paper/CatchUpConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CatchUpConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `CatchUp.value_of_even_mul_succ_self_div_two`

Open: stated without proof.

> Let $T_N = \sum_{k=1}^{N} k = \frac{N(N+1)}{2}$.
> If $T_N$ is even (equivalently $N \equiv 0 \pmod 4$ or $N \equiv 3 \pmod 4$),
> then under optimal play the game `Catch-Up($\{1, \ldots, N\}$)` ends in a draw.

```lean
theorem value_of_even_mul_succ_self_div_two
    (N : ℕ) (h_even : Even (N * (N + 1) / 2)) :
    value (.Icc 1 N) = .draw
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [91 Game theory, economics, social and behavioral sciences](../../by-subject/part-03/91-game-theory-economics-social-and-behavioral-scie/README.md). Declared in [FormalConjectures/Paper/CatchUpConjecture.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CatchUpConjecture.lean#L182).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/CatchUpConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/CatchUpConjecture.lean)
