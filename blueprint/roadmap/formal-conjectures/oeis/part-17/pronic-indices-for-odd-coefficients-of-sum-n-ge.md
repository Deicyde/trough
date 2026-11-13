---
declaration: theorem
origin: cited
lean: OeisA323557.odd_a_implies_pronic
statement: formalized
---

# Pronic indices for odd coefficients of $\sum_{n \ge 0} x^n \frac{(1+x^n)^n}{(1+x^{n+1})^{n+1}}$

> Coefficients of G.f. $\sum_{n\ge 0} x^n \cdot \frac{(1 + x^n)^n}{(1 + x^{n+1})^{n+1}}$.
> The $m$-th term $a(m)$ is the coefficient of $x^m$, which is explicitly given by the sum:
>
> $$ a(m) = \sum_{n=0}^m \sum_{k=0}^n \binom{n}{k} (-1)^j \binom{n+j}{j},$$
>
> where $j = \frac{m - n(k+1)}{n+1}$, and the term is zero unless $j$ is a natural number.
>
> *References:*
> - [A323557](https://oeis.org/A323557)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/323557.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/323557.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA323557.odd_a_implies_pronic`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/323557.wip.lean#L193](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/323557.wip.lean#L193).

> Conjecture: Odd terms occur only at positions $n(n+1)$ for $n \ge 0$ (verified for initial 32600 terms).
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).
>
> This statement is equivalent to `OeisA325046.odd_a_implies_pronic`. The two sequences differ
> only by the sign $(-1)^j$ on each summand, so they agree modulo $2$ and have the same odd
> indices.

```lean
theorem odd_a_implies_pronic (m : ℕ) : Odd (a m) → ∃ n : ℕ, m = n * (n + 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/323557.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/323557.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/323557.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/323557.lean)
- [A323557](https://oeis.org/A323557)
