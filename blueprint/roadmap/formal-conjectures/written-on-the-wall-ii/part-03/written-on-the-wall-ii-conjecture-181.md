---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture181.conjecture181
statement: formalized
---

# Written on the Wall II - Conjecture 181

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> The expression `deg_avg(B(G²))` is formalized by measuring degrees in `G²`,
> the graph whose maximum-eccentricity vertices induce `B(G²)`.
>
> The conjecture is false for the triangular graph `T(7) = L(K₇)`: it has at
> most 16 leaves in a spanning tree, largest induced bipartite subgraph order 6,
> and independence number 3. Its square is `K₂₁`, whose vertices all have
> degree 20, so the claimed inequality would give `22 ≥ 23`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture181.conjecture181`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/3bfa33d7470055a9a11d9ffde29186245dc3a329/lean/GraphConjecture181.lean#L1-L381](https://github.com/Kuberwastaken/c5-k4/blob/3bfa33d7470055a9a11d9ffde29186245dc3a329/lean/GraphConjecture181.lean#L1-L381).

> WOWII Conjecture 181 asked whether every nontrivial finite connected simple
> graph `G` satisfies
>
> `Ls G + b G ≥ G.indepNum + deg_avg(B(G²))`.
>
> The answer is no, witnessed by `T(7) = L(K₇)`.

```lean
theorem conjecture181 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] [Nontrivial V]
      (G : SimpleGraph V) [DecidableRel G.Adj], G.Connected →
        Ls G + b G ≥ G.indepNum + squarePeripheryAverage G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture181.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
