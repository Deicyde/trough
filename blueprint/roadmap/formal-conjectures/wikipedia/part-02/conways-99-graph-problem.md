---
declaration: lemma
origin: cited
lean: Conway99Graph.completeGraphIsClique, Conway99Graph.completeGraph_cliqueSet, Conway99Graph.conway99Graph
statement: formalized
---

# Conway's 99-graph problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem)

*Quoted from [FormalConjectures/Wikipedia/Conway99Graph.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Conway99Graph.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 textbook results. It also has 3 test statements and 1 API statement, counted here but not shown.

## `Conway99Graph.completeGraphIsClique`

Textbook result, proved here.

> A finset of vertices in a complete graph is always a clique.

```lean
lemma completeGraphIsClique (s : Finset V) : (⊤ : SimpleGraph V).IsClique s
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/Conway99Graph.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Conway99Graph.lean#L38).

## `Conway99Graph.completeGraph_cliqueSet`

Textbook result, proved here.

> The only clique of size `n` in a complete graph on `n` vertices is the entire set of vertices.

```lean
lemma completeGraph_cliqueSet :
    (⊤ : SimpleGraph V).cliqueSet (Fintype.card V) = {Set.univ.toFinset}
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/Conway99Graph.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Conway99Graph.lean#L45).

## `Conway99Graph.conway99Graph`

Open: stated without proof.

> Does there exist an undirected graph with 99 vertices, in which each two adjacent vertices have
> exactly one common neighbor, and in which each two non-adjacent vertices have exactly two common
> neighbors?
> Equivalently, every edge should be part of a unique triangle and every non-adjacent pair should be
> one of the two diagonals of a unique 4-cycle.
> The first condition is equivalent to being locally linear.

```lean
theorem conway99Graph : ∃ G : SimpleGraph (Fin 99),
    G.LocallyLinear ∧ NonEdgesAreDiagonals G
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/Conway99Graph.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Conway99Graph.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Conway99Graph.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Conway99Graph.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem)
