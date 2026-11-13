---
declaration: theorem
origin: cited
lean: OeisA113254.a_odd_is_square
statement: formalized
---

# Square odd-indexed terms in the recurrence $a(n) = 8a(n-1) - 8a(n-2) + 8a(n-3) - a(n-4)$

> A113254: Corresponds to $m = 8$ in a family of 4th-order linear recurrence sequences.
>
> The sequence $a(n)$ is defined by the initial conditions $a(0)=-1, a(1)=4, a(2)=176, a(3)=3136$,
> and the linear recurrence relation
> $a(n) = -4 * a (n-1) + 256 * a (n-3) + 4096 * a (n-4)$ for $n \ge 4$.
>
> *References:*
> - [A113254](https://oeis.org/A113254)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/113254.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113254.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA113254.a_odd_is_square`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/113254.wip.lean#L130](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/113254.wip.lean#L130).

> Conjecture: $a(8, 2n+1)$ is a perfect square for all $n$ (see A113249).
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_odd_is_square : ∀ n : ℕ, IsSquare (a (2 * n + 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113254.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113254.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113254.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/113254.lean)
- [A113254](https://oeis.org/A113254)
