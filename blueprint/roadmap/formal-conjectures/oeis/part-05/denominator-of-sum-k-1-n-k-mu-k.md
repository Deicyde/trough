---
declaration: theorem
origin: cited
lean: OeisA80326.conjecture
statement: formalized
---

# Denominator of $\sum_{k=1}^n k^{\mu(k)}$

> The sequence $a(n)$ is the denominator of $\sum_{k=1}^n k^{\mu(k)}$, where $\mu$ is the
> Möbius function.
>
> *References:*
> - [A080326](https://oeis.org/A080326)

*Quoted from [FormalConjectures/OEIS/80326.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/80326.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA80326.conjecture`

Open: stated without proof.

> Conjecture: $a(n) = \text{primorial}(n)$ for infinitely many $n$.

```lean
theorem conjecture : {n : ℕ | a n = primorial n}.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/80326.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/80326.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/80326.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/80326.lean)
- [A080326](https://oeis.org/A080326)
