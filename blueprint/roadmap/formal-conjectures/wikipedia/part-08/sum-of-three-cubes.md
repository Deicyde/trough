---
declaration: theorem
origin: cited
lean: SumOfThreeCubes.isSumOfThreeCubesRat_any, SumOfThreeCubes.isSumOfThreeCubes_iff_mod_9
statement: formalized
---

# Sum of three cubes

> An integer `n : ℤ` can be written as a sum of three cubes (of integers) if and only if
> `n` is not `4` or `5` mod `9`.
>
> *References:*
>  - [Wikipedia](https://en.wikipedia.org/wiki/Sums_of_three_cubes)
>  - [mathoverflow/100324](https://mathoverflow.net/a/100324)
> asked by user [*David Feldman*](https://mathoverflow.net/users/10909/david-feldman)

*Quoted from [FormalConjectures/Wikipedia/SumOfThreeCubes.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SumOfThreeCubes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 4 test statements, counted here but not shown.

## `SumOfThreeCubes.isSumOfThreeCubesRat_any`

Proved here.

> Any rational number is a sum of three rational cubes.
>
> First proved by Ryley in 1825, which can be found in [Ri1930].
> The below parametrization is brought from the MSE answer [MSE].
>
> [Ri1930] Richmond, H. W. "On Rational Solutions of $x^3 + y^3 + z^3 = R$." Proceedings of the Edinburgh Mathematical Society 2.2 (1930): 92-100.
> [MSE] Kieren MacMillan, Proving that any rational number can be represented as the sum of the cubes of three rational numbers, https://math.stackexchange.com/q/4480969

```lean
theorem isSumOfThreeCubesRat_any (r : ℚ) : IsSumOfThreeCubes r
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SumOfThreeCubes.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SumOfThreeCubes.lean#L78).

## `SumOfThreeCubes.isSumOfThreeCubes_iff_mod_9`

Open: stated without proof.

> An integer `n : ℤ` can be written as a sum of three cubes (of integers) if and only if
> `n` is not `4` or `5` mod `9`.

```lean
theorem isSumOfThreeCubes_iff_mod_9 :
    ∀ n : ℤ, IsSumOfThreeCubes n ↔ ¬(n ≡ 4 [ZMOD 9] ∨ n ≡ 5 [ZMOD 9])
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/SumOfThreeCubes.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SumOfThreeCubes.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SumOfThreeCubes.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SumOfThreeCubes.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Sums_of_three_cubes)
