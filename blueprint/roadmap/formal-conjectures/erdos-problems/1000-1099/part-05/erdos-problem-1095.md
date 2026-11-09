---
declaration: theorem
origin: cited
lean: Erdos1095.erdos_1095.variants.lower_solved, Erdos1095.erdos_1095.variants.upper_conjecture, Erdos1095.erdos_1095.variants.lower_conjecture, Erdos1095.erdos_1095.variants.log_equivalent
statement: formalized
---

# Erdős Problem 1095

> *References:*
> - [erdosproblems.com/1095](https://www.erdosproblems.com/1095)
> - [EES74] Ecklund, Jr., E. F. and Erd\H{o}s, P. and Selfridge, J. L., A new function associated with
>   the prime factors of {$(\sp{n}\sb{k})$}. Math. Comp. (1974), 647--649.
> - [ELS93] Erdős, P. and Lacampagne, C. B. and Selfridge, J. L., Estimates of the least prime factor
>   of a binomial coefficient. Math. Comp. (1993), 215--224.
> - [GrRa96] Granville, Andrew and Ramaré, Olivier, Explicit bounds on exponential sums and the
>   scarcity of squarefree binomial coefficients. Mathematika (1996), 73--107.
> - [Ko99b] Konyagin, S. V., Estimates of the least prime factor of a binomial coefficient.
>   Mathematika (1999), 41--55.
> - [SSW20] Sorenson, Brianna and Sorenson, Jonathan and Webster, Jonathan, An algorithm and estimates
>   for the {E}rdős-{S}elfridge function. (2020), 371--385.

*Quoted from [FormalConjectures/ErdosProblems/1095.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1095](https://www.erdosproblems.com/1095).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos1095.erdos_1095.variants.lower_solved`

Solved: stated here without proof.

> The current record is $g(k) \gg \exp(c(\log k)^2)$ for some $c>0$, due to Konyagin [Ko99b]. -

```lean
theorem erdos_1095.variants.lower_solved :
    ∃ c > 0, (fun k : ℕ ↦ exp (c * log k ^ 2)) =O[atTop] fun k ↦ (g k : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1095.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean#L54).

## `Erdos1095.erdos_1095.variants.upper_conjecture`

Solved: stated here without proof.

> Ecklund, Erdős, and Selfridge [EES74] proved $g(k)\leq \exp((1+o(1))k)$.

```lean
theorem erdos_1095.variants.upper_conjecture :
    ∃ f : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧ ∀ᶠ k in atTop, g k ≤ exp (k * (1 + f k))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1095.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean#L62).

## `Erdos1095.erdos_1095.variants.lower_conjecture`

Open: stated without proof.

> Erdős, Lacampagne, and Selfridge [ELS93] write 'it is clear to every right-thinking person' that
> $g(k)\geq\exp(c\frac{k}{\log k})$ for some constant $c>0$.

```lean
theorem erdos_1095.variants.lower_conjecture : ∃ c > 0, ∀ᶠ k in atTop, g k ≥ exp (c * k / log k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1095.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean#L71).

## `Erdos1095.erdos_1095.variants.log_equivalent`

Open: stated without proof.

> Sorenson, Sorenson, and Webster [SSWE20] give heuristic evidence that $\log g(k) \asymp \frac{k}{\log k}$.

```lean
theorem erdos_1095.variants.log_equivalent :
    (fun k ↦ log (g k)) =Θ[atTop] (fun k ↦ (k : ℝ) / log k)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1095.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1095.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1095.lean)
- [erdosproblems.com/1095](https://www.erdosproblems.com/1095)
