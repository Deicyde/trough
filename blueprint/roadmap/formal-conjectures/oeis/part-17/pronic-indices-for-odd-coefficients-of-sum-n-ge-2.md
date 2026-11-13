---
declaration: theorem
origin: cited
lean: OeisA325046.odd_a_implies_pronic
statement: formalized
---

# Pronic indices for odd coefficients of $\sum_{n \ge 0} x^n \frac{(1+x^n)^n}{(1-x^{n+1})^{n+1}}$

> Coefficients of G.f. $\sum_{n \ge 0} x^n \cdot \frac{(1 + x^n)^n}{(1 - x^{n+1})^{n+1}}$.
>
> The term $a(N)$ is the coefficient of $x^N$ in the generating function.
> Expanding the terms, we get a formula for $a(N)$:
>
> $$a(N) = \sum_{n=0}^N \sum_{k=0}^n \mathbf{1}_{n + nk + (n+1)j = N} \binom{n}{k} \binom{n+j}{j}$$
>
> where $j = \frac{N - n(k+1)}{n+1}$.
>
> *References:*
> - [A325046](https://oeis.org/A325046)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/325046.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/325046.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA325046.odd_a_implies_pronic`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/325046.wip.lean#L166](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/325046.wip.lean#L166).

> Conjecture: Odd terms occur only at positions $n(n+1)$ for $n \ge 0$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).
>
> This statement is equivalent to `OeisA323557.odd_a_implies_pronic`. The two sequences differ
> only by the sign $(-1)^j$ on each summand, so they agree modulo $2$ and have the same odd
> indices.

```lean
theorem odd_a_implies_pronic (N : ℕ) : a N % 2 = 1 → ∃ k : ℕ, N = k * (k + 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/325046.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/325046.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/325046.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/325046.lean)
- [A325046](https://oeis.org/A325046)
