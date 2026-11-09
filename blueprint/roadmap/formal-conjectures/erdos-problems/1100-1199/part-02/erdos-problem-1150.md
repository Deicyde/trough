---
declaration: theorem
origin: cited
lean: Erdos1150.erdos_1150, Erdos1150.erdos_1150.variants.parseval_lower_bound
statement: formalized
---

# Erdős Problem 1150

> *References:*
> - [erdosproblems.com/1150](https://www.erdosproblems.com/1150)
> - [OAI26a] OpenAI, *Asymptotically minimal maxima of real Littlewood polynomials*. OpenAI Math
>   Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/1150.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1150.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1150](https://www.erdosproblems.com/1150).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos1150.erdos_1150`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/Littlewood/Main.lean#L187](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/Littlewood/Main.lean#L187).

> Is there some constant $c > 0$ such that, for all large enough $n$ and all polynomials $P$ of
> degree $n$ with coefficients in $\{-1, 1\}$,
> $$\max_{|z|=1} |P(z)| > (1 + c) \sqrt{n}?$$
>
> No. This was disproved by an internal OpenAI model in September 2026 [OAI26a]; see the linked
> Lean proof.

```lean
theorem erdos_1150 :
    ¬ ∃ c > 0, ∀ᶠ n in Filter.atTop,
      ∀ P : ℂ[X],  (∀ i ≤ P.natDegree, P.coeff i = - 1 ∨ P.coeff i = 1) → P.natDegree = n →
        ⨆ z : Metric.sphere (0 : ℂ) 1, ‖P.eval (z : ℂ)‖ > (1 + c) * Real.sqrt n
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1150.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1150.lean#L47).

## `Erdos1150.erdos_1150.variants.parseval_lower_bound`

Textbook result, proved here.

> The trivial lower bound from Parseval's identity: for any polynomial $P$ of degree $n$ with
> coefficients in $\{-1, 1\}$, we have $\max_{|z|=1} |P(z)| \geq \sqrt{n+1}$.
>
> This follows from Parseval's identity:
> $$\frac{1}{2\pi} \int_0^{2\pi} |P(e^{i\theta})|^2 d\theta = \sum_{k=0}^{n} |a_k|^2 = n+1$$
> since each $|a_k|^2 = 1$. The circle average is bounded by the pointwise supremum squared, so
> $\max_{|z|=1} |P(z)|^2 \ge n+1$, whence $\max_{|z|=1} |P(z)| \ge \sqrt{n+1}$.

```lean
theorem erdos_1150.variants.parseval_lower_bound (P : ℂ[X]) (n : ℕ)
    (hcoeff : ∀ i ≤ P.natDegree, P.coeff i = -1 ∨ P.coeff i = 1)
    (hdeg : P.natDegree = n) :
    ⨆ z : Metric.sphere (0 : ℂ) 1, ‖P.eval (z : ℂ)‖ ≥ Real.sqrt (n + 1)
```

Category `textbook`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1150.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1150.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1150.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1150.lean)
- [erdosproblems.com/1150](https://www.erdosproblems.com/1150)
