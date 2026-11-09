---
declaration: theorem
origin: cited
lean: Erdos836.erdos_836.parts.i, Erdos836.erdos_836.parts.ii
statement: formalized
---

# Erdős Problem 836

> *References:*
> - [erdosproblems.com/836](https://www.erdosproblems.com/836)
> - [ErLo75] Erdős, P. and Lovász, L., Problems and results on {$3$}-chromatic hypergraphs and some
>   related questions. (1975), 609--627.
> - [Pr26] Price, L., *A Linear Intersection Bound*. (2026).

*Quoted from [FormalConjectures/ErdosProblems/836.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/836.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/836](https://www.erdosproblems.com/836).

The file states 2 research or textbook statements: 2 solved.

## `Erdos836.erdos_836.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ad12db51383ed41ec8b6b54e0ffabfa828773d38/erdos-836/Solution.lean#L33](https://github.com/linrock/math-proofs/blob/ad12db51383ed41ec8b6b54e0ffabfa828773d38/erdos-836/Solution.lean#L33).

> Let $r\geq 2$ and let $G$ be an intersecting $r$-uniform hypergraph with chromatic number
> $3$. Must $G$ contain $O(r^2)$ many vertices? Vertices are counted in the union of the edges,
> so isolated vertices are excluded.
>
> Alon has provided a counterexample to the first question: this hypergraph is intersecting,
> its chromatic number is $3$, and it has $\asymp 4^r/\sqrt{r}$ many vertices.

```lean
theorem erdos_836.parts.i :
    ¬ ∃ C : ℝ, 0 < C ∧ ∀ r : ℕ, 2 ≤ r →
    ∀ (n : ℕ) (H : Finset (Finset (Fin n))),
      H.IsUniform r → H.HasHypergraphChromaticNumber 3 → (H : Set (Finset (Fin n))).Intersecting →
        ((H.biUnion id).card : ℝ) ≤ C * (r : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/836.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/836.lean#L47).

## `Erdos836.erdos_836.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/ad12db51383ed41ec8b6b54e0ffabfa828773d38/erdos-836/Solution.lean#L41](https://github.com/linrock/math-proofs/blob/ad12db51383ed41ec8b6b54e0ffabfa828773d38/erdos-836/Solution.lean#L41).

> In an intersecting $r$-uniform hypergraph with chromatic number $3$, must there be two
> distinct edges which meet in $\gg r$ many vertices?

```lean
theorem erdos_836.parts.ii :
    ∃ c : ℝ, 0 < c ∧ ∀ r : ℕ, 2 ≤ r →
    ∀ (n : ℕ) (H : Finset (Finset (Fin n))),
      H.IsUniform r → H.HasHypergraphChromaticNumber 3 → (H : Set (Finset (Fin n))).Intersecting →
        ∃ e ∈ H, ∃ f ∈ H, e ≠ f ∧ c * r ≤ ((e ∩ f).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/836.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/836.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/836.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/836.lean)
- [erdosproblems.com/836](https://www.erdosproblems.com/836)
