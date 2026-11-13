---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture315.conjecture315
statement: formalized
---

# Written on the Wall II - Conjecture 315

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definitions
>
> The notions `IsTotalDominatingSet`, `IsMinimalTotalDominatingSet`,
> `IsWellTotallyDominated`, and `pendantVertices` live in
> `FormalConjecturesForMathlib.Combinatorics.SimpleGraph.GraphConjectures.WellTotallyDominated`.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture315.conjecture315`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/9ef80e1a3709ed3eda43d9ed6ff1087681621041/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean#L43](https://github.com/mo271/formal-conjectures/blob/9ef80e1a3709ed3eda43d9ed6ff1087681621041/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean#L43).

> WOWII [Conjecture 315](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> Let $G$ be a simple connected graph and let $P$ denote the set of pendant vertices
> (vertices of degree $1$). If $\alpha(G) = |P|$, then $G$ is well totally dominated.
>
> A formal proof of this conjectures has been obtained by Goran Žužić and Moritz Firsching using an
> experimental pipeline.

```lean
theorem conjecture315 (G : SimpleGraph α) [DecidableRel G.Adj] (hG : G.Connected)
    (h : G.indepNum = (pendantVertices G).card) :
    IsWellTotallyDominated G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture315.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
