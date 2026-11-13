---
declaration: theorem
origin: cited
lean: OeisA262880.conjecture_1, OeisA262880.conjecture_2
statement: formalized
---

# Sums of a triangular number and three weighted cubes

> Number of ordered ways to write $n$ as $\frac{w(w+1)}{2} + x^3 + y^3 + 2z^3$ with $w > 0$,
> $0 \le x \le y$, and $z \ge 0$.
>
> *References:*
> - [A262880](https://oeis.org/A262880)

*Quoted from [FormalConjectures/OEIS/262880.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262880.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `OeisA262880.conjecture_1`

Open: stated without proof.

> Conjecture (i): Any positive integer can be written as $\frac{w(w+1)}{2} + x^3 + by^3 + cz^3$
> with $w > 0$ and $x, y, z \ge 0$, provided that $(b, c) \in \{(1,2), (1,3), (1,4), (1,6),
> (2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (2,20), (2,21), (2,34), (3,3), (3,4), (3,5),
> (3,6), (4,10)\}$.

```lean
theorem conjecture_1 (p : ℕ × ℕ) (hp : p ∈ pairs1) (n : ℕ) (hn : 0 < n) :
    ∃ w x y z : ℕ, 0 < w ∧ n = Nat.triangular w + x ^ 3 + p.1 * y ^ 3 + p.2 * z ^ 3
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262880.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262880.lean#L74).

## `OeisA262880.conjecture_2`

Open: stated without proof.

> Conjecture (ii): For $(b, c) \in \{(3,4), (3,6), (4,8)\}$, every nonnegative integer $n$ is of
> the form $\frac{w(w+1)}{2} + 2x^3 + by^3 + cz^3$ for some nonnegative integers $w, x, y, z$.

```lean
theorem conjecture_2 (p : ℕ × ℕ) (hp : p ∈ pairs2) (n : ℕ) :
    ∃ w x y z : ℕ, n = Nat.triangular w + 2 * x ^ 3 + p.1 * y ^ 3 + p.2 * z ^ 3
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262880.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262880.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262880.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262880.lean)
- [A262880](https://oeis.org/A262880)
