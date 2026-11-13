---
declaration: theorem
origin: cited
lean: OeisA282779.periodOfPowerMod_eq
statement: formalized
---

# Period of $p$-th powers modulo $n$

> a: Period of cubes mod $n$.
> The $n$-th term $a(n)$ is the smallest positive integer $T$ such that
> $\forall k \in \mathbb{N}$, $(k+T)^3 \equiv k^3 \pmod n$.
>
> The length of the minimal positive period of the sequence $k^p \pmod n$.
> $a_p(n) = \min \{ T \in \mathbb{N}^+ \mid \forall k \in \mathbb{N}, (k+T)^p \equiv k^p \pmod n \}$.
>
> *References:*
> - [A282779](https://oeis.org/A282779)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/282779.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/282779.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA282779.periodOfPowerMod_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/282779.wip.lean#L104](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/282779.wip.lean#L104).

> Conjecture: let $a_p(n)$ be the length of the period of the sequence $k^p \bmod n$ where $p$ is a prime, then $a_p(n) = n/p$ if $n \equiv 0 \pmod{p^2}$, else $a_p(n) = n$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem periodOfPowerMod_eq (p n : ℕ) (hp : Nat.Prime p) (hn : n > 0) :
    periodOfPowerMod p n = if p ^ 2 ∣ n then n / p else n
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/282779.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/282779.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/282779.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/282779.lean)
- [A282779](https://oeis.org/A282779)
