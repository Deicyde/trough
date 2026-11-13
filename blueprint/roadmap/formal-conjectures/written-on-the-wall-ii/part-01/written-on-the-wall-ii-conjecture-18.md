---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture18.conjecture18
statement: formalized
---

# Written on the Wall II - Conjecture 18

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture18.conjecture18`

Solved: stated here without proof.

> WOWII [Conjecture 18](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$, the size $b(G)$ of a largest induced bipartite
> subgraph satisfies
> $b(G) \ge \alpha(G) + \lceil \sqrt{\mathrm{dist}_{\max}(M)} \rceil$,
> where $\alpha(G)$ is the independence number, $M$ is the set of maximum-degree
> vertices, and $\mathrm{dist}_{\max}(M) = \max\{\mathrm{dist}_G(u,v) \mid u, v \in M\}$
> is the maximum distance between two maximum-degree vertices (DeLaVina's
> `dist_max(M)`). Proven by Benny John (Feb. 2006), generalizing Schindl's proof
> of conjecture 17.

```lean
theorem conjecture18 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let M : Set α := {v | G.degree v = G.maxDegree}
    (G.indepNum : ℝ) + ⌈Real.sqrt (distMaxSet G M : ℝ)⌉ ≤ b G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture18.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
