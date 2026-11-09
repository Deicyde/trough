---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture176.conjecture176
statement: formalized
---

# Written on the Wall II - Conjecture 176

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> The conjecture is false for the graph `D₇`, formed from two triangles by
> joining distinguished vertices with a path of seven edges. It has at most four
> leaves in a spanning tree and largest induced bipartite subgraph order ten.
> The two maximum-degree vertices of its square are at distance five in the
> original graph, so the claimed inequality would give `14 ≥ 17`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture176.conjecture176`

Solved: stated here; a Lean proof is at [https://github.com/Kuberwastaken/c5-k4/blob/b0ba2b9206176b4fc30bd633de206ac230b4e01f/lean/GraphConjecture176.lean#L1-L377](https://github.com/Kuberwastaken/c5-k4/blob/b0ba2b9206176b4fc30bd633de206ac230b4e01f/lean/GraphConjecture176.lean#L1-L377).

> WOWII Conjecture 176 asked whether every nontrivial finite connected simple
> graph `G` satisfies
> `Ls(G) + b(G) ≥ n(G) + dist_min(G, M(G²))`.
> The answer is no, witnessed by `D₇`.

```lean
theorem conjecture176 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] [Nontrivial V]
      (G : SimpleGraph V) [DecidableRel G.Adj], G.Connected →
        Ls G + b G ≥ (Fintype.card V : ℝ) +
          distMin G (squareMaximumDegreeVertices G)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture176.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
