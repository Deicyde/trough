---
declaration: theorem
origin: cited
lean: Erdos1121.erdos_1121, Erdos1121.erdos_1121.variants.higher_dimension
statement: formalized
---

# Erdős Problem 1121

> *References:*
> - [erdosproblems.com/1121](https://www.erdosproblems.com/1121)
> - [BeLi16] Bezdek, Károly and Litvak, Alexander E., *Packing convex bodies by cylinders*.
>   Discrete Comput. Geom. (2016), 725-738.
> - [GoGo45] Goodman, A. W. and Goodman, R. E., *A circle covering theorem*. Amer. Math. Monthly
>   (1945), 494-498.
> - [Ha47] Hadwiger, H., *Nonseparable convex systems*. Amer. Math. Monthly (1947), 583-585.

*Quoted from [FormalConjectures/ErdosProblems/1121.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1121.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1121](https://www.erdosproblems.com/1121).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1121.erdos_1121`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1121.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1121.lean).

> If $C_1,\ldots,C_n$ are circles in $\mathbb{R}^2$ with radii $r_1,\ldots,r_n$ such that no line
> disjoint from all the circles divides them into two non-empty sets then the circles can be
> covered by a circle of radius $r=\sum r_i$.
>
> This is true, and was proved by Goodman and Goodman [GoGo45] (whose proof also generalises to
> higher dimensions). A generalisation to convex bodies was proved by Hadwiger [Ha47].
>
> An alternative proof is given by Bezdek and Litvak [BeLi16].

```lean
theorem erdos_1121 {n : ℕ} (c : Fin n → ℝ²) (r : Fin n → ℝ) (hr : ∀ i, 0 < r i)
    (hsep : ∀ (v : ℝ²) (t : ℝ), v ≠ 0 →
      (∀ i, ∀ p ∈ Metric.closedBall (c i) (r i), inner ℝ v p ≠ t) →
      (∀ i, inner ℝ v (c i) < t) ∨ (∀ i, t < inner ℝ v (c i))) :
    ∃ z : ℝ², (⋃ i, Metric.closedBall (c i) (r i)) ⊆ Metric.closedBall z (∑ i, r i)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1121.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1121.lean#L50).

## `Erdos1121.erdos_1121.variants.higher_dimension`

Solved: stated here without proof.

> The proof of Goodman and Goodman [GoGo45] also generalises to higher dimensions: if
> $B_1,\ldots,B_n$ are balls in $\mathbb{R}^d$ with radii $r_1,\ldots,r_n$ such that no hyperplane
> disjoint from all the balls divides them into two non-empty sets then the balls can be covered by
> a ball of radius $r=\sum r_i$.

```lean
theorem erdos_1121.variants.higher_dimension {d n : ℕ} (c : Fin n → EuclideanSpace ℝ (Fin d))
    (r : Fin n → ℝ) (hr : ∀ i, 0 < r i)
    (hsep : ∀ (v : EuclideanSpace ℝ (Fin d)) (t : ℝ), v ≠ 0 →
      (∀ i, ∀ p ∈ Metric.closedBall (c i) (r i), inner ℝ v p ≠ t) →
      (∀ i, inner ℝ v (c i) < t) ∨ (∀ i, t < inner ℝ v (c i))) :
    ∃ z : EuclideanSpace ℝ (Fin d),
      (⋃ i, Metric.closedBall (c i) (r i)) ⊆ Metric.closedBall z (∑ i, r i)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1121.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1121.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1121.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1121.lean)
- [erdosproblems.com/1121](https://www.erdosproblems.com/1121)
