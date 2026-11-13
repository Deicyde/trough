---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture2.conjecture2
statement: formalized
---

# Written on the Wall II - Conjecture 2

> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research
>   with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture2.conjecture2`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/alphaproof-nexus-results/blob/0647711a71183c1ea492ad60860776617ce1ea88/APNOutputs/AICollaborator/Graphs/GraphConjecture2.lean#L704](https://github.com/google-deepmind/alphaproof-nexus-results/blob/0647711a71183c1ea492ad60860776617ce1ea88/APNOutputs/AICollaborator/Graphs/GraphConjecture2.lean#L704); a Lean proof is at [https://github.com/kingcharlezz/formal-conjectures/blob/7d88e8b7946791ff53c322651f73de8d4df0ba53/FormalConjectures/WrittenOnTheWallII/Proofs/GraphConjecture2.lean#L622](https://github.com/kingcharlezz/formal-conjectures/blob/7d88e8b7946791ff53c322651f73de8d4df0ba53/FormalConjectures/WrittenOnTheWallII/Proofs/GraphConjecture2.lean#L622); a Lean proof is at [https://github.com/KitaKen1/wowii-graph-conjecture-2-lean/blob/fc6cc1f5b857e9c3f9693b98587660eb09606abc/lean/GraphConjecture2.lean#L673](https://github.com/KitaKen1/wowii-graph-conjecture-2-lean/blob/fc6cc1f5b857e9c3f9693b98587660eb09606abc/lean/GraphConjecture2.lean#L673).

> WOWII [Conjecture 2](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $Ls(G) \ge 2 \cdot (l(G) - 1)$ where $l(G)$ is the average independence number of
> the neighbourhoods of the vertices of $G$.
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763), where an informal proof is also provided.
>
> Another formal proof combines a spanning-tree leaf bound from connected domination
> with an ordered-pair double-counting argument for adjacent neighbourhoods.
>
> A third formal proof starts from a triangle-free spanning subgraph of $G$ with the maximum
> number of edges. Maximality bounds the neighbourhood independence number of each vertex by its
> degree in that subgraph; an edge whose endpoint degrees sum to at least $2 \cdot l(G)$ then
> carries a double star, which is acyclic and extends to a spanning tree with at least
> $2 \cdot (l(G) - 1)$ leaves.

```lean
theorem conjecture2 (G : SimpleGraph α) (h : G.Connected) :
  2 * (averageIndepNeighbors G - 1) ≤ Ls G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture2.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
