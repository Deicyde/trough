---
declaration: theorem
origin: cited
lean: WrittenOnTheWallII.GraphConjecture36.conjecture36
statement: formalized
proof: formalized
---

# Written on the Wall II - Conjecture 36

> The conjecture is false. The counterexample below has a subdivided triangle on
> vertices `0`, `1`, `9`; vertices `7`, `8` adjacent to all three triangle
> vertices; and leaves `3`, `2` attached to `7`, `8`, respectively. It has radius
> three, one diametrical pair, and largest induced-path order five.
>
> *Reference:*
> [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)

*Quoted from [FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `WrittenOnTheWallII.GraphConjecture36.conjecture36`

Proved here.

> WOWII [Conjecture 36](http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html#conj36):
>
> For every finite simple connected graph $G$,
> $\operatorname{path}(G) \ge 2 \cdot \operatorname{rad}(G) / \operatorname{dp}(G)$,
> where $\operatorname{path}(G)$ is the number of vertices in a largest induced path,
> $\operatorname{rad}(G)$ is the radius of $G$, and $\operatorname{dp}(G)$ is the number
> of *diametrical pairs* of $G$ — that is, the number of pairs of vertices at distance
> $\operatorname{diam}(G)$.
>
> Disproved by Waller in Oct 2003 (counterexample: path number 5, radius 3, dp 1).

```lean
theorem conjecture36 :
    ¬ ∀ {α : Type} [Fintype α] [DecidableEq α] [Nontrivial α],
      ∀ (G : SimpleGraph α) [DecidableRel G.Adj] (_ : G.Connected) (_ : 0 < dp G),
        (2 * G.radius.toNat : ℝ) / (dp G : ℝ) ≤ (path G : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/WrittenOnTheWallII/GraphConjecture36.lean)
- [E. DeLaVina, Written on the Wall II, Conjectures of Graffiti.pc](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/)
