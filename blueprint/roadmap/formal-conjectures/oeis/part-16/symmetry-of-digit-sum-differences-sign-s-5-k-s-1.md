---
declaration: theorem
origin: cited
lean: OeisA289411.a_symm
statement: formalized
---

# Symmetry of digit sum differences $\operatorname{sign}(S_5(k) - S_1(k))$

> a: $\mathrm{a}(n) = \sum_{k=0}^n \mathrm{sign}(\mathrm{A007953}(5k) - \mathrm{A007953}(k))$.
> $\mathrm{A007953}(n)$ is the digital sum of $n$ in base 10.
> The sequence is non-negative, so the sum over $\mathbb{Z}$ is converted to $\mathbb{N}$.
>
> *References:*
> - [A289411](https://oeis.org/A289411)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
> - [A007953](https://oeis.org/A007953)

*Quoted from [FormalConjectures/OEIS/289411.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/289411.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA289411.a_symm`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/289411.wip.lean#L167](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/289411.wip.lean#L167).

> Conjecture: For $k \ge 1$, let $m_k = 10^k / 2 - 1$. Then for $i = 0, \ldots, m_k$, we have $a(m_k - i) = a(m_k + i)$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_symm (k : ℕ) (hk : 0 < k) :
    let m_k : ℕ := (10 ^ k) / 2 - 1
    ∀ i : ℕ, i ≤ m_k → a (m_k - i) = a (m_k + i)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/289411.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/289411.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/289411.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/289411.lean)
- [A289411](https://oeis.org/A289411)
