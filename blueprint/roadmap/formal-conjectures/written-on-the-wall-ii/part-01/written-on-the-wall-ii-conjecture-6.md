---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture6.conjecture6
statement: formalized
---

# Written on the Wall II - Conjecture 6

> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `WrittenOnTheWallII.GraphConjecture6.conjecture6`

Solved: stated here without proof.

> WOWII [Conjecture 6](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
>
> For a connected graph `G` we have
> `Ls(G) ≥ 1 + n(G) - m(G) - a(G)` where `a(G)` is defined via independent sets.

```lean
theorem conjecture6 (G : SimpleGraph α) [DecidableRel G.Adj] (h_conn : G.Connected) :
    1 + (Fintype.card α : ℝ) - matchingNumber G - α(G) ≤ Ls G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/WrittenOnTheWallII/GraphConjecture6.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
