---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture172.conjecture172
statement: formalized
---

# Written on the Wall II - Conjecture 172

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> The conjecture is false for the graph `D₉`, formed from two triangles by
> joining distinguished vertices with a path of nine edges. It has at most four
> leaves in a spanning tree. Its peripheral vertices have degree two, while the
> two maximum-degree vertices of its square are at distance seven in the
> original graph, so the claimed inequality would give `4 ≥ 8`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture172.conjecture172`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/a948106ad2d2a5d291b6b99575fe78bf373e7e02/lean/GraphConjecture172.lean#L1-L384](https://github.com/Kuberwastaken/c5-k4/blob/a948106ad2d2a5d291b6b99575fe78bf373e7e02/lean/GraphConjecture172.lean#L1-L384).

> WOWII Conjecture 172 asked whether every nontrivial finite connected simple
> graph `G` satisfies
> `Ls G ≥ -1 + Δ(B(G)) + dist_min(G, M(G²))`.
> The answer is no, witnessed by `D₉`.

```lean
theorem conjecture172 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] [Nontrivial V]
      (G : SimpleGraph V) [DecidableRel G.Adj], G.Connected →
        Ls G ≥ (-1 : ℝ) + peripheryMaxDegree G +
          distMin G (squareMaximumDegreeVertices G)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture172.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
