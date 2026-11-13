---
declaration: theorem
origin: cited
lean: Erdos353.erdos_353, Erdos353.erdos_353.variants.isosceles_triangle, Erdos353.erdos_353.variants.right_angled_triangle, Erdos353.erdos_353.variants.cyclic_quadrilateral, Erdos353.erdos_353.variants.congruent_sides
statement: formalized
---

# Erdős Problem 353

> *References:*
> - [erdosproblems.com/353](https://www.erdosproblems.com/353)
> - [Er83d] Erdős, Paul, *Some combinatorial, geometric and set theoretic problems in measure
>   theory*. Measure Theory, Oberwolfach 1983 (1984), 321-327.
> - [Ko23] Kovač, V., *Coloring and density theorems for configurations of a given volume*.
>   arXiv:2309.09973 (2023).
> - [KoPr24] Kovač, V. and B. Predojević, *Polygons of unit area with vertices in sets of infinite
>   planar measure*. arXiv:2412.11725 (2024).
> - [Ko25] J. Koizumi, *Isosceles trapezoids of unit area with vertices in sets of infinite planar
>   measure*. arXiv:2501.01914 (2025).

*Quoted from [FormalConjectures/ErdosProblems/353.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/353](https://www.erdosproblems.com/353).

The file states 5 research or textbook statements: 5 solved.

## `Erdos353.erdos_353`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean).

> Let $A\subseteq \mathbb{R}^2$ be a measurable set with infinite measure. Must $A$ contain the
> vertices of an isosceles trapezoid of area $1$? What about an isosceles triangle, or a
> right-angled triangle, or a cyclic quadrilateral, or a convex polygon with congruent sides?
>
> Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
> contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
> triangle, all of area $1$.
>
> This statement formalizes the leading question, for isosceles trapezoids; the remaining
> configurations are given as variants below. The area of a polygon is taken to be the Lebesgue
> measure of the convex hull of its vertices.

```lean
theorem erdos_353 :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, ∃ d ∈ A,
        IsIsoscelesTrapezoid a b c d ∧
        volume (convexHull ℝ {a, b, c, d}) = 1
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/353.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean#L58).

## `Erdos353.erdos_353.variants.isosceles_triangle`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean).

> Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of an
> isosceles triangle of area $1$.
>
> Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
> contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
> triangle, all of area $1$.
>
> Note the area condition forces `a`, `b`, `c` to be affinely independent, so no separate
> non-degeneracy hypothesis is needed.

```lean
theorem erdos_353.variants.isosceles_triangle :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A,
        IsIsosceles a b c ∧
        volume (convexHull ℝ {a, b, c}) = 1
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/353.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean#L78).

## `Erdos353.erdos_353.variants.right_angled_triangle`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean).

> Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of a
> right-angled triangle of area $1$.
>
> Koizumi [Ko25] has resolved this question, proving that any set with infinite measure must
> contain the vertices of an isosceles trapezoid, an isosceles triangle, and a right-angled
> triangle, all of area $1$.
>
> Note the area condition forces `a`, `b`, `c` to be affinely independent, so no separate
> non-degeneracy hypothesis is needed.

```lean
theorem erdos_353.variants.right_angled_triangle :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A,
        IsRightAngled a b c ∧
        volume (convexHull ℝ {a, b, c}) = 1
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/353.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean#L98).

## `Erdos353.erdos_353.variants.cyclic_quadrilateral`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean).

> Every measurable $A\subseteq \mathbb{R}^2$ with infinite measure contains the vertices of a
> cyclic quadrilateral of area $1$.
>
> Kovač and Predojević [KoPr24] have proved that this is true for cyclic quadrilaterals - that
> is, every set with infinite measure contains four distinct points on a circle such that the
> quadrilateral determined by these four points has area $1$. The quadrilateral determined by
> four distinct concyclic points is their convex hull.

```lean
theorem erdos_353.variants.cyclic_quadrilateral :
    ∀ A : Set ℝ², MeasurableSet A → volume A = ⊤ →
      ∃ Q : Set ℝ², Q ⊆ A ∧ Q.ncard = 4 ∧ Cospherical Q ∧
        volume (convexHull ℝ Q) = 1
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/353.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean#L116).

## `Erdos353.erdos_353.variants.congruent_sides`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/353/Erdos353.lean).

> The answer is negative for convex polygons with congruent sides: Kovač and Predojević
> [KoPr24] prove that there exists a set of infinite measure such that every convex polygon
> with congruent sides and all vertices in the set has area $<1$.

```lean
theorem erdos_353.variants.congruent_sides :
    ∃ A : Set ℝ², MeasurableSet A ∧ volume A = ⊤ ∧
      ∀ (n : ℕ) (v : Fin (n + 3) → ℝ²),
        IsCcwConvexPolygon v → (∀ i, v i ∈ A) →
        (∀ i, dist (v i) (v (i + 1)) = dist (v 0) (v 1)) →
        volume (convexHull ℝ (Set.range v)) < 1
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/353.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean#L129).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/353.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/353.lean)
- [erdosproblems.com/353](https://www.erdosproblems.com/353)
