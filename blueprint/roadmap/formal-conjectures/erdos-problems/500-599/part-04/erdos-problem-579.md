---
declaration: theorem
origin: cited
lean: Erdos579.erdos_579, Erdos579.erdos_579.variants.ehss_large_delta
statement: formalized
---

# Erdős Problem 579

> *References:*
> - [erdosproblems.com/579](https://www.erdosproblems.com/579)
> - [EHSS83] P. Erdős, A. Hajnal, V. T. Sós and E. Szemerédi, *More results on Ramsey–Turán
>   type problems*, Combinatorica **3** (1983), 69–81.

*Quoted from [FormalConjectures/ErdosProblems/579.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/579.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/579](https://www.erdosproblems.com/579).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos579.erdos_579`

Open: stated without proof.

> Let $\delta > 0$. If $n$ is sufficiently large and $G$ is a graph on $n$ vertices with no
> $K_{2,2,2}$ (the octahedron) and at least $\delta n^2$ edges, must $G$ contain an independent
> set of size $\gg_\delta n$?
>
> This is a problem of Erdős, Hajnal, Sós, and Szemerédi [EHSS83]. It is **open**; they proved
> the statement for $\delta > 1/8$ (see `erdos_579.variants.ehss_large_delta`), and the
> difficulty is to push the edge-density threshold down to an arbitrary $\delta > 0$.
>
> Here $K_{2,2,2}$ is the complete tripartite graph with all parts of size $2$, encoded as
> `completeMultipartiteGraph (fun _ : Fin 3 => Fin 2)`; "contains no $K_{2,2,2}$" is expressed
> via `SimpleGraph.Free`.

```lean
theorem erdos_579 :
    ∀ δ : ℝ, 0 < δ → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), octahedron.Free G →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          c * n ≤ (G.indepNum : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/579.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/579.lean#L55).

## `Erdos579.erdos_579.variants.ehss_large_delta`

Solved: stated here without proof.

> The partial result of Erdős, Hajnal, Sós, and Szemerédi [EHSS83]: the statement of
> `erdos_579` holds whenever the edge-density coefficient exceeds $1/8$. That is, for every
> $\delta > 1/8$ there is a $c > 0$ such that for all sufficiently large $n$, every
> $K_{2,2,2}$-free graph $G$ on $n$ vertices with at least $\delta n^2$ edges has an independent
> set of size at least $c n$.

```lean
theorem erdos_579.variants.ehss_large_delta (δ : ℝ) (hδ : 1 / 8 < δ) :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      ∀ G : SimpleGraph (Fin n), octahedron.Free G →
        δ * (n : ℝ) ^ 2 ≤ G.edgeFinset.card →
          c * n ≤ (G.indepNum : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/579.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/579.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/579.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/579.lean)
- [erdosproblems.com/579](https://www.erdosproblems.com/579)
