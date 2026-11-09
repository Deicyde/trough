---
declaration: theorem
origin: cited
lean: OeisA62567.a_three_pow_eq
statement: formalized
---

# Reversible multiples $a(3^n) = 10^{3^{n-2}} - 1$ for powers of $3$

> First multiple of $n$ whose reverse is also divisible by $n$,
> or 0 if no such multiple exists.
>
> *References:*
> - [A062567](https://oeis.org/A062567)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/62567.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/62567.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements and 2 API statements, counted here but not shown.

## `OeisA62567.a_three_pow_eq`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/62567.wip.lean#L324](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/62567.wip.lean#L324).

> The conjecture that $a(3^n) = 10^{3^{n-2}} - 1$ for $n > 1$ was shown to be false for $4 < n < 21$
> by Farideh Firoozbakht, who conjectured that for all $n > 4$, $a(3^n) \neq 10^{3^{n-2}} - 1$.
> This latter conjecture is proved here.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem a_three_pow_eq (n : ℕ) :
    2 ≤ n → (a (3 ^ n) = 10 ^ (3 ^ (n - 2)) - 1 ↔ n = 2 ∨ n = 3 ∨ n = 4)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/62567.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/62567.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/62567.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/62567.lean)
- [A062567](https://oeis.org/A062567)
