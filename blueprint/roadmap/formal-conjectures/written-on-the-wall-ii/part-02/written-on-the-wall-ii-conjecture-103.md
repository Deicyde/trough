---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture103.conjecture103
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 103

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `WrittenOnTheWallII.GraphConjecture103.conjecture103`

Proved here.

> WOWII [Conjecture 103](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $\alpha(G) \le \lfloor b(G) - \ln(\mathrm{ecc\_avg}(G)) \rfloor$
> where $\alpha(G) = G.\mathrm{indepNum}$ is the independence number,
> $b(G)$ is the largest induced bipartite subgraph size, and
> $\mathrm{ecc\_avg}(G) = G.\mathrm{averageEccentricity}$ is the average
> eccentricity of $G$. Uses `Real.log` (natural logarithm).
>
> This conjecture is false. The graph `wowii103Counterexample` has independence number $9$,
> largest induced bipartite subgraph size $10$, and average eccentricity $30/11$. Since
> $1 < \ln(30/11) < 2$, the proposed upper bound is $8$.

```lean
theorem conjecture103 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) (_h : G.Connected),
      (G.indepNum : ℝ) ≤ ⌊b G - Real.log (averageEccentricity G)⌋
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture103.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
