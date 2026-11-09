---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture160.conjecture160
statement: formalized
---

# Written on the Wall II - Conjecture 160

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> ## Definitions
>
> For a vertex $v$ in $G$, **$T(v)$** is the number of triangles incident to $v$:
> $$T(v) = |\{\{u, w\} \subseteq N(v) \mid u \sim w\}|$$
> i.e., the number of pairs of neighbors of $v$ that are themselves adjacent.
>
> The invariant `maxTrianglesAtVertex G` is the maximum of $T(v)$ over all vertices.
>
> Conjecture 160 uses both $\max_v T(v)$ and $\chi_{C_4}(G)$, the $C_4$-free
> characteristic function: it is `1` when $G$ contains no cycle of length four
> and `0` otherwise. The cycle need not be induced. These invariants lower-bound
> the WOWII invariant $L_s(G)$, the maximum number of leaves over all spanning
> trees of $G$ (exposed as `SimpleGraph.Ls G : ℝ`).
>
> The earlier formalization used the number of induced four-cycles. The historical
> conjecture instead uses this binary $C_4$-free indicator.
>
> **Provenance.** Statement corrected by Dominic Dabish.

*Quoted from [FormalConjectures/WrittenOnTheWallII/160.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/160.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture160.conjecture160`

Solved: stated here; a Lean proof is at [https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/f0d70dfa13f92a4b631289e44487690833be8798/WOWII160AltProof.lean#L714](https://github.com/anagnorisis2peripeteia/formal-conjectures/blob/f0d70dfa13f92a4b631289e44487690833be8798/WOWII160AltProof.lean#L714).

> WOWII [Conjecture 160](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph $G$,
> $L_s(G) \ge \max_v l(v) + \max_v T(v) \cdot \chi_{C_4}(G)$
> where:
>
> - $L_s(G) = \mathrm{SimpleGraph.Ls}\, G$ is the maximum number of leaves over all
>   spanning trees of $G$,
> - $\max_v l(v)$ is the maximum local independence number over vertices,
> - $\max_v T(v)$ is the maximum number of triangles incident to any vertex,
> - $\chi_{C_4}(G)$ is `1` if $G$ has no cycle of length four and `0` otherwise.
>
> A formal proof uses the $C_4$-free neighborhood identity $d(v) = \lambda(v) + T(v)$
> with a star/geodesic case analysis, routed through the connected-seed
> spanning-tree bound developed for Conjecture 2. An independent second proof,
> via a closest maximizer pair joined by a shortest path, is linked from the
> pull request that recorded the solution.

```lean
theorem conjecture160 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let maxL := (Finset.univ.image (indepNeighborsCard G)).max' (by simp)
    let maxT := maxTrianglesAtVertex G
    let cC4 : ℕ := if ∃ v : α, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = 4 then 0 else 1
    (maxL : ℝ) + (maxT : ℝ) * (cC4 : ℝ) ≤ Ls G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/160.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/160.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/160.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/160.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
