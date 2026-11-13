---
declaration: theorem
origin: cited
lean: OeisA103311.a_abs_eq_fib
statement: formalized
---

# Fibonacci transform satisfying $|a(n)| = F(n+1)$

> The sequence $a(n)$ satisfies the linear recurrence relation:
>
> $$a(n) = 3a(n-1) - 4a(n-2) + 2a(n-3) - a(n-4)$$
>
> with initial terms $a(0)=0, a(1)=1, a(2)=1, a(3)=0$.
> The sequence takes values in $\mathbb{Z}$.
>
> *References:*
> - [A103311](https://oeis.org/A103311)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/103311.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103311.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA103311.a_abs_eq_fib`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/103311.wip.lean#L218](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/103311.wip.lean#L218).

> Fibonacci transform satisfying $|a(n)| = F(n+1)$.
>
> Conjecture: all elements in absolute value are Fibonacci numbers.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_abs_eq_fib (n : ℕ) : ∃ m : ℕ, Int.natAbs (a n) = Nat.fib m
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103311.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103311.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/103311.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103311.lean)
- [A103311](https://oeis.org/A103311)
