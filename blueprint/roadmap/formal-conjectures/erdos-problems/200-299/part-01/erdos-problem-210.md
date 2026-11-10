---
declaration: theorem
origin: cited
lean: Erdos210.erdos_210.parts.i, Erdos210.erdos_210.lower_bound, Erdos210.erdos_210.variants.csima_sawyer, Erdos210.erdos_210.variants.green_tao, Erdos210.erdos_210.variants.green_tao_odd, Erdos210.erdos_210.variants.even_upper_bound, Erdos210.erdos_210.variants.seven, Erdos210.erdos_210.variants.sylvester_gallai, Erdos210.erdos_210.upper_bound, Erdos210.erdos_210.parts.ii
statement: formalized
---

# Erdős Problem 210

> *References:*
> - [erdosproblems.com/210](https://www.erdosproblems.com/210)
> - [Mo51] Motzkin, T. S., *The lines and planes connecting the points of a finite set*.
>   Transactions of the American Mathematical Society 70 (1951), 451–464.
> - [KeMo58] Kelly, L. M. and Moser, W. O. J., *On the number of ordinary lines determined by
>   n points*. Canadian Journal of Mathematics 10 (1958), 210–219.
> - [CsSa93] Csima, J. and Sawyer, E. T., *There exist 6n/13 ordinary points*.
>   Discrete & Computational Geometry 9 (1993), 187–202.
> - [GrTa13] Green, B. and Tao, T., *On sets defining few ordinary lines*.
>   Discrete & Computational Geometry 50 (2013), 409–468.

*Quoted from [FormalConjectures/ErdosProblems/210.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/210](https://www.erdosproblems.com/210).

The file states 10 research or textbook statements: 10 solved. It also has 23 API statements, counted here but not shown.

## `Erdos210.erdos_210.parts.i`

Solved: stated here without proof.

> Let $f(n)$ be the sharp guarantee such that, for any $n$ points in $\mathbb R^2$,
> not all on a line, there are at least $f(n)$ lines which contain exactly two points
> (called ordinary lines). Does $f(n)\to\infty$?
> That $f(n)\to\infty$ was proved by Motzkin [Mo51].

```lean
theorem erdos_210.parts.i : Tendsto f atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L52).

## `Erdos210.erdos_210.lower_bound`

Solved: stated here without proof.

> Kelly and Moser [KeMo58] proved that $f(n)\geq 3n/7$ for all $n$.
> Only $n\geq3$ have noncollinear configurations.

```lean
theorem erdos_210.lower_bound : ∀ n : ℕ, 3 ≤ n → 3 * n ≤ 7 * f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L58).

## `Erdos210.erdos_210.variants.csima_sawyer`

Solved: stated here without proof.

> Csima and Sawyer [CsSa93] proved $f(n)\geq6n/13$ when $n\geq8$.

```lean
theorem erdos_210.variants.csima_sawyer : ∀ n : ℕ, 8 ≤ n → 6 * n ≤ 13 * f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L63).

## `Erdos210.erdos_210.variants.green_tao`

Solved: stated here without proof.

> Green and Tao [GrTa13] proved $f(n)\geq n/2$ for sufficiently large $n$.

```lean
theorem erdos_210.variants.green_tao : ∀ᶠ n : ℕ in atTop, n ≤ 2 * f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L68).

## `Erdos210.erdos_210.variants.green_tao_odd`

Solved: stated here without proof.

> Green and Tao [GrTa13] proved $f(n)\geq3\lfloor n/4\rfloor$ for sufficiently
> large odd $n$ [GrTa13, Theorem 2.2].

```lean
theorem erdos_210.variants.green_tao_odd :
    ∀ᶠ n : ℕ in atTop, Odd n → 3 * (n / 4) ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L74).

## `Erdos210.erdos_210.variants.even_upper_bound`

Solved: stated here without proof.

> Green and Tao [GrTa13, Proposition 2.1] give configurations attaining $n/2$
> ordinary lines for sufficiently large even $n$.

```lean
theorem erdos_210.variants.even_upper_bound :
    ∀ᶠ n : ℕ in atTop, Even n → 2 * f n ≤ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L81).

## `Erdos210.erdos_210.variants.seven`

Solved: stated here without proof.

> Kelly and Moser [KeMo58] give a seven-point configuration with three ordinary
> lines, attaining their lower bound at $n=7$.

```lean
theorem erdos_210.variants.seven : f 7 = 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L88).

## `Erdos210.erdos_210.variants.sylvester_gallai`

Proved here.

> The Sylvester–Gallai theorem states that $f(n)\geq1$.

```lean
theorem erdos_210.variants.sylvester_gallai {n : ℕ} (hn : 3 ≤ n) : 1 ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L151).

## `Erdos210.erdos_210.upper_bound`

Proved here.

> An explicit near-pencil gives the linear upper bound $f(n)\leq n$.

```lean
theorem erdos_210.upper_bound {n : ℕ} (hn : 3 ≤ n) : f n ≤ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 278](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L278).

## `Erdos210.erdos_210.parts.ii`

Solved: stated here without proof.

> How fast does $f(n)$ tend to infinity? Kelly–Moser [KeMo58] and the near-pencil
> construction show that its growth is linear.

```lean
theorem erdos_210.parts.ii :
    (fun n : ℕ => (f n : ℝ)) =Θ[atTop] (fun n : ℕ => (n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/210.lean, line 285](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean#L285).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/210.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/210.lean)
- [erdosproblems.com/210](https://www.erdosproblems.com/210)
