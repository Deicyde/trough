---
declaration: theorem
origin: cited
lean: OeisA40.conjecture
statement: formalized
---

# The prime numbers

> The $n$-th prime number $p_n$, where $p_1 = 2$.
>
> *References:*
> - [A000040](https://oeis.org/A000040)

*Quoted from [FormalConjectures/OEIS/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/40.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA40.conjecture`

Open: stated without proof.

> **Conjecture from Thomas Ordowski (2023)**:
> $\log \log a(n+1) - \log \log a(n) < 1/n$ for $n > 0$.

```lean
theorem conjecture (n : ℕ) (hn : 0 < n) :
    Real.log (Real.log (a (n + 1) : ℝ)) - Real.log (Real.log (a n : ℝ)) < 1 / (n : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/40.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/40.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/40.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/40.lean)
- [A000040](https://oeis.org/A000040)
