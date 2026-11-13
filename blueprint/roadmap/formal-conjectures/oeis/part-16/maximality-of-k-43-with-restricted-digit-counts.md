---
declaration: theorem
origin: cited
lean: OeisA306424.forty_three_is_max
statement: formalized
---

# Maximality of $k = 43$ with restricted digit counts in bases $3 \le b < k$

> Numbers $k$ such that the base $b$ expansion of $k$ for each
> $b = 3..k-1$ never contains more than two distinct digits.
>
> The sequence Numbers $k$ such that the base $b$ expansion of $k$ for each
> $b = 3..k-1$ never contains more than two distinct digits.
>
> *References:*
> - [A306424](https://oeis.org/A306424)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/306424.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306424.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 12 test statements, counted here but not shown.

## `OeisA306424.forty_three_is_max`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/306424.wip.lean#L276](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/306424.wip.lean#L276).

> Conjecture: The sequence is finite, with 43 being the last term.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem forty_three_is_max : Condition 43 ∧ ∀ k : ℕ, 43 < k → ¬Condition k
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/306424.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306424.lean#L198).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/306424.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/306424.lean)
- [A306424](https://oeis.org/A306424)
