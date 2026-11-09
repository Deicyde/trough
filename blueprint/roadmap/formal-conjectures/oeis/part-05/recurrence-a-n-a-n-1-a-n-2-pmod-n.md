---
declaration: theorem
origin: cited
lean: OeisA96535.conjecture
statement: formalized
---

# Recurrence $a(n) = (a(n-1) + a(n-2)) \pmod n$

> $a(0) = a(1) = 1$; $a(n) = (a(n-1) + a(n-2)) \pmod n$.
>
> *References:*
> - [A096535](https://oeis.org/A096535)

*Quoted from [FormalConjectures/OEIS/96535.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/96535.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA96535.conjecture`

Open: stated without proof.

> All numbers appear infinitely often, i.e., for every number $k \ge 0$ and every frequency $f > 0$
> there is an index $i$ such that $a(i) = k$ is the $f$-th occurrence of $k$ in the sequence.
> - _Klaus Brockhaus_, Aug 29 2006

```lean
theorem conjecture (k : ℕ) (N : ℕ) : ∃ i : ℕ, i > N ∧ a i = k
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/96535.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/96535.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/96535.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/96535.lean)
- [A096535](https://oeis.org/A096535)
