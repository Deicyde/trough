---
declaration: theorem
origin: cited
lean: OeisA76141.conjecture
statement: formalized
---

# Number of times $n$ occurs as a binary sub-pattern of $n^2$

> The sequence $a(n)$ is the number of times the binary expansion of $n$ appears as a contiguous
> sublist (infix) in the binary expansion of $n^2$.
>
> *References:*
> - [A076141](https://oeis.org/A076141)

*Quoted from [FormalConjectures/OEIS/76141.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/76141.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 6 test statements, counted here but not shown.

## `OeisA76141.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a076141-binary-word/blob/b4e179767fa3041c43e019b559ee77e6737317aa/lean/OeisA76141FC.lean#L1229-L1253](https://github.com/KitaKen1/oeis-a076141-binary-word/blob/b4e179767fa3041c43e019b559ee77e6737317aa/lean/OeisA76141FC.lean#L1229-L1253).

> Is $a(n) \le 1$ for all $n$?

```lean
theorem conjecture (n : ℕ) : a n ≤ 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/76141.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/76141.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/76141.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/76141.lean)
- [A076141](https://oeis.org/A076141)
