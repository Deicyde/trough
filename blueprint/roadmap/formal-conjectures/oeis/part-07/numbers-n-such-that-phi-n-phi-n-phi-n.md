---
declaration: theorem
origin: cited
lean: OeisA108569.conjecture
statement: formalized
---

# Numbers $n$ such that $\phi(n) = \phi(n + \phi(n))$

> *References:*
> - [A108569](https://oeis.org/A108569)

*Quoted from [FormalConjectures/OEIS/108569.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108569.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA108569.conjecture`

Open: stated without proof.

> Conjecture: Except for the first term all terms are even.

```lean
theorem conjecture : ∀ n, 0 < n → Even (a n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/108569.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108569.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/108569.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/108569.lean)
- [A108569](https://oeis.org/A108569)
