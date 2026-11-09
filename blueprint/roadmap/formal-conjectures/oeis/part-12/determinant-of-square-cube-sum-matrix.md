---
declaration: theorem
origin: cited
lean: OeisA228624.conjecture_1, OeisA228624.conjecture_2
statement: formalized
---

# Determinant of square/cube sum matrix

> Determinant of the $n \times n$ matrix with $(i,j)$-entry ($i, j = 1, \dots, n$) equal to $1$ or
> $0$ according as $i + j$ is a square or not.
>
> *References:*
> - [A228624](https://oeis.org/A228624)

*Quoted from [FormalConjectures/OEIS/228624.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228624.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA228624.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n)$ is nonzero for any $n > 21$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 21) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228624.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228624.lean#L71).

## `OeisA228624.conjecture_2`

Open: stated without proof.

> Conjecture: Let $A(n)$ be the $n \times n$ determinant
> with $(i,j)$-entry equal to $1$ or $0$ according as $i + j$ is a cube or not. Then $A(n)$ is
> nonzero for any $n > 176$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (n : ℕ) (hn : n > 176) : b n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228624.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228624.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228624.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228624.lean)
- [A228624](https://oeis.org/A228624)
