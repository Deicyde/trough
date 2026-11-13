---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture316.conjecture316
statement: formalized
---

# Written on the Wall II - Conjecture 316

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture316.conjecture316`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/wowii-graph-conjecture-316-lean/blob/3335e07151bc43e86d5c104dd30fee3596f06410/GraphConjecture316.lean](https://github.com/KitaKen1/wowii-graph-conjecture-316-lean/blob/3335e07151bc43e86d5c104dd30fee3596f06410/GraphConjecture316.lean).

> WOWII [Conjecture 316](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> Let `G` be a simple connected graph and let `P` denote the set of pendant vertices
> (vertices of degree 1). If `|P| ≥ deg_avg(Gᶜ)`, then `G` is well totally dominated,
> where `deg_avg(Gᶜ)` is the average degree of the complement of `G`.
>
> **Proof sketch.** In the trivial cases (`P = ∅`, or at most `2` vertices) `G` is complete,
> and complete graphs are well totally dominated. Otherwise the set `C` of non-pendant
> vertices satisfies `|C| ≤ 3` and is a clique of `G`, and a case split on the set `Q ⊆ C`
> of neighbours of pendant vertices shows that `G` is well totally dominated.

```lean
theorem conjecture316 (G : SimpleGraph α) [DecidableRel G.Adj] (hG : G.Connected)
    (h : (averageDegree Gᶜ : ℚ) ≤ (pendantVertices G).card) :
    IsWellTotallyDominated G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture316.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
