---
declaration: theorem
origin: cited
lean: OeisA194806.a_div_prime_counting_bounded
statement: formalized
---

# Size of smallest subset of $\{1, 2, \dots, n\}$ with distinct subset sums

> Size of the smallest subset $S$ of $T = \{1,2,3,\dots,n\}$
> such that $S \cdot S$ contains $T$,
> where $S \cdot S$ is the set of all products of elements of $S$.
>
> *References:*
> - [A194806](https://oeis.org/A194806)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/194806.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/194806.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA194806.a_div_prime_counting_bounded`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/194806.wip.lean#L472](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/194806.wip.lean#L472).

> Is $a(n) / \pi(n)$ bounded as $n \to \infty$? - _Robert Israel_, Jan 09 2017
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_div_prime_counting_bounded : ∃ C : ℝ,
    ∀ n : ℕ, 2 ≤ n → (a n : ℝ) / (Nat.primeCounting n : ℝ) ≤ C
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/194806.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/194806.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/194806.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/194806.lean)
- [A194806](https://oeis.org/A194806)
