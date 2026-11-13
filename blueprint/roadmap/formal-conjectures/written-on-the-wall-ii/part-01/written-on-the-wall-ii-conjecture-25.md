---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture25.conjecture25
statement: formalized
---

# Written on the Wall II - Conjecture 25

> **Verbatim statement (WOWII #25, status F):**
> > If G is a simple connected graph, then b(G) ≥ 2 CEIL[(1 + minimum of dist_even(v))/3]
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj25
>
> The WOWII page records this conjecture as disproved (status F), with the same
> counterexample as Conjecture 24.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `WrittenOnTheWallII.GraphConjecture25.conjecture25`

Solved: stated here without proof.

> WOWII [Conjecture 25](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj25)
> (status F, disproved):
>
> For every finite simple connected graph $G$,
> $b(G) ≥ 2⌈(1 + \min_v \operatorname{dist}_{\mathrm{even}}(v))/3⌉$,
> where $b(G)$ is the size of a largest induced bipartite subgraph and
> $\operatorname{dist}_{\mathrm{even}}(v)$ counts the vertices at even distance from $v$.
>
> The nontrivial vertex type excludes graphs with fewer than two vertices.
> The source gives the same counterexample as for Conjecture 24.

```lean
theorem conjecture25 :
    ¬ ∀ {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α],
      ∀ (G : SimpleGraph α) (_ : G.Connected),
        let minDistEven := (Finset.univ.image (distEven G)).min' (by simp)
        2 * ⌈(1 + (minDistEven : ℝ)) / 3⌉ ≤ (b G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture25.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
