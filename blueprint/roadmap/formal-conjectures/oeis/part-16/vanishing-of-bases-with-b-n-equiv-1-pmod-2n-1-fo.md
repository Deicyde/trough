---
declaration: theorem
origin: cited
lean: OeisA307865.a_eq_zero_of_pseudoprime
statement: formalized
---

# Vanishing of bases with $b^n \equiv -1 \pmod{2n+1}$ for absolute Euler pseudoprimes

> $a(n)$ is the number of natural bases $b < 2n+1$ such that $b^n \equiv -1 \pmod{2n+1}$.
>
> If $2n+1$ is an absolute Euler pseudoprime, then $a(n) = 0$.
>
> *References:*
> - [A307865](https://oeis.org/A307865)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/307865.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/307865.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA307865.a_eq_zero_of_pseudoprime`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/307865.wip.lean#L190](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/307865.wip.lean#L190).

> Conjecture: if $2n+1$ is an absolute Euler pseudoprime, then $a(n) = 0$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_eq_zero_of_pseudoprime (h : IsAbsoluteEulerPseudoprime (2 * n + 1)) : a n = 0
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/307865.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/307865.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/307865.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/307865.lean)
- [A307865](https://oeis.org/A307865)
