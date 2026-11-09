---
declaration: theorem
origin: cited
lean: Constant7b.irrational_gamma_one_div_four, Constant7b.c7b_lower_bound, Constant7b.c7b_lower_bound_improved, Constant7b.c7b_upper_bound, Constant7b.c7b_upper_bound_improved
statement: formalized
---

# Tao's Optimization Constant 7b / The Irrationality Measure of $\Gamma(1/4)$

> *References:*
> - [Tao's Optimization Constant 7b](https://teorth.github.io/optimizationproblems/constants/7b.html)
> - [D1842] Dirichlet, L. G. P., *Verallgemeinerung eines Satzes aus der Lehre von den
>   Kettenbrüchen nebst einigen Anwendungen auf die Theorie der Zahlen*. Sitzungsberichte der
>   Preussischen Akademie der Wissenschaften (1842), 93–95.
> - [C1976] Chudnovsky, G. V., *Algebraic independence of constants connected with the exponential
>   and the elliptic functions*. Dokl. Akad. Nauk Ukrain. SSR Ser. A 1976, no. 8, 698–701.
> - [Bru2002] Bruiltet, S., [*D'une mesure d'approximation simultanée à une mesure
>   d'irrationalité :
>   le cas de $\Gamma(1/4)$ et $\Gamma(1/3)$*](https://doi.org/10.4064/aa104-3-3).
>   Acta Arith. **104** (2002), 243–281.

*Quoted from [FormalConjectures/OptimizationConstants/7b.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Constant7b.irrational_gamma_one_div_four`

Solved: stated here without proof.

> $\Gamma(1/4)$ is irrational, as proven in [C1976].

```lean
theorem irrational_gamma_one_div_four : Irrational (Real.Gamma (1 / 4))
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/7b.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean#L49).

## `Constant7b.c7b_lower_bound`

Proved here.

> The first and current best known lower bound, given by Dirichlet's theorem [D1842]. It applies
> because $\Gamma(1/4)$ is irrational by Chudnovsky's theorem [C1976].

```lean
theorem c7b_lower_bound : 2 ≤ C7b
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/7b.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean#L55).

## `Constant7b.c7b_lower_bound_improved`

Open: stated without proof.

> Can the current best lower bound be improved?

```lean
theorem c7b_lower_bound_improved : 2 < C7b
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/7b.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean#L60).

## `Constant7b.c7b_upper_bound`

Solved: stated here without proof.

> The first and current best known upper bound, proved by Bruiltet in [Bru2002]. It follows from
> an explicit lower bound on $|\Gamma(1/4) - p/q|$ for rational $p/q$ of sufficiently large height.

```lean
theorem c7b_upper_bound : C7b ≤ 10 ^ 143
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/7b.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean#L66).

## `Constant7b.c7b_upper_bound_improved`

Open: stated without proof.

> Can the current best upper bound be improved?

```lean
theorem c7b_upper_bound_improved : C7b < 10 ^ 143
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [33 Special functions](../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/7b.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OptimizationConstants/7b.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OptimizationConstants/7b.lean)
- [Tao's Optimization Constant 7b](https://teorth.github.io/optimizationproblems/constants/7b.html)
