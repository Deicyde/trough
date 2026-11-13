---
declaration: theorem
origin: cited
lean: Erdos258.erdos_258, Erdos258.erdos_258.variants.monotone, Erdos258.erdos_258.variants.constant
statement: formalized
---

# Erdős Problem 258

> *References:*
> - [erdosproblems.com/258](https://www.erdosproblems.com/258)
> - [Ch26] P. Chojecki and GPT-5.4 Pro, [Erdős problem 258](https://www.ulam.ai/research/erdos258.pdf) (2026)
> - [St26] ster-oc, [Lean formalisation of Erdős problem 258](https://live.lean-lang.org/#project=mathlib-v4.28.0&url=https://gist.githubusercontent.com/ster-oc/2b7adcf9d753cf6e29d782f7374cc57e/raw/689a8483895cbe147634dfbf2d7b1db93a3b5b5f/Erdos258.lean) (2026)

*Quoted from [FormalConjectures/ErdosProblems/258.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/258.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/258](https://www.erdosproblems.com/258).

The file states 3 research or textbook statements: 3 solved.

## `Erdos258.erdos_258`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/ster-oc/2b7adcf9d753cf6e29d782f7374cc57e/raw/689a8483895cbe147634dfbf2d7b1db93a3b5b5f/Erdos258.lean](https://gist.githubusercontent.com/ster-oc/2b7adcf9d753cf6e29d782f7374cc57e/raw/689a8483895cbe147634dfbf2d7b1db93a3b5b5f/Erdos258.lean).

> Let $a_n \to \infty$ be a sequence of non-zero natural numbers. Is
> $\sum_n \frac{d(n)}{(a_1 ... a_n)}$ irrational, where $d(n)$ is the number of divisors of $n$?
>
> This was proved affirmatively by Chojecki and GPT-5.4 Pro [Ch26], and formalised in Lean
> by ster-oc [St26].

```lean
theorem erdos_258 : ∀ (a : ℕ → ℕ), (∀ n, 2 ≤ a n) →
    Filter.Tendsto a Filter.atTop Filter.atTop →
    Irrational (∑' (n : ℕ), ((n + 1).divisors.card / ∏ i ∈ Finset.Icc 1 (n + 1), a i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/258.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/258.lean#L43).

## `Erdos258.erdos_258.variants.monotone`

Solved: stated here without proof.

> Let $2 \leq a_1 \leq a_2 \leq \cdots$ be a monotone sequence with $a_n \to \infty$.
> Is $\sum_n \frac{d(n)}{a_1 \cdots a_n}$ irrational, where $d(n)$ is the number of divisors of $n$?
>
> Solution: True (proved by Erdős and Straus [ErSt71], Lemma 2.2 and Theorem 2.13).

```lean
theorem erdos_258.variants.monotone :
    ∀ (a : ℕ → ℕ), (∀ n, 2 ≤ a n) → Monotone a →
    Filter.Tendsto a Filter.atTop Filter.atTop →
    Irrational (∑' (n : ℕ), ((n + 1).divisors.card / ∏ i ∈ Finset.Icc 1 (n + 1), a i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/258.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/258.lean#L56).

## `Erdos258.erdos_258.variants.constant`

Solved: stated here; a Lean proof is at [https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L112-L117](https://github.com/wcook04/plectis-erdos-lean/blob/c4eab2571b4692ee9c08d3ec138176f7fbfa09a9/verification/FCMergedIntegerAdapters/research/adapters/FormalConjecturesAdapter.lean#L112-L117).

> Is $\sum_n \frac{d(n)}{t^n}$ irrational, where $t ≥ 2$ is an integer.
>
> Solution: True (proved by Erdős, see Erdős Problems website)

```lean
theorem erdos_258.variants.constant : ∀ t ≥ (2 : ℕ),
    Irrational (∑' (n : ℕ), ((n + 1).divisors.card / t^(n + 1)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/258.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/258.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/258.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/258.lean)
- [erdosproblems.com/258](https://www.erdosproblems.com/258)
