---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture20.conjecture20
statement: formalized
---

# Written on the Wall II - Conjecture 20

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [AKS87] N. Alon, J. Kahn and P. D. Seymour, [Large Induced Degenerate Subgraphs](https://doi.org/10.1007/BF01788542), Graphs and Combinatorics 3 (1987), 203–211.
> - [Li26] Wentao Li, [Lean proof of WOWII 20](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/proofs/WOWII20/PROOF.md), 2026.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture20.conjecture20`

Solved: stated here; a Lean proof is at [https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII20.lean#L499](https://github.com/VictorLiwentao/lean-graph-proofs/blob/9ce66be23570e0a9c8a6ae3f19f52e642878a8a9/LeanGraphProofs/WOWII20.lean#L499).

> WOWII [Conjecture 20](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, `b(G) ≥ n(G) / ⌊deg_avg(G)⌋`, where `b(G)` is
> the size of a largest induced bipartite subgraph, `n(G)` is the number of vertices,
> and `deg_avg(G) = (∑ v, deg(v)) / n(G)` is the average degree.
>
> Follows from the weighted induced-subgraph bound of Alon, Kahn and Seymour [AKS87].
> Lean formalization by Wentao Li, with AI assistance; see [Li26].

```lean
theorem conjecture20 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let deg_avg : ℝ := (∑ v : α, (G.degree v : ℝ)) / (Fintype.card α : ℝ)
    (Fintype.card α : ℝ) / (⌊deg_avg⌋ : ℝ) ≤ (b G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture20.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
