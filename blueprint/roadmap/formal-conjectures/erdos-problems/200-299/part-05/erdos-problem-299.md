---
declaration: theorem
origin: cited
lean: Erdos299.erdos_299, Erdos299.erdos_299.variants.density
statement: formalized
---

# Erdős Problem 299

> *References:*
> - [erdosproblems.com/298](https://www.erdosproblems.com/298)
> - [erdosproblems.com/299](https://www.erdosproblems.com/299)
> - [Bl21] Bloom, T. F., On a density conjecture about unit fractions. arXiv:2112.03726 (2021).

*Quoted from [FormalConjectures/ErdosProblems/299.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/299.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/299](https://www.erdosproblems.com/299).

The file states 2 research or textbook statements: 2 solved.

## `Erdos299.erdos_299`

Solved: stated here; a proof in another system is at [https://github.com/b-mehta/unit-fractions/blob/master/src/final_results.lean](https://github.com/b-mehta/unit-fractions/blob/master/src/final_results.lean).

> Is there an infinite sequence $a_1 < a_2 < \dots$ such that $a_{i+1} - a_i = O(1)$ and no finite
> sum of $\frac{1}{a_i}$ is equal to 1?
>
> There does not exist such a sequence, which follows from the positive solution to
> [erdosproblems.com/298] by Bloom [Bl21].
>
> This was formalized in Lean 3 by Bloom and Mehta.

```lean
theorem erdos_299 : ¬ (∃ (a : ℕ → ℕ),
    StrictMono a ∧ (∀ n, 0 < a n) ∧
    (fun n ↦ (a (n + 1) : ℝ) - a n) =O[atTop] (1 : ℕ → ℝ) ∧
    ∀ S : Finset ℕ, ∑ i ∈ S, (1 : ℝ) / a i ≠ 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/299.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/299.lean#L46).

## `Erdos299.erdos_299.variants.density`

Solved: stated here without proof.

> The corresponding question is also false if one replaces sequences such that $a_{i+1} - a_i = O(1)$
> with sets of positive density, as follows from [Bl21].
>
> The statement is as follows:
> If $A \subset \mathbb{N}$ has positive upper density (and hence certainly if $A$ has positive
> density) then there is a finite $S \subset A$ such that $\sum_{n \in S} \frac{1}{n} = 1$.

```lean
theorem erdos_299.variants.density : ∀ (A : Set ℕ), 0 ∉ A → 0 < A.upperDensity →
    ∃ S : Finset ℕ, ↑S ⊆ A ∧ ∑ n ∈ S, (1 : ℝ) / n = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/299.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/299.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/299.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/299.lean)
- [erdosproblems.com/299](https://www.erdosproblems.com/299)
