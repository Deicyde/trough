---
declaration: theorem
origin: cited
lean: OeisA258667.a_is_equivalent_asymptoticTerm
statement: formalized
---

# Asymptotics of an inner sum formula for $a(n)$

> The inner sum of the formula used in a:
>
> $$\sum_{\max(k-n+5, 0) \le j \le \min(k,4)} \binom{8-j}{j}\binom{2n-k+j-10}{k-j}$$
>
> a: A total of $n$ married couples, including a mathematician M and his wife, are to be seated
> at the $2n$ chairs around a circular table, with no man seated next to his wife. After the ladies
> are seated at every other chair, M is the first man allowed to choose one of the remaining chairs.
> The sequence gives the number of ways of seating the other men, with no man seated next to his
> wife, if M chooses the chair that is 9 seats clockwise from his wife's chair.
>
> $$a(n) = \begin{cases} 0 & \text{if } n \le 5 \cr
> \sum_{k=0}^{n-1}(-1)^k(n-k-1)! \sum_{\max(k-n+5, 0) \le j \le \min(k,4)}
> \binom{8-j}{j}\binom{2n-k+j-10}{k-j} & \text{if } n > 5 \end{cases}$$
>
> *References:*
> - [A258667](https://oeis.org/A258667)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/258667.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/258667.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA258667.a_is_equivalent_asymptoticTerm`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/258667.wip.lean#L427](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/258667.wip.lean#L427).

> Conjecture: $a(n) \sim e^{-2} \cdot n! / (n-2)$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_is_equivalent_asymptoticTerm :
    IsEquivalent atTop (fun n : ℕ => (a n : ℝ)) asymptoticTerm
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/258667.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/258667.lean#L140).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/258667.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/258667.lean)
- [A258667](https://oeis.org/A258667)
