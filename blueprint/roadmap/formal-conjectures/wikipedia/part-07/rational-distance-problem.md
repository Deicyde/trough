---
declaration: theorem
origin: cited
lean: RationalDistanceProblem.rational_distance_problem
statement: formalized
---

# Rational distance problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Unit_square#Rational_distance_problem)
> - [mathoverflow/418260](https://mathoverflow.net/questions/418260/)
> asked by user [Yuan Yang](https://mathoverflow.net/users/177957/yuan-yang)
> - D19 in [Unsolved Problems in Number Theory](https://doi.org/10.1007/978-0-387-26677-0)
> by *Richard K. Guy*

*Quoted from [FormalConjectures/Wikipedia/RationalDistanceProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RationalDistanceProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `RationalDistanceProblem.rational_distance_problem`

Open: stated without proof.

> Does there exist a point in the plane at rational distance from all four vertices of the unit square?

```lean
theorem rational_distance_problem :
    ∃ P : ℝ² , ∀ i, ¬ Irrational (dist P (UnitSquareCorners i))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [51 Geometry](../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/Wikipedia/RationalDistanceProblem.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RationalDistanceProblem.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/RationalDistanceProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/RationalDistanceProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Unit_square#Rational_distance_problem)
