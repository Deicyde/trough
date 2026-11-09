---
declaration: theorem
origin: cited
lean: OeisA113010.conjecture
statement: formalized
---

# Number of digits of n raised to the power of the sum of the digits of n

> *References:*
> - [A113010](https://oeis.org/A113010)

*Quoted from [FormalConjectures/OEIS/113010.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113010.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA113010.conjecture`

Open: stated without proof.

> $n=1$ and $32$ are two fixed points. Are there any others?

```lean
theorem conjecture : ∃ n : ℕ, a n = n ∧ n ≠ 1 ∧ n ≠ 32
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/113010.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113010.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/113010.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/113010.lean)
- [A113010](https://oeis.org/A113010)
