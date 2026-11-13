---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture4.conjecture4
statement: formalized
---

# Written on the Wall II - Conjecture 4

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture4.conjecture4`

Solved: stated here without proof.

> WOWII [Conjecture 4](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> If `G` is a connected graph then the maximum number of leaves over all spanning
> trees satisfies `Ls(G) ≥ NG(G) - 1` where `NG(G)` is the minimal neighbourhood
> size of a non-edge of `G`.

```lean
theorem conjecture4 (G : SimpleGraph α) [DecidableRel G.Adj] [Nontrivial α] (h_conn : G.Connected) :
    NG G - 1 ≤ Ls G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture4.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
