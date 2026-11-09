---
declaration: theorem
origin: cited
lean: Buchi.buchi_problem, Buchi.buchi_problem_M5
statement: formalized
---

# Büchi's problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/B%C3%BCchi%27s_problem)

*Quoted from [FormalConjectures/Wikipedia/Buchi.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Buchi.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 5 test statements, counted here but not shown.

## `Buchi.buchi_problem`

Open: stated without proof.

> **Büchi's problem**
> There exists a positive integer $M$ such that, for all integers $x$ and $a$,
> if $(x+n)^2 + a$ is a square for $M$ consecutive values of $n$, then $a = 0$.

```lean
theorem buchi_problem :
    ∃ M : ℕ, 1 ≤ M ∧ IsBuchi M
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Buchi.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Buchi.lean#L42).

## `Buchi.buchi_problem_M5`

Open: stated without proof.

> **Büchi's problem (first open case, $M = 5$)**:
> For all integers $x$ and $a$, if $(x+n)^2 + a$ is a perfect square for $n = 0, 1, 2, 3, 4$,
> then $a = 0$.
>
> Non-trivial sequences of length 3 and 4 are known to exist, so $M = 5$ is the first open case.

```lean
theorem buchi_problem_M5 : IsBuchi 5
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Buchi.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Buchi.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Buchi.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Buchi.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/B%C3%BCchi%27s_problem)
