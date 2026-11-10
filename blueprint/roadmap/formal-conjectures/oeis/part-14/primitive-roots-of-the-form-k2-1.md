---
declaration: theorem
origin: cited
lean: OeisA239957.conjecture
statement: formalized
---

# Primitive roots of the form k² + 1

> Every prime $p$ has a primitive root $0 < g < p$ of the form $k^2 + 1$, where $k$ is an integer.
>
> Zhi-Wei Sun has offered a prize of RMB 2,000 for the first proof.
>
> *References:*
> - [A239957](https://oeis.org/A239957)
> - Z.-W. Sun, "New observations on primitive roots modulo primes," arXiv:1405.0290 [math.NT], 2014.

*Quoted from [FormalConjectures/OEIS/239957.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/239957.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `OeisA239957.conjecture`

Open: stated without proof.

> **Zhi-Wei Sun's Conjecture (A239957)**: Every prime $p$ has a primitive root $0 < g < p$ of the
> form $k^2 + 1$, where $k$ is an integer.

```lean
theorem conjecture (p : ℕ) (hp : p.Prime) : A p
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/239957.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/239957.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/239957.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/239957.lean)
- [A239957](https://oeis.org/A239957)
