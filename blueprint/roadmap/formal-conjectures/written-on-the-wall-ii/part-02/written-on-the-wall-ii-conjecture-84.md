---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture84.conjecture84
statement: formalized
---

# Written on the Wall II - Conjecture 84

> **Verbatim statement (WOWII #84, status O):**
> > If G is a simple connected graph, then tree(G) ≥ 2 rad(G) / δ(G)
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj84
>
> Here `δ(G)` is the **minimum degree** of `G` (lowercase delta in the WOWII
> HTML, rendered as `<font face="Symbol">d</font>`), not the average distance.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WrittenOnTheWallII.GraphConjecture84.conjecture84`

Open: stated without proof.

> WOWII [Conjecture 84](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj84)
> (status O):
>
> For a simple connected graph `G` with positive minimum degree,
> `tree(G) ≥ 2 · rad(G) / δ(G)`,
> where `tree(G)` is the number of vertices in a largest induced subtree,
> `rad(G)` is the radius, and `δ(G) = G.minDegree` is the minimum degree.
>
> The hypothesis `0 < G.minDegree` follows from connectedness on a nontrivial
> vertex set, but is stated explicitly so the theorem reads as a real-valued
> inequality without `x / 0` corner cases.

```lean
theorem conjecture84 (G : SimpleGraph α) [DecidableRel G.Adj]
    (h : G.Connected) (hδ : 0 < G.minDegree) :
    2 * (G.radius.toNat : ℝ) / (G.minDegree : ℝ) ≤ (largestInducedTreeSize G : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture84.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
