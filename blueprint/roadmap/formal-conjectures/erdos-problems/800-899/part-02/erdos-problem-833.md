---
declaration: theorem
origin: cited
lean: Erdos833.erdos_833
statement: formalized
---

# Erdős Problem 833

> *References:*
> - [erdosproblems.com/833](https://www.erdosproblems.com/833)
> - [ErLo75] Erdős, P. and Lovász, L., Problems and results on {$3$}-chromatic hypergraphs and some
>   related questions. (1975), 609--627.

*Quoted from [FormalConjectures/ErdosProblems/833.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/833.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/833](https://www.erdosproblems.com/833).

The file states 1 research or textbook statement: 1 solved.

## `Erdos833.erdos_833`

Solved: stated here without proof.

> Does there exist an absolute constant $c>0$ such that, for all $r\geq 2$, in any $r$-uniform
> hypergraph with chromatic number $3$ there is a vertex contained in at least $(1+c)^r$ many edges?
>
> This was solved by Erdős and Lovász [ErLo75], who proved in particular that there is a vertex
> contained in at least $\frac{2^{r-1}}{4r}$ many edges.

```lean
theorem erdos_833 :
    ∃ c : ℝ, 0 < c ∧ ∀ r : ℕ, 2 ≤ r →
    ∀ (n : ℕ) (H : Finset (Finset (Fin n))),
      H.IsUniform r → H.HasHypergraphChromaticNumber 3 →
        ∃ v : Fin n, (1 + c) ^ r ≤ (H.hypergraphDegree v : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/833.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/833.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/833.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/833.lean)
- [erdosproblems.com/833](https://www.erdosproblems.com/833)
