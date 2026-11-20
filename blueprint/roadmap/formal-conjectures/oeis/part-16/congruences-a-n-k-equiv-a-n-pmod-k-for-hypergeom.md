---
declaration: theorem
origin: cited
lean: OeisA278070.a_modeq
statement: formalized
---

# Congruences $a(n+k) \equiv a(n) \pmod k$ for hypergeometric values ${}_2F_1(n, -n; ; -1)$

> a: $a(n) = \text{hypergeometric}([n, -n], [], -1)$.
> This is equivalent to the combinatorial sum:
>
> $$a(n) = \sum_{k=0}^n \binom{n}{k} \binom{n+k-1}{k} k!$$
>
> The expression uses $\mathbb{N}$ arithmetic throughout, safely handling
> the subtraction via `Nat.pred`.
>
> *References:*
> - [A278070](https://oeis.org/A278070)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/278070.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/278070.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA278070.a_modeq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/278070.wip.lean#L68](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/278070.wip.lean#L68).

> Conjecture: $a(n+k) \equiv a(n) \pmod{k}$ for all $n$ and $k$. - _Peter Bala_, Mar 12 2023
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_modeq : ∀ (n k : ℕ), Nat.ModEq k (a (n + k)) (a n)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/278070.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/278070.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/278070.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/OEIS/278070.lean)
- [A278070](https://oeis.org/A278070)
