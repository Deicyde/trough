---
declaration: theorem
origin: cited
lean: OeisA262813.conjecture_1, OeisA262813.conjecture_2
statement: formalized
---

# Sums of a cube, a square, and a positive triangular number

> Number of ordered ways to write $n$ as $x^3 + y^2 + \frac{z(z+1)}{2}$ with $x \ge 0$, $y \ge 0$,
> and $z > 0$.
>
> *References:*
> - [A262813](https://oeis.org/A262813)

*Quoted from [FormalConjectures/OEIS/262813.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262813.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA262813.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 0$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262813.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262813.lean#L67).

## `OeisA262813.conjecture_2`

Open: stated without proof.

> Conjecture: $a(n) = 1$ only for $n = 1, 9, 21, 35, 98, 152, 306$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 0 < n) :
    a n = 1 ↔ n ∈ singletons
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262813.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262813.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262813.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262813.lean)
- [A262813](https://oeis.org/A262813)
