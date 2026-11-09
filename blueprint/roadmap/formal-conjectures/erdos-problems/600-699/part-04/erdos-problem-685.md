---
declaration: theorem
origin: cited
lean: Erdos685.erdos_685.parts.i, Erdos685.erdos_685.parts.ii, Erdos685.erdos_685.variants.trivial_lower_bound
statement: formalized
---

# Erdős Problem 685

> *References:*
> - [erdosproblems.com/685](https://www.erdosproblems.com/685)
> - [Er79d] Erdős, P., *Some unconventional problems in number theory*. Acta Math. Acad. Sci.
>   Hungar. (1979), 71-80.

*Quoted from [FormalConjectures/ErdosProblems/685.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/685.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/685](https://www.erdosproblems.com/685).

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `Erdos685.erdos_685.parts.i`

Open: stated without proof.

> Let $\epsilon > 0$ and let $n$ be large depending on $\epsilon$. Is it true that for all
> $n^{\epsilon} < k \leq n^{1-\epsilon}$ the number of distinct prime divisors of $\binom{n}{k}$ is
> $$(1+o(1))\, k \sum_{k < p < n} \frac{1}{p}?$$
>
> The $o(1)$ is uniform in $k$.

```lean
theorem erdos_685.parts.i :
    ∀ ε > (0 : ℝ), ∀ δ > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ k : ℕ,
      (n : ℝ) ^ ε < (k : ℝ) → (k : ℝ) ≤ (n : ℝ) ^ (1 - ε) →
        |(ω (n.choose k) : ℝ) - (k : ℝ) * primeRecipSum k n| ≤
          δ * ((k : ℝ) * primeRecipSum k n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/685.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/685.lean#L54).

## `Erdos685.erdos_685.parts.ii`

Open: stated without proof.

> Is it true that, for some constant $c > 0$, the number of distinct prime divisors of
> $\binom{n}{k}$ is
> $$(1+o(1))\, k \sum_{k < p < n} \frac{1}{p}$$
> even for all $(\log n)^c \leq k \leq n^{1-\epsilon}$?
>
> Here $\epsilon > 0$ is as in the first question, and the $o(1)$ is uniform in $k$.

```lean
theorem erdos_685.parts.ii :
    ∃ c > (0 : ℝ), ∀ ε > (0 : ℝ), ∀ δ > (0 : ℝ), ∀ᶠ n : ℕ in atTop, ∀ k : ℕ,
      Real.log (n : ℝ) ^ c ≤ (k : ℝ) → (k : ℝ) ≤ (n : ℝ) ^ (1 - ε) →
        |(ω (n.choose k) : ℝ) - (k : ℝ) * primeRecipSum k n| ≤
          δ * ((k : ℝ) * primeRecipSum k n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/685.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/685.lean#L70).

## `Erdos685.erdos_685.variants.trivial_lower_bound`

Textbook result, proved here.

> For $1 \leq k \leq n - 1$ the number of distinct prime divisors of $\binom{n}{k}$ satisfies
> $$\omega\left(\binom{n}{k}\right) \geq \frac{\log \binom{n}{k}}{\log n}.$$

```lean
theorem erdos_685.variants.trivial_lower_bound :
    ∀ n k : ℕ, 0 < k → k < n →
      Real.log (n.choose k : ℝ) / Real.log (n : ℝ) ≤ (ω (n.choose k) : ℝ)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/685.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/685.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/685.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/685.lean)
- [erdosproblems.com/685](https://www.erdosproblems.com/685)
