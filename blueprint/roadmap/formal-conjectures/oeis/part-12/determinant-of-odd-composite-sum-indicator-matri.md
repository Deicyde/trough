---
declaration: theorem
origin: cited
lean: OeisA228591.conjecture
statement: formalized
---

# Determinant of odd composite sum indicator matrix

> Determinant of the $n \times n$ $(0,1)$-matrix with $(i,j)$-entry ($1 \le i, j \le n$) equal to $1$
> if and only if $i + j$ is $2$ or an odd composite number.
>
> *References:*
> - [A228591](https://oeis.org/A228591)

*Quoted from [FormalConjectures/OEIS/228591.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228591.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA228591.conjecture`

Open: stated without proof.

> Conjecture: $a(n) = 0$ for no $n > 15$.

```lean
theorem conjecture (n : ℕ) (hn : n > 15) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228591.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228591.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228591.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228591.lean)
- [A228591](https://oeis.org/A228591)
