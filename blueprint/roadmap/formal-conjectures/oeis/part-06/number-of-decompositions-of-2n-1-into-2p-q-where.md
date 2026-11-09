---
declaration: theorem
origin: cited
lean: OeisA103151.conjecture
statement: formalized
---

# Number of decompositions of $2n+1$ into $2p+q$, where $p$ and $q$ are both odd primes

> *References:*
> - [A103151](https://oeis.org/A103151)

*Quoted from [FormalConjectures/OEIS/103151.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103151.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA103151.conjecture`

Open: stated without proof.

> Conjecture: all items for $n \ge 4$ are greater than or equal to $1$. This is a stronger
> conjecture than the Goldbach conjecture.

```lean
theorem conjecture (n : ℕ) (hn : n ≥ 4) : a n ≥ 1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103151.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103151.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/103151.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/103151.lean)
- [A103151](https://oeis.org/A103151)
