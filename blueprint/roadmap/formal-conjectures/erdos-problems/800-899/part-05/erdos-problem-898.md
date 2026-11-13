---
declaration: theorem
origin: cited
lean: Erdos898.erdos_898
statement: formalized
---

# Erdős Problem 898

> *References:*
> - [erdosproblems.com/898](https://www.erdosproblems.com/898)
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59--79.
> - [Wikipedia](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Mordell_inequality)

*Quoted from [FormalConjectures/ErdosProblems/898.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/898.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/898](https://www.erdosproblems.com/898).

The file states 1 research or textbook statement: 1 solved.

## `Erdos898.erdos_898`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos898.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos898.lean).

> If $A,B,C\in \mathbb{R}^2$ form a triangle and $P$ is a point in the interior then, if $N$ is
> where the perpendicular from $P$ to $AB$ meets the triangle, and similarly for $M$ and $L$,
>
> $$
> \overline{PA}+\overline{PB}+\overline{PC}\geq 2(\overline{PM}+\overline{PN}+\overline{PL}).
> $$
>
> Conjectured by Erdős in 1932 (according to [Er82e]) and proved by Mordell soon afterwards, now
> known as the Erdős-Mordell inequality.

```lean
theorem erdos_898 (A B C P L M N : ℝ²) (hABC : AffineIndependent ℝ ![A, B, C])
    (hP : P ∈ interior (convexHull ℝ ({A, B, C} : Set ℝ²)))
    (hN : N ∈ line[ℝ, A, B]) (hPN : line[ℝ, P, N].direction ⟂ line[ℝ, A, B].direction)
    (hM : M ∈ line[ℝ, B, C]) (hPM : line[ℝ, P, M].direction ⟂ line[ℝ, B, C].direction)
    (hL : L ∈ line[ℝ, C, A]) (hPL : line[ℝ, P, L].direction ⟂ line[ℝ, C, A].direction) :
    dist P A + dist P B + dist P C ≥ 2 * (dist P M + dist P N + dist P L)
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/898.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/898.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/898.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/898.lean)
- [erdosproblems.com/898](https://www.erdosproblems.com/898)
