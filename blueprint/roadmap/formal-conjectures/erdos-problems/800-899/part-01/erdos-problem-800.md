---
declaration: theorem
origin: cited
lean: Erdos800.erdos_800
statement: formalized
---

# Erdős Problem 800

> *References:*
> - [erdosproblems.com/800](https://www.erdosproblems.com/800)
> - [Al94] Alon, N., Subdivided graphs have linear Ramsey numbers. J. Graph Theory (1994), 343-347.

*Quoted from [FormalConjectures/ErdosProblems/800.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/800.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/800](https://www.erdosproblems.com/800).

The file states 1 research or textbook statement: 1 solved.

## `Erdos800.erdos_800`

Solved: stated here without proof.

> If $G$ is a graph on $n$ vertices which has no two adjacent vertices of degree $\geq 3$ then
>
> $$R(G)\ll n,$$
>
> where the implied constant is absolute.
>
> A problem of Burr and Erdős. Solved in the affirmative by Alon [Al94].

```lean
theorem erdos_800 :
    ∃ C > (0 : ℝ), ∀ (n : ℕ) (V : Type) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj],
      Fintype.card V = n →
      (∀ u v, G.Adj u v → ¬(3 ≤ G.degree u ∧ 3 ≤ G.degree v)) →
      (SimpleGraph.diagonalGraphRamsey G : ℝ) ≤ C * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/800.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/800.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/800.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/800.lean)
- [erdosproblems.com/800](https://www.erdosproblems.com/800)
