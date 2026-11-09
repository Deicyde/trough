---
declaration: theorem
origin: cited
lean: PolyTime.isPolyTime_squareRootSum, PolyTime.isPolyTime_squareRootSumTwoSided
statement: formalized
---

# Polynomial-time computability of comparisons of sums of square roots

> This file formalizes the "Square-root sum problem"
> which asks if one can decide in polynomial time on a Turing machine
> whether the sum of the square roots of a list of naturals
> is at most a cutoff (or alternatively, at most another such sum).
>
> This problem is relevant to questions in computational geometry
> (for example, in determining which of two polygonal paths in Euclidean space is longer).
>
> Wikipedia states the problem for positive integers, an integer threshold, and lists of
> equal length.
> The versions here allow zeros, a natural-number threshold, and lists of any length.
> This slightly more general formulation can be reduced to the fixed length form
> (by removing zeros and introducing copies of $\sqrt{4}$ to the longer list and
> $\sqrt{1} + \sqrt{1}$ to the shorter one).
>
> *References:*
> - [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)
> - [Wikipedia: Square-root sum problem](https://en.wikipedia.org/wiki/Square-root_sum_problem)

*Quoted from [FormalConjectures/Wikipedia/SquareRootSum.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquareRootSum.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `PolyTime.isPolyTime_squareRootSum`

Open: stated without proof.

> **Is the square-root sum problem polynomial time (single sum version)?**
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Square-root_sum_problem)

```lean
theorem isPolyTime_squareRootSum :
    IsPolyTime (Function.uncurry squareRootSum)
```

Category `research open`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/SquareRootSum.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquareRootSum.lean#L65).

## `PolyTime.isPolyTime_squareRootSumTwoSided`

Open: stated without proof.

> **Is the square-root sum problem polynomial time (two sum version)?**
>
> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Square-root_sum_problem)

```lean
theorem isPolyTime_squareRootSumTwoSided :
    IsPolyTime (Function.uncurry squareRootSumTwoSided)
```

Category `research open`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/SquareRootSum.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquareRootSum.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SquareRootSum.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SquareRootSum.lean)
- [Wikipedia: List of unsolved problems in computer science](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_computer_science)
