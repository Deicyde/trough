---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture72.conjecture72
statement: formalized
---

# Written on the Wall II - Conjecture 72

> **Verbatim statement (WOWII #72, status O):**
> > If G is a simple connected graph, then tree(G) ≥ CEIL[average of ecc(v) + maximum of λ(v) /3]
>
> **Source:** http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj72
>
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `WrittenOnTheWallII.GraphConjecture72.conjecture72`

Open: stated without proof.

> WOWII [Conjecture 72](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a simple connected graph `G`,
> $\operatorname{tree}(G) ≥ ⌈\operatorname{ecc}_{\mathrm{avg}}(G) + \max_v \lambda(v)/3⌉$
> where `tree(G)` is the number of vertices in a largest induced tree,
> `ecc_avg(G)` is the average eccentricity of `G`, and
> `max_v l(v) = max_v indepNeighborsCard G v` is the maximum over all vertices of
> the independence number of the neighbourhood.

```lean
theorem conjecture72 (G : SimpleGraph α) (h : G.Connected) :
    let maxL := (Finset.univ.image (fun v => indepNeighborsCard G v)).max' (by simp)
    ⌈averageEccentricity G + (maxL : ℝ) / 3⌉ ≤ (largestInducedTreeSize G : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture72.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
