---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture91.conjecture91
statement: formalized
---

# Written on the Wall II - Conjecture 91

> **Verbatim statement (WOWII #91, status O):**
> > If G is a simple connected graph, then b(G) ≤ 1 + f(G) * (CEIL[average of λ(v) ])/2
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj91
>
> This conjecture is **false**: Max Talwar found an 11-vertex counterexample
> (graph6 `JBza_CB?wF_`): take `K₃,₃` minus an edge together with a `K₅`, joined
> by two edges into one `K₅`-vertex. There the average neighbourhood
> independence number is exactly `2`, the largest induced forest has `6` vertices,
> and the largest induced bipartite subgraph has `8`, so the conjectured bound
> reads `8 ≤ 1 + 6·⌈2⌉/2 = 7`.
>
> *References:*
> - [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> - [Counterexample certificate for WOWII 91 (Max Talwar)](https://github.com/maxtalwar/wowii91-counterexample/releases/tag/v1.0.0)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture91.conjecture91`

Solved: stated here without proof.

> WOWII [Conjecture 91](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
> (disproved, 2026):
>
> For a simple connected graph `G`,
> `b(G) ≤ 1 + f(G) · ⌈avg_v l(v)⌉ / 2`
> where `b(G)` is the largest induced bipartite subgraph size,
> `f(G) = largestInducedForestSize G` is the largest induced forest size, and
> `avg_v l(v) = l G` is the average independence number of the neighbourhoods.
>
> Disproved by an 11-vertex counterexample (Max Talwar, 2026; graph6
> `JBza_CB?wF_`) with `b(G) = 8`, `f(G) = 6` and `l G = 2`, violating
> `8 ≤ 1 + 6·⌈2⌉/2 = 7`.

```lean
theorem conjecture91 :
    ¬ ∀ {α : Type*} [Fintype α] [DecidableEq α] [Nontrivial α],
      ∀ (G : SimpleGraph α) (_ : G.Connected),
        b G ≤ 1 + (G.largestInducedForestSize : ℝ) * ⌈l G⌉ / 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/WrittenOnTheWallII/GraphConjecture91.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
