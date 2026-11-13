---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture96.conjecture96
statement: formalized
---

# Written on the Wall II - Conjecture 96

> **Verbatim statement (WOWII #96, status O):**
> > If G is a simple connected graph, then α(G) ≤ 1 + minimum dist_even(v)*(maximum of λ(v) -1)
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj96
>
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WrittenOnTheWallII.GraphConjecture96.conjecture96`

Open: stated without proof.

> WOWII [Conjecture 96](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G` on at least two vertices,
> `α(G) ≤ 1 + min_v distEven(v) · (max_v l(v) - 1)`
> where `α(G) = G.indepNum` is the independence number,
> `distEven(v)` is the number of vertices at even distance from `v`, and
> `max_v l(v)` is the maximum independence number of a vertex neighbourhood.
>
> We record the nontrivial-graph version: the literal source inequality fails on $K_1$,
> where the independence number and even-distance count are both one, but the maximum
> local independence number is zero, giving $1 ≤ 0$.

```lean
theorem conjecture96 (G : SimpleGraph α) (h : G.Connected) :
    let minDistEven := (Finset.univ.image (distEven G)).min' (by simp)
    let maxL := (Finset.univ.image (fun v => indepNeighborsCard G v)).max' (by simp)
    (G.indepNum : ℝ) ≤ 1 + (minDistEven : ℝ) * ((maxL : ℝ) - 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture96.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
