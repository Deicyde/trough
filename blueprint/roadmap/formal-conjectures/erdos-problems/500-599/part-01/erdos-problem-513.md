---
declaration: theorem
origin: cited
lean: Erdos513.erdos_513, Erdos513.erdos_513.variants.upper_bound, Erdos513.erdos_513.variants.lower_bound
statement: formalized
---

# Erdős Problem 513

> *Reference:*
>  - [erdosproblems.com/513](https://www.erdosproblems.com/513)
>  - [ClHa64] Clunie, J. and Hayman, W. K., The maximum term of a power series. J. Analyse Math.
>   (1964), 143-186.
>  - [Tao's optimization constant 51a](https://teorth.github.io/optimizationproblems/constants/51a.html)

*Quoted from [FormalConjectures/ErdosProblems/513.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/513.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/513](https://www.erdosproblems.com/513).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos513.erdos_513`

Open: stated without proof.

> Let `f` be a transcendental entire function. What is the greatest possible value of
> `liminf (fun r : ℝ => ratio r f) atTop`?

```lean
theorem erdos_513 : maxTermConstant = erdos_513.answer
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/513.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/513.lean#L53).

## `Erdos513.erdos_513.variants.upper_bound`

Solved: stated here without proof.

> There is `c > 0` such that `maxTermConstant ≤ 2 / π - c`. This is proved in [ClHa64].

```lean
theorem erdos_513.variants.upper_bound : ∃ c > 0, maxTermConstant ≤ 2 / π - c
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/513.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/513.lean#L58).

## `Erdos513.erdos_513.variants.lower_bound`

Solved: stated here without proof.

> `maxTermConstant > 1 / 2`: there is a transcendental entire `f` with
> `liminf (fun r : ℝ => ratio r f) atTop > 1 / 2`. This was observed by Kövári (unpublished), and
> [ClHa64] proves the stronger bound `> 4 / 7`. It does not hold for every `f`: for `f = exp` the
> `liminf` is `0`.

```lean
theorem erdos_513.variants.lower_bound : maxTermConstant > 1 / 2
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/513.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/513.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/513.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/513.lean)
- [erdosproblems.com/513](https://www.erdosproblems.com/513)
