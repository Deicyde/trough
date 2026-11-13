---
declaration: theorem
origin: cited
lean: Erdos970.erdos_970, Erdos970.erdos_970.variants.iterated_log
statement: formalized
---

# Erdős Problem 970

> *References:*
> - [erdosproblems.com/970](https://www.erdosproblems.com/970)
> - [FGKMT18] Ford, Kevin and Green, Ben and Konyagin, Sergei and Maynard, James and Tao, Terence,
>   *Long gaps between primes*. J. Amer. Math. Soc. (2018), 65-105.
> - [Iw78] Iwaniec, Henryk, *On the problem of {J}acobsthal*. Demonstratio Math. (1978), 225--231.
> - [OAI26a] OpenAI, *A quadratic bound for Jacobsthal's function*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/970.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/970.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/970](https://www.erdosproblems.com/970).

The file states 2 research or textbook statements: 2 solved.

## `Erdos970.erdos_970`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean#L13](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Jacobsthal/Conclusions/QuadraticBound.lean#L13).

> Let $h(k)$ be Jacobsthal's function, defined to as the minimal $m$ such that, if $n$ has at most $k$ prime factors, then in any set of $m$ consecutive integers there exists an integer coprime to $n$. Determine the order of magnitude of $h(k)$. In particular, is it true that
>
> $$h(k) \ll k^2?$$
>
> The bound $h(k) \ll k^2$ was proved by an internal OpenAI model in September 2026 [OAI26a]; see
> the linked Lean proof. The order of magnitude of $h(k)$ remains open.

```lean
theorem erdos_970 :
    ∃ C > (0 : ℝ), ∀ k : ℕ, 0 < k → (jacobsthalFunction k : ℝ) ≤ C * k ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/970.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/970.lean#L60).

## `Erdos970.erdos_970.variants.iterated_log`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Jacobsthal/Conclusions/IteratedLogBound.lean#L59](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/Jacobsthal/Conclusions/IteratedLogBound.lean#L59).

> The stronger bound
>
> $$h(k) \ll \frac{k^2}{(\log\log 3k)^2}$$
>
> proved in [OAI26a].

```lean
theorem erdos_970.variants.iterated_log :
    ∃ C > (0 : ℝ), ∀ k : ℕ, 0 < k →
      (jacobsthalFunction k : ℝ) ≤ C * k ^ 2 / (Real.log (Real.log (3 * k))) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/970.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/970.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/970.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/970.lean)
- [erdosproblems.com/970](https://www.erdosproblems.com/970)
