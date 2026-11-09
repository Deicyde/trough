---
declaration: theorem
origin: cited
lean: Erdos820.erdos_820, Erdos820.erdos_820.variants.log_log_exponent, Erdos820.erdos_820.variants.two_pow_upper, Erdos820.erdos_820.variants.erdos_lower
statement: formalized
---

# Erdős Problem 820

> *References:*
> - [erdosproblems.com/820](https://www.erdosproblems.com/820)
> - [Er74b] Erdős, P., *Remarks on some problems in number theory*. Math. Balkanica (1974),
>   197-202.
> - [OEIS A263647](https://oeis.org/A263647): the $n$ with $(2^n-1, 3^n-1) = 1$.

*Quoted from [FormalConjectures/ErdosProblems/820.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/820](https://www.erdosproblems.com/820).

The file states 4 research or textbook statements: 3 open and 1 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Erdos820.erdos_820`

Open: stated without proof.

> Let $H(n)$ be the smallest integer $l$ such that there exists $k < l$ with $(k^n-1, l^n-1) = 1$.
> Is it true that $H(n) = 3$ infinitely often? That is, is $(2^n-1, 3^n-1) = 1$ for infinitely
> many $n$ (see `Erdos820.H_eq_three_iff`)?
>
> The request to estimate $H(n)$ is open-ended and not formalised; the variants below state the
> specific questions that are asked. See also Erdős Problem 770.

```lean
theorem erdos_820 : {n : ℕ | H n = 3}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/820.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean#L127).

## `Erdos820.erdos_820.variants.log_log_exponent`

Open: stated without proof.

> Is it true that there exists some constant $c > 0$ such that, for all $\epsilon > 0$,
> $$
> H(n) > \exp\left(n^{(c-\epsilon)/\log\log n}\right)
> $$
> for infinitely many $n$ and
> $$
> H(n) < \exp\left(n^{(c+\epsilon)/\log\log n}\right)
> $$
> for all large enough $n$?

```lean
theorem erdos_820.variants.log_log_exponent :
    ∃ c > (0 : ℝ), ∀ ε > (0 : ℝ),
      (∃ᶠ n : ℕ in atTop,
        Real.exp ((n : ℝ) ^ ((c - ε) / Real.log (Real.log (n : ℝ)))) < (H n : ℝ)) ∧
      ∀ᶠ n : ℕ in atTop,
        (H n : ℝ) < Real.exp ((n : ℝ) ^ ((c + ε) / Real.log (Real.log (n : ℝ))))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/820.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean#L142).

## `Erdos820.erdos_820.variants.two_pow_upper`

Open: stated without proof.

> Let $K(n)$ be the smallest $k$ such that $(k^n-1, 2^n-1) = 1$. Does a similar upper bound hold
> for $K(n)$? That is, is there a constant $c > 0$ such that, for all $\epsilon > 0$,
> $$
> K(n) < \exp\left(n^{(c+\epsilon)/\log\log n}\right)
> $$
> for all large enough $n$?
>
> We read "similar" as an upper bound of the same shape, with its own constant $c$, which need
> not be the same as in `Erdos820.erdos_820.variants.log_log_exponent`.

```lean
theorem erdos_820.variants.two_pow_upper :
    ∃ c > (0 : ℝ), ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (K n : ℝ) < Real.exp ((n : ℝ) ^ ((c + ε) / Real.log (Real.log (n : ℝ))))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/820.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean#L162).

## `Erdos820.erdos_820.variants.erdos_lower`

Solved: stated here without proof.

> Erdős [Er74b] proved that there exists a constant $c > 0$ such that
> $$
> H(n) > \exp\left(n^{c/(\log\log n)^2}\right)
> $$
> for infinitely many $n$.

```lean
theorem erdos_820.variants.erdos_lower :
    ∃ c > (0 : ℝ), ∃ᶠ n : ℕ in atTop,
      Real.exp ((n : ℝ) ^ (c / Real.log (Real.log (n : ℝ)) ^ 2)) < (H n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/820.lean, line 175](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean#L175).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/820.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/820.lean)
- [erdosproblems.com/820](https://www.erdosproblems.com/820)
