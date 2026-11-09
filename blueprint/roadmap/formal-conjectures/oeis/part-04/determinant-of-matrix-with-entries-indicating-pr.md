---
declaration: theorem
origin: cited
lean: OeisA71524.conjecture1, OeisA71524.conjecture2
statement: formalized
---

# Determinant of matrix with entries indicating primality of $i^2 + j^2$

> The sequence $a(n)$ is the determinant of the $n \times n$ matrix $M$ defined by
> $M(i,j) = 1$ if $i^2 + j^2$ is prime, and $0$ otherwise, where $1 \le i, j \le n$.
>
> *References:*
> - [A071524](https://oeis.org/A071524)

*Quoted from [FormalConjectures/OEIS/71524.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71524.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA71524.conjecture1`

Open: stated without proof.

> Conjecture: $a(n) = 0$ for no $n > 28$.
> - _Zhi-Wei Sun_, Aug 26 2013

```lean
theorem conjecture1 (n : ℕ) (hn : 28 < n) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/71524.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71524.lean#L85).

## `OeisA71524.conjecture2`

Open: stated without proof.

> Conjecture (Generalization): For every $m \in \mathbb{N}$, the determinant `generalDet m n` is
> nonzero for all sufficiently large $n$.
> - _Zhi-Wei Sun_, Aug 26-27 2013

```lean
theorem conjecture2 (m : ℕ) : ∃ N : ℕ, ∀ n : ℕ, N < n → generalDet m n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/OEIS/71524.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71524.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/71524.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/71524.lean)
- [A071524](https://oeis.org/A071524)
