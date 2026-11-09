---
declaration: theorem
origin: cited
lean: Constant7a.two_le_irrationalityExponent, Constant7a.irrationalityExponent_of_algebraic, Constant7a.c7a_lower_bound, Constant7a.c7a_le_42, Constant7a.c7a_lt_14_797075, Constant7a.c7a_upper_bound, Constant7a.c7a_eq_two
statement: formalized
---

# Tao's Optimization Constant 7a / The Irrationality Measure of $\pi$

> *References:*
> - [Tao's Optimization Constant 7a](https://teorth.github.io/optimizationproblems/constants/7a.html)
> - [D1842] Dirichlet, L. G. P., *Verallgemeinerung eines Satzes aus der Lehre von den
>   Kettenbrüchen nebst einigen Anwendungen auf die Theorie der Zahlen*. Sitzungsberichte der
>   Preussischen Akademie der Wissenschaften (1842), 93–95.
> - [M1953] Mahler, K., *On the approximation of $\pi$*. Nederl. Akad. Wetensch. Proc. Ser. A
>   **56** = Indag. Math. **15** (1953), 30–42.
> - [R1955] Roth, K. F., [*Rational approximations to algebraic
>   numbers*](https://doi.org/10.1112/S0025579300000644). Mathematika **2** (1955), 1–20.
> - [RV1993] Rhin, G. and Viola, C., [*On the irrationality measure of
>   $\zeta(2)$*](https://doi.org/10.5802/aif.1322). Ann. Inst. Fourier **43** (1993), 85–109.
> - [ZZ2020] Zeilberger, D. and Zudilin, W., *The irrationality measure of $\pi$ is at most
>   $7.103205334137\ldots$*. Moscow J. Comb. Number Theory **9** (2020), 407–419.
>   [arXiv:1912.06345](https://arxiv.org/abs/1912.06345)
> - [OAI2026] OpenAI, [*The irrationality exponent of $\pi$ is
>   2*](https://github.com/openai/math/blob/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf),
>   2026.

*Quoted from [FormalConjectures/OptimizationConstants/7a.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 5 solved and 2 textbook results. It also has 3 API statements, counted here but not shown.

## `Constant7a.two_le_irrationalityExponent`

Textbook result, stated without proof.

> Every irrational real number has irrationality exponent at least two by Dirichlet's
> approximation theorem [D1842].

```lean
theorem two_le_irrationalityExponent {x : ℝ} (hx : Irrational x) :
    2 ≤ irrationalityExponent x
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L98).

## `Constant7a.irrationalityExponent_of_algebraic`

Solved: stated here without proof.

> Every algebraic real number has irrationality exponent at most two. For irrational algebraic
> numbers, this is Roth's theorem [R1955].

```lean
theorem irrationalityExponent_of_algebraic {x : ℝ} (hx : IsAlgebraic ℚ x) :
    irrationalityExponent x ≤ 2
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L105).

## `Constant7a.c7a_lower_bound`

Textbook result, proved here.

> The sharp lower bound, given by Dirichlet's theorem [D1842]. This bound
> holds for every irrational real number.

```lean
theorem c7a_lower_bound : 2 ≤ C7a
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L116).

## `Constant7a.c7a_le_42`

Solved: stated here without proof.

> The first known upper bound, proved by Mahler in [M1953]. This was the first proof that
> $C_{7a}$ is finite, or equivalently that $\pi$ is not a Liouville number.

```lean
theorem c7a_le_42 : C7a ≤ 42
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L121).

## `Constant7a.c7a_lt_14_797075`

Solved: stated here without proof.

> An intermediate upper bound proved by Rhin and Viola in [RV1993]. It follows from an effective
> irrationality measure for $\zeta(2) = \pi^2 / 6$.

```lean
theorem c7a_lt_14_797075 : C7a < 14.797075
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L127).

## `Constant7a.c7a_upper_bound`

Solved: stated here without proof.

> The best upper bound before [OAI2026], proved by Zeilberger and Zudilin in [ZZ2020].

```lean
theorem c7a_upper_bound : C7a < 7.103205334138
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L132).

## `Constant7a.c7a_eq_two`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean](https://github.com/openai/math/blob/main/lean/ComparatorChallenges/PiExponent.lean).

> The irrationality measure of $\pi$ is exactly $2$, proved by OpenAI in [OAI2026].

```lean
theorem c7a_eq_two : C7a = 2
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OptimizationConstants/7a.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OptimizationConstants/7a.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7a.lean)
- [Tao's Optimization Constant 7a](https://teorth.github.io/optimizationproblems/constants/7a.html)
