---
declaration: theorem
origin: cited
lean: OeisA262824.conjecture_1, OeisA262824.conjecture_2, OeisA262824.conjecture_3, OeisA262824.conjecture_4, OeisA262824.conjecture_5
statement: formalized
---

# Sums of a square and three weighted cubes

> Number of ordered ways to write $n$ as $w^2 + x^3 + 2y^3 + 3z^3$, where $w, x, y$ and $z$ are
> nonnegative integers.
>
> *References:*
> - [A262824](https://oeis.org/A262824)

*Quoted from [FormalConjectures/OEIS/262824.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `OeisA262824.conjecture_1`

Open: stated without proof.

> Conjecture (i): For any $m \in \{3, 4, 5, 6\}$ and $n \ge 0$, there are nonnegative integers
> $w, x, y, z$ such that $n = w^2 + x^3 + 2y^3 + mz^3$.

```lean
theorem conjecture_1 (m : ℕ) (hm : m ∈ ({3, 4, 5, 6} : Finset ℕ)) (n : ℕ) :
    ∃ w x y z : ℕ, n = w ^ 2 + x ^ 3 + 2 * y ^ 3 + m * z ^ 3
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262824.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean#L65).

## `OeisA262824.conjecture_2`

Open: stated without proof.

> Conjecture (ii): Every nonnegative integer $n$ can be written as $w^2 + x^3 + 2y^3 + z^4$
> for some nonnegative integers $w, x, y, z$.

```lean
theorem conjecture_2 (n : ℕ) :
    ∃ w x y z : ℕ, n = w ^ 2 + x ^ 3 + 2 * y ^ 3 + z ^ 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262824.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean#L74).

## `OeisA262824.conjecture_3`

Open: stated without proof.

> Conjecture (ii): Every nonnegative integer $n$ can be written as $w^2 + x^3 + 2y^3 + 3z^4$
> for some nonnegative integers $w, x, y, z$.

```lean
theorem conjecture_3 (n : ℕ) :
    ∃ w x y z : ℕ, n = w ^ 2 + x ^ 3 + 2 * y ^ 3 + 3 * z ^ 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262824.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean#L83).

## `OeisA262824.conjecture_4`

Open: stated without proof.

> Conjecture (ii): Every nonnegative integer $n$ can be written as $w^2 + x^3 + 2y^3 + 6z^4$
> for some nonnegative integers $w, x, y, z$.

```lean
theorem conjecture_4 (n : ℕ) :
    ∃ w x y z : ℕ, n = w ^ 2 + x ^ 3 + 2 * y ^ 3 + 6 * z ^ 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262824.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean#L92).

## `OeisA262824.conjecture_5`

Open: stated without proof.

> Conjecture (ii): Every nonnegative integer $n$ can be written as $2w^2 + x^3 + 4y^3 + z^4$
> for some nonnegative integers $w, x, y, z$.

```lean
theorem conjecture_5 (n : ℕ) :
    ∃ w x y z : ℕ, n = 2 * w ^ 2 + x ^ 3 + 4 * y ^ 3 + z ^ 4
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/262824.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/262824.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/262824.lean)
- [A262824](https://oeis.org/A262824)
