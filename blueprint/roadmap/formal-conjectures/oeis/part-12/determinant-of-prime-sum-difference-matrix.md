---
declaration: theorem
origin: cited
lean: OeisA228623.conjecture
statement: formalized
---

# Determinant of prime sum/difference matrix

> Determinant of the $n \times n$ matrix with $(i,j)$-entry ($i, j = 0, \dots, n - 1$) equal to $1$
> or $0$ according as $n + i - j$ and $n - i + j$ are both prime or not.
>
> *References:*
> - [A228623](https://oeis.org/A228623)

*Quoted from [FormalConjectures/OEIS/228623.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228623.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA228623.conjecture`

Open: stated without proof.

> Conjecture: $a(n)$ is nonzero if $n$ is odd and greater than $120$.

```lean
theorem conjecture (n : ℕ) (hn : n > 120) (hodd : Odd n) : a n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228623.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228623.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228623.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228623.lean)
- [A228623](https://oeis.org/A228623)
