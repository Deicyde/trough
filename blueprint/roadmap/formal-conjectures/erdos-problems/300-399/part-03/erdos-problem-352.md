---
declaration: theorem
origin: cited
lean: Erdos352.erdos_352
statement: formalized
---

# Erdős Problem 352

> *Reference:* [erdosproblems.com/352](https://www.erdosproblems.com/352)

*Quoted from [FormalConjectures/ErdosProblems/352.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/352.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/352](https://www.erdosproblems.com/352).

The file states 1 research or textbook statement: 1 open.

## `Erdos352.erdos_352`

Open: stated without proof.

> Is there some $c > 0$ such that every measurable $A \subseteq \mathbb{R}^2$ of measure $\geq c$
>  contains the vertices of a triangle of area 1?

```lean
theorem erdos_352 :
    ∃ c > (0: ℝ), ∀ A : Set ℝ², MeasurableSet A → ℙ A ≥ c.toEReal
       → (∃ t : Affine.Triangle ℝ ℝ²,
           (∀ p : Fin 3, t.points p ∈ A) ∧
           EuclideanGeometry.triangle_area (t.points 0) (t.points 1) (t.points 2) = 1)
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/352.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/352.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/352.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/352.lean)
- [erdosproblems.com/352](https://www.erdosproblems.com/352)
