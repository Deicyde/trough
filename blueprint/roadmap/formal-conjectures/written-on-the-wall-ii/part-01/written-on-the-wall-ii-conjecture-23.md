---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture23.conjecture23
statement: formalized
---

# Written on the Wall II - Conjecture 23

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture23.conjecture23`

Solved: stated here without proof.

> WOWII [Conjecture 23](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`, `b(G) ≥ ⌊α(G) + dist_avg(M) / 2⌋`, where `b(G)` is
> the size of a largest induced bipartite subgraph, `α(G)` is the independence number,
> `M` is the set of maximum-degree vertices, and `dist_avg(M)` is the average distance
> between distinct vertices of `M`.
>
> This conjecture is false; there is a counterexample with `b(G) = 19`, `α(G) = 15`,
> and `dist_avg(M) = 10`.

```lean
theorem conjecture23 :
  ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
    (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected),
    let M : Set α := {v | G.degree v = G.maxDegree}
    ⌊(G.indepNum : ℝ) + distAvgSet G M / 2⌋ ≤ (b G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture23.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
