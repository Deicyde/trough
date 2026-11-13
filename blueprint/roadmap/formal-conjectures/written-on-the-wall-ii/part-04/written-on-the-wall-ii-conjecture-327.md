---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture327.conjecture327
statement: formalized
---

# Written on the Wall II - Conjecture 327

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture327.conjecture327`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/6e85aabe821e6ddf718d050a5bd8f19a48e4f2d9/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean#L233](https://github.com/mo271/formal-conjectures/blob/6e85aabe821e6ddf718d050a5bd8f19a48e4f2d9/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean#L233).

> WOWII [Conjecture 327](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> Let `G` be a simple connected graph. If `3 · γ(G) = γ_i(G)`, then `G` is well
> totally dominated, where `γ(G)` is the domination number of `G` and `γ_i(G)` is
> the independent domination number of `G`.
>
> **Proof Sketch:**
> The conjecture states that if $3\gamma(G) = i(G)$ for a connected graph $G$, then $G$ is well totally dominated.
> However, this conjecture is **FALSE**.
>
> **Counterexample:**
> Consider a graph $G$ with 12 vertices: $u, v, a_0, a_1, a_2, a_3, a_4, b_0, b_1, b_2, b_3, b_4$.
> The edges are:
> - $(u, v)$
> - $(u, a_i)$ for all $i \in \{0, 1, 2, 3, 4\}$
> - $(v, b_i)$ for all $i \in \{0, 1, 2, 3, 4\}$
> - $(a_0, b_3), (a_1, b_3), (a_2, b_0), (a_3, b_0), (a_4, b_3), (a_4, b_4)$
>
> Properties of $G$:
> 1. **Connected**: Yes, path exists between any two vertices through $u$ and $v$.
> 2. **Domination Number $\gamma(G)$**: The set $\{u, v\}$ dominates all vertices. Since there is no universal vertex, $\gamma(G) = 2$.
> 3. **Independent Domination Number $i(G)$**: The minimum independent dominating set has size 6 (e.g., $\{u, b_0, b_1, b_2, b_3, b_4\}$). Thus $i(G) = 6$.
> 4. **Condition**: $3 \gamma(G) = 3 \times 2 = 6 = i(G)$. The condition holds.
> 5. **Well Totally Dominated**: A graph is well totally dominated if all minimal total dominating sets have the same size.
>    - $\{u, v\}$ is a minimal total dominating set of size 2.
>    - $\{v, b_0, b_3\}$ is a minimal total dominating set of size 3.
>    Since $2 \neq 3$, $G$ is NOT well totally dominated.
>
> The counterexample has been found by Moritz Firsching and Goran Žužić using an
> experimental pipeline.

```lean
theorem conjecture327 :
    ¬ ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj] (_hG : G.Connected)
      (_h : 3 * G.dominationNumber = G.indepDominationNumber),
      IsWellTotallyDominated G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture327.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
