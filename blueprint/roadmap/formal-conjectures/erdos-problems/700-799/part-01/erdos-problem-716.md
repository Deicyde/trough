---
declaration: theorem
origin: cited
lean: Erdos716.erdos_716
statement: formalized
---

# Erdős Problem 716

> *References:*
> - [erdosproblems.com/716](https://www.erdosproblems.com/716)
> - [BES73] Brown, W. G. and Erdős, P. and S\'os, V. T., Some extremal problems on {$r$}-graphs.
>   (1973), 53--63.
> - [RuSz78] Ruzsa, I. Z. and Szemer\'{e}di, E., Triple systems with no six points carrying three
>   triangles. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II (1978), 939-945.

*Quoted from [FormalConjectures/ErdosProblems/716.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/716.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/716](https://www.erdosproblems.com/716).

The file states 1 research or textbook statement: 1 solved.

## `Erdos716.erdos_716`

Solved: stated here without proof.

> Let $\mathcal{F}$ be the family of all $3$-uniform hypergraphs with $6$ vertices and $3$ $3$-edges.
> Is it true that
>
> $$\mathrm{ex}_3(n,\mathcal{F})=o(n^2)?$$
>
> The answer is yes, proved by Ruzsa and Szemerédi [RuSz78] (this is known as the Ruzsa-Szemerédi
> problem).

```lean
theorem erdos_716 :
    (fun n ↦ (Hypergraph.configurationExtremalNumber n 3 6 3 : ℝ)) =o[atTop]
      (fun n ↦ (n : ℝ) ^ 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/716.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/716.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/716.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/716.lean)
- [erdosproblems.com/716](https://www.erdosproblems.com/716)
