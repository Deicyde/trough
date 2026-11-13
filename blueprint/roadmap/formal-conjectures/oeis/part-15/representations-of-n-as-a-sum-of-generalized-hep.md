---
declaration: theorem
origin: cited
lean: OeisA255916.conjecture_1, OeisA255916.conjecture_2, OeisA255916.conjecture_3
statement: formalized
---

# Representations of $n$ as a sum of generalized heptagonal, octagonal, and nonagonal numbers

> The sequence $a(n)$ counts the number of ways to write $n$ as the sum of a generalized heptagonal
> number $G_7(k) = \frac{5k^2 - 3k}{2}$ ($k \in \mathbb{Z}$), an octagonal number
> $P_8(x) = x(3x - 2)$ ($x \ge 0$), and a nonagonal number $P_9(y) = \frac{y(7y - 5)}{2}$ ($y \ge 0$).
>
> *References:*
> - [A255916](https://oeis.org/A255916)

*Quoted from [FormalConjectures/OEIS/255916.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/255916.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA255916.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_1 (n : ℕ) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/255916.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/255916.lean#L94).

## `OeisA255916.conjecture_2`

Open: stated without proof.

> Conjecture (i): For $k \ge j \ge 3$, every nonnegative integer can be written as the sum of a
> generalized heptagonal number, a $j$-gonal number and a $k$-gonal number, if and only if $(j, k)$
> is among the following ordered pairs:
> $(3, k)$ ($k = 3..19, 21..24, 26, 27, 29, 30$),
> $(4, k)$ ($k = 4..11, 13, 14, 17, 19, 20, 23, 26$),
> $(5, 6), (5, 9), (6, 7), (8, 9)$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_2 (j k : ℕ) (hjk : 3 ≤ j ∧ j ≤ k) :
    (∀ n : ℕ, IsSumOfGmPjPk 7 n j k) ↔ (j, k) ∈ sunPolygonalPairsSet1
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/255916.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/255916.lean#L107).

## `OeisA255916.conjecture_3`

Open: stated without proof.

> Conjecture (ii): For $k \ge j \ge 3$, every nonnegative integer can be written as the sum of a
> generalized pentagonal number, a $j$-gonal number and a $k$-gonal number, if and only if $(j, k)$
> is among the following ordered pairs:
> $(3, k)$ ($k = 3..20, 22, 24, 25, 28..30, 32, 37$),
> $(4, k)$ ($k = 4..13, 15, 16, 18, 20..25, 27, 28, 31, 33, 34$),
> $(5, k)$ ($k = 6..12, 20$), $(6, k)$ ($k = 7..10$), $(7, 9), (7, 11), (8, 10), (9, 11)$.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (j k : ℕ) (hjk : 3 ≤ j ∧ j ≤ k) :
    (∀ n : ℕ, IsSumOfGmPjPk 5 n j k) ↔ (j, k) ∈ sunPolygonalPairsSet2
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/255916.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/255916.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/255916.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/255916.lean)
- [A255916](https://oeis.org/A255916)
