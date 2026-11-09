---
declaration: theorem
origin: cited
lean: Erdos967.erdos_967, Erdos967.erdos_967.variants.yip, Erdos967.erdos_967.variants.finite, Erdos967.erdos_967.variants.two_three_five, Erdos967.erdos_967.variants.tauberian
statement: formalized
---

# Erdős Problem 967

> *References:*
> - [erdosproblems.com/967](https://www.erdosproblems.com/967)
> - [ErIn64] Erdős, P. and Ingham, A. E., *Arithmetical Tauberian theorems*. Acta Arith. (1964),
>   341-356.
> - [Yi25] Yip, F., *On a problem of Erdős and Ingham*. arXiv:2512.16528 (2025).

*Quoted from [FormalConjectures/ErdosProblems/967.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/967](https://www.erdosproblems.com/967).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos967.erdos_967`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/llllvvuu/d25f037d1f1000bdabd6ca928c74c9bb/raw/c2d3e4ed5d88520993b508f84be029cf8808f565/967.lean](https://gist.githubusercontent.com/llllvvuu/d25f037d1f1000bdabd6ca928c74c9bb/raw/c2d3e4ed5d88520993b508f84be029cf8808f565/967.lean).

> Let $1\lt a_1\lt \cdots$ be a sequence of integers such that $\sum\frac{1}{a_i}\lt \infty$. Is it true
> that, for every $t\in \mathbb{R}$,
>
> $$1+\sum_{k}\frac{1}{a_k^{1+it}}\neq 0?$$
>
> Yip [Yi25] has proved that this is not always true - in fact, for any real $t\neq 0$, there
> exists a sequence of integers $1\lt a_1\lt \cdots$ such that $\sum \frac{1}{a_i}\lt \infty$ and
> $1+\sum_{k}\frac{1}{a_k^{1+it}}=0$.
>
> This was formalized in Lean by Wu using Aristotle.

```lean
theorem erdos_967 :
    ¬ ∀ a : ℕ → ℕ, StrictMono a → 1 < a 0 → Summable (fun k : ℕ => 1 / (a k : ℝ)) →
      ∀ t : ℝ, 1 + (∑' k, summand t (a k)) ≠ 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/967.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean#L55).

## `Erdos967.erdos_967.variants.yip`

Solved: stated here without proof.

> Yip [Yi25] has proved that this is not always true - in fact, for any real $t\neq 0$, there
> exists a sequence of integers $1\lt a_1\lt \cdots$ such that $\sum \frac{1}{a_i}\lt \infty$ and
> $1+\sum_{k}\frac{1}{a_k^{1+it}}=0$.

```lean
theorem erdos_967.variants.yip (t : ℝ) (ht : t ≠ 0) :
    ∃ a : ℕ → ℕ, StrictMono a ∧ 1 < a 0 ∧ Summable (fun k : ℕ => 1 / (a k : ℝ)) ∧
      (1 + (∑' k, summand t (a k)) = 0)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/967.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean#L66).

## `Erdos967.erdos_967.variants.finite`

Open: stated without proof.

> It remains open whether this is true for every finite sequence of integers.

```lean
theorem erdos_967.variants.finite :
    ∀ A : Finset ℕ, (∀ n ∈ A, 1 < n) → ∀ t : ℝ, 1 + (∑ n ∈ A, summand t n) ≠ 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/967.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean#L75).

## `Erdos967.erdos_967.variants.two_three_five`

Open: stated without proof.

> A question of Erdős and Ingham [ErIn64]. The simplest case they could not decide this question
> for was the finite sequence $\{2,3,5\}$.

```lean
theorem erdos_967.variants.two_three_five :
    ∀ t : ℝ, 1 + (∑ n ∈ ({2, 3, 5} : Finset ℕ), summand t n) ≠ 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/967.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean#L84).

## `Erdos967.erdos_967.variants.tauberian`

Solved: stated here without proof.

> Their interest in this problem arose from their proof that the statement that there are no such
> zeros is equivalent to the fact that, for any non-decreasing $f:\mathbb{R}\to \mathbb{R}_{\geq 0}$
> which is bounded on every bounded interval and is $=0$ for $x<1$, the relationship
>
> $$f(x)+\sum_k f(x/a_k)=\left(1+\sum_k \frac{1}{a_k}+o(1)\right)x$$
>
> implies $f(x)=(1+o(1))x$.

```lean
theorem erdos_967.variants.tauberian (a : ℕ → ℕ) (ha : StrictMono a) (ha₀ : 1 < a 0)
    (hsum : Summable (fun k : ℕ => 1 / (a k : ℝ))) :
    (∀ t : ℝ, 1 + (∑' k, summand t (a k)) ≠ 0) ↔
      ∀ f : ℝ → ℝ, Monotone f → (∀ x : ℝ, 0 ≤ f x) → (∀ x < 1, f x = 0) →
        (∀ x y : ℝ, BddAbove (f '' Set.Icc x y)) →
        Tendsto (fun x : ℝ => (f x + ∑' k, f (x / (a k : ℝ))) / x) atTop
          (𝓝 (1 + ∑' k, 1 / (a k : ℝ))) →
        Tendsto (fun x : ℝ => f x / x) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/967.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/967.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/967.lean)
- [erdosproblems.com/967](https://www.erdosproblems.com/967)
