---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture65.conjecture65
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 65

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Counterexample
>
> The conjecture is false. Start with the path $v_0-v_1-\cdots-v_{12}$ and attach one
> triangle at $v_1$ and another at $v_{11}$. The resulting graph has $17$ vertices.
> Its Graph_6 string is `PhCGGC@?G?_@?@O?G?G?G?@C`.
> Its only minimum-degree vertices are $v_0$ and $v_{12}$, at distance $12$, while its
> only maximum-degree vertices are $v_1$ and $v_{11}$, at distance $10$. Thus the
> conjectured lower bound is $12 + \lceil 10/3 \rceil = 16$.
>
> Every induced forest must omit at least one vertex from each of the two vertex-disjoint
> triangles, so it has at most $15$ vertices. Conversely, deleting one non-path vertex
> from each triangle leaves a tree on $15$ vertices.

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 8 API statements, counted here but not shown.

## `WrittenOnTheWallII.GraphConjecture65.conjecture65`

Proved here.

> WOWII [Conjecture 65](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/):
>
> Does every simple connected graph $G$ satisfy
> $f(G) \ge \operatorname{dist\_min}(A) + \lceil \operatorname{dist\_min}(M) / 3 \rceil$,
> where $A$ is the set of minimum-degree vertices, $M$ is the set of maximum-degree vertices,
> and $\operatorname{dist\_min}(S)$ is the minimum distance between two distinct vertices of $S$
> (see `distMin`).
>
> The answer is no. `Counterexample.graph` has a conjectured lower bound of $16$, but every
> induced forest in it has at most $15$ vertices.

```lean
theorem conjecture65 :
    ¬ ∀ (α : Type) [Fintype α] [DecidableEq α] [Nontrivial α]
      (G : SimpleGraph α) [DecidableRel G.Adj] (_hG : G.Connected),
      let A : Set α := {v | G.degree v = G.minDegree}
      let M : Set α := {v | G.degree v = G.maxDegree}
      (distMin G A : ℝ) + ⌈(distMin G M : ℝ) / 3⌉ ≤
        (G.largestInducedForestSize : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean, line 175](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean#L175).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture65.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
