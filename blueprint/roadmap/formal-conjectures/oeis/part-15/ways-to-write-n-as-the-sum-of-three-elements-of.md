---
declaration: theorem
origin: cited
lean: OeisA256544.conjecture
statement: formalized
---

# Ways to write $n$ as the sum of three elements of $\{\lfloor T(x)/3 \rfloor : x \ge 1\}$

> The sequence $a(n)$ counts the number of ways to write $n$ as the sum of three unordered elements
> of the set $\{\lfloor T(x)/3 \rfloor : x = 1, 2, 3, \dots\}$, where $T(x) = \frac{x(x+1)}{2}$ is
> the $x$-th triangular number.
>
> *References:*
> - [A256544](https://oeis.org/A256544)

*Quoted from [FormalConjectures/OEIS/256544.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/256544.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA256544.conjecture`

Open: stated without proof.

> Conjecture: For any positive integer $m$, every nonnegative integer $n$ can be written as
> $\lfloor T(x)/m \rfloor + \lfloor T(y)/m \rfloor + \lfloor T(z)/m \rfloor$ with $x, y, z$
> nonnegative integers.

```lean
theorem conjecture (m : ℕ) (hm : 0 < m) (n : ℕ) :
    ∃ x y z : ℕ, n = Nat.triangular x / m + Nat.triangular y / m + Nat.triangular z / m
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/256544.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/256544.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/256544.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/256544.lean)
- [A256544](https://oeis.org/A256544)
