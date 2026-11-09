---
declaration: theorem
origin: cited
lean: Erdos23.erdos_23.variants.n5, Erdos23.erdos_23.variants.n5_tight, Erdos23.erdos_23
statement: formalized
---

# Erdős Problem 23

> *References:*
> * [erdosproblems.com/23](https://www.erdosproblems.com/23)
> * [OEIS A389646](https://oeis.org/A389646)
> * [Balogh-Clemen-Lidicky, Max Cuts in Triangle-free Graphs](https://arxiv.org/abs/2103.14179)
> * [McKay, Extremal graphs for bipartization of triangle-free graphs](https://users.cecs.anu.edu.au/~bdm/data/graphs.html)

*Quoted from [FormalConjectures/ErdosProblems/23.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/23.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/23](https://www.erdosproblems.com/23).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 3 test statements, counted here but not shown.

## `Erdos23.erdos_23.variants.n5`

Solved: stated here without proof.

> Every triangle-free graph on $25$ vertices can be made bipartite by removing at most $25$
> edges.
>
> This is the $n = 5$ case of Erdős Problem 23.  It follows from the high-density range of
> Balogh-Clemen-Lidicky together with McKay's complete catalogue of the 23-vertex extremal
> graphs for bipartization of triangle-free graphs.

```lean
theorem erdos_23.variants.n5 :
    ∀ (G : SimpleGraph (Fin 25)), G.CliqueFree 3 → ∃ (H : SimpleGraph (Fin 25)),
        H ≤ G ∧ H.IsBipartite ∧ (G.edgeFinset \ H.edgeFinset).card ≤ 25
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/23.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/23.lean#L80).

## `Erdos23.erdos_23.variants.n5_tight`

Solved: stated here without proof.

> There exists a triangle-free graph on $25$ vertices such that at least $25$ edges must be
> removed to make it bipartite.  The balanced blow-up of $C_5$ with five parts of size $5$
> witnesses this.

```lean
theorem erdos_23.variants.n5_tight :
    ∃ (G : SimpleGraph (Fin 25)), G.CliqueFree 3 ∧ ∀ (H : SimpleGraph (Fin 25)),
        H ≤ G → H.IsBipartite → 25 ≤ (G.edgeFinset \ H.edgeFinset).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/23.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/23.lean#L92).

## `Erdos23.erdos_23`

Open: stated without proof.

> Can every triangle-free graph on $5n$ vertices be made bipartite by deleting at most $n^2$ edges?

```lean
theorem erdos_23 :
    ∀ (n : ℕ) (V : Type) [Fintype V], Fintype.card V = 5 * n →
      ∀ (G : SimpleGraph V), G.CliqueFree 3 →
        ∃ (H : SimpleGraph V),
          H ≤ G ∧ H.IsBipartite ∧ (G.edgeFinset \ H.edgeFinset).card ≤ n^2
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/23.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/23.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/23.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/23.lean)
- [erdosproblems.com/23](https://www.erdosproblems.com/23)
