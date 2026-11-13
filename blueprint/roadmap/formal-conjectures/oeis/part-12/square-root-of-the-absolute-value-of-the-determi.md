---
declaration: theorem
origin: cited
lean: OeisA228552.conjecture
statement: formalized
---

# Square root of the absolute value of the determinant of the prime sum indicator matrix

> Square root of the absolute value of $\det(M_n)$, where $M_n$ is the $n \times n$ matrix with
> $(i,j)$-entry ($1 \le i, j \le n$) equal to $1$ if $i + j$ is prime, and $0$ otherwise.
>
> *References:*
> - [A228552](https://oeis.org/A228552)

*Quoted from [FormalConjectures/OEIS/228552.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228552.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 6 test statements, counted here but not shown.

## `OeisA228552.conjecture`

Open: stated without proof.

> We conjecture that $a(n) > 0$ for all $n > 15$.

```lean
theorem conjecture (n : ℕ) (hn : n > 15) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228552.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228552.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228552.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/228552.lean)
- [A228552](https://oeis.org/A228552)
