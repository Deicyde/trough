---
declaration: theorem
origin: cited
lean: ClassNumberProblem.class_number_problem, ClassNumberProblem.class_number_problem.variants.imaginary
statement: formalized
---

# Class number problem for real quadratic fields

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Class_number_problem)

*Quoted from [FormalConjectures/Wikipedia/ClassNumberProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ClassNumberProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `ClassNumberProblem.class_number_problem`

Open: stated without proof.

> There are infinitely many real quadratic fields `ℚ(√d)` with class number one,
> where `d > 1` is a squarefree integer.

```lean
theorem class_number_problem :
    { d : ℤ | Squarefree d ∧ d > 1 ∧ IsClassNumberOne d }.Infinite
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ClassNumberProblem.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ClassNumberProblem.lean#L41).

## `ClassNumberProblem.class_number_problem.variants.imaginary`

Solved: stated here without proof.

> **Stark–Heegner theorem** : For any squarefree integer `d < 0`, the class number of the imaginary
> quadratic field Q(√d) is one if and only if `d ∈ {-1, -2, -3, -7, -11, -19, -43, -67, -163}`.

```lean
theorem class_number_problem.variants.imaginary :
    { d : ℤ | Squarefree d ∧ d < 0 ∧ IsClassNumberOne d } =
    {-1, -2, -3, -7, -11, -19, -43, -67, -163}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ClassNumberProblem.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ClassNumberProblem.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ClassNumberProblem.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/ClassNumberProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Class_number_problem)
