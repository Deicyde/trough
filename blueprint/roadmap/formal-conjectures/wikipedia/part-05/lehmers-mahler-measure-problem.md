---
declaration: theorem
origin: cited
lean: LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem, LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.best, LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.not_reciprocal, LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.odd
statement: formalized
---

# Lehmer's Mahler measure problem

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_conjecture)
> - [Tao's optimization constant 40a](https://teorth.github.io/optimizationproblems/constants/40a.html)

*Quoted from [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved.

## `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem`

Open: stated without proof.

> Let `M(f)` denote the Mahler measure of `f`.
> There exists a constant `μ>1` such that for any `f(x)∈ℤ[x], M(f)>1 → M(f)≥μ`.
> That is, `lehmerConstant > 1`.

```lean
theorem lehmer_mahler_measure_problem : 1 < lehmerConstant
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean#L58).

## `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.best`

Open: stated without proof.

> `μ=M(X^10 + X^9 - X^7 - X^6 - X^5 - X^4 - X^3 + X + 1)` is the best value for `lehmer_mahler_measure_problem`.

```lean
theorem lehmer_mahler_measure_problem.variants.best :
    mahlerMeasureZ lehmerPolynomial ≤ lehmerConstant
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean#L67).

## `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.not_reciprocal`

Solved: stated here without proof.

> If $f$ is irreducible and not reciprocal and $M(f) > 1$ then $M(f) \ge M(X^3 - X - 1)$.

```lean
theorem lehmer_mahler_measure_problem.variants.not_reciprocal (f : ℤ[X]) (hi : Irreducible f)
    (hf : mahlerMeasureZ f > 1) (hf' : f.reverse ≠ f) :
    mahlerMeasureZ f ≥ mahlerMeasureZ (X^3 - X - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean#L75).

## `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem.variants.odd`

Solved: stated here without proof.

> If $f$ is not reciprocal, all the coefficients of $f$ are odd and $M(f) > 1$, then
> $M(f) \ge M(X^2 - X - 1)$.
>
> A polynomial $f$ of degree $d$ is *reciprocal* when $X^d f(1/X) = \pm f$, so nonreciprocity
> rules out both signs. The negative sign has to be excluded as well: the polynomial
> $X^7 - X^6 - X^5 - X^4 + X^3 + X^2 + X - 1$ has all coefficients odd and satisfies
> $X^7 f(1/X) = -f$, but $1 < M(f) = 1.5823\dots < M(X^2 - X - 1)$.

```lean
theorem lehmer_mahler_measure_problem.variants.odd (f : ℤ[X])
    (hf : mahlerMeasureZ f > 1) (hf' : f.reverse ≠ f) (hf'' : f.reverse ≠ -f)
    (hodd : f.HasOddCoeffs) :
    mahlerMeasureZ f ≥ mahlerMeasureZ (X^2 - X - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LehmerMahlerMeasureProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Lehmer%27s_conjecture)
